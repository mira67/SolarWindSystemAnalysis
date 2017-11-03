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
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB001",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_V",
    "DeviceModePointName": "逆变器直流侧电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB002",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "DC_A_Tot",
    "DeviceModePointName": "逆变器直流侧总电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB004",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PP_V_AB",
    "DeviceModePointName": "逆变器电网AB线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB005",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PP_V_BC",
    "DeviceModePointName": "逆变器电网BC线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB006",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PP_V_CA",
    "DeviceModePointName": "逆变器电网CA线电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB007",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_A",
    "DeviceModePointName": "逆变器A相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB008",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_A",
    "DeviceModePointName": "逆变器B相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB009",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_A",
    "DeviceModePointName": "逆变器C相并网电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB010",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_V",
    "DeviceModePointName": "A相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB011",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_V",
    "DeviceModePointName": "B相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB012",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_V",
    "DeviceModePointName": "C相电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB013",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "PF",
    "DeviceModePointName": "逆变器功率因数",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB014",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri_Hz",
    "DeviceModePointName": "逆变器电网频率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB015",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_Act_W",
    "DeviceModePointName": "有功功率Pa",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB015",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_Act_W",
    "DeviceModePointName": "有功功率Pa",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB015",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_Act_W",
    "DeviceModePointName": "有功功率Pa",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB015",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_Act_W",
    "DeviceModePointName": "有功功率Pa",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB016",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_Act_W",
    "DeviceModePointName": "有功功率Pb",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB016",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_Act_W",
    "DeviceModePointName": "有功功率Pb",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB016",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_Act_W",
    "DeviceModePointName": "有功功率Pb",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB016",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_Act_W",
    "DeviceModePointName": "有功功率Pb",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB017",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_Act_W",
    "DeviceModePointName": "有功功率Pc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB017",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_Act_W",
    "DeviceModePointName": "有功功率Pc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB017",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_Act_W",
    "DeviceModePointName": "有功功率Pc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB017",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_Act_W",
    "DeviceModePointName": "有功功率Pc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB018",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Act_W_Tot",
    "DeviceModePointName": "逆变器并网有功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB019",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_React_W",
    "DeviceModePointName": "无功功率Qa",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB019",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_React_W",
    "DeviceModePointName": "无功功率Qa",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB019",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_React_W",
    "DeviceModePointName": "无功功率Qa",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB019",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_React_W",
    "DeviceModePointName": "无功功率Qa",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB020",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_React_W",
    "DeviceModePointName": "无功功率Qb",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB020",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_React_W",
    "DeviceModePointName": "无功功率Qb",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB020",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_React_W",
    "DeviceModePointName": "无功功率Qb",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB020",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_React_W",
    "DeviceModePointName": "无功功率Qb",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB021",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_React_W",
    "DeviceModePointName": "无功功率Qc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB021",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_React_W",
    "DeviceModePointName": "无功功率Qc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB021",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_React_W",
    "DeviceModePointName": "无功功率Qc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB021",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_React_W",
    "DeviceModePointName": "无功功率Qc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB022",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "React_W_Tot",
    "DeviceModePointName": "逆变器并网无功功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB023",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_APRT_W",
    "DeviceModePointName": "视在功率Sa",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB023",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_APRT_W",
    "DeviceModePointName": "视在功率Sa",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB023",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_APRT_W",
    "DeviceModePointName": "视在功率Sa",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB023",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_A_APRT_W",
    "DeviceModePointName": "视在功率Sa",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB024",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_APRT_W",
    "DeviceModePointName": "视在功率Sb",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB024",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_APRT_W",
    "DeviceModePointName": "视在功率Sb",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB024",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_APRT_W",
    "DeviceModePointName": "视在功率Sb",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB024",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_B_APRT_W",
    "DeviceModePointName": "视在功率Sb",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB025",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_APRT_W",
    "DeviceModePointName": "视在功率Sc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB025",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_APRT_W",
    "DeviceModePointName": "视在功率Sc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB025",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_APRT_W",
    "DeviceModePointName": "视在功率Sc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB025",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Ph_C_APRT_W",
    "DeviceModePointName": "视在功率Sc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB026",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": " APRT_W_Tot",
    "DeviceModePointName": "总视在功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB026",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": " APRT_W_Tot",
    "DeviceModePointName": "总视在功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB026",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": " APRT_W_Tot",
    "DeviceModePointName": "总视在功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB026",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": " APRT_W_Tot",
    "DeviceModePointName": "总视在功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB027",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Inner_Air_Tmp",
    "DeviceModePointName": "逆变器逆变器机柜温度",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB030",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Inv_DC_W",
    "DeviceModePointName": "直流侧功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB030",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Inv_DC_W",
    "DeviceModePointName": "直流侧功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB030",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Inv_DC_W",
    "DeviceModePointName": "直流侧功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB030",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Inv_DC_W",
    "DeviceModePointName": "直流侧功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器日运行时间",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器日运行时间",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB028",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Op_Tm_Dly",
    "DeviceModePointName": "逆变器日运行时间",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "逆变器总运行时间",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "逆变器总运行时间",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB029",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Op_Tm_Tot",
    "DeviceModePointName": "逆变器总运行时间",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB031",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWhDly",
    "DeviceModePointName": "逆变器日累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB032",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWhMly",
    "DeviceModePointName": "逆变器月累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB033",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWhYly",
    "DeviceModePointName": "逆变器年累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "NB034",
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "TotWh",
    "DeviceModePointName": "逆变器总累计发电量",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL001",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A1",
    "DeviceModePointName": "汇流箱支路1电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL002",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A2",
    "DeviceModePointName": "汇流箱支路2电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL003",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A3",
    "DeviceModePointName": "汇流箱支路3电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL004",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A4",
    "DeviceModePointName": "汇流箱支路4电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL005",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A5",
    "DeviceModePointName": "汇流箱支路5电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL006",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A6",
    "DeviceModePointName": "汇流箱支路6电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL007",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A7",
    "DeviceModePointName": "汇流箱支路7电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL008",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A8",
    "DeviceModePointName": "汇流箱支路8电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL009",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A9",
    "DeviceModePointName": "汇流箱支路9电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL010",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A10",
    "DeviceModePointName": "汇流箱支路10电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL011",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A11",
    "DeviceModePointName": "汇流箱支路11电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL012",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A12",
    "DeviceModePointName": "汇流箱支路12电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL013",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A13",
    "DeviceModePointName": "汇流箱支路13电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL014",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A14",
    "DeviceModePointName": "汇流箱支路14电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL015",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A15",
    "DeviceModePointName": "汇流箱支路15电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL016",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A16",
    "DeviceModePointName": "汇流箱支路16电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL101",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_V",
    "DeviceModePointName": "汇流箱总电压",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL103",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "COMB_DiscRate",
    "DeviceModePointName": "离散率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL104",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_A_Tot",
    "DeviceModePointName": "汇流箱总电流",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "HL105",
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Branch_W_Tot",
    "DeviceModePointName": "汇流箱总功率",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX001",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Hori_Radi",
    "DeviceModePointName": "水平辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX002",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Tilted_Surf_Radi",
    "DeviceModePointName": "斜面辐射瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX003",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Wind_Spd",
    "DeviceModePointName": "风速瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX004",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Wind_Dir",
    "DeviceModePointName": "风向瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX005",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Amb_Tmp",
    "DeviceModePointName": "空气温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX006",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Amb_Hum",
    "DeviceModePointName": "湿度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "背板温度瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX008",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Shrt_A_Num1",
    "DeviceModePointName": "1号短路电流瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX013",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Component_j_t",
    "DeviceModePointName": "组件结温",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX014",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "STC_rad",
    "DeviceModePointName": "STC辐射值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计",
    "CalcMethod": "Dif",
    "Divation": 600
  },
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
    "DeviceModePointName": "背板温度瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "背板温度瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "背板温度瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX007",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Back_Plate_Tmp",
    "DeviceModePointName": "背板温度瞬时值",
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
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX009",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Open_V_Num1",
    "DeviceModePointName": "1号开路电压瞬时值",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX010",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Shrt_A_Num2",
    "DeviceModePointName": "2号短路电流瞬时值",
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
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX011",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Hori_Radi_Dly",
    "DeviceModePointName": "水平面曝辐量天累计",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计",
    "CalcMethod": "Last",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计",
    "CalcMethod": "First",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "QX012",
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceModePointIECName": "Tilted_Surf_Radi_Dly",
    "DeviceModePointName": "倾斜面曝辐量天累计",
    "CalcMethod": "Dif",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD001",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD002",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD003",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD004",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD005",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD006",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD007",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "3U0",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD007",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "3U0",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD007",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "3U0",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD007",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "3U0",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD008",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD009",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD010",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD011",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "3I0",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD011",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "3I0",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD011",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "3I0",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD011",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "3I0",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD012",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD013",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD014",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "JD015",
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ001",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUab",
    "DeviceModePointName": "Uab",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ002",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUbc",
    "DeviceModePointName": "Ubc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ003",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUca",
    "DeviceModePointName": "Uca",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ004",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUa",
    "DeviceModePointName": "Ua",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ005",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUb",
    "DeviceModePointName": "Ub",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ006",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPPhVUc",
    "DeviceModePointName": "Uc",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ007",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "3U0",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ007",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "3U0",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ007",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "3U0",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ007",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri3U0",
    "DeviceModePointName": "3U0",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ008",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ008",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ008",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ008",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIa",
    "DeviceModePointName": "Ia",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ009",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ009",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ009",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ009",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIb",
    "DeviceModePointName": "Ib",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ010",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ010",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ010",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ010",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriAIc",
    "DeviceModePointName": "Ic",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ011",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "3I0",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ011",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "3I0",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ011",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "3I0",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ011",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "Gri3I0",
    "DeviceModePointName": "3I0",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ012",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ012",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ012",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ012",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriW",
    "DeviceModePointName": "P",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ013",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ013",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ013",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ013",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriVar",
    "DeviceModePointName": "Q",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ014",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ014",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ014",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ014",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriPF",
    "DeviceModePointName": "Cos",
    "CalcMethod": "Std",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ015",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Avg",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ015",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Max",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ015",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
    "CalcMethod": "Min",
    "Divation": 600
  },
  {
    "StationType": 20,
    "DeviceModePointCode": "ZJ015",
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceModePointIECName": "GriHz",
    "DeviceModePointName": "Fr",
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
    "DeviceModeCode": 1,
    "DeviceCode": 1,
    "DeviceFullCode": "340M201M1M1",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 510.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 2,
    "DeviceFullCode": "340M201M1M2",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 3,
    "DeviceFullCode": "340M201M1M3",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 510.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 4,
    "DeviceFullCode": "340M201M1M4",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 5,
    "DeviceFullCode": "340M201M1M5",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 510.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 6,
    "DeviceFullCode": "340M201M1M6",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 7,
    "DeviceFullCode": "340M201M1M7",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 510.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 8,
    "DeviceFullCode": "340M201M1M8",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 9,
    "DeviceFullCode": "340M201M1M9",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 510.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 10,
    "DeviceFullCode": "340M201M1M10",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 11,
    "DeviceFullCode": "340M201M1M11",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 12,
    "DeviceFullCode": "340M201M1M12",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 13,
    "DeviceFullCode": "340M201M1M13",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 515.1000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 14,
    "DeviceFullCode": "340M201M1M14",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 15,
    "DeviceFullCode": "340M201M1M15",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 499.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 16,
    "DeviceFullCode": "340M201M1M16",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 510.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 17,
    "DeviceFullCode": "340M201M1M17",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 499.8000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 18,
    "DeviceFullCode": "340M201M1M18",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": None,
    "Capacity": 515.1000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 19,
    "DeviceFullCode": "340M201M1M19",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M10",
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 20,
    "DeviceFullCode": "340M201M1M20",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M10",
    "Capacity": 510.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 21,
    "DeviceFullCode": "340M201M1M21",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M11",
    "Capacity": 510.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 22,
    "DeviceFullCode": "340M201M1M22",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M11",
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 23,
    "DeviceFullCode": "340M201M1M23",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M12",
    "Capacity": 510.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 24,
    "DeviceFullCode": "340M201M1M24",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M12",
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 25,
    "DeviceFullCode": "340M201M1M25",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M13",
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 26,
    "DeviceFullCode": "340M201M1M26",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M13",
    "Capacity": 510.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 27,
    "DeviceFullCode": "340M201M1M27",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M14",
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 28,
    "DeviceFullCode": "340M201M1M28",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M14",
    "Capacity": 510.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 29,
    "DeviceFullCode": "340M201M1M29",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M15",
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 30,
    "DeviceFullCode": "340M201M1M30",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M15",
    "Capacity": 510.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 31,
    "DeviceFullCode": "340M201M1M31",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M16",
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 32,
    "DeviceFullCode": "340M201M1M32",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M16",
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 33,
    "DeviceFullCode": "340M201M1M33",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M17",
    "Capacity": 510.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 34,
    "DeviceFullCode": "340M201M1M34",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M17",
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 35,
    "DeviceFullCode": "340M201M1M35",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M18",
    "Capacity": 510.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 36,
    "DeviceFullCode": "340M201M1M36",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M18",
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 37,
    "DeviceFullCode": "340M201M1M37",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M19",
    "Capacity": 510.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 38,
    "DeviceFullCode": "340M201M1M38",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M19",
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 39,
    "DeviceFullCode": "340M201M1M39",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M20",
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 40,
    "DeviceFullCode": "340M201M1M40",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M20",
    "Capacity": 510.0000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 41,
    "DeviceFullCode": "340M201M1M41",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M21",
    "Capacity": 520.2000
  },
  {
    "DeviceTypeCode": 201,
    "DeviceModeCode": 1,
    "DeviceCode": 42,
    "DeviceFullCode": "340M201M1M42",
    "DeviceModeFullCode": "340M201M1",
    "PDeviceFullCode": "340M204M2M21",
    "Capacity": 510.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 1,
    "DeviceFullCode": "340M202M1M1",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M1",
    "Capacity": 61.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 2,
    "DeviceFullCode": "340M202M1M2",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M1",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 3,
    "DeviceFullCode": "340M202M1M3",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M1",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 4,
    "DeviceFullCode": "340M202M1M4",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M1",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 5,
    "DeviceFullCode": "340M202M1M5",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M1",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 6,
    "DeviceFullCode": "340M202M1M6",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M1",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 7,
    "DeviceFullCode": "340M202M1M7",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M1",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 8,
    "DeviceFullCode": "340M202M1M8",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M2",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 9,
    "DeviceFullCode": "340M202M1M9",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M2",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 10,
    "DeviceFullCode": "340M202M1M10",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M2",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 11,
    "DeviceFullCode": "340M202M1M11",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M2",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 12,
    "DeviceFullCode": "340M202M1M12",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M2",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 13,
    "DeviceFullCode": "340M202M1M13",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M2",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 14,
    "DeviceFullCode": "340M202M1M14",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M2",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 15,
    "DeviceFullCode": "340M202M1M15",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M3",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 16,
    "DeviceFullCode": "340M202M1M16",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M3",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 17,
    "DeviceFullCode": "340M202M1M17",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M3",
    "Capacity": 30.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 18,
    "DeviceFullCode": "340M202M1M18",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M3",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 19,
    "DeviceFullCode": "340M202M1M19",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M3",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 20,
    "DeviceFullCode": "340M202M1M20",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M3",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 21,
    "DeviceFullCode": "340M202M1M21",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M3",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 22,
    "DeviceFullCode": "340M202M1M22",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M4",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 23,
    "DeviceFullCode": "340M202M1M23",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M4",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 24,
    "DeviceFullCode": "340M202M1M24",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M4",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 25,
    "DeviceFullCode": "340M202M1M25",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M4",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 26,
    "DeviceFullCode": "340M202M1M26",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M4",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 27,
    "DeviceFullCode": "340M202M1M27",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M4",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 28,
    "DeviceFullCode": "340M202M1M28",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M4",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 29,
    "DeviceFullCode": "340M202M1M29",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M5",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 30,
    "DeviceFullCode": "340M202M1M30",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M5",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 31,
    "DeviceFullCode": "340M202M1M31",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M5",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 32,
    "DeviceFullCode": "340M202M1M32",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M5",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 33,
    "DeviceFullCode": "340M202M1M33",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M5",
    "Capacity": 30.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 34,
    "DeviceFullCode": "340M202M1M34",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M5",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 35,
    "DeviceFullCode": "340M202M1M35",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M5",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 36,
    "DeviceFullCode": "340M202M1M36",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M6",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 37,
    "DeviceFullCode": "340M202M1M37",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M6",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 38,
    "DeviceFullCode": "340M202M1M38",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M6",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 39,
    "DeviceFullCode": "340M202M1M39",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M6",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 40,
    "DeviceFullCode": "340M202M1M40",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M6",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 41,
    "DeviceFullCode": "340M202M1M41",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M6",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 42,
    "DeviceFullCode": "340M202M1M42",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M6",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 43,
    "DeviceFullCode": "340M202M1M43",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M7",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 44,
    "DeviceFullCode": "340M202M1M44",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M7",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 45,
    "DeviceFullCode": "340M202M1M45",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M7",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 46,
    "DeviceFullCode": "340M202M1M46",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M7",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 47,
    "DeviceFullCode": "340M202M1M47",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M7",
    "Capacity": 30.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 48,
    "DeviceFullCode": "340M202M1M48",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M7",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 49,
    "DeviceFullCode": "340M202M1M49",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M7",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 50,
    "DeviceFullCode": "340M202M1M50",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M8",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 51,
    "DeviceFullCode": "340M202M1M51",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M8",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 52,
    "DeviceFullCode": "340M202M1M52",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M8",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 53,
    "DeviceFullCode": "340M202M1M53",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M8",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 54,
    "DeviceFullCode": "340M202M1M54",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M8",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 55,
    "DeviceFullCode": "340M202M1M55",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M8",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 56,
    "DeviceFullCode": "340M202M1M56",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M8",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 57,
    "DeviceFullCode": "340M202M1M57",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M9",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 58,
    "DeviceFullCode": "340M202M1M58",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M9",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 59,
    "DeviceFullCode": "340M202M1M59",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M9",
    "Capacity": 30.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 60,
    "DeviceFullCode": "340M202M1M60",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M9",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 61,
    "DeviceFullCode": "340M202M1M61",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M9",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 62,
    "DeviceFullCode": "340M202M1M62",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M9",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 63,
    "DeviceFullCode": "340M202M1M63",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M9",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 64,
    "DeviceFullCode": "340M202M1M64",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M10",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 65,
    "DeviceFullCode": "340M202M1M65",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M10",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 66,
    "DeviceFullCode": "340M202M1M66",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M10",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 67,
    "DeviceFullCode": "340M202M1M67",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M10",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 68,
    "DeviceFullCode": "340M202M1M68",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M10",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 69,
    "DeviceFullCode": "340M202M1M69",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M10",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 70,
    "DeviceFullCode": "340M202M1M70",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M10",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 71,
    "DeviceFullCode": "340M202M1M71",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M11",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 72,
    "DeviceFullCode": "340M202M1M72",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M11",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 73,
    "DeviceFullCode": "340M202M1M73",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M11",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 74,
    "DeviceFullCode": "340M202M1M74",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M11",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 75,
    "DeviceFullCode": "340M202M1M75",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M11",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 76,
    "DeviceFullCode": "340M202M1M76",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M11",
    "Capacity": 30.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 77,
    "DeviceFullCode": "340M202M1M77",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M11",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 78,
    "DeviceFullCode": "340M202M1M78",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M12",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 79,
    "DeviceFullCode": "340M202M1M79",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M12",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 80,
    "DeviceFullCode": "340M202M1M80",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M12",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 81,
    "DeviceFullCode": "340M202M1M81",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M12",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 82,
    "DeviceFullCode": "340M202M1M82",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M12",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 83,
    "DeviceFullCode": "340M202M1M83",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M12",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 84,
    "DeviceFullCode": "340M202M1M84",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M12",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 85,
    "DeviceFullCode": "340M202M1M85",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M13",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 86,
    "DeviceFullCode": "340M202M1M86",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M13",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 87,
    "DeviceFullCode": "340M202M1M87",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M13",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 88,
    "DeviceFullCode": "340M202M1M88",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M13",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 89,
    "DeviceFullCode": "340M202M1M89",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M13",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 90,
    "DeviceFullCode": "340M202M1M90",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M13",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 91,
    "DeviceFullCode": "340M202M1M91",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M13",
    "Capacity": 45.9000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 92,
    "DeviceFullCode": "340M202M1M92",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M14",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 93,
    "DeviceFullCode": "340M202M1M93",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M14",
    "Capacity": 51.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 94,
    "DeviceFullCode": "340M202M1M94",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M14",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 95,
    "DeviceFullCode": "340M202M1M95",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M14",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 96,
    "DeviceFullCode": "340M202M1M96",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M14",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 97,
    "DeviceFullCode": "340M202M1M97",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M14",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 98,
    "DeviceFullCode": "340M202M1M98",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M14",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 99,
    "DeviceFullCode": "340M202M1M99",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M15",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 100,
    "DeviceFullCode": "340M202M1M100",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M15",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 101,
    "DeviceFullCode": "340M202M1M101",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M15",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 102,
    "DeviceFullCode": "340M202M1M102",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M15",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 103,
    "DeviceFullCode": "340M202M1M103",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M15",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 104,
    "DeviceFullCode": "340M202M1M104",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M15",
    "Capacity": 51.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 105,
    "DeviceFullCode": "340M202M1M105",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M15",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 106,
    "DeviceFullCode": "340M202M1M106",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M16",
    "Capacity": 61.2000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 107,
    "DeviceFullCode": "340M202M1M107",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M16",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 108,
    "DeviceFullCode": "340M202M1M108",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M16",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 109,
    "DeviceFullCode": "340M202M1M109",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M16",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 110,
    "DeviceFullCode": "340M202M1M110",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M16",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 111,
    "DeviceFullCode": "340M202M1M111",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M16",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 112,
    "DeviceFullCode": "340M202M1M112",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M16",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 113,
    "DeviceFullCode": "340M202M1M113",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M17",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 114,
    "DeviceFullCode": "340M202M1M114",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M17",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 115,
    "DeviceFullCode": "340M202M1M115",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M17",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 116,
    "DeviceFullCode": "340M202M1M116",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M17",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 117,
    "DeviceFullCode": "340M202M1M117",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M17",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 118,
    "DeviceFullCode": "340M202M1M118",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M17",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 119,
    "DeviceFullCode": "340M202M1M119",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M17",
    "Capacity": 51.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 120,
    "DeviceFullCode": "340M202M1M120",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M18",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 121,
    "DeviceFullCode": "340M202M1M121",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M18",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 122,
    "DeviceFullCode": "340M202M1M122",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M18",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 123,
    "DeviceFullCode": "340M202M1M123",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M18",
    "Capacity": 66.3000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 124,
    "DeviceFullCode": "340M202M1M124",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M18",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 125,
    "DeviceFullCode": "340M202M1M125",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M18",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 126,
    "DeviceFullCode": "340M202M1M126",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M18",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 127,
    "DeviceFullCode": "340M202M1M127",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M19",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 128,
    "DeviceFullCode": "340M202M1M128",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M19",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 129,
    "DeviceFullCode": "340M202M1M129",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M19",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 130,
    "DeviceFullCode": "340M202M1M130",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M19",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 131,
    "DeviceFullCode": "340M202M1M131",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M19",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 132,
    "DeviceFullCode": "340M202M1M132",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M19",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 133,
    "DeviceFullCode": "340M202M1M133",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M19",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 134,
    "DeviceFullCode": "340M202M1M134",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M20",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 135,
    "DeviceFullCode": "340M202M1M135",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M20",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 136,
    "DeviceFullCode": "340M202M1M136",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M20",
    "Capacity": 30.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 137,
    "DeviceFullCode": "340M202M1M137",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M20",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 138,
    "DeviceFullCode": "340M202M1M138",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M20",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 139,
    "DeviceFullCode": "340M202M1M139",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M20",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 140,
    "DeviceFullCode": "340M202M1M140",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M20",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 141,
    "DeviceFullCode": "340M202M1M141",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M21",
    "Capacity": 30.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 142,
    "DeviceFullCode": "340M202M1M142",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M21",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 143,
    "DeviceFullCode": "340M202M1M143",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M21",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 144,
    "DeviceFullCode": "340M202M1M144",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M21",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 145,
    "DeviceFullCode": "340M202M1M145",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M21",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 146,
    "DeviceFullCode": "340M202M1M146",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M21",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 147,
    "DeviceFullCode": "340M202M1M147",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M21",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 148,
    "DeviceFullCode": "340M202M1M148",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M22",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 149,
    "DeviceFullCode": "340M202M1M149",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M22",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 150,
    "DeviceFullCode": "340M202M1M150",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M22",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 151,
    "DeviceFullCode": "340M202M1M151",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M22",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 152,
    "DeviceFullCode": "340M202M1M152",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M22",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 153,
    "DeviceFullCode": "340M202M1M153",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M22",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 154,
    "DeviceFullCode": "340M202M1M154",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M22",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 155,
    "DeviceFullCode": "340M202M1M155",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M23",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 156,
    "DeviceFullCode": "340M202M1M156",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M23",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 157,
    "DeviceFullCode": "340M202M1M157",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M23",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 158,
    "DeviceFullCode": "340M202M1M158",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M23",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 159,
    "DeviceFullCode": "340M202M1M159",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M23",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 160,
    "DeviceFullCode": "340M202M1M160",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M23",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 161,
    "DeviceFullCode": "340M202M1M161",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M23",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 162,
    "DeviceFullCode": "340M202M1M162",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M24",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 163,
    "DeviceFullCode": "340M202M1M163",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M24",
    "Capacity": 51.0000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 164,
    "DeviceFullCode": "340M202M1M164",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M24",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 165,
    "DeviceFullCode": "340M202M1M165",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M24",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 166,
    "DeviceFullCode": "340M202M1M166",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M24",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 167,
    "DeviceFullCode": "340M202M1M167",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M24",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 168,
    "DeviceFullCode": "340M202M1M168",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M24",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 169,
    "DeviceFullCode": "340M202M1M169",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M25",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 170,
    "DeviceFullCode": "340M202M1M170",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M25",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 171,
    "DeviceFullCode": "340M202M1M171",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M25",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 172,
    "DeviceFullCode": "340M202M1M172",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M25",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 173,
    "DeviceFullCode": "340M202M1M173",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M25",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 174,
    "DeviceFullCode": "340M202M1M174",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M25",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 175,
    "DeviceFullCode": "340M202M1M175",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M25",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 176,
    "DeviceFullCode": "340M202M1M176",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M26",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 177,
    "DeviceFullCode": "340M202M1M177",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M26",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 178,
    "DeviceFullCode": "340M202M1M178",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M26",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 179,
    "DeviceFullCode": "340M202M1M179",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M26",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 180,
    "DeviceFullCode": "340M202M1M180",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M26",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 181,
    "DeviceFullCode": "340M202M1M181",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M26",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 182,
    "DeviceFullCode": "340M202M1M182",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M26",
    "Capacity": 30.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 183,
    "DeviceFullCode": "340M202M1M183",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M27",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 184,
    "DeviceFullCode": "340M202M1M184",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M27",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 185,
    "DeviceFullCode": "340M202M1M185",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M27",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 186,
    "DeviceFullCode": "340M202M1M186",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M27",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 187,
    "DeviceFullCode": "340M202M1M187",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M27",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 188,
    "DeviceFullCode": "340M202M1M188",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M27",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 189,
    "DeviceFullCode": "340M202M1M189",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M27",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 190,
    "DeviceFullCode": "340M202M1M190",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M28",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 191,
    "DeviceFullCode": "340M202M1M191",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M28",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 192,
    "DeviceFullCode": "340M202M1M192",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M28",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 193,
    "DeviceFullCode": "340M202M1M193",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M28",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 194,
    "DeviceFullCode": "340M202M1M194",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M28",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 195,
    "DeviceFullCode": "340M202M1M195",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M28",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 196,
    "DeviceFullCode": "340M202M1M196",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M28",
    "Capacity": 30.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 197,
    "DeviceFullCode": "340M202M1M197",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M29",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 198,
    "DeviceFullCode": "340M202M1M198",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M29",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 199,
    "DeviceFullCode": "340M202M1M199",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M29",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 200,
    "DeviceFullCode": "340M202M1M200",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M29",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 201,
    "DeviceFullCode": "340M202M1M201",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M29",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 202,
    "DeviceFullCode": "340M202M1M202",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M29",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 203,
    "DeviceFullCode": "340M202M1M203",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M29",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 204,
    "DeviceFullCode": "340M202M1M204",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M30",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 205,
    "DeviceFullCode": "340M202M1M205",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M30",
    "Capacity": 30.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 206,
    "DeviceFullCode": "340M202M1M206",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M30",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 207,
    "DeviceFullCode": "340M202M1M207",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M30",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 208,
    "DeviceFullCode": "340M202M1M208",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M30",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 209,
    "DeviceFullCode": "340M202M1M209",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M30",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 210,
    "DeviceFullCode": "340M202M1M210",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M30",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 211,
    "DeviceFullCode": "340M202M1M211",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M31",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 212,
    "DeviceFullCode": "340M202M1M212",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M31",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 213,
    "DeviceFullCode": "340M202M1M213",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M31",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 214,
    "DeviceFullCode": "340M202M1M214",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M31",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 215,
    "DeviceFullCode": "340M202M1M215",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M31",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 216,
    "DeviceFullCode": "340M202M1M216",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M31",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 217,
    "DeviceFullCode": "340M202M1M217",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M31",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 218,
    "DeviceFullCode": "340M202M1M218",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M32",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 219,
    "DeviceFullCode": "340M202M1M219",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M32",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 220,
    "DeviceFullCode": "340M202M1M220",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M32",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 221,
    "DeviceFullCode": "340M202M1M221",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M32",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 222,
    "DeviceFullCode": "340M202M1M222",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M32",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 223,
    "DeviceFullCode": "340M202M1M223",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M32",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 224,
    "DeviceFullCode": "340M202M1M224",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M32",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 225,
    "DeviceFullCode": "340M202M1M225",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M33",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 226,
    "DeviceFullCode": "340M202M1M226",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M33",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 227,
    "DeviceFullCode": "340M202M1M227",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M33",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 228,
    "DeviceFullCode": "340M202M1M228",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M33",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 229,
    "DeviceFullCode": "340M202M1M229",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M33",
    "Capacity": 30.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 230,
    "DeviceFullCode": "340M202M1M230",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M33",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 231,
    "DeviceFullCode": "340M202M1M231",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M33",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 232,
    "DeviceFullCode": "340M202M1M232",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M34",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 233,
    "DeviceFullCode": "340M202M1M233",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M34",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 234,
    "DeviceFullCode": "340M202M1M234",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M34",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 235,
    "DeviceFullCode": "340M202M1M235",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M34",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 236,
    "DeviceFullCode": "340M202M1M236",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M34",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 237,
    "DeviceFullCode": "340M202M1M237",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M34",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 238,
    "DeviceFullCode": "340M202M1M238",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M34",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 239,
    "DeviceFullCode": "340M202M1M239",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M35",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 240,
    "DeviceFullCode": "340M202M1M240",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M35",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 241,
    "DeviceFullCode": "340M202M1M241",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M35",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 242,
    "DeviceFullCode": "340M202M1M242",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M35",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 243,
    "DeviceFullCode": "340M202M1M243",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M35",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 244,
    "DeviceFullCode": "340M202M1M244",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M35",
    "Capacity": 30.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 245,
    "DeviceFullCode": "340M202M1M245",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M35",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 246,
    "DeviceFullCode": "340M202M1M246",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M36",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 247,
    "DeviceFullCode": "340M202M1M247",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M36",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 248,
    "DeviceFullCode": "340M202M1M248",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M36",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 249,
    "DeviceFullCode": "340M202M1M249",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M36",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 250,
    "DeviceFullCode": "340M202M1M250",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M36",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 251,
    "DeviceFullCode": "340M202M1M251",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M36",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 252,
    "DeviceFullCode": "340M202M1M252",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M36",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 253,
    "DeviceFullCode": "340M202M1M253",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M37",
    "Capacity": 30.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 254,
    "DeviceFullCode": "340M202M1M254",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M37",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 255,
    "DeviceFullCode": "340M202M1M255",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M37",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 256,
    "DeviceFullCode": "340M202M1M256",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M37",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 257,
    "DeviceFullCode": "340M202M1M257",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M37",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 258,
    "DeviceFullCode": "340M202M1M258",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M37",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 259,
    "DeviceFullCode": "340M202M1M259",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M37",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 260,
    "DeviceFullCode": "340M202M1M260",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M38",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 261,
    "DeviceFullCode": "340M202M1M261",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M38",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 262,
    "DeviceFullCode": "340M202M1M262",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M38",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 263,
    "DeviceFullCode": "340M202M1M263",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M38",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 264,
    "DeviceFullCode": "340M202M1M264",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M38",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 265,
    "DeviceFullCode": "340M202M1M265",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M38",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 266,
    "DeviceFullCode": "340M202M1M266",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M38",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 267,
    "DeviceFullCode": "340M202M1M267",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M39",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 268,
    "DeviceFullCode": "340M202M1M268",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M39",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 269,
    "DeviceFullCode": "340M202M1M269",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M39",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 270,
    "DeviceFullCode": "340M202M1M270",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M39",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 271,
    "DeviceFullCode": "340M202M1M271",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M39",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 272,
    "DeviceFullCode": "340M202M1M272",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M39",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 273,
    "DeviceFullCode": "340M202M1M273",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M39",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 274,
    "DeviceFullCode": "340M202M1M274",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M40",
    "Capacity": 30.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 275,
    "DeviceFullCode": "340M202M1M275",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M40",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 276,
    "DeviceFullCode": "340M202M1M276",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M40",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 277,
    "DeviceFullCode": "340M202M1M277",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M40",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 278,
    "DeviceFullCode": "340M202M1M278",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M40",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 279,
    "DeviceFullCode": "340M202M1M279",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M40",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 1,
    "DeviceCode": 280,
    "DeviceFullCode": "340M202M1M280",
    "DeviceModeFullCode": "340M202M1",
    "PDeviceFullCode": "340M201M1M40",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceCode": 281,
    "DeviceFullCode": "340M202M2M281",
    "DeviceModeFullCode": "340M202M2",
    "PDeviceFullCode": "340M201M1M41",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceCode": 282,
    "DeviceFullCode": "340M202M2M282",
    "DeviceModeFullCode": "340M202M2",
    "PDeviceFullCode": "340M201M1M41",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceCode": 283,
    "DeviceFullCode": "340M202M2M283",
    "DeviceModeFullCode": "340M202M2",
    "PDeviceFullCode": "340M201M1M41",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceCode": 284,
    "DeviceFullCode": "340M202M2M284",
    "DeviceModeFullCode": "340M202M2",
    "PDeviceFullCode": "340M201M1M41",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceCode": 285,
    "DeviceFullCode": "340M202M2M285",
    "DeviceModeFullCode": "340M202M2",
    "PDeviceFullCode": "340M201M1M41",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceCode": 286,
    "DeviceFullCode": "340M202M2M286",
    "DeviceModeFullCode": "340M202M2",
    "PDeviceFullCode": "340M201M1M41",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceCode": 287,
    "DeviceFullCode": "340M202M2M287",
    "DeviceModeFullCode": "340M202M2",
    "PDeviceFullCode": "340M201M1M41",
    "Capacity": 40.8000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceCode": 288,
    "DeviceFullCode": "340M202M2M288",
    "DeviceModeFullCode": "340M202M2",
    "PDeviceFullCode": "340M201M1M42",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceCode": 289,
    "DeviceFullCode": "340M202M2M289",
    "DeviceModeFullCode": "340M202M2",
    "PDeviceFullCode": "340M201M1M42",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceCode": 290,
    "DeviceFullCode": "340M202M2M290",
    "DeviceModeFullCode": "340M202M2",
    "PDeviceFullCode": "340M201M1M42",
    "Capacity": 71.4000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceCode": 291,
    "DeviceFullCode": "340M202M2M291",
    "DeviceModeFullCode": "340M202M2",
    "PDeviceFullCode": "340M201M1M42",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceCode": 292,
    "DeviceFullCode": "340M202M2M292",
    "DeviceModeFullCode": "340M202M2",
    "PDeviceFullCode": "340M201M1M42",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceCode": 293,
    "DeviceFullCode": "340M202M2M293",
    "DeviceModeFullCode": "340M202M2",
    "PDeviceFullCode": "340M201M1M42",
    "Capacity": 30.6000
  },
  {
    "DeviceTypeCode": 202,
    "DeviceModeCode": 2,
    "DeviceCode": 294,
    "DeviceFullCode": "340M202M2M294",
    "DeviceModeFullCode": "340M202M2",
    "PDeviceFullCode": "340M201M1M42",
    "Capacity": 81.6000
  },
  {
    "DeviceTypeCode": 203,
    "DeviceModeCode": 1,
    "DeviceCode": 1,
    "DeviceFullCode": "340M203M1M1",
    "DeviceModeFullCode": "340M203M1",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 203,
    "DeviceModeCode": 2,
    "DeviceCode": 2,
    "DeviceFullCode": "340M203M2M2",
    "DeviceModeFullCode": "340M203M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceCode": 1,
    "DeviceFullCode": "340M302M1M1",
    "DeviceModeFullCode": "340M302M1",
    "PDeviceFullCode": None,
    "Capacity": 10281.6000
  },
  {
    "DeviceTypeCode": 302,
    "DeviceModeCode": 1,
    "DeviceCode": 2,
    "DeviceFullCode": "340M302M1M2",
    "DeviceModeFullCode": "340M302M1",
    "PDeviceFullCode": None,
    "Capacity": 11342.4000
  },
  {
    "DeviceTypeCode": 307,
    "DeviceModeCode": 1,
    "DeviceCode": 1,
    "DeviceFullCode": "340M307M1M1",
    "DeviceModeFullCode": "340M307M1",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 1,
    "DeviceCode": 1,
    "DeviceFullCode": "340M505M1M1",
    "DeviceModeFullCode": "340M505M1",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 1,
    "DeviceCode": 2,
    "DeviceFullCode": "340M505M1M2",
    "DeviceModeFullCode": "340M505M1",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 1,
    "DeviceCode": 3,
    "DeviceFullCode": "340M505M1M3",
    "DeviceModeFullCode": "340M505M1",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 4,
    "DeviceFullCode": "340M505M2M4",
    "DeviceModeFullCode": "340M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 5,
    "DeviceFullCode": "340M505M2M5",
    "DeviceModeFullCode": "340M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 505,
    "DeviceModeCode": 2,
    "DeviceCode": 6,
    "DeviceFullCode": "340M505M2M6",
    "DeviceModeFullCode": "340M505M2",
    "PDeviceFullCode": None,
    "Capacity": None
  },
  {
    "DeviceTypeCode": 801,
    "DeviceModeCode": 1,
    "DeviceCode": 1,
    "DeviceFullCode": "340M801M1M1",
    "DeviceModeFullCode": "340M801M1",
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
        self.stationCode = 340
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
                    if deviceTypeCode==203 and deviceItem['DeviceFullCode']=="340M203M2M2":
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
