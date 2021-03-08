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
      raise Exception('[ERROR]: Occurred during the UDP socket creation\n' + str(err))

# creates two sockets with adjacent ports
def create_pair_socket(port):
  if (port + 1 > Constants.MAX_PORT_NUM):
    port = Constants.MIN_PORT_NUM
  client_socket = None
  p2p_socket = None
  try:
    server_port = port
    p2p_port = port + 1

    client_socket = socket(AF_INET, SOCK_DGRAM)
    p2p_socket = socket(AF_INET, SOCK_DGRAM)

    client_socket.bind(('', server_port))
    p2p_socket.bind(('', p2p_port))
    
    print('UDP contact server socket bound to port ' + str(server_port))
    print('P2P instant message socket bound to port ' + str(p2p_port))
    
    return (client_socket, p2p_socket)
  except Exception as err:
    if ('[Errno 98] Address already in use' in str(err)):
      port += 1
      client_socket.close()
      if (not p2p_socket == None): p2p_socket.close()
      return create_pair_socket(port)
    else:
      raise Exception('[ERROR]: Occurred during the paired UDP socket creation\n' + str(err))
