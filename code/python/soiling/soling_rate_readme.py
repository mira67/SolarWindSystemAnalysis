# Function to compute soiling rate
# change commented part to transfer to CPR
# Qi Liu


def avgSoilingRate(df):
    # Step 1: 读入一年或更长时间对应逆变器的清洗记录和CPR
    # df 包含CPR信息
    clean = pd.read_csv(qxjl)
    clean = clean[clean.nbqno == 'S01-NBA']
    cleanDates = clean['qxdate'].tolist()
    df = df.fillna(method='ffill')
    soilingDict = {}
    gpi = []
    # remove extreme outliers

    # Step 2: 简单数据清洗，根据CPR实际值的分布，去除outliers
    # 此处使用的 Q1-1.5*IQR， Q3+1.5*IQR的标准
    # 忽略slope相关的数据，替换为CPR
    upper = np.percentile(df.Pr, 75)  # can get based on different temperatures
    slope = df.Pr / upper  # df.InvCPR  #
    df['slope'] = removeOutliers(slope, 1.5)

    # Step 3: 抓取清洗事件中间的CPR序列，计算soiling rate
    for idx, dt in enumerate(cleanDates[:-1]):
        # Step 3.1: 提取清洗事件区间的CPR List
        data = df[df.data_date > dt]
        data = data[data.data_date < cleanDates[idx + 1]]
        rgDate = [dt, cleanDates[idx + 1]]
        soilingDict[str(rgDate)] = data.slope.tolist()
        ndays = len(data.slope.tolist())
        dn = np.arange(ndays)
        plt.figure(1)

        # Step 3.2: 仅对清洗区间大于1天的CPR序列进行soiling rate计算
        if ndays > 1:
            # 计算soiling rate，方法：线性回归 robust regression
            lm, slope = linearModel(dn.reshape(-1, 1),
                                    data.slope.values.reshape(-1, 1), 'theil')
            if slope < 0:
                gpi.append(slope * 100)
                # plot
                plt.plot(dn, data.slope, '.', label=str(rgDate))
                p_pred = lm.predict(dn.reshape(-1, 1))
                plt.plot(dn, p_pred, linewidth=2, label=str(rgDate) + 'regression')
    # plt.legend()
    plt.xlabel('# of Days after Clean Event')
    plt.ylabel('Normalized G-PI to Median')
    plt.figure(2)
    plt.hist(gpi, label='Distribution of Soiling Rates', bins=20)
    plt.xlabel('Soiling Rate (%)/ Day')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

    # 求平均soiling rate，此处使用median值，减少outlier影响
    print(median(gpi), gpi)

    return soilingDict
