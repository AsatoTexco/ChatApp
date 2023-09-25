 
import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget 
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition,WipeTransition, SlideTransition
from kivy.core.window import Window
from kivy.config import Config
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ReferenceListProperty
from kivy.graphics.texture import Texture
from kivy.graphics import *
import time
import os
import threading
import time
from datetime import datetime
import socket
from requests import get



remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

remote_socket.connect(("192.168.100.10", 2006))
print("conect")
 
    
remote_socket.send(bytes("remote_msg",'utf-8'))
remote_msg = ""