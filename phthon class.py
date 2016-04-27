Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> oct(64)
'0100'
>>> hex(64)
'0x40'
>>> hex_numb=hex(64)
>>> type(hex_numb)
<type 'str'>
>>> oct(hex_numb)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    oct(hex_numb)
TypeError: oct() argument can't be converted to oct
>>> oct(100)
'0144'
>>> oct(99)
'0143'
>>> s={'Name':'Sai Teja','Age':21,'Occupation':'Data Scientist'}
>>> s
{'Age': 21, 'Name': 'Sai Teja', 'Occupation': 'Data Scientist'}
>>> s['Occupation']='Analyst'
>>> s
{'Age': 21, 'Name': 'Sai Teja', 'Occupation': 'Analyst'}
>>> s.keys()
['Age', 'Name', 'Occupation']
>>> s.values()
[21, 'Sai Teja', 'Analyst']
>>> for i in range(1,100):
	print i:
		
SyntaxError: invalid syntax
>>> for i in range(1,100):
	print i

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
>>> range(1,5)
[1, 2, 3, 4]
>>> for i in range(1,11):
	if(i%2==0):
		print i

		
2
4
6
8
10
>>> for i in range(1,21):
	if i in range(1,6):
		print i

		
1
2
3
4
5
>>> for i in range(1,13):
	if i in range(1,7):
		print i

		
1
2
3
4
5
6
>>> oct(74)
'0112'
>>> bin(12)
'0b1100'
>>> pen(74)

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    pen(74)
NameError: name 'pen' is not defined
>>> pent(74)

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    pent(74)
NameError: name 'pent' is not defined
>>> cls

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> if i in range(1,10):
	print i:
		
SyntaxError: invalid syntax
>>> for i in range(1,11):
	if i in range(1,6):
		print "Sai"
	elif i in range(6,11):
		print "Vijay"

		
Sai
Sai
Sai
Sai
Sai
Vijay
Vijay
Vijay
Vijay
Vijay
>>> i=6
>>> if i in range(1,7):
	print "True"

	
True
>>> range(1,10,2)
[1, 3, 5, 7, 9]
>>> range(1,10,4)
[1, 5, 9]
>>> range(1,20,3)
[1, 4, 7, 10, 13, 16, 19]
>>> range(1,20,2)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> range(0,20,2)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> 
>>> 
>>> while i in range(1,10):
	print i

	
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6

6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
6
Traceback (most recent call last):
  File "<pyshell#57>", line 2, in <module>
    print i
  File "C:\Python27\lib\idlelib\PyShell.py", line 1356, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> i=0
>>> while i<=10:
	print i
	i=i+1

	
0
1
2
3
4
5
6
7
8
9
10
>>> pow(2,3)
8
>>> pow(4,4)
256
>>> pow(2,5,2)
0
>>> pow(2,5,1)
0
>>> pow(2,5,4)
0
>>> pow(3,4)
81
>>> pow(3,4,4)
1
>>> import time
>>> epoch_now=time.time()
>>> epoch_now
1461211796.882
>>> print epoch_now
1461211796.88
>>> print "The current time in epoch is %s" % epoch_now
The current time in epoch is 1461211796.88
>>> human_readable_format=time.localtime(epoch_now)
>>> print human_readable_format
time.struct_time(tm_year=2016, tm_mon=4, tm_mday=21, tm_hour=9, tm_min=39, tm_sec=56, tm_wday=3, tm_yday=112, tm_isdst=0)
>>> human_readable_format[7]
112
>>> str(human_readable_format[7])
'112'
>>> human_time=time.asctime(human_readable_format)
>>> print human_time
Thu Apr 21 09:39:56 2016
>>> epoch_now=epoch_now-300
>>> print time.asctime(time.localtime(epoch_now))
Thu Apr 21 09:34:56 2016
>>> 
=============================== RESTART: Shell ===============================
>>> import time
>>> epochTime=time.time
>>> epochTime=time.time()
>>> epochTime
1461212431.705
>>> timeTuple=time.localtime(epochTime)
>>> print timeTuple
time.struct_time(tm_year=2016, tm_mon=4, tm_mday=21, tm_hour=9, tm_min=50, tm_sec=31, tm_wday=3, tm_yday=112, tm_isdst=0)
>>> timeStr=time.strftime("%Y-%m-%d %H:%M%S",timeTuple)
>>> timeStr
'2016-04-21 09:5031'
>>> timeStr=time.strftime("%Y-%m-%d %H:%M:%S",timeTuple)
>>> timeStr
'2016-04-21 09:50:31'
>>> dervTuple = time.strptime(timeStr,"%Y-%m-%d %H:%M:%S")
>>> print dervTuple
time.struct_time(tm_year=2016, tm_mon=4, tm_mday=21, tm_hour=9, tm_min=50, tm_sec=31, tm_wday=3, tm_yday=112, tm_isdst=-1)
>>> dervTuple = time.strptime(timeStr)

Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    dervTuple = time.strptime(timeStr)
  File "C:\Python27\lib\_strptime.py", line 467, in _strptime_time
    return _strptime(data_string, format)[0]
  File "C:\Python27\lib\_strptime.py", line 325, in _strptime
    (data_string, format))
