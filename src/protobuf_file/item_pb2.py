# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: item.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='item.proto',
  package='',
  serialized_pb=_b('\n\nitem.proto\"G\n\x04Item\x12\r\n\x05title\x18\x10 \x01(\t\x12\r\n\x05price\x18\x11 \x01(\r\x12\x10\n\x08num_sell\x18\x12 \x01(\r\x12\x0f\n\x07img_url\x18\x13 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='Item.title', index=0,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='Item.price', index=1,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_sell', full_name='Item.num_sell', index=2,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='img_url', full_name='Item.img_url', index=3,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=85,
)

DESCRIPTOR.message_types_by_name['Item'] = _ITEM

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
  DESCRIPTOR = _ITEM,
  __module__ = 'item_pb2'
  # @@protoc_insertion_point(class_scope:Item)
  ))
_sym_db.RegisterMessage(Item)


# @@protoc_insertion_point(module_scope)
