import serial
import time 
ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=.5)
 
def write_data():
	f = open("geez.txt",'w')
	f.close()
	f = open("geez.txt",'w')
	f.write(incoming)
	f.close()

start_time = time.time()
while True:
    ser.write('Hello User \r\n')         # write a Data
    time.sleep(0.5)
    incoming = ser.readline().strip()
    print 'Received Data : '+ incoming
    elapsed_time = time.time()-start_time
    x = str(elapsed_time).split(".")
    if(int(x[0]) % 5 == 0):
	write_data()




	
