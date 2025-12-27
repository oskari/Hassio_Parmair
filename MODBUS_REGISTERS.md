# Parmair Ventilation Modbus Register Map

This document catalogs the Modbus holding registers used by the Parmair Ventilation Home Assistant integration. The addresses below use the zero-based offset expected by most Modbus client libraries (including `pymodbus`). Register IDs match the official Parmair documentation.

**Important**: Modbus addresses are offset by +1000 from the register ID (e.g., Register ID 20 → Address 1020).

## Currently Monitored Registers

These registers are actively polled by the integration:

| Register ID | Address (0-based) | Official ID | Symbol | Access | Scaling | Notes |
|------------:|------------------:|-------------|--------|--------|---------|-------|
| 208 | 1208 | POWER_BTN_FI | POWER_BTN | R/W | 1 | Power state (0=Off, 1=Stopping, 2=Starting, 3=Running). |
| 185 | 1185 | IV01_CONTROLSTATE_FO | CONTROL_STATE | R | 1 | Operating mode (STOP/AWAY/HOME/BOOST/etc.). |
| 187 | 1187 | IV01_SPEED_FOC | SPEED_CONTROL | R/W | 1 | Fan speed control (AUTO/STOP/1-5). |
| 20 | 1020 | TE01_M | FRESH_AIR_TEMP | R | 0.1°C | Outdoor/fresh air temperature. |
| 23 | 1023 | TE10_M | SUPPLY_TEMP | R | 0.1°C | Supply air temperature (indoors). |
| 24 | 1024 | TE30_M | EXHAUST_TEMP | R | 0.1°C | Exhaust air temperature (from rooms). |
| 25 | 1025 | TE31_M | WASTE_TEMP | R | 0.1°C | Waste air temperature (after heat exchange). |
| 60 | 1060 | TE30_S | EXHAUST_TEMP_SETPOINT | R/W | 0.1°C | Target exhaust temperature. |
| 65 | 1065 | TE10_S | SUPPLY_TEMP_SETPOINT | R/W | 0.1°C | Target supply temperature. |
| 104 | 1104 | HOME_SPEED_S | HOME_SPEED | R/W | 1 | Fan speed preset for Home mode (0-4). |
| 105 | 1105 | AWAY_SPEED_S | AWAY_SPEED | R/W | 1 | Fan speed preset for Away mode (0-4). |
| 117 | 1117 | BOOST_SETTING_S | BOOST_SETTING | R/W | 1 | Fan speed preset for Boost mode (2-4). |
| 200 | 1200 | HOME_STATE_FI | HOME_STATE | R | 1 | Home mode active (0=Away, 1=Home). |
| 201 | 1201 | BOOST_STATE_FI | BOOST_STATE | R | 1 | Boost mode active (0=Inactive, 1=Active). |
| 202 | 1202 | BOOST_TIMER_FM | BOOST_TIMER | R/W | minutes | Boost timer remaining time. |
| 180 | 1180 | MEXX_FM | HUMIDITY | R | % | Indoor humidity (65535=not installed). |
| 31 | 1031 | QE20_M | CO2 | R | ppm | Indoor CO₂ (65535=not installed). |
| 4 | 1004 | ALARM_COUNT | ALARM_COUNT | R | 1 | Number of active alarms. |
| 5 | 1005 | SUM_ALARM | SUM_ALARM | R | 1 | Summary alarm flag. |
| 244 | 1244 | VENT_MACHINE | VENT_MACHINE | R/W | 1 | Machine type code (for auto-detection). |
| 206 | 1206 | ALARMS_STATE_FI | ALARMS_STATE | R | 1 | Alarm state bitmask (0=OK, 1=Alarms, 2=Filter). |

## Complete Register Map

### System Settings (Registers 1-19)

