from operator import truediv
import constants
import requests
from bs4 import BeautifulSoup
from tkinter import *
import tkinter.messagebox
import time
from datetime import datetime
from tkinter.messagebox import Message
import smtplib

gmail_ac = constants.gmail_ac
gmail_pw = constants.gmail_pw
email_from = gmail_ac
email_to = constants.email_to



def message_box(title, message):
    """Show message box with title and message"""
    MESSAGE_TIME = 2000 # in ms
    root = Tk() 
    root.withdraw()
    try:
        root.after(MESSAGE_TIME, root.destroy)  
        Message(title=title, message=message, master=root).show()
    except TclError:
        pass
    #tkinter.messagebox.showinfo(title,  message)
    
def construct_url(course_code): 
    """return url given ccorrect course_code"""
    s = course_code.split(" ")
    dept = s[0]
    course = s[1]
    section = s[2]
    return ("https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=" +
            dept + "&course=" + course + "&section=" + section)

def find_seats(course_code):
    """function for finding number of seats of courses_code"""
    url = construct_url(course_code)
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find("table", class_="'table")
    
    data = []
    rows = table.find_all('tr')
    
    #ref: https://stackoverflow.com/questions/23377533/python-beautifulsoup-parsing-table
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        #data.append([ele for ele in cols if ele]) # Get rid of empty values
        data.append(cols)
    
    print(course_code, data[0], data[1])    
    if (data[0][0] == 'Total Seats Remaining:' and data[0][1] != '0'):
        current_time = datetime.now().strftime("%H:%M:%S, %d/%m/%Y")
        title = course_code + ' HAS SEAT = ' + data[0][1] + " @ " + current_time
        email_text = email_text_const(title)
        #send_email(email_text,gmail_ac,gmail_pw,email_from,email_to)
        message_box('Seat Found', title)
        return True

    return False
        
    
    
def send_email(message,gmail_ac,gmail_pw,email_from,email_to):
    """function sending a email"""
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_ac, gmail_pw)
        server.sendmail(email_from, email_to, message)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong..., email is not sent')    
    
def email_text_const(title):
    body = title + "\nSwap: https://courses.students.ubc.ca/cs/courseschedule?pname=regi_sections&tname=regi_sections"
    s = """\
From: %s
To: %s
Subject: %s

%s
""" % (email_from, email_to, title, body)
    #print(s)
    return s