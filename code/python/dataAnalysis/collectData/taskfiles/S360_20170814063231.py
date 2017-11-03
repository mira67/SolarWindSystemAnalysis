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
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX021",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "水平总辐射分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX021",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "水平总辐射分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX021",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "水平总辐射分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX021",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "水平总辐射分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX022",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "斜面总辐射分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX022",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "斜面总辐射分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX022",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "斜面总辐射分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX022",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "斜面总辐射分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX023",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Dir_Min_Avg",
    "DeviceModePointName": "风向分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX023",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Dir_Min_Avg",
    "DeviceModePointName": "风向分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX023",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Dir_Min_Avg",
    "DeviceModePointName": "风向分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX023",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Dir_Min_Avg",
    "DeviceModePointName": "风向分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX024",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp_Min_Avg",
    "DeviceModePointName": "空气温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX024",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp_Min_Avg",
    "DeviceModePointName": "空气温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX024",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp_Min_Avg",
    "DeviceModePointName": "空气温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX024",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp_Min_Avg",
    "DeviceModePointName": "空气温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX025",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_Min_Avg",
    "DeviceModePointName": "1号背板温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX025",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_Min_Avg",
    "DeviceModePointName": "1号背板温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX025",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_Min_Avg",
    "DeviceModePointName": "1号背板温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX025",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_Min_Avg",
    "DeviceModePointName": "1号背板温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX026",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Min_Avg",
    "DeviceModePointName": "2号背板温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX026",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Min_Avg",
    "DeviceModePointName": "2号背板温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX026",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Min_Avg",
    "DeviceModePointName": "2号背板温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX026",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Min_Avg",
    "DeviceModePointName": "2号背板温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX027",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Min_Avg",
    "DeviceModePointName": "3号背板温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX027",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Min_Avg",
    "DeviceModePointName": "3号背板温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX027",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Min_Avg",
    "DeviceModePointName": "3号背板温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX027",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Min_Avg",
    "DeviceModePointName": "3号背板温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX028",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Min_Avg",
    "DeviceModePointName": "4号背板温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX028",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Min_Avg",
    "DeviceModePointName": "4号背板温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX028",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Min_Avg",
    "DeviceModePointName": "4号背板温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX028",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Min_Avg",
    "DeviceModePointName": "4号背板温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX029",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Hum_Min_Avg",
    "DeviceModePointName": "相对湿度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX029",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Hum_Min_Avg",
    "DeviceModePointName": "相对湿度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX029",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Hum_Min_Avg",
    "DeviceModePointName": "相对湿度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX029",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Hum_Min_Avg",
    "DeviceModePointName": "相对湿度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX030",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Air_Pres_Min_Avg",
    "DeviceModePointName": "大气压力分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX030",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Air_Pres_Min_Avg",
    "DeviceModePointName": "大气压力分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX030",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Air_Pres_Min_Avg",
    "DeviceModePointName": "大气压力分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX030",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Air_Pres_Min_Avg",
    "DeviceModePointName": "大气压力分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX031",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num1_Min_Avg",
    "DeviceModePointName": "1号短路电流分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX031",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num1_Min_Avg",
    "DeviceModePointName": "1号短路电流分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX031",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num1_Min_Avg",
    "DeviceModePointName": "1号短路电流分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX031",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num1_Min_Avg",
    "DeviceModePointName": "1号短路电流分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX032",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Open_V_Num1_Min_Avg",
    "DeviceModePointName": "1号开路电压分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX032",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Open_V_Num1_Min_Avg",
    "DeviceModePointName": "1号开路电压分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX032",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Open_V_Num1_Min_Avg",
    "DeviceModePointName": "1号开路电压分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX032",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Open_V_Num1_Min_Avg",
    "DeviceModePointName": "1号开路电压分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX033",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num2_Min_Avg",
    "DeviceModePointName": "2号短路电流分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX033",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num2_Min_Avg",
    "DeviceModePointName": "2号短路电流分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX033",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num2_Min_Avg",
    "DeviceModePointName": "2号短路电流分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX033",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num2_Min_Avg",
    "DeviceModePointName": "2号短路电流分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX036",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Hr_Avg",
    "DeviceModePointName": "水平总辐射小时平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX036",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Hr_Avg",
    "DeviceModePointName": "水平总辐射小时平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX036",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Hr_Avg",
    "DeviceModePointName": "水平总辐射小时平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX036",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Hr_Avg",
    "DeviceModePointName": "水平总辐射小时平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX037",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Hr_Avg",
    "DeviceModePointName": "斜面总辐射小时平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX037",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Hr_Avg",
    "DeviceModePointName": "斜面总辐射小时平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX037",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Hr_Avg",
    "DeviceModePointName": "斜面总辐射小时平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX037",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Hr_Avg",
    "DeviceModePointName": "斜面总辐射小时平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX038",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Spd_Dly_Avg",
    "DeviceModePointName": "风速天平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX038",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Spd_Dly_Avg",
    "DeviceModePointName": "风速天平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX038",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Spd_Dly_Avg",
    "DeviceModePointName": "风速天平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX038",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Spd_Dly_Avg",
    "DeviceModePointName": "风速天平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX039",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Avg",
    "DeviceModePointName": "空气温度天平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX039",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Avg",
    "DeviceModePointName": "空气温度天平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX039",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Avg",
    "DeviceModePointName": "空气温度天平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX039",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Avg",
    "DeviceModePointName": "空气温度天平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX040",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Mini",
    "DeviceModePointName": "空气温度天最小",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX040",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Mini",
    "DeviceModePointName": "空气温度天最小",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX040",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Mini",
    "DeviceModePointName": "空气温度天最小",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX040",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Mini",
    "DeviceModePointName": "空气温度天最小",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX041",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Maxm",
    "DeviceModePointName": "空气温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX041",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Maxm",
    "DeviceModePointName": "空气温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX041",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Maxm",
    "DeviceModePointName": "空气温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX041",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Maxm",
    "DeviceModePointName": "空气温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX042",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Maxm",
    "DeviceModePointName": "水平总辐射天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX042",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Maxm",
    "DeviceModePointName": "水平总辐射天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX042",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Maxm",
    "DeviceModePointName": "水平总辐射天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX042",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Maxm",
    "DeviceModePointName": "水平总辐射天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX043",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Maxm",
    "DeviceModePointName": "斜面总辐射天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX043",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Maxm",
    "DeviceModePointName": "斜面总辐射天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX043",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Maxm",
    "DeviceModePointName": "斜面总辐射天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX043",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Maxm",
    "DeviceModePointName": "斜面总辐射天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX044",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Spd_Dly_Maxm",
    "DeviceModePointName": "风速天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX044",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Spd_Dly_Maxm",
    "DeviceModePointName": "风速天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX044",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Spd_Dly_Maxm",
    "DeviceModePointName": "风速天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX044",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Wind_Spd_Dly_Maxm",
    "DeviceModePointName": "风速天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX045",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Air_Pres_Dly_Maxm",
    "DeviceModePointName": "大气压力天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX045",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Air_Pres_Dly_Maxm",
    "DeviceModePointName": "大气压力天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX045",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Air_Pres_Dly_Maxm",
    "DeviceModePointName": "大气压力天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX045",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Air_Pres_Dly_Maxm",
    "DeviceModePointName": "大气压力天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX046",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_Dly_Maxm",
    "DeviceModePointName": "1号背板温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX046",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_Dly_Maxm",
    "DeviceModePointName": "1号背板温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX046",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_Dly_Maxm",
    "DeviceModePointName": "1号背板温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX046",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_Dly_Maxm",
    "DeviceModePointName": "1号背板温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX047",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Dly_Maxm",
    "DeviceModePointName": "2号背板温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX047",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Dly_Maxm",
    "DeviceModePointName": "2号背板温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX047",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Dly_Maxm",
    "DeviceModePointName": "2号背板温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX047",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Dly_Maxm",
    "DeviceModePointName": "2号背板温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX048",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Dly_Maxm",
    "DeviceModePointName": "3号背板温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX048",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Dly_Maxm",
    "DeviceModePointName": "3号背板温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX048",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Dly_Maxm",
    "DeviceModePointName": "3号背板温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX048",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Dly_Maxm",
    "DeviceModePointName": "3号背板温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX049",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Dly_Maxm",
    "DeviceModePointName": "4号背板温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX049",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Dly_Maxm",
    "DeviceModePointName": "4号背板温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX049",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Dly_Maxm",
    "DeviceModePointName": "4号背板温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX049",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Dly_Maxm",
    "DeviceModePointName": "4号背板温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX050",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num1_Dly_Maxm",
    "DeviceModePointName": "1号短路电流天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX050",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num1_Dly_Maxm",
    "DeviceModePointName": "1号短路电流天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX050",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num1_Dly_Maxm",
    "DeviceModePointName": "1号短路电流天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX050",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num1_Dly_Maxm",
    "DeviceModePointName": "1号短路电流天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX051",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Open_V_Num1_Dly_Maxm",
    "DeviceModePointName": "1号开路电压天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX051",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Open_V_Num1_Dly_Maxm",
    "DeviceModePointName": "1号开路电压天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX051",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Open_V_Num1_Dly_Maxm",
    "DeviceModePointName": "1号开路电压天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX051",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Open_V_Num1_Dly_Maxm",
    "DeviceModePointName": "1号开路电压天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX052",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num2_Dly_Maxm",
    "DeviceModePointName": "2号短路电流天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX052",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num2_Dly_Maxm",
    "DeviceModePointName": "2号短路电流天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX052",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num2_Dly_Maxm",
    "DeviceModePointName": "2号短路电流天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX052",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Shrt_A_Num2_Dly_Maxm",
    "DeviceModePointName": "2号短路电流天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB038",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V1",
    "DeviceModePointName": " 直流电压1",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB038",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V1",
    "DeviceModePointName": " 直流电压1",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB038",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V1",
    "DeviceModePointName": " 直流电压1",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB038",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V1",
    "DeviceModePointName": " 直流电压1",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB039",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A1",
    "DeviceModePointName": " 直流电流1",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB039",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A1",
    "DeviceModePointName": " 直流电流1",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB039",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A1",
    "DeviceModePointName": " 直流电流1",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB039",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A1",
    "DeviceModePointName": " 直流电流1",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB040",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V2",
    "DeviceModePointName": " 直流电压2",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB040",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V2",
    "DeviceModePointName": " 直流电压2",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB040",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V2",
    "DeviceModePointName": " 直流电压2",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB040",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V2",
    "DeviceModePointName": " 直流电压2",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB041",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A2",
    "DeviceModePointName": " 直流电流2",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB041",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A2",
    "DeviceModePointName": " 直流电流2",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB041",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A2",
    "DeviceModePointName": " 直流电流2",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB041",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A2",
    "DeviceModePointName": " 直流电流2",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB042",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V3",
    "DeviceModePointName": " 直流电压3",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB042",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V3",
    "DeviceModePointName": " 直流电压3",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB042",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V3",
    "DeviceModePointName": " 直流电压3",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB042",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V3",
    "DeviceModePointName": " 直流电压3",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB043",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A3",
    "DeviceModePointName": " 直流电流3",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB043",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A3",
    "DeviceModePointName": " 直流电流3",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB043",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A3",
    "DeviceModePointName": " 直流电流3",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB043",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A3",
    "DeviceModePointName": " 直流电流3",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB044",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V4",
    "DeviceModePointName": " 直流电压4",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB044",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V4",
    "DeviceModePointName": " 直流电压4",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB044",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V4",
    "DeviceModePointName": " 直流电压4",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB044",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V4",
    "DeviceModePointName": " 直流电压4",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB045",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A4",
    "DeviceModePointName": " 直流电流4",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB045",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A4",
    "DeviceModePointName": " 直流电流4",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB045",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A4",
    "DeviceModePointName": " 直流电流4",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB045",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A4",
    "DeviceModePointName": " 直流电流4",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB046",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V5",
    "DeviceModePointName": " 直流电压5",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB046",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V5",
    "DeviceModePointName": " 直流电压5",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB046",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V5",
    "DeviceModePointName": " 直流电压5",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB046",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V5",
    "DeviceModePointName": " 直流电压5",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB047",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A5",
    "DeviceModePointName": " 直流电流5",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB047",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A5",
    "DeviceModePointName": " 直流电流5",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB047",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A5",
    "DeviceModePointName": " 直流电流5",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB047",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A5",
    "DeviceModePointName": " 直流电流5",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB048",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V6",
    "DeviceModePointName": " 直流电压6",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB048",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V6",
    "DeviceModePointName": " 直流电压6",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB048",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V6",
    "DeviceModePointName": " 直流电压6",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB048",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V6",
    "DeviceModePointName": " 直流电压6",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB049",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A6",
    "DeviceModePointName": " 直流电流6",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB049",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A6",
    "DeviceModePointName": " 直流电流6",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB049",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A6",
    "DeviceModePointName": " 直流电流6",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB049",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A6",
    "DeviceModePointName": " 直流电流6",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB053",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "A_DiscRate",
    "DeviceModePointName": "逆变器的电流离散率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB053",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "A_DiscRate",
    "DeviceModePointName": "逆变器的电流离散率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB053",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "A_DiscRate",
    "DeviceModePointName": "逆变器的电流离散率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB053",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "A_DiscRate",
    "DeviceModePointName": "逆变器的电流离散率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB054",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "逆变器的直流总电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB054",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "逆变器的直流总电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB054",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "逆变器的直流总电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB054",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "逆变器的直流总电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "逆变器总运行时间",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "逆变器总运行时间",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "逆变器总运行时间",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "逆变器总运行时间",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ007",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "3U0",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ007",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "3U0",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ007",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "3U0",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ007",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "3U0",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ008",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ008",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ008",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ008",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ009",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ009",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ009",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ009",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ010",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ010",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ010",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ010",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ011",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "3I0",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ011",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "3I0",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ011",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "3I0",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ011",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "3I0",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ012",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ012",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ012",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ012",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ013",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ013",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ013",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ013",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ014",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ014",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ014",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ014",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ015",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ015",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ015",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ015",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN001",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "MinTotWh",
    "DeviceModePointName": "正向有功总电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN001",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "MinTotWh",
    "DeviceModePointName": "正向有功总电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN001",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "MinTotWh",
    "DeviceModePointName": "正向有功总电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN002",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "MinTotWhCsm",
    "DeviceModePointName": "反向有功总电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN002",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "MinTotWhCsm",
    "DeviceModePointName": "反向有功总电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN002",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "MinTotWhCsm",
    "DeviceModePointName": "反向有功总电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN003",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "MinTotVArh",
    "DeviceModePointName": "正向无功总电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN003",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "MinTotVArh",
    "DeviceModePointName": "正向无功总电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN003",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "MinTotVArh",
    "DeviceModePointName": "正向无功总电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN004",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "MinTotVarhCsm",
    "DeviceModePointName": "反向无功总电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN004",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "MinTotVarhCsm",
    "DeviceModePointName": "反向无功总电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN004",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "MinTotVarhCsm",
    "DeviceModePointName": "反向无功总电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN001",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "MinTotWh",
    "DeviceModePointName": "正向有功总电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN001",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "MinTotWh",
    "DeviceModePointName": "正向有功总电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN001",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "MinTotWh",
    "DeviceModePointName": "正向有功总电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN002",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "MinTotWhCsm",
    "DeviceModePointName": "反向有功总电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN002",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "MinTotWhCsm",
    "DeviceModePointName": "反向有功总电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN002",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "MinTotWhCsm",
    "DeviceModePointName": "反向有功总电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN003",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "MinTotVArh",
    "DeviceModePointName": "正向无功总电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN003",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "MinTotVArh",
    "DeviceModePointName": "正向无功总电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN003",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "MinTotVArh",
    "DeviceModePointName": "正向无功总电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN004",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "MinTotVarhCsm",
    "DeviceModePointName": "反向无功总电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN004",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "MinTotVarhCsm",
    "DeviceModePointName": "反向无功总电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN004",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "MinTotVarhCsm",
    "DeviceModePointName": "反向无功总电量",
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
    "DeviceModeCode": 9,
    "DeviceCode": 1,
    "DeviceFullCode": "360M202M9M1",
    "DeviceModeFullCode": "360M202M9",
    "PDeviceFullCode": "360M304M19M32",
    "Capacity": 264.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 9,
    "DeviceCode": 2,
    "DeviceFullCode": "360M202M9M2",
    "DeviceModeFullCode": "360M202M9",
    "PDeviceFullCode": "360M304M19M32",
    "Capacity": 297.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 9,
    "DeviceCode": 3,
    "DeviceFullCode": "360M202M9M3",
    "DeviceModeFullCode": "360M202M9",
    "PDeviceFullCode": "360M304M19M32",
    "Capacity": 302.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 9,
    "DeviceCode": 4,
    "DeviceFullCode": "360M202M9M4",
    "DeviceModeFullCode": "360M202M9",
    "PDeviceFullCode": "360M304M19M32",
    "Capacity": 226.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 9,
    "DeviceCode": 5,
    "DeviceFullCode": "360M202M9M5",
    "DeviceModeFullCode": "360M202M9",
    "PDeviceFullCode": "360M304M19M33",
    "Capacity": 264.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 9,
    "DeviceCode": 6,
    "DeviceFullCode": "360M202M9M6",
    "DeviceModeFullCode": "360M202M9",
    "PDeviceFullCode": "360M304M19M33",
    "Capacity": 302.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 9,
    "DeviceCode": 7,
    "DeviceFullCode": "360M202M9M7",
    "DeviceModeFullCode": "360M202M9",
    "PDeviceFullCode": "360M304M19M33",
    "Capacity": 302.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 9,
    "DeviceCode": 8,
    "DeviceFullCode": "360M202M9M8",
    "DeviceModeFullCode": "360M202M9",
    "PDeviceFullCode": "360M304M19M33",
    "Capacity": 221.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 9,
    "DeviceCode": 9,
    "DeviceFullCode": "360M202M9M9",
    "DeviceModeFullCode": "360M202M9",
    "PDeviceFullCode": "360M304M19M34",
    "Capacity": 264.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 9,
    "DeviceCode": 10,
    "DeviceFullCode": "360M202M9M10",
    "DeviceModeFullCode": "360M202M9",
    "PDeviceFullCode": "360M304M19M34",
    "Capacity": 264.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 9,
    "DeviceCode": 11,
    "DeviceFullCode": "360M202M9M11",
    "DeviceModeFullCode": "360M202M9",
    "PDeviceFullCode": "360M304M19M34",
    "Capacity": 226.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 9,
    "DeviceCode": 12,
    "DeviceFullCode": "360M202M9M12",
    "DeviceModeFullCode": "360M202M9",
    "PDeviceFullCode": "360M304M19M34",
    "Capacity": 178.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 9,
    "DeviceCode": 13,
    "DeviceFullCode": "360M202M9M13",
    "DeviceModeFullCode": "360M202M9",
    "PDeviceFullCode": "360M304M19M34",
    "Capacity": 151.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 9,
    "DeviceCode": 14,
    "DeviceFullCode": "360M202M9M14",
    "DeviceModeFullCode": "360M202M9",
    "PDeviceFullCode": "360M304M19M35",
    "Capacity": 151.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 9,
    "DeviceCode": 15,
    "DeviceFullCode": "360M202M9M15",
    "DeviceModeFullCode": "360M202M9",
    "PDeviceFullCode": "360M304M19M35",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 9,
    "DeviceCode": 16,
    "DeviceFullCode": "360M202M9M16",
    "DeviceModeFullCode": "360M202M9",
    "PDeviceFullCode": "360M304M19M35",
    "Capacity": 205.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 17,
    "DeviceFullCode": "360M202M10M17",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M5",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 18,
    "DeviceFullCode": "360M202M10M18",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M5",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 19,
    "DeviceFullCode": "360M202M10M19",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M5",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 20,
    "DeviceFullCode": "360M202M10M20",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M5",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 21,
    "DeviceFullCode": "360M202M10M21",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M5",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 22,
    "DeviceFullCode": "360M202M10M22",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M5",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 23,
    "DeviceFullCode": "360M202M10M23",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M6",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 24,
    "DeviceFullCode": "360M202M10M24",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M6",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 25,
    "DeviceFullCode": "360M202M10M25",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M6",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 26,
    "DeviceFullCode": "360M202M10M26",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M6",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 27,
    "DeviceFullCode": "360M202M10M27",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M6",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 28,
    "DeviceFullCode": "360M202M10M28",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M6",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 29,
    "DeviceFullCode": "360M202M10M29",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M7",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 30,
    "DeviceFullCode": "360M202M10M30",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M7",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 31,
    "DeviceFullCode": "360M202M10M31",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M7",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 32,
    "DeviceFullCode": "360M202M10M32",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M7",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 33,
    "DeviceFullCode": "360M202M10M33",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M7",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 34,
    "DeviceFullCode": "360M202M10M34",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M7",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 35,
    "DeviceFullCode": "360M202M10M35",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M8",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 36,
    "DeviceFullCode": "360M202M10M36",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M8",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 37,
    "DeviceFullCode": "360M202M10M37",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M8",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 38,
    "DeviceFullCode": "360M202M10M38",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M8",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 39,
    "DeviceFullCode": "360M202M10M39",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M8",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 40,
    "DeviceFullCode": "360M202M10M40",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M8",
    "Capacity": 124.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 41,
    "DeviceFullCode": "360M202M10M41",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M9",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 42,
    "DeviceFullCode": "360M202M10M42",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M9",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 43,
    "DeviceFullCode": "360M202M10M43",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M9",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 44,
    "DeviceFullCode": "360M202M10M44",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M9",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 45,
    "DeviceFullCode": "360M202M10M45",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M9",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 46,
    "DeviceFullCode": "360M202M10M46",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M9",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 47,
    "DeviceFullCode": "360M202M10M47",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M10",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 48,
    "DeviceFullCode": "360M202M10M48",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M10",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 49,
    "DeviceFullCode": "360M202M10M49",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M10",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 50,
    "DeviceFullCode": "360M202M10M50",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M10",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 51,
    "DeviceFullCode": "360M202M10M51",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M10",
    "Capacity": 183.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 52,
    "DeviceFullCode": "360M202M10M52",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M10",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 53,
    "DeviceFullCode": "360M202M10M53",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M11",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 54,
    "DeviceFullCode": "360M202M10M54",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M11",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 55,
    "DeviceFullCode": "360M202M10M55",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M11",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 56,
    "DeviceFullCode": "360M202M10M56",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M11",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 57,
    "DeviceFullCode": "360M202M10M57",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M11",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 58,
    "DeviceFullCode": "360M202M10M58",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M11",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 59,
    "DeviceFullCode": "360M202M10M59",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M12",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 60,
    "DeviceFullCode": "360M202M10M60",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M12",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 61,
    "DeviceFullCode": "360M202M10M61",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M12",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 62,
    "DeviceFullCode": "360M202M10M62",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M12",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 63,
    "DeviceFullCode": "360M202M10M63",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M12",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 64,
    "DeviceFullCode": "360M202M10M64",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M12",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 65,
    "DeviceFullCode": "360M202M10M65",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M13",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 66,
    "DeviceFullCode": "360M202M10M66",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M13",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 67,
    "DeviceFullCode": "360M202M10M67",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M13",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 68,
    "DeviceFullCode": "360M202M10M68",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M13",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 69,
    "DeviceFullCode": "360M202M10M69",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M13",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 70,
    "DeviceFullCode": "360M202M10M70",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M13",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 71,
    "DeviceFullCode": "360M202M10M71",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M14",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 72,
    "DeviceFullCode": "360M202M10M72",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M14",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 73,
    "DeviceFullCode": "360M202M10M73",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M14",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 74,
    "DeviceFullCode": "360M202M10M74",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M14",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 75,
    "DeviceFullCode": "360M202M10M75",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M14",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 76,
    "DeviceFullCode": "360M202M10M76",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M14",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 77,
    "DeviceFullCode": "360M202M10M77",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M15",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 78,
    "DeviceFullCode": "360M202M10M78",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M15",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 79,
    "DeviceFullCode": "360M202M10M79",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M15",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 80,
    "DeviceFullCode": "360M202M10M80",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M15",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 81,
    "DeviceFullCode": "360M202M10M81",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M15",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 82,
    "DeviceFullCode": "360M202M10M82",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M15",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 83,
    "DeviceFullCode": "360M202M10M83",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M16",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 84,
    "DeviceFullCode": "360M202M10M84",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M16",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 85,
    "DeviceFullCode": "360M202M10M85",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M16",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 86,
    "DeviceFullCode": "360M202M10M86",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M16",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 87,
    "DeviceFullCode": "360M202M10M87",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M16",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 88,
    "DeviceFullCode": "360M202M10M88",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M16",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 89,
    "DeviceFullCode": "360M202M10M89",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M17",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 90,
    "DeviceFullCode": "360M202M10M90",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M17",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 91,
    "DeviceFullCode": "360M202M10M91",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M17",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 92,
    "DeviceFullCode": "360M202M10M92",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M17",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 93,
    "DeviceFullCode": "360M202M10M93",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M17",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 94,
    "DeviceFullCode": "360M202M10M94",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M17",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 95,
    "DeviceFullCode": "360M202M10M95",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M18",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 96,
    "DeviceFullCode": "360M202M10M96",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M18",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 97,
    "DeviceFullCode": "360M202M10M97",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M18",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 98,
    "DeviceFullCode": "360M202M10M98",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M18",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 99,
    "DeviceFullCode": "360M202M10M99",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M18",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 100,
    "DeviceFullCode": "360M202M10M100",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M18",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 101,
    "DeviceFullCode": "360M202M10M101",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M19",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 102,
    "DeviceFullCode": "360M202M10M102",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M19",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 103,
    "DeviceFullCode": "360M202M10M103",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M19",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 104,
    "DeviceFullCode": "360M202M10M104",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M19",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 105,
    "DeviceFullCode": "360M202M10M105",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M19",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 106,
    "DeviceFullCode": "360M202M10M106",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M19",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 107,
    "DeviceFullCode": "360M202M10M107",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M20",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 108,
    "DeviceFullCode": "360M202M10M108",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M20",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 109,
    "DeviceFullCode": "360M202M10M109",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M20",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 110,
    "DeviceFullCode": "360M202M10M110",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M20",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 111,
    "DeviceFullCode": "360M202M10M111",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M20",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 112,
    "DeviceFullCode": "360M202M10M112",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M20",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 113,
    "DeviceFullCode": "360M202M10M113",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M21",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 114,
    "DeviceFullCode": "360M202M10M114",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M21",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 115,
    "DeviceFullCode": "360M202M10M115",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M21",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 116,
    "DeviceFullCode": "360M202M10M116",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M21",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 117,
    "DeviceFullCode": "360M202M10M117",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M21",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 118,
    "DeviceFullCode": "360M202M10M118",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M21",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 119,
    "DeviceFullCode": "360M202M10M119",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M22",
    "Capacity": 162.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 120,
    "DeviceFullCode": "360M202M10M120",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M22",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 121,
    "DeviceFullCode": "360M202M10M121",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M22",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 122,
    "DeviceFullCode": "360M202M10M122",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M23",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 123,
    "DeviceFullCode": "360M202M10M123",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M23",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 124,
    "DeviceFullCode": "360M202M10M124",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M23",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 125,
    "DeviceFullCode": "360M202M10M125",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M23",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 126,
    "DeviceFullCode": "360M202M10M126",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M23",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 127,
    "DeviceFullCode": "360M202M10M127",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M23",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 128,
    "DeviceFullCode": "360M202M10M128",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M24",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 129,
    "DeviceFullCode": "360M202M10M129",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M24",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 130,
    "DeviceFullCode": "360M202M10M130",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M24",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 131,
    "DeviceFullCode": "360M202M10M131",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M24",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 132,
    "DeviceFullCode": "360M202M10M132",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M24",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 133,
    "DeviceFullCode": "360M202M10M133",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M24",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 134,
    "DeviceFullCode": "360M202M10M134",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M25",
    "Capacity": 178.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 135,
    "DeviceFullCode": "360M202M10M135",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M25",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 136,
    "DeviceFullCode": "360M202M10M136",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M25",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 137,
    "DeviceFullCode": "360M202M10M137",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M25",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 138,
    "DeviceFullCode": "360M202M10M138",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M25",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 139,
    "DeviceFullCode": "360M202M10M139",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M25",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 140,
    "DeviceFullCode": "360M202M10M140",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M26",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 141,
    "DeviceFullCode": "360M202M10M141",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M26",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 142,
    "DeviceFullCode": "360M202M10M142",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M26",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 143,
    "DeviceFullCode": "360M202M10M143",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M26",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 144,
    "DeviceFullCode": "360M202M10M144",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M26",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 145,
    "DeviceFullCode": "360M202M10M145",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M26",
    "Capacity": 124.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 146,
    "DeviceFullCode": "360M202M10M146",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M27",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 147,
    "DeviceFullCode": "360M202M10M147",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M27",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 148,
    "DeviceFullCode": "360M202M10M148",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M27",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 149,
    "DeviceFullCode": "360M202M10M149",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M27",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 150,
    "DeviceFullCode": "360M202M10M150",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M27",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 151,
    "DeviceFullCode": "360M202M10M151",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M27",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 152,
    "DeviceFullCode": "360M202M10M152",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M28",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 153,
    "DeviceFullCode": "360M202M10M153",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M28",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 154,
    "DeviceFullCode": "360M202M10M154",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M28",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 155,
    "DeviceFullCode": "360M202M10M155",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M28",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 156,
    "DeviceFullCode": "360M202M10M156",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M28",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 157,
    "DeviceFullCode": "360M202M10M157",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M28",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 158,
    "DeviceFullCode": "360M202M10M158",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M29",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 159,
    "DeviceFullCode": "360M202M10M159",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M29",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 160,
    "DeviceFullCode": "360M202M10M160",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M29",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 161,
    "DeviceFullCode": "360M202M10M161",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M29",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 162,
    "DeviceFullCode": "360M202M10M162",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M29",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 163,
    "DeviceFullCode": "360M202M10M163",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M29",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 164,
    "DeviceFullCode": "360M202M10M164",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M30",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 165,
    "DeviceFullCode": "360M202M10M165",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M30",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 166,
    "DeviceFullCode": "360M202M10M166",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M30",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 167,
    "DeviceFullCode": "360M202M10M167",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M30",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 168,
    "DeviceFullCode": "360M202M10M168",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M30",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 169,
    "DeviceFullCode": "360M202M10M169",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M30",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 170,
    "DeviceFullCode": "360M202M10M170",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M31",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 171,
    "DeviceFullCode": "360M202M10M171",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M31",
    "Capacity": 189.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 172,
    "DeviceFullCode": "360M202M10M172",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M31",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 173,
    "DeviceFullCode": "360M202M10M173",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M31",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 174,
    "DeviceFullCode": "360M202M10M174",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M31",
    "Capacity": 194.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 10,
    "DeviceCode": 175,
    "DeviceFullCode": "360M202M10M175",
    "DeviceModeFullCode": "360M202M10",
    "PDeviceFullCode": "360M304M18M31",
    "Capacity": 129.6000
  },
  {
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceCode": 1,
    "DeviceFullCode": "360M203M8M1",
    "DeviceModeFullCode": "360M203M8",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 1,
    "DeviceFullCode": "360M206M2M1",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M17",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 2,
    "DeviceFullCode": "360M206M2M2",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M17",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 3,
    "DeviceFullCode": "360M206M2M3",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M17",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 4,
    "DeviceFullCode": "360M206M2M4",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M17",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 5,
    "DeviceFullCode": "360M206M2M5",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M17",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 6,
    "DeviceFullCode": "360M206M2M6",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M17",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 7,
    "DeviceFullCode": "360M206M2M7",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M18",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 8,
    "DeviceFullCode": "360M206M2M8",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M18",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 9,
    "DeviceFullCode": "360M206M2M9",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M18",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 10,
    "DeviceFullCode": "360M206M2M10",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M18",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 11,
    "DeviceFullCode": "360M206M2M11",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M18",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 12,
    "DeviceFullCode": "360M206M2M12",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M18",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 13,
    "DeviceFullCode": "360M206M2M13",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M19",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 14,
    "DeviceFullCode": "360M206M2M14",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M19",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 15,
    "DeviceFullCode": "360M206M2M15",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M19",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 16,
    "DeviceFullCode": "360M206M2M16",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M19",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 17,
    "DeviceFullCode": "360M206M2M17",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M19",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 18,
    "DeviceFullCode": "360M206M2M18",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M19",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 19,
    "DeviceFullCode": "360M206M2M19",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M20",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 20,
    "DeviceFullCode": "360M206M2M20",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M20",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 21,
    "DeviceFullCode": "360M206M2M21",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M20",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 22,
    "DeviceFullCode": "360M206M2M22",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M20",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 23,
    "DeviceFullCode": "360M206M2M23",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M20",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 24,
    "DeviceFullCode": "360M206M2M24",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M20",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 25,
    "DeviceFullCode": "360M206M2M25",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M21",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 26,
    "DeviceFullCode": "360M206M2M26",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M21",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 27,
    "DeviceFullCode": "360M206M2M27",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M21",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 28,
    "DeviceFullCode": "360M206M2M28",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M21",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 29,
    "DeviceFullCode": "360M206M2M29",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M21",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 30,
    "DeviceFullCode": "360M206M2M30",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M21",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 31,
    "DeviceFullCode": "360M206M2M31",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M22",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 32,
    "DeviceFullCode": "360M206M2M32",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M22",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 33,
    "DeviceFullCode": "360M206M2M33",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M22",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 34,
    "DeviceFullCode": "360M206M2M34",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M22",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 35,
    "DeviceFullCode": "360M206M2M35",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M23",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 36,
    "DeviceFullCode": "360M206M2M36",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M23",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 37,
    "DeviceFullCode": "360M206M2M37",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M23",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 38,
    "DeviceFullCode": "360M206M2M38",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M23",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 39,
    "DeviceFullCode": "360M206M2M39",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M23",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 40,
    "DeviceFullCode": "360M206M2M40",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M23",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 41,
    "DeviceFullCode": "360M206M2M41",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M24",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 42,
    "DeviceFullCode": "360M206M2M42",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M24",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 43,
    "DeviceFullCode": "360M206M2M43",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M24",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 44,
    "DeviceFullCode": "360M206M2M44",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M24",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 45,
    "DeviceFullCode": "360M206M2M45",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M24",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 46,
    "DeviceFullCode": "360M206M2M46",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M24",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 47,
    "DeviceFullCode": "360M206M2M47",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M25",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 48,
    "DeviceFullCode": "360M206M2M48",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M25",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 49,
    "DeviceFullCode": "360M206M2M49",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M25",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 50,
    "DeviceFullCode": "360M206M2M50",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M25",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 51,
    "DeviceFullCode": "360M206M2M51",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M25",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 52,
    "DeviceFullCode": "360M206M2M52",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M25",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 53,
    "DeviceFullCode": "360M206M2M53",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M26",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 54,
    "DeviceFullCode": "360M206M2M54",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M26",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 55,
    "DeviceFullCode": "360M206M2M55",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M26",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 56,
    "DeviceFullCode": "360M206M2M56",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M26",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 57,
    "DeviceFullCode": "360M206M2M57",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M26",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 58,
    "DeviceFullCode": "360M206M2M58",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M26",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 59,
    "DeviceFullCode": "360M206M2M59",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M27",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 60,
    "DeviceFullCode": "360M206M2M60",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M27",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 61,
    "DeviceFullCode": "360M206M2M61",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M27",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 62,
    "DeviceFullCode": "360M206M2M62",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M27",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 63,
    "DeviceFullCode": "360M206M2M63",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M27",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 64,
    "DeviceFullCode": "360M206M2M64",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M27",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 65,
    "DeviceFullCode": "360M206M2M65",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M28",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 66,
    "DeviceFullCode": "360M206M2M66",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M28",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 67,
    "DeviceFullCode": "360M206M2M67",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M28",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 68,
    "DeviceFullCode": "360M206M2M68",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M28",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 69,
    "DeviceFullCode": "360M206M2M69",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M29",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 70,
    "DeviceFullCode": "360M206M2M70",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M29",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 71,
    "DeviceFullCode": "360M206M2M71",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M29",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 72,
    "DeviceFullCode": "360M206M2M72",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M29",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 73,
    "DeviceFullCode": "360M206M2M73",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M29",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 74,
    "DeviceFullCode": "360M206M2M74",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M29",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 75,
    "DeviceFullCode": "360M206M2M75",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M30",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 76,
    "DeviceFullCode": "360M206M2M76",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M30",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 77,
    "DeviceFullCode": "360M206M2M77",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M30",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 78,
    "DeviceFullCode": "360M206M2M78",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M30",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 79,
    "DeviceFullCode": "360M206M2M79",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M30",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 80,
    "DeviceFullCode": "360M206M2M80",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M30",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 81,
    "DeviceFullCode": "360M206M2M81",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M31",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 82,
    "DeviceFullCode": "360M206M2M82",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M31",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 83,
    "DeviceFullCode": "360M206M2M83",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M31",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 84,
    "DeviceFullCode": "360M206M2M84",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M31",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 85,
    "DeviceFullCode": "360M206M2M85",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M31",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 86,
    "DeviceFullCode": "360M206M2M86",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M31",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 87,
    "DeviceFullCode": "360M206M2M87",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M32",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 88,
    "DeviceFullCode": "360M206M2M88",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M32",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 89,
    "DeviceFullCode": "360M206M2M89",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M32",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 90,
    "DeviceFullCode": "360M206M2M90",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M32",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 91,
    "DeviceFullCode": "360M206M2M91",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M32",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 92,
    "DeviceFullCode": "360M206M2M92",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M32",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 93,
    "DeviceFullCode": "360M206M2M93",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M33",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 94,
    "DeviceFullCode": "360M206M2M94",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M33",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 95,
    "DeviceFullCode": "360M206M2M95",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M33",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 96,
    "DeviceFullCode": "360M206M2M96",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M33",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 97,
    "DeviceFullCode": "360M206M2M97",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M33",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 98,
    "DeviceFullCode": "360M206M2M98",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M33",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 99,
    "DeviceFullCode": "360M206M2M99",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M34",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 100,
    "DeviceFullCode": "360M206M2M100",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M34",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 101,
    "DeviceFullCode": "360M206M2M101",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M34",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 102,
    "DeviceFullCode": "360M206M2M102",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M34",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 103,
    "DeviceFullCode": "360M206M2M103",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M35",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 104,
    "DeviceFullCode": "360M206M2M104",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M35",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 105,
    "DeviceFullCode": "360M206M2M105",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M35",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 106,
    "DeviceFullCode": "360M206M2M106",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M35",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 107,
    "DeviceFullCode": "360M206M2M107",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M35",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 108,
    "DeviceFullCode": "360M206M2M108",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M35",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 109,
    "DeviceFullCode": "360M206M2M109",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M36",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 110,
    "DeviceFullCode": "360M206M2M110",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M36",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 111,
    "DeviceFullCode": "360M206M2M111",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M36",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 112,
    "DeviceFullCode": "360M206M2M112",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M36",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 113,
    "DeviceFullCode": "360M206M2M113",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M36",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 114,
    "DeviceFullCode": "360M206M2M114",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M36",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 115,
    "DeviceFullCode": "360M206M2M115",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M37",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 116,
    "DeviceFullCode": "360M206M2M116",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M37",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 117,
    "DeviceFullCode": "360M206M2M117",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M37",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 118,
    "DeviceFullCode": "360M206M2M118",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M37",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 119,
    "DeviceFullCode": "360M206M2M119",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M37",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 120,
    "DeviceFullCode": "360M206M2M120",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M37",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 121,
    "DeviceFullCode": "360M206M2M121",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M38",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 122,
    "DeviceFullCode": "360M206M2M122",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M38",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 123,
    "DeviceFullCode": "360M206M2M123",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M38",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 124,
    "DeviceFullCode": "360M206M2M124",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M38",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 125,
    "DeviceFullCode": "360M206M2M125",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M38",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 126,
    "DeviceFullCode": "360M206M2M126",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M38",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 127,
    "DeviceFullCode": "360M206M2M127",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M39",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 128,
    "DeviceFullCode": "360M206M2M128",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M39",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 129,
    "DeviceFullCode": "360M206M2M129",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M39",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 130,
    "DeviceFullCode": "360M206M2M130",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M39",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 131,
    "DeviceFullCode": "360M206M2M131",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M39",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 132,
    "DeviceFullCode": "360M206M2M132",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M39",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 133,
    "DeviceFullCode": "360M206M2M133",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M40",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 134,
    "DeviceFullCode": "360M206M2M134",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M40",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 135,
    "DeviceFullCode": "360M206M2M135",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M40",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 136,
    "DeviceFullCode": "360M206M2M136",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M40",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 137,
    "DeviceFullCode": "360M206M2M137",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M41",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 138,
    "DeviceFullCode": "360M206M2M138",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M41",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 139,
    "DeviceFullCode": "360M206M2M139",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M41",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 140,
    "DeviceFullCode": "360M206M2M140",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M41",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 141,
    "DeviceFullCode": "360M206M2M141",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M41",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 142,
    "DeviceFullCode": "360M206M2M142",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M41",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 143,
    "DeviceFullCode": "360M206M2M143",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M42",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 144,
    "DeviceFullCode": "360M206M2M144",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M42",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 145,
    "DeviceFullCode": "360M206M2M145",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M42",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 146,
    "DeviceFullCode": "360M206M2M146",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M42",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 147,
    "DeviceFullCode": "360M206M2M147",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M42",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 148,
    "DeviceFullCode": "360M206M2M148",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M42",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 149,
    "DeviceFullCode": "360M206M2M149",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M43",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 150,
    "DeviceFullCode": "360M206M2M150",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M43",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 151,
    "DeviceFullCode": "360M206M2M151",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M43",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 152,
    "DeviceFullCode": "360M206M2M152",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M43",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 153,
    "DeviceFullCode": "360M206M2M153",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M43",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 154,
    "DeviceFullCode": "360M206M2M154",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M43",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 155,
    "DeviceFullCode": "360M206M2M155",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M44",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 156,
    "DeviceFullCode": "360M206M2M156",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M44",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 157,
    "DeviceFullCode": "360M206M2M157",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M44",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 158,
    "DeviceFullCode": "360M206M2M158",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M44",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 159,
    "DeviceFullCode": "360M206M2M159",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M44",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 160,
    "DeviceFullCode": "360M206M2M160",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M44",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 161,
    "DeviceFullCode": "360M206M2M161",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M45",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 162,
    "DeviceFullCode": "360M206M2M162",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M45",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 163,
    "DeviceFullCode": "360M206M2M163",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M45",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 164,
    "DeviceFullCode": "360M206M2M164",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M45",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 165,
    "DeviceFullCode": "360M206M2M165",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M45",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 166,
    "DeviceFullCode": "360M206M2M166",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M45",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 167,
    "DeviceFullCode": "360M206M2M167",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M46",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 168,
    "DeviceFullCode": "360M206M2M168",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M46",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 169,
    "DeviceFullCode": "360M206M2M169",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M46",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 170,
    "DeviceFullCode": "360M206M2M170",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M46",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 171,
    "DeviceFullCode": "360M206M2M171",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M47",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 172,
    "DeviceFullCode": "360M206M2M172",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M47",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 173,
    "DeviceFullCode": "360M206M2M173",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M47",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 174,
    "DeviceFullCode": "360M206M2M174",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M47",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 175,
    "DeviceFullCode": "360M206M2M175",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M47",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 176,
    "DeviceFullCode": "360M206M2M176",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M47",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 177,
    "DeviceFullCode": "360M206M2M177",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M48",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 178,
    "DeviceFullCode": "360M206M2M178",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M48",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 179,
    "DeviceFullCode": "360M206M2M179",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M48",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 180,
    "DeviceFullCode": "360M206M2M180",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M48",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 181,
    "DeviceFullCode": "360M206M2M181",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M48",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 182,
    "DeviceFullCode": "360M206M2M182",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M48",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 183,
    "DeviceFullCode": "360M206M2M183",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M49",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 184,
    "DeviceFullCode": "360M206M2M184",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M49",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 185,
    "DeviceFullCode": "360M206M2M185",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M49",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 186,
    "DeviceFullCode": "360M206M2M186",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M49",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 187,
    "DeviceFullCode": "360M206M2M187",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M49",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 188,
    "DeviceFullCode": "360M206M2M188",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M49",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 189,
    "DeviceFullCode": "360M206M2M189",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M50",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 190,
    "DeviceFullCode": "360M206M2M190",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M50",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 191,
    "DeviceFullCode": "360M206M2M191",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M50",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 192,
    "DeviceFullCode": "360M206M2M192",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M50",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 193,
    "DeviceFullCode": "360M206M2M193",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M50",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 194,
    "DeviceFullCode": "360M206M2M194",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M50",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 195,
    "DeviceFullCode": "360M206M2M195",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M51",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 196,
    "DeviceFullCode": "360M206M2M196",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M51",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 197,
    "DeviceFullCode": "360M206M2M197",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M51",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 198,
    "DeviceFullCode": "360M206M2M198",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M51",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 199,
    "DeviceFullCode": "360M206M2M199",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M51",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 200,
    "DeviceFullCode": "360M206M2M200",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M51",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 201,
    "DeviceFullCode": "360M206M2M201",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M52",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 202,
    "DeviceFullCode": "360M206M2M202",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M52",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 203,
    "DeviceFullCode": "360M206M2M203",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M52",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 204,
    "DeviceFullCode": "360M206M2M204",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M52",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 205,
    "DeviceFullCode": "360M206M2M205",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M53",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 206,
    "DeviceFullCode": "360M206M2M206",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M53",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 207,
    "DeviceFullCode": "360M206M2M207",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M53",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 208,
    "DeviceFullCode": "360M206M2M208",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M53",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 209,
    "DeviceFullCode": "360M206M2M209",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M53",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 210,
    "DeviceFullCode": "360M206M2M210",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M53",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 211,
    "DeviceFullCode": "360M206M2M211",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M54",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 212,
    "DeviceFullCode": "360M206M2M212",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M54",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 213,
    "DeviceFullCode": "360M206M2M213",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M54",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 214,
    "DeviceFullCode": "360M206M2M214",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M54",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 215,
    "DeviceFullCode": "360M206M2M215",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M54",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 216,
    "DeviceFullCode": "360M206M2M216",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M54",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 217,
    "DeviceFullCode": "360M206M2M217",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M55",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 218,
    "DeviceFullCode": "360M206M2M218",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M55",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 219,
    "DeviceFullCode": "360M206M2M219",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M55",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 220,
    "DeviceFullCode": "360M206M2M220",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M55",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 221,
    "DeviceFullCode": "360M206M2M221",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M55",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 222,
    "DeviceFullCode": "360M206M2M222",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M55",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 223,
    "DeviceFullCode": "360M206M2M223",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M56",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 224,
    "DeviceFullCode": "360M206M2M224",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M56",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 225,
    "DeviceFullCode": "360M206M2M225",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M56",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 226,
    "DeviceFullCode": "360M206M2M226",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M56",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 227,
    "DeviceFullCode": "360M206M2M227",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M56",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 228,
    "DeviceFullCode": "360M206M2M228",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M56",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 229,
    "DeviceFullCode": "360M206M2M229",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M57",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 230,
    "DeviceFullCode": "360M206M2M230",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M57",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 231,
    "DeviceFullCode": "360M206M2M231",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M57",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 232,
    "DeviceFullCode": "360M206M2M232",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M57",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 233,
    "DeviceFullCode": "360M206M2M233",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M57",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 234,
    "DeviceFullCode": "360M206M2M234",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M57",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 235,
    "DeviceFullCode": "360M206M2M235",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M58",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 236,
    "DeviceFullCode": "360M206M2M236",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M58",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 237,
    "DeviceFullCode": "360M206M2M237",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M58",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 238,
    "DeviceFullCode": "360M206M2M238",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M58",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 239,
    "DeviceFullCode": "360M206M2M239",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M59",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 240,
    "DeviceFullCode": "360M206M2M240",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M59",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 241,
    "DeviceFullCode": "360M206M2M241",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M59",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 242,
    "DeviceFullCode": "360M206M2M242",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M59",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 243,
    "DeviceFullCode": "360M206M2M243",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M59",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 244,
    "DeviceFullCode": "360M206M2M244",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M59",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 245,
    "DeviceFullCode": "360M206M2M245",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M60",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 246,
    "DeviceFullCode": "360M206M2M246",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M60",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 247,
    "DeviceFullCode": "360M206M2M247",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M60",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 248,
    "DeviceFullCode": "360M206M2M248",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M60",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 249,
    "DeviceFullCode": "360M206M2M249",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M60",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 250,
    "DeviceFullCode": "360M206M2M250",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M60",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 251,
    "DeviceFullCode": "360M206M2M251",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M61",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 252,
    "DeviceFullCode": "360M206M2M252",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M61",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 253,
    "DeviceFullCode": "360M206M2M253",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M61",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 254,
    "DeviceFullCode": "360M206M2M254",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M61",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 255,
    "DeviceFullCode": "360M206M2M255",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M61",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 256,
    "DeviceFullCode": "360M206M2M256",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M61",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 257,
    "DeviceFullCode": "360M206M2M257",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M62",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 258,
    "DeviceFullCode": "360M206M2M258",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M62",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 259,
    "DeviceFullCode": "360M206M2M259",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M62",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 260,
    "DeviceFullCode": "360M206M2M260",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M62",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 261,
    "DeviceFullCode": "360M206M2M261",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M62",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 262,
    "DeviceFullCode": "360M206M2M262",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M62",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 263,
    "DeviceFullCode": "360M206M2M263",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M63",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 264,
    "DeviceFullCode": "360M206M2M264",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M63",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 265,
    "DeviceFullCode": "360M206M2M265",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M63",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 266,
    "DeviceFullCode": "360M206M2M266",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M63",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 267,
    "DeviceFullCode": "360M206M2M267",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M63",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 268,
    "DeviceFullCode": "360M206M2M268",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M63",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 269,
    "DeviceFullCode": "360M206M2M269",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M64",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 270,
    "DeviceFullCode": "360M206M2M270",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M64",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 271,
    "DeviceFullCode": "360M206M2M271",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M64",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 272,
    "DeviceFullCode": "360M206M2M272",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M64",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 273,
    "DeviceFullCode": "360M206M2M273",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M65",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 274,
    "DeviceFullCode": "360M206M2M274",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M65",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 275,
    "DeviceFullCode": "360M206M2M275",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M65",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 276,
    "DeviceFullCode": "360M206M2M276",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M65",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 277,
    "DeviceFullCode": "360M206M2M277",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M65",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 278,
    "DeviceFullCode": "360M206M2M278",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M65",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 279,
    "DeviceFullCode": "360M206M2M279",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M66",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 280,
    "DeviceFullCode": "360M206M2M280",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M66",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 281,
    "DeviceFullCode": "360M206M2M281",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M66",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 282,
    "DeviceFullCode": "360M206M2M282",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M66",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 283,
    "DeviceFullCode": "360M206M2M283",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M66",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 284,
    "DeviceFullCode": "360M206M2M284",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M66",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 285,
    "DeviceFullCode": "360M206M2M285",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M67",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 286,
    "DeviceFullCode": "360M206M2M286",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M67",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 287,
    "DeviceFullCode": "360M206M2M287",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M67",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 288,
    "DeviceFullCode": "360M206M2M288",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M67",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 289,
    "DeviceFullCode": "360M206M2M289",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M67",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 290,
    "DeviceFullCode": "360M206M2M290",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M67",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 291,
    "DeviceFullCode": "360M206M2M291",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M68",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 292,
    "DeviceFullCode": "360M206M2M292",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M68",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 293,
    "DeviceFullCode": "360M206M2M293",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M68",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 294,
    "DeviceFullCode": "360M206M2M294",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M68",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 295,
    "DeviceFullCode": "360M206M2M295",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M68",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 296,
    "DeviceFullCode": "360M206M2M296",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M68",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 297,
    "DeviceFullCode": "360M206M2M297",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M69",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 298,
    "DeviceFullCode": "360M206M2M298",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M69",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 299,
    "DeviceFullCode": "360M206M2M299",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M69",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 300,
    "DeviceFullCode": "360M206M2M300",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M69",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 301,
    "DeviceFullCode": "360M206M2M301",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M69",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 302,
    "DeviceFullCode": "360M206M2M302",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M69",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 303,
    "DeviceFullCode": "360M206M2M303",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M70",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 304,
    "DeviceFullCode": "360M206M2M304",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M70",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 305,
    "DeviceFullCode": "360M206M2M305",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M70",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 306,
    "DeviceFullCode": "360M206M2M306",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M70",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 307,
    "DeviceFullCode": "360M206M2M307",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M71",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 308,
    "DeviceFullCode": "360M206M2M308",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M71",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 309,
    "DeviceFullCode": "360M206M2M309",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M71",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 310,
    "DeviceFullCode": "360M206M2M310",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M71",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 311,
    "DeviceFullCode": "360M206M2M311",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M71",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 312,
    "DeviceFullCode": "360M206M2M312",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M71",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 313,
    "DeviceFullCode": "360M206M2M313",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M72",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 314,
    "DeviceFullCode": "360M206M2M314",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M72",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 315,
    "DeviceFullCode": "360M206M2M315",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M72",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 316,
    "DeviceFullCode": "360M206M2M316",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M72",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 317,
    "DeviceFullCode": "360M206M2M317",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M72",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 318,
    "DeviceFullCode": "360M206M2M318",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M72",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 319,
    "DeviceFullCode": "360M206M2M319",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M73",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 320,
    "DeviceFullCode": "360M206M2M320",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M73",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 321,
    "DeviceFullCode": "360M206M2M321",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M73",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 322,
    "DeviceFullCode": "360M206M2M322",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M73",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 323,
    "DeviceFullCode": "360M206M2M323",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M73",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 324,
    "DeviceFullCode": "360M206M2M324",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M73",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 325,
    "DeviceFullCode": "360M206M2M325",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M74",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 326,
    "DeviceFullCode": "360M206M2M326",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M74",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 327,
    "DeviceFullCode": "360M206M2M327",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M74",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 328,
    "DeviceFullCode": "360M206M2M328",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M74",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 329,
    "DeviceFullCode": "360M206M2M329",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M74",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 330,
    "DeviceFullCode": "360M206M2M330",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M74",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 331,
    "DeviceFullCode": "360M206M2M331",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M75",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 332,
    "DeviceFullCode": "360M206M2M332",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M75",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 333,
    "DeviceFullCode": "360M206M2M333",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M75",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 334,
    "DeviceFullCode": "360M206M2M334",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M75",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 335,
    "DeviceFullCode": "360M206M2M335",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M75",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 336,
    "DeviceFullCode": "360M206M2M336",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M75",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 337,
    "DeviceFullCode": "360M206M2M337",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M76",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 338,
    "DeviceFullCode": "360M206M2M338",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M76",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 339,
    "DeviceFullCode": "360M206M2M339",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M76",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 340,
    "DeviceFullCode": "360M206M2M340",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M76",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 341,
    "DeviceFullCode": "360M206M2M341",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M77",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 342,
    "DeviceFullCode": "360M206M2M342",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M77",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 343,
    "DeviceFullCode": "360M206M2M343",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M77",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 344,
    "DeviceFullCode": "360M206M2M344",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M77",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 345,
    "DeviceFullCode": "360M206M2M345",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M77",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 346,
    "DeviceFullCode": "360M206M2M346",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M77",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 347,
    "DeviceFullCode": "360M206M2M347",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M78",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 348,
    "DeviceFullCode": "360M206M2M348",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M78",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 349,
    "DeviceFullCode": "360M206M2M349",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M78",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 350,
    "DeviceFullCode": "360M206M2M350",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M78",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 351,
    "DeviceFullCode": "360M206M2M351",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M78",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 352,
    "DeviceFullCode": "360M206M2M352",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M78",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 353,
    "DeviceFullCode": "360M206M2M353",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M79",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 354,
    "DeviceFullCode": "360M206M2M354",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M79",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 355,
    "DeviceFullCode": "360M206M2M355",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M79",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 356,
    "DeviceFullCode": "360M206M2M356",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M79",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 357,
    "DeviceFullCode": "360M206M2M357",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M79",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 358,
    "DeviceFullCode": "360M206M2M358",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M79",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 359,
    "DeviceFullCode": "360M206M2M359",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M80",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 360,
    "DeviceFullCode": "360M206M2M360",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M80",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 361,
    "DeviceFullCode": "360M206M2M361",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M80",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 362,
    "DeviceFullCode": "360M206M2M362",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M80",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 363,
    "DeviceFullCode": "360M206M2M363",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M80",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 364,
    "DeviceFullCode": "360M206M2M364",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M80",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 365,
    "DeviceFullCode": "360M206M2M365",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M81",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 366,
    "DeviceFullCode": "360M206M2M366",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M81",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 367,
    "DeviceFullCode": "360M206M2M367",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M81",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 368,
    "DeviceFullCode": "360M206M2M368",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M81",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 369,
    "DeviceFullCode": "360M206M2M369",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M81",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 370,
    "DeviceFullCode": "360M206M2M370",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M81",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 371,
    "DeviceFullCode": "360M206M2M371",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M82",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 372,
    "DeviceFullCode": "360M206M2M372",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M82",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 373,
    "DeviceFullCode": "360M206M2M373",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M82",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 374,
    "DeviceFullCode": "360M206M2M374",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M82",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 375,
    "DeviceFullCode": "360M206M2M375",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M83",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 376,
    "DeviceFullCode": "360M206M2M376",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M83",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 377,
    "DeviceFullCode": "360M206M2M377",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M83",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 378,
    "DeviceFullCode": "360M206M2M378",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M83",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 379,
    "DeviceFullCode": "360M206M2M379",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M83",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 380,
    "DeviceFullCode": "360M206M2M380",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M83",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 381,
    "DeviceFullCode": "360M206M2M381",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M84",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 382,
    "DeviceFullCode": "360M206M2M382",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M84",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 383,
    "DeviceFullCode": "360M206M2M383",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M84",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 384,
    "DeviceFullCode": "360M206M2M384",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M84",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 385,
    "DeviceFullCode": "360M206M2M385",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M84",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 386,
    "DeviceFullCode": "360M206M2M386",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M84",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 387,
    "DeviceFullCode": "360M206M2M387",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M85",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 388,
    "DeviceFullCode": "360M206M2M388",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M85",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 389,
    "DeviceFullCode": "360M206M2M389",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M85",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 390,
    "DeviceFullCode": "360M206M2M390",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M85",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 391,
    "DeviceFullCode": "360M206M2M391",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M85",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 392,
    "DeviceFullCode": "360M206M2M392",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M85",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 393,
    "DeviceFullCode": "360M206M2M393",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M86",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 394,
    "DeviceFullCode": "360M206M2M394",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M86",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 395,
    "DeviceFullCode": "360M206M2M395",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M86",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 396,
    "DeviceFullCode": "360M206M2M396",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M86",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 397,
    "DeviceFullCode": "360M206M2M397",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M86",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 398,
    "DeviceFullCode": "360M206M2M398",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M86",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 399,
    "DeviceFullCode": "360M206M2M399",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M87",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 400,
    "DeviceFullCode": "360M206M2M400",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M87",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 401,
    "DeviceFullCode": "360M206M2M401",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M87",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 402,
    "DeviceFullCode": "360M206M2M402",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M87",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 403,
    "DeviceFullCode": "360M206M2M403",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M87",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 404,
    "DeviceFullCode": "360M206M2M404",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M87",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 405,
    "DeviceFullCode": "360M206M2M405",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M88",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 406,
    "DeviceFullCode": "360M206M2M406",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M88",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 407,
    "DeviceFullCode": "360M206M2M407",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M88",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 408,
    "DeviceFullCode": "360M206M2M408",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M88",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 409,
    "DeviceFullCode": "360M206M2M409",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M89",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 410,
    "DeviceFullCode": "360M206M2M410",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M89",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 411,
    "DeviceFullCode": "360M206M2M411",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M89",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 412,
    "DeviceFullCode": "360M206M2M412",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M89",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 413,
    "DeviceFullCode": "360M206M2M413",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M89",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 414,
    "DeviceFullCode": "360M206M2M414",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M89",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 415,
    "DeviceFullCode": "360M206M2M415",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M90",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 416,
    "DeviceFullCode": "360M206M2M416",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M90",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 417,
    "DeviceFullCode": "360M206M2M417",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M90",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 418,
    "DeviceFullCode": "360M206M2M418",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M90",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 419,
    "DeviceFullCode": "360M206M2M419",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M90",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 420,
    "DeviceFullCode": "360M206M2M420",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M90",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 421,
    "DeviceFullCode": "360M206M2M421",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M91",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 422,
    "DeviceFullCode": "360M206M2M422",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M91",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 423,
    "DeviceFullCode": "360M206M2M423",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M91",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 424,
    "DeviceFullCode": "360M206M2M424",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M91",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 425,
    "DeviceFullCode": "360M206M2M425",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M91",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 426,
    "DeviceFullCode": "360M206M2M426",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M91",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 427,
    "DeviceFullCode": "360M206M2M427",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M92",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 428,
    "DeviceFullCode": "360M206M2M428",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M92",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 429,
    "DeviceFullCode": "360M206M2M429",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M92",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 430,
    "DeviceFullCode": "360M206M2M430",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M92",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 431,
    "DeviceFullCode": "360M206M2M431",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M92",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 432,
    "DeviceFullCode": "360M206M2M432",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M92",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 433,
    "DeviceFullCode": "360M206M2M433",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M93",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 434,
    "DeviceFullCode": "360M206M2M434",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M93",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 435,
    "DeviceFullCode": "360M206M2M435",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M93",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 436,
    "DeviceFullCode": "360M206M2M436",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M93",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 437,
    "DeviceFullCode": "360M206M2M437",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M93",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 438,
    "DeviceFullCode": "360M206M2M438",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M93",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 439,
    "DeviceFullCode": "360M206M2M439",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M94",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 440,
    "DeviceFullCode": "360M206M2M440",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M94",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 441,
    "DeviceFullCode": "360M206M2M441",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M94",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 442,
    "DeviceFullCode": "360M206M2M442",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M94",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 443,
    "DeviceFullCode": "360M206M2M443",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M95",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 444,
    "DeviceFullCode": "360M206M2M444",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M95",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 445,
    "DeviceFullCode": "360M206M2M445",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M95",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 446,
    "DeviceFullCode": "360M206M2M446",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M95",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 447,
    "DeviceFullCode": "360M206M2M447",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M95",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 448,
    "DeviceFullCode": "360M206M2M448",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M95",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 449,
    "DeviceFullCode": "360M206M2M449",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M96",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 450,
    "DeviceFullCode": "360M206M2M450",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M96",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 451,
    "DeviceFullCode": "360M206M2M451",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M96",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 452,
    "DeviceFullCode": "360M206M2M452",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M96",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 453,
    "DeviceFullCode": "360M206M2M453",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M96",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 454,
    "DeviceFullCode": "360M206M2M454",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M96",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 455,
    "DeviceFullCode": "360M206M2M455",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M97",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 456,
    "DeviceFullCode": "360M206M2M456",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M97",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 457,
    "DeviceFullCode": "360M206M2M457",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M97",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 458,
    "DeviceFullCode": "360M206M2M458",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M97",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 459,
    "DeviceFullCode": "360M206M2M459",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M97",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 460,
    "DeviceFullCode": "360M206M2M460",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M97",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 461,
    "DeviceFullCode": "360M206M2M461",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M98",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 462,
    "DeviceFullCode": "360M206M2M462",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M98",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 463,
    "DeviceFullCode": "360M206M2M463",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M98",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 464,
    "DeviceFullCode": "360M206M2M464",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M98",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 465,
    "DeviceFullCode": "360M206M2M465",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M98",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 466,
    "DeviceFullCode": "360M206M2M466",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M98",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 467,
    "DeviceFullCode": "360M206M2M467",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M99",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 468,
    "DeviceFullCode": "360M206M2M468",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M99",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 469,
    "DeviceFullCode": "360M206M2M469",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M99",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 470,
    "DeviceFullCode": "360M206M2M470",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M99",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 471,
    "DeviceFullCode": "360M206M2M471",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M99",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 472,
    "DeviceFullCode": "360M206M2M472",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M99",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 473,
    "DeviceFullCode": "360M206M2M473",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M100",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 474,
    "DeviceFullCode": "360M206M2M474",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M100",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 475,
    "DeviceFullCode": "360M206M2M475",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M100",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 476,
    "DeviceFullCode": "360M206M2M476",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M100",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 477,
    "DeviceFullCode": "360M206M2M477",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M101",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 478,
    "DeviceFullCode": "360M206M2M478",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M101",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 479,
    "DeviceFullCode": "360M206M2M479",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M101",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 480,
    "DeviceFullCode": "360M206M2M480",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M101",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 481,
    "DeviceFullCode": "360M206M2M481",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M101",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 482,
    "DeviceFullCode": "360M206M2M482",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M101",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 483,
    "DeviceFullCode": "360M206M2M483",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M102",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 484,
    "DeviceFullCode": "360M206M2M484",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M102",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 485,
    "DeviceFullCode": "360M206M2M485",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M102",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 486,
    "DeviceFullCode": "360M206M2M486",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M102",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 487,
    "DeviceFullCode": "360M206M2M487",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M102",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 488,
    "DeviceFullCode": "360M206M2M488",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M102",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 489,
    "DeviceFullCode": "360M206M2M489",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M103",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 490,
    "DeviceFullCode": "360M206M2M490",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M103",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 491,
    "DeviceFullCode": "360M206M2M491",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M103",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 492,
    "DeviceFullCode": "360M206M2M492",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M103",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 493,
    "DeviceFullCode": "360M206M2M493",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M103",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 494,
    "DeviceFullCode": "360M206M2M494",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M103",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 495,
    "DeviceFullCode": "360M206M2M495",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M104",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 496,
    "DeviceFullCode": "360M206M2M496",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M104",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 497,
    "DeviceFullCode": "360M206M2M497",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M104",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 498,
    "DeviceFullCode": "360M206M2M498",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M104",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 499,
    "DeviceFullCode": "360M206M2M499",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M104",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 500,
    "DeviceFullCode": "360M206M2M500",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M104",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 501,
    "DeviceFullCode": "360M206M2M501",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M105",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 502,
    "DeviceFullCode": "360M206M2M502",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M105",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 503,
    "DeviceFullCode": "360M206M2M503",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M105",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 504,
    "DeviceFullCode": "360M206M2M504",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M105",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 505,
    "DeviceFullCode": "360M206M2M505",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M105",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 506,
    "DeviceFullCode": "360M206M2M506",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M105",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 507,
    "DeviceFullCode": "360M206M2M507",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M106",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 508,
    "DeviceFullCode": "360M206M2M508",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M106",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 509,
    "DeviceFullCode": "360M206M2M509",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M106",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 510,
    "DeviceFullCode": "360M206M2M510",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M106",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 511,
    "DeviceFullCode": "360M206M2M511",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M107",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 512,
    "DeviceFullCode": "360M206M2M512",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M107",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 513,
    "DeviceFullCode": "360M206M2M513",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M107",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 514,
    "DeviceFullCode": "360M206M2M514",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M107",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 515,
    "DeviceFullCode": "360M206M2M515",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M107",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 516,
    "DeviceFullCode": "360M206M2M516",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M107",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 517,
    "DeviceFullCode": "360M206M2M517",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M108",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 518,
    "DeviceFullCode": "360M206M2M518",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M108",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 519,
    "DeviceFullCode": "360M206M2M519",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M108",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 520,
    "DeviceFullCode": "360M206M2M520",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M108",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 521,
    "DeviceFullCode": "360M206M2M521",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M108",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 522,
    "DeviceFullCode": "360M206M2M522",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M108",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 523,
    "DeviceFullCode": "360M206M2M523",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M109",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 524,
    "DeviceFullCode": "360M206M2M524",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M109",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 525,
    "DeviceFullCode": "360M206M2M525",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M109",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 526,
    "DeviceFullCode": "360M206M2M526",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M109",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 527,
    "DeviceFullCode": "360M206M2M527",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M109",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 528,
    "DeviceFullCode": "360M206M2M528",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M109",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 529,
    "DeviceFullCode": "360M206M2M529",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M110",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 530,
    "DeviceFullCode": "360M206M2M530",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M110",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 531,
    "DeviceFullCode": "360M206M2M531",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M110",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 532,
    "DeviceFullCode": "360M206M2M532",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M110",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 533,
    "DeviceFullCode": "360M206M2M533",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M110",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 534,
    "DeviceFullCode": "360M206M2M534",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M110",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 535,
    "DeviceFullCode": "360M206M2M535",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M111",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 536,
    "DeviceFullCode": "360M206M2M536",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M111",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 537,
    "DeviceFullCode": "360M206M2M537",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M111",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 538,
    "DeviceFullCode": "360M206M2M538",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M111",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 539,
    "DeviceFullCode": "360M206M2M539",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M111",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 540,
    "DeviceFullCode": "360M206M2M540",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M111",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 541,
    "DeviceFullCode": "360M206M2M541",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M112",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 542,
    "DeviceFullCode": "360M206M2M542",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M112",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 543,
    "DeviceFullCode": "360M206M2M543",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M112",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 544,
    "DeviceFullCode": "360M206M2M544",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M112",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 545,
    "DeviceFullCode": "360M206M2M545",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M113",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 546,
    "DeviceFullCode": "360M206M2M546",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M113",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 547,
    "DeviceFullCode": "360M206M2M547",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M113",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 548,
    "DeviceFullCode": "360M206M2M548",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M113",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 549,
    "DeviceFullCode": "360M206M2M549",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M113",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 550,
    "DeviceFullCode": "360M206M2M550",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M113",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 551,
    "DeviceFullCode": "360M206M2M551",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M114",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 552,
    "DeviceFullCode": "360M206M2M552",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M114",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 553,
    "DeviceFullCode": "360M206M2M553",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M114",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 554,
    "DeviceFullCode": "360M206M2M554",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M114",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 555,
    "DeviceFullCode": "360M206M2M555",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M114",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 556,
    "DeviceFullCode": "360M206M2M556",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M114",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 557,
    "DeviceFullCode": "360M206M2M557",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M115",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 558,
    "DeviceFullCode": "360M206M2M558",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M115",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 559,
    "DeviceFullCode": "360M206M2M559",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M115",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 560,
    "DeviceFullCode": "360M206M2M560",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M115",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 561,
    "DeviceFullCode": "360M206M2M561",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M115",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 562,
    "DeviceFullCode": "360M206M2M562",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M115",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 563,
    "DeviceFullCode": "360M206M2M563",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M116",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 564,
    "DeviceFullCode": "360M206M2M564",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M116",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 565,
    "DeviceFullCode": "360M206M2M565",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M116",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 566,
    "DeviceFullCode": "360M206M2M566",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M116",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 567,
    "DeviceFullCode": "360M206M2M567",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M116",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 568,
    "DeviceFullCode": "360M206M2M568",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M116",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 569,
    "DeviceFullCode": "360M206M2M569",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M117",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 570,
    "DeviceFullCode": "360M206M2M570",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M117",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 571,
    "DeviceFullCode": "360M206M2M571",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M117",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 572,
    "DeviceFullCode": "360M206M2M572",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M117",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 573,
    "DeviceFullCode": "360M206M2M573",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M117",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 574,
    "DeviceFullCode": "360M206M2M574",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M117",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 575,
    "DeviceFullCode": "360M206M2M575",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M118",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 576,
    "DeviceFullCode": "360M206M2M576",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M118",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 577,
    "DeviceFullCode": "360M206M2M577",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M118",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 578,
    "DeviceFullCode": "360M206M2M578",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M118",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 579,
    "DeviceFullCode": "360M206M2M579",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M119",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 580,
    "DeviceFullCode": "360M206M2M580",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M119",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 581,
    "DeviceFullCode": "360M206M2M581",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M119",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 582,
    "DeviceFullCode": "360M206M2M582",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M119",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 583,
    "DeviceFullCode": "360M206M2M583",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M119",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 584,
    "DeviceFullCode": "360M206M2M584",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M120",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 585,
    "DeviceFullCode": "360M206M2M585",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M120",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 586,
    "DeviceFullCode": "360M206M2M586",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M120",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 587,
    "DeviceFullCode": "360M206M2M587",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M120",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 588,
    "DeviceFullCode": "360M206M2M588",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M120",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 589,
    "DeviceFullCode": "360M206M2M589",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M120",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 590,
    "DeviceFullCode": "360M206M2M590",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M121",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 591,
    "DeviceFullCode": "360M206M2M591",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M121",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 592,
    "DeviceFullCode": "360M206M2M592",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M121",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 593,
    "DeviceFullCode": "360M206M2M593",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M121",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 594,
    "DeviceFullCode": "360M206M2M594",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M121",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 595,
    "DeviceFullCode": "360M206M2M595",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M121",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 596,
    "DeviceFullCode": "360M206M2M596",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M122",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 597,
    "DeviceFullCode": "360M206M2M597",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M122",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 598,
    "DeviceFullCode": "360M206M2M598",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M122",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 599,
    "DeviceFullCode": "360M206M2M599",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M122",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 600,
    "DeviceFullCode": "360M206M2M600",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M122",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 601,
    "DeviceFullCode": "360M206M2M601",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M122",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 602,
    "DeviceFullCode": "360M206M2M602",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M123",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 603,
    "DeviceFullCode": "360M206M2M603",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M123",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 604,
    "DeviceFullCode": "360M206M2M604",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M123",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 605,
    "DeviceFullCode": "360M206M2M605",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M123",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 606,
    "DeviceFullCode": "360M206M2M606",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M123",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 607,
    "DeviceFullCode": "360M206M2M607",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M123",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 608,
    "DeviceFullCode": "360M206M2M608",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M124",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 609,
    "DeviceFullCode": "360M206M2M609",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M124",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 610,
    "DeviceFullCode": "360M206M2M610",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M124",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 611,
    "DeviceFullCode": "360M206M2M611",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M124",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 612,
    "DeviceFullCode": "360M206M2M612",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M124",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 613,
    "DeviceFullCode": "360M206M2M613",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M124",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 614,
    "DeviceFullCode": "360M206M2M614",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M125",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 615,
    "DeviceFullCode": "360M206M2M615",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M125",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 616,
    "DeviceFullCode": "360M206M2M616",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M125",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 617,
    "DeviceFullCode": "360M206M2M617",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M125",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 618,
    "DeviceFullCode": "360M206M2M618",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M125",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 619,
    "DeviceFullCode": "360M206M2M619",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M125",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 620,
    "DeviceFullCode": "360M206M2M620",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M126",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 621,
    "DeviceFullCode": "360M206M2M621",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M126",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 622,
    "DeviceFullCode": "360M206M2M622",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M126",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 623,
    "DeviceFullCode": "360M206M2M623",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M126",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 624,
    "DeviceFullCode": "360M206M2M624",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M126",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 625,
    "DeviceFullCode": "360M206M2M625",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M126",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 626,
    "DeviceFullCode": "360M206M2M626",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M127",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 627,
    "DeviceFullCode": "360M206M2M627",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M127",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 628,
    "DeviceFullCode": "360M206M2M628",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M127",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 629,
    "DeviceFullCode": "360M206M2M629",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M127",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 630,
    "DeviceFullCode": "360M206M2M630",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M128",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 631,
    "DeviceFullCode": "360M206M2M631",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M128",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 632,
    "DeviceFullCode": "360M206M2M632",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M128",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 633,
    "DeviceFullCode": "360M206M2M633",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M128",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 634,
    "DeviceFullCode": "360M206M2M634",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M128",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 635,
    "DeviceFullCode": "360M206M2M635",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M128",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 636,
    "DeviceFullCode": "360M206M2M636",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M129",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 637,
    "DeviceFullCode": "360M206M2M637",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M129",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 638,
    "DeviceFullCode": "360M206M2M638",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M129",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 639,
    "DeviceFullCode": "360M206M2M639",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M129",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 640,
    "DeviceFullCode": "360M206M2M640",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M129",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 641,
    "DeviceFullCode": "360M206M2M641",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M129",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 642,
    "DeviceFullCode": "360M206M2M642",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M130",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 643,
    "DeviceFullCode": "360M206M2M643",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M130",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 644,
    "DeviceFullCode": "360M206M2M644",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M130",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 645,
    "DeviceFullCode": "360M206M2M645",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M130",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 646,
    "DeviceFullCode": "360M206M2M646",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M130",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 647,
    "DeviceFullCode": "360M206M2M647",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M130",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 648,
    "DeviceFullCode": "360M206M2M648",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M131",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 649,
    "DeviceFullCode": "360M206M2M649",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M131",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 650,
    "DeviceFullCode": "360M206M2M650",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M131",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 651,
    "DeviceFullCode": "360M206M2M651",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M131",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 652,
    "DeviceFullCode": "360M206M2M652",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M131",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 653,
    "DeviceFullCode": "360M206M2M653",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M131",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 654,
    "DeviceFullCode": "360M206M2M654",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M132",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 655,
    "DeviceFullCode": "360M206M2M655",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M132",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 656,
    "DeviceFullCode": "360M206M2M656",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M132",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 657,
    "DeviceFullCode": "360M206M2M657",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M132",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 658,
    "DeviceFullCode": "360M206M2M658",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M132",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 659,
    "DeviceFullCode": "360M206M2M659",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M132",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 660,
    "DeviceFullCode": "360M206M2M660",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M133",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 661,
    "DeviceFullCode": "360M206M2M661",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M133",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 662,
    "DeviceFullCode": "360M206M2M662",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M133",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 663,
    "DeviceFullCode": "360M206M2M663",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M133",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 664,
    "DeviceFullCode": "360M206M2M664",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M134",
    "Capacity": 16.2000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 665,
    "DeviceFullCode": "360M206M2M665",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M134",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 666,
    "DeviceFullCode": "360M206M2M666",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M134",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 667,
    "DeviceFullCode": "360M206M2M667",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M134",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 668,
    "DeviceFullCode": "360M206M2M668",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M134",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 669,
    "DeviceFullCode": "360M206M2M669",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M134",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 670,
    "DeviceFullCode": "360M206M2M670",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M135",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 671,
    "DeviceFullCode": "360M206M2M671",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M135",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 672,
    "DeviceFullCode": "360M206M2M672",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M135",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 673,
    "DeviceFullCode": "360M206M2M673",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M135",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 674,
    "DeviceFullCode": "360M206M2M674",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M135",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 675,
    "DeviceFullCode": "360M206M2M675",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M135",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 676,
    "DeviceFullCode": "360M206M2M676",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M136",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 677,
    "DeviceFullCode": "360M206M2M677",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M136",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 678,
    "DeviceFullCode": "360M206M2M678",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M136",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 679,
    "DeviceFullCode": "360M206M2M679",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M136",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 680,
    "DeviceFullCode": "360M206M2M680",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M136",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 681,
    "DeviceFullCode": "360M206M2M681",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M136",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 682,
    "DeviceFullCode": "360M206M2M682",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M137",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 683,
    "DeviceFullCode": "360M206M2M683",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M137",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 684,
    "DeviceFullCode": "360M206M2M684",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M137",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 685,
    "DeviceFullCode": "360M206M2M685",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M137",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 686,
    "DeviceFullCode": "360M206M2M686",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M137",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 687,
    "DeviceFullCode": "360M206M2M687",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M137",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 688,
    "DeviceFullCode": "360M206M2M688",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M138",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 689,
    "DeviceFullCode": "360M206M2M689",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M138",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 690,
    "DeviceFullCode": "360M206M2M690",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M138",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 691,
    "DeviceFullCode": "360M206M2M691",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M138",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 692,
    "DeviceFullCode": "360M206M2M692",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M138",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 693,
    "DeviceFullCode": "360M206M2M693",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M138",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 694,
    "DeviceFullCode": "360M206M2M694",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M139",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 695,
    "DeviceFullCode": "360M206M2M695",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M139",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 696,
    "DeviceFullCode": "360M206M2M696",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M139",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 697,
    "DeviceFullCode": "360M206M2M697",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M139",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 698,
    "DeviceFullCode": "360M206M2M698",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M140",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 699,
    "DeviceFullCode": "360M206M2M699",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M140",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 700,
    "DeviceFullCode": "360M206M2M700",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M140",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 701,
    "DeviceFullCode": "360M206M2M701",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M140",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 702,
    "DeviceFullCode": "360M206M2M702",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M140",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 703,
    "DeviceFullCode": "360M206M2M703",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M140",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 704,
    "DeviceFullCode": "360M206M2M704",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M141",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 705,
    "DeviceFullCode": "360M206M2M705",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M141",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 706,
    "DeviceFullCode": "360M206M2M706",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M141",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 707,
    "DeviceFullCode": "360M206M2M707",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M141",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 708,
    "DeviceFullCode": "360M206M2M708",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M141",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 709,
    "DeviceFullCode": "360M206M2M709",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M141",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 710,
    "DeviceFullCode": "360M206M2M710",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M142",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 711,
    "DeviceFullCode": "360M206M2M711",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M142",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 712,
    "DeviceFullCode": "360M206M2M712",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M142",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 713,
    "DeviceFullCode": "360M206M2M713",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M142",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 714,
    "DeviceFullCode": "360M206M2M714",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M142",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 715,
    "DeviceFullCode": "360M206M2M715",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M142",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 716,
    "DeviceFullCode": "360M206M2M716",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M143",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 717,
    "DeviceFullCode": "360M206M2M717",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M143",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 718,
    "DeviceFullCode": "360M206M2M718",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M143",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 719,
    "DeviceFullCode": "360M206M2M719",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M143",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 720,
    "DeviceFullCode": "360M206M2M720",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M143",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 721,
    "DeviceFullCode": "360M206M2M721",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M143",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 722,
    "DeviceFullCode": "360M206M2M722",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M144",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 723,
    "DeviceFullCode": "360M206M2M723",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M144",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 724,
    "DeviceFullCode": "360M206M2M724",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M144",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 725,
    "DeviceFullCode": "360M206M2M725",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M144",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 726,
    "DeviceFullCode": "360M206M2M726",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M144",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 727,
    "DeviceFullCode": "360M206M2M727",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M144",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 728,
    "DeviceFullCode": "360M206M2M728",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M145",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 729,
    "DeviceFullCode": "360M206M2M729",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M145",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 730,
    "DeviceFullCode": "360M206M2M730",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M145",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 731,
    "DeviceFullCode": "360M206M2M731",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M145",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 732,
    "DeviceFullCode": "360M206M2M732",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M146",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 733,
    "DeviceFullCode": "360M206M2M733",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M146",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 734,
    "DeviceFullCode": "360M206M2M734",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M146",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 735,
    "DeviceFullCode": "360M206M2M735",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M146",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 736,
    "DeviceFullCode": "360M206M2M736",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M146",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 737,
    "DeviceFullCode": "360M206M2M737",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M146",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 738,
    "DeviceFullCode": "360M206M2M738",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M147",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 739,
    "DeviceFullCode": "360M206M2M739",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M147",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 740,
    "DeviceFullCode": "360M206M2M740",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M147",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 741,
    "DeviceFullCode": "360M206M2M741",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M147",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 742,
    "DeviceFullCode": "360M206M2M742",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M147",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 743,
    "DeviceFullCode": "360M206M2M743",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M147",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 744,
    "DeviceFullCode": "360M206M2M744",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M148",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 745,
    "DeviceFullCode": "360M206M2M745",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M148",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 746,
    "DeviceFullCode": "360M206M2M746",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M148",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 747,
    "DeviceFullCode": "360M206M2M747",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M148",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 748,
    "DeviceFullCode": "360M206M2M748",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M148",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 749,
    "DeviceFullCode": "360M206M2M749",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M148",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 750,
    "DeviceFullCode": "360M206M2M750",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M149",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 751,
    "DeviceFullCode": "360M206M2M751",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M149",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 752,
    "DeviceFullCode": "360M206M2M752",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M149",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 753,
    "DeviceFullCode": "360M206M2M753",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M149",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 754,
    "DeviceFullCode": "360M206M2M754",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M149",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 755,
    "DeviceFullCode": "360M206M2M755",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M149",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 756,
    "DeviceFullCode": "360M206M2M756",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M150",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 757,
    "DeviceFullCode": "360M206M2M757",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M150",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 758,
    "DeviceFullCode": "360M206M2M758",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M150",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 759,
    "DeviceFullCode": "360M206M2M759",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M150",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 760,
    "DeviceFullCode": "360M206M2M760",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M150",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 761,
    "DeviceFullCode": "360M206M2M761",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M150",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 762,
    "DeviceFullCode": "360M206M2M762",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M151",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 763,
    "DeviceFullCode": "360M206M2M763",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M151",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 764,
    "DeviceFullCode": "360M206M2M764",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M151",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 765,
    "DeviceFullCode": "360M206M2M765",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M151",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 766,
    "DeviceFullCode": "360M206M2M766",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M152",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 767,
    "DeviceFullCode": "360M206M2M767",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M152",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 768,
    "DeviceFullCode": "360M206M2M768",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M152",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 769,
    "DeviceFullCode": "360M206M2M769",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M152",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 770,
    "DeviceFullCode": "360M206M2M770",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M152",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 771,
    "DeviceFullCode": "360M206M2M771",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M152",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 772,
    "DeviceFullCode": "360M206M2M772",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M153",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 773,
    "DeviceFullCode": "360M206M2M773",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M153",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 774,
    "DeviceFullCode": "360M206M2M774",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M153",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 775,
    "DeviceFullCode": "360M206M2M775",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M153",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 776,
    "DeviceFullCode": "360M206M2M776",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M153",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 777,
    "DeviceFullCode": "360M206M2M777",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M153",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 778,
    "DeviceFullCode": "360M206M2M778",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M154",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 779,
    "DeviceFullCode": "360M206M2M779",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M154",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 780,
    "DeviceFullCode": "360M206M2M780",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M154",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 781,
    "DeviceFullCode": "360M206M2M781",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M154",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 782,
    "DeviceFullCode": "360M206M2M782",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M154",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 783,
    "DeviceFullCode": "360M206M2M783",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M154",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 784,
    "DeviceFullCode": "360M206M2M784",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M155",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 785,
    "DeviceFullCode": "360M206M2M785",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M155",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 786,
    "DeviceFullCode": "360M206M2M786",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M155",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 787,
    "DeviceFullCode": "360M206M2M787",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M155",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 788,
    "DeviceFullCode": "360M206M2M788",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M155",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 789,
    "DeviceFullCode": "360M206M2M789",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M155",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 790,
    "DeviceFullCode": "360M206M2M790",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M156",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 791,
    "DeviceFullCode": "360M206M2M791",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M156",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 792,
    "DeviceFullCode": "360M206M2M792",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M156",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 793,
    "DeviceFullCode": "360M206M2M793",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M156",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 794,
    "DeviceFullCode": "360M206M2M794",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M156",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 795,
    "DeviceFullCode": "360M206M2M795",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M156",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 796,
    "DeviceFullCode": "360M206M2M796",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M157",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 797,
    "DeviceFullCode": "360M206M2M797",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M157",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 798,
    "DeviceFullCode": "360M206M2M798",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M157",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 799,
    "DeviceFullCode": "360M206M2M799",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M157",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 800,
    "DeviceFullCode": "360M206M2M800",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M158",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 801,
    "DeviceFullCode": "360M206M2M801",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M158",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 802,
    "DeviceFullCode": "360M206M2M802",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M158",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 803,
    "DeviceFullCode": "360M206M2M803",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M158",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 804,
    "DeviceFullCode": "360M206M2M804",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M158",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 805,
    "DeviceFullCode": "360M206M2M805",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M158",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 806,
    "DeviceFullCode": "360M206M2M806",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M159",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 807,
    "DeviceFullCode": "360M206M2M807",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M159",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 808,
    "DeviceFullCode": "360M206M2M808",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M159",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 809,
    "DeviceFullCode": "360M206M2M809",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M159",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 810,
    "DeviceFullCode": "360M206M2M810",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M159",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 811,
    "DeviceFullCode": "360M206M2M811",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M159",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 812,
    "DeviceFullCode": "360M206M2M812",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M160",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 813,
    "DeviceFullCode": "360M206M2M813",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M160",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 814,
    "DeviceFullCode": "360M206M2M814",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M160",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 815,
    "DeviceFullCode": "360M206M2M815",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M160",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 816,
    "DeviceFullCode": "360M206M2M816",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M160",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 817,
    "DeviceFullCode": "360M206M2M817",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M160",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 818,
    "DeviceFullCode": "360M206M2M818",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M161",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 819,
    "DeviceFullCode": "360M206M2M819",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M161",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 820,
    "DeviceFullCode": "360M206M2M820",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M161",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 821,
    "DeviceFullCode": "360M206M2M821",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M161",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 822,
    "DeviceFullCode": "360M206M2M822",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M161",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 823,
    "DeviceFullCode": "360M206M2M823",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M161",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 824,
    "DeviceFullCode": "360M206M2M824",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M162",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 825,
    "DeviceFullCode": "360M206M2M825",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M162",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 826,
    "DeviceFullCode": "360M206M2M826",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M162",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 827,
    "DeviceFullCode": "360M206M2M827",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M162",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 828,
    "DeviceFullCode": "360M206M2M828",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M162",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 829,
    "DeviceFullCode": "360M206M2M829",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M162",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 830,
    "DeviceFullCode": "360M206M2M830",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M163",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 831,
    "DeviceFullCode": "360M206M2M831",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M163",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 832,
    "DeviceFullCode": "360M206M2M832",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M163",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 833,
    "DeviceFullCode": "360M206M2M833",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M163",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 834,
    "DeviceFullCode": "360M206M2M834",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M164",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 835,
    "DeviceFullCode": "360M206M2M835",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M164",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 836,
    "DeviceFullCode": "360M206M2M836",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M164",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 837,
    "DeviceFullCode": "360M206M2M837",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M164",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 838,
    "DeviceFullCode": "360M206M2M838",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M164",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 839,
    "DeviceFullCode": "360M206M2M839",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M164",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 840,
    "DeviceFullCode": "360M206M2M840",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M165",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 841,
    "DeviceFullCode": "360M206M2M841",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M165",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 842,
    "DeviceFullCode": "360M206M2M842",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M165",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 843,
    "DeviceFullCode": "360M206M2M843",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M165",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 844,
    "DeviceFullCode": "360M206M2M844",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M165",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 845,
    "DeviceFullCode": "360M206M2M845",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M165",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 846,
    "DeviceFullCode": "360M206M2M846",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M166",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 847,
    "DeviceFullCode": "360M206M2M847",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M166",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 848,
    "DeviceFullCode": "360M206M2M848",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M166",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 849,
    "DeviceFullCode": "360M206M2M849",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M166",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 850,
    "DeviceFullCode": "360M206M2M850",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M166",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 851,
    "DeviceFullCode": "360M206M2M851",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M166",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 852,
    "DeviceFullCode": "360M206M2M852",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M167",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 853,
    "DeviceFullCode": "360M206M2M853",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M167",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 854,
    "DeviceFullCode": "360M206M2M854",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M167",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 855,
    "DeviceFullCode": "360M206M2M855",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M167",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 856,
    "DeviceFullCode": "360M206M2M856",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M167",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 857,
    "DeviceFullCode": "360M206M2M857",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M167",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 858,
    "DeviceFullCode": "360M206M2M858",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M168",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 859,
    "DeviceFullCode": "360M206M2M859",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M168",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 860,
    "DeviceFullCode": "360M206M2M860",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M168",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 861,
    "DeviceFullCode": "360M206M2M861",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M168",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 862,
    "DeviceFullCode": "360M206M2M862",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M168",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 863,
    "DeviceFullCode": "360M206M2M863",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M168",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 864,
    "DeviceFullCode": "360M206M2M864",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M169",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 865,
    "DeviceFullCode": "360M206M2M865",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M169",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 866,
    "DeviceFullCode": "360M206M2M866",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M169",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 867,
    "DeviceFullCode": "360M206M2M867",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M169",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 868,
    "DeviceFullCode": "360M206M2M868",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M170",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 869,
    "DeviceFullCode": "360M206M2M869",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M170",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 870,
    "DeviceFullCode": "360M206M2M870",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M170",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 871,
    "DeviceFullCode": "360M206M2M871",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M170",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 872,
    "DeviceFullCode": "360M206M2M872",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M170",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 873,
    "DeviceFullCode": "360M206M2M873",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M170",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 874,
    "DeviceFullCode": "360M206M2M874",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M171",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 875,
    "DeviceFullCode": "360M206M2M875",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M171",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 876,
    "DeviceFullCode": "360M206M2M876",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M171",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 877,
    "DeviceFullCode": "360M206M2M877",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M171",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 878,
    "DeviceFullCode": "360M206M2M878",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M171",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 879,
    "DeviceFullCode": "360M206M2M879",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M171",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 880,
    "DeviceFullCode": "360M206M2M880",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M172",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 881,
    "DeviceFullCode": "360M206M2M881",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M172",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 882,
    "DeviceFullCode": "360M206M2M882",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M172",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 883,
    "DeviceFullCode": "360M206M2M883",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M172",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 884,
    "DeviceFullCode": "360M206M2M884",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M172",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 885,
    "DeviceFullCode": "360M206M2M885",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M172",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 886,
    "DeviceFullCode": "360M206M2M886",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M173",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 887,
    "DeviceFullCode": "360M206M2M887",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M173",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 888,
    "DeviceFullCode": "360M206M2M888",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M173",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 889,
    "DeviceFullCode": "360M206M2M889",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M173",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 890,
    "DeviceFullCode": "360M206M2M890",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M173",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 891,
    "DeviceFullCode": "360M206M2M891",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M173",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 892,
    "DeviceFullCode": "360M206M2M892",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M174",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 893,
    "DeviceFullCode": "360M206M2M893",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M174",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 894,
    "DeviceFullCode": "360M206M2M894",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M174",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 895,
    "DeviceFullCode": "360M206M2M895",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M174",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 896,
    "DeviceFullCode": "360M206M2M896",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M174",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 897,
    "DeviceFullCode": "360M206M2M897",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M174",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 898,
    "DeviceFullCode": "360M206M2M898",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M175",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 899,
    "DeviceFullCode": "360M206M2M899",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M175",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 900,
    "DeviceFullCode": "360M206M2M900",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M175",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 2,
    "DeviceCode": 901,
    "DeviceFullCode": "360M206M2M901",
    "DeviceModeFullCode": "360M206M2",
    "PDeviceFullCode": "360M202M10M175",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 902,
    "DeviceFullCode": "360M206M3M902",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M1",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 903,
    "DeviceFullCode": "360M206M3M903",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M1",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 904,
    "DeviceFullCode": "360M206M3M904",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M1",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 905,
    "DeviceFullCode": "360M206M3M905",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M1",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 906,
    "DeviceFullCode": "360M206M3M906",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M1",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 907,
    "DeviceFullCode": "360M206M3M907",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M1",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 908,
    "DeviceFullCode": "360M206M3M908",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M1",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 909,
    "DeviceFullCode": "360M206M3M909",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M2",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 910,
    "DeviceFullCode": "360M206M3M910",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M2",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 911,
    "DeviceFullCode": "360M206M3M911",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M2",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 912,
    "DeviceFullCode": "360M206M3M912",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M2",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 913,
    "DeviceFullCode": "360M206M3M913",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M2",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 914,
    "DeviceFullCode": "360M206M3M914",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M2",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 915,
    "DeviceFullCode": "360M206M3M915",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M2",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 916,
    "DeviceFullCode": "360M206M3M916",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M2",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 917,
    "DeviceFullCode": "360M206M3M917",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M3",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 918,
    "DeviceFullCode": "360M206M3M918",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M3",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 919,
    "DeviceFullCode": "360M206M3M919",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M3",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 920,
    "DeviceFullCode": "360M206M3M920",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M3",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 921,
    "DeviceFullCode": "360M206M3M921",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M3",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 922,
    "DeviceFullCode": "360M206M3M922",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M3",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 923,
    "DeviceFullCode": "360M206M3M923",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M3",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 924,
    "DeviceFullCode": "360M206M3M924",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M3",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 925,
    "DeviceFullCode": "360M206M3M925",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M4",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 926,
    "DeviceFullCode": "360M206M3M926",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M4",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 927,
    "DeviceFullCode": "360M206M3M927",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M4",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 928,
    "DeviceFullCode": "360M206M3M928",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M4",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 929,
    "DeviceFullCode": "360M206M3M929",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M4",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 930,
    "DeviceFullCode": "360M206M3M930",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M4",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 931,
    "DeviceFullCode": "360M206M3M931",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M5",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 932,
    "DeviceFullCode": "360M206M3M932",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M5",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 933,
    "DeviceFullCode": "360M206M3M933",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M5",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 934,
    "DeviceFullCode": "360M206M3M934",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M5",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 935,
    "DeviceFullCode": "360M206M3M935",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M5",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 936,
    "DeviceFullCode": "360M206M3M936",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M5",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 937,
    "DeviceFullCode": "360M206M3M937",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M5",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 938,
    "DeviceFullCode": "360M206M3M938",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M6",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 939,
    "DeviceFullCode": "360M206M3M939",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M6",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 940,
    "DeviceFullCode": "360M206M3M940",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M6",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 941,
    "DeviceFullCode": "360M206M3M941",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M6",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 942,
    "DeviceFullCode": "360M206M3M942",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M6",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 943,
    "DeviceFullCode": "360M206M3M943",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M6",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 944,
    "DeviceFullCode": "360M206M3M944",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M6",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 945,
    "DeviceFullCode": "360M206M3M945",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M6",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 946,
    "DeviceFullCode": "360M206M3M946",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M7",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 947,
    "DeviceFullCode": "360M206M3M947",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M7",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 948,
    "DeviceFullCode": "360M206M3M948",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M7",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 949,
    "DeviceFullCode": "360M206M3M949",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M7",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 950,
    "DeviceFullCode": "360M206M3M950",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M7",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 951,
    "DeviceFullCode": "360M206M3M951",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M7",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 952,
    "DeviceFullCode": "360M206M3M952",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M7",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 953,
    "DeviceFullCode": "360M206M3M953",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M7",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 954,
    "DeviceFullCode": "360M206M3M954",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M8",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 955,
    "DeviceFullCode": "360M206M3M955",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M8",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 956,
    "DeviceFullCode": "360M206M3M956",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M8",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 957,
    "DeviceFullCode": "360M206M3M957",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M8",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 958,
    "DeviceFullCode": "360M206M3M958",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M8",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 959,
    "DeviceFullCode": "360M206M3M959",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M8",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 960,
    "DeviceFullCode": "360M206M3M960",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M9",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 961,
    "DeviceFullCode": "360M206M3M961",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M9",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 962,
    "DeviceFullCode": "360M206M3M962",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M9",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 963,
    "DeviceFullCode": "360M206M3M963",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M9",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 964,
    "DeviceFullCode": "360M206M3M964",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M9",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 965,
    "DeviceFullCode": "360M206M3M965",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M9",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 966,
    "DeviceFullCode": "360M206M3M966",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M9",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 967,
    "DeviceFullCode": "360M206M3M967",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M10",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 968,
    "DeviceFullCode": "360M206M3M968",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M10",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 969,
    "DeviceFullCode": "360M206M3M969",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M10",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 970,
    "DeviceFullCode": "360M206M3M970",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M10",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 971,
    "DeviceFullCode": "360M206M3M971",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M10",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 972,
    "DeviceFullCode": "360M206M3M972",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M10",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 973,
    "DeviceFullCode": "360M206M3M973",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M10",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 974,
    "DeviceFullCode": "360M206M3M974",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M11",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 975,
    "DeviceFullCode": "360M206M3M975",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M11",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 976,
    "DeviceFullCode": "360M206M3M976",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M11",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 977,
    "DeviceFullCode": "360M206M3M977",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M11",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 978,
    "DeviceFullCode": "360M206M3M978",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M11",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 979,
    "DeviceFullCode": "360M206M3M979",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M11",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 980,
    "DeviceFullCode": "360M206M3M980",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M12",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 981,
    "DeviceFullCode": "360M206M3M981",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M12",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 982,
    "DeviceFullCode": "360M206M3M982",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M12",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 983,
    "DeviceFullCode": "360M206M3M983",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M12",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 984,
    "DeviceFullCode": "360M206M3M984",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M12",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 985,
    "DeviceFullCode": "360M206M3M985",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M13",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 986,
    "DeviceFullCode": "360M206M3M986",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M13",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 987,
    "DeviceFullCode": "360M206M3M987",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M13",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 988,
    "DeviceFullCode": "360M206M3M988",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M13",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 989,
    "DeviceFullCode": "360M206M3M989",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M14",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 990,
    "DeviceFullCode": "360M206M3M990",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M14",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 991,
    "DeviceFullCode": "360M206M3M991",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M14",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 992,
    "DeviceFullCode": "360M206M3M992",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M14",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 993,
    "DeviceFullCode": "360M206M3M993",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M15",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 994,
    "DeviceFullCode": "360M206M3M994",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M15",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 995,
    "DeviceFullCode": "360M206M3M995",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M15",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 996,
    "DeviceFullCode": "360M206M3M996",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M15",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 997,
    "DeviceFullCode": "360M206M3M997",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M15",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 998,
    "DeviceFullCode": "360M206M3M998",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M16",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 999,
    "DeviceFullCode": "360M206M3M999",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M16",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 1000,
    "DeviceFullCode": "360M206M3M1000",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M16",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 1001,
    "DeviceFullCode": "360M206M3M1001",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M16",
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 1002,
    "DeviceFullCode": "360M206M3M1002",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M16",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 1003,
    "DeviceFullCode": "360M206M3M1003",
    "DeviceModeFullCode": "360M206M3",
    "PDeviceFullCode": "360M202M9M16",
    "Capacity": 27.0000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceCode": 1,
    "DeviceFullCode": "360M302M6M1",
    "DeviceModeFullCode": "360M302M6",
    "PDeviceFullCode": None,
    "Capacity": 10384.2000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceCode": 2,
    "DeviceFullCode": "360M302M6M2",
    "DeviceModeFullCode": "360M302M6",
    "PDeviceFullCode": None,
    "Capacity": 10956.6000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 6,
    "DeviceCode": 3,
    "DeviceFullCode": "360M302M6M3",
    "DeviceModeFullCode": "360M302M6",
    "PDeviceFullCode": None,
    "Capacity": 11502.0000
  },
  {
    "DeviceTypeCode": 307,
    "DeviceModeCode": 17,
    "DeviceCode": 1,
    "DeviceFullCode": "360M307M17M1",
    "DeviceModeFullCode": "360M307M17",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceCode": 1,
    "DeviceFullCode": "360M505M7M1",
    "DeviceModeFullCode": "360M505M7",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceCode": 2,
    "DeviceFullCode": "360M505M7M2",
    "DeviceModeFullCode": "360M505M7",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 3,
    "DeviceFullCode": "360M505M2M3",
    "DeviceModeFullCode": "360M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 4,
    "DeviceFullCode": "360M505M2M4",
    "DeviceModeFullCode": "360M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 5,
    "DeviceFullCode": "360M505M2M5",
    "DeviceModeFullCode": "360M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 6,
    "DeviceFullCode": "360M505M2M6",
    "DeviceModeFullCode": "360M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 7,
    "DeviceFullCode": "360M505M2M7",
    "DeviceModeFullCode": "360M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceCode": 1,
    "DeviceFullCode": "360M801M1M1",
    "DeviceModeFullCode": "360M801M1",
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
        self.stationCode = 360
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
            pool =ThreadPool(4)
            results = pool.map(self.___calcDeviceAggrega,[203,206,302,307,505,801])
            pool.close() 
            pool.join()
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
        if deviceTypeCode==202:
           self.___calcComboxAndBranch() 
           return 
        try:
            allDeviceTypeDevice= filter(lambda x: x['DeviceTypeCode'] == deviceTypeCode, allDevice)
            deviceMsg=''
            errCount=0
            for  deviceItem  in allDeviceTypeDevice:
                try:
                    df = self.___readAzureTableToDF(deviceItem)
                    point_item=filter(lambda x: x['DeviceTypeCode'] == deviceItem['DeviceTypeCode'] and x['DeviceModeCode']==deviceItem['DeviceModeCode'], deviceModePointConfig)
                    data = self.___calcAggrega(df,point_item,deviceItem['DeviceTypeCode'],deviceItem['DeviceModeFullCode'],deviceItem['DeviceFullCode'])
                    if deviceTypeCode==203 and deviceItem['DeviceFullCode']=="360M203M8M1":
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
                        if  data[dbc] != None and not self.___isNan(data[dbc]):
                              newDBData[dbc] = data[dbc]

                    for branchColumn  in BranchData:
                        if  BranchData[branchColumn] != None and not self.___isNan(BranchData[branchColumn]):
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
          
    def ___isNan(self,var):
        if var!=var:
           return True
        return  False   


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
