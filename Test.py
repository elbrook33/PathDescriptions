import os
import urllib

from gi.repository import Nautilus, GObject

class CaptionTest(GObject.GObject, Nautilus.ColumnProvider, Nautilus.InfoProvider):
  def __init__(self):
    pass

  def get_columns(self):
    return Nautilus.Column(
      name="NautilusPython::test_column",
      attribute="test_attr",
      label="Test",
      description="Test for icon captions"),

  def update_file_info(self, file):
    file.add_string_attribute("test_attr", "Testing")

