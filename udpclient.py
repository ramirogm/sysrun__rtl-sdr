#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# * UDP modifications: Original Code by Olgierd Pilarczyk
# * Extended by Frederik Granna <rtlsdr@granna.de>
#
import socket, sys

if len(sys.argv) < 3:
	print("Needs at least 2 arguments.")
	sys.exit(3)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("192.168.0.97", 6020))

buf = ""

mode = sys.argv[1]
data = sys.argv[2]

if mode == 'freq':
	print("Doing freq")
	buf = buf + chr(0)
elif mode == 'mode':
	buf = buf + chr(1)
elif mode == 'squelch':
  buf = buf + chr(2)
elif mode == 'gain':
  buf = buf + chr(3)
  if data == 'auto':
    data = -100
elif mode == 'agc':
  buf = buf + chr(8)
  if data == 'on':
    data = 1
  elif data == 'off':
    data = 0
else:
	sys.exit(1)

data = int(data)

i=0
while i < 4:
	buf = buf + chr(data & 0xff)
	data = data >> 8
	i = i + 1


s.send(buf)
print("SENT")
s.close()
print("CLOSED")