| Register ID | Address | Official ID | Description | Access | Scale | Unit |
|------------:|--------:|-------------|-------------|--------|------:|------|
| 1 | 1000 | LANGUAGE | Language selection (0=Finnish, 1=English, 2=Swedish, 3=Estonian) | R/W | 1 | - |
| 2 | 1001 | FACTORY_SETTINGS | Factory reset (0=OK/Reset, 1=Reset settings) | R/W | 1 | - |
| 3 | 1002 | ACK_ALARMS | Alarm acknowledgment (0=Waiting, 1=OK/Acknowledge) | R/W | 1 | - |
| 4 | 1003 | ALARM_COUNT | Number of active alarms | R | 1 | - |
| 5 | 1004 | SUM_ALARM | Summary alarm (0=No alarms, 1=Alarm active) | R | 1 | - |
| 6 | 1005 | ALARM_SOUND | Alarm sound (0=Disabled, 1=Enabled) | R/W | 1 | - |
| 7 | 1006 | DISPLAY_BRIGHTNESS | Display brightness (0-5 = 10-40%) | R/W | 1 | - |
| 10 | 1009 | TIME_DAYOFWEEK | Day of week | R/W | 1 | - |
| 11 | 1010 | TIME_YEAR | Year | R/W | 1 | - |
| 12 | 1011 | TIME_MONTH | Month | R/W | 1 | - |
| 13 | 1012 | TIME_DAY | Day | R/W | 1 | - |
| 14 | 1013 | TIME_HOUR | Hours | R/W | 1 | - |
| 15 | 1014 | TIME_MIN | Minutes | R/W | 1 | - |
| 16 | 1015 | SETUP_STATE | Setup state (0=Not setup, 1=Setup ongoing, 2=Setup complete) | R/W | 1 | - |
| 17 | 1016 | MULTI_FW_VER | Multi24 firmware version | R | 100 | - |
| 18 | 1017 | MULTI_SW_VER | Multi24 software version | R | 100 | - |
| 19 | 1018 | MULTI_BL_VER | Multi24 bootloader version | R | 100 | - |

### Physical Inputs (Registers 20-38)

| Register ID | Address | Official ID | Description | Access | Scale | Unit |
|------------:|--------:|-------------|-------------|--------|------:|------|
| 20 | 1019 | TE01_M | Fresh air temperature measurement | R | 10 | °C |
| 21 | 1020 | TE01_MC | Fresh air temp control mode (0=Auto, 1=Manual) | R/W | 1 | - |
| 22 | 1021 | TE05_M | Supply air temp after heat recovery | R | 10 | °C |
| 23 | 1022 | TE10_M | Supply air temperature | R | 10 | °C |
| 24 | 1023 | TE30_M | Exhaust air temperature | R | 10 | °C |
| 25 | 1024 | TE31_M | Waste air temperature | R | 10 | °C |
| 26 | 1025 | ME05_M | Humidity measurement at heat recovery unit | R | 1 | % |
| 27 | 1026 | QEBOOST_I | Humidity/CO2 sensor boost switch indication | R | 1 | - |
| 28 | 1027 | TF10_I | Supply fan indication | R | 1 | - |
| 29 | 1028 | PF30_I | Exhaust fan indication | R | 1 | - |
| 30 | 1029 | ME20_M | Humidity measurement, wet room | R | 1 | %Rh |
| 31 | 1030 | QE20_M | CO2 measurement, indoor air | R | 1 | ppm |
| 32 | 1031 | EXTERNAL_M | External control signal (0-10V) | R | 10 | % |
| 33 | 1032 | HOME_SWITCH_I | Home/Away switch indication | R | 1 | - |
| 34 | 1033 | TK01_I | Fireplace switch indication (overpressure) | R | 1 | - |
| 35 | 1034 | BOOST_SWITCH_I | Boost switch indication | R | 1 | - |
| 36 | 1035 | EXTERNAL_BOOST_M | External boost signal (1-10V) | R | 10 | % |
| 37 | 1036 | TE10_DEFLECTION_M | Supply temp deviation (+/- 3 degrees) | R | 10 | °C |
| 38 | 1037 | TE45_M | Post-heater return water temperature | R | 10 | °C |

### Physical Outputs (Registers 40-50)

| Register ID | Address | Official ID | Description | Access | Scale | Unit |
|------------:|--------:|-------------|-------------|--------|------:|------|
| 40 | 1039 | TF10_Y | Supply fan control | R/W | 10 | % |
| 41 | 1040 | TF10_YC | Supply fan control mode (0=Auto, 1=Manual) | R/W | 1 | - |
| 42 | 1041 | PF30_Y | Exhaust fan control | R/W | 10 | % |
| 43 | 1042 | PF30_YC | Exhaust fan control mode (0=Auto, 1=Manual) | R/W | 1 | - |
| 44 | 1043 | TV45_Y | Post-heater actuator control | R/W | 10 | % |
| 45 | 1044 | TV45_YC | Post-heater control mode (0=Auto, 1=Manual) | R/W | 1 | - |
| 46 | 1045 | FG50_Y | Heat recovery control | R/W | 10 | % |
| 47 | 1046 | FG50_YC | Heat recovery control mode (0=Auto, 1=Manual) | R/W | 1 | - |
| 48 | 1047 | EC05_Y | Pre-heater control | R | 10 | % |
| 49 | 1048 | EC05_YC | Pre-heater control mode (0=Auto, 1=Manual) | R/W | 1 | - |
| 50 | 1049 | JH01_O | Relay alarm output (summary alarm) | R/W | 1 | - |

