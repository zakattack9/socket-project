from socket import *
import argparse

parser = argparse.ArgumentParser(description='UDP client socket process')
parser.add_argument(
  'server_ip',
  help='IPv4 address of UDP socket server'
)
parser.add_argument(
  'server_port',
  help='Listnening port number of UDP socket server'
)

args = parser.parse_args()
print(args)
