# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from scout_msgs/ScoutLightCmd.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ScoutLightCmd(genpy.Message):
  _md5sum = "4efcbd363caf677fd8138923f982df13"
  _type = "scout_msgs/ScoutLightCmd"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint8 LIGHT_CONST_OFF = 0
uint8 LIGHT_CONST_ON = 1
uint8 LIGHT_BREATH = 2
uint8 LIGHT_CUSTOM = 3

bool enable_cmd_light_control
uint8 front_mode
uint8 front_custom_value
uint8 rear_mode
uint8 rear_custom_value
"""
  # Pseudo-constants
  LIGHT_CONST_OFF = 0
  LIGHT_CONST_ON = 1
  LIGHT_BREATH = 2
  LIGHT_CUSTOM = 3

  __slots__ = ['enable_cmd_light_control','front_mode','front_custom_value','rear_mode','rear_custom_value']
  _slot_types = ['bool','uint8','uint8','uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       enable_cmd_light_control,front_mode,front_custom_value,rear_mode,rear_custom_value

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ScoutLightCmd, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.enable_cmd_light_control is None:
        self.enable_cmd_light_control = False
      if self.front_mode is None:
        self.front_mode = 0
      if self.front_custom_value is None:
        self.front_custom_value = 0
      if self.rear_mode is None:
        self.rear_mode = 0
      if self.rear_custom_value is None:
        self.rear_custom_value = 0
    else:
      self.enable_cmd_light_control = False
      self.front_mode = 0
      self.front_custom_value = 0
      self.rear_mode = 0
      self.rear_custom_value = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_5B().pack(_x.enable_cmd_light_control, _x.front_mode, _x.front_custom_value, _x.rear_mode, _x.rear_custom_value))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 5
      (_x.enable_cmd_light_control, _x.front_mode, _x.front_custom_value, _x.rear_mode, _x.rear_custom_value,) = _get_struct_5B().unpack(str[start:end])
      self.enable_cmd_light_control = bool(self.enable_cmd_light_control)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_5B().pack(_x.enable_cmd_light_control, _x.front_mode, _x.front_custom_value, _x.rear_mode, _x.rear_custom_value))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 5
      (_x.enable_cmd_light_control, _x.front_mode, _x.front_custom_value, _x.rear_mode, _x.rear_custom_value,) = _get_struct_5B().unpack(str[start:end])
      self.enable_cmd_light_control = bool(self.enable_cmd_light_control)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_5B = None
def _get_struct_5B():
    global _struct_5B
    if _struct_5B is None:
        _struct_5B = struct.Struct("<5B")
    return _struct_5B
