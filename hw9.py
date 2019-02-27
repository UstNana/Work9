# -*- coding: utf-8 -*-
import datetime


k = 0
cookbook = {}
big_list = []

class FileMerge:
    def __init__(self, path1):
        self.path1 = path1
        self.start = datetime.datetime.now()

    def __enter__(self):
        with open("HW8.txt") as file:
            while True:
                meal = file.readline().strip()
                list_meal = meal.split()
                quantity = file.readline().rstrip('\n')
                h = quantity.split()
                for i in h:
                    i = int(i)
                    for k in range(i):
                        list_1 = file.readline().strip()
                        l_list_1 = list_1.split()
                        big_list.append({'ingridient_name': l_list_1[0], 'quantity': l_list_1[2], 'measure': l_list_1[4]})
                        for eat in list_meal:
                          if eat not in cookbook.keys():
                            cookbook[eat] = big_list

                    file.readline()
        return cookbook

    def __exit__(self, exc_type, exc_val, exc_tb ):
      self.end = datetime.datetime.now()
      print(self.end - self.start)

with FileMerge("HW8.txt") as sorted_list:
  print(sorted_list)