### Settings (Registers 60-129)

| Register ID | Address | Official ID | Description | Access | Scale | Unit |
|------------:|--------:|-------------|-------------|--------|------:|------|
| 60 | 1059 | TE30_S | Exhaust temperature setpoint | R/W | 10 | °C |
| 61 | 1060 | TE45_LA_S | Post-heater return water freeze alarm limit | R/W | 10 | °C |
| 62 | 1061 | TE45_ANTICIPATION_S | Post-heater freeze anticipation | R/W | 10 | °C |
| 65 | 1064 | TE10_S | Supply temperature setpoint | R/W | 10 | °C |
| 66 | 1065 | TE10_P1_S | P-band for supply temp control, step 1 | R/W | 10 | °C |
| 67 | 1066 | TE10_P2_S | P-band for supply temp control, step 2 | R/W | 1 | °C |
| 68 | 1067 | TE10_P3_S | P-band for supply temp control, step 3 | R/W | 10 | °C |
| 69 | 1068 | TE10_P4_S | P-band for supply temp control, step 4 | R/W | 10 | °C |
| 71 | 1070 | TE10_I_S | I-time for supply temp control | R/W | 1 | s |
| 72 | 1071 | BST_MAXTIME | Boost maximum time | R/W | 1 | min |
| 73 | 1072 | BST_MINTIME | Boost minimum time | R/W | 1 | min |
| 74 | 1073 | BST_BREAKTIME | Boost break time | R/W | 1 | min |
| 78 | 1077 | SUMMER_MODE_TE01_LIMIT | Heat recovery summer mode outdoor temp limit | R/W | 10 | °C |
| 79 | 1078 | SUMMER_MODE_S | Heat recovery summer mode enable | R/W | 1 | - |
| 80 | 1079 | BST_TE01_LIMIT | Boost outdoor temperature limit | R/W | 10 | °C |
| 82 | 1081 | FG50_DFRST_Y | Heat recovery defrost position | R/W | 1 | % |
| 83 | 1082 | FG50_TE01_LIMIT | Heat recovery heating control outdoor temp limit | R/W | 10 | °C |
| 84 | 1083 | FG50_DRVTIME_S | Heat recovery actuator drive time | R/W | 1 | s |
| 85 | 1084 | FILTER_INTERVAL_S | Filter change interval (0=3mo, 1=4mo, 2=6mo) | R/W | 1 | - |
| 86 | 1085 | FILTER_DAY | Filter last change day | R/W | 1 | - |
| 87 | 1086 | FILTER_MONTH | Filter last change month | R/W | 1 | - |
| 88 | 1087 | FILTER_YEAR | Filter last change year | R/W | 1 | - |
| 89 | 1088 | FILTERNEXT_DAY | Filter next change day | R/W | 1 | - |
| 90 | 1089 | FILTERNEXT_MONTH | Filter next change month | R/W | 1 | - |
| 91 | 1090 | FILTERNEXT_YEAR | Filter next change year | R/W | 1 | - |
| 92 | 1091 | QE30_MIN_S | CO2 minimum limit (boost starts) | R/W | 1 | ppm |
| 93 | 1092 | QE30_MAX_S | CO2 maximum limit (boost maximum) | R/W | 1 | ppm |
| 96 | 1095 | HRU_START_TE_FS | Heat recovery defrost start limit (calculated) | R | 10 | °C |
| 97 | 1096 | HRU_START_EFF_S | Efficiency lower limit for defrost start | R/W | 1 | % |
| 98 | 1097 | HRU_STOP_TE_S | Heat recovery defrost stop limit (waste air) | R/W | 10 | °C |
| 99 | 1098 | DFRST_IDLETIME_S | Heat recovery defrost idle time between cycles | R/W | 1 | min |
| 100 | 1099 | DFRST_MINTIME_S | Heat recovery defrost minimum time | R/W | 1 | min |
| 101 | 1100 | DFRST_MAXTIME_S | Heat recovery defrost maximum time | R/W | 1 | min |
| 102 | 1101 | HRU_START_TE_S | Heat recovery defrost start limit (waste air) | R/W | 10 | °C |
| 103 | 1102 | SP45_POSTRUN_T | Electric heater post-ventilation time | R/W | 1 | s |
| 104 | 1103 | HOME_SPEED_S | Ventilation speed preset for Home mode | R/W | 1 | - |
| 105 | 1104 | AWAY_SPEED_S | Ventilation speed preset for Away mode | R/W | 1 | - |
| 106 | 1105 | BOOST_TIME_S | Boost time setting (30/60/90/120/180 min) | R/W | 1 | - |
| 107 | 1106 | OVERP_TIME_S | Overpressure time setting (15/30/45/60/120 min) | R/W | 1 | - |
| 108 | 1107 | TP_ENABLE_S | Time program enable (0=Disabled, 1=Enabled) | R/W | 1 | - |
| 109 | 1108 | HEATER_ENABLE_S | Post-heater enable (0=Disabled, 1=Enabled) | R/W | 1 | - |
| 110 | 1109 | SF_SPEEDRATIO_S | Supply fan speed ratio | R/W | 1 | % |
| 111 | 1110 | EF_SPEEDRATIO_S | Exhaust fan speed ratio | R/W | 1 | % |
| 112 | 1111 | SF_SPEEDRATIO2_S | Supply fan speed ratio for overpressure | R/W | 1 | % |
| 113 | 1112 | EF_SPEEDRATIO2_S | Exhaust fan speed ratio for overpressure | R/W | 1 | % |
| 114 | 1113 | ME05_BOOSTSTART_S | Heat recovery RH% boost start threshold | R/W | 1 | % |
| 115 | 1114 | ME05_DISP_S | Heat recovery RH% boost range size | R/W | 1 | % |
| 116 | 1115 | HRU_TEMPCONTROL_S | Heat recovery temp control enable | R/W | 1 | - |
| 117 | 1116 | BOOST_SETTING_S | Boost speed setting (2-4 = speed 3-5) | R/W | 1 | - |
| 120 | 1119 | FAN_SPEED1_S | Fan speed setting 1 | R/W | 1 | % |
| 121 | 1120 | FAN_SPEED2_S | Fan speed setting 2 | R/W | 1 | % |
| 122 | 1121 | FAN_SPEED3_S | Fan speed setting 3 | R/W | 1 | % |
| 123 | 1122 | FAN_SPEED4_S | Fan speed setting 4 | R/W | 1 | % |
| 124 | 1123 | FAN_SPEED5_S | Fan speed setting 5 | R/W | 1 | % |
| 125 | 1124 | SERVICECODE_OK | Service code acceptance | R | 1 | - |
| 126 | 1125 | SERVICECODE_1 | Entered service code (auto-resets to 0) | R/W | 1 | - |
| 127 | 1126 | SERVICECODE_2 | Correct service code value (encrypted) | R/W | 1 | - |
| 128 | 1127 | SERVICECODE_SET | New service code setup (0=Normal, 1=Enter old, 2=Set new) | R/W | 1 | - |
| 129 | 1128 | SERVICECODE_CHECK | Service code check (1=Check, 2=Confirm new) | R/W | 1 | - |

