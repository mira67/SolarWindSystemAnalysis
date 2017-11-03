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
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器日运行时间",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器日运行时间",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器日运行时间",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器日运行时间",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB030",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Inv_DC_W",
    "DeviceModePointName": "直流侧功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB030",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Inv_DC_W",
    "DeviceModePointName": "直流侧功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB030",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Inv_DC_W",
    "DeviceModePointName": "直流侧功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB030",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Inv_DC_W",
    "DeviceModePointName": "直流侧功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX601",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Back_Plate_Tmp2",
    "DeviceModePointName": "环境监测仪_标准气象站_2号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX601",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Back_Plate_Tmp2",
    "DeviceModePointName": "环境监测仪_标准气象站_2号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX601",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Back_Plate_Tmp2",
    "DeviceModePointName": "环境监测仪_标准气象站_2号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX601",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Back_Plate_Tmp2",
    "DeviceModePointName": "环境监测仪_标准气象站_2号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX602",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Back_Plate_Tmp3",
    "DeviceModePointName": "环境监测仪_标准气象站_3号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX602",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Back_Plate_Tmp3",
    "DeviceModePointName": "环境监测仪_标准气象站_3号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX602",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Back_Plate_Tmp3",
    "DeviceModePointName": "环境监测仪_标准气象站_3号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX602",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Back_Plate_Tmp3",
    "DeviceModePointName": "环境监测仪_标准气象站_3号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX603",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "环境监测仪_标准气象站_水平总辐射分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX603",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "环境监测仪_标准气象站_水平总辐射分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX603",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "环境监测仪_标准气象站_水平总辐射分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX603",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Hori_Radi_Min_Avg",
    "DeviceModePointName": "环境监测仪_标准气象站_水平总辐射分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX604",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "环境监测仪_标准气象站_斜面总辐射分钟平均",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX604",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "环境监测仪_标准气象站_斜面总辐射分钟平均",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX604",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "环境监测仪_标准气象站_斜面总辐射分钟平均",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX604",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Min_Avg",
    "DeviceModePointName": "环境监测仪_标准气象站_斜面总辐射分钟平均",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX601",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Back_Plate_Tmp1",
    "DeviceModePointName": "环境监测仪_老气象站_SG背板温度1",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX601",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Back_Plate_Tmp1",
    "DeviceModePointName": "环境监测仪_老气象站_SG背板温度1",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX601",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Back_Plate_Tmp1",
    "DeviceModePointName": "环境监测仪_老气象站_SG背板温度1",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX601",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Back_Plate_Tmp1",
    "DeviceModePointName": "环境监测仪_老气象站_SG背板温度1",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX602",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Back_Plate_Tmp2",
    "DeviceModePointName": "环境监测仪_老气象站_SG背板温度2",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX602",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Back_Plate_Tmp2",
    "DeviceModePointName": "环境监测仪_老气象站_SG背板温度2",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX602",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Back_Plate_Tmp2",
    "DeviceModePointName": "环境监测仪_老气象站_SG背板温度2",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX602",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Back_Plate_Tmp2",
    "DeviceModePointName": "环境监测仪_老气象站_SG背板温度2",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB004",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriPPhVUa",
    "DeviceModePointName": "高压侧Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB004",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriPPhVUa",
    "DeviceModePointName": "高压侧Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB004",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriPPhVUa",
    "DeviceModePointName": "高压侧Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB004",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriPPhVUa",
    "DeviceModePointName": "高压侧Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB005",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriPPhVUb",
    "DeviceModePointName": "高压侧Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB005",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriPPhVUb",
    "DeviceModePointName": "高压侧Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB005",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriPPhVUb",
    "DeviceModePointName": "高压侧Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB005",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriPPhVUb",
    "DeviceModePointName": "高压侧Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB006",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriPPhVUc",
    "DeviceModePointName": "高压侧Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB006",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriPPhVUc",
    "DeviceModePointName": "高压侧Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB006",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriPPhVUc",
    "DeviceModePointName": "高压侧Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB006",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriPPhVUc",
    "DeviceModePointName": "高压侧Uc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB009",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriAIa",
    "DeviceModePointName": "高压侧Ia",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB009",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriAIa",
    "DeviceModePointName": "高压侧Ia",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB009",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriAIa",
    "DeviceModePointName": "高压侧Ia",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB009",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriAIa",
    "DeviceModePointName": "高压侧Ia",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB010",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriAIb",
    "DeviceModePointName": "高压侧Ib",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB010",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriAIb",
    "DeviceModePointName": "高压侧Ib",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB010",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriAIb",
    "DeviceModePointName": "高压侧Ib",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB010",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriAIb",
    "DeviceModePointName": "高压侧Ib",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB011",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriAIc",
    "DeviceModePointName": "高压侧Ic",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB011",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriAIc",
    "DeviceModePointName": "高压侧Ic",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB011",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriAIc",
    "DeviceModePointName": "高压侧Ic",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB011",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriAIc",
    "DeviceModePointName": "高压侧Ic",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB013",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriW",
    "DeviceModePointName": "高压侧P",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB013",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriW",
    "DeviceModePointName": "高压侧P",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB013",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriW",
    "DeviceModePointName": "高压侧P",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB013",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriW",
    "DeviceModePointName": "高压侧P",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB014",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriVar",
    "DeviceModePointName": "高压侧Q",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB014",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriVar",
    "DeviceModePointName": "高压侧Q",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB014",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriVar",
    "DeviceModePointName": "高压侧Q",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB014",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriVar",
    "DeviceModePointName": "高压侧Q",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB015",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriPF",
    "DeviceModePointName": "高压侧Cos",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB015",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriPF",
    "DeviceModePointName": "高压侧Cos",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB015",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriPF",
    "DeviceModePointName": "高压侧Cos",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB015",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriPF",
    "DeviceModePointName": "高压侧Cos",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB016",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriHz",
    "DeviceModePointName": "高压侧Fr",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB016",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriHz",
    "DeviceModePointName": "高压侧Fr",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB016",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriHz",
    "DeviceModePointName": "高压侧Fr",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB016",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "HiGriHz",
    "DeviceModePointName": "高压侧Fr",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB020",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriPPhVUa",
    "DeviceModePointName": "低压侧Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB020",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriPPhVUa",
    "DeviceModePointName": "低压侧Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB020",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriPPhVUa",
    "DeviceModePointName": "低压侧Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB020",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriPPhVUa",
    "DeviceModePointName": "低压侧Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB021",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriPPhVUb",
    "DeviceModePointName": "低压侧Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB021",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriPPhVUb",
    "DeviceModePointName": "低压侧Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB021",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriPPhVUb",
    "DeviceModePointName": "低压侧Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB021",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriPPhVUb",
    "DeviceModePointName": "低压侧Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB022",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriPPhVUc",
    "DeviceModePointName": "低压侧Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB022",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriPPhVUc",
    "DeviceModePointName": "低压侧Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB022",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriPPhVUc",
    "DeviceModePointName": "低压侧Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB022",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriPPhVUc",
    "DeviceModePointName": "低压侧Uc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB025",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriAIa",
    "DeviceModePointName": "低压侧Ia",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB025",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriAIa",
    "DeviceModePointName": "低压侧Ia",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB025",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriAIa",
    "DeviceModePointName": "低压侧Ia",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB025",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriAIa",
    "DeviceModePointName": "低压侧Ia",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB026",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriAIb",
    "DeviceModePointName": "低压侧Ib",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB026",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriAIb",
    "DeviceModePointName": "低压侧Ib",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB026",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriAIb",
    "DeviceModePointName": "低压侧Ib",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB026",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriAIb",
    "DeviceModePointName": "低压侧Ib",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB027",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriAIc",
    "DeviceModePointName": "低压侧Ic",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB027",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriAIc",
    "DeviceModePointName": "低压侧Ic",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB027",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriAIc",
    "DeviceModePointName": "低压侧Ic",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB027",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriAIc",
    "DeviceModePointName": "低压侧Ic",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB029",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriW",
    "DeviceModePointName": "低压侧P",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB029",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriW",
    "DeviceModePointName": "低压侧P",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB029",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriW",
    "DeviceModePointName": "低压侧P",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB029",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriW",
    "DeviceModePointName": "低压侧P",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB030",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriVar",
    "DeviceModePointName": "低压侧Q",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB030",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriVar",
    "DeviceModePointName": "低压侧Q",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB030",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriVar",
    "DeviceModePointName": "低压侧Q",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB030",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriVar",
    "DeviceModePointName": "低压侧Q",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB031",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriPF",
    "DeviceModePointName": "低压侧Cos",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB031",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriPF",
    "DeviceModePointName": "低压侧Cos",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB031",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriPF",
    "DeviceModePointName": "低压侧Cos",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB031",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriPF",
    "DeviceModePointName": "低压侧Cos",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB032",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriHz",
    "DeviceModePointName": "低压侧Fr",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB032",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriHz",
    "DeviceModePointName": "低压侧Fr",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB032",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriHz",
    "DeviceModePointName": "低压侧Fr",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB032",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "LoGriHz",
    "DeviceModePointName": "低压侧Fr",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB034",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "OilTmp1",
    "DeviceModePointName": "主变油温1",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB034",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "OilTmp1",
    "DeviceModePointName": "主变油温1",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB034",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "OilTmp1",
    "DeviceModePointName": "主变油温1",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB034",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "OilTmp1",
    "DeviceModePointName": "主变油温1",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB035",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "OilTmp2",
    "DeviceModePointName": "主变油温2",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB035",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "OilTmp2",
    "DeviceModePointName": "主变油温2",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB035",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "OilTmp2",
    "DeviceModePointName": "主变油温2",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB035",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "OilTmp2",
    "DeviceModePointName": "主变油温2",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
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
    "DeviceModePointName": "全场有功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ003",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_W",
    "DeviceModePointName": "全场有功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ003",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_W",
    "DeviceModePointName": "全场有功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ003",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_W",
    "DeviceModePointName": "全场有功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ002",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Tilted_Radi_TotDly",
    "DeviceModePointName": "斜面曝幅值",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ002",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Tilted_Radi_TotDly",
    "DeviceModePointName": "斜面曝幅值",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ002",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Tilted_Radi_TotDly",
    "DeviceModePointName": "斜面曝幅值",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ004",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_TotWhDly",
    "DeviceModePointName": "全场日累计电量（逆变器出口）",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ004",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_TotWhDly",
    "DeviceModePointName": "全场日累计电量（逆变器出口）",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QZ004",
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PV_TotWhDly",
    "DeviceModePointName": "全场日累计电量（逆变器出口）",
    "CalcMethod": "Dif",
    "Divation": 600
  }
]

