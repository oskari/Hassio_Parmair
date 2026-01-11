"""Constants and register metadata for the Parmair integration."""

from __future__ import annotations

from dataclasses import dataclass

DOMAIN = "parmair"

# Configuration
CONF_SLAVE_ID = "slave_id"
CONF_SCAN_INTERVAL = "scan_interval"
CONF_SOFTWARE_VERSION = "software_version"
CONF_HEATER_TYPE = "heater_type"

DEFAULT_NAME = "Parmair MAC"
DEFAULT_SCAN_INTERVAL = 30  # seconds
DEFAULT_PORT = 502
DEFAULT_SLAVE_ID = 1

# Software versions
SOFTWARE_VERSION_1 = "1.x"
SOFTWARE_VERSION_2 = "2.x"
SOFTWARE_VERSION_UNKNOWN = "unknown"

# Heater types (from HEAT_RADIATOR_TYPE register 1240)
# 0 = Water heater (Vesipatteri)
# 1 = Electric heater (Sähköpatteri)
# 2 = No heater
HEATER_TYPE_WATER = 0
HEATER_TYPE_ELECTRIC = 1
HEATER_TYPE_NONE = 2
HEATER_TYPE_UNKNOWN = -1


@dataclass(frozen=True)
class RegisterDefinition:
    """Describe a Modbus holding register used by the integration."""

    key: str
    address: int  # zero-based address expected by pymodbus
    label: str
    scale: float = 1.0
    writable: bool = False
    optional: bool = False
    description: str | None = None

    @property
    def register_id(self) -> int:
        """Return the register ID (Address - 1000 = Register ID)."""

        return self.address - 1000


# Register keys
REG_HARDWARE_TYPE = "hardware_type"
REG_SOFTWARE_VERSION = "software_version"
REG_POWER = "power"
REG_CONTROL_STATE = "control_state"
REG_ACTUAL_SPEED = "actual_speed"
REG_SPEED_CONTROL = "speed_control"
REG_FRESH_AIR_TEMP = "fresh_air_temp"
REG_SUPPLY_AFTER_RECOVERY_TEMP = "supply_after_recovery_temp"
REG_SUPPLY_TEMP = "supply_temp"
REG_EXHAUST_TEMP = "exhaust_temp"
REG_WASTE_TEMP = "waste_temp"
REG_EXHAUST_TEMP_SETPOINT = "exhaust_temp_setpoint"
REG_SUPPLY_TEMP_SETPOINT = "supply_temp_setpoint"
REG_HOME_SPEED = "home_speed"
REG_AWAY_SPEED = "away_speed"
REG_BOOST_SETTING = "boost_setting"
REG_HOME_STATE = "home_state"
REG_BOOST_STATE = "boost_state"
REG_BOOST_TIMER = "boost_timer"
REG_OVERPRESSURE_STATE = "overpressure_state"
REG_OVERPRESSURE_TIMER = "overpressure_timer"
REG_HUMIDITY = "humidity"
REG_HUMIDITY_24H_AVG = "humidity_24h_avg"
REG_CO2 = "co2"
REG_ALARM_COUNT = "alarm_count"
REG_SUM_ALARM = "sum_alarm"
REG_ALARMS_STATE = "alarms_state"

# Switch register keys
REG_SUMMER_MODE = "summer_mode"
REG_TIME_PROGRAM_ENABLE = "time_program_enable"
REG_HEATER_ENABLE = "heater_enable"

# V2 specific sensor register keys
REG_SEASON_STATE = "season_state"  # V2 only: 0=Winter, 1=Transition, 2=Summer

