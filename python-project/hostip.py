# importing socket library
import socket
import sys

def get_hostname_IP(hostname):
    
    try:
        print (f'Hostname: {hostname}')
        print (f'IP: {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print (f'Invalid Hostname, error raised is {error}')


if __name__ == '__main__' :
    arguments=sys.argv
    get_hostname_IP(arguments[1])
