import time
f=open("/testfile/testfile","w")
x='asdfasdfasdf' * 1000000
try:
  while True:
    f.write(x) 
except:
  print "execpt"


f=open("/testfile/testfile","r")
time.sleep(100000)