ValueError: time data '2016-04-21 09:50:31' does not match format '%a %b %d %H:%M:%S %Y'
>>> dtimeEpoch = time.mktime(dervTuple)
>>> print dtimeEpoch
1461212431.0
>>> dervTuple.tm_yday
112
>>> today=dervTuple.tm_yday
>>> print "Today is %s th day of the year" % today
Today is 112 th day of the year
>>> type(today)
<type 'int'>
>>> str(today)
'112'
>>> tod = str(today)
>>> type(tod)
<type 'str'>
>>> timeStr=time.strftime("%A %Y/%m/%d %H@%M@%S",timeTuple)
>>> timeStr
'Thursday 2016/04/21 09@50@31'
>>> oct(9_
    
SyntaxError: invalid syntax
>>> oct(9)
'011'
>>> hex(9)
'0x9'
>>> hex(16)
'0x10'
>>> list=[1,2,3,4,5,6]
>>> list[1]
2
>>> oct(10)
'012'
>>> bin(10)
'0b1010'
>>> def show(str):
	#This prints a string
	print str
	return

>>> show("Sai-Data Scientist")
Sai-Data Scientist
>>> def show(str):
	#This prints a string
	print str

	
>>> show("Sai-Data Scientist")
Sai-Data Scientist
>>> "Sai"
'Sai'
>>> def show(str):
	"This prints a string"
	print str
	return

>>> show("Sai Teja-Data Scientist")
Sai Teja-Data Scientist
>>> show(5)
5
>>> def printinfo(arg1,*vartuple):
	"This print all the variables passed to this function"
	print "Output is:"
	print arg1
	for var in vartuple:
		print var

		
>>> printinfo(10)
Output is:
10
>>> printinfo(10,20,30)
Output is:
10
20
30
>>> def printinfo(*arg1,*vartuple):
	"This print all the variables passed to this function"
	print "Output is:"
	print arg1
	for var in vartuple:
		print var
		
SyntaxError: invalid syntax
>>> def printaasc(*vartuple):
	print vartuple

	
>>> printaasc()
()
>>> lambda()
SyntaxError: invalid syntax
>>> lambda a,b:a+b
<function <lambda> at 0x02ADAFB0>
>>> sum=lambda a,b:a+b
>>> print sum(1,3)
4
>>> sum(10,20)
30
>>> lambda a,b,c:a+b
<function <lambda> at 0x02ADAFB0>
>>> sum=lambda a,b,c:a+b
>>> sum(10,20)

Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    sum(10,20)
TypeError: <lambda>() takes exactly 3 arguments (2 given)
>>> sum(1,*,3)
SyntaxError: invalid syntax
>>> var=100
>>> if(var==100):
	print "TRUE"

TRUE
>>> var=100
>>> if(var==100):
	print var

	
100
>>> var=100
>>> var==100
True
>>> var=100
>>> if(var==100):
	print "Sai"
	print "Teja"
print "Data Scientist"
SyntaxError: invalid syntax
>>> var=100
>>> if
SyntaxError: invalid syntax
(
>>> var=100
>>> if(var==100)
SyntaxError: invalid syntax
>>> var=100
>>> if(var==100):
	print"sai"
	print"sai2"
	print"vijay"

	
sai
sai2
vijay
>>> 
======================= RESTART: C:/Python27/Ifelse.py =======================
sai
teja
Data Scientist
>>> for i in range(0.1,1.0,0.1):
	print i

	

Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    for i in range(0.1,1.0,0.1):
TypeError: range() integer end argument expected, got float.
>>> range(1,3,1)
[1, 2]
>>> xrange(1,3,1)
xrange(1, 3)
>>> xrange(1,3,2)
xrange(1, 3, 2)
>>> xrange(1,10,1)
xrange(1, 10)
>>> xrange(1,10)
xrange(1, 10)
>>> xrange(1,10,3)
xrange(1, 10, 3)
>>> xrange(0.1,1.0,0.1)

Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    xrange(0.1,1.0,0.1)
TypeError: integer argument expected, got float
>>> xrange(0.1,1)

Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    xrange(0.1,1)
TypeError: integer argument expected, got float
>>> 
=============================== RESTART: Shell ===============================
>>> xrange(1,5,1)
xrange(1, 5)
>>> xrange(1,5)
xrange(1, 5)
>>> for i in xrange(1,5,1):
	print i

	
1
2
3
4
>>>  >
