import smtplib
import configparser
from logging import log
import os
import subprocess
import matplotlib.pyplot as plt
import numpy as np
from configparser import ConfigParser
import time

def host_monitor(*args):
    host = args[0]
    credentials = args[1]
    intentos = 0
    while True:

        if(subprocess.check_output(["ping", "-c", "5", host])):
            intentos = 0
        elif intentos<3:
            intentos =+ 1
        elif intentos==3:
            mail_service()
            intentos = 0

        response = os.system("ping " + " -n 5 "+host+">> log.txt")

        print("------------------------")


host_monitor("www.google.es", "a")

def obtener_latencias():
    texto = ""
    with open("D:\PyCharm\Ejercicios\log.txt", encoding='utf8' ,mode="r") as log:
        texto = log.readlines()
        for word in texto:
            if word.startswith('Respuesta desde '):
                begin = word.find("tiempo=")
                end = word.find("ms", begin)
                error_line = word[begin+len(str("tiempo=")):end]
                print(error_line)



def graficas():
    #para pilla los valores:
        #Minimos = min(lista de numeros donde esten guardos)
        #Maximo = max(lista de numeros donde esten guardos)
        #Media = sum(lista de numeros donde esten guardos)/len(de la misma lista)

    ax = "pillar los datos de los valores ms del log"
    x = list(range(0,80))
    y = list(range(0,51))
    plt.plot(x, y)


def mail_service():
    config = ConfigParser()
    config.read('config.ini')

    sender = config['email']['sender']
    reciver  = config['email']['reciver']
    #password = config['email']['password']
    smtp_server = config['email']['server']
    server_port = config['email']['port']

    msg = "Server is down!"
    server = smtplib.SMTP(smtp_server, server_port)
    server.starttls()
    #server.login(sender, password)
    server.sendmail(sender, reciver, msg)
    server.quit()

#EJEMPLO de como es el config
#[DEFAULT]
#title = Hello world
#compression = yes
#compression_level = 9

#[email]
#host = 127.0.0.1
#user = username
#pass = password
