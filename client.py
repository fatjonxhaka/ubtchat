import socket 
import threading 
from tkinter import *
from tkinter import font 
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import db


class ChatGeneral:
    ### Informacionet kryesore 
    PORT = 5080
    SERVER = "127.0.0.1"
    ADDRESS = (SERVER, PORT) 
    FORMAT = "utf-8"
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect(ADDRESS) 
