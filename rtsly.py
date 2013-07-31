#Indian Railways Running Train Status Tracker [RTSly]

import os,urllib2,time,random,datetime
from BeautifulSoup import BeautifulSoup as BS
if not os.path.exists("sendsms.auth"):
	user=raw_input("Enter fullonsms.com login details:\nEnter Username: ")
	pas=raw_input("Enter Password: ")
	s = "[Login]\nusername = "+user+"\npassword = "+pas+"\n\n[Phonebook]\n\n[Auth]\nlogindone = http://fullonsms.com/landing_page.php\nloginpage = http://fullonsms.com/login.php\nsms_sent = http://fullonsms.com/MsgSent.php\nsendsms = http://fullonsms.com/home.php\nlogincheck = http://fullonsms.com/login.php\n"
	f = open("sendsms.auth",'w')
	f.write(s)
	f.close()

user='1'
while len(user) != 10:
	user=raw_input("Enter Recepient's Mobile No.: ")
while True:
	try:
		print "Sending Test SMS"
		#For Linux uncomment the next line and comment the line after it
		#os.system('./sendsms.py '+user+' "Test Message Sent from RTSly #%d"  -t ./sendsms.auth'%random.randint(1000,9999))
		os.system('sendsms.py '+user+' "Test Message Sent from RTSly #%d"  -t sendsms.auth'%random.randint(1000,9999))
	except Exception, e:
		print e
		user=raw_input("Invalid Creds !\nRe-Enter fullonsms.com login details:\nEnter Username: ")
		pas=raw_input("Enter Password: ")
		s = "[Login]\nusername = "+user+"\npassword = "+pas+"\n\n[Phonebook]\n\n[Auth]\nlogindone = http://fullonsms.com/landing_page.php\nloginpage = http://fullonsms.com/login.php\nsms_sent = http://fullonsms.com/MsgSent.php\nsendsms = http://fullonsms.com/home.php\nlogincheck = http://fullonsms.com/login.php\n"
		f = open("sendsms.auth",'w')
		f.write(s)
		f.close()					
	else:
		break

tno=raw_input("Gimme the Train details\nTrain No.: ")
tday=5
while tday not in range(5):
	tday=int(raw_input("0 - Today\n1 - Yesterday\n2 - 2 Days Ago\n3 - 3 Days Ago\n4 - 4 Days Ago\nStart Day: "))

print "Tracking Train..."


sentsms=1;
mydict={}
errorlevel=0
checked=0

def track():
	global sentsms
	global mydict
	global tno
	global errorlevel
	global checked
	while True:
		url="http://onthego.trainenquiry.com/train/eta_data?q="+str(tno)+"&s="+str(tday)
		try:
			response=urllib2.urlopen(url, timeout=50)
		except Exception, e:
			print "Something went wrong !! :( \nCheck Your Internet Connection\n%s"%e
			errorlevel=errorlevel+1
			# # if errorlevel>3 and raw_input("\n\nRe-enter Train no. ? (y/n): ")=='y':
			# # 	errorlevel=0
			# 	#tno=raw_input("Enter Train No.: ")
			# 	print tno
			# elif errorlevel>3:
			# 	errorlevel=0
			print "Checking..."
		else:
			break

	try:
		the_response=response.read()
		soup=BS(the_response)
	except Exception, e:
		print "%r"%e
	mylist=[]
	try:
		for i in range(3):
			mylist.append(str(soup.find('tr',attrs={'class':'even'}).findAll('td')[i].getText()))
	except Exception, e:
		return

	try:
		if (not mydict.has_key('u')) or (mydict['u'] != mylist[0] or mydict['e'] != mylist[1] or mydict['d'] != mylist[2]):
			#For Linux uncomment the next line and comment the line after it
			#os.system('./sendsms.py '+user+' "#%d   TRAIN NO - %s   UPCOMING STATION - %s  ETA - %s   DELAY - %s   Checked @ %s"  -t ./sendsms.auth'%(random.randint(100,999),tno,mylist[0],mylist[1],mylist[2], str(datetime.datetime.now().time().strftime("%I:%M:%S %p"))))
			os.system('sendsms.py '+user+' "#%d   TRAIN NO - %s   UPCOMING STATION - %s  ETA - %s   DELAY - %s   Checked @ %s"  -t sendsms.auth'%(random.randint(100,999),tno,mylist[0],mylist[1],mylist[2], str(datetime.datetime.now().time().strftime("%I:%M:%S %p"))))
			sentsms=sentsms+1
			mydict['u'],mydict['e'],mydict['d']=tuple(mylist)
		else:
			print "Nothing New\n"
		checked=1
	except Exception, e:
		print "%r"%e
		checked=0
		pass
round=0
while True:
	print "Checking..."
	try:
		while checked==0:
			round+=1
			print "Check Round %d"%round
			track()
	except Exception, e:
		print "Check Train Name / Start Day %r"%e 
		pass
	print "Waiting..."
	time.sleep(600)	#Wait 600seconds (5mins)
	checked=0