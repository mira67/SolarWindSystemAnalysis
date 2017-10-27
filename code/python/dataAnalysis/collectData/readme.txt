关于环境配置：

需要 pip install azure 
azure 版本需高于1.0， 如果版本低于1.0，需重先卸载再安装。
查看azure 版本 pip freeze
详情请看：https://github.com/Azure/azure-storage-python


关于文件：
AzureTableHelper.py： 为查询主文件，封装了登录方法，以及table的查询码。
mathtool.py： 封装了一些计算方法，AzureTableHelper.py 会调用该模块中计算时间的方法，该模块内容不用动。
taskscript_config.py： 封装登录信息，内容不用动，AzureTableHelper.py 会调用。
deviceMode.csv: 设备型号表
deviceType.csv：设备类型表
station.csv：光伏电站表
taskfiles:为一些设备文件



关于AzureTableHelper.py：

ReadAzureTable 类中的方法 readData，为查询table数据的方法。
参数依次为：设备编号，设备类型编号，开始时间，结束时间。已经附有模板。
查询只会查询某一个设备的数据，若要查询一个设备类型下所有设备的数据，需要写一个循环，进行查询。
每一个设备类型下有多少个设备，并且设备编号是多少，可以参考：http://p.cnecloud.cn/  账号：raoyb, 密码：rao@2017
入口：管理器 -- 设备信息 -- 筛选电站名称，设备名称，设备型号， 可查看该设备型号下的设备编号。


关于table 查询语法：

在readData 方法中，filter_string 为查询语法，没有关键字，只需列名筛选即可，等于--eq 大于--gt 小于 --lt 大于等于--ge 小于等于--le
目前表中结构为一个partitionKey 为一个设备， 例如 partitionKey eq 2，表示你需要查找设备编号是2的数据。


关于table中，列名的意思：

partitionKey : 一般为一个设备一个key，比如平原电站的汇流箱10，partitionKey 为10
RowKey: 为时间，在mathtool.py文件中，已经做过处理了
c: 设备编号，一般与partitionKey 的值相同
m: 设备型号编码，命名方式为 电站编码 + M + 设备编码 + M + 型号编码， 都可以在csv文件中查到。
其他列名，请参考：http://p.cnecloud.cn/ 账号：raoyb, 密码：rao@2017
入口：管理器 -- 设备型号点表， 筛选条件后，可查到意思。


关于main.py:
代码亲测可以用，文件格式为"设备名称_日期" 可以自己定义一下。
需要自己先选择某一个电站，选择某一个电站是修改stationDevicedevice变量，
例如平原电站，就写成stationDevicedevice = s350.allDevice， 乃东为  stationDevicedevice = s340.allDevice
需自己定义的变量有： path 路径，deviceType 设备类型代码 int 类型， 可以在devicetypelist 中添加设备类型的一个列表。
在datelist 中添加一下日期列表，每个元素为一个长度为二的列表，索引0为开始时间，索引1为结束时间，从而可以循环一直生成数据。
循环代码已经在主函数下注释了。

如有任何问题敬请联系：饶毅彬 raoyb@cnegroup.com