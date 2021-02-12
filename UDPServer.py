from socket import *
import argparse

parser = argparse.ArgumentParser(description='IDP server socket process')
parser.add_argument(
  'port_number',
  help='Port number that the server will listen on'
)

args = parser.parse_args()
print(args)