### Time Programs (Registers 130-150)

Weekly time programs stored as bitmasks (each bit represents one hour).

| Register ID | Address | Official ID | Description | Access |
|------------:|--------:|-------------|-------------|--------|
| 130 | 1129 | TP_DAY1_HOURS1 | Time program Day 1, hours 00-07 | R/W |
| 131 | 1130 | TP_DAY1_HOURS2 | Time program Day 1, hours 08-15 | R/W |
| 132 | 1131 | TP_DAY1_HOURS3 | Time program Day 1, hours 16-23 | R/W |
| 133 | 1132 | TP_DAY2_HOURS1 | Time program Day 2, hours 00-07 | R/W |
| 134 | 1133 | TP_DAY2_HOURS2 | Time program Day 2, hours 08-15 | R/W |
| 135 | 1134 | TP_DAY2_HOURS3 | Time program Day 2, hours 16-23 | R/W |
| 136 | 1135 | TP_DAY3_HOURS1 | Time program Day 3, hours 00-07 | R/W |
| 137 | 1136 | TP_DAY3_HOURS2 | Time program Day 3, hours 08-15 | R/W |
| 138 | 1137 | TP_DAY3_HOURS3 | Time program Day 3, hours 16-23 | R/W |
| 139 | 1138 | TP_DAY4_HOURS1 | Time program Day 4, hours 00-07 | R/W |
| 140 | 1139 | TP_DAY4_HOURS2 | Time program Day 4, hours 08-15 | R/W |
| 141 | 1140 | TP_DAY4_HOURS3 | Time program Day 4, hours 16-23 | R/W |
| 142 | 1141 | TP_DAY5_HOURS1 | Time program Day 5, hours 00-07 | R/W |
| 143 | 1142 | TP_DAY5_HOURS2 | Time program Day 5, hours 08-15 | R/W |
| 144 | 1143 | TP_DAY5_HOURS3 | Time program Day 5, hours 16-23 | R/W |
| 145 | 1144 | TP_DAY6_HOURS1 | Time program Day 6, hours 00-07 | R/W |
| 146 | 1145 | TP_DAY6_HOURS2 | Time program Day 6, hours 08-15 | R/W |
| 147 | 1146 | TP_DAY6_HOURS3 | Time program Day 6, hours 16-23 | R/W |
| 148 | 1147 | TP_DAY7_HOURS1 | Time program Day 7, hours 00-07 | R/W |
| 149 | 1148 | TP_DAY7_HOURS2 | Time program Day 7, hours 08-15 | R/W |
| 150 | 1149 | TP_DAY7_HOURS3 | Time program Day 7, hours 16-23 | R/W |

