#!/bin/python3

#SOCKETS - can be used to connecting two nodes on a network to communicate with each other
import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#AF_INET = IPV4    SOCK_STREAM - providing port

s.connect((HOST,PORT)) 
#this script is going to local host, and trying to connect to the port
