# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hyq.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\thyq.proto\x12\x08iit.advr\"\x8b\x02\n\x0eHyqKnee_rx_pdo\x12\x18\n\x10\x65ncoder_position\x18\x01 \x01(\x02\x12\r\n\x05\x66orce\x18\x02 \x01(\x02\x12\x12\n\npressure_1\x18\x03 \x01(\x02\x12\x12\n\npressure_2\x18\x04 \x01(\x02\x12\x0f\n\x07\x63urrent\x18\x05 \x01(\x02\x12\x13\n\x0btemperature\x18\x06 \x01(\x02\x12\r\n\x05\x66\x61ult\x18\x07 \x01(\r\x12\x0b\n\x03rtt\x18\x08 \x01(\r\x12\x12\n\nop_idx_ack\x18\t \x01(\r\x12\x0b\n\x03\x61ux\x18\n \x01(\x02\x12\x16\n\x0e\x63urrent_ref_fb\x18\x0b \x01(\x02\x12\x17\n\x0fposition_ref_fb\x18\x0c \x01(\x02\x12\x14\n\x0c\x66orce_ref_fb\x18\r \x01(\x02\"\xde\x01\n\x0eHyqKnee_tx_pdo\x12\x13\n\x0b\x63urrent_ref\x18\x01 \x01(\x02\x12\x14\n\x0cposition_ref\x18\x02 \x01(\x02\x12\x11\n\tforce_ref\x18\x03 \x01(\x02\x12\x0e\n\x06gain_0\x18\x04 \x01(\x02\x12\x0e\n\x06gain_1\x18\x05 \x01(\x02\x12\x0e\n\x06gain_2\x18\x06 \x01(\x02\x12\x0e\n\x06gain_3\x18\x07 \x01(\x02\x12\x0e\n\x06gain_4\x18\x08 \x01(\x02\x12\x11\n\tfault_ack\x18\t \x01(\r\x12\n\n\x02ts\x18\n \x01(\r\x12\x12\n\nop_idx_aux\x18\x0b \x01(\r\x12\x0b\n\x03\x61ux\x18\x0c \x01(\x02\"\xc8\x03\n\rHyqHpu_rx_pdo\x12\x10\n\x08pressure\x18\x01 \x01(\r\x12\x12\n\nstatusWord\x18\x02 \x01(\r\x12\x16\n\x0evesc1BoardTemp\x18\x03 \x01(\r\x12\x14\n\x0cvesc1MotTemp\x18\x04 \x01(\r\x12\x16\n\x0evesc2BoardTemp\x18\x05 \x01(\r\x12\x14\n\x0cvesc2MotTemp\x18\x06 \x01(\r\x12\x13\n\x0bvesc1ActCur\x18\x07 \x01(\x02\x12\x13\n\x0bvesc1ActSpd\x18\x08 \x01(\r\x12\x13\n\x0bvesc1Status\x18\t \x01(\r\x12\x13\n\x0bvesc2ActCur\x18\n \x01(\x02\x12\x13\n\x0bvesc2ActSpd\x18\x0b \x01(\r\x12\x13\n\x0bvesc2Status\x18\x0c \x01(\r\x12\r\n\x05temp1\x18\r \x01(\r\x12\r\n\x05temp2\x18\x0e \x01(\r\x12\r\n\x05temp3\x18\x0f \x01(\r\x12\x18\n\x10vesc1FBDutyCycle\x18\x10 \x01(\r\x12\x18\n\x10vesc2FBDutyCycle\x18\x11 \x01(\r\x12\x13\n\x0bvesc1Demand\x18\x12 \x01(\x02\x12\x13\n\x0bvesc2Demand\x18\x13 \x01(\x02\x12\x15\n\rpwm1DutyCycle\x18\x14 \x01(\r\x12\x15\n\rpwm2DutyCycle\x18\x15 \x01(\r\"\xce\x01\n\rHyqHpu_tx_pdo\x12\x16\n\x0e\x64\x65mandPressure\x18\x01 \x01(\r\x12\x18\n\x10singlePumpHighLt\x18\x02 \x01(\r\x12\x17\n\x0fsinglePumpLowLt\x18\x03 \x01(\r\x12\x15\n\rHPUDemandMode\x18\x04 \x01(\r\x12\x11\n\tvesc1Mode\x18\x05 \x01(\r\x12\x11\n\tvesc2Mode\x18\x06 \x01(\r\x12\x0f\n\x07\x66\x61n1Spd\x18\x07 \x01(\r\x12\x0f\n\x07\x66\x61n2Spd\x18\x08 \x01(\r\x12\x13\n\x0bsysStateCmd\x18\t \x01(\r')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hyq_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HYQKNEE_RX_PDO._serialized_start=24
  _HYQKNEE_RX_PDO._serialized_end=291
  _HYQKNEE_TX_PDO._serialized_start=294
  _HYQKNEE_TX_PDO._serialized_end=516
  _HYQHPU_RX_PDO._serialized_start=519
  _HYQHPU_RX_PDO._serialized_end=975
  _HYQHPU_TX_PDO._serialized_start=978
  _HYQHPU_TX_PDO._serialized_end=1184
# @@protoc_insertion_point(module_scope)
