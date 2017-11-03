#-*- coding:utf-8 -*-



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
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
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
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
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
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX019",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Min",
    "DeviceModePointName": "水平面曝辐量分钟累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX020",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Min",
    "DeviceModePointName": "倾斜面曝辐量分钟累计(*1000)",
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
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX034",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Hori_Radi_Dly_Hr",
    "DeviceModePointName": "水平面曝辐量小时累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX035",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly_Hr",
    "DeviceModePointName": "倾斜面曝辐量小时累计(*1000)",
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
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB001",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUab",
    "DeviceModePointName": "高压侧Uab",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB001",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUab",
    "DeviceModePointName": "高压侧Uab",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB001",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUab",
    "DeviceModePointName": "高压侧Uab",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB001",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUab",
    "DeviceModePointName": "高压侧Uab",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB002",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUbc",
    "DeviceModePointName": "高压侧Ubc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB002",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUbc",
    "DeviceModePointName": "高压侧Ubc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB002",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUbc",
    "DeviceModePointName": "高压侧Ubc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB002",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUbc",
    "DeviceModePointName": "高压侧Ubc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB003",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUca",
    "DeviceModePointName": "高压侧Uca",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB003",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUca",
    "DeviceModePointName": "高压侧Uca",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB003",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUca",
    "DeviceModePointName": "高压侧Uca",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB003",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUca",
    "DeviceModePointName": "高压侧Uca",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB004",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUa",
    "DeviceModePointName": "高压侧Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB004",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUa",
    "DeviceModePointName": "高压侧Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB004",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUa",
    "DeviceModePointName": "高压侧Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB004",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUa",
    "DeviceModePointName": "高压侧Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB005",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUb",
    "DeviceModePointName": "高压侧Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB005",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUb",
    "DeviceModePointName": "高压侧Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB005",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUb",
    "DeviceModePointName": "高压侧Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB005",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUb",
    "DeviceModePointName": "高压侧Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB006",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUc",
    "DeviceModePointName": "高压侧Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB006",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUc",
    "DeviceModePointName": "高压侧Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB006",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUc",
    "DeviceModePointName": "高压侧Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB006",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPPhVUc",
    "DeviceModePointName": "高压侧Uc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB007",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGri3U0",
    "DeviceModePointName": "高压侧3U0",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB007",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGri3U0",
    "DeviceModePointName": "高压侧3U0",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB007",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGri3U0",
    "DeviceModePointName": "高压侧3U0",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB007",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGri3U0",
    "DeviceModePointName": "高压侧3U0",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB009",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriAIa",
    "DeviceModePointName": "高压侧Ia",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB009",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriAIa",
    "DeviceModePointName": "高压侧Ia",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB009",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriAIa",
    "DeviceModePointName": "高压侧Ia",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB009",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriAIa",
    "DeviceModePointName": "高压侧Ia",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB010",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriAIb",
    "DeviceModePointName": "高压侧Ib",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB010",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriAIb",
    "DeviceModePointName": "高压侧Ib",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB010",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriAIb",
    "DeviceModePointName": "高压侧Ib",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB010",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriAIb",
    "DeviceModePointName": "高压侧Ib",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB011",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriAIc",
    "DeviceModePointName": "高压侧Ic",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB011",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriAIc",
    "DeviceModePointName": "高压侧Ic",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB011",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriAIc",
    "DeviceModePointName": "高压侧Ic",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB011",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriAIc",
    "DeviceModePointName": "高压侧Ic",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB013",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriW",
    "DeviceModePointName": "高压侧P",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB013",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriW",
    "DeviceModePointName": "高压侧P",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB013",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriW",
    "DeviceModePointName": "高压侧P",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB013",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriW",
    "DeviceModePointName": "高压侧P",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB014",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriVar",
    "DeviceModePointName": "高压侧Q",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB014",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriVar",
    "DeviceModePointName": "高压侧Q",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB014",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriVar",
    "DeviceModePointName": "高压侧Q",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB014",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriVar",
    "DeviceModePointName": "高压侧Q",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB015",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPF",
    "DeviceModePointName": "高压侧Cos",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB015",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPF",
    "DeviceModePointName": "高压侧Cos",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB015",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPF",
    "DeviceModePointName": "高压侧Cos",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB015",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriPF",
    "DeviceModePointName": "高压侧Cos",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB016",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriHz",
    "DeviceModePointName": "高压侧Fr",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB016",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriHz",
    "DeviceModePointName": "高压侧Fr",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB016",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriHz",
    "DeviceModePointName": "高压侧Fr",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB016",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "HiGriHz",
    "DeviceModePointName": "高压侧Fr",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB017",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUab",
    "DeviceModePointName": "低压侧Uab",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB017",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUab",
    "DeviceModePointName": "低压侧Uab",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB017",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUab",
    "DeviceModePointName": "低压侧Uab",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB017",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUab",
    "DeviceModePointName": "低压侧Uab",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB018",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUbc",
    "DeviceModePointName": "低压侧Ubc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB018",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUbc",
    "DeviceModePointName": "低压侧Ubc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB018",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUbc",
    "DeviceModePointName": "低压侧Ubc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB018",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUbc",
    "DeviceModePointName": "低压侧Ubc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB019",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUca",
    "DeviceModePointName": "低压侧Uca",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB019",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUca",
    "DeviceModePointName": "低压侧Uca",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB019",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUca",
    "DeviceModePointName": "低压侧Uca",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB019",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUca",
    "DeviceModePointName": "低压侧Uca",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB020",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUa",
    "DeviceModePointName": "低压侧Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB020",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUa",
    "DeviceModePointName": "低压侧Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB020",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUa",
    "DeviceModePointName": "低压侧Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB020",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUa",
    "DeviceModePointName": "低压侧Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB021",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUb",
    "DeviceModePointName": "低压侧Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB021",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUb",
    "DeviceModePointName": "低压侧Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB021",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUb",
    "DeviceModePointName": "低压侧Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB021",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUb",
    "DeviceModePointName": "低压侧Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB022",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUc",
    "DeviceModePointName": "低压侧Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB022",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUc",
    "DeviceModePointName": "低压侧Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB022",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUc",
    "DeviceModePointName": "低压侧Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB022",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPPhVUc",
    "DeviceModePointName": "低压侧Uc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB023",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGri3U0",
    "DeviceModePointName": "低压侧3U0",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB023",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGri3U0",
    "DeviceModePointName": "低压侧3U0",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB023",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGri3U0",
    "DeviceModePointName": "低压侧3U0",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB023",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGri3U0",
    "DeviceModePointName": "低压侧3U0",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB025",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriAIa",
    "DeviceModePointName": "低压侧Ia",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB025",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriAIa",
    "DeviceModePointName": "低压侧Ia",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB025",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriAIa",
    "DeviceModePointName": "低压侧Ia",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB025",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriAIa",
    "DeviceModePointName": "低压侧Ia",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB026",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriAIb",
    "DeviceModePointName": "低压侧Ib",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB026",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriAIb",
    "DeviceModePointName": "低压侧Ib",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB026",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriAIb",
    "DeviceModePointName": "低压侧Ib",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB026",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriAIb",
    "DeviceModePointName": "低压侧Ib",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB027",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriAIc",
    "DeviceModePointName": "低压侧Ic",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB027",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriAIc",
    "DeviceModePointName": "低压侧Ic",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB027",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriAIc",
    "DeviceModePointName": "低压侧Ic",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB027",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriAIc",
    "DeviceModePointName": "低压侧Ic",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB029",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriW",
    "DeviceModePointName": "低压侧P",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB029",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriW",
    "DeviceModePointName": "低压侧P",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB029",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriW",
    "DeviceModePointName": "低压侧P",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB029",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriW",
    "DeviceModePointName": "低压侧P",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB030",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriVar",
    "DeviceModePointName": "低压侧Q",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB030",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriVar",
    "DeviceModePointName": "低压侧Q",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB030",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriVar",
    "DeviceModePointName": "低压侧Q",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB030",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriVar",
    "DeviceModePointName": "低压侧Q",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB031",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPF",
    "DeviceModePointName": "低压侧Cos",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB031",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPF",
    "DeviceModePointName": "低压侧Cos",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB031",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPF",
    "DeviceModePointName": "低压侧Cos",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB031",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriPF",
    "DeviceModePointName": "低压侧Cos",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB032",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriHz",
    "DeviceModePointName": "低压侧Fr",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB032",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriHz",
    "DeviceModePointName": "低压侧Fr",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB032",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriHz",
    "DeviceModePointName": "低压侧Fr",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB032",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "LoGriHz",
    "DeviceModePointName": "低压侧Fr",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB033",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "WinTmp",
    "DeviceModePointName": "主变绕组温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB033",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "WinTmp",
    "DeviceModePointName": "主变绕组温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB033",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "WinTmp",
    "DeviceModePointName": "主变绕组温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB033",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "WinTmp",
    "DeviceModePointName": "主变绕组温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB034",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "OilTmp1",
    "DeviceModePointName": "主变油温1",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB034",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "OilTmp1",
    "DeviceModePointName": "主变油温1",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB034",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "OilTmp1",
    "DeviceModePointName": "主变油温1",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB034",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "OilTmp1",
    "DeviceModePointName": "主变油温1",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB036",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Stl",
    "DeviceModePointName": "档位",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB036",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Stl",
    "DeviceModePointName": "档位",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB036",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Stl",
    "DeviceModePointName": "档位",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB036",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceModePointIECName": "Stl",
    "DeviceModePointName": "档位",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Std",
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
  }
]

