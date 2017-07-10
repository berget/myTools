#!/usr/bin/env python

import threading
import subprocess
import sys

# setup thread


class myThread(threading.Thread):

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        ping(self.name, self.counter)


def ping(threadName, IPnumber):

    cmd = ['ping', '-c', '1', str(IPnumber)]

    p_cmd = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    formatCmd = subprocess.Popen(
        ['grep', 'ttl'], stdin=p_cmd.stdout, stdout=subprocess.PIPE)
    stdout, stderr = formatCmd.communicate()
    if formatCmd.returncode > 0:
        pass
    else:
        ipdata = stdout.split(' ')
        iplist.append(ipdata[3] + ipdata[5])


if __name__ == '__main__':

    flag = 0
    set_IP = ''
    for n in sys.argv[1].split('.'):
        try:
            if type(int(n)) is int:
                set_IP += n + '.'
            flag += 1
            if flag == 3:
                break
        except:
            sys.exit('input error')

    print(set_IP)

    global iplist
    iplist = []
    number = 255
    while number:

        IP = set_IP + str(number)
        Thread1 = myThread(IP)
        Thread1.start()

        number -= 1

    print("Exiting Main Thread")
    iplist.sort()
    for ip in iplist:
        print(ip)
