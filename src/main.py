from urllib.request import urlopen
import subprocess

def getLocalIP():
    try:
        proc = subprocess.Popen('./local.ip.sh', stdout=subprocess.PIPE)
        output = proc.stdout.read()
        localIP = output.decode('utf-8')
        localIP = localIP.strip("\n")
        if localIP == "" :
            localIP = "(empty)"
        return localIP.strip("\n")
    except Exception as e:
        print( "[CRASH] Could not get local IP address.", e )

def getPublicIP():
    try:
        globalIP = urlopen('http://ipinfo.io/ip').read().decode('utf-8')
        return globalIP.strip("\n")
    except Exception as e:
        print( "Could not get global IP address. Do you have an internet connection?")

if __name__ == '__main__':
    localIP = getLocalIP()
    publicIP = getPublicIP()
    format = '%-10s%-15s'
    print( format % ("Local IP", localIP) )
    print( format % ("Public IP ", publicIP) )