### Soft Measurements and Control Points (Registers 180-210)

Virtual/calculated measurements and control points.

| Register ID | Address | Official ID | Description | Access | Scale | Unit |
|------------:|--------:|-------------|-------------|--------|------:|------|
| 180 | 1179 | MEXX_FM | Humidity measurement, main display | R | 1 | %Rh |
| 181 | 1180 | TE10_FS | Virtual setpoint, supply air temperature | R/W | 10 | °C |
| 182 | 1181 | TE10_FSC | Virtual setpoint control mode (0=Auto, 1=Manual) | R/W | 1 | - |
| 183 | 1182 | DFRST_FI | Virtual indication, heat recovery defrost on/off | R | 1 | - |
| 184 | 1183 | IV01_STATE_FO | Virtual control, ventilation operating point | R | 1 | - |
| 185 | 1184 | IV01_CONTROLSTATE_FO | Virtual control, ventilation run control (0-9) | R/W | 1 | - |
| 186 | 1185 | IV01_SPEED_FO | Virtual control, ventilation speed control (0-5) | R | 1 | - |
| 187 | 1186 | IV01_SPEED_FOC | Virtual control mode, ventilation speed (0-6) | R/W | 1 | - |
| 188 | 1187 | IV01_TEMP_FO | Virtual control, ventilation temp control (0-3) | R | 1 | - |
| 189 | 1188 | IV01_SPEED2_FO | Virtual control, ventilation speed auto/manual (0-23) | R | 1 | - |
| 190 | 1189 | FG50_EA_M | Virtual measurement, heat recovery efficiency | R | 10 | % |
| 191 | 1190 | PWR_LIMIT_FY | Virtual control, fan power limit | R | 10 | % |
| 192 | 1191 | ME05_AVG_FM | Virtual measurement, heat recovery 24h avg humidity | R | 10 | % |
| 193 | 1192 | BST_TIMER_FM | Virtual measurement, boost timer time | R | 1 | min |
| 194 | 1193 | DFRST_CYCLE_FI | Virtual indication, heat recovery defrost cycle number | R | 1 | - |
| 200 | 1199 | HOME_STATE_FI | Virtual indication (0=Away, 1=Home) | R | 1 | - |
| 201 | 1200 | BOOST_STATE_FI | Virtual indication, boost active | R | 1 | - |
| 202 | 1201 | BOOST_TIMER_FM | Virtual measurement, boost timer time | R/W | 1 | min |
| 203 | 1202 | OVERP_STATE_FI | Virtual setting, overpressure active | R | 1 | - |
| 204 | 1203 | OVERP_TIMER_FM | Virtual measurement, overpressure timer time | R/W | 1 | min |
| 205 | 1204 | FILTER_STATE_FI | Virtual setting, filter status (0=Replace, 1=Ack/Replaced) | R/W | 1 | - |
| 206 | 1205 | ALARMS_STATE_FI | Virtual status, alarm state (0=OK, 1=Alarms, 2=Filter dirty) | R | 1 | - |
| 207 | 1206 | IO_INITIALIZED_FI | Virtual status, I/O initialized (0=Not init, 1=Initialized) | R | 1 | - |
| 208 | 1207 | POWER_BTN_FI | Unit shutdown (0=Off, 1=Stopping, 2=Starting, 3=Running) | R/W | 1 | - |
| 209 | 1208 | POSTV_TIMER_FM | Post-ventilation timer time | R | 1 | s |
| 210 | 1209 | CLEAR_WEEKCLOCK | Clear weekly time program (1=Clear) | R/W | 1 | - |

