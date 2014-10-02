#!/usr/bin/python

import threading
import time
import socket
exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        send_search()
        print "Exiting " + self.name

def send_search():
   print"send_search"
   TCP_IP = '127.0.0.1'
   TCP_PORT = 8080
   BUFFER_SIZE = 10024
   MESSAGE = "Hello world!\n"
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   print "connecting"
   s.connect((TCP_IP, TCP_PORT))
   print "send"
   s.send(MESSAGE)
   print "receiving"
   data = s.recv(BUFFER_SIZE)
   s.close()
   print "received data:", data



# Create new threads
i= 0
thread_array=[]
while ( i < 100 ):
        thread_array.append(  myThread(i, "Thread", i) )
        thread_array[i].start()
        i=i+1

print "Exiting Main Thread"

