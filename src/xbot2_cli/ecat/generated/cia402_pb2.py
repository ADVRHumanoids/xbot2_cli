# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cia402.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63ia402.proto\x12\x08iit.advr\"\xec\x02\n\rCia402_rx_pdo\x12\x12\n\nstatusword\x18\x01 \x02(\r\x12\x13\n\x0bmodes_of_op\x18\x02 \x02(\x05\x12\x11\n\tmotor_pos\x18\x03 \x02(\x02\x12\x11\n\tmotor_vel\x18\x04 \x02(\x02\x12\x10\n\x08link_pos\x18\x05 \x02(\x02\x12\x10\n\x08link_vel\x18\x06 \x02(\x02\x12\x0f\n\x07\x63urrent\x18\x07 \x02(\x02\x12\x0e\n\x06torque\x18\x08 \x02(\x02\x12\x14\n\x0c\x64\x65manded_pos\x18\t \x01(\x02\x12\x14\n\x0c\x64\x65manded_vel\x18\n \x01(\x02\x12\x18\n\x10\x64\x65manded_current\x18\x0b \x01(\x02\x12\x17\n\x0f\x64\x65manded_torque\x18\x0c \x01(\x02\x12\x16\n\x0e\x63ontrol_effort\x18\r \x01(\x02\x12\x12\n\nmotor_temp\x18\x0e \x01(\x02\x12\x12\n\ndrive_temp\x18\x0f \x01(\x05\x12\x12\n\nerror_code\x18\x10 \x01(\x05\x12\x14\n\x0c\x65rror_report\x18\x11 \x01(\t\"\xb6\x01\n\rCia402_tx_pdo\x12\x15\n\rtarget_torque\x18\x01 \x02(\x02\x12\x12\n\ntarget_pos\x18\x02 \x02(\x02\x12\x12\n\ntarget_vel\x18\x03 \x02(\x02\x12\x16\n\x0etarget_current\x18\x04 \x02(\x02\x12\x0e\n\x06gain_0\x18\x05 \x01(\x02\x12\x0e\n\x06gain_1\x18\x06 \x01(\x02\x12\x0e\n\x06gain_2\x18\x07 \x01(\x02\x12\x0e\n\x06gain_3\x18\x08 \x01(\x02\x12\x0e\n\x06gain_4\x18\t \x01(\x02')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cia402_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CIA402_RX_PDO._serialized_start=27
  _CIA402_RX_PDO._serialized_end=391
  _CIA402_TX_PDO._serialized_start=394
  _CIA402_TX_PDO._serialized_end=576
# @@protoc_insertion_point(module_scope)
