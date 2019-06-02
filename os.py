import serial
import time
import json
import requests
 
ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=.5)
url = "http://localhost:3000/" 

def write_data():
	f = open("geez.txt",'w')
	f.close()
	f = open("geez.txt",'w')
	f.write(incoming)
	f.close()

start_time = time.time()
k = 0
while True:
    ser.write('Hello User \r\n')         
    time.sleep(0.5)
    incoming = ser.readline().strip()
    print 'Received Data : '+ incoming
    t = incoming.split(" ")
    payload = {'app_id':t[0],'consumption':t[1],'app_id':t[2],'consumption':t[3]}
    e = requests.post(url,data=payload)
    elapsed_time = time.time()-start_time
    x = str(elapsed_time).split(".")
    print('in')
    if(int(x[0]) % 5 == 0):
		write_data()
		



	
