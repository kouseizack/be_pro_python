import time
a = "123"
b = int(a)+23
print(b)
start_time = time.time()
x = 0
def call_me():
	print(x)

time.sleep(3)
print(time.strftime("%H:%M:%S", time.gmtime(time.time()-start_time)))
while True:
	x = x+1
	time.sleep(2)
	#if(x % 2 == 0):
	call_me()


