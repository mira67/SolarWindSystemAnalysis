#-*- coding: UTF-8 -*-

# 读取气象站数据
# 读取逆变器数据
# 读取汇流箱数据
# 计算天数据
DATETIME_FMT = '%Y-%m-%d %H:%M' 


deviceModePointConfig=[
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Open_V_Num2",
    "DeviceModePointName": "2号开路电压瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Open_V_Num2",
    "DeviceModePointName": "2号开路电压瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Open_V_Num2",
    "DeviceModePointName": "2号开路电压瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Open_V_Num2",
    "DeviceModePointName": "2号开路电压瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num3",
    "DeviceModePointName": "3号短路电流瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num3",
    "DeviceModePointName": "3号短路电流瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num3",
    "DeviceModePointName": "3号短路电流瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num3",
    "DeviceModePointName": "3号短路电流瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "水平总辐射分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "水平总辐射分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "水平总辐射分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "水平总辐射分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "斜面总辐射分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "斜面总辐射分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "斜面总辐射分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "斜面总辐射分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX021",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Dir_Min_Avg",
    "DeviceModePointName": "风向分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX021",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Dir_Min_Avg",
    "DeviceModePointName": "风向分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX021",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Dir_Min_Avg",
    "DeviceModePointName": "风向分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX021",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Dir_Min_Avg",
    "DeviceModePointName": "风向分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX022",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp_Min_Avg",
    "DeviceModePointName": "空气温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX022",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp_Min_Avg",
    "DeviceModePointName": "空气温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX022",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp_Min_Avg",
    "DeviceModePointName": "空气温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX022",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp_Min_Avg",
    "DeviceModePointName": "空气温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX023",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_Min_Avg",
    "DeviceModePointName": "1号背板温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX023",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_Min_Avg",
    "DeviceModePointName": "1号背板温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX023",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_Min_Avg",
    "DeviceModePointName": "1号背板温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX023",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_Min_Avg",
    "DeviceModePointName": "1号背板温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX024",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Min_Avg",
    "DeviceModePointName": "2号背板温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX024",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Min_Avg",
    "DeviceModePointName": "2号背板温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX024",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Min_Avg",
    "DeviceModePointName": "2号背板温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX024",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Min_Avg",
    "DeviceModePointName": "2号背板温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX025",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Min_Avg",
    "DeviceModePointName": "3号背板温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX025",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Min_Avg",
    "DeviceModePointName": "3号背板温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX025",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Min_Avg",
    "DeviceModePointName": "3号背板温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX025",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Min_Avg",
    "DeviceModePointName": "3号背板温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX026",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Min_Avg",
    "DeviceModePointName": "4号背板温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX026",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Min_Avg",
    "DeviceModePointName": "4号背板温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX026",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Min_Avg",
    "DeviceModePointName": "4号背板温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX026",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Min_Avg",
    "DeviceModePointName": "4号背板温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX027",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Hum_Min_Avg",
    "DeviceModePointName": "相对湿度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX027",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Hum_Min_Avg",
    "DeviceModePointName": "相对湿度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX027",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Hum_Min_Avg",
    "DeviceModePointName": "相对湿度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX027",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Hum_Min_Avg",
    "DeviceModePointName": "相对湿度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX028",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Air_Pres_Min_Avg",
    "DeviceModePointName": "大气压力分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX028",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Air_Pres_Min_Avg",
    "DeviceModePointName": "大气压力分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX028",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Air_Pres_Min_Avg",
    "DeviceModePointName": "大气压力分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX028",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Air_Pres_Min_Avg",
    "DeviceModePointName": "大气压力分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX029",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num1_Min_Avg",
    "DeviceModePointName": "1号短路电流分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX029",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num1_Min_Avg",
    "DeviceModePointName": "1号短路电流分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX029",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num1_Min_Avg",
    "DeviceModePointName": "1号短路电流分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX029",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num1_Min_Avg",
    "DeviceModePointName": "1号短路电流分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX030",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num2_Min_Avg",
    "DeviceModePointName": "2号开路电压分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX030",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num2_Min_Avg",
    "DeviceModePointName": "2号开路电压分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX030",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num2_Min_Avg",
    "DeviceModePointName": "2号开路电压分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX030",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num2_Min_Avg",
    "DeviceModePointName": "2号开路电压分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX031",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num3_Min_Avg",
    "DeviceModePointName": "3号短路电流分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX031",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num3_Min_Avg",
    "DeviceModePointName": "3号短路电流分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX031",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num3_Min_Avg",
    "DeviceModePointName": "3号短路电流分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX031",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num3_Min_Avg",
    "DeviceModePointName": "3号短路电流分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX032",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX032",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX032",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX032",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX033",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX033",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX033",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX033",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Hr_Avg",
    "DeviceModePointName": "水平总辐射小时平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Hr_Avg",
    "DeviceModePointName": "水平总辐射小时平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Hr_Avg",
    "DeviceModePointName": "水平总辐射小时平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Hr_Avg",
    "DeviceModePointName": "水平总辐射小时平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Hr_Avg",
    "DeviceModePointName": "斜面总辐射小时平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Hr_Avg",
    "DeviceModePointName": "斜面总辐射小时平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Hr_Avg",
    "DeviceModePointName": "斜面总辐射小时平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Hr_Avg",
    "DeviceModePointName": "斜面总辐射小时平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX036",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly_YstDay",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX036",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly_YstDay",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX036",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly_YstDay",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX036",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly_YstDay",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX037",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_YstDay",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX037",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_YstDay",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX037",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_YstDay",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX037",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_YstDay",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX038",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Spd_Dly_Avg",
    "DeviceModePointName": "风速天平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX038",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Spd_Dly_Avg",
    "DeviceModePointName": "风速天平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX038",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Spd_Dly_Avg",
    "DeviceModePointName": "风速天平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX038",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Spd_Dly_Avg",
    "DeviceModePointName": "风速天平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX039",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Avg",
    "DeviceModePointName": "空气温度天平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX039",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Avg",
    "DeviceModePointName": "空气温度天平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX039",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Avg",
    "DeviceModePointName": "空气温度天平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX039",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Avg",
    "DeviceModePointName": "空气温度天平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX040",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Mini",
    "DeviceModePointName": "空气温度天最小",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX040",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Mini",
    "DeviceModePointName": "空气温度天最小",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX040",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Mini",
    "DeviceModePointName": "空气温度天最小",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX040",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Mini",
    "DeviceModePointName": "空气温度天最小",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX041",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Maxm",
    "DeviceModePointName": "空气温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX041",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Maxm",
    "DeviceModePointName": "空气温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX041",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Maxm",
    "DeviceModePointName": "空气温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX041",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Maxm",
    "DeviceModePointName": "空气温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX042",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly_Maxm",
    "DeviceModePointName": "水平总辐射天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX042",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly_Maxm",
    "DeviceModePointName": "水平总辐射天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX042",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly_Maxm",
    "DeviceModePointName": "水平总辐射天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX042",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly_Maxm",
    "DeviceModePointName": "水平总辐射天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX043",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Maxm",
    "DeviceModePointName": "斜面总辐射天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX043",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Maxm",
    "DeviceModePointName": "斜面总辐射天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX043",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Maxm",
    "DeviceModePointName": "斜面总辐射天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX043",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Maxm",
    "DeviceModePointName": "斜面总辐射天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX044",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Spd_Dly_Maxm",
    "DeviceModePointName": "风速天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX044",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Spd_Dly_Maxm",
    "DeviceModePointName": "风速天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX044",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Spd_Dly_Maxm",
    "DeviceModePointName": "风速天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX044",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Wind_Spd_Dly_Maxm",
    "DeviceModePointName": "风速天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX045",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Air_Pres_Dly_Maxm",
    "DeviceModePointName": "大气压力天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX045",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Air_Pres_Dly_Maxm",
    "DeviceModePointName": "大气压力天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX045",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Air_Pres_Dly_Maxm",
    "DeviceModePointName": "大气压力天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX045",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Air_Pres_Dly_Maxm",
    "DeviceModePointName": "大气压力天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX046",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_Dly_Maxm",
    "DeviceModePointName": "1号背板温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX046",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_Dly_Maxm",
    "DeviceModePointName": "1号背板温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX046",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_Dly_Maxm",
    "DeviceModePointName": "1号背板温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX046",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_Dly_Maxm",
    "DeviceModePointName": "1号背板温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX047",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Dly_Maxm",
    "DeviceModePointName": "2号背板温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX047",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Dly_Maxm",
    "DeviceModePointName": "2号背板温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX047",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Dly_Maxm",
    "DeviceModePointName": "2号背板温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX047",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Dly_Maxm",
    "DeviceModePointName": "2号背板温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX048",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Dly_Maxm",
    "DeviceModePointName": "3号背板温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX048",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Dly_Maxm",
    "DeviceModePointName": "3号背板温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX048",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Dly_Maxm",
    "DeviceModePointName": "3号背板温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX048",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Dly_Maxm",
    "DeviceModePointName": "3号背板温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX049",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Dly_Maxm",
    "DeviceModePointName": "4号背板温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX049",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Dly_Maxm",
    "DeviceModePointName": "4号背板温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX049",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Dly_Maxm",
    "DeviceModePointName": "4号背板温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX049",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Dly_Maxm",
    "DeviceModePointName": "4号背板温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX050",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num1_Dly_Maxm",
    "DeviceModePointName": "1号短路电流天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX050",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num1_Dly_Maxm",
    "DeviceModePointName": "1号短路电流天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX050",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num1_Dly_Maxm",
    "DeviceModePointName": "1号短路电流天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX050",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num1_Dly_Maxm",
    "DeviceModePointName": "1号短路电流天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX051",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Open_V_Num2_Dly_Maxm",
    "DeviceModePointName": "2号开路电压天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX051",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Open_V_Num2_Dly_Maxm",
    "DeviceModePointName": "2号开路电压天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX051",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Open_V_Num2_Dly_Maxm",
    "DeviceModePointName": "2号开路电压天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX051",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Open_V_Num2_Dly_Maxm",
    "DeviceModePointName": "2号开路电压天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX052",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num3_Dly_Maxm",
    "DeviceModePointName": "3号短路电流天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX052",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num3_Dly_Maxm",
    "DeviceModePointName": "3号短路电流天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX052",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num3_Dly_Maxm",
    "DeviceModePointName": "3号短路电流天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX052",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num3_Dly_Maxm",
    "DeviceModePointName": "3号短路电流天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器日运行时间",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器日运行时间",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器日运行时间",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器日运行时间",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB038",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V1",
    "DeviceModePointName": " 直流电压1",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB038",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V1",
    "DeviceModePointName": " 直流电压1",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB038",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V1",
    "DeviceModePointName": " 直流电压1",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB038",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V1",
    "DeviceModePointName": " 直流电压1",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB039",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A1",
    "DeviceModePointName": " 直流电流1",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB039",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A1",
    "DeviceModePointName": " 直流电流1",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB039",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A1",
    "DeviceModePointName": " 直流电流1",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB039",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A1",
    "DeviceModePointName": " 直流电流1",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB040",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V2",
    "DeviceModePointName": " 直流电压2",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB040",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V2",
    "DeviceModePointName": " 直流电压2",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB040",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V2",
    "DeviceModePointName": " 直流电压2",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB040",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V2",
    "DeviceModePointName": " 直流电压2",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB041",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A2",
    "DeviceModePointName": " 直流电流2",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB041",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A2",
    "DeviceModePointName": " 直流电流2",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB041",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A2",
    "DeviceModePointName": " 直流电流2",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB041",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A2",
    "DeviceModePointName": " 直流电流2",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB042",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V3",
    "DeviceModePointName": " 直流电压3",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB042",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V3",
    "DeviceModePointName": " 直流电压3",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB042",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V3",
    "DeviceModePointName": " 直流电压3",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB042",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V3",
    "DeviceModePointName": " 直流电压3",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB043",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A3",
    "DeviceModePointName": " 直流电流3",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB043",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A3",
    "DeviceModePointName": " 直流电流3",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB043",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A3",
    "DeviceModePointName": " 直流电流3",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB043",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A3",
    "DeviceModePointName": " 直流电流3",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB044",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V4",
    "DeviceModePointName": " 直流电压4",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB044",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V4",
    "DeviceModePointName": " 直流电压4",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB044",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V4",
    "DeviceModePointName": " 直流电压4",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB044",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V4",
    "DeviceModePointName": " 直流电压4",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB045",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A4",
    "DeviceModePointName": " 直流电流4",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB045",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A4",
    "DeviceModePointName": " 直流电流4",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB045",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A4",
    "DeviceModePointName": " 直流电流4",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB045",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A4",
    "DeviceModePointName": " 直流电流4",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB050",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Act_W_Set",
    "DeviceModePointName": " 逆变器当前有功功率设定实际值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB050",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Act_W_Set",
    "DeviceModePointName": " 逆变器当前有功功率设定实际值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB050",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Act_W_Set",
    "DeviceModePointName": " 逆变器当前有功功率设定实际值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB050",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Act_W_Set",
    "DeviceModePointName": " 逆变器当前有功功率设定实际值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB051",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "React_W_Set",
    "DeviceModePointName": " 逆变器当前无功功率设定实际值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB051",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "React_W_Set",
    "DeviceModePointName": " 逆变器当前无功功率设定实际值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB051",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "React_W_Set",
    "DeviceModePointName": " 逆变器当前无功功率设定实际值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB051",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "React_W_Set",
    "DeviceModePointName": " 逆变器当前无功功率设定实际值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB052",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PF_Set",
    "DeviceModePointName": " 逆变器当前功率因数设定实际值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB052",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PF_Set",
    "DeviceModePointName": " 逆变器当前功率因数设定实际值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB052",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PF_Set",
    "DeviceModePointName": " 逆变器当前功率因数设定实际值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB052",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PF_Set",
    "DeviceModePointName": " 逆变器当前功率因数设定实际值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ001",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Tilted_Radi_Inst",
    "DeviceModePointName": "斜面辐射",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ001",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Tilted_Radi_Inst",
    "DeviceModePointName": "斜面辐射",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ001",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Tilted_Radi_Inst",
    "DeviceModePointName": "斜面辐射",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ001",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Tilted_Radi_Inst",
    "DeviceModePointName": "斜面辐射",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ003",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_W",
    "DeviceModePointName": "有功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ003",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_W",
    "DeviceModePointName": "有功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ003",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_W",
    "DeviceModePointName": "有功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ003",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_W",
    "DeviceModePointName": "有功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ002",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Tilted_Radi_TotDly",
    "DeviceModePointName": "斜面辐射累计值",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ002",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Tilted_Radi_TotDly",
    "DeviceModePointName": "斜面辐射累计值",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ002",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Tilted_Radi_TotDly",
    "DeviceModePointName": "斜面辐射累计值",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ004",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_TotWhDly",
    "DeviceModePointName": "日累计电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ004",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_TotWhDly",
    "DeviceModePointName": "日累计电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ004",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_TotWhDly",
    "DeviceModePointName": "日累计电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ005",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_TotWhMly",
    "DeviceModePointName": "月累计电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ005",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_TotWhMly",
    "DeviceModePointName": "月累计电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ005",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_TotWhMly",
    "DeviceModePointName": "月累计电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ006",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_TotWhYly",
    "DeviceModePointName": "年累计电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ006",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_TotWhYly",
    "DeviceModePointName": "年累计电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ006",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_TotWhYly",
    "DeviceModePointName": "年累计电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ007",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_TotWh",
    "DeviceModePointName": "总发出有功电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ007",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_TotWh",
    "DeviceModePointName": "总发出有功电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ007",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_TotWh",
    "DeviceModePointName": "总发出有功电量",
    "CalcMethod": "Dif",
    "Divation": 600
  }
]

