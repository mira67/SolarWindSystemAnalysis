#-*- coding: UTF-8 -*-

# 读取气象站数据
# 读取逆变器数据
# 读取汇流箱数据
# 计算天数据
DATETIME_FMT = '%Y-%m-%d %H:%M' 


deviceModePointConfig=[
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB026",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": " APRT_W_Tot",
    "DeviceModePointName": "总视在功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB026",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": " APRT_W_Tot",
    "DeviceModePointName": "总视在功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB026",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": " APRT_W_Tot",
    "DeviceModePointName": "总视在功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB026",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": " APRT_W_Tot",
    "DeviceModePointName": "总视在功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器日运行时间",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器日运行时间",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器日运行时间",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器日运行时间",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "逆变器总运行时间",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "逆变器总运行时间",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "逆变器总运行时间",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "逆变器总运行时间",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX021",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "水平总辐射分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX021",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "水平总辐射分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX021",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "水平总辐射分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX021",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "水平总辐射分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX022",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "斜面总辐射分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX022",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "斜面总辐射分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX022",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "斜面总辐射分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX022",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "斜面总辐射分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX023",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Dir_Min_Avg",
    "DeviceModePointName": "风向分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX023",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Dir_Min_Avg",
    "DeviceModePointName": "风向分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX023",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Dir_Min_Avg",
    "DeviceModePointName": "风向分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX023",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Dir_Min_Avg",
    "DeviceModePointName": "风向分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX024",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp_Min_Avg",
    "DeviceModePointName": "空气温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX024",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp_Min_Avg",
    "DeviceModePointName": "空气温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX024",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp_Min_Avg",
    "DeviceModePointName": "空气温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX024",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp_Min_Avg",
    "DeviceModePointName": "空气温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX025",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_Min_Avg",
    "DeviceModePointName": "1号背板温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX025",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_Min_Avg",
    "DeviceModePointName": "1号背板温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX025",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_Min_Avg",
    "DeviceModePointName": "1号背板温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX025",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_Min_Avg",
    "DeviceModePointName": "1号背板温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX026",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Min_Avg",
    "DeviceModePointName": "2号背板温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX026",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Min_Avg",
    "DeviceModePointName": "2号背板温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX026",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Min_Avg",
    "DeviceModePointName": "2号背板温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX026",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Min_Avg",
    "DeviceModePointName": "2号背板温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX027",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Min_Avg",
    "DeviceModePointName": "3号背板温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX027",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Min_Avg",
    "DeviceModePointName": "3号背板温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX027",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Min_Avg",
    "DeviceModePointName": "3号背板温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX027",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Min_Avg",
    "DeviceModePointName": "3号背板温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX028",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Min_Avg",
    "DeviceModePointName": "4号背板温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX028",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Min_Avg",
    "DeviceModePointName": "4号背板温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX028",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Min_Avg",
    "DeviceModePointName": "4号背板温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX028",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Min_Avg",
    "DeviceModePointName": "4号背板温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX029",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Hum_Min_Avg",
    "DeviceModePointName": "相对湿度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX029",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Hum_Min_Avg",
    "DeviceModePointName": "相对湿度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX029",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Hum_Min_Avg",
    "DeviceModePointName": "相对湿度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX029",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Hum_Min_Avg",
    "DeviceModePointName": "相对湿度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX030",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Air_Pres_Min_Avg",
    "DeviceModePointName": "大气压力分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX030",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Air_Pres_Min_Avg",
    "DeviceModePointName": "大气压力分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX030",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Air_Pres_Min_Avg",
    "DeviceModePointName": "大气压力分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX030",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Air_Pres_Min_Avg",
    "DeviceModePointName": "大气压力分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX031",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num1_Min_Avg",
    "DeviceModePointName": "1号短路电流分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX031",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num1_Min_Avg",
    "DeviceModePointName": "1号短路电流分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX031",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num1_Min_Avg",
    "DeviceModePointName": "1号短路电流分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX031",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num1_Min_Avg",
    "DeviceModePointName": "1号短路电流分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX032",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Open_V_Num1_Min_Avg",
    "DeviceModePointName": "1号开路电压分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX032",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Open_V_Num1_Min_Avg",
    "DeviceModePointName": "1号开路电压分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX032",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Open_V_Num1_Min_Avg",
    "DeviceModePointName": "1号开路电压分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX032",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Open_V_Num1_Min_Avg",
    "DeviceModePointName": "1号开路电压分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX033",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num2_Min_Avg",
    "DeviceModePointName": "2号短路电流分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX033",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num2_Min_Avg",
    "DeviceModePointName": "2号短路电流分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX033",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num2_Min_Avg",
    "DeviceModePointName": "2号短路电流分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX033",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num2_Min_Avg",
    "DeviceModePointName": "2号短路电流分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX036",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Hr_Avg",
    "DeviceModePointName": "水平总辐射小时平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX036",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Hr_Avg",
    "DeviceModePointName": "水平总辐射小时平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX036",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Hr_Avg",
    "DeviceModePointName": "水平总辐射小时平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX036",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Hr_Avg",
    "DeviceModePointName": "水平总辐射小时平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX037",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Hr_Avg",
    "DeviceModePointName": "斜面总辐射小时平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX037",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Hr_Avg",
    "DeviceModePointName": "斜面总辐射小时平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX037",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Hr_Avg",
    "DeviceModePointName": "斜面总辐射小时平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX037",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Hr_Avg",
    "DeviceModePointName": "斜面总辐射小时平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX038",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Spd_Dly_Avg",
    "DeviceModePointName": "风速天平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX038",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Spd_Dly_Avg",
    "DeviceModePointName": "风速天平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX038",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Spd_Dly_Avg",
    "DeviceModePointName": "风速天平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX038",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Spd_Dly_Avg",
    "DeviceModePointName": "风速天平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX039",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Avg",
    "DeviceModePointName": "空气温度天平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX039",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Avg",
    "DeviceModePointName": "空气温度天平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX039",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Avg",
    "DeviceModePointName": "空气温度天平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX039",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Avg",
    "DeviceModePointName": "空气温度天平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX040",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Mini",
    "DeviceModePointName": "空气温度天最小",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX040",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Mini",
    "DeviceModePointName": "空气温度天最小",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX040",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Mini",
    "DeviceModePointName": "空气温度天最小",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX040",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Mini",
    "DeviceModePointName": "空气温度天最小",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX041",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Maxm",
    "DeviceModePointName": "空气温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX041",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Maxm",
    "DeviceModePointName": "空气温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX041",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Maxm",
    "DeviceModePointName": "空气温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX041",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Maxm",
    "DeviceModePointName": "空气温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX042",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Dly_Maxm",
    "DeviceModePointName": "水平总辐射天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX042",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Dly_Maxm",
    "DeviceModePointName": "水平总辐射天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX042",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Dly_Maxm",
    "DeviceModePointName": "水平总辐射天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX042",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Hori_Radi_Dly_Maxm",
    "DeviceModePointName": "水平总辐射天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX043",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Maxm",
    "DeviceModePointName": "斜面总辐射天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX043",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Maxm",
    "DeviceModePointName": "斜面总辐射天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX043",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Maxm",
    "DeviceModePointName": "斜面总辐射天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX043",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Maxm",
    "DeviceModePointName": "斜面总辐射天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX044",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Spd_Dly_Maxm",
    "DeviceModePointName": "风速天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX044",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Spd_Dly_Maxm",
    "DeviceModePointName": "风速天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX044",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Spd_Dly_Maxm",
    "DeviceModePointName": "风速天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX044",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Wind_Spd_Dly_Maxm",
    "DeviceModePointName": "风速天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX045",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Air_Pres_Dly_Maxm",
    "DeviceModePointName": "大气压力天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX045",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Air_Pres_Dly_Maxm",
    "DeviceModePointName": "大气压力天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX045",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Air_Pres_Dly_Maxm",
    "DeviceModePointName": "大气压力天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX045",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Air_Pres_Dly_Maxm",
    "DeviceModePointName": "大气压力天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX046",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_Dly_Maxm",
    "DeviceModePointName": "1号背板温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX046",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_Dly_Maxm",
    "DeviceModePointName": "1号背板温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX046",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_Dly_Maxm",
    "DeviceModePointName": "1号背板温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX046",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_Dly_Maxm",
    "DeviceModePointName": "1号背板温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX047",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Dly_Maxm",
    "DeviceModePointName": "2号背板温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX047",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Dly_Maxm",
    "DeviceModePointName": "2号背板温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX047",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Dly_Maxm",
    "DeviceModePointName": "2号背板温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX047",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Dly_Maxm",
    "DeviceModePointName": "2号背板温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX048",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Dly_Maxm",
    "DeviceModePointName": "3号背板温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX048",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Dly_Maxm",
    "DeviceModePointName": "3号背板温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX048",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Dly_Maxm",
    "DeviceModePointName": "3号背板温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX048",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Dly_Maxm",
    "DeviceModePointName": "3号背板温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX049",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Dly_Maxm",
    "DeviceModePointName": "4号背板温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX049",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Dly_Maxm",
    "DeviceModePointName": "4号背板温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX049",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Dly_Maxm",
    "DeviceModePointName": "4号背板温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX049",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Dly_Maxm",
    "DeviceModePointName": "4号背板温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX050",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num1_Dly_Maxm",
    "DeviceModePointName": "1号短路电流天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX050",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num1_Dly_Maxm",
    "DeviceModePointName": "1号短路电流天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX050",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num1_Dly_Maxm",
    "DeviceModePointName": "1号短路电流天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX050",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num1_Dly_Maxm",
    "DeviceModePointName": "1号短路电流天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX051",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Open_V_Num1_Dly_Maxm",
    "DeviceModePointName": "1号开路电压天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX051",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Open_V_Num1_Dly_Maxm",
    "DeviceModePointName": "1号开路电压天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX051",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Open_V_Num1_Dly_Maxm",
    "DeviceModePointName": "1号开路电压天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX051",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Open_V_Num1_Dly_Maxm",
    "DeviceModePointName": "1号开路电压天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX052",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num2_Dly_Maxm",
    "DeviceModePointName": "2号短路电流天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX052",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num2_Dly_Maxm",
    "DeviceModePointName": "2号短路电流天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX052",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num2_Dly_Maxm",
    "DeviceModePointName": "2号短路电流天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX052",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Shrt_A_Num2_Dly_Maxm",
    "DeviceModePointName": "2号短路电流天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX601",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX601",
    "DeviceModePointName": "环境温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX601",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX601",
    "DeviceModePointName": "环境温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX601",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX601",
    "DeviceModePointName": "环境温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX601",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX601",
    "DeviceModePointName": "环境温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX602",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX602",
    "DeviceModePointName": "温度1",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX602",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX602",
    "DeviceModePointName": "温度1",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX602",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX602",
    "DeviceModePointName": "温度1",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX602",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX602",
    "DeviceModePointName": "温度1",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX603",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX603",
    "DeviceModePointName": "环境湿度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX603",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX603",
    "DeviceModePointName": "环境湿度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX603",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX603",
    "DeviceModePointName": "环境湿度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX603",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX603",
    "DeviceModePointName": "环境湿度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX604",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX604",
    "DeviceModePointName": "总辐射1瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX604",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX604",
    "DeviceModePointName": "总辐射1瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX604",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX604",
    "DeviceModePointName": "总辐射1瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX604",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX604",
    "DeviceModePointName": "总辐射1瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX605",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX605",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX605",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX605",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX605",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX605",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX605",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX605",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX606",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX606",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX606",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX606",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX606",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX606",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX606",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX606",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX607",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX607",
    "DeviceModePointName": "2分钟风速",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX607",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX607",
    "DeviceModePointName": "2分钟风速",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX607",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX607",
    "DeviceModePointName": "2分钟风速",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX607",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX607",
    "DeviceModePointName": "2分钟风速",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX608",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX608",
    "DeviceModePointName": "10分钟风速",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX608",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX608",
    "DeviceModePointName": "10分钟风速",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX608",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX608",
    "DeviceModePointName": "10分钟风速",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX608",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX608",
    "DeviceModePointName": "10分钟风速",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX609",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX609",
    "DeviceModePointName": "总辐射1间隔累计",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX609",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX609",
    "DeviceModePointName": "总辐射1间隔累计",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX609",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX609",
    "DeviceModePointName": "总辐射1间隔累计",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX609",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "QX609",
    "DeviceModePointName": "总辐射1间隔累计",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ007",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "3U0",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ007",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "3U0",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ007",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "3U0",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ007",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "3U0",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ008",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ008",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ008",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ008",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ009",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ009",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ009",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ009",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ010",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ010",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ010",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ010",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ011",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "3I0",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ011",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "3I0",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ011",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "3I0",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ011",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "3I0",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ012",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ012",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ012",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ012",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ013",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ013",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ013",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ013",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ014",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ014",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ014",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ014",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ015",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ015",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ015",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ015",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
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
    "DeviceModeCode": 19,
    "DeviceModePointIECName": "MinTotWh",
    "DeviceModePointName": "正向有功总电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN001",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 19,
    "DeviceModePointIECName": "MinTotWh",
    "DeviceModePointName": "正向有功总电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN001",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 19,
    "DeviceModePointIECName": "MinTotWh",
    "DeviceModePointName": "正向有功总电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN002",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 19,
    "DeviceModePointIECName": "MinTotWhCsm",
    "DeviceModePointName": "反向有功总电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN002",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 19,
    "DeviceModePointIECName": "MinTotWhCsm",
    "DeviceModePointName": "反向有功总电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN002",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 19,
    "DeviceModePointIECName": "MinTotWhCsm",
    "DeviceModePointName": "反向有功总电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN003",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 19,
    "DeviceModePointIECName": "MinTotVArh",
    "DeviceModePointName": "正向无功总电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN003",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 19,
    "DeviceModePointIECName": "MinTotVArh",
    "DeviceModePointName": "正向无功总电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN003",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 19,
    "DeviceModePointIECName": "MinTotVArh",
    "DeviceModePointName": "正向无功总电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN004",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 19,
    "DeviceModePointIECName": "MinTotVarhCsm",
    "DeviceModePointName": "反向无功总电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN004",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 19,
    "DeviceModePointIECName": "MinTotVarhCsm",
    "DeviceModePointName": "反向无功总电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "DN004",
    "DeviceTypeCode": 505,
    "DeviceModeCode": 19,
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
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 1,
    "DeviceFullCode": "394M201M3M1",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M1",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 2,
    "DeviceFullCode": "394M201M3M2",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M1",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 3,
    "DeviceFullCode": "394M201M3M3",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M2",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 4,
    "DeviceFullCode": "394M201M3M4",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M2",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 5,
    "DeviceFullCode": "394M201M3M5",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M3",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 6,
    "DeviceFullCode": "394M201M3M6",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M3",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 7,
    "DeviceFullCode": "394M201M3M7",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M4",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 8,
    "DeviceFullCode": "394M201M3M8",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M4",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 9,
    "DeviceFullCode": "394M201M3M9",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M5",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 10,
    "DeviceFullCode": "394M201M3M10",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M5",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 11,
    "DeviceFullCode": "394M201M3M11",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M6",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 12,
    "DeviceFullCode": "394M201M3M12",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M6",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 13,
    "DeviceFullCode": "394M201M3M13",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M7",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 14,
    "DeviceFullCode": "394M201M3M14",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M7",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 15,
    "DeviceFullCode": "394M201M3M15",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M8",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 16,
    "DeviceFullCode": "394M201M3M16",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M8",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 17,
    "DeviceFullCode": "394M201M3M17",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M9",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 18,
    "DeviceFullCode": "394M201M3M18",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M9",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 19,
    "DeviceFullCode": "394M201M3M19",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M10",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 20,
    "DeviceFullCode": "394M201M3M20",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M10",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 21,
    "DeviceFullCode": "394M201M3M21",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M11",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 22,
    "DeviceFullCode": "394M201M3M22",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M11",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 23,
    "DeviceFullCode": "394M201M3M23",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M12",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 24,
    "DeviceFullCode": "394M201M3M24",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M12",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 25,
    "DeviceFullCode": "394M201M3M25",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M13",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 26,
    "DeviceFullCode": "394M201M3M26",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M13",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 27,
    "DeviceFullCode": "394M201M3M27",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M14",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 28,
    "DeviceFullCode": "394M201M3M28",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M14",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 29,
    "DeviceFullCode": "394M201M3M29",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M15",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 30,
    "DeviceFullCode": "394M201M3M30",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M15",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 31,
    "DeviceFullCode": "394M201M3M31",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M16",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 32,
    "DeviceFullCode": "394M201M3M32",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M16",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 33,
    "DeviceFullCode": "394M201M3M33",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M17",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 34,
    "DeviceFullCode": "394M201M3M34",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M17",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 35,
    "DeviceFullCode": "394M201M3M35",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M18",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 36,
    "DeviceFullCode": "394M201M3M36",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M18",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 37,
    "DeviceFullCode": "394M201M3M37",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M19",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 38,
    "DeviceFullCode": "394M201M3M38",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M19",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 39,
    "DeviceFullCode": "394M201M3M39",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M20",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 3,
    "DeviceCode": 40,
    "DeviceFullCode": "394M201M3M40",
    "DeviceModeFullCode": "394M201M3",
    "PDeviceFullCode": "394M204M2M20",
    "Capacity": 500.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 1,
    "DeviceFullCode": "394M202M6M1",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M1",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 2,
    "DeviceFullCode": "394M202M6M2",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M1",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 3,
    "DeviceFullCode": "394M202M6M3",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M1",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 4,
    "DeviceFullCode": "394M202M6M4",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M1",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 5,
    "DeviceFullCode": "394M202M6M5",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M1",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 6,
    "DeviceFullCode": "394M202M6M6",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M1",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 7,
    "DeviceFullCode": "394M202M6M7",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M2",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 8,
    "DeviceFullCode": "394M202M6M8",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M2",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 9,
    "DeviceFullCode": "394M202M6M9",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M2",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 10,
    "DeviceFullCode": "394M202M6M10",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M2",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 11,
    "DeviceFullCode": "394M202M6M11",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M2",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 12,
    "DeviceFullCode": "394M202M6M12",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M2",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 13,
    "DeviceFullCode": "394M202M6M13",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M3",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 14,
    "DeviceFullCode": "394M202M6M14",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M3",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 15,
    "DeviceFullCode": "394M202M6M15",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M3",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 16,
    "DeviceFullCode": "394M202M6M16",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M3",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 17,
    "DeviceFullCode": "394M202M6M17",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M3",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 18,
    "DeviceFullCode": "394M202M6M18",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M3",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 19,
    "DeviceFullCode": "394M202M6M19",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M4",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 20,
    "DeviceFullCode": "394M202M6M20",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M4",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 21,
    "DeviceFullCode": "394M202M6M21",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M4",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 22,
    "DeviceFullCode": "394M202M6M22",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M4",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 23,
    "DeviceFullCode": "394M202M6M23",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M4",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 24,
    "DeviceFullCode": "394M202M6M24",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M4",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 25,
    "DeviceFullCode": "394M202M6M25",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M5",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 26,
    "DeviceFullCode": "394M202M6M26",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M5",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 27,
    "DeviceFullCode": "394M202M6M27",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M5",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 28,
    "DeviceFullCode": "394M202M6M28",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M5",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 29,
    "DeviceFullCode": "394M202M6M29",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M5",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 30,
    "DeviceFullCode": "394M202M6M30",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M5",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 31,
    "DeviceFullCode": "394M202M6M31",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M6",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 32,
    "DeviceFullCode": "394M202M6M32",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M6",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 33,
    "DeviceFullCode": "394M202M6M33",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M6",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 34,
    "DeviceFullCode": "394M202M6M34",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M6",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 35,
    "DeviceFullCode": "394M202M6M35",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M6",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 36,
    "DeviceFullCode": "394M202M6M36",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M6",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 37,
    "DeviceFullCode": "394M202M6M37",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M7",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 38,
    "DeviceFullCode": "394M202M6M38",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M7",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 39,
    "DeviceFullCode": "394M202M6M39",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M7",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 40,
    "DeviceFullCode": "394M202M6M40",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M7",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 41,
    "DeviceFullCode": "394M202M6M41",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M7",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 42,
    "DeviceFullCode": "394M202M6M42",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M7",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 43,
    "DeviceFullCode": "394M202M6M43",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M8",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 44,
    "DeviceFullCode": "394M202M6M44",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M8",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 45,
    "DeviceFullCode": "394M202M6M45",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M8",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 46,
    "DeviceFullCode": "394M202M6M46",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M8",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 47,
    "DeviceFullCode": "394M202M6M47",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M8",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 48,
    "DeviceFullCode": "394M202M6M48",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M8",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 49,
    "DeviceFullCode": "394M202M6M49",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M9",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 50,
    "DeviceFullCode": "394M202M6M50",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M9",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 51,
    "DeviceFullCode": "394M202M6M51",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M9",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 52,
    "DeviceFullCode": "394M202M6M52",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M9",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 53,
    "DeviceFullCode": "394M202M6M53",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M9",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 54,
    "DeviceFullCode": "394M202M6M54",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M9",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 55,
    "DeviceFullCode": "394M202M6M55",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M10",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 56,
    "DeviceFullCode": "394M202M6M56",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M10",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 57,
    "DeviceFullCode": "394M202M6M57",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M10",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 58,
    "DeviceFullCode": "394M202M6M58",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M10",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 59,
    "DeviceFullCode": "394M202M6M59",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M10",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 60,
    "DeviceFullCode": "394M202M6M60",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M10",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 61,
    "DeviceFullCode": "394M202M6M61",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M11",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 62,
    "DeviceFullCode": "394M202M6M62",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M11",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 63,
    "DeviceFullCode": "394M202M6M63",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M11",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 64,
    "DeviceFullCode": "394M202M6M64",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M11",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 65,
    "DeviceFullCode": "394M202M6M65",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M11",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 66,
    "DeviceFullCode": "394M202M6M66",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M11",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 67,
    "DeviceFullCode": "394M202M6M67",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M12",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 68,
    "DeviceFullCode": "394M202M6M68",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M12",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 69,
    "DeviceFullCode": "394M202M6M69",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M12",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 70,
    "DeviceFullCode": "394M202M6M70",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M12",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 71,
    "DeviceFullCode": "394M202M6M71",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M12",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 72,
    "DeviceFullCode": "394M202M6M72",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M12",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 73,
    "DeviceFullCode": "394M202M6M73",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M13",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 74,
    "DeviceFullCode": "394M202M6M74",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M13",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 75,
    "DeviceFullCode": "394M202M6M75",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M13",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 76,
    "DeviceFullCode": "394M202M6M76",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M13",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 77,
    "DeviceFullCode": "394M202M6M77",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M13",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 78,
    "DeviceFullCode": "394M202M6M78",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M13",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 79,
    "DeviceFullCode": "394M202M6M79",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M14",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 80,
    "DeviceFullCode": "394M202M6M80",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M14",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 81,
    "DeviceFullCode": "394M202M6M81",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M14",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 82,
    "DeviceFullCode": "394M202M6M82",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M14",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 83,
    "DeviceFullCode": "394M202M6M83",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M14",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 84,
    "DeviceFullCode": "394M202M6M84",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M14",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 85,
    "DeviceFullCode": "394M202M6M85",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M15",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 86,
    "DeviceFullCode": "394M202M6M86",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M15",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 87,
    "DeviceFullCode": "394M202M6M87",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M15",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 88,
    "DeviceFullCode": "394M202M6M88",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M15",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 89,
    "DeviceFullCode": "394M202M6M89",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M15",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 90,
    "DeviceFullCode": "394M202M6M90",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M15",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 91,
    "DeviceFullCode": "394M202M6M91",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M16",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 92,
    "DeviceFullCode": "394M202M6M92",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M16",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 93,
    "DeviceFullCode": "394M202M6M93",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M16",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 94,
    "DeviceFullCode": "394M202M6M94",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M16",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 95,
    "DeviceFullCode": "394M202M6M95",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M16",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 96,
    "DeviceFullCode": "394M202M6M96",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M16",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 97,
    "DeviceFullCode": "394M202M6M97",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M17",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 98,
    "DeviceFullCode": "394M202M6M98",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M17",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 99,
    "DeviceFullCode": "394M202M6M99",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M17",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 100,
    "DeviceFullCode": "394M202M6M100",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M17",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 101,
    "DeviceFullCode": "394M202M6M101",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M17",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 102,
    "DeviceFullCode": "394M202M6M102",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M17",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 103,
    "DeviceFullCode": "394M202M6M103",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M18",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 104,
    "DeviceFullCode": "394M202M6M104",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M18",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 105,
    "DeviceFullCode": "394M202M6M105",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M18",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 106,
    "DeviceFullCode": "394M202M6M106",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M18",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 107,
    "DeviceFullCode": "394M202M6M107",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M18",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 108,
    "DeviceFullCode": "394M202M6M108",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M18",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 109,
    "DeviceFullCode": "394M202M6M109",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M19",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 110,
    "DeviceFullCode": "394M202M6M110",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M19",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 111,
    "DeviceFullCode": "394M202M6M111",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M19",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 112,
    "DeviceFullCode": "394M202M6M112",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M19",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 113,
    "DeviceFullCode": "394M202M6M113",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M19",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 114,
    "DeviceFullCode": "394M202M6M114",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M19",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 115,
    "DeviceFullCode": "394M202M6M115",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M20",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 116,
    "DeviceFullCode": "394M202M6M116",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M20",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 117,
    "DeviceFullCode": "394M202M6M117",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M20",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 118,
    "DeviceFullCode": "394M202M6M118",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M20",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 119,
    "DeviceFullCode": "394M202M6M119",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M20",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 120,
    "DeviceFullCode": "394M202M6M120",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M20",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 121,
    "DeviceFullCode": "394M202M6M121",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M21",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 122,
    "DeviceFullCode": "394M202M6M122",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M21",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 123,
    "DeviceFullCode": "394M202M6M123",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M21",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 124,
    "DeviceFullCode": "394M202M6M124",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M21",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 125,
    "DeviceFullCode": "394M202M6M125",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M21",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 126,
    "DeviceFullCode": "394M202M6M126",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M21",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 127,
    "DeviceFullCode": "394M202M6M127",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M22",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 128,
    "DeviceFullCode": "394M202M6M128",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M22",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 129,
    "DeviceFullCode": "394M202M6M129",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M22",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 130,
    "DeviceFullCode": "394M202M6M130",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M22",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 131,
    "DeviceFullCode": "394M202M6M131",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M22",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 132,
    "DeviceFullCode": "394M202M6M132",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M22",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 133,
    "DeviceFullCode": "394M202M6M133",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M23",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 134,
    "DeviceFullCode": "394M202M6M134",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M23",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 135,
    "DeviceFullCode": "394M202M6M135",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M23",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 136,
    "DeviceFullCode": "394M202M6M136",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M23",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 137,
    "DeviceFullCode": "394M202M6M137",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M23",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 138,
    "DeviceFullCode": "394M202M6M138",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M23",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 139,
    "DeviceFullCode": "394M202M6M139",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M24",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 140,
    "DeviceFullCode": "394M202M6M140",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M24",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 141,
    "DeviceFullCode": "394M202M6M141",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M24",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 142,
    "DeviceFullCode": "394M202M6M142",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M24",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 143,
    "DeviceFullCode": "394M202M6M143",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M24",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 144,
    "DeviceFullCode": "394M202M6M144",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M24",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 145,
    "DeviceFullCode": "394M202M6M145",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M25",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 146,
    "DeviceFullCode": "394M202M6M146",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M25",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 147,
    "DeviceFullCode": "394M202M6M147",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M25",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 148,
    "DeviceFullCode": "394M202M6M148",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M25",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 149,
    "DeviceFullCode": "394M202M6M149",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M25",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 150,
    "DeviceFullCode": "394M202M6M150",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M25",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 151,
    "DeviceFullCode": "394M202M6M151",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M26",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 152,
    "DeviceFullCode": "394M202M6M152",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M26",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 153,
    "DeviceFullCode": "394M202M6M153",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M26",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 154,
    "DeviceFullCode": "394M202M6M154",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M26",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 155,
    "DeviceFullCode": "394M202M6M155",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M26",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 156,
    "DeviceFullCode": "394M202M6M156",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M26",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 157,
    "DeviceFullCode": "394M202M6M157",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M27",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 158,
    "DeviceFullCode": "394M202M6M158",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M27",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 159,
    "DeviceFullCode": "394M202M6M159",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M27",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 160,
    "DeviceFullCode": "394M202M6M160",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M27",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 161,
    "DeviceFullCode": "394M202M6M161",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M27",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 162,
    "DeviceFullCode": "394M202M6M162",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M27",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 163,
    "DeviceFullCode": "394M202M6M163",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M28",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 164,
    "DeviceFullCode": "394M202M6M164",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M28",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 165,
    "DeviceFullCode": "394M202M6M165",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M28",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 166,
    "DeviceFullCode": "394M202M6M166",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M28",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 167,
    "DeviceFullCode": "394M202M6M167",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M28",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 168,
    "DeviceFullCode": "394M202M6M168",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M28",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 169,
    "DeviceFullCode": "394M202M6M169",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M29",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 170,
    "DeviceFullCode": "394M202M6M170",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M29",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 171,
    "DeviceFullCode": "394M202M6M171",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M29",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 172,
    "DeviceFullCode": "394M202M6M172",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M29",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 173,
    "DeviceFullCode": "394M202M6M173",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M29",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 174,
    "DeviceFullCode": "394M202M6M174",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M29",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 175,
    "DeviceFullCode": "394M202M6M175",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M30",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 176,
    "DeviceFullCode": "394M202M6M176",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M30",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 177,
    "DeviceFullCode": "394M202M6M177",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M30",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 178,
    "DeviceFullCode": "394M202M6M178",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M30",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 179,
    "DeviceFullCode": "394M202M6M179",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M30",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 180,
    "DeviceFullCode": "394M202M6M180",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M30",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 181,
    "DeviceFullCode": "394M202M6M181",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M31",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 182,
    "DeviceFullCode": "394M202M6M182",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M31",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 183,
    "DeviceFullCode": "394M202M6M183",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M31",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 184,
    "DeviceFullCode": "394M202M6M184",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M31",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 185,
    "DeviceFullCode": "394M202M6M185",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M31",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 186,
    "DeviceFullCode": "394M202M6M186",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M31",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 187,
    "DeviceFullCode": "394M202M6M187",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M32",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 188,
    "DeviceFullCode": "394M202M6M188",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M32",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 189,
    "DeviceFullCode": "394M202M6M189",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M32",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 190,
    "DeviceFullCode": "394M202M6M190",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M32",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 191,
    "DeviceFullCode": "394M202M6M191",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M32",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 192,
    "DeviceFullCode": "394M202M6M192",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M32",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 193,
    "DeviceFullCode": "394M202M6M193",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M33",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 194,
    "DeviceFullCode": "394M202M6M194",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M33",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 195,
    "DeviceFullCode": "394M202M6M195",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M33",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 196,
    "DeviceFullCode": "394M202M6M196",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M33",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 197,
    "DeviceFullCode": "394M202M6M197",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M33",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 198,
    "DeviceFullCode": "394M202M6M198",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M33",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 199,
    "DeviceFullCode": "394M202M6M199",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M34",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 200,
    "DeviceFullCode": "394M202M6M200",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M34",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 201,
    "DeviceFullCode": "394M202M6M201",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M34",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 202,
    "DeviceFullCode": "394M202M6M202",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M34",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 203,
    "DeviceFullCode": "394M202M6M203",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M34",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 204,
    "DeviceFullCode": "394M202M6M204",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M34",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 205,
    "DeviceFullCode": "394M202M6M205",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M35",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 206,
    "DeviceFullCode": "394M202M6M206",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M35",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 207,
    "DeviceFullCode": "394M202M6M207",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M35",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 208,
    "DeviceFullCode": "394M202M6M208",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M35",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 209,
    "DeviceFullCode": "394M202M6M209",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M35",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 210,
    "DeviceFullCode": "394M202M6M210",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M35",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 211,
    "DeviceFullCode": "394M202M6M211",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M36",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 212,
    "DeviceFullCode": "394M202M6M212",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M36",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 213,
    "DeviceFullCode": "394M202M6M213",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M36",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 214,
    "DeviceFullCode": "394M202M6M214",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M36",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 215,
    "DeviceFullCode": "394M202M6M215",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M36",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 216,
    "DeviceFullCode": "394M202M6M216",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M36",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 217,
    "DeviceFullCode": "394M202M6M217",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M37",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 218,
    "DeviceFullCode": "394M202M6M218",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M37",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 219,
    "DeviceFullCode": "394M202M6M219",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M37",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 220,
    "DeviceFullCode": "394M202M6M220",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M37",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 221,
    "DeviceFullCode": "394M202M6M221",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M37",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 222,
    "DeviceFullCode": "394M202M6M222",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M37",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 223,
    "DeviceFullCode": "394M202M6M223",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M38",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 224,
    "DeviceFullCode": "394M202M6M224",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M38",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 225,
    "DeviceFullCode": "394M202M6M225",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M38",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 226,
    "DeviceFullCode": "394M202M6M226",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M38",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 227,
    "DeviceFullCode": "394M202M6M227",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M38",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 228,
    "DeviceFullCode": "394M202M6M228",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M38",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 229,
    "DeviceFullCode": "394M202M6M229",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M39",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 230,
    "DeviceFullCode": "394M202M6M230",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M39",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 231,
    "DeviceFullCode": "394M202M6M231",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M39",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 232,
    "DeviceFullCode": "394M202M6M232",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M39",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 233,
    "DeviceFullCode": "394M202M6M233",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M39",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 234,
    "DeviceFullCode": "394M202M6M234",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M39",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 235,
    "DeviceFullCode": "394M202M6M235",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M40",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 236,
    "DeviceFullCode": "394M202M6M236",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M40",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 237,
    "DeviceFullCode": "394M202M6M237",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M40",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 238,
    "DeviceFullCode": "394M202M6M238",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M40",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 239,
    "DeviceFullCode": "394M202M6M239",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M40",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 240,
    "DeviceFullCode": "394M202M6M240",
    "DeviceModeFullCode": "394M202M6",
    "PDeviceFullCode": "394M201M3M40",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 203,
    "DeviceModeCode": 6,
    "DeviceCode": 1,
    "DeviceFullCode": "394M203M6M1",
    "DeviceModeFullCode": "394M203M6",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 203,
    "DeviceModeCode": 11,
    "DeviceCode": 2,
    "DeviceFullCode": "394M203M11M2",
    "DeviceModeFullCode": "394M203M11",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceCode": 1,
    "DeviceFullCode": "394M302M16M1",
    "DeviceModeFullCode": "394M302M16",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 16,
    "DeviceCode": 2,
    "DeviceFullCode": "394M302M16M2",
    "DeviceModeFullCode": "394M302M16",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 307,
    "DeviceModeCode": 13,
    "DeviceCode": 1,
    "DeviceFullCode": "394M307M13M1",
    "DeviceModeFullCode": "394M307M13",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 19,
    "DeviceCode": 1,
    "DeviceFullCode": "394M505M19M1",
    "DeviceModeFullCode": "394M505M19",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 19,
    "DeviceCode": 2,
    "DeviceFullCode": "394M505M19M2",
    "DeviceModeFullCode": "394M505M19",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 3,
    "DeviceFullCode": "394M505M2M3",
    "DeviceModeFullCode": "394M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 4,
    "DeviceFullCode": "394M505M2M4",
    "DeviceModeFullCode": "394M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 5,
    "DeviceFullCode": "394M505M2M5",
    "DeviceModeFullCode": "394M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 6,
    "DeviceFullCode": "394M505M2M6",
    "DeviceModeFullCode": "394M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 7,
    "DeviceFullCode": "394M505M2M7",
    "DeviceModeFullCode": "394M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceCode": 1,
    "DeviceFullCode": "394M801M1M1",
    "DeviceModeFullCode": "394M801M1",
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
        self.stationCode = 394
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
                if not self.___isNan(data[dbc]):
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
            results = pool.map(self.___calcDeviceAggrega,[801])
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
                    if deviceTypeCode==203 and deviceItem['DeviceFullCode']=="394M203M6M1":
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