# V2 additional register keys (documented in V2 PDF)
REG_TIME_YEAR = "time_year"
REG_TIME_MONTH = "time_month"
REG_TIME_DAY = "time_day"
REG_TIME_HOUR = "time_hour"
REG_TIME_MIN = "time_min"
REG_FIRMWARE_VERSION = "firmware_version"
REG_BOOTLOADER_VERSION = "bootloader_version"
REG_EXHAUST_CO2 = "exhaust_co2"
REG_SUPPLY_FAN_INDICATOR = "supply_fan_indicator"
REG_EXHAUST_FAN_INDICATOR = "exhaust_fan_indicator"
REG_WET_ROOM_HUMIDITY = "wet_room_humidity"
REG_EXTERNAL_SIGNAL = "external_signal"
REG_EXTERNAL_BOOST_SIGNAL = "external_boost_signal"
REG_TEMP_DEFLECTION = "temp_deflection"
REG_POST_HEATER_OUTPUT = "post_heater_output"
REG_HEAT_RECOVERY_OUTPUT = "heat_recovery_output"
REG_PRE_HEATER_OUTPUT = "pre_heater_output"
REG_HEAT_PUMP_OUTPUT = "heat_pump_output"
REG_TEMP_CONTROL_MODE = "temp_control_mode"
REG_AWAY_TEMP_SETPOINT = "away_temp_setpoint"
REG_OVERPRESSURE_AMOUNT = "overpressure_amount"
REG_AUTO_SUMMER_POWER = "auto_summer_power"
REG_AUTO_COLD_LOWSPEED = "auto_cold_lowspeed"
REG_COLD_LOWSPEED_LIMIT = "cold_lowspeed_limit"
REG_AUTO_HUMIDITY_BOOST = "auto_humidity_boost"
REG_HUMIDITY_BOOST_SENSITIVITY = "humidity_boost_sensitivity"
REG_HUMIDITY_BOOST_TEMP_LIMIT = "humidity_boost_temp_limit"
REG_AUTO_CO2_BOOST = "auto_co2_boost"
REG_AUTO_HOME_AWAY = "auto_home_away"
REG_CO2_HOME_THRESHOLD = "co2_home_threshold"
REG_CO2_BOOST_THRESHOLD = "co2_boost_threshold"
REG_HP_RAD_MODE = "hp_rad_mode"
REG_HP_RAD_WINTER = "hp_rad_winter"
REG_HP_RAD_SUMMER = "hp_rad_summer"
REG_HEATING_SEASON_AVERAGE = "heating_season_average"
REG_HEATING_SEASON_MOMENT = "heating_season_moment"
REG_SUMMER_TEMP_SETPOINT = "summer_temp_setpoint"
REG_SUPPLY_TEMP_MAX = "supply_temp_max"
REG_BOOST_TEMP_LIMIT = "boost_temp_limit"
REG_SENSOR_TEMP_CORRECTION = "sensor_temp_correction"
REG_SENSOR_HUMIDITY_CORRECTION = "sensor_humidity_correction"
REG_SENSOR_CO2_CORRECTION = "sensor_co2_correction"
REG_SUPPLY_TEMP_MIN = "supply_temp_min"
REG_SUPPLY_TEMP_BASE = "supply_temp_base"
REG_BOOST_MIN_TIME = "boost_min_time"
REG_CO2_MIN_TIME = "co2_min_time"
REG_BOOST_TIME_LIMIT = "boost_time_limit"
REG_SENSOR_STATUS = "sensor_status"
REG_SUMMER_POWER_CHANGE = "summer_power_change"
REG_CALCULATED_HUMIDITY = "calculated_humidity"
REG_POWER_LIMIT = "power_limit"
REG_OUTDOOR_TEMP_AVG = "outdoor_temp_avg"
# Alarm registers
REG_ALARM_TE01 = "alarm_te01"
REG_ALARM_TE10 = "alarm_te10"
REG_ALARM_TE05 = "alarm_te05"
REG_ALARM_TE30 = "alarm_te30"
REG_ALARM_TE31 = "alarm_te31"
REG_ALARM_ME05 = "alarm_me05"
REG_ALARM_TF10 = "alarm_tf10"
REG_ALARM_PF30 = "alarm_pf30"
REG_ALARM_TE10_HIGH = "alarm_te10_high"
REG_ALARM_TE30_HIGH = "alarm_te30_high"
REG_ALARM_TE10_LOW = "alarm_te10_low"
REG_ALARM_FILTER = "alarm_filter"
# Speed settings (configuration)
REG_SF_SPEED1 = "sf_speed1"
REG_SF_SPEED2 = "sf_speed2"
REG_SF_SPEED3 = "sf_speed3"
REG_SF_SPEED4 = "sf_speed4"
REG_SF_SPEED5 = "sf_speed5"
REG_EF_SPEED1 = "ef_speed1"
REG_EF_SPEED2 = "ef_speed2"
REG_EF_SPEED3 = "ef_speed3"
REG_EF_SPEED4 = "ef_speed4"
REG_EF_SPEED5 = "ef_speed5"
REG_M10_TYPE = "m10_type"
REG_M11_TYPE = "m11_type"
REG_M12_TYPE = "m12_type"

# Predefined settings register keys
REG_BOOST_TIME_SETTING = "boost_time_setting"
REG_OVERPRESSURE_TIME_SETTING = "overpressure_time_setting"
REG_SUMMER_MODE_TEMP_LIMIT = "summer_mode_temp_limit"

# Button register keys
REG_ACKNOWLEDGE_ALARMS = "acknowledge_alarms"
REG_FILTER_REPLACED = "filter_replaced"

# Select register keys
REG_HEATER_TYPE = "heater_type"

# Additional number register keys
REG_FILTER_INTERVAL = "filter_interval"

# Additional sensor register keys
REG_HEAT_RECOVERY_EFFICIENCY = "heat_recovery_efficiency"
REG_DEFROST_STATE = "defrost_state"
REG_SUPPLY_FAN_SPEED = "supply_fan_speed"
REG_EXHAUST_FAN_SPEED = "exhaust_fan_speed"
REG_FILTER_STATE = "filter_state"
REG_FILTER_DAY = "filter_day"
REG_FILTER_MONTH = "filter_month"
REG_FILTER_YEAR = "filter_year"
REG_FILTER_NEXT_DAY = "filter_next_day"
REG_FILTER_NEXT_MONTH = "filter_next_month"
REG_FILTER_NEXT_YEAR = "filter_next_year"


