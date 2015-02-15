#!/usr/bin/env python

import threading
import subprocess

class myThread(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        ping(self.name, self.counter)
                                                                                 
def ping(threadName, IPnumber):

    cmd = ['ping','-c','1', str(IPnumber)]

    p_cmd = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    formatCmd =  subprocess.Popen(['grep','ttl'], stdin=p_cmd.stdout, stdout=subprocess.PIPE)
    stdout, stderr = formatCmd.communicate()
    if formatCmd.returncode > 0:
        pass
        #print stderr
    else:
        print stdout,



if __name__ == '__main__' :
	
	set_IP = '192.168.3.'
	number = 255	
	while number:
		
		IP = set_IP + str( number )
		Thread1 = myThread( IP )
		Thread1.start()
		number -= 1
	print "Exiting Main Thread"
