# UBC Course Seats Helper

## Motivation
Sometimes it might be annoying to monitor if a course has empty seats or not, if you want to register into a course that is full without a waitlist. This program aims to solve this problem by monitoring automatically and send you notification email once there is empty seats.



## Functions
Users can use this program to:
- ***monitor*** several courses
- ***receive email notification*** once the course has empty seats
- ***receive a pop-up message*** which self-destruct after 10 seconds once the course has empty seat



## Steps to run this program
Steps are outlined here, as well as inside main.py
1. Create a file *constants.py* and add your
    - *gmail_ac* : sender gmail account
    - *gmail_pw* : sender gmail password
    - *email_to*: address of receving notificaion email

    Remark: You might have to allow "Less secure app access" first
    at: https://www.google.com/settings/security/lesssecureapp

2. In main.py, add courses you want to monitor following the example below
    >   course_codes.append("XXXX YYY ZZZ")
    - *XXXX*: subject, eg CPSC
    - *YYY*: class, eg 213
    - *ZZZ*: section, eg L2D

3. In main.py, set time interval(unit: minute) by assigning the interval to variable *sleep_time* for fetching data

4. Run main.py to start monitoring, enjoy!



### Disclaimer   
This program is for web scraping and automating sending email practice only.
It is user's sole responsibilty to comply with UBC CWL and SSC usage policy.
Any consequences of violating UBC CWL and SSC usage policy shall be borne by the user,
and are unrelated to the developer of this program.