def _build_registers_v1() -> dict[str, RegisterDefinition]:
    """Build the complete register map for Parmair MAC devices with software version 1.xx.

    This is the current register map from the CSV documentation.
    """

    return {
        REG_HARDWARE_TYPE: RegisterDefinition(REG_HARDWARE_TYPE, 1244, "VENT_MACHINE"),
        REG_SOFTWARE_VERSION: RegisterDefinition(REG_SOFTWARE_VERSION, 1018, "MULTI_SW_VER", scale=0.01),
        REG_POWER: RegisterDefinition(REG_POWER, 1208, "POWER_BTN_FI", writable=True),
        REG_CONTROL_STATE: RegisterDefinition(
            REG_CONTROL_STATE, 1185, "IV01_CONTROLSTATE_FO", writable=True
        ),
        REG_ACTUAL_SPEED: RegisterDefinition(
            REG_ACTUAL_SPEED, 1186, "IV01_SPEED_FO"
        ),
        REG_SPEED_CONTROL: RegisterDefinition(
            REG_SPEED_CONTROL, 1187, "IV01_SPEED_FOC", writable=True
        ),
        REG_FRESH_AIR_TEMP: RegisterDefinition(
            REG_FRESH_AIR_TEMP, 1020, "TE01_M", scale=0.1
        ),
        REG_SUPPLY_AFTER_RECOVERY_TEMP: RegisterDefinition(
            REG_SUPPLY_AFTER_RECOVERY_TEMP, 1022, "TE05_M", scale=0.1
        ),
        REG_SUPPLY_TEMP: RegisterDefinition(
            REG_SUPPLY_TEMP, 1023, "TE10_M", scale=0.1
        ),
        REG_EXHAUST_TEMP: RegisterDefinition(
            REG_EXHAUST_TEMP, 1024, "TE30_M", scale=0.1
        ),
        REG_WASTE_TEMP: RegisterDefinition(
            REG_WASTE_TEMP, 1025, "TE31_M", scale=0.1
        ),
        REG_EXHAUST_TEMP_SETPOINT: RegisterDefinition(
            REG_EXHAUST_TEMP_SETPOINT, 1060, "TE30_S", scale=0.1, writable=True
        ),
        REG_SUPPLY_TEMP_SETPOINT: RegisterDefinition(
            REG_SUPPLY_TEMP_SETPOINT, 1065, "TE10_S", scale=0.1, writable=True
        ),
        REG_HOME_SPEED: RegisterDefinition(
            REG_HOME_SPEED, 1104, "HOME_SPEED_S", writable=True
        ),
        REG_AWAY_SPEED: RegisterDefinition(
            REG_AWAY_SPEED, 1105, "AWAY_SPEED_S", writable=True
        ),
        REG_BOOST_SETTING: RegisterDefinition(
            REG_BOOST_SETTING, 1117, "BOOST_SETTING_S", writable=True
        ),
        REG_HOME_STATE: RegisterDefinition(
            REG_HOME_STATE, 1200, "HOME_STATE_FI"
        ),
        REG_BOOST_STATE: RegisterDefinition(
            REG_BOOST_STATE, 1201, "BOOST_STATE_FI"
        ),
        REG_BOOST_TIMER: RegisterDefinition(
            REG_BOOST_TIMER, 1202, "BOOST_TIMER_FM", writable=True
        ),
        REG_OVERPRESSURE_STATE: RegisterDefinition(
            REG_OVERPRESSURE_STATE, 1203, "OVERP_STATE_FI"
        ),
        REG_OVERPRESSURE_TIMER: RegisterDefinition(
            REG_OVERPRESSURE_TIMER, 1204, "OVERP_TIMER_FM", writable=True
        ),
        REG_HUMIDITY: RegisterDefinition(
            REG_HUMIDITY, 1180, "MEXX_FM", optional=True
        ),
        REG_HUMIDITY_24H_AVG: RegisterDefinition(
            REG_HUMIDITY_24H_AVG, 1192, "ME05_AVG_FM", scale=0.1, optional=True
        ),
        REG_CO2: RegisterDefinition(
            REG_CO2, 1031, "QE20_M", optional=True
        ),
        REG_ALARM_COUNT: RegisterDefinition(
            REG_ALARM_COUNT, 1004, "ALARM_COUNT"
        ),
        REG_SUM_ALARM: RegisterDefinition(
            REG_SUM_ALARM, 1005, "SUM_ALARM"
        ),
        REG_ALARMS_STATE: RegisterDefinition(
            REG_ALARMS_STATE, 1206, "ALARMS_STATE_FI"
        ),
        REG_SUMMER_MODE: RegisterDefinition(
            REG_SUMMER_MODE, 1079, "SUMMER_MODE_S", writable=True
        ),
        REG_TIME_PROGRAM_ENABLE: RegisterDefinition(
            REG_TIME_PROGRAM_ENABLE, 1108, "TP_ENABLE_S", writable=True
        ),
        REG_HEATER_ENABLE: RegisterDefinition(
            REG_HEATER_ENABLE, 1109, "HEATER_ENABLE_S", writable=True
        ),
        # Button registers
        REG_ACKNOWLEDGE_ALARMS: RegisterDefinition(
            REG_ACKNOWLEDGE_ALARMS, 1003, "ACK_ALARMS", writable=True
        ),
        REG_FILTER_REPLACED: RegisterDefinition(
            REG_FILTER_REPLACED, 1205, "FILTER_STATE_FI", writable=True
        ),
        # Select registers
        REG_HEATER_TYPE: RegisterDefinition(
            REG_HEATER_TYPE, 1240, "HEAT_RADIATOR_TYPE", writable=True
        ),
        # Predefined settings registers
        REG_BOOST_TIME_SETTING: RegisterDefinition(
            REG_BOOST_TIME_SETTING, 1106, "BOOST_TIME_S", writable=True
        ),
        REG_OVERPRESSURE_TIME_SETTING: RegisterDefinition(
            REG_OVERPRESSURE_TIME_SETTING, 1107, "OVERP_TIME_S", writable=True
        ),
        REG_SUMMER_MODE_TEMP_LIMIT: RegisterDefinition(
            REG_SUMMER_MODE_TEMP_LIMIT, 1078, "SUMMER_MODE_TE01_LIMIT", scale=0.1, writable=True
        ),
        # Additional number registers
        REG_FILTER_INTERVAL: RegisterDefinition(
            REG_FILTER_INTERVAL, 1085, "FILTER_INTERVAL_S", writable=True
        ),
        # Additional sensor registers
        REG_HEAT_RECOVERY_EFFICIENCY: RegisterDefinition(
            REG_HEAT_RECOVERY_EFFICIENCY, 1190, "FG50_EA_M", scale=0.1
        ),
        REG_DEFROST_STATE: RegisterDefinition(
            REG_DEFROST_STATE, 1183, "DFRST_FI"
        ),
        REG_SUPPLY_FAN_SPEED: RegisterDefinition(
            REG_SUPPLY_FAN_SPEED, 1040, "TF10_Y", scale=0.1
        ),
        REG_EXHAUST_FAN_SPEED: RegisterDefinition(
            REG_EXHAUST_FAN_SPEED, 1042, "PF30_Y", scale=0.1
        ),
        REG_FILTER_STATE: RegisterDefinition(
            REG_FILTER_STATE, 1205, "FILTER_STATE_FI"
        ),
        REG_FILTER_DAY: RegisterDefinition(
            REG_FILTER_DAY, 1086, "FILTER_DAY", writable=True
        ),
        REG_FILTER_MONTH: RegisterDefinition(
            REG_FILTER_MONTH, 1087, "FILTER_MONTH", writable=True
        ),
        REG_FILTER_YEAR: RegisterDefinition(
            REG_FILTER_YEAR, 1088, "FILTER_YEAR", writable=True
        ),
        REG_FILTER_NEXT_DAY: RegisterDefinition(
            REG_FILTER_NEXT_DAY, 1089, "FILTERNEXT_DAY", writable=True
        ),
        REG_FILTER_NEXT_MONTH: RegisterDefinition(
            REG_FILTER_NEXT_MONTH, 1090, "FILTERNEXT_MONTH", writable=True
        ),
        REG_FILTER_NEXT_YEAR: RegisterDefinition(
            REG_FILTER_NEXT_YEAR, 1091, "FILTERNEXT_YEAR", writable=True
        ),
    }