allDevice=[
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 1,
    "DeviceFullCode": "350M201M2M1",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M1",
    "Capacity": 532.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 2,
    "DeviceFullCode": "350M201M2M2",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M1",
    "Capacity": 528.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 3,
    "DeviceFullCode": "350M201M2M3",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M2",
    "Capacity": 508.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 4,
    "DeviceFullCode": "350M201M2M4",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M2",
    "Capacity": 566.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 5,
    "DeviceFullCode": "350M201M2M5",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M3",
    "Capacity": 566.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 6,
    "DeviceFullCode": "350M201M2M6",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M3",
    "Capacity": 504.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 7,
    "DeviceFullCode": "350M201M2M7",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M4",
    "Capacity": 537.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 8,
    "DeviceFullCode": "350M201M2M8",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M4",
    "Capacity": 537.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 9,
    "DeviceFullCode": "350M201M2M9",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M5",
    "Capacity": 542.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 10,
    "DeviceFullCode": "350M201M2M10",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M5",
    "Capacity": 537.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 11,
    "DeviceFullCode": "350M201M2M11",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M6",
    "Capacity": 499.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 12,
    "DeviceFullCode": "350M201M2M12",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M6",
    "Capacity": 398.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 13,
    "DeviceFullCode": "350M201M2M13",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M7",
    "Capacity": 532.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 14,
    "DeviceFullCode": "350M201M2M14",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M7",
    "Capacity": 513.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 15,
    "DeviceFullCode": "350M201M2M15",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M8",
    "Capacity": 532.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 16,
    "DeviceFullCode": "350M201M2M16",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M8",
    "Capacity": 513.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 17,
    "DeviceFullCode": "350M201M2M17",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M9",
    "Capacity": 556.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 18,
    "DeviceFullCode": "350M201M2M18",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M9",
    "Capacity": 504.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 19,
    "DeviceFullCode": "350M201M2M19",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M10",
    "Capacity": 432.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 20,
    "DeviceFullCode": "350M201M2M20",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M10",
    "Capacity": 422.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 21,
    "DeviceFullCode": "350M201M2M21",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M11",
    "Capacity": 470.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 22,
    "DeviceFullCode": "350M201M2M22",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M11",
    "Capacity": 508.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 23,
    "DeviceFullCode": "350M201M2M23",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M12",
    "Capacity": 494.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 24,
    "DeviceFullCode": "350M201M2M24",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M12",
    "Capacity": 513.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 25,
    "DeviceFullCode": "350M201M2M25",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M13",
    "Capacity": 590.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 26,
    "DeviceFullCode": "350M201M2M26",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M13",
    "Capacity": 595.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 27,
    "DeviceFullCode": "350M201M2M27",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M14",
    "Capacity": 518.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 28,
    "DeviceFullCode": "350M201M2M28",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M14",
    "Capacity": 595.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 29,
    "DeviceFullCode": "350M201M2M29",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M15",
    "Capacity": 518.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 30,
    "DeviceFullCode": "350M201M2M30",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M15",
    "Capacity": 537.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 31,
    "DeviceFullCode": "350M201M2M31",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M16",
    "Capacity": 537.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 32,
    "DeviceFullCode": "350M201M2M32",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M16",
    "Capacity": 499.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 33,
    "DeviceFullCode": "350M201M2M33",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M17",
    "Capacity": 523.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 34,
    "DeviceFullCode": "350M201M2M34",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M17",
    "Capacity": 518.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 35,
    "DeviceFullCode": "350M201M2M35",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M18",
    "Capacity": 614.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 36,
    "DeviceFullCode": "350M201M2M36",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M18",
    "Capacity": 609.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 37,
    "DeviceFullCode": "350M201M2M37",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M19",
    "Capacity": 542.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 38,
    "DeviceFullCode": "350M201M2M38",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M19",
    "Capacity": 537.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 39,
    "DeviceFullCode": "350M201M2M39",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M20",
    "Capacity": 556.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 40,
    "DeviceFullCode": "350M201M2M40",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M20",
    "Capacity": 528.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 41,
    "DeviceFullCode": "350M201M2M41",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M21",
    "Capacity": 614.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 42,
    "DeviceFullCode": "350M201M2M42",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M21",
    "Capacity": 566.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 43,
    "DeviceFullCode": "350M201M2M43",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M22",
    "Capacity": 422.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 44,
    "DeviceFullCode": "350M201M2M44",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M22",
    "Capacity": 340.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 45,
    "DeviceFullCode": "350M201M2M45",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M23",
    "Capacity": 561.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 46,
    "DeviceFullCode": "350M201M2M46",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M23",
    "Capacity": 576.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 47,
    "DeviceFullCode": "350M201M2M47",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M24",
    "Capacity": 590.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 48,
    "DeviceFullCode": "350M201M2M48",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M24",
    "Capacity": 590.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 49,
    "DeviceFullCode": "350M201M2M49",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M25",
    "Capacity": 595.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 50,
    "DeviceFullCode": "350M201M2M50",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M25",
    "Capacity": 576.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 51,
    "DeviceFullCode": "350M201M2M51",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M26",
    "Capacity": 595.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 52,
    "DeviceFullCode": "350M201M2M52",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M26",
    "Capacity": 595.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 53,
    "DeviceFullCode": "350M201M2M53",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M27",
    "Capacity": 489.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 54,
    "DeviceFullCode": "350M201M2M54",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M27",
    "Capacity": 499.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 55,
    "DeviceFullCode": "350M201M2M55",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M28",
    "Capacity": 518.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 56,
    "DeviceFullCode": "350M201M2M56",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M28",
    "Capacity": 523.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 57,
    "DeviceFullCode": "350M201M2M57",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M29",
    "Capacity": 580.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 58,
    "DeviceFullCode": "350M201M2M58",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M29",
    "Capacity": 518.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 59,
    "DeviceFullCode": "350M201M2M59",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M30",
    "Capacity": 576.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 60,
    "DeviceFullCode": "350M201M2M60",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M30",
    "Capacity": 523.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 61,
    "DeviceFullCode": "350M201M2M61",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M31",
    "Capacity": 499.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 62,
    "DeviceFullCode": "350M201M2M62",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M31",
    "Capacity": 451.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 63,
    "DeviceFullCode": "350M201M2M63",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M32",
    "Capacity": 542.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 64,
    "DeviceFullCode": "350M201M2M64",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M32",
    "Capacity": 484.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 65,
    "DeviceFullCode": "350M201M2M65",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M33",
    "Capacity": 580.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 66,
    "DeviceFullCode": "350M201M2M66",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M33",
    "Capacity": 604.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 67,
    "DeviceFullCode": "350M201M2M67",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M34",
    "Capacity": 523.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 68,
    "DeviceFullCode": "350M201M2M68",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M34",
    "Capacity": 441.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 69,
    "DeviceFullCode": "350M201M2M69",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M35",
    "Capacity": 566.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 70,
    "DeviceFullCode": "350M201M2M70",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M35",
    "Capacity": 523.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 71,
    "DeviceFullCode": "350M201M2M71",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M36",
    "Capacity": 537.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 72,
    "DeviceFullCode": "350M201M2M72",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M36",
    "Capacity": 595.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 73,
    "DeviceFullCode": "350M201M2M73",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M37",
    "Capacity": 537.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 74,
    "DeviceFullCode": "350M201M2M74",
    "DeviceModeFullCode": "350M201M2",
    "PDeviceFullCode": "350M204M2M37",
    "Capacity": 537.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 1,
    "DeviceFullCode": "350M202M4M1",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M1",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 2,
    "DeviceFullCode": "350M202M4M2",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M1",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 3,
    "DeviceFullCode": "350M202M4M3",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M1",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 4,
    "DeviceFullCode": "350M202M4M4",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M1",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 5,
    "DeviceFullCode": "350M202M4M5",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M1",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 6,
    "DeviceFullCode": "350M202M4M6",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M1",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 7,
    "DeviceFullCode": "350M202M4M7",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M1",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 8,
    "DeviceFullCode": "350M202M4M8",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M2",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 9,
    "DeviceFullCode": "350M202M4M9",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M2",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 10,
    "DeviceFullCode": "350M202M4M10",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M2",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 11,
    "DeviceFullCode": "350M202M4M11",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M2",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 12,
    "DeviceFullCode": "350M202M4M12",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M2",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 13,
    "DeviceFullCode": "350M202M4M13",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M2",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 14,
    "DeviceFullCode": "350M202M4M14",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M2",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 15,
    "DeviceFullCode": "350M202M4M15",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M3",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 16,
    "DeviceFullCode": "350M202M4M16",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M3",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 17,
    "DeviceFullCode": "350M202M4M17",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M3",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 18,
    "DeviceFullCode": "350M202M4M18",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M3",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 19,
    "DeviceFullCode": "350M202M4M19",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M3",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 20,
    "DeviceFullCode": "350M202M4M20",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M3",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 21,
    "DeviceFullCode": "350M202M4M21",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M4",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 22,
    "DeviceFullCode": "350M202M4M22",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M4",
    "Capacity": 62.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 23,
    "DeviceFullCode": "350M202M4M23",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M4",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 24,
    "DeviceFullCode": "350M202M4M24",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M4",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 25,
    "DeviceFullCode": "350M202M4M25",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M4",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 26,
    "DeviceFullCode": "350M202M4M26",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M4",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 27,
    "DeviceFullCode": "350M202M4M27",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M4",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 28,
    "DeviceFullCode": "350M202M4M28",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M5",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 29,
    "DeviceFullCode": "350M202M4M29",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M5",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 30,
    "DeviceFullCode": "350M202M4M30",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M5",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 31,
    "DeviceFullCode": "350M202M4M31",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M5",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 32,
    "DeviceFullCode": "350M202M4M32",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M5",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 33,
    "DeviceFullCode": "350M202M4M33",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M5",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 34,
    "DeviceFullCode": "350M202M4M34",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M6",
    "Capacity": 62.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 35,
    "DeviceFullCode": "350M202M4M35",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M6",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 36,
    "DeviceFullCode": "350M202M4M36",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M6",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 37,
    "DeviceFullCode": "350M202M4M37",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M6",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 38,
    "DeviceFullCode": "350M202M4M38",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M6",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 39,
    "DeviceFullCode": "350M202M4M39",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M6",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 40,
    "DeviceFullCode": "350M202M4M40",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M7",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 41,
    "DeviceFullCode": "350M202M4M41",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M7",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 42,
    "DeviceFullCode": "350M202M4M42",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M7",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 43,
    "DeviceFullCode": "350M202M4M43",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M7",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 44,
    "DeviceFullCode": "350M202M4M44",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M7",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 45,
    "DeviceFullCode": "350M202M4M45",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M7",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 46,
    "DeviceFullCode": "350M202M4M46",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M7",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 47,
    "DeviceFullCode": "350M202M4M47",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M8",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 48,
    "DeviceFullCode": "350M202M4M48",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M8",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 49,
    "DeviceFullCode": "350M202M4M49",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M8",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 50,
    "DeviceFullCode": "350M202M4M50",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M8",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 51,
    "DeviceFullCode": "350M202M4M51",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M8",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 52,
    "DeviceFullCode": "350M202M4M52",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M8",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 53,
    "DeviceFullCode": "350M202M4M53",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M9",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 54,
    "DeviceFullCode": "350M202M4M54",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M9",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 55,
    "DeviceFullCode": "350M202M4M55",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M9",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 56,
    "DeviceFullCode": "350M202M4M56",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M9",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 57,
    "DeviceFullCode": "350M202M4M57",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M9",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 58,
    "DeviceFullCode": "350M202M4M58",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M9",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 59,
    "DeviceFullCode": "350M202M4M59",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M10",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 60,
    "DeviceFullCode": "350M202M4M60",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M10",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 61,
    "DeviceFullCode": "350M202M4M61",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M10",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 62,
    "DeviceFullCode": "350M202M4M62",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M10",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 63,
    "DeviceFullCode": "350M202M4M63",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M10",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 64,
    "DeviceFullCode": "350M202M4M64",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M10",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 65,
    "DeviceFullCode": "350M202M4M65",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M10",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 66,
    "DeviceFullCode": "350M202M4M66",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M11",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 67,
    "DeviceFullCode": "350M202M4M67",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M11",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 68,
    "DeviceFullCode": "350M202M4M68",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M11",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 69,
    "DeviceFullCode": "350M202M4M69",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M11",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 70,
    "DeviceFullCode": "350M202M4M70",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M11",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 71,
    "DeviceFullCode": "350M202M4M71",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M12",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 72,
    "DeviceFullCode": "350M202M4M72",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M12",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 73,
    "DeviceFullCode": "350M202M4M73",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M12",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 74,
    "DeviceFullCode": "350M202M4M74",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M12",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 75,
    "DeviceFullCode": "350M202M4M75",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M13",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 76,
    "DeviceFullCode": "350M202M4M76",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M13",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 77,
    "DeviceFullCode": "350M202M4M77",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M13",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 78,
    "DeviceFullCode": "350M202M4M78",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M13",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 79,
    "DeviceFullCode": "350M202M4M79",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M13",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 80,
    "DeviceFullCode": "350M202M4M80",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M14",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 81,
    "DeviceFullCode": "350M202M4M81",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M13",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 82,
    "DeviceFullCode": "350M202M4M82",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M14",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 83,
    "DeviceFullCode": "350M202M4M83",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M14",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 84,
    "DeviceFullCode": "350M202M4M84",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M14",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 85,
    "DeviceFullCode": "350M202M4M85",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M14",
    "Capacity": 62.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 86,
    "DeviceFullCode": "350M202M4M86",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M14",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 87,
    "DeviceFullCode": "350M202M4M87",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M14",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 88,
    "DeviceFullCode": "350M202M4M88",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M14",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 89,
    "DeviceFullCode": "350M202M4M89",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M15",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 90,
    "DeviceFullCode": "350M202M4M90",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M15",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 91,
    "DeviceFullCode": "350M202M4M91",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M15",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 92,
    "DeviceFullCode": "350M202M4M92",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M15",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 93,
    "DeviceFullCode": "350M202M4M93",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M15",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 94,
    "DeviceFullCode": "350M202M4M94",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M16",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 95,
    "DeviceFullCode": "350M202M4M95",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M15",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 96,
    "DeviceFullCode": "350M202M4M96",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M16",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 97,
    "DeviceFullCode": "350M202M4M97",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M15",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 98,
    "DeviceFullCode": "350M202M4M98",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M16",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 99,
    "DeviceFullCode": "350M202M4M99",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M16",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 100,
    "DeviceFullCode": "350M202M4M100",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M16",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 101,
    "DeviceFullCode": "350M202M4M101",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M16",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 102,
    "DeviceFullCode": "350M202M4M102",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M17",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 103,
    "DeviceFullCode": "350M202M4M103",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M17",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 104,
    "DeviceFullCode": "350M202M4M104",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M17",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 105,
    "DeviceFullCode": "350M202M4M105",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M17",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 106,
    "DeviceFullCode": "350M202M4M106",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M17",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 107,
    "DeviceFullCode": "350M202M4M107",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M18",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 108,
    "DeviceFullCode": "350M202M4M108",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M18",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 109,
    "DeviceFullCode": "350M202M4M109",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M18",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 110,
    "DeviceFullCode": "350M202M4M110",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M18",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 111,
    "DeviceFullCode": "350M202M4M111",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M18",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 112,
    "DeviceFullCode": "350M202M4M112",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M18",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 113,
    "DeviceFullCode": "350M202M4M113",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M19",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 114,
    "DeviceFullCode": "350M202M4M114",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M19",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 115,
    "DeviceFullCode": "350M202M4M115",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M19",
    "Capacity": 24.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 116,
    "DeviceFullCode": "350M202M4M116",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M19",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 117,
    "DeviceFullCode": "350M202M4M117",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M19",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 118,
    "DeviceFullCode": "350M202M4M118",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M19",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 119,
    "DeviceFullCode": "350M202M4M119",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M19",
    "Capacity": 24.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 120,
    "DeviceFullCode": "350M202M4M120",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M20",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 121,
    "DeviceFullCode": "350M202M4M121",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M20",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 122,
    "DeviceFullCode": "350M202M4M122",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M20",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 123,
    "DeviceFullCode": "350M202M4M123",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M20",
    "Capacity": 24.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 124,
    "DeviceFullCode": "350M202M4M124",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M20",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 125,
    "DeviceFullCode": "350M202M4M125",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M20",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 126,
    "DeviceFullCode": "350M202M4M126",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M20",
    "Capacity": 19.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 127,
    "DeviceFullCode": "350M202M4M127",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M21",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 128,
    "DeviceFullCode": "350M202M4M128",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M21",
    "Capacity": 19.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 129,
    "DeviceFullCode": "350M202M4M129",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M21",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 130,
    "DeviceFullCode": "350M202M4M130",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M21",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 131,
    "DeviceFullCode": "350M202M4M131",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M21",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 132,
    "DeviceFullCode": "350M202M4M132",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M22",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 133,
    "DeviceFullCode": "350M202M4M133",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M22",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 134,
    "DeviceFullCode": "350M202M4M134",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M22",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 135,
    "DeviceFullCode": "350M202M4M135",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M22",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 136,
    "DeviceFullCode": "350M202M4M136",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M23",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 137,
    "DeviceFullCode": "350M202M4M137",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M23",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 138,
    "DeviceFullCode": "350M202M4M138",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M23",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 139,
    "DeviceFullCode": "350M202M4M139",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M23",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 140,
    "DeviceFullCode": "350M202M4M140",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M24",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 141,
    "DeviceFullCode": "350M202M4M141",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M23",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 142,
    "DeviceFullCode": "350M202M4M142",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M23",
    "Capacity": 52.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 143,
    "DeviceFullCode": "350M202M4M143",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M24",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 144,
    "DeviceFullCode": "350M202M4M144",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M24",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 145,
    "DeviceFullCode": "350M202M4M145",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M24",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 146,
    "DeviceFullCode": "350M202M4M146",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M24",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 147,
    "DeviceFullCode": "350M202M4M147",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M24",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 148,
    "DeviceFullCode": "350M202M4M148",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M25",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 149,
    "DeviceFullCode": "350M202M4M149",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M25",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 150,
    "DeviceFullCode": "350M202M4M150",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M25",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 151,
    "DeviceFullCode": "350M202M4M151",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M25",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 152,
    "DeviceFullCode": "350M202M4M152",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M25",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 153,
    "DeviceFullCode": "350M202M4M153",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M25",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 154,
    "DeviceFullCode": "350M202M4M154",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M25",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 155,
    "DeviceFullCode": "350M202M4M155",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M25",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 156,
    "DeviceFullCode": "350M202M4M156",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M26",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 157,
    "DeviceFullCode": "350M202M4M157",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M26",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 158,
    "DeviceFullCode": "350M202M4M158",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M26",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 159,
    "DeviceFullCode": "350M202M4M159",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M26",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 160,
    "DeviceFullCode": "350M202M4M160",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M26",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 161,
    "DeviceFullCode": "350M202M4M161",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M26",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 162,
    "DeviceFullCode": "350M202M4M162",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M26",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 163,
    "DeviceFullCode": "350M202M4M163",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M26",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 164,
    "DeviceFullCode": "350M202M4M164",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M27",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 165,
    "DeviceFullCode": "350M202M4M165",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M27",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 166,
    "DeviceFullCode": "350M202M4M166",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M27",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 167,
    "DeviceFullCode": "350M202M4M167",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M27",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 168,
    "DeviceFullCode": "350M202M4M168",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M27",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 169,
    "DeviceFullCode": "350M202M4M169",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M27",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 170,
    "DeviceFullCode": "350M202M4M170",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M28",
    "Capacity": 62.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 171,
    "DeviceFullCode": "350M202M4M171",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M28",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 172,
    "DeviceFullCode": "350M202M4M172",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M28",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 173,
    "DeviceFullCode": "350M202M4M173",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M28",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 174,
    "DeviceFullCode": "350M202M4M174",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M28",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 175,
    "DeviceFullCode": "350M202M4M175",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M28",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 176,
    "DeviceFullCode": "350M202M4M176",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M28",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 177,
    "DeviceFullCode": "350M202M4M177",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M28",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 178,
    "DeviceFullCode": "350M202M4M178",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M29",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 179,
    "DeviceFullCode": "350M202M4M179",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M29",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 180,
    "DeviceFullCode": "350M202M4M180",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M29",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 181,
    "DeviceFullCode": "350M202M4M181",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M29",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 182,
    "DeviceFullCode": "350M202M4M182",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M29",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 183,
    "DeviceFullCode": "350M202M4M183",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M29",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 184,
    "DeviceFullCode": "350M202M4M184",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M29",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 185,
    "DeviceFullCode": "350M202M4M185",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M30",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 186,
    "DeviceFullCode": "350M202M4M186",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M30",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 187,
    "DeviceFullCode": "350M202M4M187",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M30",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 188,
    "DeviceFullCode": "350M202M4M188",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M30",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 189,
    "DeviceFullCode": "350M202M4M189",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M30",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 190,
    "DeviceFullCode": "350M202M4M190",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M30",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 191,
    "DeviceFullCode": "350M202M4M191",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M30",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 192,
    "DeviceFullCode": "350M202M4M192",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M31",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 193,
    "DeviceFullCode": "350M202M4M193",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M31",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 194,
    "DeviceFullCode": "350M202M4M194",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M31",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 195,
    "DeviceFullCode": "350M202M4M195",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M31",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 196,
    "DeviceFullCode": "350M202M4M196",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M31",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 197,
    "DeviceFullCode": "350M202M4M197",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M31",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 198,
    "DeviceFullCode": "350M202M4M198",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M31",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 199,
    "DeviceFullCode": "350M202M4M199",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M32",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 200,
    "DeviceFullCode": "350M202M4M200",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M32",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 201,
    "DeviceFullCode": "350M202M4M201",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M32",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 202,
    "DeviceFullCode": "350M202M4M202",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M32",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 203,
    "DeviceFullCode": "350M202M4M203",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M32",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 204,
    "DeviceFullCode": "350M202M4M204",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M32",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 205,
    "DeviceFullCode": "350M202M4M205",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M32",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 206,
    "DeviceFullCode": "350M202M4M206",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M33",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 207,
    "DeviceFullCode": "350M202M4M207",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M33",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 208,
    "DeviceFullCode": "350M202M4M208",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M33",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 209,
    "DeviceFullCode": "350M202M4M209",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M33",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 210,
    "DeviceFullCode": "350M202M4M210",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M33",
    "Capacity": 62.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 211,
    "DeviceFullCode": "350M202M4M211",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M33",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 212,
    "DeviceFullCode": "350M202M4M212",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M33",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 213,
    "DeviceFullCode": "350M202M4M213",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M34",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 214,
    "DeviceFullCode": "350M202M4M214",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M34",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 215,
    "DeviceFullCode": "350M202M4M215",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M34",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 216,
    "DeviceFullCode": "350M202M4M216",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M34",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 217,
    "DeviceFullCode": "350M202M4M217",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M34",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 218,
    "DeviceFullCode": "350M202M4M218",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M34",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 219,
    "DeviceFullCode": "350M202M4M219",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M34",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 220,
    "DeviceFullCode": "350M202M4M220",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M35",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 221,
    "DeviceFullCode": "350M202M4M221",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M35",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 222,
    "DeviceFullCode": "350M202M4M222",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M35",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 223,
    "DeviceFullCode": "350M202M4M223",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M35",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 224,
    "DeviceFullCode": "350M202M4M224",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M35",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 225,
    "DeviceFullCode": "350M202M4M225",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M35",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 226,
    "DeviceFullCode": "350M202M4M226",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M35",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 227,
    "DeviceFullCode": "350M202M4M227",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M35",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 228,
    "DeviceFullCode": "350M202M4M228",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M36",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 229,
    "DeviceFullCode": "350M202M4M229",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M36",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 230,
    "DeviceFullCode": "350M202M4M230",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M36",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 231,
    "DeviceFullCode": "350M202M4M231",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M36",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 232,
    "DeviceFullCode": "350M202M4M232",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M36",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 233,
    "DeviceFullCode": "350M202M4M233",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M36",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 234,
    "DeviceFullCode": "350M202M4M234",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M36",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 235,
    "DeviceFullCode": "350M202M4M235",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M36",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 236,
    "DeviceFullCode": "350M202M4M236",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M37",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 237,
    "DeviceFullCode": "350M202M4M237",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M37",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 238,
    "DeviceFullCode": "350M202M4M238",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M37",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 239,
    "DeviceFullCode": "350M202M4M239",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M37",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 240,
    "DeviceFullCode": "350M202M4M240",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M37",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 241,
    "DeviceFullCode": "350M202M4M241",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M38",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 242,
    "DeviceFullCode": "350M202M4M242",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M38",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 243,
    "DeviceFullCode": "350M202M4M243",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M38",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 244,
    "DeviceFullCode": "350M202M4M244",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M38",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 245,
    "DeviceFullCode": "350M202M4M245",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M38",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 246,
    "DeviceFullCode": "350M202M4M246",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M38",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 247,
    "DeviceFullCode": "350M202M4M247",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M38",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 248,
    "DeviceFullCode": "350M202M4M248",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M39",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 249,
    "DeviceFullCode": "350M202M4M249",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M39",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 250,
    "DeviceFullCode": "350M202M4M250",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M39",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 251,
    "DeviceFullCode": "350M202M4M251",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M39",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 252,
    "DeviceFullCode": "350M202M4M252",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M39",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 253,
    "DeviceFullCode": "350M202M4M253",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M39",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 254,
    "DeviceFullCode": "350M202M4M254",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M40",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 255,
    "DeviceFullCode": "350M202M4M255",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M40",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 256,
    "DeviceFullCode": "350M202M4M256",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M40",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 257,
    "DeviceFullCode": "350M202M4M257",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M40",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 258,
    "DeviceFullCode": "350M202M4M258",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M40",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 259,
    "DeviceFullCode": "350M202M4M259",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M40",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 260,
    "DeviceFullCode": "350M202M4M260",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M41",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 261,
    "DeviceFullCode": "350M202M4M261",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M41",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 262,
    "DeviceFullCode": "350M202M4M262",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M41",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 263,
    "DeviceFullCode": "350M202M4M263",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M41",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 264,
    "DeviceFullCode": "350M202M4M264",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M41",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 265,
    "DeviceFullCode": "350M202M4M265",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M41",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 266,
    "DeviceFullCode": "350M202M4M266",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M41",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 267,
    "DeviceFullCode": "350M202M4M267",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M41",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 268,
    "DeviceFullCode": "350M202M4M268",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M42",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 269,
    "DeviceFullCode": "350M202M4M269",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M42",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 270,
    "DeviceFullCode": "350M202M4M270",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M42",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 271,
    "DeviceFullCode": "350M202M4M271",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M42",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 272,
    "DeviceFullCode": "350M202M4M272",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M42",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 273,
    "DeviceFullCode": "350M202M4M273",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M42",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 274,
    "DeviceFullCode": "350M202M4M274",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M42",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 275,
    "DeviceFullCode": "350M202M4M275",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M43",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 276,
    "DeviceFullCode": "350M202M4M276",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M43",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 277,
    "DeviceFullCode": "350M202M4M277",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M43",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 278,
    "DeviceFullCode": "350M202M4M278",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M43",
    "Capacity": 38.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 279,
    "DeviceFullCode": "350M202M4M279",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M43",
    "Capacity": 33.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 280,
    "DeviceFullCode": "350M202M4M280",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M43",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 281,
    "DeviceFullCode": "350M202M4M281",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M44",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 282,
    "DeviceFullCode": "350M202M4M282",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M44",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 283,
    "DeviceFullCode": "350M202M4M283",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M45",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 284,
    "DeviceFullCode": "350M202M4M284",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M45",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 285,
    "DeviceFullCode": "350M202M4M285",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M45",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 286,
    "DeviceFullCode": "350M202M4M286",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M45",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 287,
    "DeviceFullCode": "350M202M4M287",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M45",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 288,
    "DeviceFullCode": "350M202M4M288",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M45",
    "Capacity": 52.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 289,
    "DeviceFullCode": "350M202M4M289",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M45",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 290,
    "DeviceFullCode": "350M202M4M290",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M45",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 291,
    "DeviceFullCode": "350M202M4M291",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M46",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 292,
    "DeviceFullCode": "350M202M4M292",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M46",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 293,
    "DeviceFullCode": "350M202M4M293",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M46",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 294,
    "DeviceFullCode": "350M202M4M294",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M46",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 295,
    "DeviceFullCode": "350M202M4M295",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M46",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 296,
    "DeviceFullCode": "350M202M4M296",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M46",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 297,
    "DeviceFullCode": "350M202M4M297",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M46",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 298,
    "DeviceFullCode": "350M202M4M298",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M46",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 299,
    "DeviceFullCode": "350M202M4M299",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M47",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 300,
    "DeviceFullCode": "350M202M4M300",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M47",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 301,
    "DeviceFullCode": "350M202M4M301",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M47",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 302,
    "DeviceFullCode": "350M202M4M302",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M47",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 303,
    "DeviceFullCode": "350M202M4M303",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M47",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 304,
    "DeviceFullCode": "350M202M4M304",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M47",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 305,
    "DeviceFullCode": "350M202M4M305",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M47",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 306,
    "DeviceFullCode": "350M202M4M306",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M47",
    "Capacity": 52.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 307,
    "DeviceFullCode": "350M202M4M307",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M48",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 308,
    "DeviceFullCode": "350M202M4M308",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M48",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 309,
    "DeviceFullCode": "350M202M4M309",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M48",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 310,
    "DeviceFullCode": "350M202M4M310",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M48",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 311,
    "DeviceFullCode": "350M202M4M311",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M48",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 312,
    "DeviceFullCode": "350M202M4M312",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M48",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 313,
    "DeviceFullCode": "350M202M4M313",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M48",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 314,
    "DeviceFullCode": "350M202M4M314",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M49",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 315,
    "DeviceFullCode": "350M202M4M315",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M49",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 316,
    "DeviceFullCode": "350M202M4M316",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M49",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 317,
    "DeviceFullCode": "350M202M4M317",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M49",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 318,
    "DeviceFullCode": "350M202M4M318",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M49",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 319,
    "DeviceFullCode": "350M202M4M319",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M49",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 320,
    "DeviceFullCode": "350M202M4M320",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M49",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 321,
    "DeviceFullCode": "350M202M4M321",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M49",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 322,
    "DeviceFullCode": "350M202M4M322",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M50",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 323,
    "DeviceFullCode": "350M202M4M323",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M50",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 324,
    "DeviceFullCode": "350M202M4M324",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M50",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 325,
    "DeviceFullCode": "350M202M4M325",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M50",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 326,
    "DeviceFullCode": "350M202M4M326",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M50",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 327,
    "DeviceFullCode": "350M202M4M327",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M50",
    "Capacity": 38.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 328,
    "DeviceFullCode": "350M202M4M328",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M50",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 329,
    "DeviceFullCode": "350M202M4M329",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M51",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 330,
    "DeviceFullCode": "350M202M4M330",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M51",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 331,
    "DeviceFullCode": "350M202M4M331",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M51",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 332,
    "DeviceFullCode": "350M202M4M332",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M51",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 333,
    "DeviceFullCode": "350M202M4M333",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M51",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 334,
    "DeviceFullCode": "350M202M4M334",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M51",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 335,
    "DeviceFullCode": "350M202M4M335",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M51",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 336,
    "DeviceFullCode": "350M202M4M336",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M52",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 337,
    "DeviceFullCode": "350M202M4M337",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M52",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 338,
    "DeviceFullCode": "350M202M4M338",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M52",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 339,
    "DeviceFullCode": "350M202M4M339",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M52",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 340,
    "DeviceFullCode": "350M202M4M340",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M52",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 341,
    "DeviceFullCode": "350M202M4M341",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M52",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 342,
    "DeviceFullCode": "350M202M4M342",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M52",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 343,
    "DeviceFullCode": "350M202M4M343",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M53",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 344,
    "DeviceFullCode": "350M202M4M344",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M53",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 345,
    "DeviceFullCode": "350M202M4M345",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M53",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 346,
    "DeviceFullCode": "350M202M4M346",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M53",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 347,
    "DeviceFullCode": "350M202M4M347",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M53",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 348,
    "DeviceFullCode": "350M202M4M348",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M53",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 349,
    "DeviceFullCode": "350M202M4M349",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M54",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 350,
    "DeviceFullCode": "350M202M4M350",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M54",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 351,
    "DeviceFullCode": "350M202M4M351",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M54",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 352,
    "DeviceFullCode": "350M202M4M352",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M54",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 353,
    "DeviceFullCode": "350M202M4M353",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M54",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 354,
    "DeviceFullCode": "350M202M4M354",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M54",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 355,
    "DeviceFullCode": "350M202M4M355",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M55",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 356,
    "DeviceFullCode": "350M202M4M356",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M55",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 357,
    "DeviceFullCode": "350M202M4M357",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M55",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 358,
    "DeviceFullCode": "350M202M4M358",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M55",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 359,
    "DeviceFullCode": "350M202M4M359",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M55",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 360,
    "DeviceFullCode": "350M202M4M360",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M55",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 361,
    "DeviceFullCode": "350M202M4M361",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M56",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 362,
    "DeviceFullCode": "350M202M4M362",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M56",
    "Capacity": 62.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 363,
    "DeviceFullCode": "350M202M4M363",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M56",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 364,
    "DeviceFullCode": "350M202M4M364",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M56",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 365,
    "DeviceFullCode": "350M202M4M365",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M56",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 366,
    "DeviceFullCode": "350M202M4M366",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M56",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 367,
    "DeviceFullCode": "350M202M4M367",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M56",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 368,
    "DeviceFullCode": "350M202M4M368",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M57",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 369,
    "DeviceFullCode": "350M202M4M369",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M57",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 370,
    "DeviceFullCode": "350M202M4M370",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M57",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 371,
    "DeviceFullCode": "350M202M4M371",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M57",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 372,
    "DeviceFullCode": "350M202M4M372",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M57",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 373,
    "DeviceFullCode": "350M202M4M373",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M57",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 374,
    "DeviceFullCode": "350M202M4M374",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M57",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 375,
    "DeviceFullCode": "350M202M4M375",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M57",
    "Capacity": 43.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 376,
    "DeviceFullCode": "350M202M4M376",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M58",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 377,
    "DeviceFullCode": "350M202M4M377",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M58",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 378,
    "DeviceFullCode": "350M202M4M378",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M58",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 379,
    "DeviceFullCode": "350M202M4M379",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M58",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 380,
    "DeviceFullCode": "350M202M4M380",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M58",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 381,
    "DeviceFullCode": "350M202M4M381",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M58",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 382,
    "DeviceFullCode": "350M202M4M382",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M58",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 383,
    "DeviceFullCode": "350M202M4M383",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M59",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 384,
    "DeviceFullCode": "350M202M4M384",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M59",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 385,
    "DeviceFullCode": "350M202M4M385",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M59",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 386,
    "DeviceFullCode": "350M202M4M386",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M59",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 387,
    "DeviceFullCode": "350M202M4M387",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M59",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 388,
    "DeviceFullCode": "350M202M4M388",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M59",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 389,
    "DeviceFullCode": "350M202M4M389",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M60",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 390,
    "DeviceFullCode": "350M202M4M390",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M60",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 391,
    "DeviceFullCode": "350M202M4M391",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M60",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 392,
    "DeviceFullCode": "350M202M4M392",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M60",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 393,
    "DeviceFullCode": "350M202M4M393",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M60",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 394,
    "DeviceFullCode": "350M202M4M394",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M61",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 395,
    "DeviceFullCode": "350M202M4M395",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M61",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 396,
    "DeviceFullCode": "350M202M4M396",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M61",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 397,
    "DeviceFullCode": "350M202M4M397",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M61",
    "Capacity": 38.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 398,
    "DeviceFullCode": "350M202M4M398",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M61",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 399,
    "DeviceFullCode": "350M202M4M399",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M61",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 400,
    "DeviceFullCode": "350M202M4M400",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M61",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 401,
    "DeviceFullCode": "350M202M4M401",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M62",
    "Capacity": 38.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 402,
    "DeviceFullCode": "350M202M4M402",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M62",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 403,
    "DeviceFullCode": "350M202M4M403",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M62",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 404,
    "DeviceFullCode": "350M202M4M404",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M62",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 405,
    "DeviceFullCode": "350M202M4M405",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M62",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 406,
    "DeviceFullCode": "350M202M4M406",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M63",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 407,
    "DeviceFullCode": "350M202M4M407",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M63",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 408,
    "DeviceFullCode": "350M202M4M408",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M63",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 409,
    "DeviceFullCode": "350M202M4M409",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M63",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 410,
    "DeviceFullCode": "350M202M4M410",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M63",
    "Capacity": 24.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 411,
    "DeviceFullCode": "350M202M4M411",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M63",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 412,
    "DeviceFullCode": "350M202M4M412",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M63",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 413,
    "DeviceFullCode": "350M202M4M413",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M64",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 414,
    "DeviceFullCode": "350M202M4M414",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M64",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 415,
    "DeviceFullCode": "350M202M4M415",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M64",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 416,
    "DeviceFullCode": "350M202M4M416",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M64",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 417,
    "DeviceFullCode": "350M202M4M417",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M64",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 418,
    "DeviceFullCode": "350M202M4M418",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M64",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 419,
    "DeviceFullCode": "350M202M4M419",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M65",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 420,
    "DeviceFullCode": "350M202M4M420",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M65",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 421,
    "DeviceFullCode": "350M202M4M421",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M65",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 422,
    "DeviceFullCode": "350M202M4M422",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M65",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 423,
    "DeviceFullCode": "350M202M4M423",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M65",
    "Capacity": 72.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 424,
    "DeviceFullCode": "350M202M4M424",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M65",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 425,
    "DeviceFullCode": "350M202M4M425",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M65",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 426,
    "DeviceFullCode": "350M202M4M426",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M65",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 427,
    "DeviceFullCode": "350M202M4M427",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M66",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 428,
    "DeviceFullCode": "350M202M4M428",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M66",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 429,
    "DeviceFullCode": "350M202M4M429",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M66",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 430,
    "DeviceFullCode": "350M202M4M430",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M66",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 431,
    "DeviceFullCode": "350M202M4M431",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M66",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 432,
    "DeviceFullCode": "350M202M4M432",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M66",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 433,
    "DeviceFullCode": "350M202M4M433",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M66",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 434,
    "DeviceFullCode": "350M202M4M434",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M66",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 435,
    "DeviceFullCode": "350M202M4M435",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M67",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 436,
    "DeviceFullCode": "350M202M4M436",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M67",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 437,
    "DeviceFullCode": "350M202M4M437",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M67",
    "Capacity": 67.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 438,
    "DeviceFullCode": "350M202M4M438",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M67",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 439,
    "DeviceFullCode": "350M202M4M439",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M67",
    "Capacity": 43.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 440,
    "DeviceFullCode": "350M202M4M440",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M68",
    "Capacity": 48.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 441,
    "DeviceFullCode": "350M202M4M441",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M68",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 442,
    "DeviceFullCode": "350M202M4M442",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M68",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 443,
    "DeviceFullCode": "350M202M4M443",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M68",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 444,
    "DeviceFullCode": "350M202M4M444",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M68",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 445,
    "DeviceFullCode": "350M202M4M445",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M69",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 446,
    "DeviceFullCode": "350M202M4M446",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M69",
    "Capacity": 48.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 447,
    "DeviceFullCode": "350M202M4M447",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M69",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 448,
    "DeviceFullCode": "350M202M4M448",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M69",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 449,
    "DeviceFullCode": "350M202M4M449",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M69",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 450,
    "DeviceFullCode": "350M202M4M450",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M69",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 451,
    "DeviceFullCode": "350M202M4M451",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M69",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 452,
    "DeviceFullCode": "350M202M4M452",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M69",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 453,
    "DeviceFullCode": "350M202M4M453",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M70",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 454,
    "DeviceFullCode": "350M202M4M454",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M70",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 455,
    "DeviceFullCode": "350M202M4M455",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M70",
    "Capacity": 62.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 456,
    "DeviceFullCode": "350M202M4M456",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M70",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 457,
    "DeviceFullCode": "350M202M4M457",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M70",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 458,
    "DeviceFullCode": "350M202M4M458",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M70",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 459,
    "DeviceFullCode": "350M202M4M459",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M70",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 460,
    "DeviceFullCode": "350M202M4M460",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M70",
    "Capacity": 38.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 461,
    "DeviceFullCode": "350M202M4M461",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M71",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 462,
    "DeviceFullCode": "350M202M4M462",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M71",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 463,
    "DeviceFullCode": "350M202M4M463",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M71",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 464,
    "DeviceFullCode": "350M202M4M464",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M71",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 465,
    "DeviceFullCode": "350M202M4M465",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M71",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 466,
    "DeviceFullCode": "350M202M4M466",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M71",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 467,
    "DeviceFullCode": "350M202M4M467",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M71",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 468,
    "DeviceFullCode": "350M202M4M468",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M72",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 469,
    "DeviceFullCode": "350M202M4M469",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M72",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 470,
    "DeviceFullCode": "350M202M4M470",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M72",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 471,
    "DeviceFullCode": "350M202M4M471",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M72",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 472,
    "DeviceFullCode": "350M202M4M472",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M72",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 473,
    "DeviceFullCode": "350M202M4M473",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M72",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 474,
    "DeviceFullCode": "350M202M4M474",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M72",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 475,
    "DeviceFullCode": "350M202M4M475",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M72",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 476,
    "DeviceFullCode": "350M202M4M476",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M73",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 477,
    "DeviceFullCode": "350M202M4M477",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M73",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 478,
    "DeviceFullCode": "350M202M4M478",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M73",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 479,
    "DeviceFullCode": "350M202M4M479",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M73",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 480,
    "DeviceFullCode": "350M202M4M480",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M73",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 481,
    "DeviceFullCode": "350M202M4M481",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M74",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 482,
    "DeviceFullCode": "350M202M4M482",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M74",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 483,
    "DeviceFullCode": "350M202M4M483",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M74",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 484,
    "DeviceFullCode": "350M202M4M484",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M74",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 485,
    "DeviceFullCode": "350M202M4M485",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M74",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 486,
    "DeviceFullCode": "350M202M4M486",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M74",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 487,
    "DeviceFullCode": "350M202M4M487",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M74",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 488,
    "DeviceFullCode": "350M202M4M488",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M74",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 4,
    "DeviceCode": 489,
    "DeviceFullCode": "350M202M4M489",
    "DeviceModeFullCode": "350M202M4",
    "PDeviceFullCode": "350M201M2M74",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 490,
    "DeviceFullCode": "350M202M3M490",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M3",
    "Capacity": 48.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 491,
    "DeviceFullCode": "350M202M3M491",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M4",
    "Capacity": 43.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 492,
    "DeviceFullCode": "350M202M3M492",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M5",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 493,
    "DeviceFullCode": "350M202M3M493",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M5",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 494,
    "DeviceFullCode": "350M202M3M494",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M6",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 495,
    "DeviceFullCode": "350M202M3M495",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M8",
    "Capacity": 33.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 496,
    "DeviceFullCode": "350M202M3M496",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M8",
    "Capacity": 52.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 497,
    "DeviceFullCode": "350M202M3M497",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M9",
    "Capacity": 52.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 498,
    "DeviceFullCode": "350M202M3M498",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M9",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 499,
    "DeviceFullCode": "350M202M3M499",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M11",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 500,
    "DeviceFullCode": "350M202M3M500",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M11",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 501,
    "DeviceFullCode": "350M202M3M501",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M12",
    "Capacity": 33.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 502,
    "DeviceFullCode": "350M202M3M502",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M12",
    "Capacity": 19.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 503,
    "DeviceFullCode": "350M202M3M503",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M12",
    "Capacity": 38.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 504,
    "DeviceFullCode": "350M202M3M504",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M16",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 505,
    "DeviceFullCode": "350M202M3M505",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M17",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 506,
    "DeviceFullCode": "350M202M3M506",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M17",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 507,
    "DeviceFullCode": "350M202M3M507",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M17",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 508,
    "DeviceFullCode": "350M202M3M508",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M18",
    "Capacity": 43.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 509,
    "DeviceFullCode": "350M202M3M509",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M21",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 510,
    "DeviceFullCode": "350M202M3M510",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M21",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 511,
    "DeviceFullCode": "350M202M3M511",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M21",
    "Capacity": 28.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 512,
    "DeviceFullCode": "350M202M3M512",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M22",
    "Capacity": 38.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 513,
    "DeviceFullCode": "350M202M3M513",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M22",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 514,
    "DeviceFullCode": "350M202M3M514",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M22",
    "Capacity": 48.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 515,
    "DeviceFullCode": "350M202M3M515",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M22",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 516,
    "DeviceFullCode": "350M202M3M516",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M23",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 517,
    "DeviceFullCode": "350M202M3M517",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M24",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 518,
    "DeviceFullCode": "350M202M3M518",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M27",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 519,
    "DeviceFullCode": "350M202M3M519",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M37",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 520,
    "DeviceFullCode": "350M202M3M520",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M37",
    "Capacity": 52.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 521,
    "DeviceFullCode": "350M202M3M521",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M37",
    "Capacity": 52.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 522,
    "DeviceFullCode": "350M202M3M522",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M39",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 523,
    "DeviceFullCode": "350M202M3M523",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M39",
    "Capacity": 38.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 524,
    "DeviceFullCode": "350M202M3M524",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M40",
    "Capacity": 33.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 525,
    "DeviceFullCode": "350M202M3M525",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M40",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 526,
    "DeviceFullCode": "350M202M3M526",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M42",
    "Capacity": 28.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 527,
    "DeviceFullCode": "350M202M3M527",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M43",
    "Capacity": 43.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 528,
    "DeviceFullCode": "350M202M3M528",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M43",
    "Capacity": 48.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 529,
    "DeviceFullCode": "350M202M3M529",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M44",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 530,
    "DeviceFullCode": "350M202M3M530",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M44",
    "Capacity": 38.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 531,
    "DeviceFullCode": "350M202M3M531",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M44",
    "Capacity": 52.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 532,
    "DeviceFullCode": "350M202M3M532",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M48",
    "Capacity": 52.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 533,
    "DeviceFullCode": "350M202M3M533",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M49",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 534,
    "DeviceFullCode": "350M202M3M534",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M51",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 535,
    "DeviceFullCode": "350M202M3M535",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M52",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 536,
    "DeviceFullCode": "350M202M3M536",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M53",
    "Capacity": 28.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 537,
    "DeviceFullCode": "350M202M3M537",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M54",
    "Capacity": 43.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 538,
    "DeviceFullCode": "350M202M3M538",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M55",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 539,
    "DeviceFullCode": "350M202M3M539",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M59",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 540,
    "DeviceFullCode": "350M202M3M540",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M59",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 541,
    "DeviceFullCode": "350M202M3M541",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M60",
    "Capacity": 48.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 542,
    "DeviceFullCode": "350M202M3M542",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M60",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 543,
    "DeviceFullCode": "350M202M3M543",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M60",
    "Capacity": 43.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 544,
    "DeviceFullCode": "350M202M3M544",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M62",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 545,
    "DeviceFullCode": "350M202M3M545",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M62",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 546,
    "DeviceFullCode": "350M202M3M546",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M63",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 547,
    "DeviceFullCode": "350M202M3M547",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M64",
    "Capacity": 28.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 548,
    "DeviceFullCode": "350M202M3M548",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M67",
    "Capacity": 57.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 549,
    "DeviceFullCode": "350M202M3M549",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M67",
    "Capacity": 48.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 550,
    "DeviceFullCode": "350M202M3M550",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M67",
    "Capacity": 76.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 551,
    "DeviceFullCode": "350M202M3M551",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M68",
    "Capacity": 38.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 552,
    "DeviceFullCode": "350M202M3M552",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M68",
    "Capacity": 28.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 3,
    "DeviceCode": 553,
    "DeviceFullCode": "350M202M3M553",
    "DeviceModeFullCode": "350M202M3",
    "PDeviceFullCode": "350M201M2M68",
    "Capacity": 19.2000
  },
  {
    "DeviceTypeCode": 203,
    "DeviceModeCode": 4,
    "DeviceCode": 1,
    "DeviceFullCode": "350M203M4M1",
    "DeviceModeFullCode": "350M203M4",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 203,
    "DeviceModeCode": 3,
    "DeviceCode": 2,
    "DeviceFullCode": "350M203M3M2",
    "DeviceModeFullCode": "350M203M3",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceCode": 1,
    "DeviceFullCode": "350M302M8M1",
    "DeviceModeFullCode": "350M302M8",
    "PDeviceFullCode": None,
    "Capacity": 10267.2000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceCode": 2,
    "DeviceFullCode": "350M302M8M2",
    "DeviceModeFullCode": "350M302M8",
    "PDeviceFullCode": None,
    "Capacity": 8644.8000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceCode": 3,
    "DeviceFullCode": "350M302M8M3",
    "DeviceModeFullCode": "350M302M8",
    "PDeviceFullCode": None,
    "Capacity": 9777.6000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceCode": 4,
    "DeviceFullCode": "350M302M8M4",
    "DeviceModeFullCode": "350M302M8",
    "PDeviceFullCode": None,
    "Capacity": 10665.6000
  },
  {
    "DeviceTypeCode": 305,
    "DeviceModeCode": 5,
    "DeviceCode": 1,
    "DeviceFullCode": "350M305M5M1",
    "DeviceModeFullCode": "350M305M5",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 307,
    "DeviceModeCode": 6,
    "DeviceCode": 1,
    "DeviceFullCode": "350M307M6M1",
    "DeviceModeFullCode": "350M307M6",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 1,
    "DeviceFullCode": "350M505M2M1",
    "DeviceModeFullCode": "350M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 2,
    "DeviceFullCode": "350M505M2M2",
    "DeviceModeFullCode": "350M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 3,
    "DeviceFullCode": "350M505M2M3",
    "DeviceModeFullCode": "350M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 4,
    "DeviceFullCode": "350M505M2M4",
    "DeviceModeFullCode": "350M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 5,
    "DeviceFullCode": "350M505M2M5",
    "DeviceModeFullCode": "350M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 6,
    "DeviceFullCode": "350M505M2M6",
    "DeviceModeFullCode": "350M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 7,
    "DeviceFullCode": "350M505M2M7",
    "DeviceModeFullCode": "350M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 8,
    "DeviceFullCode": "350M505M2M8",
    "DeviceModeFullCode": "350M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceCode": 1,
    "DeviceFullCode": "350M801M1M1",
    "DeviceModeFullCode": "350M801M1",
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
        self.stationCode = 350
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
            results = pool.map(self.___calcDeviceAggrega,[201,202,203,302,305,307,505,801])
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
                    if deviceTypeCode==203 and deviceItem['DeviceFullCode']=="350M203M3M2":
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
