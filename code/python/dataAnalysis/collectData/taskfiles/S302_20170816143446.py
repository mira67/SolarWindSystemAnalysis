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
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "直流输入电压1",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "直流输入电压1",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "直流输入电压1",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "直流输入电压1",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "直流输入电流1",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "直流输入电流1",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "直流输入电流1",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "直流输入电流1",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "AB线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "AB线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "AB线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "AB线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "BC线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "BC线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "BC线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "BC线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "CA线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "CA线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "CA线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "CA线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "A相电网侧电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "A相电网侧电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "A相电网侧电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "A相电网侧电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "B相电网侧电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "B相电网侧电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "B相电网侧电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "B相电网侧电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "C相电网侧电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "C相电网侧电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "C相电网侧电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "C相电网侧电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电网侧电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电网侧电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电网侧电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电网侧电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电网侧电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电网侧电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电网侧电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电网侧电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电网侧电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电网侧电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电网侧电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电网侧电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "功率因数",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "功率因数",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "功率因数",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "功率因数",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "并网频率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "并网频率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "并网频率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "并网频率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "并网功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "并网功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "并网功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "并网功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "交流输出无功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "交流输出无功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "交流输出无功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "交流输出无功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "散热器温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "散热器温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "散热器温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "散热器温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器开机时间日",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器开机时间日",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器开机时间日",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器开机时间日",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "并网时间(小时)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "并网时间(小时)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "并网时间(小时)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "并网时间(小时)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB030",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Inv_DC_W",
    "DeviceModePointName": "直流侧功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB030",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Inv_DC_W",
    "DeviceModePointName": "直流侧功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB030",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Inv_DC_W",
    "DeviceModePointName": "直流侧功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB030",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "Inv_DC_W",
    "DeviceModePointName": "直流侧功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "线路电流01",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "线路电流01",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "线路电流01",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "线路电流01",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "线路电流02",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "线路电流02",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "线路电流02",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "线路电流02",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "线路电流03",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "线路电流03",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "线路电流03",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "线路电流03",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "线路电流04",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "线路电流04",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "线路电流04",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "线路电流04",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "线路电流05",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "线路电流05",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "线路电流05",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "线路电流05",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "线路电流06",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "线路电流06",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "线路电流06",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "线路电流06",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "线路电流07",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "线路电流07",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "线路电流07",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "线路电流07",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "线路电流08",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "线路电流08",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "线路电流08",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "线路电流08",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "线路电流09",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "线路电流09",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "线路电流09",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "线路电流09",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "线路电流10",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "线路电流10",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "线路电流10",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "线路电流10",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "线路电流11",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "线路电流11",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "线路电流11",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "线路电流11",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "线路电流12",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "线路电流12",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "线路电流12",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "线路电流12",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "线路电流13",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "线路电流13",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "线路电流13",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "线路电流13",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "线路电流14",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "线路电流14",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "线路电流14",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "线路电流14",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "线路电流15",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "线路电流15",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "线路电流15",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "线路电流15",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "线路电流16",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "线路电流16",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "线路电流16",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "线路电流16",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "输出电压值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "输出电压值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "输出电压值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "输出电压值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱内部温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱内部温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱内部温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱内部温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "线路电流01",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "线路电流01",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "线路电流01",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "线路电流01",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "线路电流02",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "线路电流02",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "线路电流02",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "线路电流02",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "线路电流03",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "线路电流03",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "线路电流03",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "线路电流03",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "线路电流04",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "线路电流04",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "线路电流04",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "线路电流04",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "线路电流05",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "线路电流05",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "线路电流05",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "线路电流05",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "线路电流06",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "线路电流06",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "线路电流06",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "线路电流06",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "线路电流07",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "线路电流07",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "线路电流07",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "线路电流07",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "线路电流08",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "线路电流08",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "线路电流08",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "线路电流08",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "线路电流09",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "线路电流09",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "线路电流09",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "线路电流09",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "线路电流10",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "线路电流10",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "线路电流10",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "线路电流10",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "线路电流11",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "线路电流11",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "线路电流11",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "线路电流11",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "线路电流12",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "线路电流12",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "线路电流12",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "线路电流12",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "线路电流13",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "线路电流13",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "线路电流13",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "线路电流13",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "线路电流14",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "线路电流14",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "线路电流14",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "线路电流14",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "线路电流15",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "线路电流15",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "线路电流15",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "线路电流15",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "线路电流16",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "线路电流16",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "线路电流16",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "线路电流16",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "输出电压值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "输出电压值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "输出电压值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "输出电压值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱内部温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱内部温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱内部温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL102",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "汇流箱内部温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "1号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计(*1000)",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX015",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Back_Plate_Tmp_2",
    "DeviceModePointName": "2号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX016",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Back_Plate_Tmp_3",
    "DeviceModePointName": "3号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX017",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Back_Plate_Tmp_4",
    "DeviceModePointName": "4号背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX018",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceModePointIECName": "Air_Pres",
    "DeviceModePointName": "大气压力瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "AB相线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "AB相线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "AB相线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "AB相线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "BC相线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "BC相线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "BC相线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "BC相线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "CA相线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "CA相线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "CA相线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "CA相线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "A相电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "A相电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "A相电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "A相电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "C相电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "C相电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "C相电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "C相电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "有功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "有功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "有功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "有功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "无功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "无功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "无功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "无功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "功率因素",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "功率因素",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "功率因素",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "功率因素",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "频率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "频率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "频率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "频率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "AB相线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "AB相线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "AB相线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "AB相线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "BC相线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "BC相线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "BC相线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "BC相线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "CA相线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "CA相线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "CA相线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "CA相线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ007",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "零序电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ007",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "零序电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ007",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "零序电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ007",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "零序电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ008",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "A相电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ008",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "A相电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ008",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "A相电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ008",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "A相电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ010",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "C相电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ010",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "C相电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ010",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "C相电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ010",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "C相电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ011",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "零序电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ011",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "零序电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ011",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "零序电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ011",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "零序电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ012",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "有功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ012",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "有功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ012",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "有功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ012",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "有功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ013",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "无功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ013",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "无功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ013",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "无功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ013",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "无功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ014",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "功率因素",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ014",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "功率因素",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ014",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "功率因素",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ014",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "功率因素",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ015",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "频率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ015",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "频率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ015",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "频率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ015",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "频率",
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
    "DeviceModeCode": 4,
    "DeviceCode": 1,
    "DeviceFullCode": "302M201M4M1",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M1",
    "Capacity": 502.9000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceCode": 2,
    "DeviceFullCode": "302M201M4M2",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M1",
    "Capacity": 502.9000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceCode": 3,
    "DeviceFullCode": "302M201M4M3",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M2",
    "Capacity": 500.3200
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceCode": 4,
    "DeviceFullCode": "302M201M4M4",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M2",
    "Capacity": 500.3200
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceCode": 5,
    "DeviceFullCode": "302M201M4M5",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M3",
    "Capacity": 500.3200
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceCode": 6,
    "DeviceFullCode": "302M201M4M6",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M3",
    "Capacity": 500.3200
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceCode": 7,
    "DeviceFullCode": "302M201M4M7",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M4",
    "Capacity": 500.3200
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceCode": 8,
    "DeviceFullCode": "302M201M4M8",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M4",
    "Capacity": 500.3200
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceCode": 9,
    "DeviceFullCode": "302M201M4M9",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M5",
    "Capacity": 500.3200
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceCode": 10,
    "DeviceFullCode": "302M201M4M10",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M5",
    "Capacity": 500.3200
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceCode": 11,
    "DeviceFullCode": "302M201M4M11",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M6",
    "Capacity": 500.3200
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceCode": 12,
    "DeviceFullCode": "302M201M4M12",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M6",
    "Capacity": 500.3200
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceCode": 13,
    "DeviceFullCode": "302M201M4M13",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M7",
    "Capacity": 500.3200
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceCode": 14,
    "DeviceFullCode": "302M201M4M14",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M7",
    "Capacity": 500.3200
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceCode": 15,
    "DeviceFullCode": "302M201M4M15",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M8",
    "Capacity": 500.3200
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceCode": 16,
    "DeviceFullCode": "302M201M4M16",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M8",
    "Capacity": 500.3200
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceCode": 17,
    "DeviceFullCode": "302M201M4M17",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M9",
    "Capacity": 500.3200
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 4,
    "DeviceCode": 18,
    "DeviceFullCode": "302M201M4M18",
    "DeviceModeFullCode": "302M201M4",
    "PDeviceFullCode": "302M204M2M9",
    "Capacity": 500.3200
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 1,
    "DeviceFullCode": "302M202M7M1",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M3",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 2,
    "DeviceFullCode": "302M202M7M2",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M3",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 3,
    "DeviceFullCode": "302M202M7M3",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M3",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 4,
    "DeviceFullCode": "302M202M7M4",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M4",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 5,
    "DeviceFullCode": "302M202M7M5",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M4",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 6,
    "DeviceFullCode": "302M202M7M6",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M4",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 7,
    "DeviceFullCode": "302M202M7M7",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M5",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 8,
    "DeviceFullCode": "302M202M7M8",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M5",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 9,
    "DeviceFullCode": "302M202M7M9",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M5",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 10,
    "DeviceFullCode": "302M202M7M10",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M6",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 11,
    "DeviceFullCode": "302M202M7M11",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M6",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 12,
    "DeviceFullCode": "302M202M7M12",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M6",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 13,
    "DeviceFullCode": "302M202M7M13",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M7",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 14,
    "DeviceFullCode": "302M202M7M14",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M7",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 15,
    "DeviceFullCode": "302M202M7M15",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M7",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 16,
    "DeviceFullCode": "302M202M7M16",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M8",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 17,
    "DeviceFullCode": "302M202M7M17",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M8",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 18,
    "DeviceFullCode": "302M202M7M18",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M8",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 19,
    "DeviceFullCode": "302M202M7M19",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M9",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 20,
    "DeviceFullCode": "302M202M7M20",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M9",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 21,
    "DeviceFullCode": "302M202M7M21",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M9",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 22,
    "DeviceFullCode": "302M202M7M22",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M10",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 23,
    "DeviceFullCode": "302M202M7M23",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M10",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 24,
    "DeviceFullCode": "302M202M7M24",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M10",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 25,
    "DeviceFullCode": "302M202M7M25",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M11",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 26,
    "DeviceFullCode": "302M202M7M26",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M11",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 27,
    "DeviceFullCode": "302M202M7M27",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M11",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 28,
    "DeviceFullCode": "302M202M7M28",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M12",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 29,
    "DeviceFullCode": "302M202M7M29",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M12",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 30,
    "DeviceFullCode": "302M202M7M30",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M12",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 31,
    "DeviceFullCode": "302M202M7M31",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M13",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 32,
    "DeviceFullCode": "302M202M7M32",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M13",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 33,
    "DeviceFullCode": "302M202M7M33",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M13",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 34,
    "DeviceFullCode": "302M202M7M34",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M14",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 35,
    "DeviceFullCode": "302M202M7M35",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M14",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 36,
    "DeviceFullCode": "302M202M7M36",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M14",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 37,
    "DeviceFullCode": "302M202M7M37",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M15",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 38,
    "DeviceFullCode": "302M202M7M38",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M15",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 39,
    "DeviceFullCode": "302M202M7M39",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M15",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 40,
    "DeviceFullCode": "302M202M7M40",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M16",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 41,
    "DeviceFullCode": "302M202M7M41",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M16",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 42,
    "DeviceFullCode": "302M202M7M42",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M16",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 43,
    "DeviceFullCode": "302M202M7M43",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M17",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 44,
    "DeviceFullCode": "302M202M7M44",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M17",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 45,
    "DeviceFullCode": "302M202M7M45",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M17",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 46,
    "DeviceFullCode": "302M202M7M46",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M18",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 47,
    "DeviceFullCode": "302M202M7M47",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M18",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 7,
    "DeviceCode": 48,
    "DeviceFullCode": "302M202M7M48",
    "DeviceModeFullCode": "302M202M7",
    "PDeviceFullCode": "302M201M4M18",
    "Capacity": 56.6400
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 49,
    "DeviceFullCode": "302M202M8M49",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M1",
    "Capacity": 75.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 50,
    "DeviceFullCode": "302M202M8M50",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M1",
    "Capacity": 75.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 51,
    "DeviceFullCode": "302M202M8M51",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M1",
    "Capacity": 70.5000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 52,
    "DeviceFullCode": "302M202M8M52",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M1",
    "Capacity": 65.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 53,
    "DeviceFullCode": "302M202M8M53",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M1",
    "Capacity": 65.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 54,
    "DeviceFullCode": "302M202M8M54",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M1",
    "Capacity": 75.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 55,
    "DeviceFullCode": "302M202M8M55",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M1",
    "Capacity": 75.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 56,
    "DeviceFullCode": "302M202M8M56",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M2",
    "Capacity": 75.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 57,
    "DeviceFullCode": "302M202M8M57",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M2",
    "Capacity": 75.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 58,
    "DeviceFullCode": "302M202M8M58",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M2",
    "Capacity": 70.5000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 59,
    "DeviceFullCode": "302M202M8M59",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M2",
    "Capacity": 65.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 60,
    "DeviceFullCode": "302M202M8M60",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M2",
    "Capacity": 65.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 61,
    "DeviceFullCode": "302M202M8M61",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M2",
    "Capacity": 75.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 62,
    "DeviceFullCode": "302M202M8M62",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M2",
    "Capacity": 75.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 63,
    "DeviceFullCode": "302M202M8M63",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M3",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 64,
    "DeviceFullCode": "302M202M8M64",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M3",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 65,
    "DeviceFullCode": "302M202M8M65",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M3",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 66,
    "DeviceFullCode": "302M202M8M66",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M3",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 67,
    "DeviceFullCode": "302M202M8M67",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M3",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 68,
    "DeviceFullCode": "302M202M8M68",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M4",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 69,
    "DeviceFullCode": "302M202M8M69",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M4",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 70,
    "DeviceFullCode": "302M202M8M70",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M4",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 71,
    "DeviceFullCode": "302M202M8M71",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M4",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 72,
    "DeviceFullCode": "302M202M8M72",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M4",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 73,
    "DeviceFullCode": "302M202M8M73",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M5",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 74,
    "DeviceFullCode": "302M202M8M74",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M5",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 75,
    "DeviceFullCode": "302M202M8M75",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M5",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 76,
    "DeviceFullCode": "302M202M8M76",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M5",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 77,
    "DeviceFullCode": "302M202M8M77",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M5",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 78,
    "DeviceFullCode": "302M202M8M78",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M6",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 79,
    "DeviceFullCode": "302M202M8M79",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M6",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 80,
    "DeviceFullCode": "302M202M8M80",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M6",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 81,
    "DeviceFullCode": "302M202M8M81",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M6",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 82,
    "DeviceFullCode": "302M202M8M82",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M6",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 83,
    "DeviceFullCode": "302M202M8M83",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M7",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 84,
    "DeviceFullCode": "302M202M8M84",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M7",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 85,
    "DeviceFullCode": "302M202M8M85",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M7",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 86,
    "DeviceFullCode": "302M202M8M86",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M7",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 87,
    "DeviceFullCode": "302M202M8M87",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M7",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 88,
    "DeviceFullCode": "302M202M8M88",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M8",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 89,
    "DeviceFullCode": "302M202M8M89",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M8",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 90,
    "DeviceFullCode": "302M202M8M90",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M8",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 91,
    "DeviceFullCode": "302M202M8M91",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M8",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 92,
    "DeviceFullCode": "302M202M8M92",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M8",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 93,
    "DeviceFullCode": "302M202M8M93",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M9",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 94,
    "DeviceFullCode": "302M202M8M94",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M9",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 95,
    "DeviceFullCode": "302M202M8M95",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M9",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 96,
    "DeviceFullCode": "302M202M8M96",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M9",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 97,
    "DeviceFullCode": "302M202M8M97",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M9",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 98,
    "DeviceFullCode": "302M202M8M98",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M10",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 99,
    "DeviceFullCode": "302M202M8M99",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M10",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 100,
    "DeviceFullCode": "302M202M8M100",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M10",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 101,
    "DeviceFullCode": "302M202M8M101",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M10",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 102,
    "DeviceFullCode": "302M202M8M102",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M10",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 103,
    "DeviceFullCode": "302M202M8M103",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M11",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 104,
    "DeviceFullCode": "302M202M8M104",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M11",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 105,
    "DeviceFullCode": "302M202M8M105",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M11",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 106,
    "DeviceFullCode": "302M202M8M106",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M11",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 107,
    "DeviceFullCode": "302M202M8M107",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M11",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 108,
    "DeviceFullCode": "302M202M8M108",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M12",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 109,
    "DeviceFullCode": "302M202M8M109",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M12",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 110,
    "DeviceFullCode": "302M202M8M110",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M12",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 111,
    "DeviceFullCode": "302M202M8M111",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M12",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 112,
    "DeviceFullCode": "302M202M8M112",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M12",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 113,
    "DeviceFullCode": "302M202M8M113",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M13",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 114,
    "DeviceFullCode": "302M202M8M114",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M13",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 115,
    "DeviceFullCode": "302M202M8M115",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M13",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 116,
    "DeviceFullCode": "302M202M8M116",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M13",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 117,
    "DeviceFullCode": "302M202M8M117",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M13",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 118,
    "DeviceFullCode": "302M202M8M118",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M14",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 119,
    "DeviceFullCode": "302M202M8M119",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M14",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 120,
    "DeviceFullCode": "302M202M8M120",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M14",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 121,
    "DeviceFullCode": "302M202M8M121",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M14",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 122,
    "DeviceFullCode": "302M202M8M122",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M14",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 123,
    "DeviceFullCode": "302M202M8M123",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M15",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 124,
    "DeviceFullCode": "302M202M8M124",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M15",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 125,
    "DeviceFullCode": "302M202M8M125",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M15",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 126,
    "DeviceFullCode": "302M202M8M126",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M15",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 127,
    "DeviceFullCode": "302M202M8M127",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M15",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 128,
    "DeviceFullCode": "302M202M8M128",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M16",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 129,
    "DeviceFullCode": "302M202M8M129",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M16",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 130,
    "DeviceFullCode": "302M202M8M130",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M16",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 131,
    "DeviceFullCode": "302M202M8M131",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M16",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 132,
    "DeviceFullCode": "302M202M8M132",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M16",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 133,
    "DeviceFullCode": "302M202M8M133",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M17",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 134,
    "DeviceFullCode": "302M202M8M134",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M17",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 135,
    "DeviceFullCode": "302M202M8M135",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M17",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 136,
    "DeviceFullCode": "302M202M8M136",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M17",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 137,
    "DeviceFullCode": "302M202M8M137",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M17",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 138,
    "DeviceFullCode": "302M202M8M138",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M18",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 139,
    "DeviceFullCode": "302M202M8M139",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M18",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 140,
    "DeviceFullCode": "302M202M8M140",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M18",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 141,
    "DeviceFullCode": "302M202M8M141",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M18",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 8,
    "DeviceCode": 142,
    "DeviceFullCode": "302M202M8M142",
    "DeviceModeFullCode": "302M202M8",
    "PDeviceFullCode": "302M201M4M18",
    "Capacity": 66.0800
  },
  {
    "DeviceTypeCode": 203,
    "DeviceModeCode": 5,
    "DeviceCode": 1,
    "DeviceFullCode": "302M203M5M1",
    "DeviceModeFullCode": "302M203M5",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 17,
    "DeviceCode": 1,
    "DeviceFullCode": "302M302M17M1",
    "DeviceModeFullCode": "302M302M17",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 307,
    "DeviceModeCode": 15,
    "DeviceCode": 1,
    "DeviceFullCode": "302M307M15M1",
    "DeviceModeFullCode": "302M307M15",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 7,
    "DeviceCode": 1,
    "DeviceFullCode": "302M505M7M1",
    "DeviceModeFullCode": "302M505M7",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 2,
    "DeviceFullCode": "302M505M2M2",
    "DeviceModeFullCode": "302M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 3,
    "DeviceFullCode": "302M505M2M3",
    "DeviceModeFullCode": "302M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 4,
    "DeviceFullCode": "302M505M2M4",
    "DeviceModeFullCode": "302M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 5,
    "DeviceFullCode": "302M505M2M5",
    "DeviceModeFullCode": "302M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceCode": 1,
    "DeviceFullCode": "302M801M1M1",
    "DeviceModeFullCode": "302M801M1",
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
        self.stationCode = 302
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
                    if deviceTypeCode==203 and deviceItem['DeviceFullCode']=="302M203M5M1":
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