def _build_registers_v2() -> dict[str, RegisterDefinition]:
    """Build the complete register map for Parmair MAC devices with software version 2.xx.

    Based on official Parmair Modbus V2.XX documentation.
    Firmware 2.xx uses Register ID + 1000 addressing scheme.
    For example: Register ID 20 (TE01_M) -> Address 1020

    Control states for V2.xx (USERSTATECONTROL_FO):
    0=Off, 1=Away, 2=Home, 3=Boost, 4=Sauna, 5=Fireplace

    Note: These registers are NOT compatible with 1.xx firmware which uses different
    control registers (POWER_BTN_FI, IV01_CONTROLSTATE_FO, etc.).
    """
    return {
        # === 1 SYSTEM SETTINGS ===
        REG_ACKNOWLEDGE_ALARMS: RegisterDefinition(REG_ACKNOWLEDGE_ALARMS, 1003, "ACK_ALARMS", writable=True),
        REG_ALARM_COUNT: RegisterDefinition(REG_ALARM_COUNT, 1004, "ALARM_COUNT"),
        REG_TIME_YEAR: RegisterDefinition(REG_TIME_YEAR, 1009, "TIME_YEAR", writable=True),
        REG_TIME_MONTH: RegisterDefinition(REG_TIME_MONTH, 1010, "TIME_MONTH", writable=True),
        REG_TIME_DAY: RegisterDefinition(REG_TIME_DAY, 1011, "TIME_DAY", writable=True),
        REG_TIME_HOUR: RegisterDefinition(REG_TIME_HOUR, 1012, "TIME_HOUR", writable=True),
        REG_TIME_MIN: RegisterDefinition(REG_TIME_MIN, 1013, "TIME_MIN", writable=True),
        REG_FIRMWARE_VERSION: RegisterDefinition(REG_FIRMWARE_VERSION, 1014, "MULTI_FW_VER", scale=0.01),
        REG_SOFTWARE_VERSION: RegisterDefinition(REG_SOFTWARE_VERSION, 1015, "MULTI_SW_VER", scale=0.01),
        REG_BOOTLOADER_VERSION: RegisterDefinition(REG_BOOTLOADER_VERSION, 1016, "MULTI_BL_VER", scale=0.01),

        # === 10 CONFIGURATION PARAMETERS ===
        REG_M10_TYPE: RegisterDefinition(REG_M10_TYPE, 1105, "M10_TYPE", writable=True),
        REG_M11_TYPE: RegisterDefinition(REG_M11_TYPE, 1106, "M11_TYPE", writable=True),
        REG_M12_TYPE: RegisterDefinition(REG_M12_TYPE, 1107, "M12_TYPE", writable=True),
        REG_SF_SPEED1: RegisterDefinition(REG_SF_SPEED1, 1108, "SF_SPEED1_S", writable=True),
        REG_SF_SPEED2: RegisterDefinition(REG_SF_SPEED2, 1109, "SF_SPEED2_S", writable=True),
        REG_SF_SPEED3: RegisterDefinition(REG_SF_SPEED3, 1110, "SF_SPEED3_S", writable=True),
        REG_SF_SPEED4: RegisterDefinition(REG_SF_SPEED4, 1111, "SF_SPEED4_S", writable=True),
        REG_SF_SPEED5: RegisterDefinition(REG_SF_SPEED5, 1112, "SF_SPEED5_S", writable=True),
        REG_EF_SPEED1: RegisterDefinition(REG_EF_SPEED1, 1113, "EF_SPEED1_S", writable=True),
        REG_EF_SPEED2: RegisterDefinition(REG_EF_SPEED2, 1114, "EF_SPEED2_S", writable=True),
        REG_EF_SPEED3: RegisterDefinition(REG_EF_SPEED3, 1115, "EF_SPEED3_S", writable=True),
        REG_EF_SPEED4: RegisterDefinition(REG_EF_SPEED4, 1116, "EF_SPEED4_S", writable=True),
        REG_EF_SPEED5: RegisterDefinition(REG_EF_SPEED5, 1117, "EF_SPEED5_S", writable=True),
        REG_SENSOR_TEMP_CORRECTION: RegisterDefinition(REG_SENSOR_TEMP_CORRECTION, 1120, "SENSOR_TE_COR", scale=0.1, writable=True),
        REG_SENSOR_HUMIDITY_CORRECTION: RegisterDefinition(REG_SENSOR_HUMIDITY_CORRECTION, 1121, "SENSOR_ME_COR", writable=True),
        REG_SENSOR_CO2_CORRECTION: RegisterDefinition(REG_SENSOR_CO2_CORRECTION, 1122, "SENSOR_CO2_COR", writable=True),
        REG_HEATER_TYPE: RegisterDefinition(REG_HEATER_TYPE, 1124, "HEATPUMP_RADIATOR_ENABLE", writable=True),
        REG_HARDWARE_TYPE: RegisterDefinition(REG_HARDWARE_TYPE, 1125, "VENT_MACHINE"),
        REG_SUPPLY_TEMP_MIN: RegisterDefinition(REG_SUPPLY_TEMP_MIN, 1129, "TE10_MIN_S", scale=0.1, writable=True),
        REG_SUPPLY_TEMP_BASE: RegisterDefinition(REG_SUPPLY_TEMP_BASE, 1137, "TE10_BASE_S", scale=0.1, writable=True),
        REG_BOOST_MIN_TIME: RegisterDefinition(REG_BOOST_MIN_TIME, 1140, "BST_MINTIME", writable=True),
        REG_CO2_MIN_TIME: RegisterDefinition(REG_CO2_MIN_TIME, 1141, "CO2_MINTIME", writable=True),
        REG_BOOST_TIME_LIMIT: RegisterDefinition(REG_BOOST_TIME_LIMIT, 1144, "BST_TIME_LIMIT", writable=True),

        # Control registers - v2 uses different control scheme
        # 180: UNIT_CONTROL_FO - 0=Off, 1=On
        REG_POWER: RegisterDefinition(REG_POWER, 1180, "UNIT_CONTROL_FO", writable=True),
        # 181: USERSTATECONTROL_FO - 0=Off, 1=Away, 2=Home, 3=Boost, 4=Sauna, 5=Fireplace
        REG_CONTROL_STATE: RegisterDefinition(REG_CONTROL_STATE, 1181, "USERSTATECONTROL_FO", writable=True),
        # V2 doesn't have separate speed register - speed is determined by mode
        REG_ACTUAL_SPEED: RegisterDefinition(REG_ACTUAL_SPEED, 1181, "USERSTATECONTROL_FO"),
        REG_SPEED_CONTROL: RegisterDefinition(REG_SPEED_CONTROL, 1181, "USERSTATECONTROL_FO", writable=True),

        # === 2 PHYSICAL INPUTS ===
        REG_FRESH_AIR_TEMP: RegisterDefinition(REG_FRESH_AIR_TEMP, 1020, "TE01_M", scale=0.1),
        REG_SUPPLY_AFTER_RECOVERY_TEMP: RegisterDefinition(REG_SUPPLY_AFTER_RECOVERY_TEMP, 1021, "TE05_M", scale=0.1),
        REG_SUPPLY_TEMP: RegisterDefinition(REG_SUPPLY_TEMP, 1022, "TE10_M", scale=0.1),
        REG_WASTE_TEMP: RegisterDefinition(REG_WASTE_TEMP, 1023, "TE31_M", scale=0.1),
        REG_EXHAUST_TEMP: RegisterDefinition(REG_EXHAUST_TEMP, 1024, "TE30_M", scale=0.1),
        REG_HUMIDITY: RegisterDefinition(REG_HUMIDITY, 1025, "ME05_M", optional=True),
        REG_EXHAUST_CO2: RegisterDefinition(REG_EXHAUST_CO2, 1026, "QE05_M", optional=True),
        REG_SUPPLY_FAN_INDICATOR: RegisterDefinition(REG_SUPPLY_FAN_INDICATOR, 1027, "TF10_I"),
        REG_EXHAUST_FAN_INDICATOR: RegisterDefinition(REG_EXHAUST_FAN_INDICATOR, 1028, "PF30_I"),
        REG_WET_ROOM_HUMIDITY: RegisterDefinition(REG_WET_ROOM_HUMIDITY, 1029, "ME20_M", optional=True),
        REG_CO2: RegisterDefinition(REG_CO2, 1030, "QE20_M", optional=True),
        REG_EXTERNAL_SIGNAL: RegisterDefinition(REG_EXTERNAL_SIGNAL, 1031, "EXTERNAL_M", scale=0.1),
        REG_EXTERNAL_BOOST_SIGNAL: RegisterDefinition(REG_EXTERNAL_BOOST_SIGNAL, 1035, "EXTERNAL_BOOST_M", scale=0.1),
        REG_TEMP_DEFLECTION: RegisterDefinition(REG_TEMP_DEFLECTION, 1036, "TE10_DEFECTION_M", scale=0.1),

        # === 3 PHYSICAL OUTPUTS ===
        REG_SUPPLY_FAN_SPEED: RegisterDefinition(REG_SUPPLY_FAN_SPEED, 1040, "TF10_Y", scale=0.1),
        REG_EXHAUST_FAN_SPEED: RegisterDefinition(REG_EXHAUST_FAN_SPEED, 1042, "PF30_Y", scale=0.1),
        REG_POST_HEATER_OUTPUT: RegisterDefinition(REG_POST_HEATER_OUTPUT, 1044, "TV45_Y", scale=0.1),
        REG_HEAT_RECOVERY_OUTPUT: RegisterDefinition(REG_HEAT_RECOVERY_OUTPUT, 1046, "FG50_Y", scale=0.1),
        REG_PRE_HEATER_OUTPUT: RegisterDefinition(REG_PRE_HEATER_OUTPUT, 1048, "EC05_Y", scale=0.1),
        REG_HEAT_PUMP_OUTPUT: RegisterDefinition(REG_HEAT_PUMP_OUTPUT, 1050, "HP_RAD_O"),

        # === 4 SETTINGS ===
        REG_HOME_SPEED: RegisterDefinition(REG_HOME_SPEED, 1060, "HOME_SPEED_S", writable=True),
        REG_SUPPLY_TEMP_SETPOINT: RegisterDefinition(REG_SUPPLY_TEMP_SETPOINT, 1061, "TE10_MIN_HOME_S", scale=0.1, writable=True),
        REG_TEMP_CONTROL_MODE: RegisterDefinition(REG_TEMP_CONTROL_MODE, 1062, "TE10_CONTROL_MODE_S", writable=True),
        REG_AWAY_SPEED: RegisterDefinition(REG_AWAY_SPEED, 1063, "AWAY_SPEED_S", writable=True),
        REG_AWAY_TEMP_SETPOINT: RegisterDefinition(REG_AWAY_TEMP_SETPOINT, 1064, "TE10_MIN_AWAY_S", scale=0.1, writable=True),
        REG_BOOST_SETTING: RegisterDefinition(REG_BOOST_SETTING, 1065, "BOOST_SETTING_S", writable=True),
        REG_OVERPRESSURE_AMOUNT: RegisterDefinition(REG_OVERPRESSURE_AMOUNT, 1068, "OVERP_AMOUNT_S", writable=True),
        REG_TIME_PROGRAM_ENABLE: RegisterDefinition(REG_TIME_PROGRAM_ENABLE, 1070, "TP_ENABLE_S", writable=True),
        REG_SUMMER_MODE: RegisterDefinition(REG_SUMMER_MODE, 1071, "AUTO_SUMMER_COOL_S", writable=True),
        REG_AUTO_SUMMER_POWER: RegisterDefinition(REG_AUTO_SUMMER_POWER, 1072, "AUTO_SUMMER_POWER_S", writable=True),
        REG_EXHAUST_TEMP_SETPOINT: RegisterDefinition(REG_EXHAUST_TEMP_SETPOINT, 1073, "TE30_S", scale=0.1, writable=True),
        REG_HEATER_ENABLE: RegisterDefinition(REG_HEATER_ENABLE, 1074, "AUTO_HEATER_ENABLE_S", writable=True),
        REG_AUTO_COLD_LOWSPEED: RegisterDefinition(REG_AUTO_COLD_LOWSPEED, 1075, "AUTO_COLD_LOWSPEED_S", writable=True),
        REG_COLD_LOWSPEED_LIMIT: RegisterDefinition(REG_COLD_LOWSPEED_LIMIT, 1076, "COLD_LOWSPEED_S", scale=0.1, writable=True),
        REG_AUTO_HUMIDITY_BOOST: RegisterDefinition(REG_AUTO_HUMIDITY_BOOST, 1077, "AUTO_HUMIDITY_BOOST_S", writable=True),
        REG_HUMIDITY_BOOST_SENSITIVITY: RegisterDefinition(REG_HUMIDITY_BOOST_SENSITIVITY, 1078, "ME05_BOOST_SENSITIVITY", writable=True),
        REG_HUMIDITY_BOOST_TEMP_LIMIT: RegisterDefinition(REG_HUMIDITY_BOOST_TEMP_LIMIT, 1079, "ME_BST_TE01_LIMIT", scale=0.1, writable=True),
        REG_AUTO_CO2_BOOST: RegisterDefinition(REG_AUTO_CO2_BOOST, 1080, "AUTO_CO2_BOOST_S", writable=True),
        REG_AUTO_HOME_AWAY: RegisterDefinition(REG_AUTO_HOME_AWAY, 1081, "AUTO_HOMEAWAY_S", writable=True),
        REG_CO2_HOME_THRESHOLD: RegisterDefinition(REG_CO2_HOME_THRESHOLD, 1082, "QE_HOME_S", writable=True),
        REG_CO2_BOOST_THRESHOLD: RegisterDefinition(REG_CO2_BOOST_THRESHOLD, 1083, "QE_BOOST_S", writable=True),
        REG_FILTER_INTERVAL: RegisterDefinition(REG_FILTER_INTERVAL, 1090, "FILTER_INTERVAL_S", writable=True),
        REG_HP_RAD_MODE: RegisterDefinition(REG_HP_RAD_MODE, 1091, "HP_RAD_MODE", writable=True),
        REG_HP_RAD_WINTER: RegisterDefinition(REG_HP_RAD_WINTER, 1092, "HP_RAD_WINTER", scale=0.1, writable=True),
        REG_HP_RAD_SUMMER: RegisterDefinition(REG_HP_RAD_SUMMER, 1093, "HP_RAD_SUMMER", scale=0.1, writable=True),
        REG_HEATING_SEASON_AVERAGE: RegisterDefinition(REG_HEATING_SEASON_AVERAGE, 1094, "HEATING_SEASON_AVERAGE", scale=0.1, writable=True),
        REG_HEATING_SEASON_MOMENT: RegisterDefinition(REG_HEATING_SEASON_MOMENT, 1095, "HEATING_SEASON_MOMENT", scale=0.1, writable=True),
        REG_SUMMER_TEMP_SETPOINT: RegisterDefinition(REG_SUMMER_TEMP_SETPOINT, 1096, "TE10_MIN_SUMMER_S", scale=0.1, writable=True),
        REG_SUPPLY_TEMP_MAX: RegisterDefinition(REG_SUPPLY_TEMP_MAX, 1097, "TE10_MAX_S", scale=0.1, writable=True),
        REG_BOOST_TEMP_LIMIT: RegisterDefinition(REG_BOOST_TEMP_LIMIT, 1098, "BST_TE01_LIMIT", scale=0.1, writable=True),

        # === 6 SOFT MEASUREMENTS AND CONTROL POINTS ===
        REG_HOME_STATE: RegisterDefinition(REG_HOME_STATE, 1181, "USERSTATECONTROL_FO"),
        REG_BOOST_STATE: RegisterDefinition(REG_BOOST_STATE, 1181, "USERSTATECONTROL_FO"),
        REG_OVERPRESSURE_STATE: RegisterDefinition(REG_OVERPRESSURE_STATE, 1181, "USERSTATECONTROL_FO"),
        REG_DEFROST_STATE: RegisterDefinition(REG_DEFROST_STATE, 1182, "DFRST_FI"),
        REG_HEAT_RECOVERY_EFFICIENCY: RegisterDefinition(REG_HEAT_RECOVERY_EFFICIENCY, 1183, "FG50_EA_M", scale=0.1),
        REG_FILTER_STATE: RegisterDefinition(REG_FILTER_STATE, 1184, "FILTER_STATE_FI"),
        REG_FILTER_REPLACED: RegisterDefinition(REG_FILTER_REPLACED, 1184, "FILTER_STATE_FI", writable=True),
        REG_SENSOR_STATUS: RegisterDefinition(REG_SENSOR_STATUS, 1185, "SENSOR_STATUS"),
        REG_SEASON_STATE: RegisterDefinition(REG_SEASON_STATE, 1189, "SUMMER_MODE_I"),
        REG_SUMMER_POWER_CHANGE: RegisterDefinition(REG_SUMMER_POWER_CHANGE, 1190, "SUMMER_POWER_CHANGE_F"),
        REG_CALCULATED_HUMIDITY: RegisterDefinition(REG_CALCULATED_HUMIDITY, 1191, "HUMIDITY_FM", scale=0.01),
        REG_HUMIDITY_24H_AVG: RegisterDefinition(REG_HUMIDITY_24H_AVG, 1192, "ME05_AVG_FM", scale=0.1),
        REG_POWER_LIMIT: RegisterDefinition(REG_POWER_LIMIT, 1199, "PWR_LIMIT_FY", scale=0.1),
        REG_OUTDOOR_TEMP_AVG: RegisterDefinition(REG_OUTDOOR_TEMP_AVG, 1213, "TE01_AVG_FM", scale=0.1),

        # === 7 ALARMS ===
        REG_ALARM_TE01: RegisterDefinition(REG_ALARM_TE01, 1220, "TE01_FA"),
        REG_ALARM_TE10: RegisterDefinition(REG_ALARM_TE10, 1221, "TE10_FA"),
        REG_ALARM_TE05: RegisterDefinition(REG_ALARM_TE05, 1222, "TE05_FA"),
        REG_ALARM_TE30: RegisterDefinition(REG_ALARM_TE30, 1223, "TE30_FA"),
        REG_ALARM_TE31: RegisterDefinition(REG_ALARM_TE31, 1224, "TE31_FA"),
        REG_ALARM_ME05: RegisterDefinition(REG_ALARM_ME05, 1225, "ME05_FA"),
        REG_ALARM_TF10: RegisterDefinition(REG_ALARM_TF10, 1226, "TF10_CA"),
        REG_ALARM_PF30: RegisterDefinition(REG_ALARM_PF30, 1227, "PF30_CA"),
        REG_ALARM_TE10_HIGH: RegisterDefinition(REG_ALARM_TE10_HIGH, 1228, "TE10_HA"),
        REG_ALARM_TE30_HIGH: RegisterDefinition(REG_ALARM_TE30_HIGH, 1229, "TE30_HA"),
        REG_ALARM_TE10_LOW: RegisterDefinition(REG_ALARM_TE10_LOW, 1230, "TE10_LA"),
        REG_ALARM_FILTER: RegisterDefinition(REG_ALARM_FILTER, 1240, "FILTER_FA"),

        # === UNDOCUMENTED but confirmed working on MAC 120 fw 2.25 ===
        REG_BOOST_TIME_SETTING: RegisterDefinition(REG_BOOST_TIME_SETTING, 1066, "BOOST_TIME_S", writable=True),  # undocumented
        REG_OVERPRESSURE_TIME_SETTING: RegisterDefinition(REG_OVERPRESSURE_TIME_SETTING, 1069, "OVERP_TIME_S", writable=True),  # undocumented
        REG_BOOST_TIMER: RegisterDefinition(REG_BOOST_TIMER, 1200, "BOOST_TIMER_FM", writable=True),  # undocumented
        REG_OVERPRESSURE_TIMER: RegisterDefinition(REG_OVERPRESSURE_TIMER, 1201, "OVERP_TIMER_FM", writable=True),  # undocumented
        REG_FILTER_DAY: RegisterDefinition(REG_FILTER_DAY, 1193, "FILTER_DAY", writable=True),  # undocumented
        REG_FILTER_MONTH: RegisterDefinition(REG_FILTER_MONTH, 1194, "FILTER_MONTH", writable=True),  # undocumented
        REG_FILTER_YEAR: RegisterDefinition(REG_FILTER_YEAR, 1195, "FILTER_YEAR", writable=True),  # undocumented
        REG_FILTER_NEXT_DAY: RegisterDefinition(REG_FILTER_NEXT_DAY, 1196, "FILTERNEXT_DAY", writable=True),  # undocumented
        REG_FILTER_NEXT_MONTH: RegisterDefinition(REG_FILTER_NEXT_MONTH, 1197, "FILTERNEXT_MONTH", writable=True),  # undocumented
        REG_FILTER_NEXT_YEAR: RegisterDefinition(REG_FILTER_NEXT_YEAR, 1198, "FILTERNEXT_YEAR", writable=True),  # undocumented

        # === Optional/Undocumented ===
        REG_SUM_ALARM: RegisterDefinition(REG_SUM_ALARM, 1005, "SUM_ALARM", optional=True),  # undocumented
        REG_ALARMS_STATE: RegisterDefinition(REG_ALARMS_STATE, 1204, "ALARMS_STATE_FI", optional=True),  # undocumented
    }


