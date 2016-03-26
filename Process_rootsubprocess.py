#!/usr/bin/env python

from subprocess import Popen, PIPE
from re import split
from sys import stdout
from __future__ import print_function
import os
import platform

class Proc(object):
    ''' Data structure for a processes . The class properties are
    process attributes '''
    def __init__(self, proc_info):
        self.user = proc_info[0]
        self.pid = proc_info[1]
        
    def to_str(self):
        ''' Returns a string containing minimalistic info
        about the process : user, pid, and command '''
        return '%s %s %s' % (self.user, self.pid, self.cmd)

def get_processlist():
    ''' Retrieves a list [] of Proc objects representing the active process list '''
    processlist = []
    sub_proc = Popen(['ps', 'aux'], shell=False, stdout=PIPE)
    sub_proc.stdout.readline()
    for line in sub_proc.stdout:
        proc_info = split(" *", line.strip())
        processlist.append(Proc(proc_info))
    return processlist

if __name__ == "__main__":
    processlist = get_processlist()
    #Show the minimal proc list (user, pid, cmd)
    stdout.write('Process list:n')
    for proc in processlist:
        stdout.write('t' + proc.to_str() + 'n')


# Define total number of processes and list  out #
def process_list():

    pids = []
    for subdir in os.listdir('/usr/local/brs/bin'):
        if subdir.isdigit():
            pids.append(subdir)

    return pids


if __name__=='__main__':

    pids = process_list()
    print('Total number of running processes:: {0}'.format(len(pids)))
