# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: repl_cmd.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import msg_header_pb2 as msg__header__pb2
import time_pb2 as time__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0erepl_cmd.proto\x12\x08iit.advr\x1a\x10msg_header.proto\x1a\ntime.proto\" \n\x08Vector2d\x12\t\n\x01x\x18\x01 \x02(\x01\x12\t\n\x01y\x18\x02 \x02(\x01\"\xca\x01\n\x05Gains\x12\"\n\x04type\x18\x01 \x02(\x0e\x32\x14.iit.advr.Gains.Type\x12\x0e\n\x06pos_kp\x18\x02 \x02(\x01\x12\x0e\n\x06pos_kd\x18\x03 \x02(\x01\x12\x0e\n\x06tor_kp\x18\x04 \x01(\x01\x12\x0e\n\x06tor_ki\x18\x05 \x01(\x01\x12\x0e\n\x06tor_kd\x18\x06 \x01(\x01\"M\n\x04Type\x12\x0c\n\x08POSITION\x10;\x12\x0c\n\x08VELOCITY\x10q\x12\x0e\n\tIMPEDANCE\x10\xd4\x01\x12\x0b\n\x06TORQUE\x10\xcc\x01\x12\x0c\n\x07\x43URRENT\x10\xdd\x01\"f\n\x06\x41uxPDO\x12\x1f\n\x02op\x18\x01 \x02(\x0e\x32\x13.iit.advr.AuxPDO.Op\x12\x0b\n\x03idx\x18\x02 \x01(\x05\x12\r\n\x05value\x18\x03 \x01(\x02\"\x1f\n\x02Op\x12\x07\n\x03NOP\x10\x01\x12\x07\n\x03GET\x10\x02\x12\x07\n\x03SET\x10\x03\"p\n\nSlave_objd\x12\r\n\x05index\x18\x01 \x02(\x05\x12\x10\n\x08subindex\x18\x02 \x02(\x05\x12\x10\n\x08\x64\x61tatype\x18\x03 \x02(\x05\x12\x11\n\tbitlength\x18\x04 \x02(\x05\x12\x0e\n\x06\x61\x63\x63\x65ss\x18\x05 \x02(\x05\x12\x0c\n\x04name\x18\x06 \x02(\t\"(\n\tKeyValStr\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"\xf1\x04\n\x0eTrajectory_cmd\x12+\n\x04type\x18\x01 \x02(\x0e\x32\x1d.iit.advr.Trajectory_cmd.Type\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x10\n\x08\x62oard_id\x18\x03 \x02(\x05\x12\x37\n\nsmooth_par\x18\x04 \x01(\x0b\x32#.iit.advr.Trajectory_cmd.Smooth_par\x12\x37\n\nperiod_par\x18\x05 \x01(\x0b\x32#.iit.advr.Trajectory_cmd.Period_par\x12\x37\n\nhoming_par\x18\x06 \x01(\x0b\x32#.iit.advr.Trajectory_cmd.Homing_par\x12>\n\x0esmooth_vel_par\x18\x07 \x01(\x0b\x32&.iit.advr.Trajectory_cmd.SmoothVel_par\x1a\x17\n\nHoming_par\x12\t\n\x01x\x18\x01 \x03(\x01\x1a\x44\n\nPeriod_par\x12\x0c\n\x04\x66req\x18\x01 \x02(\x01\x12\x0c\n\x04\x61mpl\x18\x02 \x02(\x01\x12\x0c\n\x04teta\x18\x03 \x02(\x01\x12\x0c\n\x04secs\x18\x04 \x02(\x01\x1a\"\n\nSmooth_par\x12\t\n\x01x\x18\x01 \x03(\x01\x12\t\n\x01y\x18\x02 \x03(\x01\x1a\x66\n\rSmoothVel_par\x12\n\n\x02\x64t\x18\x01 \x02(\x01\x12\n\n\x02p0\x18\x02 \x01(\x01\x12\n\n\x02v0\x18\x03 \x01(\x01\x12\n\n\x02pt\x18\x04 \x01(\x01\x12\n\n\x02vt\x18\x05 \x01(\x01\x12\n\n\x02\x64s\x18\x06 \x01(\x01\x12\r\n\x05magic\x18\x07 \x01(\x01\"<\n\x04Type\x12\n\n\x06HOMING\x10\x01\x12\x08\n\x04SINE\x10\x02\x12\x0c\n\x08SMOOTHER\x10\x03\x12\x10\n\x0cSMOOTHER_VEL\x10\x04\"s\n\rTrj_queue_cmd\x12*\n\x04type\x18\x01 \x02(\x0e\x32\x1c.iit.advr.Trj_queue_cmd.Type\x12\x11\n\ttrj_names\x18\x02 \x03(\t\"#\n\x04Type\x12\x0c\n\x08PUSH_QUE\x10\x01\x12\r\n\tEMPTY_QUE\x10\x02\"\n\n\x08Repl_hdr\"\x80\x01\n\x14Slave_registry_write\x12\x31\n\x04type\x18\x01 \x02(\x0e\x32#.iit.advr.Slave_registry_write.Type\x12\x10\n\x08\x62oard_id\x18\x02 \x02(\x05\"#\n\x04Type\x12\x0c\n\x08\x44RILL_ON\x10\x01\x12\r\n\tDRILL_OFF\x10\x02\"\x8b\x05\n\x08\x43trl_cmd\x12%\n\x04type\x18\x01 \x02(\x0e\x32\x17.iit.advr.Ctrl_cmd.Type\x12\x10\n\x08\x62oard_id\x18\x02 \x02(\x05\x12\r\n\x05value\x18\x03 \x01(\x02\x12\x1e\n\x05gains\x18\x04 \x01(\x0b\x32\x0f.iit.advr.Gains\"\x96\x04\n\x04Type\x12\x12\n\x0e\x43TRL_TEST_DONE\x10\x01\x12\x13\n\x0f\x43TRL_TEST_ERROR\x10\x02\x12\x11\n\rCTRL_DAC_TUNE\x10\x03\x12\x1b\n\x17\x43TRL_REMOVE_TORQUE_OFFS\x10\x04\x12\x1a\n\x16\x43TRL_SET_ZERO_POSITION\x10\x05\x12\x0c\n\x08\x43TRL_FAN\x10\x06\x12\x0c\n\x08\x43TRL_LED\x10\x07\x12\x10\n\x0c\x43TRL_SANDBOX\x10\x08\x12\x13\n\x0f\x43TRL_REF_FILTER\x10\t\x12\x12\n\x0e\x43TRL_POWER_MOD\x10\n\x12\x12\n\x0e\x43TRL_CMD_START\x10\x0b\x12\x11\n\rCTRL_CMD_STOP\x10\x0c\x12\x11\n\rCTRL_SET_HOME\x10\r\x12\x19\n\x15\x43TRL_SET_MIN_POSITION\x10\x0e\x12\x19\n\x15\x43TRL_SET_MAX_POSITION\x10\x0f\x12\x19\n\x15\x43TRL_RUN_TORQUE_CALIB\x10\x10\x12\x12\n\x0e\x43TRL_SET_GAINS\x10\x11\x12\x15\n\x11\x43TRL_SET_POSITION\x10\x12\x12\x15\n\x11\x43TRL_SET_VELOCITY\x10\x13\x12\x13\n\x0f\x43TRL_SET_TORQUE\x10\x14\x12\x14\n\x10\x43TRL_SET_CURRENT\x10\x15\x12\x10\n\x0c\x43TRL_GET_ADC\x10\x16\x12\x10\n\x0c\x43TRL_SET_DAC\x10\x17\x12\x0e\n\nCTRL_BRAKE\x10\x18\x12\x16\n\x12\x43TRL_SET_DAC_FLASH\x10\x19\"\x9c\x01\n\tFlash_cmd\x12&\n\x04type\x18\x01 \x02(\x0e\x32\x18.iit.advr.Flash_cmd.Type\x12\x10\n\x08\x62oard_id\x18\x02 \x02(\x05\"U\n\x04Type\x12\x18\n\x14SAVE_PARAMS_TO_FLASH\x10\x01\x12\x1a\n\x16LOAD_PARAMS_FROM_FLASH\x10\x02\x12\x17\n\x13LOAD_DEFAULT_PARAMS\x10\x03\"V\n\rSlave_SDO_cmd\x12\x10\n\x08\x62oard_id\x18\x01 \x02(\x05\x12\x0e\n\x06rd_sdo\x18\x02 \x03(\t\x12#\n\x06wr_sdo\x18\x03 \x03(\x0b\x32\x13.iit.advr.KeyValStr\"s\n\x0eSlave_SDO_info\x12+\n\x04type\x18\x01 \x02(\x0e\x32\x1d.iit.advr.Slave_SDO_info.Type\x12\x10\n\x08\x62oard_id\x18\x02 \x02(\x05\"\"\n\x04Type\x12\x0c\n\x08SDO_NAME\x10\x01\x12\x0c\n\x08SDO_OBJD\x10\x02\"\xa3\x01\n\x0f\x45\x63\x61t_Master_cmd\x12,\n\x04type\x18\x01 \x02(\x0e\x32\x1e.iit.advr.Ecat_Master_cmd.Type\x12!\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\x13.iit.advr.KeyValStr\"?\n\x04Type\x12\x10\n\x0cSTART_MASTER\x10\x01\x12\x0f\n\x0bSTOP_MASTER\x10\x02\x12\x14\n\x10GET_SLAVES_DESCR\x10\x03\"g\n\nFOE_Master\x12\x10\n\x08\x66ilename\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x02(\r\x12\x10\n\x08mcu_type\x18\x03 \x01(\t\x12\x11\n\tslave_pos\x18\x04 \x01(\x05\x12\x10\n\x08\x62oard_id\x18\x05 \x01(\x05\"\xe4\x01\n\x0eMotors_PDO_cmd\x12\x39\n\nmotors_pdo\x18\x01 \x03(\x0b\x32%.iit.advr.Motors_PDO_cmd.Moto_PDO_cmd\x1a\x96\x01\n\x0cMoto_PDO_cmd\x12\x10\n\x08motor_id\x18\x01 \x02(\x05\x12\x0f\n\x07pos_ref\x18\x02 \x01(\x02\x12\x0f\n\x07vel_ref\x18\x03 \x01(\x02\x12\x0f\n\x07tor_ref\x18\x04 \x01(\x02\x12\x1e\n\x05gains\x18\x05 \x01(\x0b\x32\x0f.iit.advr.Gains\x12!\n\x07\x61ux_pdo\x18\x06 \x01(\x0b\x32\x10.iit.advr.AuxPDO\"\xd7\x01\n\x0cPDOs_aux_cmd\x12\x30\n\x08\x61ux_cmds\x18\x01 \x03(\x0b\x32\x1e.iit.advr.PDOs_aux_cmd.Aux_cmd\x1a\x94\x01\n\x07\x41ux_cmd\x12\x31\n\x04type\x18\x01 \x02(\x0e\x32#.iit.advr.PDOs_aux_cmd.Aux_cmd.Type\x12\x10\n\x08\x62oard_id\x18\x02 \x02(\x05\"D\n\x04Type\x12\x11\n\rBRAKE_RELEASE\x10\x01\x12\x10\n\x0c\x42RAKE_ENGAGE\x10\x02\x12\n\n\x06LED_ON\x10\x03\x12\x0b\n\x07LED_OFF\x10\x04\"\xdb\x04\n\x08Repl_cmd\x12\x1f\n\x04type\x18\x01 \x02(\x0e\x32\x11.iit.advr.CmdType\x12 \n\x06header\x18\x02 \x01(\x0b\x32\x10.iit.advr.Header\x12\x30\n\x0etrajectory_cmd\x18\x03 \x01(\x0b\x32\x18.iit.advr.Trajectory_cmd\x12$\n\x08\x63trl_cmd\x18\x04 \x01(\x0b\x32\x12.iit.advr.Ctrl_cmd\x12&\n\tflash_cmd\x18\x05 \x01(\x0b\x32\x13.iit.advr.Flash_cmd\x12\x32\n\x0f\x65\x63\x61t_master_cmd\x18\x06 \x01(\x0b\x32\x19.iit.advr.Ecat_Master_cmd\x12(\n\nfoe_master\x18\x07 \x01(\x0b\x32\x14.iit.advr.FOE_Master\x12.\n\rtrj_queue_cmd\x18\x08 \x01(\x0b\x32\x17.iit.advr.Trj_queue_cmd\x12.\n\rslave_sdo_cmd\x18\t \x01(\x0b\x32\x17.iit.advr.Slave_SDO_cmd\x12\x30\n\x0eslave_sdo_info\x18\n \x01(\x0b\x32\x18.iit.advr.Slave_SDO_info\x12\x30\n\x0emotors_pdo_cmd\x18\x0b \x01(\x0b\x32\x18.iit.advr.Motors_PDO_cmd\x12<\n\x14slave_registry_write\x18\x0c \x01(\x0b\x32\x1e.iit.advr.Slave_registry_write\x12,\n\x0cpdos_aux_cmd\x18\x63 \x01(\x0b\x32\x16.iit.advr.PDOs_aux_cmd\"\xaf\x01\n\tCmd_reply\x12&\n\x04type\x18\x01 \x02(\x0e\x32\x18.iit.advr.Cmd_reply.Type\x12#\n\x08\x63md_type\x18\x02 \x02(\x0e\x32\x11.iit.advr.CmdType\x12\x0b\n\x03msg\x18\x03 \x02(\t\x12 \n\x06header\x18\x04 \x01(\x0b\x32\x10.iit.advr.Header\x12\x0b\n\x03pdo\x18\x05 \x01(\t\"\x19\n\x04Type\x12\x07\n\x03\x41\x43K\x10\x01\x12\x08\n\x04NACK\x10\x02\"5\n\nTrj_Status\x12\x12\n\nqueue_size\x18\x01 \x02(\r\x12\x13\n\x0brunning_trj\x18\x02 \x01(\t\"\x98\x01\n\x08TM_Stats\x12\x14\n\x0crecv_dc_time\x18\x01 \x02(\x03\x12\x0e\n\x06offset\x18\x02 \x02(\x03\x12\x11\n\tloop_time\x18\x03 \x02(\x04\x12\x13\n\x0b\x65\x63\x61t_rx_wkc\x18\x04 \x02(\x05\x12\r\n\x05\x64\x65lta\x18\x05 \x02(\x03\x12\x13\n\x0b\x65\x63_cycle_ns\x18\x06 \x02(\x04\x12\x1a\n\x02ts\x18\x07 \x02(\x0b\x32\x0e.iit.advr.Time\"\x8a\x01\n\tRepl_info\x12 \n\x06header\x18\x01 \x01(\x0b\x32\x10.iit.advr.Header\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12(\n\ntrj_status\x18\x03 \x01(\x0b\x32\x14.iit.advr.Trj_Status\x12$\n\x08tm_stats\x18\x04 \x01(\x0b\x32\x12.iit.advr.TM_Stats*\xd0\x01\n\x07\x43mdType\x12\x0b\n\x07TRJ_CMD\x10\x01\x12\x0c\n\x08\x43TRL_CMD\x10\x02\x12\r\n\tFLASH_CMD\x10\x03\x12\x13\n\x0f\x45\x43\x41T_MASTER_CMD\x10\x04\x12\x0e\n\nFOE_MASTER\x10\x05\x12\x11\n\rTRJ_QUEUE_CMD\x10\x06\x12\x11\n\rSLAVE_SDO_CMD\x10\x07\x12\x12\n\x0eSLAVE_SDO_INFO\x10\x08\x12\x11\n\rMOTOR_PDO_CMD\x10\t\x12\x18\n\x14SLAVE_REGISTRY_WRITE\x10\n\x12\x0f\n\x0bPDO_AUX_CMD\x10\x63')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'repl_cmd_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CMDTYPE._serialized_start=4319
  _CMDTYPE._serialized_end=4527
  _VECTOR2D._serialized_start=58
  _VECTOR2D._serialized_end=90
  _GAINS._serialized_start=93
  _GAINS._serialized_end=295
  _GAINS_TYPE._serialized_start=218
  _GAINS_TYPE._serialized_end=295
  _AUXPDO._serialized_start=297
  _AUXPDO._serialized_end=399
  _AUXPDO_OP._serialized_start=368
  _AUXPDO_OP._serialized_end=399
  _SLAVE_OBJD._serialized_start=401
  _SLAVE_OBJD._serialized_end=513
  _KEYVALSTR._serialized_start=515
  _KEYVALSTR._serialized_end=555
  _TRAJECTORY_CMD._serialized_start=558
  _TRAJECTORY_CMD._serialized_end=1183
  _TRAJECTORY_CMD_HOMING_PAR._serialized_start=888
  _TRAJECTORY_CMD_HOMING_PAR._serialized_end=911
  _TRAJECTORY_CMD_PERIOD_PAR._serialized_start=913
  _TRAJECTORY_CMD_PERIOD_PAR._serialized_end=981
  _TRAJECTORY_CMD_SMOOTH_PAR._serialized_start=983
  _TRAJECTORY_CMD_SMOOTH_PAR._serialized_end=1017
  _TRAJECTORY_CMD_SMOOTHVEL_PAR._serialized_start=1019
  _TRAJECTORY_CMD_SMOOTHVEL_PAR._serialized_end=1121
  _TRAJECTORY_CMD_TYPE._serialized_start=1123
  _TRAJECTORY_CMD_TYPE._serialized_end=1183
  _TRJ_QUEUE_CMD._serialized_start=1185
  _TRJ_QUEUE_CMD._serialized_end=1300
  _TRJ_QUEUE_CMD_TYPE._serialized_start=1265
  _TRJ_QUEUE_CMD_TYPE._serialized_end=1300
  _REPL_HDR._serialized_start=1302
  _REPL_HDR._serialized_end=1312
  _SLAVE_REGISTRY_WRITE._serialized_start=1315
  _SLAVE_REGISTRY_WRITE._serialized_end=1443
  _SLAVE_REGISTRY_WRITE_TYPE._serialized_start=1408
  _SLAVE_REGISTRY_WRITE_TYPE._serialized_end=1443
  _CTRL_CMD._serialized_start=1446
  _CTRL_CMD._serialized_end=2097
  _CTRL_CMD_TYPE._serialized_start=1563
  _CTRL_CMD_TYPE._serialized_end=2097
  _FLASH_CMD._serialized_start=2100
  _FLASH_CMD._serialized_end=2256
  _FLASH_CMD_TYPE._serialized_start=2171
  _FLASH_CMD_TYPE._serialized_end=2256
  _SLAVE_SDO_CMD._serialized_start=2258
  _SLAVE_SDO_CMD._serialized_end=2344
  _SLAVE_SDO_INFO._serialized_start=2346
  _SLAVE_SDO_INFO._serialized_end=2461
  _SLAVE_SDO_INFO_TYPE._serialized_start=2427
  _SLAVE_SDO_INFO_TYPE._serialized_end=2461
  _ECAT_MASTER_CMD._serialized_start=2464
  _ECAT_MASTER_CMD._serialized_end=2627
  _ECAT_MASTER_CMD_TYPE._serialized_start=2564
  _ECAT_MASTER_CMD_TYPE._serialized_end=2627
  _FOE_MASTER._serialized_start=2629
  _FOE_MASTER._serialized_end=2732
  _MOTORS_PDO_CMD._serialized_start=2735
  _MOTORS_PDO_CMD._serialized_end=2963
  _MOTORS_PDO_CMD_MOTO_PDO_CMD._serialized_start=2813
  _MOTORS_PDO_CMD_MOTO_PDO_CMD._serialized_end=2963
  _PDOS_AUX_CMD._serialized_start=2966
  _PDOS_AUX_CMD._serialized_end=3181
  _PDOS_AUX_CMD_AUX_CMD._serialized_start=3033
  _PDOS_AUX_CMD_AUX_CMD._serialized_end=3181
  _PDOS_AUX_CMD_AUX_CMD_TYPE._serialized_start=3113
  _PDOS_AUX_CMD_AUX_CMD_TYPE._serialized_end=3181
  _REPL_CMD._serialized_start=3184
  _REPL_CMD._serialized_end=3787
  _CMD_REPLY._serialized_start=3790
  _CMD_REPLY._serialized_end=3965
  _CMD_REPLY_TYPE._serialized_start=3940
  _CMD_REPLY_TYPE._serialized_end=3965
  _TRJ_STATUS._serialized_start=3967
  _TRJ_STATUS._serialized_end=4020
  _TM_STATS._serialized_start=4023
  _TM_STATS._serialized_end=4175
  _REPL_INFO._serialized_start=4178
  _REPL_INFO._serialized_end=4316
# @@protoc_insertion_point(module_scope)
