import constants
import requests
import functions
from bs4 import BeautifulSoup
from tkinter import *
import tkinter.messagebox
import time
from datetime import datetime
import smtplib
course_codes = []

###################################################################
# TODO 1. Please add your
# a. gmail_ac : sender gmail account
# b. gmail_pw : sender gmail password
# c. email_from : address of receving notificaion email
# in the file constants.py (you might need to create one by yourself)
# 
# Remark: You might have to allow "Less secure app access" first
# ref: https://www.google.com/settings/security/lesssecureapps
###################################################################

################################################################
# TODO 2. Add courses you want to monitor following the example below
# course_codes.append("XXXX YYY ZZZ")
# XXXX: subj, eg CPSC
# YYY: class, eg 213
# ZZZ: section, eg L2D
################################################################
course_codes.append("BIOL 111 2W1")
course_codes.append("CPSC 213 L2D")


################################################################
# TODO 3. Set time interval(unit: minute) for fetching data
# Disclaimer:   This program is for web scraping and automating sending email practice only.
#               This is user's sole responsibilty to comply with UBC CWL and SSC usage policy.
#               Any consequences of violating UBC CWL and SSC usage policy shall be borne by the user,
#               and are unrelated to the developer of this program.
###############################################################
SLEEP_TIME = 5



###############################################################
# Do not modifiy below
###############################################################
current_time = datetime.now().strftime("%H:%M:%S, %d/%m/%Y")

while True:
    print(datetime.now().strftime("%H:%M:%S, %d/%m/%Y"))
    for c in course_codes[:]:
        if (functions.find_seats(c)): 
            course_codes.remove(c)
        
    time.sleep(SLEEP_TIME*60) 
