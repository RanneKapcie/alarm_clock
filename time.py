#/usr/bin/python
# -*- coding: utf-8 -*-

import time
import webbrowser
import random

print 'O której chcesz random linka?'
print 'Użyj tego formatu: \nPrzykład: 12:00:00'
alarm = raw_input ( '> ')

Time = time.strftime('%H:%M:%S')

with open ('links.txt') as f:
	content = f.readlines()

while Time != alarm:
	print "Jest godzina", Time
	Time = time.strftime('%H:%M:%S')
	time.sleep(1)

if Time == alarm:
	print "Czas na inbe!!!!!!!!!!"
	random_link = random.choice(content)
	webbrowser.open(random_link) 


