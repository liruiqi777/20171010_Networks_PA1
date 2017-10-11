# UDPPingerClient.py
from socket import *
import time

clientSocket = socket(AF_INET, SOCK_DGRAM)
IP = '139.140.209.193'
for x in range(0, 10):
    msg = "Ping {} {}".format(x+1, time.time())
    # print (msg)
    returnMsg = clientSocket.sendto(msg, (IP.encode(), 12000))
    clientSocket.settimeout(1.00)
    timerStart = time.time()

    print ("Ping #{}:".format(x+1))

    try:
        message, address = clientSocket.recvfrom(1024)
        timerStop = time.time()
        print ("- Time Elapse: {}".format(timerStop-timerStart))
        print ("- The message is \'{}\'".format(message))
    except timeout:
        print ("- Request timed out")

    print("\n")
