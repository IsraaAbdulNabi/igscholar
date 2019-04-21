from Models import Publication
import re
import pprint
import config


class Author(object):
  def __init__(self, __data):
    self.name=__data["name"]
    self.role=__data["role"]
    self.university=__data["uni"]
    self.email=__data["email"]
    self.intrestes=__data["intrests"]
    self.h_index= __data["h_index"]
    self.citations=__data["citations"]
    self.pic_url=__data["pic_url"]
    self.last_active_year= __data["last_active_year"]

  def print_auther(self):
      print("NAME: "+self.name)
      print(self.role+ " " + self.university)
      print ("Verified email at " + self.email)
      print( i for i in self.intrestes)