# -*- coding: utf-8 -*-
import datetime


class FileMerge:
  def __init__(self, path1):
    self.path1 = path1
    self.start = datetime.datetime.now()

  def __enter__(self):
    with open(self.path1) as file:
      list1 = file.readlines()
    return list1


  def __exit__(self, exc_type, exc_val, exc_tb ):
    self.end = datetime.datetime.now()
    print(self.end - self.start)

with FileMerge("HW8.txt") as sorted_list:
  print(sorted_list)
