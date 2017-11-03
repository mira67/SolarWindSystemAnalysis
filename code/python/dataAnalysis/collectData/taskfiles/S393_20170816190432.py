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
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB026",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": " APRT_W_Tot",
    "DeviceModePointName": "总视在功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB026",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": " APRT_W_Tot",
    "DeviceModePointName": "总视在功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB026",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": " APRT_W_Tot",
    "DeviceModePointName": "总视在功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB026",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": " APRT_W_Tot",
    "DeviceModePointName": "总视在功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX021",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "水平总辐射分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX021",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "水平总辐射分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX021",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "水平总辐射分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX021",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "水平总辐射分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX022",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "斜面总辐射分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX022",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "斜面总辐射分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX022",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "斜面总辐射分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX022",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "斜面总辐射分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX023",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Dir_Min_Avg",
    "DeviceModePointName": "风向分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX023",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Dir_Min_Avg",
    "DeviceModePointName": "风向分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX023",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Dir_Min_Avg",
    "DeviceModePointName": "风向分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX023",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Dir_Min_Avg",
    "DeviceModePointName": "风向分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX024",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp_Min_Avg",
    "DeviceModePointName": "空气温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX024",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp_Min_Avg",
    "DeviceModePointName": "空气温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX024",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp_Min_Avg",
    "DeviceModePointName": "空气温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX024",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp_Min_Avg",
    "DeviceModePointName": "空气温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX025",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_Min_Avg",
    "DeviceModePointName": "1号背板温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX025",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_Min_Avg",
    "DeviceModePointName": "1号背板温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX025",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_Min_Avg",
    "DeviceModePointName": "1号背板温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX025",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_Min_Avg",
    "DeviceModePointName": "1号背板温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX026",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Min_Avg",
    "DeviceModePointName": "2号背板温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX026",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Min_Avg",
    "DeviceModePointName": "2号背板温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX026",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Min_Avg",
    "DeviceModePointName": "2号背板温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX026",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Min_Avg",
    "DeviceModePointName": "2号背板温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX027",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Min_Avg",
    "DeviceModePointName": "3号背板温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX027",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Min_Avg",
    "DeviceModePointName": "3号背板温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX027",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Min_Avg",
    "DeviceModePointName": "3号背板温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX027",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Min_Avg",
    "DeviceModePointName": "3号背板温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX028",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Min_Avg",
    "DeviceModePointName": "4号背板温度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX028",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Min_Avg",
    "DeviceModePointName": "4号背板温度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX028",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Min_Avg",
    "DeviceModePointName": "4号背板温度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX028",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Min_Avg",
    "DeviceModePointName": "4号背板温度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX029",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Hum_Min_Avg",
    "DeviceModePointName": "相对湿度分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX029",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Hum_Min_Avg",
    "DeviceModePointName": "相对湿度分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX029",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Hum_Min_Avg",
    "DeviceModePointName": "相对湿度分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX029",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Hum_Min_Avg",
    "DeviceModePointName": "相对湿度分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX030",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Air_Pres_Min_Avg",
    "DeviceModePointName": "大气压力分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX030",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Air_Pres_Min_Avg",
    "DeviceModePointName": "大气压力分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX030",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Air_Pres_Min_Avg",
    "DeviceModePointName": "大气压力分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX030",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Air_Pres_Min_Avg",
    "DeviceModePointName": "大气压力分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX031",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num1_Min_Avg",
    "DeviceModePointName": "1号短路电流分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX031",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num1_Min_Avg",
    "DeviceModePointName": "1号短路电流分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX031",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num1_Min_Avg",
    "DeviceModePointName": "1号短路电流分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX031",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num1_Min_Avg",
    "DeviceModePointName": "1号短路电流分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX032",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_V_Num1_Min_Avg",
    "DeviceModePointName": "1号开路电压分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX032",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_V_Num1_Min_Avg",
    "DeviceModePointName": "1号开路电压分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX032",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_V_Num1_Min_Avg",
    "DeviceModePointName": "1号开路电压分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX032",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_V_Num1_Min_Avg",
    "DeviceModePointName": "1号开路电压分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX033",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num2_Min_Avg",
    "DeviceModePointName": "2号短路电流分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX033",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num2_Min_Avg",
    "DeviceModePointName": "2号短路电流分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX033",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num2_Min_Avg",
    "DeviceModePointName": "2号短路电流分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX033",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num2_Min_Avg",
    "DeviceModePointName": "2号短路电流分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX036",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Hr_Avg",
    "DeviceModePointName": "水平总辐射小时平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX036",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Hr_Avg",
    "DeviceModePointName": "水平总辐射小时平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX036",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Hr_Avg",
    "DeviceModePointName": "水平总辐射小时平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX036",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Hr_Avg",
    "DeviceModePointName": "水平总辐射小时平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX037",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Hr_Avg",
    "DeviceModePointName": "斜面总辐射小时平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX037",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Hr_Avg",
    "DeviceModePointName": "斜面总辐射小时平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX037",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Hr_Avg",
    "DeviceModePointName": "斜面总辐射小时平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX037",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Hr_Avg",
    "DeviceModePointName": "斜面总辐射小时平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX038",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Spd_Dly_Avg",
    "DeviceModePointName": "风速天平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX038",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Spd_Dly_Avg",
    "DeviceModePointName": "风速天平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX038",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Spd_Dly_Avg",
    "DeviceModePointName": "风速天平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX038",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Spd_Dly_Avg",
    "DeviceModePointName": "风速天平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX039",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Avg",
    "DeviceModePointName": "空气温度天平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX039",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Avg",
    "DeviceModePointName": "空气温度天平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX039",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Avg",
    "DeviceModePointName": "空气温度天平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX039",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Avg",
    "DeviceModePointName": "空气温度天平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX040",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Mini",
    "DeviceModePointName": "空气温度天最小",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX040",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Mini",
    "DeviceModePointName": "空气温度天最小",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX040",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Mini",
    "DeviceModePointName": "空气温度天最小",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX040",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Mini",
    "DeviceModePointName": "空气温度天最小",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX041",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Maxm",
    "DeviceModePointName": "空气温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX041",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Maxm",
    "DeviceModePointName": "空气温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX041",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Maxm",
    "DeviceModePointName": "空气温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX041",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Amb_Tmp_Dly_Maxm",
    "DeviceModePointName": "空气温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX042",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Dly_Maxm",
    "DeviceModePointName": "水平总辐射天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX042",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Dly_Maxm",
    "DeviceModePointName": "水平总辐射天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX042",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Dly_Maxm",
    "DeviceModePointName": "水平总辐射天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX042",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Dly_Maxm",
    "DeviceModePointName": "水平总辐射天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX043",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Maxm",
    "DeviceModePointName": "斜面总辐射天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX043",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Maxm",
    "DeviceModePointName": "斜面总辐射天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX043",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Maxm",
    "DeviceModePointName": "斜面总辐射天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX043",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Maxm",
    "DeviceModePointName": "斜面总辐射天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX044",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Spd_Dly_Maxm",
    "DeviceModePointName": "风速天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX044",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Spd_Dly_Maxm",
    "DeviceModePointName": "风速天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX044",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Spd_Dly_Maxm",
    "DeviceModePointName": "风速天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX044",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Wind_Spd_Dly_Maxm",
    "DeviceModePointName": "风速天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX045",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Air_Pres_Dly_Maxm",
    "DeviceModePointName": "大气压力天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX045",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Air_Pres_Dly_Maxm",
    "DeviceModePointName": "大气压力天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX045",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Air_Pres_Dly_Maxm",
    "DeviceModePointName": "大气压力天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX045",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Air_Pres_Dly_Maxm",
    "DeviceModePointName": "大气压力天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX046",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_Dly_Maxm",
    "DeviceModePointName": "1号背板温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX046",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_Dly_Maxm",
    "DeviceModePointName": "1号背板温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX046",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_Dly_Maxm",
    "DeviceModePointName": "1号背板温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX046",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_Dly_Maxm",
    "DeviceModePointName": "1号背板温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX047",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Dly_Maxm",
    "DeviceModePointName": "2号背板温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX047",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Dly_Maxm",
    "DeviceModePointName": "2号背板温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX047",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Dly_Maxm",
    "DeviceModePointName": "2号背板温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX047",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_2_Dly_Maxm",
    "DeviceModePointName": "2号背板温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX048",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Dly_Maxm",
    "DeviceModePointName": "3号背板温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX048",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Dly_Maxm",
    "DeviceModePointName": "3号背板温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX048",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Dly_Maxm",
    "DeviceModePointName": "3号背板温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX048",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_3_Dly_Maxm",
    "DeviceModePointName": "3号背板温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX049",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Dly_Maxm",
    "DeviceModePointName": "4号背板温度天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX049",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Dly_Maxm",
    "DeviceModePointName": "4号背板温度天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX049",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Dly_Maxm",
    "DeviceModePointName": "4号背板温度天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX049",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Back_Plate_Tmp_4_Dly_Maxm",
    "DeviceModePointName": "4号背板温度天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX050",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num1_Dly_Maxm",
    "DeviceModePointName": "1号短路电流天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX050",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num1_Dly_Maxm",
    "DeviceModePointName": "1号短路电流天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX050",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num1_Dly_Maxm",
    "DeviceModePointName": "1号短路电流天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX050",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num1_Dly_Maxm",
    "DeviceModePointName": "1号短路电流天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX051",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Open_V_Num1_Dly_Maxm",
    "DeviceModePointName": "1号开路电压天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX051",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Open_V_Num1_Dly_Maxm",
    "DeviceModePointName": "1号开路电压天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX051",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Open_V_Num1_Dly_Maxm",
    "DeviceModePointName": "1号开路电压天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX051",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Open_V_Num1_Dly_Maxm",
    "DeviceModePointName": "1号开路电压天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX052",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num2_Dly_Maxm",
    "DeviceModePointName": "2号短路电流天最大",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX052",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num2_Dly_Maxm",
    "DeviceModePointName": "2号短路电流天最大",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX052",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num2_Dly_Maxm",
    "DeviceModePointName": "2号短路电流天最大",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX052",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Shrt_A_Num2_Dly_Maxm",
    "DeviceModePointName": "2号短路电流天最大",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB001",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUab",
    "DeviceModePointName": "高压侧Uab",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB001",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUab",
    "DeviceModePointName": "高压侧Uab",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB001",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUab",
    "DeviceModePointName": "高压侧Uab",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB001",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUab",
    "DeviceModePointName": "高压侧Uab",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB002",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUbc",
    "DeviceModePointName": "高压侧Ubc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB002",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUbc",
    "DeviceModePointName": "高压侧Ubc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB002",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUbc",
    "DeviceModePointName": "高压侧Ubc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB002",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUbc",
    "DeviceModePointName": "高压侧Ubc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB003",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUca",
    "DeviceModePointName": "高压侧Uca",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB003",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUca",
    "DeviceModePointName": "高压侧Uca",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB003",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUca",
    "DeviceModePointName": "高压侧Uca",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB003",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUca",
    "DeviceModePointName": "高压侧Uca",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB004",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUa",
    "DeviceModePointName": "高压侧Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB004",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUa",
    "DeviceModePointName": "高压侧Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB004",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUa",
    "DeviceModePointName": "高压侧Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB004",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUa",
    "DeviceModePointName": "高压侧Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB005",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUb",
    "DeviceModePointName": "高压侧Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB005",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUb",
    "DeviceModePointName": "高压侧Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB005",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUb",
    "DeviceModePointName": "高压侧Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB005",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUb",
    "DeviceModePointName": "高压侧Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB006",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUc",
    "DeviceModePointName": "高压侧Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB006",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUc",
    "DeviceModePointName": "高压侧Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB006",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUc",
    "DeviceModePointName": "高压侧Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB006",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPPhVUc",
    "DeviceModePointName": "高压侧Uc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB009",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriAIa",
    "DeviceModePointName": "高压侧Ia",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB009",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriAIa",
    "DeviceModePointName": "高压侧Ia",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB009",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriAIa",
    "DeviceModePointName": "高压侧Ia",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB009",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriAIa",
    "DeviceModePointName": "高压侧Ia",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB010",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriAIb",
    "DeviceModePointName": "高压侧Ib",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB010",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriAIb",
    "DeviceModePointName": "高压侧Ib",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB010",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriAIb",
    "DeviceModePointName": "高压侧Ib",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB010",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriAIb",
    "DeviceModePointName": "高压侧Ib",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB011",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriAIc",
    "DeviceModePointName": "高压侧Ic",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB011",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriAIc",
    "DeviceModePointName": "高压侧Ic",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB011",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriAIc",
    "DeviceModePointName": "高压侧Ic",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB011",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriAIc",
    "DeviceModePointName": "高压侧Ic",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB013",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriW",
    "DeviceModePointName": "高压侧P",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB013",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriW",
    "DeviceModePointName": "高压侧P",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB013",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriW",
    "DeviceModePointName": "高压侧P",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB013",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriW",
    "DeviceModePointName": "高压侧P",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB014",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriVar",
    "DeviceModePointName": "高压侧Q",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB014",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriVar",
    "DeviceModePointName": "高压侧Q",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB014",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriVar",
    "DeviceModePointName": "高压侧Q",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB014",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriVar",
    "DeviceModePointName": "高压侧Q",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB015",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPF",
    "DeviceModePointName": "高压侧Cos",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB015",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPF",
    "DeviceModePointName": "高压侧Cos",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB015",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPF",
    "DeviceModePointName": "高压侧Cos",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB015",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriPF",
    "DeviceModePointName": "高压侧Cos",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB016",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriHz",
    "DeviceModePointName": "高压侧Fr",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB016",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriHz",
    "DeviceModePointName": "高压侧Fr",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB016",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriHz",
    "DeviceModePointName": "高压侧Fr",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB016",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "HiGriHz",
    "DeviceModePointName": "高压侧Fr",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB017",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUab",
    "DeviceModePointName": "低压侧Uab",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB017",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUab",
    "DeviceModePointName": "低压侧Uab",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB017",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUab",
    "DeviceModePointName": "低压侧Uab",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB017",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUab",
    "DeviceModePointName": "低压侧Uab",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB018",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUbc",
    "DeviceModePointName": "低压侧Ubc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB018",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUbc",
    "DeviceModePointName": "低压侧Ubc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB018",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUbc",
    "DeviceModePointName": "低压侧Ubc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB018",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUbc",
    "DeviceModePointName": "低压侧Ubc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB019",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUca",
    "DeviceModePointName": "低压侧Uca",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB019",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUca",
    "DeviceModePointName": "低压侧Uca",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB019",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUca",
    "DeviceModePointName": "低压侧Uca",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB019",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUca",
    "DeviceModePointName": "低压侧Uca",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB020",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUa",
    "DeviceModePointName": "低压侧Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB020",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUa",
    "DeviceModePointName": "低压侧Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB020",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUa",
    "DeviceModePointName": "低压侧Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB020",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUa",
    "DeviceModePointName": "低压侧Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB021",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUb",
    "DeviceModePointName": "低压侧Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB021",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUb",
    "DeviceModePointName": "低压侧Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB021",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUb",
    "DeviceModePointName": "低压侧Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB021",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUb",
    "DeviceModePointName": "低压侧Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB022",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUc",
    "DeviceModePointName": "低压侧Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB022",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUc",
    "DeviceModePointName": "低压侧Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB022",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUc",
    "DeviceModePointName": "低压侧Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB022",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPPhVUc",
    "DeviceModePointName": "低压侧Uc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB025",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriAIa",
    "DeviceModePointName": "低压侧Ia",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB025",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriAIa",
    "DeviceModePointName": "低压侧Ia",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB025",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriAIa",
    "DeviceModePointName": "低压侧Ia",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB025",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriAIa",
    "DeviceModePointName": "低压侧Ia",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB026",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriAIb",
    "DeviceModePointName": "低压侧Ib",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB026",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriAIb",
    "DeviceModePointName": "低压侧Ib",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB026",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriAIb",
    "DeviceModePointName": "低压侧Ib",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB026",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriAIb",
    "DeviceModePointName": "低压侧Ib",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB027",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriAIc",
    "DeviceModePointName": "低压侧Ic",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB027",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriAIc",
    "DeviceModePointName": "低压侧Ic",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB027",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriAIc",
    "DeviceModePointName": "低压侧Ic",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB027",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriAIc",
    "DeviceModePointName": "低压侧Ic",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB029",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriW",
    "DeviceModePointName": "低压侧P",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB029",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriW",
    "DeviceModePointName": "低压侧P",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB029",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriW",
    "DeviceModePointName": "低压侧P",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB029",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriW",
    "DeviceModePointName": "低压侧P",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB030",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriVar",
    "DeviceModePointName": "低压侧Q",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB030",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriVar",
    "DeviceModePointName": "低压侧Q",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB030",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriVar",
    "DeviceModePointName": "低压侧Q",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB030",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriVar",
    "DeviceModePointName": "低压侧Q",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB031",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPF",
    "DeviceModePointName": "低压侧Cos",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB031",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPF",
    "DeviceModePointName": "低压侧Cos",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB031",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPF",
    "DeviceModePointName": "低压侧Cos",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB031",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriPF",
    "DeviceModePointName": "低压侧Cos",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB032",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriHz",
    "DeviceModePointName": "低压侧Fr",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB032",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriHz",
    "DeviceModePointName": "低压侧Fr",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB032",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriHz",
    "DeviceModePointName": "低压侧Fr",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB032",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "LoGriHz",
    "DeviceModePointName": "低压侧Fr",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB033",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "WinTmp",
    "DeviceModePointName": "主变绕组温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB033",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "WinTmp",
    "DeviceModePointName": "主变绕组温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB033",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "WinTmp",
    "DeviceModePointName": "主变绕组温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB033",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "WinTmp",
    "DeviceModePointName": "主变绕组温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB034",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "OilTmp1",
    "DeviceModePointName": "主变油温1",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB034",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "OilTmp1",
    "DeviceModePointName": "主变油温1",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB034",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "OilTmp1",
    "DeviceModePointName": "主变油温1",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB034",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "OilTmp1",
    "DeviceModePointName": "主变油温1",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB035",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "OilTmp2",
    "DeviceModePointName": "主变油温2",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB035",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "OilTmp2",
    "DeviceModePointName": "主变油温2",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB035",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "OilTmp2",
    "DeviceModePointName": "主变油温2",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB035",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "OilTmp2",
    "DeviceModePointName": "主变油温2",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB036",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "Stl",
    "DeviceModePointName": "档位",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB036",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "Stl",
    "DeviceModePointName": "档位",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB036",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "Stl",
    "DeviceModePointName": "档位",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB036",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceModePointIECName": "Stl",
    "DeviceModePointName": "档位",
    "CalcMethod": "Std",
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
    "DeviceModeCode": 14,
    "DeviceCode": 1,
    "DeviceFullCode": "393M201M14M1",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M1",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 2,
    "DeviceFullCode": "393M201M14M2",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M1",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 3,
    "DeviceFullCode": "393M201M14M3",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M2",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 4,
    "DeviceFullCode": "393M201M14M4",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M2",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 5,
    "DeviceFullCode": "393M201M14M5",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M3",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 6,
    "DeviceFullCode": "393M201M14M6",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M3",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 7,
    "DeviceFullCode": "393M201M14M7",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M4",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 8,
    "DeviceFullCode": "393M201M14M8",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M4",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 9,
    "DeviceFullCode": "393M201M14M9",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M5",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 10,
    "DeviceFullCode": "393M201M14M10",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M5",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 11,
    "DeviceFullCode": "393M201M14M11",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M6",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 12,
    "DeviceFullCode": "393M201M14M12",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M6",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 13,
    "DeviceFullCode": "393M201M14M13",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M7",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 14,
    "DeviceFullCode": "393M201M14M14",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M7",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 15,
    "DeviceFullCode": "393M201M14M15",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M8",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 16,
    "DeviceFullCode": "393M201M14M16",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M8",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 17,
    "DeviceFullCode": "393M201M14M17",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M9",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 18,
    "DeviceFullCode": "393M201M14M18",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M9",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 19,
    "DeviceFullCode": "393M201M14M19",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M10",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 20,
    "DeviceFullCode": "393M201M14M20",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M10",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 21,
    "DeviceFullCode": "393M201M14M21",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M11",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 22,
    "DeviceFullCode": "393M201M14M22",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M11",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 23,
    "DeviceFullCode": "393M201M14M23",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M12",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 24,
    "DeviceFullCode": "393M201M14M24",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M12",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 25,
    "DeviceFullCode": "393M201M14M25",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M13",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 26,
    "DeviceFullCode": "393M201M14M26",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M13",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 27,
    "DeviceFullCode": "393M201M14M27",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M14",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 28,
    "DeviceFullCode": "393M201M14M28",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M14",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 29,
    "DeviceFullCode": "393M201M14M29",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M15",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 30,
    "DeviceFullCode": "393M201M14M30",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M15",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 31,
    "DeviceFullCode": "393M201M14M31",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M16",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 32,
    "DeviceFullCode": "393M201M14M32",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M16",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 33,
    "DeviceFullCode": "393M201M14M33",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M17",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 34,
    "DeviceFullCode": "393M201M14M34",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M17",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 35,
    "DeviceFullCode": "393M201M14M35",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M18",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 36,
    "DeviceFullCode": "393M201M14M36",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M18",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 37,
    "DeviceFullCode": "393M201M14M37",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M19",
    "Capacity": 604.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 38,
    "DeviceFullCode": "393M201M14M38",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M19",
    "Capacity": 496.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 39,
    "DeviceFullCode": "393M201M14M39",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M20",
    "Capacity": 604.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 14,
    "DeviceCode": 40,
    "DeviceFullCode": "393M201M14M40",
    "DeviceModeFullCode": "393M201M14",
    "PDeviceFullCode": "393M204M2M20",
    "Capacity": 496.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 1,
    "DeviceFullCode": "393M202M13M1",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 2,
    "DeviceFullCode": "393M202M13M2",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 3,
    "DeviceFullCode": "393M202M13M3",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 4,
    "DeviceFullCode": "393M202M13M4",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 5,
    "DeviceFullCode": "393M202M13M5",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 6,
    "DeviceFullCode": "393M202M13M6",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 7,
    "DeviceFullCode": "393M202M13M7",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 8,
    "DeviceFullCode": "393M202M13M8",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 9,
    "DeviceFullCode": "393M202M13M9",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 10,
    "DeviceFullCode": "393M202M13M10",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 11,
    "DeviceFullCode": "393M202M13M11",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 12,
    "DeviceFullCode": "393M202M13M12",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 13,
    "DeviceFullCode": "393M202M13M13",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 14,
    "DeviceFullCode": "393M202M13M14",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 15,
    "DeviceFullCode": "393M202M13M15",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 16,
    "DeviceFullCode": "393M202M13M16",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 17,
    "DeviceFullCode": "393M202M13M17",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 18,
    "DeviceFullCode": "393M202M13M18",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 19,
    "DeviceFullCode": "393M202M13M19",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 20,
    "DeviceFullCode": "393M202M13M20",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 21,
    "DeviceFullCode": "393M202M13M21",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 22,
    "DeviceFullCode": "393M202M13M22",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 23,
    "DeviceFullCode": "393M202M13M23",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 24,
    "DeviceFullCode": "393M202M13M24",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 25,
    "DeviceFullCode": "393M202M13M25",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 26,
    "DeviceFullCode": "393M202M13M26",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 27,
    "DeviceFullCode": "393M202M13M27",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 28,
    "DeviceFullCode": "393M202M13M28",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 29,
    "DeviceFullCode": "393M202M13M29",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 30,
    "DeviceFullCode": "393M202M13M30",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 31,
    "DeviceFullCode": "393M202M13M31",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 32,
    "DeviceFullCode": "393M202M13M32",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 33,
    "DeviceFullCode": "393M202M13M33",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 34,
    "DeviceFullCode": "393M202M13M34",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 35,
    "DeviceFullCode": "393M202M13M35",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 36,
    "DeviceFullCode": "393M202M13M36",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 37.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 37,
    "DeviceFullCode": "393M202M13M37",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 38,
    "DeviceFullCode": "393M202M13M38",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 39,
    "DeviceFullCode": "393M202M13M39",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 40,
    "DeviceFullCode": "393M202M13M40",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 41,
    "DeviceFullCode": "393M202M13M41",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 42,
    "DeviceFullCode": "393M202M13M42",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 43,
    "DeviceFullCode": "393M202M13M43",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 44,
    "DeviceFullCode": "393M202M13M44",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 45,
    "DeviceFullCode": "393M202M13M45",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 46,
    "DeviceFullCode": "393M202M13M46",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 47,
    "DeviceFullCode": "393M202M13M47",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 48,
    "DeviceFullCode": "393M202M13M48",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 49,
    "DeviceFullCode": "393M202M13M49",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 50,
    "DeviceFullCode": "393M202M13M50",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 51,
    "DeviceFullCode": "393M202M13M51",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 52,
    "DeviceFullCode": "393M202M13M52",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 53,
    "DeviceFullCode": "393M202M13M53",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 54,
    "DeviceFullCode": "393M202M13M54",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 55,
    "DeviceFullCode": "393M202M13M55",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 56,
    "DeviceFullCode": "393M202M13M56",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 57,
    "DeviceFullCode": "393M202M13M57",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 58,
    "DeviceFullCode": "393M202M13M58",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 59,
    "DeviceFullCode": "393M202M13M59",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 60,
    "DeviceFullCode": "393M202M13M60",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 61,
    "DeviceFullCode": "393M202M13M61",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 62,
    "DeviceFullCode": "393M202M13M62",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 63,
    "DeviceFullCode": "393M202M13M63",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 64,
    "DeviceFullCode": "393M202M13M64",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 65,
    "DeviceFullCode": "393M202M13M65",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 66,
    "DeviceFullCode": "393M202M13M66",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 67,
    "DeviceFullCode": "393M202M13M67",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 68,
    "DeviceFullCode": "393M202M13M68",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 69,
    "DeviceFullCode": "393M202M13M69",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 70,
    "DeviceFullCode": "393M202M13M70",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 71,
    "DeviceFullCode": "393M202M13M71",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 72,
    "DeviceFullCode": "393M202M13M72",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 73,
    "DeviceFullCode": "393M202M13M73",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 74,
    "DeviceFullCode": "393M202M13M74",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 75,
    "DeviceFullCode": "393M202M13M75",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 76,
    "DeviceFullCode": "393M202M13M76",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 77,
    "DeviceFullCode": "393M202M13M77",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 78,
    "DeviceFullCode": "393M202M13M78",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 79,
    "DeviceFullCode": "393M202M13M79",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 80,
    "DeviceFullCode": "393M202M13M80",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 81,
    "DeviceFullCode": "393M202M13M81",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 82,
    "DeviceFullCode": "393M202M13M82",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 83,
    "DeviceFullCode": "393M202M13M83",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 84,
    "DeviceFullCode": "393M202M13M84",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 85,
    "DeviceFullCode": "393M202M13M85",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 86,
    "DeviceFullCode": "393M202M13M86",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 87,
    "DeviceFullCode": "393M202M13M87",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 88,
    "DeviceFullCode": "393M202M13M88",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 89,
    "DeviceFullCode": "393M202M13M89",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 90,
    "DeviceFullCode": "393M202M13M90",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 91,
    "DeviceFullCode": "393M202M13M91",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 92,
    "DeviceFullCode": "393M202M13M92",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 93,
    "DeviceFullCode": "393M202M13M93",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 94,
    "DeviceFullCode": "393M202M13M94",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 95,
    "DeviceFullCode": "393M202M13M95",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 96,
    "DeviceFullCode": "393M202M13M96",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 97,
    "DeviceFullCode": "393M202M13M97",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 98,
    "DeviceFullCode": "393M202M13M98",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 99,
    "DeviceFullCode": "393M202M13M99",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 100,
    "DeviceFullCode": "393M202M13M100",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 101,
    "DeviceFullCode": "393M202M13M101",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 102,
    "DeviceFullCode": "393M202M13M102",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 103,
    "DeviceFullCode": "393M202M13M103",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 104,
    "DeviceFullCode": "393M202M13M104",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 105,
    "DeviceFullCode": "393M202M13M105",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 106,
    "DeviceFullCode": "393M202M13M106",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 107,
    "DeviceFullCode": "393M202M13M107",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 108,
    "DeviceFullCode": "393M202M13M108",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 109,
    "DeviceFullCode": "393M202M13M109",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 110,
    "DeviceFullCode": "393M202M13M110",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 111,
    "DeviceFullCode": "393M202M13M111",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 112,
    "DeviceFullCode": "393M202M13M112",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 113,
    "DeviceFullCode": "393M202M13M113",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 114,
    "DeviceFullCode": "393M202M13M114",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 115,
    "DeviceFullCode": "393M202M13M115",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 116,
    "DeviceFullCode": "393M202M13M116",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 117,
    "DeviceFullCode": "393M202M13M117",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 118,
    "DeviceFullCode": "393M202M13M118",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 119,
    "DeviceFullCode": "393M202M13M119",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 120,
    "DeviceFullCode": "393M202M13M120",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 121,
    "DeviceFullCode": "393M202M13M121",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 122,
    "DeviceFullCode": "393M202M13M122",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 123,
    "DeviceFullCode": "393M202M13M123",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 124,
    "DeviceFullCode": "393M202M13M124",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 125,
    "DeviceFullCode": "393M202M13M125",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 126,
    "DeviceFullCode": "393M202M13M126",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 127,
    "DeviceFullCode": "393M202M13M127",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 128,
    "DeviceFullCode": "393M202M13M128",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 129,
    "DeviceFullCode": "393M202M13M129",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 130,
    "DeviceFullCode": "393M202M13M130",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 131,
    "DeviceFullCode": "393M202M13M131",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 132,
    "DeviceFullCode": "393M202M13M132",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 133,
    "DeviceFullCode": "393M202M13M133",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 134,
    "DeviceFullCode": "393M202M13M134",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 135,
    "DeviceFullCode": "393M202M13M135",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 136,
    "DeviceFullCode": "393M202M13M136",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 137,
    "DeviceFullCode": "393M202M13M137",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 138,
    "DeviceFullCode": "393M202M13M138",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 139,
    "DeviceFullCode": "393M202M13M139",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 140,
    "DeviceFullCode": "393M202M13M140",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 141,
    "DeviceFullCode": "393M202M13M141",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 142,
    "DeviceFullCode": "393M202M13M142",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 143,
    "DeviceFullCode": "393M202M13M143",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 144,
    "DeviceFullCode": "393M202M13M144",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 145,
    "DeviceFullCode": "393M202M13M145",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 146,
    "DeviceFullCode": "393M202M13M146",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 147,
    "DeviceFullCode": "393M202M13M147",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 148,
    "DeviceFullCode": "393M202M13M148",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 149,
    "DeviceFullCode": "393M202M13M149",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 150,
    "DeviceFullCode": "393M202M13M150",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 151,
    "DeviceFullCode": "393M202M13M151",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 152,
    "DeviceFullCode": "393M202M13M152",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 153,
    "DeviceFullCode": "393M202M13M153",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 154,
    "DeviceFullCode": "393M202M13M154",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 155,
    "DeviceFullCode": "393M202M13M155",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 156,
    "DeviceFullCode": "393M202M13M156",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 157,
    "DeviceFullCode": "393M202M13M157",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 158,
    "DeviceFullCode": "393M202M13M158",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 159,
    "DeviceFullCode": "393M202M13M159",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 160,
    "DeviceFullCode": "393M202M13M160",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 161,
    "DeviceFullCode": "393M202M13M161",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 162,
    "DeviceFullCode": "393M202M13M162",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 163,
    "DeviceFullCode": "393M202M13M163",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 164,
    "DeviceFullCode": "393M202M13M164",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 165,
    "DeviceFullCode": "393M202M13M165",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 166,
    "DeviceFullCode": "393M202M13M166",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 167,
    "DeviceFullCode": "393M202M13M167",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 168,
    "DeviceFullCode": "393M202M13M168",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 169,
    "DeviceFullCode": "393M202M13M169",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 170,
    "DeviceFullCode": "393M202M13M170",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 171,
    "DeviceFullCode": "393M202M13M171",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 172,
    "DeviceFullCode": "393M202M13M172",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 173,
    "DeviceFullCode": "393M202M13M173",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 174,
    "DeviceFullCode": "393M202M13M174",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 175,
    "DeviceFullCode": "393M202M13M175",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 176,
    "DeviceFullCode": "393M202M13M176",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 177,
    "DeviceFullCode": "393M202M13M177",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 178,
    "DeviceFullCode": "393M202M13M178",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 179,
    "DeviceFullCode": "393M202M13M179",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 180,
    "DeviceFullCode": "393M202M13M180",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 181,
    "DeviceFullCode": "393M202M13M181",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 182,
    "DeviceFullCode": "393M202M13M182",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 183,
    "DeviceFullCode": "393M202M13M183",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 184,
    "DeviceFullCode": "393M202M13M184",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 185,
    "DeviceFullCode": "393M202M13M185",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 186,
    "DeviceFullCode": "393M202M13M186",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 187,
    "DeviceFullCode": "393M202M13M187",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 188,
    "DeviceFullCode": "393M202M13M188",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 189,
    "DeviceFullCode": "393M202M13M189",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 190,
    "DeviceFullCode": "393M202M13M190",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 191,
    "DeviceFullCode": "393M202M13M191",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 192,
    "DeviceFullCode": "393M202M13M192",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 193,
    "DeviceFullCode": "393M202M13M193",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 194,
    "DeviceFullCode": "393M202M13M194",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 195,
    "DeviceFullCode": "393M202M13M195",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 196,
    "DeviceFullCode": "393M202M13M196",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 197,
    "DeviceFullCode": "393M202M13M197",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 198,
    "DeviceFullCode": "393M202M13M198",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 199,
    "DeviceFullCode": "393M202M13M199",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 200,
    "DeviceFullCode": "393M202M13M200",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 201,
    "DeviceFullCode": "393M202M13M201",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 202,
    "DeviceFullCode": "393M202M13M202",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 203,
    "DeviceFullCode": "393M202M13M203",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 204,
    "DeviceFullCode": "393M202M13M204",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 205,
    "DeviceFullCode": "393M202M13M205",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 206,
    "DeviceFullCode": "393M202M13M206",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 207,
    "DeviceFullCode": "393M202M13M207",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 208,
    "DeviceFullCode": "393M202M13M208",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 209,
    "DeviceFullCode": "393M202M13M209",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 210,
    "DeviceFullCode": "393M202M13M210",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 211,
    "DeviceFullCode": "393M202M13M211",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 212,
    "DeviceFullCode": "393M202M13M212",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 213,
    "DeviceFullCode": "393M202M13M213",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 214,
    "DeviceFullCode": "393M202M13M214",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 215,
    "DeviceFullCode": "393M202M13M215",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 216,
    "DeviceFullCode": "393M202M13M216",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 217,
    "DeviceFullCode": "393M202M13M217",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 218,
    "DeviceFullCode": "393M202M13M218",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 219,
    "DeviceFullCode": "393M202M13M219",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 220,
    "DeviceFullCode": "393M202M13M220",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 221,
    "DeviceFullCode": "393M202M13M221",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 222,
    "DeviceFullCode": "393M202M13M222",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 223,
    "DeviceFullCode": "393M202M13M223",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 224,
    "DeviceFullCode": "393M202M13M224",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 225,
    "DeviceFullCode": "393M202M13M225",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 226,
    "DeviceFullCode": "393M202M13M226",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 227,
    "DeviceFullCode": "393M202M13M227",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 228,
    "DeviceFullCode": "393M202M13M228",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 229,
    "DeviceFullCode": "393M202M13M229",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 230,
    "DeviceFullCode": "393M202M13M230",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 231,
    "DeviceFullCode": "393M202M13M231",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 232,
    "DeviceFullCode": "393M202M13M232",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 233,
    "DeviceFullCode": "393M202M13M233",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 234,
    "DeviceFullCode": "393M202M13M234",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 235,
    "DeviceFullCode": "393M202M13M235",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 236,
    "DeviceFullCode": "393M202M13M236",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 237,
    "DeviceFullCode": "393M202M13M237",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 238,
    "DeviceFullCode": "393M202M13M238",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 239,
    "DeviceFullCode": "393M202M13M239",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 240,
    "DeviceFullCode": "393M202M13M240",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 241,
    "DeviceFullCode": "393M202M13M241",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 242,
    "DeviceFullCode": "393M202M13M242",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 243,
    "DeviceFullCode": "393M202M13M243",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 244,
    "DeviceFullCode": "393M202M13M244",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 245,
    "DeviceFullCode": "393M202M13M245",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 246,
    "DeviceFullCode": "393M202M13M246",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 247,
    "DeviceFullCode": "393M202M13M247",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 248,
    "DeviceFullCode": "393M202M13M248",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 249,
    "DeviceFullCode": "393M202M13M249",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 250,
    "DeviceFullCode": "393M202M13M250",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 251,
    "DeviceFullCode": "393M202M13M251",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 252,
    "DeviceFullCode": "393M202M13M252",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 253,
    "DeviceFullCode": "393M202M13M253",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 254,
    "DeviceFullCode": "393M202M13M254",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 255,
    "DeviceFullCode": "393M202M13M255",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 256,
    "DeviceFullCode": "393M202M13M256",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 257,
    "DeviceFullCode": "393M202M13M257",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 258,
    "DeviceFullCode": "393M202M13M258",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 259,
    "DeviceFullCode": "393M202M13M259",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 260,
    "DeviceFullCode": "393M202M13M260",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 261,
    "DeviceFullCode": "393M202M13M261",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 262,
    "DeviceFullCode": "393M202M13M262",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 263,
    "DeviceFullCode": "393M202M13M263",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 264,
    "DeviceFullCode": "393M202M13M264",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 265,
    "DeviceFullCode": "393M202M13M265",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 266,
    "DeviceFullCode": "393M202M13M266",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 267,
    "DeviceFullCode": "393M202M13M267",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 268,
    "DeviceFullCode": "393M202M13M268",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 269,
    "DeviceFullCode": "393M202M13M269",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 270,
    "DeviceFullCode": "393M202M13M270",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 271,
    "DeviceFullCode": "393M202M13M271",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 272,
    "DeviceFullCode": "393M202M13M272",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 273,
    "DeviceFullCode": "393M202M13M273",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 274,
    "DeviceFullCode": "393M202M13M274",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 275,
    "DeviceFullCode": "393M202M13M275",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 276,
    "DeviceFullCode": "393M202M13M276",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 277,
    "DeviceFullCode": "393M202M13M277",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 278,
    "DeviceFullCode": "393M202M13M278",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 279,
    "DeviceFullCode": "393M202M13M279",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 13,
    "DeviceCode": 280,
    "DeviceFullCode": "393M202M13M280",
    "DeviceModeFullCode": "393M202M13",
    "PDeviceFullCode": None,
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 203,
    "DeviceModeCode": 13,
    "DeviceCode": 1,
    "DeviceFullCode": "393M203M13M1",
    "DeviceModeFullCode": "393M203M13",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 24,
    "DeviceCode": 1,
    "DeviceFullCode": "393M302M24M1",
    "DeviceModeFullCode": "393M302M24",
    "PDeviceFullCode": None,
    "Capacity": 11016.0000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 24,
    "DeviceCode": 2,
    "DeviceFullCode": "393M302M24M2",
    "DeviceModeFullCode": "393M302M24",
    "PDeviceFullCode": None,
    "Capacity": 11016.0000
  },
  {
    "DeviceTypeCode": 305,
    "DeviceModeCode": 16,
    "DeviceCode": 1,
    "DeviceFullCode": "393M305M16M1",
    "DeviceModeFullCode": "393M305M16",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 307,
    "DeviceModeCode": 22,
    "DeviceCode": 1,
    "DeviceFullCode": "393M307M22M1",
    "DeviceModeFullCode": "393M307M22",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 29,
    "DeviceCode": 1,
    "DeviceFullCode": "393M505M29M1",
    "DeviceModeFullCode": "393M505M29",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 29,
    "DeviceCode": 2,
    "DeviceFullCode": "393M505M29M2",
    "DeviceModeFullCode": "393M505M29",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 29,
    "DeviceCode": 3,
    "DeviceFullCode": "393M505M29M3",
    "DeviceModeFullCode": "393M505M29",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 29,
    "DeviceCode": 4,
    "DeviceFullCode": "393M505M29M4",
    "DeviceModeFullCode": "393M505M29",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 30,
    "DeviceCode": 5,
    "DeviceFullCode": "393M505M30M5",
    "DeviceModeFullCode": "393M505M30",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 14,
    "DeviceCode": 6,
    "DeviceFullCode": "393M505M14M6",
    "DeviceModeFullCode": "393M505M14",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 31,
    "DeviceCode": 7,
    "DeviceFullCode": "393M505M31M7",
    "DeviceModeFullCode": "393M505M31",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceCode": 1,
    "DeviceFullCode": "393M801M1M1",
    "DeviceModeFullCode": "393M801M1",
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
        self.stationCode = 393
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
            results = pool.map(self.___calcDeviceAggrega,[201,202,203,305,801])
            pool.close() 
            pool.join()
        except BaseException as err: 
            self.messages.append(str(err))
        finally:
            info=str(self.stationCode)+':success'
            if(len(self.q)):
                self.___insertIntoSql()
            if(len(self.messages)): 
                info=str(self.stationCode)+':'+';'.join(self.messages)

            result={"tableRow":self.azureTableRow,"sqlRow":len(self.q),"info":info}

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
                    if deviceTypeCode==203 and deviceItem['DeviceFullCode']=="393M203M13M1":
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
          result["info"] = jsonResult["info"] 
    except BaseException as err:  
       result["Status"] = 404
       result["tableRow"] = 0
       result["sqlRow"] = 0
       result["info"] = str(err)   

    return result
