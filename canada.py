#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############################################
# Access Canadian Express Entry Application
#############################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'user'
passwordStr = 'pass'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('https://onlineservices-servicesenligne-cic.fjgc-gccf.gc.ca/mycic/gccf?lang=eng&idp=gckey&svc=/mycic/start')

username = browser.find_element_by_name("token1")
username.send_keys(usernameStr)
password = browser.find_element_by_name("token2")
password.send_keys(passwordStr)
signInButton = browser.find_element_by_class_name('btn-primary')
signInButton.click()

cont = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, '_eventId_continue')))
cont.click()

terms = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
terms.click()

answer = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'answer')))
html_source = browser.page_source
if "Question 1" in html_source:
    answerStr = 'Answer 1'
elif "Question 2" in html_source:
    answerStr = 'Answer 2'
elif "Question 3" in html_source:
    answerStr = 'Answer 3'
elif "Question 4" in html_source:
    answerStr = 'Answer 4'
answer.send_keys(answerStr)
contAnswer = browser.find_element_by_class_name('btn-primary')
contAnswer.click()