def get_registers_for_version(software_version: str) -> dict[str, RegisterDefinition]:
    """Get the appropriate register map based on software version.

    Args:
        software_version: Software version string (e.g., "1.83", "2.10")

    Returns:
        Dictionary mapping register keys to RegisterDefinition objects
    """
    if software_version.startswith("2."):
        return _build_registers_v2()
    else:
        # Default to v1 for 1.xx or unknown versions
        return _build_registers_v1()


# Build the default register map (v1)
REGISTERS = _build_registers_v1()

# Ordered list of registers to poll on each update.
POLLING_REGISTER_KEYS = (
    # System
    REG_SOFTWARE_VERSION,
    REG_HARDWARE_TYPE,
    REG_HEATER_TYPE,
    REG_FIRMWARE_VERSION,
    REG_BOOTLOADER_VERSION,
    # Control
    REG_POWER,
    REG_CONTROL_STATE,
    REG_ACTUAL_SPEED,
    REG_SPEED_CONTROL,
    # Temperatures
    REG_FRESH_AIR_TEMP,
    REG_SUPPLY_AFTER_RECOVERY_TEMP,
    REG_SUPPLY_TEMP,
    REG_EXHAUST_TEMP,
    REG_WASTE_TEMP,
    REG_EXHAUST_TEMP_SETPOINT,
    REG_SUPPLY_TEMP_SETPOINT,
    REG_OUTDOOR_TEMP_AVG,
    # Speed settings
    REG_HOME_SPEED,
    REG_AWAY_SPEED,
    REG_BOOST_SETTING,
    # States
    REG_HOME_STATE,
    REG_BOOST_STATE,
    REG_BOOST_TIMER,
    REG_OVERPRESSURE_STATE,
    REG_OVERPRESSURE_TIMER,
    REG_DEFROST_STATE,
    REG_SEASON_STATE,
    # Sensors
    REG_HUMIDITY,
    REG_HUMIDITY_24H_AVG,
    REG_CO2,
    REG_EXHAUST_CO2,
    REG_WET_ROOM_HUMIDITY,
    # Fan output
    REG_SUPPLY_FAN_SPEED,
    REG_EXHAUST_FAN_SPEED,
    REG_SUPPLY_FAN_INDICATOR,
    REG_EXHAUST_FAN_INDICATOR,
    # Heater/recovery output
    REG_POST_HEATER_OUTPUT,
    REG_PRE_HEATER_OUTPUT,
    REG_HEAT_RECOVERY_OUTPUT,
    REG_HEAT_RECOVERY_EFFICIENCY,
    REG_HEAT_PUMP_OUTPUT,
    # External signals
    REG_EXTERNAL_SIGNAL,
    REG_EXTERNAL_BOOST_SIGNAL,
    REG_TEMP_DEFLECTION,
    # Alarms
    REG_ALARM_COUNT,
    REG_SUM_ALARM,
    REG_ALARMS_STATE,
    REG_SENSOR_STATUS,
    # Filter
    REG_FILTER_STATE,
    REG_FILTER_DAY,
    REG_FILTER_MONTH,
    REG_FILTER_YEAR,
    REG_FILTER_NEXT_DAY,
    REG_FILTER_NEXT_MONTH,
    REG_FILTER_NEXT_YEAR,
    REG_FILTER_INTERVAL,
    # Settings
    REG_SUMMER_MODE,
    REG_TIME_PROGRAM_ENABLE,
    REG_HEATER_ENABLE,
    REG_BOOST_TIME_SETTING,
    REG_OVERPRESSURE_TIME_SETTING,
    REG_SUMMER_MODE_TEMP_LIMIT,
    REG_POWER_LIMIT,
    REG_SUMMER_POWER_CHANGE,
)


