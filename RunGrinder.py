__author__ = 'minosniu'
import sys
import os

path_root = 'D:\\Subject01_e2_example'

expt = 'FES_reaching'
date = '20150902'
analyst = 'zcwaxs'
addr = 'mongodb://localhost:27017/'
patient = 'YJZ'
side = 'left'
movement = 'forward_reaching'

if __name__ == '__main__':
    #for gd in [0, 100, 200]:
    #    for gs in [0, 100, 200]:
    #for gd in [0]:
    #   for gs in [0]:
    path = path_root
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) if not f.startswith('.')]
    for f in files:
        fullname = os.path.abspath(os.path.join(path, f))
        print('Processing "%s"' % (f))
        print('python Grinder.py "%s" "%s" "%s" "%s" "%s" "%s" "%s" "%s"' % 
            (fullname, expt, date, analyst, addr, patient, side,movement))
        os.system('python Grinder.py "%s" "%s" "%s" "%s" "%s" "%s" "%s" "%s"' % 
            (fullname, expt, date, analyst, addr, patient, side,movement))