allDevice=[
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 1,
    "DeviceFullCode": "392M202M5M1",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 2,
    "DeviceFullCode": "392M202M5M2",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 3,
    "DeviceFullCode": "392M202M5M3",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 4,
    "DeviceFullCode": "392M202M5M4",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 5,
    "DeviceFullCode": "392M202M5M5",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 6,
    "DeviceFullCode": "392M202M5M6",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 7,
    "DeviceFullCode": "392M202M5M7",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 8,
    "DeviceFullCode": "392M202M5M8",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 9,
    "DeviceFullCode": "392M202M5M9",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 10,
    "DeviceFullCode": "392M202M5M10",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 11,
    "DeviceFullCode": "392M202M5M11",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 12,
    "DeviceFullCode": "392M202M5M12",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 13,
    "DeviceFullCode": "392M202M5M13",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 14,
    "DeviceFullCode": "392M202M5M14",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 15,
    "DeviceFullCode": "392M202M5M15",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 16,
    "DeviceFullCode": "392M202M5M16",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 17,
    "DeviceFullCode": "392M202M5M17",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 18,
    "DeviceFullCode": "392M202M5M18",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 19,
    "DeviceFullCode": "392M202M5M19",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 20,
    "DeviceFullCode": "392M202M5M20",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 21,
    "DeviceFullCode": "392M202M5M21",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 22,
    "DeviceFullCode": "392M202M5M22",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 23,
    "DeviceFullCode": "392M202M5M23",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 24,
    "DeviceFullCode": "392M202M5M24",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 25,
    "DeviceFullCode": "392M202M5M25",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 26,
    "DeviceFullCode": "392M202M5M26",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 27,
    "DeviceFullCode": "392M202M5M27",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 28,
    "DeviceFullCode": "392M202M5M28",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 29,
    "DeviceFullCode": "392M202M5M29",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 30,
    "DeviceFullCode": "392M202M5M30",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 31,
    "DeviceFullCode": "392M202M5M31",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 251.1000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 32,
    "DeviceFullCode": "392M202M5M32",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 245.5200
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 33,
    "DeviceFullCode": "392M202M5M33",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 223.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 34,
    "DeviceFullCode": "392M202M5M34",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 35,
    "DeviceFullCode": "392M202M5M35",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 36,
    "DeviceFullCode": "392M202M5M36",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 37,
    "DeviceFullCode": "392M202M5M37",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 38,
    "DeviceFullCode": "392M202M5M38",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 39,
    "DeviceFullCode": "392M202M5M39",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 40,
    "DeviceFullCode": "392M202M5M40",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 239.9400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 41,
    "DeviceFullCode": "392M202M5M41",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 42,
    "DeviceFullCode": "392M202M5M42",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 245.5200
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 43,
    "DeviceFullCode": "392M202M5M43",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 44,
    "DeviceFullCode": "392M202M5M44",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 251.1000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 45,
    "DeviceFullCode": "392M202M5M45",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 46,
    "DeviceFullCode": "392M202M5M46",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 234.3600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 47,
    "DeviceFullCode": "392M202M5M47",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 48,
    "DeviceFullCode": "392M202M5M48",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 49,
    "DeviceFullCode": "392M202M5M49",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 50,
    "DeviceFullCode": "392M202M5M50",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 51,
    "DeviceFullCode": "392M202M5M51",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 251.1000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 52,
    "DeviceFullCode": "392M202M5M52",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 53,
    "DeviceFullCode": "392M202M5M53",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 54,
    "DeviceFullCode": "392M202M5M54",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 251.1000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 55,
    "DeviceFullCode": "392M202M5M55",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 56,
    "DeviceFullCode": "392M202M5M56",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 251.1000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 57,
    "DeviceFullCode": "392M202M5M57",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 58,
    "DeviceFullCode": "392M202M5M58",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 59,
    "DeviceFullCode": "392M202M5M59",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 60,
    "DeviceFullCode": "392M202M5M60",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 61,
    "DeviceFullCode": "392M202M5M61",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 247.5000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 62,
    "DeviceFullCode": "392M202M5M62",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 63,
    "DeviceFullCode": "392M202M5M63",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 64,
    "DeviceFullCode": "392M202M5M64",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 65,
    "DeviceFullCode": "392M202M5M65",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 245.5200
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 66,
    "DeviceFullCode": "392M202M5M66",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 67,
    "DeviceFullCode": "392M202M5M67",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 68,
    "DeviceFullCode": "392M202M5M68",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 69,
    "DeviceFullCode": "392M202M5M69",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 245.5200
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 70,
    "DeviceFullCode": "392M202M5M70",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 71,
    "DeviceFullCode": "392M202M5M71",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 72,
    "DeviceFullCode": "392M202M5M72",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 73,
    "DeviceFullCode": "392M202M5M73",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 239.9400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 74,
    "DeviceFullCode": "392M202M5M74",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 75,
    "DeviceFullCode": "392M202M5M75",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 76,
    "DeviceFullCode": "392M202M5M76",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 77,
    "DeviceFullCode": "392M202M5M77",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 78,
    "DeviceFullCode": "392M202M5M78",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 79,
    "DeviceFullCode": "392M202M5M79",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 251.1000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 80,
    "DeviceFullCode": "392M202M5M80",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 81,
    "DeviceFullCode": "392M202M5M81",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 82,
    "DeviceFullCode": "392M202M5M82",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 83,
    "DeviceFullCode": "392M202M5M83",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 251.1000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 84,
    "DeviceFullCode": "392M202M5M84",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 85,
    "DeviceFullCode": "392M202M5M85",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 86,
    "DeviceFullCode": "392M202M5M86",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 87,
    "DeviceFullCode": "392M202M5M87",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 88,
    "DeviceFullCode": "392M202M5M88",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 228.7800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 89,
    "DeviceFullCode": "392M202M5M89",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 90,
    "DeviceFullCode": "392M202M5M90",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 251.1000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 91,
    "DeviceFullCode": "392M202M5M91",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 92,
    "DeviceFullCode": "392M202M5M92",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 93,
    "DeviceFullCode": "392M202M5M93",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 94,
    "DeviceFullCode": "392M202M5M94",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 251.1000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 95,
    "DeviceFullCode": "392M202M5M95",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 251.1000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 96,
    "DeviceFullCode": "392M202M5M96",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 97,
    "DeviceFullCode": "392M202M5M97",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 239.9400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 98,
    "DeviceFullCode": "392M202M5M98",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 99,
    "DeviceFullCode": "392M202M5M99",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 100,
    "DeviceFullCode": "392M202M5M100",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 101,
    "DeviceFullCode": "392M202M5M101",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 102,
    "DeviceFullCode": "392M202M5M102",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 239.9400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 103,
    "DeviceFullCode": "392M202M5M103",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 104,
    "DeviceFullCode": "392M202M5M104",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 105,
    "DeviceFullCode": "392M202M5M105",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 245.5200
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 106,
    "DeviceFullCode": "392M202M5M106",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 107,
    "DeviceFullCode": "392M202M5M107",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 108,
    "DeviceFullCode": "392M202M5M108",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 109,
    "DeviceFullCode": "392M202M5M109",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 110,
    "DeviceFullCode": "392M202M5M110",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 111,
    "DeviceFullCode": "392M202M5M111",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 251.1000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 112,
    "DeviceFullCode": "392M202M5M112",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 239.9400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 113,
    "DeviceFullCode": "392M202M5M113",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 239.9400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 114,
    "DeviceFullCode": "392M202M5M114",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 267.8400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 115,
    "DeviceFullCode": "392M202M5M115",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 116,
    "DeviceFullCode": "392M202M5M116",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 117,
    "DeviceFullCode": "392M202M5M117",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 118,
    "DeviceFullCode": "392M202M5M118",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 256.6800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 119,
    "DeviceFullCode": "392M202M5M119",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 251.1000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 5,
    "DeviceCode": 120,
    "DeviceFullCode": "392M202M5M120",
    "DeviceModeFullCode": "392M202M5",
    "PDeviceFullCode": None,
    "Capacity": 262.2600
  },
  {
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceCode": 1,
    "DeviceFullCode": "392M203M5M1",
    "DeviceModeFullCode": "392M203M5",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceCode": 2,
    "DeviceFullCode": "392M203M2M2",
    "DeviceModeFullCode": "392M203M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 1,
    "DeviceFullCode": "392M206M1M1",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 2,
    "DeviceFullCode": "392M206M1M2",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 3,
    "DeviceFullCode": "392M206M1M3",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 4,
    "DeviceFullCode": "392M206M1M4",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 5,
    "DeviceFullCode": "392M206M1M5",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 6,
    "DeviceFullCode": "392M206M1M6",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 7,
    "DeviceFullCode": "392M206M1M7",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 8,
    "DeviceFullCode": "392M206M1M8",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 9,
    "DeviceFullCode": "392M206M1M9",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 10,
    "DeviceFullCode": "392M206M1M10",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 11,
    "DeviceFullCode": "392M206M1M11",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 12,
    "DeviceFullCode": "392M206M1M12",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 13,
    "DeviceFullCode": "392M206M1M13",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 14,
    "DeviceFullCode": "392M206M1M14",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 15,
    "DeviceFullCode": "392M206M1M15",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 16,
    "DeviceFullCode": "392M206M1M16",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 17,
    "DeviceFullCode": "392M206M1M17",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 22.3200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 18,
    "DeviceFullCode": "392M206M1M18",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 19,
    "DeviceFullCode": "392M206M1M19",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 20,
    "DeviceFullCode": "392M206M1M20",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 21,
    "DeviceFullCode": "392M206M1M21",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 22,
    "DeviceFullCode": "392M206M1M22",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 23,
    "DeviceFullCode": "392M206M1M23",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 24,
    "DeviceFullCode": "392M206M1M24",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 25,
    "DeviceFullCode": "392M206M1M25",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 26,
    "DeviceFullCode": "392M206M1M26",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 27,
    "DeviceFullCode": "392M206M1M27",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 28,
    "DeviceFullCode": "392M206M1M28",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 29,
    "DeviceFullCode": "392M206M1M29",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 30,
    "DeviceFullCode": "392M206M1M30",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 31,
    "DeviceFullCode": "392M206M1M31",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 32,
    "DeviceFullCode": "392M206M1M32",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 33,
    "DeviceFullCode": "392M206M1M33",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 34,
    "DeviceFullCode": "392M206M1M34",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 22.3200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 35,
    "DeviceFullCode": "392M206M1M35",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 36,
    "DeviceFullCode": "392M206M1M36",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 37,
    "DeviceFullCode": "392M206M1M37",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 38,
    "DeviceFullCode": "392M206M1M38",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 39,
    "DeviceFullCode": "392M206M1M39",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 40,
    "DeviceFullCode": "392M206M1M40",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 41,
    "DeviceFullCode": "392M206M1M41",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 42,
    "DeviceFullCode": "392M206M1M42",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 43,
    "DeviceFullCode": "392M206M1M43",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 44,
    "DeviceFullCode": "392M206M1M44",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 45,
    "DeviceFullCode": "392M206M1M45",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 46,
    "DeviceFullCode": "392M206M1M46",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 47,
    "DeviceFullCode": "392M206M1M47",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 48,
    "DeviceFullCode": "392M206M1M48",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 49,
    "DeviceFullCode": "392M206M1M49",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 50,
    "DeviceFullCode": "392M206M1M50",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 51,
    "DeviceFullCode": "392M206M1M51",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 22.3200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 52,
    "DeviceFullCode": "392M206M1M52",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 53,
    "DeviceFullCode": "392M206M1M53",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 54,
    "DeviceFullCode": "392M206M1M54",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 55,
    "DeviceFullCode": "392M206M1M55",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 56,
    "DeviceFullCode": "392M206M1M56",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 57,
    "DeviceFullCode": "392M206M1M57",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 58,
    "DeviceFullCode": "392M206M1M58",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 59,
    "DeviceFullCode": "392M206M1M59",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 60,
    "DeviceFullCode": "392M206M1M60",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 61,
    "DeviceFullCode": "392M206M1M61",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 62,
    "DeviceFullCode": "392M206M1M62",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 63,
    "DeviceFullCode": "392M206M1M63",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 64,
    "DeviceFullCode": "392M206M1M64",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 65,
    "DeviceFullCode": "392M206M1M65",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 66,
    "DeviceFullCode": "392M206M1M66",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 22.3200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 67,
    "DeviceFullCode": "392M206M1M67",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 68,
    "DeviceFullCode": "392M206M1M68",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 69,
    "DeviceFullCode": "392M206M1M69",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 70,
    "DeviceFullCode": "392M206M1M70",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 71,
    "DeviceFullCode": "392M206M1M71",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 72,
    "DeviceFullCode": "392M206M1M72",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 73,
    "DeviceFullCode": "392M206M1M73",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 74,
    "DeviceFullCode": "392M206M1M74",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 75,
    "DeviceFullCode": "392M206M1M75",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 76,
    "DeviceFullCode": "392M206M1M76",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 77,
    "DeviceFullCode": "392M206M1M77",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 78,
    "DeviceFullCode": "392M206M1M78",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 79,
    "DeviceFullCode": "392M206M1M79",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 80,
    "DeviceFullCode": "392M206M1M80",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 81,
    "DeviceFullCode": "392M206M1M81",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 82,
    "DeviceFullCode": "392M206M1M82",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 83,
    "DeviceFullCode": "392M206M1M83",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 84,
    "DeviceFullCode": "392M206M1M84",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 85,
    "DeviceFullCode": "392M206M1M85",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 22.3200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 86,
    "DeviceFullCode": "392M206M1M86",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 87,
    "DeviceFullCode": "392M206M1M87",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 88,
    "DeviceFullCode": "392M206M1M88",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 89,
    "DeviceFullCode": "392M206M1M89",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 90,
    "DeviceFullCode": "392M206M1M90",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 91,
    "DeviceFullCode": "392M206M1M91",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 92,
    "DeviceFullCode": "392M206M1M92",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 93,
    "DeviceFullCode": "392M206M1M93",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 94,
    "DeviceFullCode": "392M206M1M94",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 95,
    "DeviceFullCode": "392M206M1M95",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 96,
    "DeviceFullCode": "392M206M1M96",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 97,
    "DeviceFullCode": "392M206M1M97",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 98,
    "DeviceFullCode": "392M206M1M98",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 99,
    "DeviceFullCode": "392M206M1M99",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 100,
    "DeviceFullCode": "392M206M1M100",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 101,
    "DeviceFullCode": "392M206M1M101",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 102,
    "DeviceFullCode": "392M206M1M102",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 22.3200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 103,
    "DeviceFullCode": "392M206M1M103",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 104,
    "DeviceFullCode": "392M206M1M104",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 105,
    "DeviceFullCode": "392M206M1M105",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 106,
    "DeviceFullCode": "392M206M1M106",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 107,
    "DeviceFullCode": "392M206M1M107",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 108,
    "DeviceFullCode": "392M206M1M108",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 109,
    "DeviceFullCode": "392M206M1M109",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 110,
    "DeviceFullCode": "392M206M1M110",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 111,
    "DeviceFullCode": "392M206M1M111",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 112,
    "DeviceFullCode": "392M206M1M112",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 113,
    "DeviceFullCode": "392M206M1M113",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 114,
    "DeviceFullCode": "392M206M1M114",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 115,
    "DeviceFullCode": "392M206M1M115",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 116,
    "DeviceFullCode": "392M206M1M116",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 117,
    "DeviceFullCode": "392M206M1M117",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 118,
    "DeviceFullCode": "392M206M1M118",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 119,
    "DeviceFullCode": "392M206M1M119",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 120,
    "DeviceFullCode": "392M206M1M120",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 121,
    "DeviceFullCode": "392M206M1M121",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 122,
    "DeviceFullCode": "392M206M1M122",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 123,
    "DeviceFullCode": "392M206M1M123",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 124,
    "DeviceFullCode": "392M206M1M124",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 125,
    "DeviceFullCode": "392M206M1M125",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 126,
    "DeviceFullCode": "392M206M1M126",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 127,
    "DeviceFullCode": "392M206M1M127",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 128,
    "DeviceFullCode": "392M206M1M128",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 129,
    "DeviceFullCode": "392M206M1M129",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 130,
    "DeviceFullCode": "392M206M1M130",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 131,
    "DeviceFullCode": "392M206M1M131",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 132,
    "DeviceFullCode": "392M206M1M132",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 133,
    "DeviceFullCode": "392M206M1M133",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 50.2200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 134,
    "DeviceFullCode": "392M206M1M134",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 135,
    "DeviceFullCode": "392M206M1M135",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 136,
    "DeviceFullCode": "392M206M1M136",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 137,
    "DeviceFullCode": "392M206M1M137",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 44.6400
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 138,
    "DeviceFullCode": "392M206M1M138",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 44.6400
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 139,
    "DeviceFullCode": "392M206M1M139",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 140,
    "DeviceFullCode": "392M206M1M140",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 141,
    "DeviceFullCode": "392M206M1M141",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 142,
    "DeviceFullCode": "392M206M1M142",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 143,
    "DeviceFullCode": "392M206M1M143",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 144,
    "DeviceFullCode": "392M206M1M144",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 145,
    "DeviceFullCode": "392M206M1M145",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 146,
    "DeviceFullCode": "392M206M1M146",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 147,
    "DeviceFullCode": "392M206M1M147",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 148,
    "DeviceFullCode": "392M206M1M148",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 149,
    "DeviceFullCode": "392M206M1M149",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 150,
    "DeviceFullCode": "392M206M1M150",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 151,
    "DeviceFullCode": "392M206M1M151",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 152,
    "DeviceFullCode": "392M206M1M152",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 153,
    "DeviceFullCode": "392M206M1M153",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 154,
    "DeviceFullCode": "392M206M1M154",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 155,
    "DeviceFullCode": "392M206M1M155",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 156,
    "DeviceFullCode": "392M206M1M156",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 157,
    "DeviceFullCode": "392M206M1M157",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 158,
    "DeviceFullCode": "392M206M1M158",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 159,
    "DeviceFullCode": "392M206M1M159",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 160,
    "DeviceFullCode": "392M206M1M160",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 161,
    "DeviceFullCode": "392M206M1M161",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 162,
    "DeviceFullCode": "392M206M1M162",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 163,
    "DeviceFullCode": "392M206M1M163",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 164,
    "DeviceFullCode": "392M206M1M164",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 165,
    "DeviceFullCode": "392M206M1M165",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 166,
    "DeviceFullCode": "392M206M1M166",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 167,
    "DeviceFullCode": "392M206M1M167",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 168,
    "DeviceFullCode": "392M206M1M168",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 169,
    "DeviceFullCode": "392M206M1M169",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 50.2200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 170,
    "DeviceFullCode": "392M206M1M170",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 171,
    "DeviceFullCode": "392M206M1M171",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 172,
    "DeviceFullCode": "392M206M1M172",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 173,
    "DeviceFullCode": "392M206M1M173",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 174,
    "DeviceFullCode": "392M206M1M174",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 175,
    "DeviceFullCode": "392M206M1M175",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 176,
    "DeviceFullCode": "392M206M1M176",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 177,
    "DeviceFullCode": "392M206M1M177",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 50.2200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 178,
    "DeviceFullCode": "392M206M1M178",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 179,
    "DeviceFullCode": "392M206M1M179",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 180,
    "DeviceFullCode": "392M206M1M180",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 181,
    "DeviceFullCode": "392M206M1M181",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 182,
    "DeviceFullCode": "392M206M1M182",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 183,
    "DeviceFullCode": "392M206M1M183",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 184,
    "DeviceFullCode": "392M206M1M184",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 185,
    "DeviceFullCode": "392M206M1M185",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 50.2200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 186,
    "DeviceFullCode": "392M206M1M186",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 187,
    "DeviceFullCode": "392M206M1M187",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 188,
    "DeviceFullCode": "392M206M1M188",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 189,
    "DeviceFullCode": "392M206M1M189",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 190,
    "DeviceFullCode": "392M206M1M190",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 191,
    "DeviceFullCode": "392M206M1M191",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 192,
    "DeviceFullCode": "392M206M1M192",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 193,
    "DeviceFullCode": "392M206M1M193",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 194,
    "DeviceFullCode": "392M206M1M194",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 195,
    "DeviceFullCode": "392M206M1M195",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 196,
    "DeviceFullCode": "392M206M1M196",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 50.2200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 197,
    "DeviceFullCode": "392M206M1M197",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 198,
    "DeviceFullCode": "392M206M1M198",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 199,
    "DeviceFullCode": "392M206M1M199",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 200,
    "DeviceFullCode": "392M206M1M200",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 201,
    "DeviceFullCode": "392M206M1M201",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 202,
    "DeviceFullCode": "392M206M1M202",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 203,
    "DeviceFullCode": "392M206M1M203",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 204,
    "DeviceFullCode": "392M206M1M204",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 205,
    "DeviceFullCode": "392M206M1M205",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 206,
    "DeviceFullCode": "392M206M1M206",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 207,
    "DeviceFullCode": "392M206M1M207",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 208,
    "DeviceFullCode": "392M206M1M208",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 209,
    "DeviceFullCode": "392M206M1M209",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 210,
    "DeviceFullCode": "392M206M1M210",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 211,
    "DeviceFullCode": "392M206M1M211",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 212,
    "DeviceFullCode": "392M206M1M212",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 213,
    "DeviceFullCode": "392M206M1M213",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 214,
    "DeviceFullCode": "392M206M1M214",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 215,
    "DeviceFullCode": "392M206M1M215",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 216,
    "DeviceFullCode": "392M206M1M216",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 217,
    "DeviceFullCode": "392M206M1M217",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 218,
    "DeviceFullCode": "392M206M1M218",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 219,
    "DeviceFullCode": "392M206M1M219",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 220,
    "DeviceFullCode": "392M206M1M220",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 221,
    "DeviceFullCode": "392M206M1M221",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 50.2200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 222,
    "DeviceFullCode": "392M206M1M222",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 223,
    "DeviceFullCode": "392M206M1M223",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 224,
    "DeviceFullCode": "392M206M1M224",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 225,
    "DeviceFullCode": "392M206M1M225",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 226,
    "DeviceFullCode": "392M206M1M226",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 50.2200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 227,
    "DeviceFullCode": "392M206M1M227",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 228,
    "DeviceFullCode": "392M206M1M228",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 229,
    "DeviceFullCode": "392M206M1M229",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 230,
    "DeviceFullCode": "392M206M1M230",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 231,
    "DeviceFullCode": "392M206M1M231",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 232,
    "DeviceFullCode": "392M206M1M232",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 233,
    "DeviceFullCode": "392M206M1M233",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 234,
    "DeviceFullCode": "392M206M1M234",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 235,
    "DeviceFullCode": "392M206M1M235",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 50.2200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 236,
    "DeviceFullCode": "392M206M1M236",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 237,
    "DeviceFullCode": "392M206M1M237",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 238,
    "DeviceFullCode": "392M206M1M238",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 239,
    "DeviceFullCode": "392M206M1M239",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 44.6400
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 240,
    "DeviceFullCode": "392M206M1M240",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 241,
    "DeviceFullCode": "392M206M1M241",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 242,
    "DeviceFullCode": "392M206M1M242",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 243,
    "DeviceFullCode": "392M206M1M243",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 244,
    "DeviceFullCode": "392M206M1M244",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 245,
    "DeviceFullCode": "392M206M1M245",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 246,
    "DeviceFullCode": "392M206M1M246",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 247,
    "DeviceFullCode": "392M206M1M247",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 248,
    "DeviceFullCode": "392M206M1M248",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 249,
    "DeviceFullCode": "392M206M1M249",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 250,
    "DeviceFullCode": "392M206M1M250",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 251,
    "DeviceFullCode": "392M206M1M251",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 252,
    "DeviceFullCode": "392M206M1M252",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 253,
    "DeviceFullCode": "392M206M1M253",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 254,
    "DeviceFullCode": "392M206M1M254",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 255,
    "DeviceFullCode": "392M206M1M255",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 256,
    "DeviceFullCode": "392M206M1M256",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 257,
    "DeviceFullCode": "392M206M1M257",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 52.2000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 258,
    "DeviceFullCode": "392M206M1M258",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 259,
    "DeviceFullCode": "392M206M1M259",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 260,
    "DeviceFullCode": "392M206M1M260",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 261,
    "DeviceFullCode": "392M206M1M261",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 262,
    "DeviceFullCode": "392M206M1M262",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 263,
    "DeviceFullCode": "392M206M1M263",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 264,
    "DeviceFullCode": "392M206M1M264",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 265,
    "DeviceFullCode": "392M206M1M265",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 266,
    "DeviceFullCode": "392M206M1M266",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 267,
    "DeviceFullCode": "392M206M1M267",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 268,
    "DeviceFullCode": "392M206M1M268",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 269,
    "DeviceFullCode": "392M206M1M269",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 270,
    "DeviceFullCode": "392M206M1M270",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 271,
    "DeviceFullCode": "392M206M1M271",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 272,
    "DeviceFullCode": "392M206M1M272",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 273,
    "DeviceFullCode": "392M206M1M273",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 274,
    "DeviceFullCode": "392M206M1M274",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 275,
    "DeviceFullCode": "392M206M1M275",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 50.2200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 276,
    "DeviceFullCode": "392M206M1M276",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 277,
    "DeviceFullCode": "392M206M1M277",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 278,
    "DeviceFullCode": "392M206M1M278",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 279,
    "DeviceFullCode": "392M206M1M279",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 280,
    "DeviceFullCode": "392M206M1M280",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 281,
    "DeviceFullCode": "392M206M1M281",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 282,
    "DeviceFullCode": "392M206M1M282",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 283,
    "DeviceFullCode": "392M206M1M283",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 284,
    "DeviceFullCode": "392M206M1M284",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 285,
    "DeviceFullCode": "392M206M1M285",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 286,
    "DeviceFullCode": "392M206M1M286",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 287,
    "DeviceFullCode": "392M206M1M287",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 288,
    "DeviceFullCode": "392M206M1M288",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 289,
    "DeviceFullCode": "392M206M1M289",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 50.2200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 290,
    "DeviceFullCode": "392M206M1M290",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 291,
    "DeviceFullCode": "392M206M1M291",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 292,
    "DeviceFullCode": "392M206M1M292",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 44.6400
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 293,
    "DeviceFullCode": "392M206M1M293",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 294,
    "DeviceFullCode": "392M206M1M294",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 295,
    "DeviceFullCode": "392M206M1M295",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 296,
    "DeviceFullCode": "392M206M1M296",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 297,
    "DeviceFullCode": "392M206M1M297",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 298,
    "DeviceFullCode": "392M206M1M298",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 299,
    "DeviceFullCode": "392M206M1M299",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 300,
    "DeviceFullCode": "392M206M1M300",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 301,
    "DeviceFullCode": "392M206M1M301",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 302,
    "DeviceFullCode": "392M206M1M302",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 303,
    "DeviceFullCode": "392M206M1M303",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 304,
    "DeviceFullCode": "392M206M1M304",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 305,
    "DeviceFullCode": "392M206M1M305",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 306,
    "DeviceFullCode": "392M206M1M306",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 307,
    "DeviceFullCode": "392M206M1M307",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 308,
    "DeviceFullCode": "392M206M1M308",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 309,
    "DeviceFullCode": "392M206M1M309",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 310,
    "DeviceFullCode": "392M206M1M310",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 39.0600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 311,
    "DeviceFullCode": "392M206M1M311",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 312,
    "DeviceFullCode": "392M206M1M312",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 313,
    "DeviceFullCode": "392M206M1M313",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 314,
    "DeviceFullCode": "392M206M1M314",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 315,
    "DeviceFullCode": "392M206M1M315",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 316,
    "DeviceFullCode": "392M206M1M316",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 317,
    "DeviceFullCode": "392M206M1M317",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 318,
    "DeviceFullCode": "392M206M1M318",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 319,
    "DeviceFullCode": "392M206M1M319",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 320,
    "DeviceFullCode": "392M206M1M320",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 321,
    "DeviceFullCode": "392M206M1M321",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 322,
    "DeviceFullCode": "392M206M1M322",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 323,
    "DeviceFullCode": "392M206M1M323",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 324,
    "DeviceFullCode": "392M206M1M324",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 325,
    "DeviceFullCode": "392M206M1M325",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 326,
    "DeviceFullCode": "392M206M1M326",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 327,
    "DeviceFullCode": "392M206M1M327",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 328,
    "DeviceFullCode": "392M206M1M328",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 329,
    "DeviceFullCode": "392M206M1M329",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 330,
    "DeviceFullCode": "392M206M1M330",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 331,
    "DeviceFullCode": "392M206M1M331",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 332,
    "DeviceFullCode": "392M206M1M332",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 333,
    "DeviceFullCode": "392M206M1M333",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 334,
    "DeviceFullCode": "392M206M1M334",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 335,
    "DeviceFullCode": "392M206M1M335",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 336,
    "DeviceFullCode": "392M206M1M336",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 337,
    "DeviceFullCode": "392M206M1M337",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 338,
    "DeviceFullCode": "392M206M1M338",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 339,
    "DeviceFullCode": "392M206M1M339",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 340,
    "DeviceFullCode": "392M206M1M340",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 341,
    "DeviceFullCode": "392M206M1M341",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 342,
    "DeviceFullCode": "392M206M1M342",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 343,
    "DeviceFullCode": "392M206M1M343",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 344,
    "DeviceFullCode": "392M206M1M344",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 345,
    "DeviceFullCode": "392M206M1M345",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 346,
    "DeviceFullCode": "392M206M1M346",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 347,
    "DeviceFullCode": "392M206M1M347",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 348,
    "DeviceFullCode": "392M206M1M348",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 349,
    "DeviceFullCode": "392M206M1M349",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 350,
    "DeviceFullCode": "392M206M1M350",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 351,
    "DeviceFullCode": "392M206M1M351",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 352,
    "DeviceFullCode": "392M206M1M352",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 353,
    "DeviceFullCode": "392M206M1M353",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 354,
    "DeviceFullCode": "392M206M1M354",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 355,
    "DeviceFullCode": "392M206M1M355",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 356,
    "DeviceFullCode": "392M206M1M356",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 357,
    "DeviceFullCode": "392M206M1M357",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 358,
    "DeviceFullCode": "392M206M1M358",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 359,
    "DeviceFullCode": "392M206M1M359",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 360,
    "DeviceFullCode": "392M206M1M360",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 361,
    "DeviceFullCode": "392M206M1M361",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 362,
    "DeviceFullCode": "392M206M1M362",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 363,
    "DeviceFullCode": "392M206M1M363",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 364,
    "DeviceFullCode": "392M206M1M364",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 365,
    "DeviceFullCode": "392M206M1M365",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 366,
    "DeviceFullCode": "392M206M1M366",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 367,
    "DeviceFullCode": "392M206M1M367",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 368,
    "DeviceFullCode": "392M206M1M368",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 369,
    "DeviceFullCode": "392M206M1M369",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 370,
    "DeviceFullCode": "392M206M1M370",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 371,
    "DeviceFullCode": "392M206M1M371",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 372,
    "DeviceFullCode": "392M206M1M372",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 44.6400
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 373,
    "DeviceFullCode": "392M206M1M373",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 374,
    "DeviceFullCode": "392M206M1M374",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 375,
    "DeviceFullCode": "392M206M1M375",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 376,
    "DeviceFullCode": "392M206M1M376",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 377,
    "DeviceFullCode": "392M206M1M377",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 378,
    "DeviceFullCode": "392M206M1M378",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 379,
    "DeviceFullCode": "392M206M1M379",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 380,
    "DeviceFullCode": "392M206M1M380",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 50.2200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 381,
    "DeviceFullCode": "392M206M1M381",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 382,
    "DeviceFullCode": "392M206M1M382",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 383,
    "DeviceFullCode": "392M206M1M383",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 384,
    "DeviceFullCode": "392M206M1M384",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 385,
    "DeviceFullCode": "392M206M1M385",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 386,
    "DeviceFullCode": "392M206M1M386",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 387,
    "DeviceFullCode": "392M206M1M387",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 388,
    "DeviceFullCode": "392M206M1M388",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 389,
    "DeviceFullCode": "392M206M1M389",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 390,
    "DeviceFullCode": "392M206M1M390",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 391,
    "DeviceFullCode": "392M206M1M391",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 392,
    "DeviceFullCode": "392M206M1M392",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 393,
    "DeviceFullCode": "392M206M1M393",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 394,
    "DeviceFullCode": "392M206M1M394",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 395,
    "DeviceFullCode": "392M206M1M395",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 396,
    "DeviceFullCode": "392M206M1M396",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 50.2200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 397,
    "DeviceFullCode": "392M206M1M397",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 398,
    "DeviceFullCode": "392M206M1M398",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 399,
    "DeviceFullCode": "392M206M1M399",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 400,
    "DeviceFullCode": "392M206M1M400",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 401,
    "DeviceFullCode": "392M206M1M401",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 402,
    "DeviceFullCode": "392M206M1M402",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 403,
    "DeviceFullCode": "392M206M1M403",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 404,
    "DeviceFullCode": "392M206M1M404",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 405,
    "DeviceFullCode": "392M206M1M405",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 406,
    "DeviceFullCode": "392M206M1M406",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 407,
    "DeviceFullCode": "392M206M1M407",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 408,
    "DeviceFullCode": "392M206M1M408",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 409,
    "DeviceFullCode": "392M206M1M409",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 410,
    "DeviceFullCode": "392M206M1M410",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 44.6400
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 411,
    "DeviceFullCode": "392M206M1M411",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 412,
    "DeviceFullCode": "392M206M1M412",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 413,
    "DeviceFullCode": "392M206M1M413",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 414,
    "DeviceFullCode": "392M206M1M414",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 415,
    "DeviceFullCode": "392M206M1M415",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 416,
    "DeviceFullCode": "392M206M1M416",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 417,
    "DeviceFullCode": "392M206M1M417",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 418,
    "DeviceFullCode": "392M206M1M418",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 419,
    "DeviceFullCode": "392M206M1M419",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 420,
    "DeviceFullCode": "392M206M1M420",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 421,
    "DeviceFullCode": "392M206M1M421",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 422,
    "DeviceFullCode": "392M206M1M422",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 423,
    "DeviceFullCode": "392M206M1M423",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 424,
    "DeviceFullCode": "392M206M1M424",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 425,
    "DeviceFullCode": "392M206M1M425",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 426,
    "DeviceFullCode": "392M206M1M426",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 427,
    "DeviceFullCode": "392M206M1M427",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 428,
    "DeviceFullCode": "392M206M1M428",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 429,
    "DeviceFullCode": "392M206M1M429",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 430,
    "DeviceFullCode": "392M206M1M430",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 431,
    "DeviceFullCode": "392M206M1M431",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 432,
    "DeviceFullCode": "392M206M1M432",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 50.2200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 433,
    "DeviceFullCode": "392M206M1M433",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 434,
    "DeviceFullCode": "392M206M1M434",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 435,
    "DeviceFullCode": "392M206M1M435",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 436,
    "DeviceFullCode": "392M206M1M436",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 437,
    "DeviceFullCode": "392M206M1M437",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 438,
    "DeviceFullCode": "392M206M1M438",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 439,
    "DeviceFullCode": "392M206M1M439",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 440,
    "DeviceFullCode": "392M206M1M440",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 441,
    "DeviceFullCode": "392M206M1M441",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 442,
    "DeviceFullCode": "392M206M1M442",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 443,
    "DeviceFullCode": "392M206M1M443",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 44.6400
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 444,
    "DeviceFullCode": "392M206M1M444",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 445,
    "DeviceFullCode": "392M206M1M445",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 446,
    "DeviceFullCode": "392M206M1M446",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 447,
    "DeviceFullCode": "392M206M1M447",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 448,
    "DeviceFullCode": "392M206M1M448",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 449,
    "DeviceFullCode": "392M206M1M449",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 450,
    "DeviceFullCode": "392M206M1M450",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 451,
    "DeviceFullCode": "392M206M1M451",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 452,
    "DeviceFullCode": "392M206M1M452",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 453,
    "DeviceFullCode": "392M206M1M453",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 454,
    "DeviceFullCode": "392M206M1M454",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 455,
    "DeviceFullCode": "392M206M1M455",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 456,
    "DeviceFullCode": "392M206M1M456",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 457,
    "DeviceFullCode": "392M206M1M457",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 458,
    "DeviceFullCode": "392M206M1M458",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 459,
    "DeviceFullCode": "392M206M1M459",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 460,
    "DeviceFullCode": "392M206M1M460",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 461,
    "DeviceFullCode": "392M206M1M461",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 462,
    "DeviceFullCode": "392M206M1M462",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 463,
    "DeviceFullCode": "392M206M1M463",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 464,
    "DeviceFullCode": "392M206M1M464",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 465,
    "DeviceFullCode": "392M206M1M465",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 466,
    "DeviceFullCode": "392M206M1M466",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 467,
    "DeviceFullCode": "392M206M1M467",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 468,
    "DeviceFullCode": "392M206M1M468",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 469,
    "DeviceFullCode": "392M206M1M469",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 470,
    "DeviceFullCode": "392M206M1M470",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 50.2200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 471,
    "DeviceFullCode": "392M206M1M471",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 472,
    "DeviceFullCode": "392M206M1M472",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 473,
    "DeviceFullCode": "392M206M1M473",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 50.2200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 474,
    "DeviceFullCode": "392M206M1M474",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 475,
    "DeviceFullCode": "392M206M1M475",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 476,
    "DeviceFullCode": "392M206M1M476",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 477,
    "DeviceFullCode": "392M206M1M477",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 478,
    "DeviceFullCode": "392M206M1M478",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 479,
    "DeviceFullCode": "392M206M1M479",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 480,
    "DeviceFullCode": "392M206M1M480",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 481,
    "DeviceFullCode": "392M206M1M481",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 50.2200
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 482,
    "DeviceFullCode": "392M206M1M482",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 483,
    "DeviceFullCode": "392M206M1M483",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 484,
    "DeviceFullCode": "392M206M1M484",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 485,
    "DeviceFullCode": "392M206M1M485",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 486,
    "DeviceFullCode": "392M206M1M486",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 487,
    "DeviceFullCode": "392M206M1M487",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 488,
    "DeviceFullCode": "392M206M1M488",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 489,
    "DeviceFullCode": "392M206M1M489",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 490,
    "DeviceFullCode": "392M206M1M490",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 491,
    "DeviceFullCode": "392M206M1M491",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 492,
    "DeviceFullCode": "392M206M1M492",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 493,
    "DeviceFullCode": "392M206M1M493",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 494,
    "DeviceFullCode": "392M206M1M494",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 495,
    "DeviceFullCode": "392M206M1M495",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 496,
    "DeviceFullCode": "392M206M1M496",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 497,
    "DeviceFullCode": "392M206M1M497",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 498,
    "DeviceFullCode": "392M206M1M498",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 499,
    "DeviceFullCode": "392M206M1M499",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 500,
    "DeviceFullCode": "392M206M1M500",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 501,
    "DeviceFullCode": "392M206M1M501",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 502,
    "DeviceFullCode": "392M206M1M502",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 503,
    "DeviceFullCode": "392M206M1M503",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 55.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 504,
    "DeviceFullCode": "392M206M1M504",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 505,
    "DeviceFullCode": "392M206M1M505",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 506,
    "DeviceFullCode": "392M206M1M506",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 507,
    "DeviceFullCode": "392M206M1M507",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 508,
    "DeviceFullCode": "392M206M1M508",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 509,
    "DeviceFullCode": "392M206M1M509",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 61.3800
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 1,
    "DeviceCode": 510,
    "DeviceFullCode": "392M206M1M510",
    "DeviceModeFullCode": "392M206M1",
    "PDeviceFullCode": None,
    "Capacity": 66.9600
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceCode": 1,
    "DeviceFullCode": "392M302M8M1",
    "DeviceModeFullCode": "392M302M8",
    "PDeviceFullCode": None,
    "Capacity": 18581.0000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceCode": 2,
    "DeviceFullCode": "392M302M8M2",
    "DeviceModeFullCode": "392M302M8",
    "PDeviceFullCode": None,
    "Capacity": 9837.0000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceCode": 3,
    "DeviceFullCode": "392M302M8M3",
    "DeviceModeFullCode": "392M302M8",
    "PDeviceFullCode": None,
    "Capacity": 4372.0000
  },
  {
    "DeviceTypeCode": 305,
    "DeviceModeCode": 7,
    "DeviceCode": 1,
    "DeviceFullCode": "392M305M7M1",
    "DeviceModeFullCode": "392M305M7",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 307,
    "DeviceModeCode": 7,
    "DeviceCode": 1,
    "DeviceFullCode": "392M307M7M1",
    "DeviceModeFullCode": "392M307M7",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceCode": 1,
    "DeviceFullCode": "392M505M7M1",
    "DeviceModeFullCode": "392M505M7",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceCode": 2,
    "DeviceFullCode": "392M505M7M2",
    "DeviceModeFullCode": "392M505M7",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceCode": 3,
    "DeviceFullCode": "392M505M7M3",
    "DeviceModeFullCode": "392M505M7",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceCode": 4,
    "DeviceFullCode": "392M505M7M4",
    "DeviceModeFullCode": "392M505M7",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 8,
    "DeviceCode": 5,
    "DeviceFullCode": "392M505M8M5",
    "DeviceModeFullCode": "392M505M8",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 8,
    "DeviceCode": 6,
    "DeviceFullCode": "392M505M8M6",
    "DeviceModeFullCode": "392M505M8",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 7,
    "DeviceFullCode": "392M505M2M7",
    "DeviceModeFullCode": "392M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 8,
    "DeviceFullCode": "392M505M2M8",
    "DeviceModeFullCode": "392M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 9,
    "DeviceFullCode": "392M505M2M9",
    "DeviceModeFullCode": "392M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 10,
    "DeviceFullCode": "392M505M2M10",
    "DeviceModeFullCode": "392M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 11,
    "DeviceFullCode": "392M505M2M11",
    "DeviceModeFullCode": "392M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 12,
    "DeviceFullCode": "392M505M2M12",
    "DeviceModeFullCode": "392M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 13,
    "DeviceFullCode": "392M505M2M13",
    "DeviceModeFullCode": "392M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 14,
    "DeviceFullCode": "392M505M2M14",
    "DeviceModeFullCode": "392M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 9,
    "DeviceCode": 15,
    "DeviceFullCode": "392M505M9M15",
    "DeviceModeFullCode": "392M505M9",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 9,
    "DeviceCode": 16,
    "DeviceFullCode": "392M505M9M16",
    "DeviceModeFullCode": "392M505M9",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceCode": 1,
    "DeviceFullCode": "392M801M1M1",
    "DeviceModeFullCode": "392M801M1",
    "PDeviceFullCode": None,
    "Capacity": None
  }
]



