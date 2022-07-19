import pyfiglet
import socket
import sys



X = '\033[1;33m'
C = '\033[2;35m'
Y = '\033[1;34m'

logo = pyfiglet.figlet_format(((('ipnet'))))
print((((C+logo))))


print(X+'''
                                                  INSTA:@__so1dier
''')










print(Y+'[+]',X+'Enter your Dns Or target:')













hostname = input()










ip=socket.gethostbyname(hostname)










print ('host name ls:' ,C+hostname, X+'\n' 'target ip is:',C+ip)