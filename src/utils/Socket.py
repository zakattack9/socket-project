from socket import *
from utils import Constants

def validate_port(port):
  # constrain port number to dedicated port range
  if (port > Constants.MAX_PORT_NUM or port < Constants.MIN_PORT_NUM):
    port = Constants.MIN_PORT_NUM
  return port

def create_socket(port):
  if (port > Constants.MAX_PORT_NUM):
    port = Constants.MIN_PORT_NUM
  new_socket = None
  try:
    # AF_INET indicates that the underlying network is using IPv4
    # SOCK_DGRAM indicates that it is a UDP socket
    new_socket = socket(AF_INET, SOCK_DGRAM)
    # bind the specified port number to the socket instantiated above
    new_socket.bind(('', port))
    print('Socket bound to port ' + str(port))
    return new_socket
  except Exception as err:
    if ('[Errno 98] Address already in use' in str(err)):
      port += 1
      new_socket.close()
      return create_socket(port)
    else:
      raise Exception('[ERROR] Occurred during the UDP socket creation\n' + str(err))