class station:
    def __init__(self,PT_azuretable,PT_sql,DataBeginTime,DataEndTime):
      
        self.sDt = parser.parse(DataBeginTime)
        eDt = parser.parse(DataEndTime)
        self.time_width = PT_sql * 60
        self.sRowKey = mathtool.TimetoStamp(self.sDt)
        self.eRowKey = mathtool.TimetoStamp(eDt)
        self.sTime = self.sDt.strftime("%Y-%m-%d %H:%M:%S")
        self.table_service = TableService(account_name=tc.account_name, account_key=tc.account_key,endpoint_suffix=tc.endpoint_suffix)
        self.azureTableNameSuffix = 'T' + self.sDt.strftime('%Y%m') + 'PT' + str(PT_azuretable) + 'S'
        self.stringCapacity = 4.8
        self.stationCode = 392
        self.STC_rad_Avg= -1
        self.Tilted_Surf_Radi_Avg= -1
        self.Tilted_Surf_Radi_Std=0
        self.q = []
        self.azureTableRow = 0
        #lm 执行过程异常消息
        self.messages=[] 
  
    def ___calcAggrega(self,df,pointConfig,DeviceTypeCode, DeviceModeCode,DeviceCode):
      
      #DeviceCode = DeviceModeCode + 'M' + str(DeviceCode)
    
      ##聚合计算
      data = newMathUtility.calcAggrega(df,pointConfig)
      newDBData = {}
      for dbc  in data:
          if  data[dbc] != None:
                newDBData[dbc] = data[dbc]
      colum = list(newDBData.keys())
      #(lm)添加len(colum) > 0
      if len(colum) > 0:
        value = [newDBData[v] for v in colum]
        count = len(df)
        tablename_Aggrega = 'S' + str(self.stationCode) + 'M' + str(DeviceTypeCode) + 'PT10M_Aggrega'
        sql = 'delete from dbo.' + tablename_Aggrega + ' where DeviceCode=' + '\'' + DeviceCode + '\'' + ' and TimeStamp=' + '\'' + self.sTime + '\'' + ' \
            insert into dbo.' + tablename_Aggrega + '(DeviceCode,TimeStamp,count,' + str(colum).replace('[','').replace(']','').replace('\'','') + ') \
            values (' + '\'' + DeviceCode + '\'' + ',' + '\'' + self.sTime + '\'' + ',' + str(count) + ',' + str(value).replace('[','').replace(']','') + ') '
        self.q.append(sql)

      return newDBData  
        
    def ___readAzureTableToDF(self,device):

        deviceCode = device.get('DeviceCode')
        deviceModeCode = device.get('DeviceModeFullCode')
        devicetypeCode = device.get('DeviceTypeCode')
        if(deviceCode is not None or deviceModeCode is not None and devicetypeCode is not None):
          #print(str(deviceCode)+',')
          filter_string = 'PartitionKey eq ' + '\'' + str(deviceCode) + '\'' + ' and RowKey ge ' + '\'' + str(self.sRowKey) + '\'' + ' and RowKey le ' + '\'' + str(self.eRowKey) + '\''  
          tasks = self.table_service.query_entities('S' + str(deviceModeCode) + self.azureTableNameSuffix,filter_string)
          rows_list = []
          for item in tasks:  
              rows_list.append(item)
          
          df = pd.DataFrame(rows_list) 
          self.azureTableRow = self.azureTableRow + len(df)
          return df 

        return None

    def execute(self):
        try:
            self.___calcDeviceAggrega(203)
            self.___calcDeviceAggrega(206)
            self.___calcDeviceAggrega(801)
 


            self.___calcComboxAndBranch() 
        except BaseException as err: 
            self.messages.append(str(err))
        finally:
            if(len(self.q)):
                self.___insertIntoSql()
            if(len(self.messages)): 
                raise  Exception(';'.join(self.messages))

            result={"tableRow":self.azureTableRow,"sqlRow":len(self.q)}

            return result
        
    
    def ___insertIntoSql(self): 
        try:
          ms = msconn.MSSQL(host=tc.mssqlConn_host,user=tc.mssqlConn_user,pwd=tc.mssqlConn_pwd,db=tc.mssqlConn_dbname)
          ms.ExecNonQueryS(self.q) 

        except BaseException as err:  
          self.messages.append('execute sql failure:'+str(err))

    def ___calcWeatherStation(self): 
        try:  
            alldevice203= filter(lambda x: x['DeviceTypeCode'] ==203, allDevice)
            for  device203  in alldevice203:
                df = self.___readAzureTableToDF(device203)
                point_203=filter(lambda x: x['DeviceTypeCode'] ==device203['DeviceTypeCode'] and x['DeviceModeCode']==device203['DeviceModeCode'], deviceModePointConfig)
                data = self.___calcAggrega(df,point_203,device203['DeviceTypeCode'],device203['DeviceModeFullCode'],device203['DeviceFullCode'])
                if(device203['DeviceFullCode']=="56M203M10M2"):  
                     self.Tilted_Surf_Radi_Avg=data.get('Tilted_Surf_Radi_Avg')
                     self.Tilted_Surf_Radi_Std=data.get('Tilted_Surf_Radi_Std')
                     self.STC_rad_Avg=data.get('STC_rad_Avg')
            pass

        except BaseException as err:  
             self.messages.append(str(err))


    def ___calcDeviceAggrega(self,deviceTypeCode):
        try:
            allDeviceTypeDevice= filter(lambda x: x['DeviceTypeCode'] == deviceTypeCode, allDevice)
            deviceMsg=''
            errCount=0
            for  deviceItem  in allDeviceTypeDevice:
                try:
                    df = self.___readAzureTableToDF(deviceItem)
                    point_item=filter(lambda x: x['DeviceTypeCode'] == deviceItem['DeviceTypeCode'] and x['DeviceModeCode']==deviceItem['DeviceModeCode'], deviceModePointConfig)
                    data = self.___calcAggrega(df,point_item,deviceItem['DeviceTypeCode'],deviceItem['DeviceModeFullCode'],deviceItem['DeviceFullCode'])
                    if deviceTypeCode==203 and deviceItem['DeviceFullCode']=="392M203M2M2":
                        self.Tilted_Surf_Radi_Avg=data.get('Tilted_Surf_Radi_Avg')
                        self.Tilted_Surf_Radi_Std=data.get('Tilted_Surf_Radi_Std')
                        self.STC_rad_Avg=data.get('STC_rad_Avg')
                except BaseException as err:
                    errCount=errCount+1
                    if deviceMsg=='':
                        deviceMsg=str(err)
            if errCount>0:
                self.messages.append('%sDevice:%s:%s'%(deviceTypeCode,errCount,deviceMsg))
        except  BaseException as err:
            self.messages.append('%s:%s'%(deviceTypeCode,str(err)))

    def ___calcComboxAndBranch(self):
        try:
            allDeviceTypeDevice= filter(lambda x: x['DeviceTypeCode'] ==202, allDevice)
            deviceMsg=''
            errCount=0
            for  deviceItem  in allDeviceTypeDevice:
                try:
                    deviceCode=deviceItem['DeviceFullCode'] 
                    df = self.___readAzureTableToDF(deviceItem)
                    point_item=filter(lambda x: x['DeviceTypeCode'] ==deviceItem['DeviceTypeCode'] and x['DeviceModeCode']==deviceItem['DeviceModeCode'], deviceModePointConfig)
                
                    data = newMathUtility.calcAggrega(df,point_item)
                    Branch_V = data.get('Branch_V_Avg')

                    Branch_A_Tot_Avg = data.get('Branch_A_Tot_Avg')
                    BranchData={}
                    if(Branch_V != None and Branch_A_Tot_Avg != None):
                        BranchData=self.___calcSingleBranch(deviceItem['DeviceFullCode'],df,Branch_V)
                  
                
                    newDBData = {}
                    for dbc  in data:
                        if  data[dbc] != None:
                              newDBData[dbc] = data[dbc]

                    for branchColumn  in BranchData:
                        if  BranchData[branchColumn] != None:
                              newDBData[branchColumn] = BranchData[branchColumn]

                    colum = list(newDBData.keys())
                    #(lm)添加len(colum) > 0
                    if len(colum) > 0:
                      value = [newDBData[v] for v in colum]
                      count = len(df)
                      tablename_Aggrega = 'S' + str(self.stationCode) + 'M' + str(202) + 'PT10M_Aggrega'
                      sql = 'delete from dbo.' + tablename_Aggrega + ' where DeviceCode=' + '\'' + deviceCode + '\'' + ' and TimeStamp=' + '\'' + self.sTime + '\'' + ' \
                          insert into dbo.' + tablename_Aggrega + '(DeviceCode,TimeStamp,count,' + str(colum).replace('[','').replace(']','').replace('\'','') + ') \
                          values (' + '\'' + deviceCode + '\'' + ',' + '\'' + self.sTime + '\'' + ',' + str(count) + ',' + str(value).replace('[','').replace(']','') + ') '
                      self.q.append(sql)
                except BaseException as err:
                    errCount=errCount+1
                    if deviceMsg=='':
                        deviceMsg=str(err)
            if errCount>0:
                self.messages.append('202Device:%s:%s'%(errCount,deviceMsg))          

        except BaseException as err:
            self.messages.append('202:'+str(err))
        

    def ___calcSingleBranch(self,deviceCode,df,Branch_V):
        branchData={} 
        rows_list = []
        
        for item in df['HL107']:  
          rows_list.append(item.split(','))

        branch_Status_list=[]
        for item in df['HL106']:  
          branch_Status_list.append(item.split(','))
        dfSt_all = pd.DataFrame(branch_Status_list)

        dfA_all = pd.DataFrame(rows_list) 

        Count_Col = dfA_all.shape[1]

        for i in range(Count_Col):  
            if self.Tilted_Surf_Radi_Avg:
                dfSt_all_df =  dfSt_all[i].astype(int)
                st=dfSt_all_df.mean()
                if(st==1):  
                    cdf=dfA_all[i].apply(lambda x: None if (str(x).isspace() or str(x)=='') else x)
                    cdf=cdf[cdf.notnull()].astype(float)
                    branchData["Branch_A"+str(i+1)+"_Max"]=cdf.max()
                    branchData["Branch_A"+str(i+1)+"_Min"]=cdf.min()
                    branchData["Branch_A"+str(i+1)+"_Avg"]=cdf.mean()
                    branchData["Branch_A"+str(i+1)+"_Std"]=cdf.std()

        return branchData
          



def run(taskparam):

    DataBeginTime = taskparam['DataBeginTime'] 
    DataEndTime = taskparam['DataEndTime'] 
    #print(DataBeginTime)
    result = {}
    #info = ReadWrite(DataBeginTime,DataEndTime).CalTable(table_WdDir = True,
    #table_WdSpdZon = True, table_TurIECSt = True, table_Aggrega = True,
    #table_Day = True)
    try:
          #testFL=[]
          #for s in range(1,75):
          #   testFL.append(s)
          s350 = station(5,10,DataBeginTime,DataEndTime) 
          jsonResult = s350.execute()
          
          result["Status"] = 400
          result["tableRow"] = jsonResult["tableRow"]
          result["sqlRow"] = jsonResult["sqlRow"]
          result["info"] = "success" 
    except BaseException as err:  
       result["Status"] = 404
       result["tableRow"] = 0
       result["sqlRow"] = 0
       result["info"] = str(err)   

    return result
