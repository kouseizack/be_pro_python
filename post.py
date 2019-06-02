import serial
import time
import json
import requests
import matplotlib.pyplot as plt


#ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=.5)
url = "http://ec2-13-127-141-200.ap-south-1.compute.amazonaws.com:3000/"

def write_data():
	f = open("geez.txt",'w')
	f.close()
	f = open("geez.txt",'w')
	#f.write(incoming)
	f.close()

start_time = time.time()
k = 0
while True:
    #ser.write('Hello User \r\n')         
    time.sleep(0.5)
    #incoming = ser.readline().strip()
    #print 'Received Data : '+ incoming
    #t = incoming.split(" ")
    #print t
    payload = {'app_id':'ajay','consumption':'yo'}
    print('mar')
    e = requests.post(url,data=payload)
    elapsed_time = time.time()-start_time
    x = str(elapsed_time).split(".")
    print('in')
    if(int(x[0]) % 5 == 0):
		write_data()
	
		



	
