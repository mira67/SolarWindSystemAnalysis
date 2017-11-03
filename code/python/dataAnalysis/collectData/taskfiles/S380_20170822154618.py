#-*- coding: UTF-8 -*-

# 读取气象站数据
# 读取逆变器数据
# 读取汇流箱数据
# 计算天数据
DATETIME_FMT = '%Y-%m-%d %H:%M' 


deviceModePointConfig=[
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB003",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "DC_W",
    "DeviceModePointName": "逆变器直流侧输入功率",
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
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "逆变器总运行时间",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "逆变器总运行时间",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "逆变器总运行时间",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "逆变器总运行时间",
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
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
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
    "DeviceModePointCode": "HL107",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_All",
    "DeviceModePointName": "汇流箱各串电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL107",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_All",
    "DeviceModePointName": "汇流箱各串电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL107",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_All",
    "DeviceModePointName": "汇流箱各串电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL107",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceModePointIECName": "Branch_All",
    "DeviceModePointName": "汇流箱各串电流",
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
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX601",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX601",
    "DeviceModePointName": "风速2分钟平均值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX601",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX601",
    "DeviceModePointName": "风速2分钟平均值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX601",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX601",
    "DeviceModePointName": "风速2分钟平均值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX601",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX601",
    "DeviceModePointName": "风速2分钟平均值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX602",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX602",
    "DeviceModePointName": "风速10分钟钟平均值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX602",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX602",
    "DeviceModePointName": "风速10分钟钟平均值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX602",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX602",
    "DeviceModePointName": "风速10分钟钟平均值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX602",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX602",
    "DeviceModePointName": "风速10分钟钟平均值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX603",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX603",
    "DeviceModePointName": "露点温度瞬时",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX603",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX603",
    "DeviceModePointName": "露点温度瞬时",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX603",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX603",
    "DeviceModePointName": "露点温度瞬时",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX603",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX603",
    "DeviceModePointName": "露点温度瞬时",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX604",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX604",
    "DeviceModePointName": "电量",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX604",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX604",
    "DeviceModePointName": "电量",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX604",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX604",
    "DeviceModePointName": "电量",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX604",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX604",
    "DeviceModePointName": "电量",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX605",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX605",
    "DeviceModePointName": "日照时数",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX605",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX605",
    "DeviceModePointName": "日照时数",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX605",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX605",
    "DeviceModePointName": "日照时数",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX605",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX605",
    "DeviceModePointName": "日照时数",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX606",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX606",
    "DeviceModePointName": "CR800电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX606",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX606",
    "DeviceModePointName": "CR800电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX606",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX606",
    "DeviceModePointName": "CR800电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX606",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX606",
    "DeviceModePointName": "CR800电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX607",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX607",
    "DeviceModePointName": "CR800采集器面板温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX607",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX607",
    "DeviceModePointName": "CR800采集器面板温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX607",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX607",
    "DeviceModePointName": "CR800采集器面板温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX607",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "QX607",
    "DeviceModePointName": "CR800采集器面板温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
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
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
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
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
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
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Std",
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
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB001",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUab",
    "DeviceModePointName": "高压侧Uab",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB001",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUab",
    "DeviceModePointName": "高压侧Uab",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB001",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUab",
    "DeviceModePointName": "高压侧Uab",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB001",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUab",
    "DeviceModePointName": "高压侧Uab",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB002",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUbc",
    "DeviceModePointName": "高压侧Ubc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB002",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUbc",
    "DeviceModePointName": "高压侧Ubc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB002",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUbc",
    "DeviceModePointName": "高压侧Ubc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB002",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUbc",
    "DeviceModePointName": "高压侧Ubc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB003",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUca",
    "DeviceModePointName": "高压侧Uca",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB003",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUca",
    "DeviceModePointName": "高压侧Uca",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB003",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUca",
    "DeviceModePointName": "高压侧Uca",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB003",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUca",
    "DeviceModePointName": "高压侧Uca",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB004",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUa",
    "DeviceModePointName": "高压侧Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB004",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUa",
    "DeviceModePointName": "高压侧Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB004",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUa",
    "DeviceModePointName": "高压侧Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB004",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUa",
    "DeviceModePointName": "高压侧Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB005",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUb",
    "DeviceModePointName": "高压侧Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB005",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUb",
    "DeviceModePointName": "高压侧Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB005",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUb",
    "DeviceModePointName": "高压侧Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB005",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUb",
    "DeviceModePointName": "高压侧Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB006",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUc",
    "DeviceModePointName": "高压侧Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB006",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUc",
    "DeviceModePointName": "高压侧Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB006",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUc",
    "DeviceModePointName": "高压侧Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB006",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPPhVUc",
    "DeviceModePointName": "高压侧Uc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB007",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGri3U0",
    "DeviceModePointName": "高压侧3U0",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB007",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGri3U0",
    "DeviceModePointName": "高压侧3U0",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB007",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGri3U0",
    "DeviceModePointName": "高压侧3U0",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB007",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGri3U0",
    "DeviceModePointName": "高压侧3U0",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB009",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriAIa",
    "DeviceModePointName": "高压侧Ia",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB009",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriAIa",
    "DeviceModePointName": "高压侧Ia",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB009",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriAIa",
    "DeviceModePointName": "高压侧Ia",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB009",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriAIa",
    "DeviceModePointName": "高压侧Ia",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB010",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriAIb",
    "DeviceModePointName": "高压侧Ib",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB010",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriAIb",
    "DeviceModePointName": "高压侧Ib",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB010",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriAIb",
    "DeviceModePointName": "高压侧Ib",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB010",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriAIb",
    "DeviceModePointName": "高压侧Ib",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB011",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriAIc",
    "DeviceModePointName": "高压侧Ic",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB011",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriAIc",
    "DeviceModePointName": "高压侧Ic",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB011",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriAIc",
    "DeviceModePointName": "高压侧Ic",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB011",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriAIc",
    "DeviceModePointName": "高压侧Ic",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB012",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGri3I0",
    "DeviceModePointName": "高压侧3I0",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB012",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGri3I0",
    "DeviceModePointName": "高压侧3I0",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB012",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGri3I0",
    "DeviceModePointName": "高压侧3I0",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB012",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGri3I0",
    "DeviceModePointName": "高压侧3I0",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB013",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriW",
    "DeviceModePointName": "高压侧P",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB013",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriW",
    "DeviceModePointName": "高压侧P",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB013",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriW",
    "DeviceModePointName": "高压侧P",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB013",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriW",
    "DeviceModePointName": "高压侧P",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB014",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriVar",
    "DeviceModePointName": "高压侧Q",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB014",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriVar",
    "DeviceModePointName": "高压侧Q",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB014",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriVar",
    "DeviceModePointName": "高压侧Q",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB014",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriVar",
    "DeviceModePointName": "高压侧Q",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB015",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPF",
    "DeviceModePointName": "高压侧Cos",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB015",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPF",
    "DeviceModePointName": "高压侧Cos",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB015",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPF",
    "DeviceModePointName": "高压侧Cos",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB015",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriPF",
    "DeviceModePointName": "高压侧Cos",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB016",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriHz",
    "DeviceModePointName": "高压侧Fr",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB016",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriHz",
    "DeviceModePointName": "高压侧Fr",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB016",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriHz",
    "DeviceModePointName": "高压侧Fr",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB016",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "HiGriHz",
    "DeviceModePointName": "高压侧Fr",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB017",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUab",
    "DeviceModePointName": "低压侧Uab",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB017",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUab",
    "DeviceModePointName": "低压侧Uab",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB017",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUab",
    "DeviceModePointName": "低压侧Uab",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB017",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUab",
    "DeviceModePointName": "低压侧Uab",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB018",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUbc",
    "DeviceModePointName": "低压侧Ubc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB018",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUbc",
    "DeviceModePointName": "低压侧Ubc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB018",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUbc",
    "DeviceModePointName": "低压侧Ubc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB018",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUbc",
    "DeviceModePointName": "低压侧Ubc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB019",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUca",
    "DeviceModePointName": "低压侧Uca",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB019",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUca",
    "DeviceModePointName": "低压侧Uca",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB019",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUca",
    "DeviceModePointName": "低压侧Uca",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB019",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUca",
    "DeviceModePointName": "低压侧Uca",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB020",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUa",
    "DeviceModePointName": "低压侧Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB020",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUa",
    "DeviceModePointName": "低压侧Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB020",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUa",
    "DeviceModePointName": "低压侧Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB020",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUa",
    "DeviceModePointName": "低压侧Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB021",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUb",
    "DeviceModePointName": "低压侧Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB021",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUb",
    "DeviceModePointName": "低压侧Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB021",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUb",
    "DeviceModePointName": "低压侧Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB021",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUb",
    "DeviceModePointName": "低压侧Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB022",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUc",
    "DeviceModePointName": "低压侧Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB022",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUc",
    "DeviceModePointName": "低压侧Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB022",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUc",
    "DeviceModePointName": "低压侧Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB022",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPPhVUc",
    "DeviceModePointName": "低压侧Uc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB023",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGri3U0",
    "DeviceModePointName": "低压侧3U0",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB023",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGri3U0",
    "DeviceModePointName": "低压侧3U0",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB023",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGri3U0",
    "DeviceModePointName": "低压侧3U0",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB023",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGri3U0",
    "DeviceModePointName": "低压侧3U0",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB025",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriAIa",
    "DeviceModePointName": "低压侧Ia",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB025",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriAIa",
    "DeviceModePointName": "低压侧Ia",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB025",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriAIa",
    "DeviceModePointName": "低压侧Ia",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB025",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriAIa",
    "DeviceModePointName": "低压侧Ia",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB026",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriAIb",
    "DeviceModePointName": "低压侧Ib",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB026",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriAIb",
    "DeviceModePointName": "低压侧Ib",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB026",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriAIb",
    "DeviceModePointName": "低压侧Ib",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB026",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriAIb",
    "DeviceModePointName": "低压侧Ib",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB027",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriAIc",
    "DeviceModePointName": "低压侧Ic",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB027",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriAIc",
    "DeviceModePointName": "低压侧Ic",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB027",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriAIc",
    "DeviceModePointName": "低压侧Ic",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB027",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriAIc",
    "DeviceModePointName": "低压侧Ic",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB028",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGri3I0",
    "DeviceModePointName": "低压侧3I0",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB028",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGri3I0",
    "DeviceModePointName": "低压侧3I0",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB028",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGri3I0",
    "DeviceModePointName": "低压侧3I0",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB028",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGri3I0",
    "DeviceModePointName": "低压侧3I0",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB029",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriW",
    "DeviceModePointName": "低压侧P",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB029",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriW",
    "DeviceModePointName": "低压侧P",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB029",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriW",
    "DeviceModePointName": "低压侧P",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB029",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriW",
    "DeviceModePointName": "低压侧P",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB030",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriVar",
    "DeviceModePointName": "低压侧Q",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB030",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriVar",
    "DeviceModePointName": "低压侧Q",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB030",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriVar",
    "DeviceModePointName": "低压侧Q",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB030",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriVar",
    "DeviceModePointName": "低压侧Q",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB031",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPF",
    "DeviceModePointName": "低压侧Cos",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB031",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPF",
    "DeviceModePointName": "低压侧Cos",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB031",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPF",
    "DeviceModePointName": "低压侧Cos",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB031",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriPF",
    "DeviceModePointName": "低压侧Cos",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB032",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriHz",
    "DeviceModePointName": "低压侧Fr",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB032",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriHz",
    "DeviceModePointName": "低压侧Fr",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB032",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriHz",
    "DeviceModePointName": "低压侧Fr",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB032",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "LoGriHz",
    "DeviceModePointName": "低压侧Fr",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB033",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "WinTmp",
    "DeviceModePointName": "主变绕组温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB033",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "WinTmp",
    "DeviceModePointName": "主变绕组温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB033",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "WinTmp",
    "DeviceModePointName": "主变绕组温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB033",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "WinTmp",
    "DeviceModePointName": "主变绕组温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB034",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "OilTmp1",
    "DeviceModePointName": "主变油温1",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB034",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "OilTmp1",
    "DeviceModePointName": "主变油温1",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB034",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "OilTmp1",
    "DeviceModePointName": "主变油温1",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB034",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "OilTmp1",
    "DeviceModePointName": "主变油温1",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB035",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "OilTmp2",
    "DeviceModePointName": "主变油温2",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB035",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "OilTmp2",
    "DeviceModePointName": "主变油温2",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB035",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "OilTmp2",
    "DeviceModePointName": "主变油温2",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB035",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "OilTmp2",
    "DeviceModePointName": "主变油温2",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB036",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "Stl",
    "DeviceModePointName": "档位",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB036",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "Stl",
    "DeviceModePointName": "档位",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB036",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "Stl",
    "DeviceModePointName": "档位",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZB036",
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
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
    "DeviceModeCode": 2,
    "DeviceCode": 1,
    "DeviceFullCode": "380M201M2M1",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M1",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 2,
    "DeviceFullCode": "380M201M2M2",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M1",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 3,
    "DeviceFullCode": "380M201M2M3",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M4",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 4,
    "DeviceFullCode": "380M201M2M4",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M4",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 5,
    "DeviceFullCode": "380M201M2M5",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M5",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 6,
    "DeviceFullCode": "380M201M2M6",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M5",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 7,
    "DeviceFullCode": "380M201M2M7",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M6",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 8,
    "DeviceFullCode": "380M201M2M8",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M6",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 9,
    "DeviceFullCode": "380M201M2M9",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M8",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 10,
    "DeviceFullCode": "380M201M2M10",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M8",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 11,
    "DeviceFullCode": "380M201M2M11",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M10",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 12,
    "DeviceFullCode": "380M201M2M12",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M10",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 13,
    "DeviceFullCode": "380M201M2M13",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M11",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 14,
    "DeviceFullCode": "380M201M2M14",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M11",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 15,
    "DeviceFullCode": "380M201M2M15",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M12",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 16,
    "DeviceFullCode": "380M201M2M16",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M12",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 17,
    "DeviceFullCode": "380M201M2M17",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M13",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 18,
    "DeviceFullCode": "380M201M2M18",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M13",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 19,
    "DeviceFullCode": "380M201M2M19",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M14",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 20,
    "DeviceFullCode": "380M201M2M20",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M14",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 21,
    "DeviceFullCode": "380M201M2M21",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M15",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 22,
    "DeviceFullCode": "380M201M2M22",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M15",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 23,
    "DeviceFullCode": "380M201M2M23",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M16",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 24,
    "DeviceFullCode": "380M201M2M24",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M16",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 25,
    "DeviceFullCode": "380M201M2M25",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M17",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 26,
    "DeviceFullCode": "380M201M2M26",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M17",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 27,
    "DeviceFullCode": "380M201M2M27",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M18",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 28,
    "DeviceFullCode": "380M201M2M28",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M18",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 29,
    "DeviceFullCode": "380M201M2M29",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M19",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 30,
    "DeviceFullCode": "380M201M2M30",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M19",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 31,
    "DeviceFullCode": "380M201M2M31",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M20",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 32,
    "DeviceFullCode": "380M201M2M32",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M20",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 33,
    "DeviceFullCode": "380M201M2M33",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M21",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 34,
    "DeviceFullCode": "380M201M2M34",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M21",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 35,
    "DeviceFullCode": "380M201M2M35",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M22",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 36,
    "DeviceFullCode": "380M201M2M36",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M22",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 37,
    "DeviceFullCode": "380M201M2M37",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M23",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 38,
    "DeviceFullCode": "380M201M2M38",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M23",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 39,
    "DeviceFullCode": "380M201M2M39",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M24",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 40,
    "DeviceFullCode": "380M201M2M40",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M24",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 41,
    "DeviceFullCode": "380M201M2M41",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M25",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 42,
    "DeviceFullCode": "380M201M2M42",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M25",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 43,
    "DeviceFullCode": "380M201M2M43",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M26",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 44,
    "DeviceFullCode": "380M201M2M44",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M26",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 45,
    "DeviceFullCode": "380M201M2M45",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M27",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 46,
    "DeviceFullCode": "380M201M2M46",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M27",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 47,
    "DeviceFullCode": "380M201M2M47",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M28",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 48,
    "DeviceFullCode": "380M201M2M48",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M28",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 49,
    "DeviceFullCode": "380M201M2M49",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M29",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 50,
    "DeviceFullCode": "380M201M2M50",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M29",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 51,
    "DeviceFullCode": "380M201M2M51",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M30",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 52,
    "DeviceFullCode": "380M201M2M52",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M30",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 53,
    "DeviceFullCode": "380M201M2M53",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M31",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 54,
    "DeviceFullCode": "380M201M2M54",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M31",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 55,
    "DeviceFullCode": "380M201M2M55",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M32",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 56,
    "DeviceFullCode": "380M201M2M56",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M32",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 57,
    "DeviceFullCode": "380M201M2M57",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M33",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 58,
    "DeviceFullCode": "380M201M2M58",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M33",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 59,
    "DeviceFullCode": "380M201M2M59",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M34",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 60,
    "DeviceFullCode": "380M201M2M60",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M34",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 61,
    "DeviceFullCode": "380M201M2M61",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M35",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 62,
    "DeviceFullCode": "380M201M2M62",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M35",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 63,
    "DeviceFullCode": "380M201M2M63",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M36",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 64,
    "DeviceFullCode": "380M201M2M64",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M36",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 65,
    "DeviceFullCode": "380M201M2M65",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M37",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 66,
    "DeviceFullCode": "380M201M2M66",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M37",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 67,
    "DeviceFullCode": "380M201M2M67",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M38",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 68,
    "DeviceFullCode": "380M201M2M68",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M38",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 69,
    "DeviceFullCode": "380M201M2M69",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M39",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 70,
    "DeviceFullCode": "380M201M2M70",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M39",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 71,
    "DeviceFullCode": "380M201M2M71",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M40",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 72,
    "DeviceFullCode": "380M201M2M72",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M40",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 73,
    "DeviceFullCode": "380M201M2M73",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M41",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 74,
    "DeviceFullCode": "380M201M2M74",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M41",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 75,
    "DeviceFullCode": "380M201M2M75",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M42",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 76,
    "DeviceFullCode": "380M201M2M76",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M42",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 77,
    "DeviceFullCode": "380M201M2M77",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M43",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 78,
    "DeviceFullCode": "380M201M2M78",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M43",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 79,
    "DeviceFullCode": "380M201M2M79",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M44",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 80,
    "DeviceFullCode": "380M201M2M80",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M44",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 81,
    "DeviceFullCode": "380M201M2M81",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M45",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 82,
    "DeviceFullCode": "380M201M2M82",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M45",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 83,
    "DeviceFullCode": "380M201M2M83",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M46",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 84,
    "DeviceFullCode": "380M201M2M84",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M46",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 85,
    "DeviceFullCode": "380M201M2M85",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M47",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 86,
    "DeviceFullCode": "380M201M2M86",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M47",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 87,
    "DeviceFullCode": "380M201M2M87",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M48",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 88,
    "DeviceFullCode": "380M201M2M88",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M48",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 89,
    "DeviceFullCode": "380M201M2M89",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M49",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 90,
    "DeviceFullCode": "380M201M2M90",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M49",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 91,
    "DeviceFullCode": "380M201M2M91",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M50",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 2,
    "DeviceCode": 92,
    "DeviceFullCode": "380M201M2M92",
    "DeviceModeFullCode": "380M201M2",
    "PDeviceFullCode": "380M204M2M50",
    "Capacity": 545.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 1,
    "DeviceFullCode": "380M202M6M1",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M1",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 2,
    "DeviceFullCode": "380M202M6M2",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M1",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 3,
    "DeviceFullCode": "380M202M6M3",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M1",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 4,
    "DeviceFullCode": "380M202M6M4",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M1",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 5,
    "DeviceFullCode": "380M202M6M5",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M1",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 6,
    "DeviceFullCode": "380M202M6M6",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M1",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 7,
    "DeviceFullCode": "380M202M6M7",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M1",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 8,
    "DeviceFullCode": "380M202M6M8",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M2",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 9,
    "DeviceFullCode": "380M202M6M9",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M2",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 10,
    "DeviceFullCode": "380M202M6M10",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M2",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 11,
    "DeviceFullCode": "380M202M6M11",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M2",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 12,
    "DeviceFullCode": "380M202M6M12",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M2",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 13,
    "DeviceFullCode": "380M202M6M13",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M2",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 14,
    "DeviceFullCode": "380M202M6M14",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M2",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 15,
    "DeviceFullCode": "380M202M6M15",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M3",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 16,
    "DeviceFullCode": "380M202M6M16",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M3",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 17,
    "DeviceFullCode": "380M202M6M17",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M3",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 18,
    "DeviceFullCode": "380M202M6M18",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M3",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 19,
    "DeviceFullCode": "380M202M6M19",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M3",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 20,
    "DeviceFullCode": "380M202M6M20",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M3",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 21,
    "DeviceFullCode": "380M202M6M21",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M3",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 22,
    "DeviceFullCode": "380M202M6M22",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M4",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 23,
    "DeviceFullCode": "380M202M6M23",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M4",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 24,
    "DeviceFullCode": "380M202M6M24",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M4",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 25,
    "DeviceFullCode": "380M202M6M25",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M4",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 26,
    "DeviceFullCode": "380M202M6M26",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M4",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 27,
    "DeviceFullCode": "380M202M6M27",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M4",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 28,
    "DeviceFullCode": "380M202M6M28",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M4",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 29,
    "DeviceFullCode": "380M202M6M29",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M5",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 30,
    "DeviceFullCode": "380M202M6M30",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M5",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 31,
    "DeviceFullCode": "380M202M6M31",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M5",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 32,
    "DeviceFullCode": "380M202M6M32",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M5",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 33,
    "DeviceFullCode": "380M202M6M33",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M5",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 34,
    "DeviceFullCode": "380M202M6M34",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M5",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 35,
    "DeviceFullCode": "380M202M6M35",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M5",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 36,
    "DeviceFullCode": "380M202M6M36",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M6",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 37,
    "DeviceFullCode": "380M202M6M37",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M6",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 38,
    "DeviceFullCode": "380M202M6M38",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M6",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 39,
    "DeviceFullCode": "380M202M6M39",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M6",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 40,
    "DeviceFullCode": "380M202M6M40",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M6",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 41,
    "DeviceFullCode": "380M202M6M41",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M6",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 42,
    "DeviceFullCode": "380M202M6M42",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M6",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 43,
    "DeviceFullCode": "380M202M6M43",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M7",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 44,
    "DeviceFullCode": "380M202M6M44",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M7",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 45,
    "DeviceFullCode": "380M202M6M45",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M7",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 46,
    "DeviceFullCode": "380M202M6M46",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M7",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 47,
    "DeviceFullCode": "380M202M6M47",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M7",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 48,
    "DeviceFullCode": "380M202M6M48",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M7",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 49,
    "DeviceFullCode": "380M202M6M49",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M7",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 50,
    "DeviceFullCode": "380M202M6M50",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M8",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 51,
    "DeviceFullCode": "380M202M6M51",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M8",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 52,
    "DeviceFullCode": "380M202M6M52",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M8",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 53,
    "DeviceFullCode": "380M202M6M53",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M8",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 54,
    "DeviceFullCode": "380M202M6M54",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M8",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 55,
    "DeviceFullCode": "380M202M6M55",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M8",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 56,
    "DeviceFullCode": "380M202M6M56",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M8",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 57,
    "DeviceFullCode": "380M202M6M57",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M9",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 58,
    "DeviceFullCode": "380M202M6M58",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M9",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 59,
    "DeviceFullCode": "380M202M6M59",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M9",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 60,
    "DeviceFullCode": "380M202M6M60",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M9",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 61,
    "DeviceFullCode": "380M202M6M61",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M9",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 62,
    "DeviceFullCode": "380M202M6M62",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M9",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 63,
    "DeviceFullCode": "380M202M6M63",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M9",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 64,
    "DeviceFullCode": "380M202M6M64",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M10",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 65,
    "DeviceFullCode": "380M202M6M65",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M10",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 66,
    "DeviceFullCode": "380M202M6M66",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M10",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 67,
    "DeviceFullCode": "380M202M6M67",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M10",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 68,
    "DeviceFullCode": "380M202M6M68",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M10",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 69,
    "DeviceFullCode": "380M202M6M69",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M10",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 70,
    "DeviceFullCode": "380M202M6M70",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M10",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 71,
    "DeviceFullCode": "380M202M6M71",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M11",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 72,
    "DeviceFullCode": "380M202M6M72",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M11",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 73,
    "DeviceFullCode": "380M202M6M73",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M11",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 74,
    "DeviceFullCode": "380M202M6M74",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M11",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 75,
    "DeviceFullCode": "380M202M6M75",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M11",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 76,
    "DeviceFullCode": "380M202M6M76",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M11",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 77,
    "DeviceFullCode": "380M202M6M77",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M11",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 78,
    "DeviceFullCode": "380M202M6M78",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M12",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 79,
    "DeviceFullCode": "380M202M6M79",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M12",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 80,
    "DeviceFullCode": "380M202M6M80",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M12",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 81,
    "DeviceFullCode": "380M202M6M81",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M12",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 82,
    "DeviceFullCode": "380M202M6M82",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M12",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 83,
    "DeviceFullCode": "380M202M6M83",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M12",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 84,
    "DeviceFullCode": "380M202M6M84",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M12",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 85,
    "DeviceFullCode": "380M202M6M85",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M13",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 86,
    "DeviceFullCode": "380M202M6M86",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M13",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 87,
    "DeviceFullCode": "380M202M6M87",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M13",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 88,
    "DeviceFullCode": "380M202M6M88",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M13",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 89,
    "DeviceFullCode": "380M202M6M89",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M13",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 90,
    "DeviceFullCode": "380M202M6M90",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M13",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 91,
    "DeviceFullCode": "380M202M6M91",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M13",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 92,
    "DeviceFullCode": "380M202M6M92",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M14",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 93,
    "DeviceFullCode": "380M202M6M93",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M14",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 94,
    "DeviceFullCode": "380M202M6M94",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M14",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 95,
    "DeviceFullCode": "380M202M6M95",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M14",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 96,
    "DeviceFullCode": "380M202M6M96",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M14",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 97,
    "DeviceFullCode": "380M202M6M97",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M14",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 98,
    "DeviceFullCode": "380M202M6M98",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M14",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 99,
    "DeviceFullCode": "380M202M6M99",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M15",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 100,
    "DeviceFullCode": "380M202M6M100",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M15",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 101,
    "DeviceFullCode": "380M202M6M101",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M15",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 102,
    "DeviceFullCode": "380M202M6M102",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M15",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 103,
    "DeviceFullCode": "380M202M6M103",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M15",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 104,
    "DeviceFullCode": "380M202M6M104",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M15",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 105,
    "DeviceFullCode": "380M202M6M105",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M15",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 106,
    "DeviceFullCode": "380M202M6M106",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M16",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 107,
    "DeviceFullCode": "380M202M6M107",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M16",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 108,
    "DeviceFullCode": "380M202M6M108",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M16",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 109,
    "DeviceFullCode": "380M202M6M109",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M16",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 110,
    "DeviceFullCode": "380M202M6M110",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M16",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 111,
    "DeviceFullCode": "380M202M6M111",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M16",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 112,
    "DeviceFullCode": "380M202M6M112",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M16",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 113,
    "DeviceFullCode": "380M202M6M113",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M17",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 114,
    "DeviceFullCode": "380M202M6M114",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M17",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 115,
    "DeviceFullCode": "380M202M6M115",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M17",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 116,
    "DeviceFullCode": "380M202M6M116",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M17",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 117,
    "DeviceFullCode": "380M202M6M117",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M17",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 118,
    "DeviceFullCode": "380M202M6M118",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M17",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 119,
    "DeviceFullCode": "380M202M6M119",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M17",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 120,
    "DeviceFullCode": "380M202M6M120",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M18",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 121,
    "DeviceFullCode": "380M202M6M121",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M18",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 122,
    "DeviceFullCode": "380M202M6M122",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M18",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 123,
    "DeviceFullCode": "380M202M6M123",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M18",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 124,
    "DeviceFullCode": "380M202M6M124",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M18",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 125,
    "DeviceFullCode": "380M202M6M125",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M18",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 126,
    "DeviceFullCode": "380M202M6M126",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M18",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 127,
    "DeviceFullCode": "380M202M6M127",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M19",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 128,
    "DeviceFullCode": "380M202M6M128",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M19",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 129,
    "DeviceFullCode": "380M202M6M129",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M19",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 130,
    "DeviceFullCode": "380M202M6M130",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M19",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 131,
    "DeviceFullCode": "380M202M6M131",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M19",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 132,
    "DeviceFullCode": "380M202M6M132",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M19",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 133,
    "DeviceFullCode": "380M202M6M133",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M19",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 134,
    "DeviceFullCode": "380M202M6M134",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M20",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 135,
    "DeviceFullCode": "380M202M6M135",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M20",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 136,
    "DeviceFullCode": "380M202M6M136",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M20",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 137,
    "DeviceFullCode": "380M202M6M137",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M20",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 138,
    "DeviceFullCode": "380M202M6M138",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M20",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 139,
    "DeviceFullCode": "380M202M6M139",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M20",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 140,
    "DeviceFullCode": "380M202M6M140",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M20",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 141,
    "DeviceFullCode": "380M202M6M141",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M21",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 142,
    "DeviceFullCode": "380M202M6M142",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M21",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 143,
    "DeviceFullCode": "380M202M6M143",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M21",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 144,
    "DeviceFullCode": "380M202M6M144",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M21",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 145,
    "DeviceFullCode": "380M202M6M145",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M21",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 146,
    "DeviceFullCode": "380M202M6M146",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M21",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 147,
    "DeviceFullCode": "380M202M6M147",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M21",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 148,
    "DeviceFullCode": "380M202M6M148",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M22",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 149,
    "DeviceFullCode": "380M202M6M149",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M22",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 150,
    "DeviceFullCode": "380M202M6M150",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M22",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 151,
    "DeviceFullCode": "380M202M6M151",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M22",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 152,
    "DeviceFullCode": "380M202M6M152",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M22",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 153,
    "DeviceFullCode": "380M202M6M153",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M22",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 154,
    "DeviceFullCode": "380M202M6M154",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M22",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 155,
    "DeviceFullCode": "380M202M6M155",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M23",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 156,
    "DeviceFullCode": "380M202M6M156",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M23",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 157,
    "DeviceFullCode": "380M202M6M157",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M23",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 158,
    "DeviceFullCode": "380M202M6M158",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M23",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 159,
    "DeviceFullCode": "380M202M6M159",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M23",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 160,
    "DeviceFullCode": "380M202M6M160",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M23",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 161,
    "DeviceFullCode": "380M202M6M161",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M23",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 162,
    "DeviceFullCode": "380M202M6M162",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M24",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 163,
    "DeviceFullCode": "380M202M6M163",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M24",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 164,
    "DeviceFullCode": "380M202M6M164",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M24",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 165,
    "DeviceFullCode": "380M202M6M165",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M24",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 166,
    "DeviceFullCode": "380M202M6M166",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M24",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 167,
    "DeviceFullCode": "380M202M6M167",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M24",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 168,
    "DeviceFullCode": "380M202M6M168",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M24",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 169,
    "DeviceFullCode": "380M202M6M169",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M25",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 170,
    "DeviceFullCode": "380M202M6M170",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M25",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 171,
    "DeviceFullCode": "380M202M6M171",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M25",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 172,
    "DeviceFullCode": "380M202M6M172",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M25",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 173,
    "DeviceFullCode": "380M202M6M173",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M25",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 174,
    "DeviceFullCode": "380M202M6M174",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M25",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 175,
    "DeviceFullCode": "380M202M6M175",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M25",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 176,
    "DeviceFullCode": "380M202M6M176",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M26",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 177,
    "DeviceFullCode": "380M202M6M177",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M26",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 178,
    "DeviceFullCode": "380M202M6M178",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M26",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 179,
    "DeviceFullCode": "380M202M6M179",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M26",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 180,
    "DeviceFullCode": "380M202M6M180",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M26",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 181,
    "DeviceFullCode": "380M202M6M181",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M26",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 182,
    "DeviceFullCode": "380M202M6M182",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M26",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 183,
    "DeviceFullCode": "380M202M6M183",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M27",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 184,
    "DeviceFullCode": "380M202M6M184",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M27",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 185,
    "DeviceFullCode": "380M202M6M185",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M27",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 186,
    "DeviceFullCode": "380M202M6M186",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M27",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 187,
    "DeviceFullCode": "380M202M6M187",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M27",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 188,
    "DeviceFullCode": "380M202M6M188",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M27",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 189,
    "DeviceFullCode": "380M202M6M189",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M27",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 190,
    "DeviceFullCode": "380M202M6M190",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M28",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 191,
    "DeviceFullCode": "380M202M6M191",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M28",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 192,
    "DeviceFullCode": "380M202M6M192",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M28",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 193,
    "DeviceFullCode": "380M202M6M193",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M28",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 194,
    "DeviceFullCode": "380M202M6M194",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M28",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 195,
    "DeviceFullCode": "380M202M6M195",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M28",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 196,
    "DeviceFullCode": "380M202M6M196",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M28",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 197,
    "DeviceFullCode": "380M202M6M197",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M29",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 198,
    "DeviceFullCode": "380M202M6M198",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M29",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 199,
    "DeviceFullCode": "380M202M6M199",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M29",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 200,
    "DeviceFullCode": "380M202M6M200",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M29",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 201,
    "DeviceFullCode": "380M202M6M201",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M29",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 202,
    "DeviceFullCode": "380M202M6M202",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M29",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 203,
    "DeviceFullCode": "380M202M6M203",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M29",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 204,
    "DeviceFullCode": "380M202M6M204",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M30",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 205,
    "DeviceFullCode": "380M202M6M205",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M30",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 206,
    "DeviceFullCode": "380M202M6M206",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M30",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 207,
    "DeviceFullCode": "380M202M6M207",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M30",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 208,
    "DeviceFullCode": "380M202M6M208",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M30",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 209,
    "DeviceFullCode": "380M202M6M209",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M30",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 210,
    "DeviceFullCode": "380M202M6M210",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M30",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 211,
    "DeviceFullCode": "380M202M6M211",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M31",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 212,
    "DeviceFullCode": "380M202M6M212",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M31",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 213,
    "DeviceFullCode": "380M202M6M213",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M31",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 214,
    "DeviceFullCode": "380M202M6M214",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M31",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 215,
    "DeviceFullCode": "380M202M6M215",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M31",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 216,
    "DeviceFullCode": "380M202M6M216",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M31",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 217,
    "DeviceFullCode": "380M202M6M217",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M31",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 218,
    "DeviceFullCode": "380M202M6M218",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M32",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 219,
    "DeviceFullCode": "380M202M6M219",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M32",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 220,
    "DeviceFullCode": "380M202M6M220",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M32",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 221,
    "DeviceFullCode": "380M202M6M221",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M32",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 222,
    "DeviceFullCode": "380M202M6M222",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M32",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 223,
    "DeviceFullCode": "380M202M6M223",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M32",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 224,
    "DeviceFullCode": "380M202M6M224",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M32",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 225,
    "DeviceFullCode": "380M202M6M225",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M33",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 226,
    "DeviceFullCode": "380M202M6M226",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M33",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 227,
    "DeviceFullCode": "380M202M6M227",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M33",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 228,
    "DeviceFullCode": "380M202M6M228",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M33",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 229,
    "DeviceFullCode": "380M202M6M229",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M33",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 230,
    "DeviceFullCode": "380M202M6M230",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M33",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 231,
    "DeviceFullCode": "380M202M6M231",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M33",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 232,
    "DeviceFullCode": "380M202M6M232",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M34",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 233,
    "DeviceFullCode": "380M202M6M233",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M34",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 234,
    "DeviceFullCode": "380M202M6M234",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M34",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 235,
    "DeviceFullCode": "380M202M6M235",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M34",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 236,
    "DeviceFullCode": "380M202M6M236",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M34",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 237,
    "DeviceFullCode": "380M202M6M237",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M34",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 238,
    "DeviceFullCode": "380M202M6M238",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M34",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 239,
    "DeviceFullCode": "380M202M6M239",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M35",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 240,
    "DeviceFullCode": "380M202M6M240",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M35",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 241,
    "DeviceFullCode": "380M202M6M241",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M35",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 242,
    "DeviceFullCode": "380M202M6M242",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M35",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 243,
    "DeviceFullCode": "380M202M6M243",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M35",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 244,
    "DeviceFullCode": "380M202M6M244",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M35",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 245,
    "DeviceFullCode": "380M202M6M245",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M35",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 246,
    "DeviceFullCode": "380M202M6M246",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M36",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 247,
    "DeviceFullCode": "380M202M6M247",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M36",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 248,
    "DeviceFullCode": "380M202M6M248",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M36",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 249,
    "DeviceFullCode": "380M202M6M249",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M36",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 250,
    "DeviceFullCode": "380M202M6M250",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M36",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 251,
    "DeviceFullCode": "380M202M6M251",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M36",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 252,
    "DeviceFullCode": "380M202M6M252",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M36",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 253,
    "DeviceFullCode": "380M202M6M253",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M37",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 254,
    "DeviceFullCode": "380M202M6M254",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M37",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 255,
    "DeviceFullCode": "380M202M6M255",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M37",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 256,
    "DeviceFullCode": "380M202M6M256",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M37",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 257,
    "DeviceFullCode": "380M202M6M257",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M37",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 258,
    "DeviceFullCode": "380M202M6M258",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M37",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 259,
    "DeviceFullCode": "380M202M6M259",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M37",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 260,
    "DeviceFullCode": "380M202M6M260",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M38",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 261,
    "DeviceFullCode": "380M202M6M261",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M38",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 262,
    "DeviceFullCode": "380M202M6M262",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M38",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 263,
    "DeviceFullCode": "380M202M6M263",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M38",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 264,
    "DeviceFullCode": "380M202M6M264",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M38",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 265,
    "DeviceFullCode": "380M202M6M265",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M38",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 266,
    "DeviceFullCode": "380M202M6M266",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M38",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 267,
    "DeviceFullCode": "380M202M6M267",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M39",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 268,
    "DeviceFullCode": "380M202M6M268",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M39",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 269,
    "DeviceFullCode": "380M202M6M269",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M39",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 270,
    "DeviceFullCode": "380M202M6M270",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M39",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 271,
    "DeviceFullCode": "380M202M6M271",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M39",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 272,
    "DeviceFullCode": "380M202M6M272",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M39",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 273,
    "DeviceFullCode": "380M202M6M273",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M39",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 274,
    "DeviceFullCode": "380M202M6M274",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M40",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 275,
    "DeviceFullCode": "380M202M6M275",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M40",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 276,
    "DeviceFullCode": "380M202M6M276",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M40",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 277,
    "DeviceFullCode": "380M202M6M277",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M40",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 278,
    "DeviceFullCode": "380M202M6M278",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M40",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 279,
    "DeviceFullCode": "380M202M6M279",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M40",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 280,
    "DeviceFullCode": "380M202M6M280",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M40",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 281,
    "DeviceFullCode": "380M202M6M281",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M41",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 282,
    "DeviceFullCode": "380M202M6M282",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M41",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 283,
    "DeviceFullCode": "380M202M6M283",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M41",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 284,
    "DeviceFullCode": "380M202M6M284",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M41",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 285,
    "DeviceFullCode": "380M202M6M285",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M41",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 286,
    "DeviceFullCode": "380M202M6M286",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M41",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 287,
    "DeviceFullCode": "380M202M6M287",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M41",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 288,
    "DeviceFullCode": "380M202M6M288",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M42",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 289,
    "DeviceFullCode": "380M202M6M289",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M42",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 290,
    "DeviceFullCode": "380M202M6M290",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M42",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 291,
    "DeviceFullCode": "380M202M6M291",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M42",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 292,
    "DeviceFullCode": "380M202M6M292",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M42",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 293,
    "DeviceFullCode": "380M202M6M293",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M42",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 294,
    "DeviceFullCode": "380M202M6M294",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M42",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 295,
    "DeviceFullCode": "380M202M6M295",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M43",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 296,
    "DeviceFullCode": "380M202M6M296",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M43",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 297,
    "DeviceFullCode": "380M202M6M297",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M43",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 298,
    "DeviceFullCode": "380M202M6M298",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M43",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 299,
    "DeviceFullCode": "380M202M6M299",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M43",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 300,
    "DeviceFullCode": "380M202M6M300",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M43",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 301,
    "DeviceFullCode": "380M202M6M301",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M43",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 302,
    "DeviceFullCode": "380M202M6M302",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M44",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 303,
    "DeviceFullCode": "380M202M6M303",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M44",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 304,
    "DeviceFullCode": "380M202M6M304",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M44",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 305,
    "DeviceFullCode": "380M202M6M305",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M44",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 306,
    "DeviceFullCode": "380M202M6M306",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M44",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 307,
    "DeviceFullCode": "380M202M6M307",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M44",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 308,
    "DeviceFullCode": "380M202M6M308",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M44",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 309,
    "DeviceFullCode": "380M202M6M309",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M45",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 310,
    "DeviceFullCode": "380M202M6M310",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M45",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 311,
    "DeviceFullCode": "380M202M6M311",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M45",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 312,
    "DeviceFullCode": "380M202M6M312",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M45",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 313,
    "DeviceFullCode": "380M202M6M313",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M45",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 314,
    "DeviceFullCode": "380M202M6M314",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M45",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 315,
    "DeviceFullCode": "380M202M6M315",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M45",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 316,
    "DeviceFullCode": "380M202M6M316",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M46",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 317,
    "DeviceFullCode": "380M202M6M317",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M46",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 318,
    "DeviceFullCode": "380M202M6M318",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M46",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 319,
    "DeviceFullCode": "380M202M6M319",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M46",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 320,
    "DeviceFullCode": "380M202M6M320",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M46",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 321,
    "DeviceFullCode": "380M202M6M321",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M46",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 322,
    "DeviceFullCode": "380M202M6M322",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M46",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 323,
    "DeviceFullCode": "380M202M6M323",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M47",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 324,
    "DeviceFullCode": "380M202M6M324",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M47",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 325,
    "DeviceFullCode": "380M202M6M325",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M47",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 326,
    "DeviceFullCode": "380M202M6M326",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M47",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 327,
    "DeviceFullCode": "380M202M6M327",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M47",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 328,
    "DeviceFullCode": "380M202M6M328",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M47",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 329,
    "DeviceFullCode": "380M202M6M329",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M47",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 330,
    "DeviceFullCode": "380M202M6M330",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M48",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 331,
    "DeviceFullCode": "380M202M6M331",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M48",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 332,
    "DeviceFullCode": "380M202M6M332",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M48",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 333,
    "DeviceFullCode": "380M202M6M333",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M48",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 334,
    "DeviceFullCode": "380M202M6M334",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M48",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 335,
    "DeviceFullCode": "380M202M6M335",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M48",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 336,
    "DeviceFullCode": "380M202M6M336",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M48",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 337,
    "DeviceFullCode": "380M202M6M337",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M49",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 338,
    "DeviceFullCode": "380M202M6M338",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M49",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 339,
    "DeviceFullCode": "380M202M6M339",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M49",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 340,
    "DeviceFullCode": "380M202M6M340",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M49",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 341,
    "DeviceFullCode": "380M202M6M341",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M49",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 342,
    "DeviceFullCode": "380M202M6M342",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M49",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 343,
    "DeviceFullCode": "380M202M6M343",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M49",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 344,
    "DeviceFullCode": "380M202M6M344",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M50",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 345,
    "DeviceFullCode": "380M202M6M345",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M50",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 346,
    "DeviceFullCode": "380M202M6M346",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M50",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 347,
    "DeviceFullCode": "380M202M6M347",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M50",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 348,
    "DeviceFullCode": "380M202M6M348",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M50",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 349,
    "DeviceFullCode": "380M202M6M349",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M50",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 350,
    "DeviceFullCode": "380M202M6M350",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M50",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 351,
    "DeviceFullCode": "380M202M6M351",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M51",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 352,
    "DeviceFullCode": "380M202M6M352",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M51",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 353,
    "DeviceFullCode": "380M202M6M353",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M51",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 354,
    "DeviceFullCode": "380M202M6M354",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M51",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 355,
    "DeviceFullCode": "380M202M6M355",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M51",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 356,
    "DeviceFullCode": "380M202M6M356",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M51",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 357,
    "DeviceFullCode": "380M202M6M357",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M51",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 358,
    "DeviceFullCode": "380M202M6M358",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M52",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 359,
    "DeviceFullCode": "380M202M6M359",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M52",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 360,
    "DeviceFullCode": "380M202M6M360",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M52",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 361,
    "DeviceFullCode": "380M202M6M361",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M52",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 362,
    "DeviceFullCode": "380M202M6M362",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M52",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 363,
    "DeviceFullCode": "380M202M6M363",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M52",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 364,
    "DeviceFullCode": "380M202M6M364",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M52",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 365,
    "DeviceFullCode": "380M202M6M365",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M53",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 366,
    "DeviceFullCode": "380M202M6M366",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M53",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 367,
    "DeviceFullCode": "380M202M6M367",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M53",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 368,
    "DeviceFullCode": "380M202M6M368",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M53",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 369,
    "DeviceFullCode": "380M202M6M369",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M53",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 370,
    "DeviceFullCode": "380M202M6M370",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M53",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 371,
    "DeviceFullCode": "380M202M6M371",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M53",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 372,
    "DeviceFullCode": "380M202M6M372",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M54",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 373,
    "DeviceFullCode": "380M202M6M373",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M54",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 374,
    "DeviceFullCode": "380M202M6M374",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M54",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 375,
    "DeviceFullCode": "380M202M6M375",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M54",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 376,
    "DeviceFullCode": "380M202M6M376",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M54",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 377,
    "DeviceFullCode": "380M202M6M377",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M54",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 378,
    "DeviceFullCode": "380M202M6M378",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M54",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 379,
    "DeviceFullCode": "380M202M6M379",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M55",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 380,
    "DeviceFullCode": "380M202M6M380",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M55",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 381,
    "DeviceFullCode": "380M202M6M381",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M55",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 382,
    "DeviceFullCode": "380M202M6M382",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M55",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 383,
    "DeviceFullCode": "380M202M6M383",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M55",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 384,
    "DeviceFullCode": "380M202M6M384",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M55",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 385,
    "DeviceFullCode": "380M202M6M385",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M55",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 386,
    "DeviceFullCode": "380M202M6M386",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M56",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 387,
    "DeviceFullCode": "380M202M6M387",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M56",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 388,
    "DeviceFullCode": "380M202M6M388",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M56",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 389,
    "DeviceFullCode": "380M202M6M389",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M56",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 390,
    "DeviceFullCode": "380M202M6M390",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M56",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 391,
    "DeviceFullCode": "380M202M6M391",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M56",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 392,
    "DeviceFullCode": "380M202M6M392",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M56",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 393,
    "DeviceFullCode": "380M202M6M393",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M57",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 394,
    "DeviceFullCode": "380M202M6M394",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M57",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 395,
    "DeviceFullCode": "380M202M6M395",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M57",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 396,
    "DeviceFullCode": "380M202M6M396",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M57",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 397,
    "DeviceFullCode": "380M202M6M397",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M57",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 398,
    "DeviceFullCode": "380M202M6M398",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M57",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 399,
    "DeviceFullCode": "380M202M6M399",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M57",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 400,
    "DeviceFullCode": "380M202M6M400",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M58",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 401,
    "DeviceFullCode": "380M202M6M401",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M58",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 402,
    "DeviceFullCode": "380M202M6M402",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M58",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 403,
    "DeviceFullCode": "380M202M6M403",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M58",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 404,
    "DeviceFullCode": "380M202M6M404",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M58",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 405,
    "DeviceFullCode": "380M202M6M405",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M58",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 406,
    "DeviceFullCode": "380M202M6M406",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M58",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 407,
    "DeviceFullCode": "380M202M6M407",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M59",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 408,
    "DeviceFullCode": "380M202M6M408",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M59",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 409,
    "DeviceFullCode": "380M202M6M409",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M59",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 410,
    "DeviceFullCode": "380M202M6M410",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M59",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 411,
    "DeviceFullCode": "380M202M6M411",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M59",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 412,
    "DeviceFullCode": "380M202M6M412",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M59",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 413,
    "DeviceFullCode": "380M202M6M413",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M59",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 414,
    "DeviceFullCode": "380M202M6M414",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M60",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 415,
    "DeviceFullCode": "380M202M6M415",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M60",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 416,
    "DeviceFullCode": "380M202M6M416",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M60",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 417,
    "DeviceFullCode": "380M202M6M417",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M60",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 418,
    "DeviceFullCode": "380M202M6M418",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M60",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 419,
    "DeviceFullCode": "380M202M6M419",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M60",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 420,
    "DeviceFullCode": "380M202M6M420",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M60",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 421,
    "DeviceFullCode": "380M202M6M421",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M61",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 422,
    "DeviceFullCode": "380M202M6M422",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M61",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 423,
    "DeviceFullCode": "380M202M6M423",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M61",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 424,
    "DeviceFullCode": "380M202M6M424",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M61",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 425,
    "DeviceFullCode": "380M202M6M425",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M61",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 426,
    "DeviceFullCode": "380M202M6M426",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M61",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 427,
    "DeviceFullCode": "380M202M6M427",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M61",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 428,
    "DeviceFullCode": "380M202M6M428",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M62",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 429,
    "DeviceFullCode": "380M202M6M429",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M62",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 430,
    "DeviceFullCode": "380M202M6M430",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M62",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 431,
    "DeviceFullCode": "380M202M6M431",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M62",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 432,
    "DeviceFullCode": "380M202M6M432",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M62",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 433,
    "DeviceFullCode": "380M202M6M433",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M62",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 434,
    "DeviceFullCode": "380M202M6M434",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M62",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 435,
    "DeviceFullCode": "380M202M6M435",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M63",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 436,
    "DeviceFullCode": "380M202M6M436",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M63",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 437,
    "DeviceFullCode": "380M202M6M437",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M63",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 438,
    "DeviceFullCode": "380M202M6M438",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M63",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 439,
    "DeviceFullCode": "380M202M6M439",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M63",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 440,
    "DeviceFullCode": "380M202M6M440",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M63",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 441,
    "DeviceFullCode": "380M202M6M441",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M63",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 442,
    "DeviceFullCode": "380M202M6M442",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M64",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 443,
    "DeviceFullCode": "380M202M6M443",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M64",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 444,
    "DeviceFullCode": "380M202M6M444",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M64",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 445,
    "DeviceFullCode": "380M202M6M445",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M64",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 446,
    "DeviceFullCode": "380M202M6M446",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M64",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 447,
    "DeviceFullCode": "380M202M6M447",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M64",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 448,
    "DeviceFullCode": "380M202M6M448",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M64",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 449,
    "DeviceFullCode": "380M202M6M449",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M65",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 450,
    "DeviceFullCode": "380M202M6M450",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M65",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 451,
    "DeviceFullCode": "380M202M6M451",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M65",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 452,
    "DeviceFullCode": "380M202M6M452",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M65",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 453,
    "DeviceFullCode": "380M202M6M453",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M65",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 454,
    "DeviceFullCode": "380M202M6M454",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M65",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 455,
    "DeviceFullCode": "380M202M6M455",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M65",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 456,
    "DeviceFullCode": "380M202M6M456",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M66",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 457,
    "DeviceFullCode": "380M202M6M457",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M66",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 458,
    "DeviceFullCode": "380M202M6M458",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M66",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 459,
    "DeviceFullCode": "380M202M6M459",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M66",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 460,
    "DeviceFullCode": "380M202M6M460",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M66",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 461,
    "DeviceFullCode": "380M202M6M461",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M66",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 462,
    "DeviceFullCode": "380M202M6M462",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M66",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 463,
    "DeviceFullCode": "380M202M6M463",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M67",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 464,
    "DeviceFullCode": "380M202M6M464",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M67",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 465,
    "DeviceFullCode": "380M202M6M465",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M67",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 466,
    "DeviceFullCode": "380M202M6M466",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M67",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 467,
    "DeviceFullCode": "380M202M6M467",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M67",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 468,
    "DeviceFullCode": "380M202M6M468",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M67",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 469,
    "DeviceFullCode": "380M202M6M469",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M67",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 470,
    "DeviceFullCode": "380M202M6M470",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M68",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 471,
    "DeviceFullCode": "380M202M6M471",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M68",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 472,
    "DeviceFullCode": "380M202M6M472",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M68",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 473,
    "DeviceFullCode": "380M202M6M473",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M68",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 474,
    "DeviceFullCode": "380M202M6M474",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M68",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 475,
    "DeviceFullCode": "380M202M6M475",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M68",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 476,
    "DeviceFullCode": "380M202M6M476",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M68",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 477,
    "DeviceFullCode": "380M202M6M477",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M69",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 478,
    "DeviceFullCode": "380M202M6M478",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M69",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 479,
    "DeviceFullCode": "380M202M6M479",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M69",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 480,
    "DeviceFullCode": "380M202M6M480",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M69",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 481,
    "DeviceFullCode": "380M202M6M481",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M69",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 482,
    "DeviceFullCode": "380M202M6M482",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M69",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 483,
    "DeviceFullCode": "380M202M6M483",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M69",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 484,
    "DeviceFullCode": "380M202M6M484",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M70",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 485,
    "DeviceFullCode": "380M202M6M485",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M70",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 486,
    "DeviceFullCode": "380M202M6M486",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M70",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 487,
    "DeviceFullCode": "380M202M6M487",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M70",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 488,
    "DeviceFullCode": "380M202M6M488",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M70",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 489,
    "DeviceFullCode": "380M202M6M489",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M70",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 490,
    "DeviceFullCode": "380M202M6M490",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M70",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 491,
    "DeviceFullCode": "380M202M6M491",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M71",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 492,
    "DeviceFullCode": "380M202M6M492",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M71",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 493,
    "DeviceFullCode": "380M202M6M493",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M71",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 494,
    "DeviceFullCode": "380M202M6M494",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M71",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 495,
    "DeviceFullCode": "380M202M6M495",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M71",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 496,
    "DeviceFullCode": "380M202M6M496",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M71",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 497,
    "DeviceFullCode": "380M202M6M497",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M71",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 498,
    "DeviceFullCode": "380M202M6M498",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M72",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 499,
    "DeviceFullCode": "380M202M6M499",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M72",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 500,
    "DeviceFullCode": "380M202M6M500",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M72",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 501,
    "DeviceFullCode": "380M202M6M501",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M72",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 502,
    "DeviceFullCode": "380M202M6M502",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M72",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 503,
    "DeviceFullCode": "380M202M6M503",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M72",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 504,
    "DeviceFullCode": "380M202M6M504",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M72",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 505,
    "DeviceFullCode": "380M202M6M505",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M73",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 506,
    "DeviceFullCode": "380M202M6M506",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M73",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 507,
    "DeviceFullCode": "380M202M6M507",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M73",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 508,
    "DeviceFullCode": "380M202M6M508",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M73",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 509,
    "DeviceFullCode": "380M202M6M509",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M73",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 510,
    "DeviceFullCode": "380M202M6M510",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M73",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 511,
    "DeviceFullCode": "380M202M6M511",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M73",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 512,
    "DeviceFullCode": "380M202M6M512",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M74",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 513,
    "DeviceFullCode": "380M202M6M513",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M74",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 514,
    "DeviceFullCode": "380M202M6M514",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M74",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 515,
    "DeviceFullCode": "380M202M6M515",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M74",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 516,
    "DeviceFullCode": "380M202M6M516",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M74",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 517,
    "DeviceFullCode": "380M202M6M517",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M74",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 518,
    "DeviceFullCode": "380M202M6M518",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M74",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 519,
    "DeviceFullCode": "380M202M6M519",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M75",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 520,
    "DeviceFullCode": "380M202M6M520",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M75",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 521,
    "DeviceFullCode": "380M202M6M521",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M75",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 522,
    "DeviceFullCode": "380M202M6M522",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M75",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 523,
    "DeviceFullCode": "380M202M6M523",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M75",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 524,
    "DeviceFullCode": "380M202M6M524",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M75",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 525,
    "DeviceFullCode": "380M202M6M525",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M75",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 526,
    "DeviceFullCode": "380M202M6M526",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M76",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 527,
    "DeviceFullCode": "380M202M6M527",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M76",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 528,
    "DeviceFullCode": "380M202M6M528",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M76",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 529,
    "DeviceFullCode": "380M202M6M529",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M76",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 530,
    "DeviceFullCode": "380M202M6M530",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M76",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 531,
    "DeviceFullCode": "380M202M6M531",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M76",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 532,
    "DeviceFullCode": "380M202M6M532",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M76",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 533,
    "DeviceFullCode": "380M202M6M533",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M77",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 534,
    "DeviceFullCode": "380M202M6M534",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M77",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 535,
    "DeviceFullCode": "380M202M6M535",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M77",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 536,
    "DeviceFullCode": "380M202M6M536",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M77",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 537,
    "DeviceFullCode": "380M202M6M537",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M77",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 538,
    "DeviceFullCode": "380M202M6M538",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M77",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 539,
    "DeviceFullCode": "380M202M6M539",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M77",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 540,
    "DeviceFullCode": "380M202M6M540",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M78",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 541,
    "DeviceFullCode": "380M202M6M541",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M78",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 542,
    "DeviceFullCode": "380M202M6M542",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M78",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 543,
    "DeviceFullCode": "380M202M6M543",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M78",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 544,
    "DeviceFullCode": "380M202M6M544",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M78",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 545,
    "DeviceFullCode": "380M202M6M545",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M78",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 546,
    "DeviceFullCode": "380M202M6M546",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M78",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 547,
    "DeviceFullCode": "380M202M6M547",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M79",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 548,
    "DeviceFullCode": "380M202M6M548",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M79",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 549,
    "DeviceFullCode": "380M202M6M549",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M79",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 550,
    "DeviceFullCode": "380M202M6M550",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M79",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 551,
    "DeviceFullCode": "380M202M6M551",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M79",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 552,
    "DeviceFullCode": "380M202M6M552",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M79",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 553,
    "DeviceFullCode": "380M202M6M553",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M79",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 554,
    "DeviceFullCode": "380M202M6M554",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M80",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 555,
    "DeviceFullCode": "380M202M6M555",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M80",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 556,
    "DeviceFullCode": "380M202M6M556",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M80",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 557,
    "DeviceFullCode": "380M202M6M557",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M80",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 558,
    "DeviceFullCode": "380M202M6M558",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M80",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 559,
    "DeviceFullCode": "380M202M6M559",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M80",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 560,
    "DeviceFullCode": "380M202M6M560",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M80",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 561,
    "DeviceFullCode": "380M202M6M561",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M81",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 562,
    "DeviceFullCode": "380M202M6M562",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M81",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 563,
    "DeviceFullCode": "380M202M6M563",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M81",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 564,
    "DeviceFullCode": "380M202M6M564",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M81",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 565,
    "DeviceFullCode": "380M202M6M565",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M81",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 566,
    "DeviceFullCode": "380M202M6M566",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M81",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 567,
    "DeviceFullCode": "380M202M6M567",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M81",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 568,
    "DeviceFullCode": "380M202M6M568",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M82",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 569,
    "DeviceFullCode": "380M202M6M569",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M82",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 570,
    "DeviceFullCode": "380M202M6M570",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M82",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 571,
    "DeviceFullCode": "380M202M6M571",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M82",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 572,
    "DeviceFullCode": "380M202M6M572",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M82",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 573,
    "DeviceFullCode": "380M202M6M573",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M82",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 574,
    "DeviceFullCode": "380M202M6M574",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M82",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 575,
    "DeviceFullCode": "380M202M6M575",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M83",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 576,
    "DeviceFullCode": "380M202M6M576",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M83",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 577,
    "DeviceFullCode": "380M202M6M577",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M83",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 578,
    "DeviceFullCode": "380M202M6M578",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M83",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 579,
    "DeviceFullCode": "380M202M6M579",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M83",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 580,
    "DeviceFullCode": "380M202M6M580",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M83",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 581,
    "DeviceFullCode": "380M202M6M581",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M83",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 582,
    "DeviceFullCode": "380M202M6M582",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M84",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 583,
    "DeviceFullCode": "380M202M6M583",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M84",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 584,
    "DeviceFullCode": "380M202M6M584",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M84",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 585,
    "DeviceFullCode": "380M202M6M585",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M84",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 586,
    "DeviceFullCode": "380M202M6M586",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M84",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 587,
    "DeviceFullCode": "380M202M6M587",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M84",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 588,
    "DeviceFullCode": "380M202M6M588",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M84",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 589,
    "DeviceFullCode": "380M202M6M589",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M85",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 590,
    "DeviceFullCode": "380M202M6M590",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M85",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 591,
    "DeviceFullCode": "380M202M6M591",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M85",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 592,
    "DeviceFullCode": "380M202M6M592",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M85",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 593,
    "DeviceFullCode": "380M202M6M593",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M85",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 594,
    "DeviceFullCode": "380M202M6M594",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M85",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 595,
    "DeviceFullCode": "380M202M6M595",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M85",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 596,
    "DeviceFullCode": "380M202M6M596",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M86",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 597,
    "DeviceFullCode": "380M202M6M597",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M86",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 598,
    "DeviceFullCode": "380M202M6M598",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M86",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 599,
    "DeviceFullCode": "380M202M6M599",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M86",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 600,
    "DeviceFullCode": "380M202M6M600",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M86",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 601,
    "DeviceFullCode": "380M202M6M601",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M86",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 602,
    "DeviceFullCode": "380M202M6M602",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M86",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 603,
    "DeviceFullCode": "380M202M6M603",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M87",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 604,
    "DeviceFullCode": "380M202M6M604",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M87",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 605,
    "DeviceFullCode": "380M202M6M605",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M87",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 606,
    "DeviceFullCode": "380M202M6M606",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M87",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 607,
    "DeviceFullCode": "380M202M6M607",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M87",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 608,
    "DeviceFullCode": "380M202M6M608",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M87",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 609,
    "DeviceFullCode": "380M202M6M609",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M87",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 610,
    "DeviceFullCode": "380M202M6M610",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M88",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 611,
    "DeviceFullCode": "380M202M6M611",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M88",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 612,
    "DeviceFullCode": "380M202M6M612",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M88",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 613,
    "DeviceFullCode": "380M202M6M613",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M88",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 614,
    "DeviceFullCode": "380M202M6M614",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M88",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 615,
    "DeviceFullCode": "380M202M6M615",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M88",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 616,
    "DeviceFullCode": "380M202M6M616",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M88",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 617,
    "DeviceFullCode": "380M202M6M617",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M89",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 618,
    "DeviceFullCode": "380M202M6M618",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M89",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 619,
    "DeviceFullCode": "380M202M6M619",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M89",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 620,
    "DeviceFullCode": "380M202M6M620",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M89",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 621,
    "DeviceFullCode": "380M202M6M621",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M89",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 622,
    "DeviceFullCode": "380M202M6M622",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M89",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 623,
    "DeviceFullCode": "380M202M6M623",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M89",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 624,
    "DeviceFullCode": "380M202M6M624",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M90",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 625,
    "DeviceFullCode": "380M202M6M625",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M90",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 626,
    "DeviceFullCode": "380M202M6M626",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M90",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 627,
    "DeviceFullCode": "380M202M6M627",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M90",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 628,
    "DeviceFullCode": "380M202M6M628",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M90",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 629,
    "DeviceFullCode": "380M202M6M629",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M90",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 630,
    "DeviceFullCode": "380M202M6M630",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M90",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 631,
    "DeviceFullCode": "380M202M6M631",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M91",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 632,
    "DeviceFullCode": "380M202M6M632",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M91",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 633,
    "DeviceFullCode": "380M202M6M633",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M91",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 634,
    "DeviceFullCode": "380M202M6M634",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M91",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 635,
    "DeviceFullCode": "380M202M6M635",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M91",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 636,
    "DeviceFullCode": "380M202M6M636",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M91",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 637,
    "DeviceFullCode": "380M202M6M637",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M91",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 638,
    "DeviceFullCode": "380M202M6M638",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M92",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 639,
    "DeviceFullCode": "380M202M6M639",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M92",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 640,
    "DeviceFullCode": "380M202M6M640",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M92",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 641,
    "DeviceFullCode": "380M202M6M641",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M92",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 642,
    "DeviceFullCode": "380M202M6M642",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M92",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 643,
    "DeviceFullCode": "380M202M6M643",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M92",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 6,
    "DeviceCode": 644,
    "DeviceFullCode": "380M202M6M644",
    "DeviceModeFullCode": "380M202M6",
    "PDeviceFullCode": "380M201M2M92",
    "Capacity": None
  },
  {
    "DeviceTypeCode": 203,
    "DeviceModeCode": 12,
    "DeviceCode": 1,
    "DeviceFullCode": "380M203M12M1",
    "DeviceModeFullCode": "380M203M12",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 203,
    "DeviceModeCode": 8,
    "DeviceCode": 2,
    "DeviceFullCode": "380M203M8M2",
    "DeviceModeFullCode": "380M203M8",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 1,
    "DeviceFullCode": "380M206M3M1",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 2,
    "DeviceFullCode": "380M206M3M2",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 3,
    "DeviceFullCode": "380M206M3M3",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 4,
    "DeviceFullCode": "380M206M3M4",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 5,
    "DeviceFullCode": "380M206M3M5",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 6,
    "DeviceFullCode": "380M206M3M6",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 7,
    "DeviceFullCode": "380M206M3M7",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 8,
    "DeviceFullCode": "380M206M3M8",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 9,
    "DeviceFullCode": "380M206M3M9",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 10,
    "DeviceFullCode": "380M206M3M10",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 11,
    "DeviceFullCode": "380M206M3M11",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 12,
    "DeviceFullCode": "380M206M3M12",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 13,
    "DeviceFullCode": "380M206M3M13",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 14,
    "DeviceFullCode": "380M206M3M14",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 15,
    "DeviceFullCode": "380M206M3M15",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 16,
    "DeviceFullCode": "380M206M3M16",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 17,
    "DeviceFullCode": "380M206M3M17",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 18,
    "DeviceFullCode": "380M206M3M18",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 19,
    "DeviceFullCode": "380M206M3M19",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 20,
    "DeviceFullCode": "380M206M3M20",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 21,
    "DeviceFullCode": "380M206M3M21",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 22,
    "DeviceFullCode": "380M206M3M22",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 23,
    "DeviceFullCode": "380M206M3M23",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 24,
    "DeviceFullCode": "380M206M3M24",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 25,
    "DeviceFullCode": "380M206M3M25",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 26,
    "DeviceFullCode": "380M206M3M26",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 27,
    "DeviceFullCode": "380M206M3M27",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 28,
    "DeviceFullCode": "380M206M3M28",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 29,
    "DeviceFullCode": "380M206M3M29",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 30,
    "DeviceFullCode": "380M206M3M30",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 31,
    "DeviceFullCode": "380M206M3M31",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 32,
    "DeviceFullCode": "380M206M3M32",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 33,
    "DeviceFullCode": "380M206M3M33",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 34,
    "DeviceFullCode": "380M206M3M34",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 35,
    "DeviceFullCode": "380M206M3M35",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 36,
    "DeviceFullCode": "380M206M3M36",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 37,
    "DeviceFullCode": "380M206M3M37",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 38,
    "DeviceFullCode": "380M206M3M38",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 39,
    "DeviceFullCode": "380M206M3M39",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 40,
    "DeviceFullCode": "380M206M3M40",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 41,
    "DeviceFullCode": "380M206M3M41",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 42,
    "DeviceFullCode": "380M206M3M42",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 43,
    "DeviceFullCode": "380M206M3M43",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 44,
    "DeviceFullCode": "380M206M3M44",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 45,
    "DeviceFullCode": "380M206M3M45",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 46,
    "DeviceFullCode": "380M206M3M46",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 47,
    "DeviceFullCode": "380M206M3M47",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 48,
    "DeviceFullCode": "380M206M3M48",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 49,
    "DeviceFullCode": "380M206M3M49",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 50,
    "DeviceFullCode": "380M206M3M50",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 51,
    "DeviceFullCode": "380M206M3M51",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 52,
    "DeviceFullCode": "380M206M3M52",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 53,
    "DeviceFullCode": "380M206M3M53",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 54,
    "DeviceFullCode": "380M206M3M54",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 55,
    "DeviceFullCode": "380M206M3M55",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 56,
    "DeviceFullCode": "380M206M3M56",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 57,
    "DeviceFullCode": "380M206M3M57",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 58,
    "DeviceFullCode": "380M206M3M58",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 59,
    "DeviceFullCode": "380M206M3M59",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 60,
    "DeviceFullCode": "380M206M3M60",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 61,
    "DeviceFullCode": "380M206M3M61",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 62,
    "DeviceFullCode": "380M206M3M62",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 63,
    "DeviceFullCode": "380M206M3M63",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 64,
    "DeviceFullCode": "380M206M3M64",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 65,
    "DeviceFullCode": "380M206M3M65",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 66,
    "DeviceFullCode": "380M206M3M66",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 67,
    "DeviceFullCode": "380M206M3M67",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 68,
    "DeviceFullCode": "380M206M3M68",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 69,
    "DeviceFullCode": "380M206M3M69",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 70,
    "DeviceFullCode": "380M206M3M70",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 71,
    "DeviceFullCode": "380M206M3M71",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 72,
    "DeviceFullCode": "380M206M3M72",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 73,
    "DeviceFullCode": "380M206M3M73",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 74,
    "DeviceFullCode": "380M206M3M74",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 75,
    "DeviceFullCode": "380M206M3M75",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 76,
    "DeviceFullCode": "380M206M3M76",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 77,
    "DeviceFullCode": "380M206M3M77",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 78,
    "DeviceFullCode": "380M206M3M78",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 79,
    "DeviceFullCode": "380M206M3M79",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 80,
    "DeviceFullCode": "380M206M3M80",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 81,
    "DeviceFullCode": "380M206M3M81",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 82,
    "DeviceFullCode": "380M206M3M82",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 83,
    "DeviceFullCode": "380M206M3M83",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 84,
    "DeviceFullCode": "380M206M3M84",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 85,
    "DeviceFullCode": "380M206M3M85",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 86,
    "DeviceFullCode": "380M206M3M86",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 87,
    "DeviceFullCode": "380M206M3M87",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 88,
    "DeviceFullCode": "380M206M3M88",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 89,
    "DeviceFullCode": "380M206M3M89",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 90,
    "DeviceFullCode": "380M206M3M90",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 91,
    "DeviceFullCode": "380M206M3M91",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 92,
    "DeviceFullCode": "380M206M3M92",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 93,
    "DeviceFullCode": "380M206M3M93",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 94,
    "DeviceFullCode": "380M206M3M94",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 95,
    "DeviceFullCode": "380M206M3M95",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 96,
    "DeviceFullCode": "380M206M3M96",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 97,
    "DeviceFullCode": "380M206M3M97",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 98,
    "DeviceFullCode": "380M206M3M98",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 99,
    "DeviceFullCode": "380M206M3M99",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 100,
    "DeviceFullCode": "380M206M3M100",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 101,
    "DeviceFullCode": "380M206M3M101",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 102,
    "DeviceFullCode": "380M206M3M102",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 103,
    "DeviceFullCode": "380M206M3M103",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 104,
    "DeviceFullCode": "380M206M3M104",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 105,
    "DeviceFullCode": "380M206M3M105",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 106,
    "DeviceFullCode": "380M206M3M106",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 107,
    "DeviceFullCode": "380M206M3M107",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 108,
    "DeviceFullCode": "380M206M3M108",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 109,
    "DeviceFullCode": "380M206M3M109",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 110,
    "DeviceFullCode": "380M206M3M110",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 111,
    "DeviceFullCode": "380M206M3M111",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 112,
    "DeviceFullCode": "380M206M3M112",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 113,
    "DeviceFullCode": "380M206M3M113",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 114,
    "DeviceFullCode": "380M206M3M114",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 115,
    "DeviceFullCode": "380M206M3M115",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 206,
    "DeviceModeCode": 3,
    "DeviceCode": 116,
    "DeviceFullCode": "380M206M3M116",
    "DeviceModeFullCode": "380M206M3",
    "PDeviceFullCode": None,
    "Capacity": 37.6000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceCode": 1,
    "DeviceFullCode": "380M302M8M1",
    "DeviceModeFullCode": "380M302M8",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceCode": 2,
    "DeviceFullCode": "380M302M8M2",
    "DeviceModeFullCode": "380M302M8",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceCode": 3,
    "DeviceFullCode": "380M302M8M3",
    "DeviceModeFullCode": "380M302M8",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceCode": 4,
    "DeviceFullCode": "380M302M8M4",
    "DeviceModeFullCode": "380M302M8",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 8,
    "DeviceCode": 5,
    "DeviceFullCode": "380M302M8M5",
    "DeviceModeFullCode": "380M302M8",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 305,
    "DeviceModeCode": 15,
    "DeviceCode": 1,
    "DeviceFullCode": "380M305M15M1",
    "DeviceModeFullCode": "380M305M15",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 307,
    "DeviceModeCode": 21,
    "DeviceCode": 1,
    "DeviceFullCode": "380M307M21M1",
    "DeviceModeFullCode": "380M307M21",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceCode": 1,
    "DeviceFullCode": "380M505M7M1",
    "DeviceModeFullCode": "380M505M7",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceCode": 2,
    "DeviceFullCode": "380M505M7M2",
    "DeviceModeFullCode": "380M505M7",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceCode": 1,
    "DeviceFullCode": "380M801M1M1",
    "DeviceModeFullCode": "380M801M1",
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
        self.stationCode = 380
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
            results = pool.map(self.___calcDeviceAggrega,[201,202,203,206,302,305,307,801])
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
                    if deviceTypeCode==203 and deviceItem['DeviceFullCode']=="380M203M8M2":
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
