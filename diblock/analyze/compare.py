#!/usr/bin/env python2.7

from pscf.sweep import *
import sys, os

# Prefix (i.e., directory path) for output files
prefix = 'out/'

# Read lamellar phase
lam = Sweep('../lam/sweep/out')
string = lam.write('block_length[0][0]','f_Helmholtz - f_homo')
file = open(prefix + 'lam','w')
file.write(string)
file.close()

## Read hex phase
hex = Sweep('../hex/sweep/out')
string = hex.write('block_length[0][0]','f_Helmholtz - f_homo')
file = open(prefix + 'hex','w')
file.write(string)
file.close()
 
# Read gyr phase
gyr = Sweep('../gyr/sweep/out')
string = gyr.write('block_length[0][0]','f_Helmholtz - f_homo')
file = open(prefix + 'gyr','w')
file.write(string)
file.close()

## Read bcc phase
#bcc = Sweep('../bcc/sweep/ref')
#string = bcc.write('block_length[0][0]','f_Helmholtz - f_homo')
#file = open(prefix + 'bcc','w')
#file.write(string)
#file.close()
