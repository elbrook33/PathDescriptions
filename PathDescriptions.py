import os
import urllib

from gi.repository import Nautilus, GObject

class PathDescriptions(GObject.GObject, Nautilus.ColumnProvider, Nautilus.InfoProvider):
  def __init__(self):
    self.table = self.get_table()

  def get_columns(self):
    return Nautilus.Column(
      name="NautilusPython::path_description_column",
      attribute="path_description",
      label="Description",
      description="Explains system directories"),

  def update_file_info(self, file):
    if file.get_uri()[7:] in self.table:
      file.add_string_attribute("path_description", self.table[file.get_uri()[7:]])
    else:
      file.add_string_attribute("path_description", "")

  def get_table(self):
    place = 0 # 0) outside, 1) header, 2) body
    pivot = -1
    table = {}
    file = open("/usr/share/path-descriptions/Short-descriptions.md")
    for line in file:
      if line[0] == '-':
        pivot = line.find(" -")+1
        if place == 2:
          place = 0
        else:
          place = place+1
      else:
        if place == 2:
          table[line[0:pivot].strip()] = line[pivot:].strip()
    return table