### Alarms (Registers 220-238)

Alarm states for various sensors and components.

| Register ID | Address | Official ID | Description | Access |
|------------:|--------:|-------------|-------------|--------|
| 220 | 1219 | TE01_FA | Fresh air temperature sensor fault alarm | R |
| 221 | 1220 | TE10_FA | Supply air temperature sensor fault alarm | R |
| 222 | 1221 | TE05_FA | Supply air temp after heat recovery sensor fault | R |
| 223 | 1222 | TE30_FA | Exhaust air temperature sensor fault alarm | R |
| 224 | 1223 | TE31_FA | Waste air temperature sensor fault alarm | R |
| 225 | 1224 | ME05_FA | Heat recovery humidity sensor fault alarm | R |
| 226 | 1225 | TF10_CA | Supply fan conflict alarm | R |
| 227 | 1226 | PF30_CA | Exhaust fan conflict alarm | R |
| 228 | 1227 | TE10_HA | Supply air temperature high limit alarm | R |
| 229 | 1228 | TE30_HA | Exhaust air temperature high limit alarm | R |
| 230 | 1229 | TE10_LA | Supply air temperature low limit alarm | R |
| 231 | 1230 | FILTER_FA | Filter alarm | R |
| 232 | 1231 | TE45_LA | Post-heater return water low limit alarm | R |
| 238 | 1237 | TE45_FA | Post-heater return water sensor fault alarm | R |

### Configuration Parameters (Registers 240-245)

System configuration parameters.

| Register ID | Address | Official ID | Description | Access | Notes |
|------------:|--------:|-------------|-------------|--------|-------|
| 240 | 1239 | HEAT_RADIATOR_TYPE | Heater type (0=Water, 1=Electric) | R/W | - |
| 241 | 1240 | RECOVERY_TYPE | Heat recovery type (0=Rotary, 1=Cube) | R/W | - |
| 242 | 1241 | M10_SENSORTYPE | M10 sensor type (0=None, 1=CO2, 2=Humidity) | R/W | - |
| 243 | 1242 | M12_USAGE | M12 usage mode (0=Empty, 1=Home/Away, 2=Overpressure, 3=Boost switch, 4=Boost 0-10V, 5=Supply temp deviation) | R/W | - |
| 244 | 1243 | VENT_MACHINE | Ventilation unit type number (e.g., 80=MAC 80) | R/W | Used for auto-detection |
| 245 | 1244 | M11_POTENTIOMETER_PRIORITY | M11 remote control 0-10V priority (0=Low/boosts allowed, 1=High/bypass boosts) | R/W | - |

## Operating Modes

`CONTROL_STATE` (register 185 / address 184) reports the current operating mode:

| Value | Mode |
|------:|------|
| 0 | Stop |
| 1 | Away |
| 2 | Home |
| 3 | Boost |
| 4 | Overpressure |
| 5 | Away (timer) |
| 6 | Home (timer) |
| 7 | Boost (timer) |
| 8 | Overpressure (timer) |
| 9 | Manual |

## Fan Speed Control

`SPEED_CONTROL` (register 187 / address 186) accepts the following values:

| Value | Description |
|------:|-------------|
| 0 | Auto |
| 1 | Stop |
| 2 | Speed 1 |
| 3 | Speed 2 |
| 4 | Speed 3 |
| 5 | Speed 4 |
| 6 | Speed 5 |

## Scaling and Units

- Temperatures use a scale factor of 10 (e.g., raw value 210 equals 21.0 °C).
- Fan speed presets (`HOME_SPEED`, `AWAY_SPEED`, `BOOST_SETTING`) are stored as 0-100 percentages.
- Humidity is expressed directly in percent, CO₂ in parts per million, timers in minutes.

## Access Notes

- All registers listed here are holding registers. Read operations use Modbus function code 03; writes use function codes 06 (single register) or 16 (multiple registers).
- Values marked **R/W** can be safely written when the device is reachable; **R** entries should be treated as read-only status information.
- Optional sensors (humidity, CO₂) may return negative values if the hardware module is not installed.

Use this register map as the authoritative reference when extending or troubleshooting the integration.