allDevice=[
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 1,
    "DeviceFullCode": "56M201M9M1",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M1",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 2,
    "DeviceFullCode": "56M201M9M2",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M1",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 3,
    "DeviceFullCode": "56M201M9M3",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M2",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 4,
    "DeviceFullCode": "56M201M9M4",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M2",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 5,
    "DeviceFullCode": "56M201M9M5",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M3",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 6,
    "DeviceFullCode": "56M201M9M6",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M3",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 7,
    "DeviceFullCode": "56M201M9M7",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M4",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 8,
    "DeviceFullCode": "56M201M9M8",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M4",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 9,
    "DeviceFullCode": "56M201M9M9",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M5",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 10,
    "DeviceFullCode": "56M201M9M10",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M5",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 11,
    "DeviceFullCode": "56M201M9M11",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M6",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 12,
    "DeviceFullCode": "56M201M9M12",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M6",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 13,
    "DeviceFullCode": "56M201M9M13",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M7",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 14,
    "DeviceFullCode": "56M201M9M14",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M7",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 15,
    "DeviceFullCode": "56M201M9M15",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M8",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 16,
    "DeviceFullCode": "56M201M9M16",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M8",
    "Capacity": 583.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 17,
    "DeviceFullCode": "56M201M9M17",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M9",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 18,
    "DeviceFullCode": "56M201M9M18",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M9",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 19,
    "DeviceFullCode": "56M201M9M19",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M10",
    "Capacity": 561.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 20,
    "DeviceFullCode": "56M201M9M20",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M10",
    "Capacity": 561.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 21,
    "DeviceFullCode": "56M201M9M21",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M11",
    "Capacity": 583.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 22,
    "DeviceFullCode": "56M201M9M22",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M11",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 23,
    "DeviceFullCode": "56M201M9M23",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M12",
    "Capacity": 577.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 24,
    "DeviceFullCode": "56M201M9M24",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M12",
    "Capacity": 556.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 25,
    "DeviceFullCode": "56M201M9M25",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M13",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 26,
    "DeviceFullCode": "56M201M9M26",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M13",
    "Capacity": 577.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 27,
    "DeviceFullCode": "56M201M9M27",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M14",
    "Capacity": 583.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 28,
    "DeviceFullCode": "56M201M9M28",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M14",
    "Capacity": 550.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 29,
    "DeviceFullCode": "56M201M9M29",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M15",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 30,
    "DeviceFullCode": "56M201M9M30",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M15",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 31,
    "DeviceFullCode": "56M201M9M31",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M16",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 32,
    "DeviceFullCode": "56M201M9M32",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M16",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 33,
    "DeviceFullCode": "56M201M9M33",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M17",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 34,
    "DeviceFullCode": "56M201M9M34",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M17",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 35,
    "DeviceFullCode": "56M201M9M35",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M18",
    "Capacity": 561.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 36,
    "DeviceFullCode": "56M201M9M36",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M18",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 37,
    "DeviceFullCode": "56M201M9M37",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M19",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 38,
    "DeviceFullCode": "56M201M9M38",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M19",
    "Capacity": 561.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 39,
    "DeviceFullCode": "56M201M9M39",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M20",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 40,
    "DeviceFullCode": "56M201M9M40",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M20",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 41,
    "DeviceFullCode": "56M201M9M41",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M21",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 42,
    "DeviceFullCode": "56M201M9M42",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M21",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 43,
    "DeviceFullCode": "56M201M9M43",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M22",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 44,
    "DeviceFullCode": "56M201M9M44",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M22",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 45,
    "DeviceFullCode": "56M201M9M45",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M23",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 46,
    "DeviceFullCode": "56M201M9M46",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M23",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 47,
    "DeviceFullCode": "56M201M9M47",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M24",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 48,
    "DeviceFullCode": "56M201M9M48",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M24",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 49,
    "DeviceFullCode": "56M201M9M49",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M25",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 50,
    "DeviceFullCode": "56M201M9M50",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M25",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 51,
    "DeviceFullCode": "56M201M9M51",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M26",
    "Capacity": 577.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 52,
    "DeviceFullCode": "56M201M9M52",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M26",
    "Capacity": 577.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 53,
    "DeviceFullCode": "56M201M9M53",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M27",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 54,
    "DeviceFullCode": "56M201M9M54",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M27",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 55,
    "DeviceFullCode": "56M201M9M55",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M28",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 56,
    "DeviceFullCode": "56M201M9M56",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M28",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 57,
    "DeviceFullCode": "56M201M9M57",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M29",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 58,
    "DeviceFullCode": "56M201M9M58",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M29",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 59,
    "DeviceFullCode": "56M201M9M59",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M30",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 60,
    "DeviceFullCode": "56M201M9M60",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M30",
    "Capacity": 577.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 61,
    "DeviceFullCode": "56M201M9M61",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M31",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 62,
    "DeviceFullCode": "56M201M9M62",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M31",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 63,
    "DeviceFullCode": "56M201M9M63",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M32",
    "Capacity": 588.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 64,
    "DeviceFullCode": "56M201M9M64",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M32",
    "Capacity": 588.6000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 65,
    "DeviceFullCode": "56M201M9M65",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M33",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 66,
    "DeviceFullCode": "56M201M9M66",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M33",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 67,
    "DeviceFullCode": "56M201M9M67",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M34",
    "Capacity": 577.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 68,
    "DeviceFullCode": "56M201M9M68",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M34",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 69,
    "DeviceFullCode": "56M201M9M69",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M35",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 70,
    "DeviceFullCode": "56M201M9M70",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M35",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 71,
    "DeviceFullCode": "56M201M9M71",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M36",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 72,
    "DeviceFullCode": "56M201M9M72",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M36",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 73,
    "DeviceFullCode": "56M201M9M73",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M37",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 74,
    "DeviceFullCode": "56M201M9M74",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M37",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 75,
    "DeviceFullCode": "56M201M9M75",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M38",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 76,
    "DeviceFullCode": "56M201M9M76",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M38",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 77,
    "DeviceFullCode": "56M201M9M77",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M39",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 78,
    "DeviceFullCode": "56M201M9M78",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M39",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 79,
    "DeviceFullCode": "56M201M9M79",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M40",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 80,
    "DeviceFullCode": "56M201M9M80",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M40",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 81,
    "DeviceFullCode": "56M201M9M81",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M41",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 82,
    "DeviceFullCode": "56M201M9M82",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M41",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 83,
    "DeviceFullCode": "56M201M9M83",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M42",
    "Capacity": 567.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 84,
    "DeviceFullCode": "56M201M9M84",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M42",
    "Capacity": 572.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 85,
    "DeviceFullCode": "56M201M9M85",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M43",
    "Capacity": 529.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 86,
    "DeviceFullCode": "56M201M9M86",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M43",
    "Capacity": 529.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 87,
    "DeviceFullCode": "56M201M9M87",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M44",
    "Capacity": 529.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 88,
    "DeviceFullCode": "56M201M9M88",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M44",
    "Capacity": 529.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 89,
    "DeviceFullCode": "56M201M9M89",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M45",
    "Capacity": 529.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 9,
    "DeviceCode": 90,
    "DeviceFullCode": "56M201M9M90",
    "DeviceModeFullCode": "56M201M9",
    "PDeviceFullCode": "56M204M2M45",
    "Capacity": 529.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 1,
    "DeviceFullCode": "56M202M11M1",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M1",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 2,
    "DeviceFullCode": "56M202M11M2",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M1",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 3,
    "DeviceFullCode": "56M202M11M3",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M1",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 4,
    "DeviceFullCode": "56M202M11M4",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M1",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 5,
    "DeviceFullCode": "56M202M11M5",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M2",
    "Capacity": 32.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 6,
    "DeviceFullCode": "56M202M11M6",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M1",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 7,
    "DeviceFullCode": "56M202M11M7",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M1",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 8,
    "DeviceFullCode": "56M202M11M8",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M2",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 9,
    "DeviceFullCode": "56M202M11M9",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M2",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 10,
    "DeviceFullCode": "56M202M11M10",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M1",
    "Capacity": 81.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 11,
    "DeviceFullCode": "56M202M11M11",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M2",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 12,
    "DeviceFullCode": "56M202M11M12",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M2",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 13,
    "DeviceFullCode": "56M202M11M13",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M2",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 14,
    "DeviceFullCode": "56M202M11M14",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M2",
    "Capacity": 81.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 15,
    "DeviceFullCode": "56M202M11M15",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M3",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 16,
    "DeviceFullCode": "56M202M11M16",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M3",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 17,
    "DeviceFullCode": "56M202M11M17",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M3",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 18,
    "DeviceFullCode": "56M202M11M18",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M3",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 19,
    "DeviceFullCode": "56M202M11M19",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M3",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 20,
    "DeviceFullCode": "56M202M11M20",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M3",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 21,
    "DeviceFullCode": "56M202M11M21",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M4",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 22,
    "DeviceFullCode": "56M202M11M22",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M3",
    "Capacity": 81.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 23,
    "DeviceFullCode": "56M202M11M23",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M4",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 24,
    "DeviceFullCode": "56M202M11M24",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M4",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 25,
    "DeviceFullCode": "56M202M11M25",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M4",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 26,
    "DeviceFullCode": "56M202M11M26",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M4",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 27,
    "DeviceFullCode": "56M202M11M27",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M4",
    "Capacity": 86.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 28,
    "DeviceFullCode": "56M202M11M28",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M4",
    "Capacity": 81.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 29,
    "DeviceFullCode": "56M202M11M29",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M5",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 30,
    "DeviceFullCode": "56M202M11M30",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M5",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 31,
    "DeviceFullCode": "56M202M11M31",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M5",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 32,
    "DeviceFullCode": "56M202M11M32",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M5",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 33,
    "DeviceFullCode": "56M202M11M33",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M5",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 34,
    "DeviceFullCode": "56M202M11M34",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M5",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 35,
    "DeviceFullCode": "56M202M11M35",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M5",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 36,
    "DeviceFullCode": "56M202M11M36",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M5",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 37,
    "DeviceFullCode": "56M202M11M37",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M5",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 38,
    "DeviceFullCode": "56M202M11M38",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M6",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 39,
    "DeviceFullCode": "56M202M11M39",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M6",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 40,
    "DeviceFullCode": "56M202M11M40",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M6",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 41,
    "DeviceFullCode": "56M202M11M41",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M6",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 42,
    "DeviceFullCode": "56M202M11M42",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M6",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 43,
    "DeviceFullCode": "56M202M11M43",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M6",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 44,
    "DeviceFullCode": "56M202M11M44",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M6",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 45,
    "DeviceFullCode": "56M202M11M45",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M6",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 46,
    "DeviceFullCode": "56M202M11M46",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M6",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 47,
    "DeviceFullCode": "56M202M11M47",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M7",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 48,
    "DeviceFullCode": "56M202M11M48",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M7",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 49,
    "DeviceFullCode": "56M202M11M49",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M7",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 50,
    "DeviceFullCode": "56M202M11M50",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M7",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 51,
    "DeviceFullCode": "56M202M11M51",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M7",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 52,
    "DeviceFullCode": "56M202M11M52",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M7",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 53,
    "DeviceFullCode": "56M202M11M53",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M7",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 54,
    "DeviceFullCode": "56M202M11M54",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M7",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 55,
    "DeviceFullCode": "56M202M11M55",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M8",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 56,
    "DeviceFullCode": "56M202M11M56",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M8",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 57,
    "DeviceFullCode": "56M202M11M57",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M8",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 58,
    "DeviceFullCode": "56M202M11M58",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M8",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 59,
    "DeviceFullCode": "56M202M11M59",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M8",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 60,
    "DeviceFullCode": "56M202M11M60",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M8",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 61,
    "DeviceFullCode": "56M202M11M61",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M8",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 62,
    "DeviceFullCode": "56M202M11M62",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M8",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 63,
    "DeviceFullCode": "56M202M11M63",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M7",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 64,
    "DeviceFullCode": "56M202M11M64",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M8",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 65,
    "DeviceFullCode": "56M202M11M65",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M9",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 66,
    "DeviceFullCode": "56M202M11M66",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M9",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 67,
    "DeviceFullCode": "56M202M11M67",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M10",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 68,
    "DeviceFullCode": "56M202M11M68",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M9",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 69,
    "DeviceFullCode": "56M202M11M69",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M9",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 70,
    "DeviceFullCode": "56M202M11M70",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M9",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 71,
    "DeviceFullCode": "56M202M11M71",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M9",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 72,
    "DeviceFullCode": "56M202M11M72",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M9",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 73,
    "DeviceFullCode": "56M202M11M73",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M9",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 74,
    "DeviceFullCode": "56M202M11M74",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M9",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 75,
    "DeviceFullCode": "56M202M11M75",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M10",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 76,
    "DeviceFullCode": "56M202M11M76",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M10",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 77,
    "DeviceFullCode": "56M202M11M77",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M10",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 78,
    "DeviceFullCode": "56M202M11M78",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M10",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 79,
    "DeviceFullCode": "56M202M11M79",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M10",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 80,
    "DeviceFullCode": "56M202M11M80",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M10",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 81,
    "DeviceFullCode": "56M202M11M81",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M10",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 82,
    "DeviceFullCode": "56M202M11M82",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M10",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 83,
    "DeviceFullCode": "56M202M11M83",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M11",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 84,
    "DeviceFullCode": "56M202M11M84",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M11",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 85,
    "DeviceFullCode": "56M202M11M85",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M11",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 86,
    "DeviceFullCode": "56M202M11M86",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M11",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 87,
    "DeviceFullCode": "56M202M11M87",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M11",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 88,
    "DeviceFullCode": "56M202M11M88",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M11",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 89,
    "DeviceFullCode": "56M202M11M89",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M11",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 90,
    "DeviceFullCode": "56M202M11M90",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M11",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 91,
    "DeviceFullCode": "56M202M11M91",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M11",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 92,
    "DeviceFullCode": "56M202M11M92",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M12",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 93,
    "DeviceFullCode": "56M202M11M93",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M12",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 94,
    "DeviceFullCode": "56M202M11M94",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M12",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 95,
    "DeviceFullCode": "56M202M11M95",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M12",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 96,
    "DeviceFullCode": "56M202M11M96",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M12",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 97,
    "DeviceFullCode": "56M202M11M97",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M12",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 98,
    "DeviceFullCode": "56M202M11M98",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M12",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 99,
    "DeviceFullCode": "56M202M11M99",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M12",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 100,
    "DeviceFullCode": "56M202M11M100",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M12",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 101,
    "DeviceFullCode": "56M202M11M101",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M13",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 102,
    "DeviceFullCode": "56M202M11M102",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M13",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 103,
    "DeviceFullCode": "56M202M11M103",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M13",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 104,
    "DeviceFullCode": "56M202M11M104",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M13",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 105,
    "DeviceFullCode": "56M202M11M105",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M13",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 106,
    "DeviceFullCode": "56M202M11M106",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M13",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 107,
    "DeviceFullCode": "56M202M11M107",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M13",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 108,
    "DeviceFullCode": "56M202M11M108",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M13",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 109,
    "DeviceFullCode": "56M202M11M109",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M13",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 110,
    "DeviceFullCode": "56M202M11M110",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M14",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 111,
    "DeviceFullCode": "56M202M11M111",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M14",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 112,
    "DeviceFullCode": "56M202M11M112",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M14",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 113,
    "DeviceFullCode": "56M202M11M113",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M14",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 114,
    "DeviceFullCode": "56M202M11M114",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M14",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 115,
    "DeviceFullCode": "56M202M11M115",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M14",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 116,
    "DeviceFullCode": "56M202M11M116",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M14",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 117,
    "DeviceFullCode": "56M202M11M117",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M14",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 118,
    "DeviceFullCode": "56M202M11M118",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M14",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 119,
    "DeviceFullCode": "56M202M11M119",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M15",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 120,
    "DeviceFullCode": "56M202M11M120",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M15",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 121,
    "DeviceFullCode": "56M202M11M121",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M15",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 122,
    "DeviceFullCode": "56M202M11M122",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M15",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 123,
    "DeviceFullCode": "56M202M11M123",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M15",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 124,
    "DeviceFullCode": "56M202M11M124",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M15",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 125,
    "DeviceFullCode": "56M202M11M125",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M15",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 126,
    "DeviceFullCode": "56M202M11M126",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M15",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 127,
    "DeviceFullCode": "56M202M11M127",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M15",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 128,
    "DeviceFullCode": "56M202M11M128",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M16",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 129,
    "DeviceFullCode": "56M202M11M129",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M16",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 130,
    "DeviceFullCode": "56M202M11M130",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M16",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 131,
    "DeviceFullCode": "56M202M11M131",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M16",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 132,
    "DeviceFullCode": "56M202M11M132",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M16",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 133,
    "DeviceFullCode": "56M202M11M133",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M16",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 134,
    "DeviceFullCode": "56M202M11M134",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M16",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 135,
    "DeviceFullCode": "56M202M11M135",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M16",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 136,
    "DeviceFullCode": "56M202M11M136",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M16",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 137,
    "DeviceFullCode": "56M202M11M137",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M17",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 138,
    "DeviceFullCode": "56M202M11M138",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M17",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 139,
    "DeviceFullCode": "56M202M11M139",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M17",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 140,
    "DeviceFullCode": "56M202M11M140",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M17",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 141,
    "DeviceFullCode": "56M202M11M141",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M17",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 142,
    "DeviceFullCode": "56M202M11M142",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M17",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 143,
    "DeviceFullCode": "56M202M11M143",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M17",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 144,
    "DeviceFullCode": "56M202M11M144",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M17",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 145,
    "DeviceFullCode": "56M202M11M145",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M17",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 146,
    "DeviceFullCode": "56M202M11M146",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M18",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 147,
    "DeviceFullCode": "56M202M11M147",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M18",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 148,
    "DeviceFullCode": "56M202M11M148",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M18",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 149,
    "DeviceFullCode": "56M202M11M149",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M18",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 150,
    "DeviceFullCode": "56M202M11M150",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M18",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 151,
    "DeviceFullCode": "56M202M11M151",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M18",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 152,
    "DeviceFullCode": "56M202M11M152",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M18",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 153,
    "DeviceFullCode": "56M202M11M153",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M18",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 154,
    "DeviceFullCode": "56M202M11M154",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M18",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 155,
    "DeviceFullCode": "56M202M11M155",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M19",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 156,
    "DeviceFullCode": "56M202M11M156",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M19",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 157,
    "DeviceFullCode": "56M202M11M157",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M19",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 158,
    "DeviceFullCode": "56M202M11M158",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M19",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 159,
    "DeviceFullCode": "56M202M11M159",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M19",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 160,
    "DeviceFullCode": "56M202M11M160",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M19",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 161,
    "DeviceFullCode": "56M202M11M161",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M20",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 162,
    "DeviceFullCode": "56M202M11M162",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M20",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 163,
    "DeviceFullCode": "56M202M11M163",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M19",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 164,
    "DeviceFullCode": "56M202M11M164",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M19",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 165,
    "DeviceFullCode": "56M202M11M165",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M19",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 166,
    "DeviceFullCode": "56M202M11M166",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M20",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 167,
    "DeviceFullCode": "56M202M11M167",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M20",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 168,
    "DeviceFullCode": "56M202M11M168",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M20",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 169,
    "DeviceFullCode": "56M202M11M169",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M20",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 170,
    "DeviceFullCode": "56M202M11M170",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M20",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 171,
    "DeviceFullCode": "56M202M11M171",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M20",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 172,
    "DeviceFullCode": "56M202M11M172",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M20",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 173,
    "DeviceFullCode": "56M202M11M173",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M21",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 174,
    "DeviceFullCode": "56M202M11M174",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M21",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 175,
    "DeviceFullCode": "56M202M11M175",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M21",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 176,
    "DeviceFullCode": "56M202M11M176",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M21",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 177,
    "DeviceFullCode": "56M202M11M177",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M21",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 178,
    "DeviceFullCode": "56M202M11M178",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M21",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 179,
    "DeviceFullCode": "56M202M11M179",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M21",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 180,
    "DeviceFullCode": "56M202M11M180",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M21",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 181,
    "DeviceFullCode": "56M202M11M181",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M22",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 182,
    "DeviceFullCode": "56M202M11M182",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M22",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 183,
    "DeviceFullCode": "56M202M11M183",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M22",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 184,
    "DeviceFullCode": "56M202M11M184",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M22",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 185,
    "DeviceFullCode": "56M202M11M185",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M22",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 186,
    "DeviceFullCode": "56M202M11M186",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M22",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 187,
    "DeviceFullCode": "56M202M11M187",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M21",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 188,
    "DeviceFullCode": "56M202M11M188",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M22",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 189,
    "DeviceFullCode": "56M202M11M189",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M22",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 190,
    "DeviceFullCode": "56M202M11M190",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M22",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 191,
    "DeviceFullCode": "56M202M11M191",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M23",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 192,
    "DeviceFullCode": "56M202M11M192",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M23",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 193,
    "DeviceFullCode": "56M202M11M193",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M23",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 194,
    "DeviceFullCode": "56M202M11M194",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M23",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 195,
    "DeviceFullCode": "56M202M11M195",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M23",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 196,
    "DeviceFullCode": "56M202M11M196",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M23",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 197,
    "DeviceFullCode": "56M202M11M197",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M23",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 198,
    "DeviceFullCode": "56M202M11M198",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M23",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 199,
    "DeviceFullCode": "56M202M11M199",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M23",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 200,
    "DeviceFullCode": "56M202M11M200",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M24",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 201,
    "DeviceFullCode": "56M202M11M201",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M24",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 202,
    "DeviceFullCode": "56M202M11M202",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M24",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 203,
    "DeviceFullCode": "56M202M11M203",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M24",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 204,
    "DeviceFullCode": "56M202M11M204",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M24",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 205,
    "DeviceFullCode": "56M202M11M205",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M24",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 206,
    "DeviceFullCode": "56M202M11M206",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M24",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 207,
    "DeviceFullCode": "56M202M11M207",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M24",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 208,
    "DeviceFullCode": "56M202M11M208",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M24",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 209,
    "DeviceFullCode": "56M202M11M209",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M25",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 210,
    "DeviceFullCode": "56M202M11M210",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M25",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 211,
    "DeviceFullCode": "56M202M11M211",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M25",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 212,
    "DeviceFullCode": "56M202M11M212",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M25",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 213,
    "DeviceFullCode": "56M202M11M213",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M25",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 214,
    "DeviceFullCode": "56M202M11M214",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M25",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 215,
    "DeviceFullCode": "56M202M11M215",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M25",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 216,
    "DeviceFullCode": "56M202M11M216",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M25",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 217,
    "DeviceFullCode": "56M202M11M217",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M25",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 218,
    "DeviceFullCode": "56M202M11M218",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M26",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 219,
    "DeviceFullCode": "56M202M11M219",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M26",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 220,
    "DeviceFullCode": "56M202M11M220",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M26",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 221,
    "DeviceFullCode": "56M202M11M221",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M26",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 222,
    "DeviceFullCode": "56M202M11M222",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M26",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 223,
    "DeviceFullCode": "56M202M11M223",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M26",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 224,
    "DeviceFullCode": "56M202M11M224",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M26",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 225,
    "DeviceFullCode": "56M202M11M225",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M26",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 226,
    "DeviceFullCode": "56M202M11M226",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M26",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 227,
    "DeviceFullCode": "56M202M11M227",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M27",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 228,
    "DeviceFullCode": "56M202M11M228",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M27",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 229,
    "DeviceFullCode": "56M202M11M229",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M27",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 230,
    "DeviceFullCode": "56M202M11M230",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M27",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 231,
    "DeviceFullCode": "56M202M11M231",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M27",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 232,
    "DeviceFullCode": "56M202M11M232",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M27",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 233,
    "DeviceFullCode": "56M202M11M233",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M27",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 234,
    "DeviceFullCode": "56M202M11M234",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M27",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 235,
    "DeviceFullCode": "56M202M11M235",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M28",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 236,
    "DeviceFullCode": "56M202M11M236",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M28",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 237,
    "DeviceFullCode": "56M202M11M237",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M28",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 238,
    "DeviceFullCode": "56M202M11M238",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M28",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 239,
    "DeviceFullCode": "56M202M11M239",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M28",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 240,
    "DeviceFullCode": "56M202M11M240",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M27",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 241,
    "DeviceFullCode": "56M202M11M241",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M28",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 242,
    "DeviceFullCode": "56M202M11M242",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M28",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 243,
    "DeviceFullCode": "56M202M11M243",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M28",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 244,
    "DeviceFullCode": "56M202M11M244",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M28",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 245,
    "DeviceFullCode": "56M202M11M245",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M29",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 246,
    "DeviceFullCode": "56M202M11M246",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M29",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 247,
    "DeviceFullCode": "56M202M11M247",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M29",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 248,
    "DeviceFullCode": "56M202M11M248",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M29",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 249,
    "DeviceFullCode": "56M202M11M249",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M29",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 250,
    "DeviceFullCode": "56M202M11M250",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M29",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 251,
    "DeviceFullCode": "56M202M11M251",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M29",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 252,
    "DeviceFullCode": "56M202M11M252",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M29",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 253,
    "DeviceFullCode": "56M202M11M253",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M30",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 254,
    "DeviceFullCode": "56M202M11M254",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M30",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 255,
    "DeviceFullCode": "56M202M11M255",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M30",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 256,
    "DeviceFullCode": "56M202M11M256",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M30",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 257,
    "DeviceFullCode": "56M202M11M257",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M30",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 258,
    "DeviceFullCode": "56M202M11M258",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M29",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 259,
    "DeviceFullCode": "56M202M11M259",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M30",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 260,
    "DeviceFullCode": "56M202M11M260",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M30",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 261,
    "DeviceFullCode": "56M202M11M261",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M30",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 262,
    "DeviceFullCode": "56M202M11M262",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M30",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 263,
    "DeviceFullCode": "56M202M11M263",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M31",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 264,
    "DeviceFullCode": "56M202M11M264",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M31",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 265,
    "DeviceFullCode": "56M202M11M265",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M31",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 266,
    "DeviceFullCode": "56M202M11M266",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M31",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 267,
    "DeviceFullCode": "56M202M11M267",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M31",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 268,
    "DeviceFullCode": "56M202M11M268",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M31",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 269,
    "DeviceFullCode": "56M202M11M269",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M31",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 270,
    "DeviceFullCode": "56M202M11M270",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M32",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 271,
    "DeviceFullCode": "56M202M11M271",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M32",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 272,
    "DeviceFullCode": "56M202M11M272",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M32",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 273,
    "DeviceFullCode": "56M202M11M273",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M32",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 274,
    "DeviceFullCode": "56M202M11M274",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M32",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 275,
    "DeviceFullCode": "56M202M11M275",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M32",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 276,
    "DeviceFullCode": "56M202M11M276",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M32",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 277,
    "DeviceFullCode": "56M202M11M277",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M32",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 278,
    "DeviceFullCode": "56M202M11M278",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M31",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 279,
    "DeviceFullCode": "56M202M11M279",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M31",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 280,
    "DeviceFullCode": "56M202M11M280",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M32",
    "Capacity": 43.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 281,
    "DeviceFullCode": "56M202M11M281",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M33",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 282,
    "DeviceFullCode": "56M202M11M282",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M33",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 283,
    "DeviceFullCode": "56M202M11M283",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M33",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 284,
    "DeviceFullCode": "56M202M11M284",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M33",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 285,
    "DeviceFullCode": "56M202M11M285",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M33",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 286,
    "DeviceFullCode": "56M202M11M286",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M34",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 287,
    "DeviceFullCode": "56M202M11M287",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M34",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 288,
    "DeviceFullCode": "56M202M11M288",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M33",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 289,
    "DeviceFullCode": "56M202M11M289",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M33",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 290,
    "DeviceFullCode": "56M202M11M290",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M33",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 291,
    "DeviceFullCode": "56M202M11M291",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M33",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 292,
    "DeviceFullCode": "56M202M11M292",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M34",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 293,
    "DeviceFullCode": "56M202M11M293",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M34",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 294,
    "DeviceFullCode": "56M202M11M294",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M34",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 295,
    "DeviceFullCode": "56M202M11M295",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M34",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 296,
    "DeviceFullCode": "56M202M11M296",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M34",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 297,
    "DeviceFullCode": "56M202M11M297",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M34",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 298,
    "DeviceFullCode": "56M202M11M298",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M34",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 299,
    "DeviceFullCode": "56M202M11M299",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M35",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 300,
    "DeviceFullCode": "56M202M11M300",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M36",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 301,
    "DeviceFullCode": "56M202M11M301",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M35",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 302,
    "DeviceFullCode": "56M202M11M302",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M35",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 303,
    "DeviceFullCode": "56M202M11M303",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M35",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 304,
    "DeviceFullCode": "56M202M11M304",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M35",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 305,
    "DeviceFullCode": "56M202M11M305",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M35",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 306,
    "DeviceFullCode": "56M202M11M306",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M35",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 307,
    "DeviceFullCode": "56M202M11M307",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M35",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 308,
    "DeviceFullCode": "56M202M11M308",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M35",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 309,
    "DeviceFullCode": "56M202M11M309",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M36",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 310,
    "DeviceFullCode": "56M202M11M310",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M36",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 311,
    "DeviceFullCode": "56M202M11M311",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M36",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 312,
    "DeviceFullCode": "56M202M11M312",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M36",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 313,
    "DeviceFullCode": "56M202M11M313",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M36",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 314,
    "DeviceFullCode": "56M202M11M314",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M36",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 315,
    "DeviceFullCode": "56M202M11M315",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M36",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 316,
    "DeviceFullCode": "56M202M11M316",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M36",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 317,
    "DeviceFullCode": "56M202M11M317",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M37",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 318,
    "DeviceFullCode": "56M202M11M318",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M37",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 319,
    "DeviceFullCode": "56M202M11M319",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M37",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 320,
    "DeviceFullCode": "56M202M11M320",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M37",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 321,
    "DeviceFullCode": "56M202M11M321",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M37",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 322,
    "DeviceFullCode": "56M202M11M322",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M38",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 323,
    "DeviceFullCode": "56M202M11M323",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M37",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 324,
    "DeviceFullCode": "56M202M11M324",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M37",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 325,
    "DeviceFullCode": "56M202M11M325",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M38",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 326,
    "DeviceFullCode": "56M202M11M326",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M38",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 327,
    "DeviceFullCode": "56M202M11M327",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M38",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 328,
    "DeviceFullCode": "56M202M11M328",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M38",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 329,
    "DeviceFullCode": "56M202M11M329",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M38",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 330,
    "DeviceFullCode": "56M202M11M330",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M37",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 331,
    "DeviceFullCode": "56M202M11M331",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M38",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 332,
    "DeviceFullCode": "56M202M11M332",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M38",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 333,
    "DeviceFullCode": "56M202M11M333",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M37",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 334,
    "DeviceFullCode": "56M202M11M334",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M38",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 335,
    "DeviceFullCode": "56M202M11M335",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M39",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 336,
    "DeviceFullCode": "56M202M11M336",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M39",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 337,
    "DeviceFullCode": "56M202M11M337",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M39",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 338,
    "DeviceFullCode": "56M202M11M338",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M39",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 339,
    "DeviceFullCode": "56M202M11M339",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M39",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 340,
    "DeviceFullCode": "56M202M11M340",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M39",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 341,
    "DeviceFullCode": "56M202M11M341",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M39",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 342,
    "DeviceFullCode": "56M202M11M342",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M39",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 343,
    "DeviceFullCode": "56M202M11M343",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M40",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 344,
    "DeviceFullCode": "56M202M11M344",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M40",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 345,
    "DeviceFullCode": "56M202M11M345",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M40",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 346,
    "DeviceFullCode": "56M202M11M346",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M40",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 347,
    "DeviceFullCode": "56M202M11M347",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M40",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 348,
    "DeviceFullCode": "56M202M11M348",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M39",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 349,
    "DeviceFullCode": "56M202M11M349",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M40",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 350,
    "DeviceFullCode": "56M202M11M350",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M40",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 351,
    "DeviceFullCode": "56M202M11M351",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M40",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 352,
    "DeviceFullCode": "56M202M11M352",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M40",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 353,
    "DeviceFullCode": "56M202M11M353",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M41",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 354,
    "DeviceFullCode": "56M202M11M354",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M41",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 355,
    "DeviceFullCode": "56M202M11M355",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M41",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 356,
    "DeviceFullCode": "56M202M11M356",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M41",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 357,
    "DeviceFullCode": "56M202M11M357",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M41",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 358,
    "DeviceFullCode": "56M202M11M358",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M41",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 359,
    "DeviceFullCode": "56M202M11M359",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M41",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 360,
    "DeviceFullCode": "56M202M11M360",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M41",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 361,
    "DeviceFullCode": "56M202M11M361",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M42",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 362,
    "DeviceFullCode": "56M202M11M362",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M41",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 363,
    "DeviceFullCode": "56M202M11M363",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M42",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 364,
    "DeviceFullCode": "56M202M11M364",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M42",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 365,
    "DeviceFullCode": "56M202M11M365",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M42",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 366,
    "DeviceFullCode": "56M202M11M366",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M42",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 367,
    "DeviceFullCode": "56M202M11M367",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M42",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 368,
    "DeviceFullCode": "56M202M11M368",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M42",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 369,
    "DeviceFullCode": "56M202M11M369",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M42",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 370,
    "DeviceFullCode": "56M202M11M370",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M42",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 371,
    "DeviceFullCode": "56M202M11M371",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M43",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 372,
    "DeviceFullCode": "56M202M11M372",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M43",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 373,
    "DeviceFullCode": "56M202M11M373",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M43",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 374,
    "DeviceFullCode": "56M202M11M374",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M43",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 375,
    "DeviceFullCode": "56M202M11M375",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M43",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 376,
    "DeviceFullCode": "56M202M11M376",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M43",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 377,
    "DeviceFullCode": "56M202M11M377",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M43",
    "Capacity": 43.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 378,
    "DeviceFullCode": "56M202M11M378",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M44",
    "Capacity": 43.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 379,
    "DeviceFullCode": "56M202M11M379",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M43",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 380,
    "DeviceFullCode": "56M202M11M380",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M44",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 381,
    "DeviceFullCode": "56M202M11M381",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M43",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 382,
    "DeviceFullCode": "56M202M11M382",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M44",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 383,
    "DeviceFullCode": "56M202M11M383",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M44",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 384,
    "DeviceFullCode": "56M202M11M384",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M44",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 385,
    "DeviceFullCode": "56M202M11M385",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M44",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 386,
    "DeviceFullCode": "56M202M11M386",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M44",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 387,
    "DeviceFullCode": "56M202M11M387",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M44",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 388,
    "DeviceFullCode": "56M202M11M388",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M44",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 389,
    "DeviceFullCode": "56M202M11M389",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M45",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 390,
    "DeviceFullCode": "56M202M11M390",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M45",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 391,
    "DeviceFullCode": "56M202M11M391",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M45",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 392,
    "DeviceFullCode": "56M202M11M392",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M45",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 393,
    "DeviceFullCode": "56M202M11M393",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M45",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 394,
    "DeviceFullCode": "56M202M11M394",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M45",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 395,
    "DeviceFullCode": "56M202M11M395",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M45",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 396,
    "DeviceFullCode": "56M202M11M396",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M46",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 397,
    "DeviceFullCode": "56M202M11M397",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M45",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 398,
    "DeviceFullCode": "56M202M11M398",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M46",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 399,
    "DeviceFullCode": "56M202M11M399",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M46",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 400,
    "DeviceFullCode": "56M202M11M400",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M46",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 401,
    "DeviceFullCode": "56M202M11M401",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M46",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 402,
    "DeviceFullCode": "56M202M11M402",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M45",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 403,
    "DeviceFullCode": "56M202M11M403",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M46",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 404,
    "DeviceFullCode": "56M202M11M404",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M46",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 405,
    "DeviceFullCode": "56M202M11M405",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M46",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 406,
    "DeviceFullCode": "56M202M11M406",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M46",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 407,
    "DeviceFullCode": "56M202M11M407",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M47",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 408,
    "DeviceFullCode": "56M202M11M408",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M47",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 409,
    "DeviceFullCode": "56M202M11M409",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M47",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 410,
    "DeviceFullCode": "56M202M11M410",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M48",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 411,
    "DeviceFullCode": "56M202M11M411",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M47",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 412,
    "DeviceFullCode": "56M202M11M412",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M47",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 413,
    "DeviceFullCode": "56M202M11M413",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M47",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 414,
    "DeviceFullCode": "56M202M11M414",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M47",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 415,
    "DeviceFullCode": "56M202M11M415",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M48",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 416,
    "DeviceFullCode": "56M202M11M416",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M47",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 417,
    "DeviceFullCode": "56M202M11M417",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M47",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 418,
    "DeviceFullCode": "56M202M11M418",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M48",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 419,
    "DeviceFullCode": "56M202M11M419",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M48",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 420,
    "DeviceFullCode": "56M202M11M420",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M48",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 421,
    "DeviceFullCode": "56M202M11M421",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M48",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 422,
    "DeviceFullCode": "56M202M11M422",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M48",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 423,
    "DeviceFullCode": "56M202M11M423",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M48",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 424,
    "DeviceFullCode": "56M202M11M424",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M48",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 425,
    "DeviceFullCode": "56M202M11M425",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M49",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 426,
    "DeviceFullCode": "56M202M11M426",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M49",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 427,
    "DeviceFullCode": "56M202M11M427",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M50",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 428,
    "DeviceFullCode": "56M202M11M428",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M49",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 429,
    "DeviceFullCode": "56M202M11M429",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M49",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 430,
    "DeviceFullCode": "56M202M11M430",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M49",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 431,
    "DeviceFullCode": "56M202M11M431",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M49",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 432,
    "DeviceFullCode": "56M202M11M432",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M49",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 433,
    "DeviceFullCode": "56M202M11M433",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M49",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 434,
    "DeviceFullCode": "56M202M11M434",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M49",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 435,
    "DeviceFullCode": "56M202M11M435",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M50",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 436,
    "DeviceFullCode": "56M202M11M436",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M50",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 437,
    "DeviceFullCode": "56M202M11M437",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M50",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 438,
    "DeviceFullCode": "56M202M11M438",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M50",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 439,
    "DeviceFullCode": "56M202M11M439",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M50",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 440,
    "DeviceFullCode": "56M202M11M440",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M50",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 441,
    "DeviceFullCode": "56M202M11M441",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M50",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 442,
    "DeviceFullCode": "56M202M11M442",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M50",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 443,
    "DeviceFullCode": "56M202M11M443",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M51",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 444,
    "DeviceFullCode": "56M202M11M444",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M51",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 445,
    "DeviceFullCode": "56M202M11M445",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M51",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 446,
    "DeviceFullCode": "56M202M11M446",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M51",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 447,
    "DeviceFullCode": "56M202M11M447",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M51",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 448,
    "DeviceFullCode": "56M202M11M448",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M51",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 449,
    "DeviceFullCode": "56M202M11M449",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M52",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 450,
    "DeviceFullCode": "56M202M11M450",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M51",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 451,
    "DeviceFullCode": "56M202M11M451",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M51",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 452,
    "DeviceFullCode": "56M202M11M452",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M52",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 453,
    "DeviceFullCode": "56M202M11M453",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M52",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 454,
    "DeviceFullCode": "56M202M11M454",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M51",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 455,
    "DeviceFullCode": "56M202M11M455",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M52",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 456,
    "DeviceFullCode": "56M202M11M456",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M52",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 457,
    "DeviceFullCode": "56M202M11M457",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M52",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 458,
    "DeviceFullCode": "56M202M11M458",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M52",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 459,
    "DeviceFullCode": "56M202M11M459",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M52",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 460,
    "DeviceFullCode": "56M202M11M460",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M52",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 461,
    "DeviceFullCode": "56M202M11M461",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M53",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 462,
    "DeviceFullCode": "56M202M11M462",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M53",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 463,
    "DeviceFullCode": "56M202M11M463",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M53",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 464,
    "DeviceFullCode": "56M202M11M464",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M53",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 465,
    "DeviceFullCode": "56M202M11M465",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M53",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 466,
    "DeviceFullCode": "56M202M11M466",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M53",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 467,
    "DeviceFullCode": "56M202M11M467",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M53",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 468,
    "DeviceFullCode": "56M202M11M468",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M53",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 469,
    "DeviceFullCode": "56M202M11M469",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M54",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 470,
    "DeviceFullCode": "56M202M11M470",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M54",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 471,
    "DeviceFullCode": "56M202M11M471",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M53",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 472,
    "DeviceFullCode": "56M202M11M472",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M54",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 473,
    "DeviceFullCode": "56M202M11M473",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M54",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 474,
    "DeviceFullCode": "56M202M11M474",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M54",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 475,
    "DeviceFullCode": "56M202M11M475",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M54",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 476,
    "DeviceFullCode": "56M202M11M476",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M54",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 477,
    "DeviceFullCode": "56M202M11M477",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M54",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 478,
    "DeviceFullCode": "56M202M11M478",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M54",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 479,
    "DeviceFullCode": "56M202M11M479",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M55",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 480,
    "DeviceFullCode": "56M202M11M480",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M55",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 481,
    "DeviceFullCode": "56M202M11M481",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M55",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 482,
    "DeviceFullCode": "56M202M11M482",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M55",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 483,
    "DeviceFullCode": "56M202M11M483",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M56",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 484,
    "DeviceFullCode": "56M202M11M484",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M55",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 485,
    "DeviceFullCode": "56M202M11M485",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M55",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 486,
    "DeviceFullCode": "56M202M11M486",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M55",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 487,
    "DeviceFullCode": "56M202M11M487",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M55",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 488,
    "DeviceFullCode": "56M202M11M488",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M55",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 489,
    "DeviceFullCode": "56M202M11M489",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M56",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 490,
    "DeviceFullCode": "56M202M11M490",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M56",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 491,
    "DeviceFullCode": "56M202M11M491",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M56",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 492,
    "DeviceFullCode": "56M202M11M492",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M56",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 493,
    "DeviceFullCode": "56M202M11M493",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M56",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 494,
    "DeviceFullCode": "56M202M11M494",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M56",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 495,
    "DeviceFullCode": "56M202M11M495",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M56",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 496,
    "DeviceFullCode": "56M202M11M496",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M56",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 497,
    "DeviceFullCode": "56M202M11M497",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M57",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 498,
    "DeviceFullCode": "56M202M11M498",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M57",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 499,
    "DeviceFullCode": "56M202M11M499",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M57",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 500,
    "DeviceFullCode": "56M202M11M500",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M57",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 501,
    "DeviceFullCode": "56M202M11M501",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M57",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 502,
    "DeviceFullCode": "56M202M11M502",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M57",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 503,
    "DeviceFullCode": "56M202M11M503",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M57",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 504,
    "DeviceFullCode": "56M202M11M504",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M57",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 505,
    "DeviceFullCode": "56M202M11M505",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M58",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 506,
    "DeviceFullCode": "56M202M11M506",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M58",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 507,
    "DeviceFullCode": "56M202M11M507",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M58",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 508,
    "DeviceFullCode": "56M202M11M508",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M58",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 509,
    "DeviceFullCode": "56M202M11M509",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M58",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 510,
    "DeviceFullCode": "56M202M11M510",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M58",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 511,
    "DeviceFullCode": "56M202M11M511",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M58",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 512,
    "DeviceFullCode": "56M202M11M512",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M58",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 513,
    "DeviceFullCode": "56M202M11M513",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M57",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 514,
    "DeviceFullCode": "56M202M11M514",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M58",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 515,
    "DeviceFullCode": "56M202M11M515",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M59",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 516,
    "DeviceFullCode": "56M202M11M516",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M59",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 517,
    "DeviceFullCode": "56M202M11M517",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M59",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 518,
    "DeviceFullCode": "56M202M11M518",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M59",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 519,
    "DeviceFullCode": "56M202M11M519",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M59",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 520,
    "DeviceFullCode": "56M202M11M520",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M60",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 521,
    "DeviceFullCode": "56M202M11M521",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M59",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 522,
    "DeviceFullCode": "56M202M11M522",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M59",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 523,
    "DeviceFullCode": "56M202M11M523",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M59",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 524,
    "DeviceFullCode": "56M202M11M524",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M59",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 525,
    "DeviceFullCode": "56M202M11M525",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M60",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 526,
    "DeviceFullCode": "56M202M11M526",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M60",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 527,
    "DeviceFullCode": "56M202M11M527",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M60",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 528,
    "DeviceFullCode": "56M202M11M528",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M60",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 529,
    "DeviceFullCode": "56M202M11M529",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M60",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 530,
    "DeviceFullCode": "56M202M11M530",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M60",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 531,
    "DeviceFullCode": "56M202M11M531",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M60",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 532,
    "DeviceFullCode": "56M202M11M532",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M60",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 533,
    "DeviceFullCode": "56M202M11M533",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M61",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 534,
    "DeviceFullCode": "56M202M11M534",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M61",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 535,
    "DeviceFullCode": "56M202M11M535",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M61",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 536,
    "DeviceFullCode": "56M202M11M536",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M62",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 537,
    "DeviceFullCode": "56M202M11M537",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M61",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 538,
    "DeviceFullCode": "56M202M11M538",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M61",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 539,
    "DeviceFullCode": "56M202M11M539",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M61",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 540,
    "DeviceFullCode": "56M202M11M540",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M61",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 541,
    "DeviceFullCode": "56M202M11M541",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M61",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 542,
    "DeviceFullCode": "56M202M11M542",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M61",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 543,
    "DeviceFullCode": "56M202M11M543",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M62",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 544,
    "DeviceFullCode": "56M202M11M544",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M62",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 545,
    "DeviceFullCode": "56M202M11M545",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M62",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 546,
    "DeviceFullCode": "56M202M11M546",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M62",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 547,
    "DeviceFullCode": "56M202M11M547",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M62",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 548,
    "DeviceFullCode": "56M202M11M548",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M62",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 549,
    "DeviceFullCode": "56M202M11M549",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M62",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 550,
    "DeviceFullCode": "56M202M11M550",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M62",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 551,
    "DeviceFullCode": "56M202M11M551",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M63",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 552,
    "DeviceFullCode": "56M202M11M552",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M63",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 553,
    "DeviceFullCode": "56M202M11M553",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M63",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 554,
    "DeviceFullCode": "56M202M11M554",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M63",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 555,
    "DeviceFullCode": "56M202M11M555",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M63",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 556,
    "DeviceFullCode": "56M202M11M556",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M63",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 557,
    "DeviceFullCode": "56M202M11M557",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M63",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 558,
    "DeviceFullCode": "56M202M11M558",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M64",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 559,
    "DeviceFullCode": "56M202M11M559",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M64",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 560,
    "DeviceFullCode": "56M202M11M560",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M64",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 561,
    "DeviceFullCode": "56M202M11M561",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M63",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 562,
    "DeviceFullCode": "56M202M11M562",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M63",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 563,
    "DeviceFullCode": "56M202M11M563",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M64",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 564,
    "DeviceFullCode": "56M202M11M564",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M64",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 565,
    "DeviceFullCode": "56M202M11M565",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M64",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 566,
    "DeviceFullCode": "56M202M11M566",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M64",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 567,
    "DeviceFullCode": "56M202M11M567",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M64",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 568,
    "DeviceFullCode": "56M202M11M568",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M64",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 569,
    "DeviceFullCode": "56M202M11M569",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M65",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 570,
    "DeviceFullCode": "56M202M11M570",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M65",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 571,
    "DeviceFullCode": "56M202M11M571",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M65",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 572,
    "DeviceFullCode": "56M202M11M572",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M65",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 573,
    "DeviceFullCode": "56M202M11M573",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M65",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 574,
    "DeviceFullCode": "56M202M11M574",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M65",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 575,
    "DeviceFullCode": "56M202M11M575",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M65",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 576,
    "DeviceFullCode": "56M202M11M576",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M65",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 577,
    "DeviceFullCode": "56M202M11M577",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M66",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 578,
    "DeviceFullCode": "56M202M11M578",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M66",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 579,
    "DeviceFullCode": "56M202M11M579",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M66",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 580,
    "DeviceFullCode": "56M202M11M580",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M66",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 581,
    "DeviceFullCode": "56M202M11M581",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M66",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 582,
    "DeviceFullCode": "56M202M11M582",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M66",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 583,
    "DeviceFullCode": "56M202M11M583",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M66",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 584,
    "DeviceFullCode": "56M202M11M584",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M66",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 585,
    "DeviceFullCode": "56M202M11M585",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M65",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 586,
    "DeviceFullCode": "56M202M11M586",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M66",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 587,
    "DeviceFullCode": "56M202M11M587",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M67",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 588,
    "DeviceFullCode": "56M202M11M588",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M67",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 589,
    "DeviceFullCode": "56M202M11M589",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M67",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 590,
    "DeviceFullCode": "56M202M11M590",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M67",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 591,
    "DeviceFullCode": "56M202M11M591",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M67",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 592,
    "DeviceFullCode": "56M202M11M592",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M67",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 593,
    "DeviceFullCode": "56M202M11M593",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M68",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 594,
    "DeviceFullCode": "56M202M11M594",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M67",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 595,
    "DeviceFullCode": "56M202M11M595",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M67",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 596,
    "DeviceFullCode": "56M202M11M596",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M67",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 597,
    "DeviceFullCode": "56M202M11M597",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M68",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 598,
    "DeviceFullCode": "56M202M11M598",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M68",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 599,
    "DeviceFullCode": "56M202M11M599",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M68",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 600,
    "DeviceFullCode": "56M202M11M600",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M68",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 601,
    "DeviceFullCode": "56M202M11M601",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M68",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 602,
    "DeviceFullCode": "56M202M11M602",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M68",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 603,
    "DeviceFullCode": "56M202M11M603",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M68",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 604,
    "DeviceFullCode": "56M202M11M604",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M68",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 605,
    "DeviceFullCode": "56M202M11M605",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M69",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 606,
    "DeviceFullCode": "56M202M11M606",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M70",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 607,
    "DeviceFullCode": "56M202M11M607",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M69",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 608,
    "DeviceFullCode": "56M202M11M608",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M69",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 609,
    "DeviceFullCode": "56M202M11M609",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M69",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 610,
    "DeviceFullCode": "56M202M11M610",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M69",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 611,
    "DeviceFullCode": "56M202M11M611",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M69",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 612,
    "DeviceFullCode": "56M202M11M612",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M69",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 613,
    "DeviceFullCode": "56M202M11M613",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M69",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 614,
    "DeviceFullCode": "56M202M11M614",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M69",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 615,
    "DeviceFullCode": "56M202M11M615",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M70",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 616,
    "DeviceFullCode": "56M202M11M616",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M70",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 617,
    "DeviceFullCode": "56M202M11M617",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M70",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 618,
    "DeviceFullCode": "56M202M11M618",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M70",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 619,
    "DeviceFullCode": "56M202M11M619",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M70",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 620,
    "DeviceFullCode": "56M202M11M620",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M70",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 621,
    "DeviceFullCode": "56M202M11M621",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M70",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 622,
    "DeviceFullCode": "56M202M11M622",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M70",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 623,
    "DeviceFullCode": "56M202M11M623",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M71",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 624,
    "DeviceFullCode": "56M202M11M624",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M72",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 625,
    "DeviceFullCode": "56M202M11M625",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M72",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 626,
    "DeviceFullCode": "56M202M11M626",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M72",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 627,
    "DeviceFullCode": "56M202M11M627",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M71",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 628,
    "DeviceFullCode": "56M202M11M628",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M71",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 629,
    "DeviceFullCode": "56M202M11M629",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M71",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 630,
    "DeviceFullCode": "56M202M11M630",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M72",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 631,
    "DeviceFullCode": "56M202M11M631",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M72",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 632,
    "DeviceFullCode": "56M202M11M632",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M71",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 633,
    "DeviceFullCode": "56M202M11M633",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M71",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 634,
    "DeviceFullCode": "56M202M11M634",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M71",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 635,
    "DeviceFullCode": "56M202M11M635",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M71",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 636,
    "DeviceFullCode": "56M202M11M636",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M72",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 637,
    "DeviceFullCode": "56M202M11M637",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M71",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 638,
    "DeviceFullCode": "56M202M11M638",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M72",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 639,
    "DeviceFullCode": "56M202M11M639",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M72",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 640,
    "DeviceFullCode": "56M202M11M640",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M72",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 641,
    "DeviceFullCode": "56M202M11M641",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M73",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 642,
    "DeviceFullCode": "56M202M11M642",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M73",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 643,
    "DeviceFullCode": "56M202M11M643",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M73",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 644,
    "DeviceFullCode": "56M202M11M644",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M73",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 645,
    "DeviceFullCode": "56M202M11M645",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M73",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 646,
    "DeviceFullCode": "56M202M11M646",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M73",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 647,
    "DeviceFullCode": "56M202M11M647",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M73",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 648,
    "DeviceFullCode": "56M202M11M648",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M73",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 649,
    "DeviceFullCode": "56M202M11M649",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M73",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 650,
    "DeviceFullCode": "56M202M11M650",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M74",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 651,
    "DeviceFullCode": "56M202M11M651",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M74",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 652,
    "DeviceFullCode": "56M202M11M652",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M74",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 653,
    "DeviceFullCode": "56M202M11M653",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M74",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 654,
    "DeviceFullCode": "56M202M11M654",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M74",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 655,
    "DeviceFullCode": "56M202M11M655",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M74",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 656,
    "DeviceFullCode": "56M202M11M656",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M74",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 657,
    "DeviceFullCode": "56M202M11M657",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M74",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 658,
    "DeviceFullCode": "56M202M11M658",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M74",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 659,
    "DeviceFullCode": "56M202M11M659",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M75",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 660,
    "DeviceFullCode": "56M202M11M660",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M75",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 661,
    "DeviceFullCode": "56M202M11M661",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M75",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 662,
    "DeviceFullCode": "56M202M11M662",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M76",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 663,
    "DeviceFullCode": "56M202M11M663",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M75",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 664,
    "DeviceFullCode": "56M202M11M664",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M75",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 665,
    "DeviceFullCode": "56M202M11M665",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M75",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 666,
    "DeviceFullCode": "56M202M11M666",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M75",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 667,
    "DeviceFullCode": "56M202M11M667",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M75",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 668,
    "DeviceFullCode": "56M202M11M668",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M76",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 669,
    "DeviceFullCode": "56M202M11M669",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M76",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 670,
    "DeviceFullCode": "56M202M11M670",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M76",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 671,
    "DeviceFullCode": "56M202M11M671",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M76",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 672,
    "DeviceFullCode": "56M202M11M672",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M76",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 673,
    "DeviceFullCode": "56M202M11M673",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M76",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 674,
    "DeviceFullCode": "56M202M11M674",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M76",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 675,
    "DeviceFullCode": "56M202M11M675",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M75",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 676,
    "DeviceFullCode": "56M202M11M676",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M76",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 677,
    "DeviceFullCode": "56M202M11M677",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M77",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 678,
    "DeviceFullCode": "56M202M11M678",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M77",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 679,
    "DeviceFullCode": "56M202M11M679",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M77",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 680,
    "DeviceFullCode": "56M202M11M680",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M77",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 681,
    "DeviceFullCode": "56M202M11M681",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M77",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 682,
    "DeviceFullCode": "56M202M11M682",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M77",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 683,
    "DeviceFullCode": "56M202M11M683",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M77",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 684,
    "DeviceFullCode": "56M202M11M684",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M78",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 685,
    "DeviceFullCode": "56M202M11M685",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M78",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 686,
    "DeviceFullCode": "56M202M11M686",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M78",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 687,
    "DeviceFullCode": "56M202M11M687",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M77",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 688,
    "DeviceFullCode": "56M202M11M688",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M78",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 689,
    "DeviceFullCode": "56M202M11M689",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M78",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 690,
    "DeviceFullCode": "56M202M11M690",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M78",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 691,
    "DeviceFullCode": "56M202M11M691",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M78",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 692,
    "DeviceFullCode": "56M202M11M692",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M78",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 693,
    "DeviceFullCode": "56M202M11M693",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M78",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 694,
    "DeviceFullCode": "56M202M11M694",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M77",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 695,
    "DeviceFullCode": "56M202M11M695",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M79",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 696,
    "DeviceFullCode": "56M202M11M696",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M79",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 697,
    "DeviceFullCode": "56M202M11M697",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M79",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 698,
    "DeviceFullCode": "56M202M11M698",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M79",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 699,
    "DeviceFullCode": "56M202M11M699",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M80",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 700,
    "DeviceFullCode": "56M202M11M700",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M79",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 701,
    "DeviceFullCode": "56M202M11M701",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M79",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 702,
    "DeviceFullCode": "56M202M11M702",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M79",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 703,
    "DeviceFullCode": "56M202M11M703",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M79",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 704,
    "DeviceFullCode": "56M202M11M704",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M79",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 705,
    "DeviceFullCode": "56M202M11M705",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M80",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 706,
    "DeviceFullCode": "56M202M11M706",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M80",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 707,
    "DeviceFullCode": "56M202M11M707",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M80",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 708,
    "DeviceFullCode": "56M202M11M708",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M80",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 709,
    "DeviceFullCode": "56M202M11M709",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M80",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 710,
    "DeviceFullCode": "56M202M11M710",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M80",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 711,
    "DeviceFullCode": "56M202M11M711",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M80",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 712,
    "DeviceFullCode": "56M202M11M712",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M80",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 713,
    "DeviceFullCode": "56M202M11M713",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M81",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 714,
    "DeviceFullCode": "56M202M11M714",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M81",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 715,
    "DeviceFullCode": "56M202M11M715",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M81",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 716,
    "DeviceFullCode": "56M202M11M716",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M81",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 717,
    "DeviceFullCode": "56M202M11M717",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M82",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 718,
    "DeviceFullCode": "56M202M11M718",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M81",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 719,
    "DeviceFullCode": "56M202M11M719",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M81",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 720,
    "DeviceFullCode": "56M202M11M720",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M81",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 721,
    "DeviceFullCode": "56M202M11M721",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M82",
    "Capacity": 48.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 722,
    "DeviceFullCode": "56M202M11M722",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M81",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 723,
    "DeviceFullCode": "56M202M11M723",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M81",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 724,
    "DeviceFullCode": "56M202M11M724",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M82",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 725,
    "DeviceFullCode": "56M202M11M725",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M82",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 726,
    "DeviceFullCode": "56M202M11M726",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M82",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 727,
    "DeviceFullCode": "56M202M11M727",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M82",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 728,
    "DeviceFullCode": "56M202M11M728",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M82",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 729,
    "DeviceFullCode": "56M202M11M729",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M82",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 730,
    "DeviceFullCode": "56M202M11M730",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M82",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 731,
    "DeviceFullCode": "56M202M11M731",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M83",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 732,
    "DeviceFullCode": "56M202M11M732",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M83",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 733,
    "DeviceFullCode": "56M202M11M733",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M83",
    "Capacity": 59.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 734,
    "DeviceFullCode": "56M202M11M734",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M83",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 735,
    "DeviceFullCode": "56M202M11M735",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M83",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 736,
    "DeviceFullCode": "56M202M11M736",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M83",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 737,
    "DeviceFullCode": "56M202M11M737",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M84",
    "Capacity": 54.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 738,
    "DeviceFullCode": "56M202M11M738",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M83",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 739,
    "DeviceFullCode": "56M202M11M739",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M83",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 740,
    "DeviceFullCode": "56M202M11M740",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M83",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 741,
    "DeviceFullCode": "56M202M11M741",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M84",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 742,
    "DeviceFullCode": "56M202M11M742",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M84",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 743,
    "DeviceFullCode": "56M202M11M743",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M84",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 744,
    "DeviceFullCode": "56M202M11M744",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M84",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 745,
    "DeviceFullCode": "56M202M11M745",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M84",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 746,
    "DeviceFullCode": "56M202M11M746",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M84",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 747,
    "DeviceFullCode": "56M202M11M747",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M84",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 748,
    "DeviceFullCode": "56M202M11M748",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M84",
    "Capacity": 64.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 749,
    "DeviceFullCode": "56M202M11M749",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M85",
    "Capacity": 81.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 750,
    "DeviceFullCode": "56M202M11M750",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M85",
    "Capacity": 81.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 751,
    "DeviceFullCode": "56M202M11M751",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M85",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 752,
    "DeviceFullCode": "56M202M11M752",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M85",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 753,
    "DeviceFullCode": "56M202M11M753",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M86",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 754,
    "DeviceFullCode": "56M202M11M754",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M85",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 755,
    "DeviceFullCode": "56M202M11M755",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M85",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 756,
    "DeviceFullCode": "56M202M11M756",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M85",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 757,
    "DeviceFullCode": "56M202M11M757",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M86",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 758,
    "DeviceFullCode": "56M202M11M758",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M86",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 759,
    "DeviceFullCode": "56M202M11M759",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M86",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 760,
    "DeviceFullCode": "56M202M11M760",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M86",
    "Capacity": 81.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 761,
    "DeviceFullCode": "56M202M11M761",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M86",
    "Capacity": 81.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 762,
    "DeviceFullCode": "56M202M11M762",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M86",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 763,
    "DeviceFullCode": "56M202M11M763",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M87",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 764,
    "DeviceFullCode": "56M202M11M764",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M87",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 765,
    "DeviceFullCode": "56M202M11M765",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M87",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 766,
    "DeviceFullCode": "56M202M11M766",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M87",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 767,
    "DeviceFullCode": "56M202M11M767",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M87",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 768,
    "DeviceFullCode": "56M202M11M768",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M88",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 769,
    "DeviceFullCode": "56M202M11M769",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M88",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 770,
    "DeviceFullCode": "56M202M11M770",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M88",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 771,
    "DeviceFullCode": "56M202M11M771",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M87",
    "Capacity": 81.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 772,
    "DeviceFullCode": "56M202M11M772",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M88",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 773,
    "DeviceFullCode": "56M202M11M773",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M88",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 774,
    "DeviceFullCode": "56M202M11M774",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M87",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 775,
    "DeviceFullCode": "56M202M11M775",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M88",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 776,
    "DeviceFullCode": "56M202M11M776",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M88",
    "Capacity": 81.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 777,
    "DeviceFullCode": "56M202M11M777",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M89",
    "Capacity": 81.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 778,
    "DeviceFullCode": "56M202M11M778",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M89",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 779,
    "DeviceFullCode": "56M202M11M779",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M89",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 780,
    "DeviceFullCode": "56M202M11M780",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M89",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 781,
    "DeviceFullCode": "56M202M11M781",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M89",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 782,
    "DeviceFullCode": "56M202M11M782",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M90",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 783,
    "DeviceFullCode": "56M202M11M783",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M89",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 784,
    "DeviceFullCode": "56M202M11M784",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M89",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 785,
    "DeviceFullCode": "56M202M11M785",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M90",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 786,
    "DeviceFullCode": "56M202M11M786",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M90",
    "Capacity": 81.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 787,
    "DeviceFullCode": "56M202M11M787",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M90",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 788,
    "DeviceFullCode": "56M202M11M788",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M90",
    "Capacity": 70.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 789,
    "DeviceFullCode": "56M202M11M789",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M90",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 11,
    "DeviceCode": 790,
    "DeviceFullCode": "56M202M11M790",
    "DeviceModeFullCode": "56M202M11",
    "PDeviceFullCode": "56M201M9M90",
    "Capacity": 75.6000
  },
  {
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceCode": 1,
    "DeviceFullCode": "56M203M8M1",
    "DeviceModeFullCode": "56M203M8",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 203,
    "DeviceModeCode": 10,
    "DeviceCode": 2,
    "DeviceFullCode": "56M203M10M2",
    "DeviceModeFullCode": "56M203M10",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceCode": 1,
    "DeviceFullCode": "56M302M22M1",
    "DeviceModeFullCode": "56M302M22",
    "PDeviceFullCode": None,
    "Capacity": 5659.2000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceCode": 2,
    "DeviceFullCode": "56M302M22M2",
    "DeviceModeFullCode": "56M302M22",
    "PDeviceFullCode": None,
    "Capacity": 5670.0000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceCode": 3,
    "DeviceFullCode": "56M302M22M3",
    "DeviceModeFullCode": "56M302M22",
    "PDeviceFullCode": None,
    "Capacity": 5443.2000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceCode": 4,
    "DeviceFullCode": "56M302M22M4",
    "DeviceModeFullCode": "56M302M22",
    "PDeviceFullCode": None,
    "Capacity": 5718.6000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceCode": 5,
    "DeviceFullCode": "56M302M22M5",
    "DeviceModeFullCode": "56M302M22",
    "PDeviceFullCode": None,
    "Capacity": 5729.4000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceCode": 6,
    "DeviceFullCode": "56M302M22M6",
    "DeviceModeFullCode": "56M302M22",
    "PDeviceFullCode": None,
    "Capacity": 5729.4000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceCode": 7,
    "DeviceFullCode": "56M302M22M7",
    "DeviceModeFullCode": "56M302M22",
    "PDeviceFullCode": None,
    "Capacity": 5734.8000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceCode": 8,
    "DeviceFullCode": "56M302M22M8",
    "DeviceModeFullCode": "56M302M22",
    "PDeviceFullCode": None,
    "Capacity": 5670.0000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 22,
    "DeviceCode": 9,
    "DeviceFullCode": "56M302M22M9",
    "DeviceModeFullCode": "56M302M22",
    "PDeviceFullCode": None,
    "Capacity": 5686.2000
  },
  {
    "DeviceTypeCode": 305,
    "DeviceModeCode": 14,
    "DeviceCode": 1,
    "DeviceFullCode": "56M305M14M1",
    "DeviceModeFullCode": "56M305M14",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 307,
    "DeviceModeCode": 20,
    "DeviceCode": 1,
    "DeviceFullCode": "56M307M20M1",
    "DeviceModeFullCode": "56M307M20",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 18,
    "DeviceCode": 3,
    "DeviceFullCode": "56M505M18M3",
    "DeviceModeFullCode": "56M505M18",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 18,
    "DeviceCode": 4,
    "DeviceFullCode": "56M505M18M4",
    "DeviceModeFullCode": "56M505M18",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 18,
    "DeviceCode": 5,
    "DeviceFullCode": "56M505M18M5",
    "DeviceModeFullCode": "56M505M18",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 18,
    "DeviceCode": 6,
    "DeviceFullCode": "56M505M18M6",
    "DeviceModeFullCode": "56M505M18",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 18,
    "DeviceCode": 7,
    "DeviceFullCode": "56M505M18M7",
    "DeviceModeFullCode": "56M505M18",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 18,
    "DeviceCode": 8,
    "DeviceFullCode": "56M505M18M8",
    "DeviceModeFullCode": "56M505M18",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 18,
    "DeviceCode": 9,
    "DeviceFullCode": "56M505M18M9",
    "DeviceModeFullCode": "56M505M18",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 18,
    "DeviceCode": 10,
    "DeviceFullCode": "56M505M18M10",
    "DeviceModeFullCode": "56M505M18",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 18,
    "DeviceCode": 11,
    "DeviceFullCode": "56M505M18M11",
    "DeviceModeFullCode": "56M505M18",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 18,
    "DeviceCode": 12,
    "DeviceFullCode": "56M505M18M12",
    "DeviceModeFullCode": "56M505M18",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 18,
    "DeviceCode": 13,
    "DeviceFullCode": "56M505M18M13",
    "DeviceModeFullCode": "56M505M18",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 18,
    "DeviceCode": 14,
    "DeviceFullCode": "56M505M18M14",
    "DeviceModeFullCode": "56M505M18",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceCode": 15,
    "DeviceFullCode": "56M505M7M15",
    "DeviceModeFullCode": "56M505M7",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceCode": 16,
    "DeviceFullCode": "56M505M7M16",
    "DeviceModeFullCode": "56M505M7",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceCode": 1,
    "DeviceFullCode": "56M801M1M1",
    "DeviceModeFullCode": "56M801M1",
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
        self.stationCode = 56
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
                    if deviceTypeCode==203 and deviceItem['DeviceFullCode']=="56M203M10M2":
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