def get_register_definition(key: str, registers: dict[str, RegisterDefinition] | None = None) -> RegisterDefinition:
    """Return the register definition for a given key.

    Args:
        key: Register key to look up
        registers: Optional register map to use. If None, uses default REGISTERS.

    Returns:
        RegisterDefinition for the requested register
    """
    reg_map = registers if registers is not None else REGISTERS
    if key not in reg_map:
        raise KeyError(f"Register '{key}' not defined")
    return reg_map[key]


# Operating modes for IV01_CONTROLSTATE
MODE_STOP = 0
MODE_AWAY = 1
MODE_HOME = 2
MODE_BOOST = 3
MODE_OVERPRESSURE = 4
MODE_AWAY_TIMER = 5
MODE_HOME_TIMER = 6
MODE_BOOST_TIMER = 7
MODE_OVERPRESSURE_TIMER = 8
MODE_MANUAL = 9

# Speed control values for IV01_SPEED
SPEED_AUTO = 0
SPEED_STOP = 1
SPEED_1 = 2
SPEED_2 = 3
SPEED_3 = 4
SPEED_4 = 5
SPEED_5 = 6

# POWER_BTN states
POWER_OFF = 0
POWER_SHUTTING_DOWN = 1
POWER_STARTING = 2
POWER_RUNNING = 3

HARDWARE_TYPE_MAP_V2 = {
    112: 120,  # Type code 112 = MAC 120
}
