### Server port number
Group 42</br>
Lower bound port number: 42/2 * 1000 + 1000 = 22000</br>
Upper bound port number: 42/2 * 1000 + 1499 = 22499</br>
Client port range: [22000, 22499]

Server commands are sent from the client to the contact server as one string delimited by the string "-_-"

Commands to be implemented for milestone:
- `register`
- `create`
- `query-lists`
- `join`
- `save`
- `exit` (partial functionality)

### Database model
```python
contacts = {
  'user1': {
    'ip': '10.0.0.1',
    'port': 22000
  },
  'user2': {
    'ip': '10.0.0.2',
    'port': 22001
  },
  'user3': {
    'ip': '10.0.0.3',
    'port': 22002
  },
}
contact_list = {
  'list1': ['user1', 'user2']
  'list2': ['user2', 'user3']
}
```

### How to run
```bash
# connect a client machine to the contact server
python3 UDPClient.py <server-ip-address> <server-port>
# start up the contact server on specific port
python3 UDPServer.py <server-port>
```

### Demo Commands
1. Compile your server and peer programs (if applicable).
2. Run the freshly compiled programs on at least two (2) distinct end hosts.
3. First, start your server program. Then start 3 peers that each register with the server.
4. Create 2 contact lists, and have peers query and join lists, until each contact list has 2-3 contacts.
5. Save the configuration to a file.
6. Exit the peers; kill the server process.

[DEMO VIDEO LINK](https://youtu.be/V6trnoBKt0s)
```bash
# run on all terminals (allows use of py alias)
source ~/.bashrc
cd socket_project/src

py UDPServer.py 22000
py UDPClient.py 10.120.70.145 22000
py UDPClient.py 10.120.70.145 22000
py UDPClient.py 10.120.70.145 22000

register me '10.120.70.106' 22000
register myself '10.120.70.106' 22001
register i '10.120.70.106' 22002

create list_1
create list_2

# run on all client terminals
query-lists

join list_1 me
join list_2 me

join list_1 myself
join list_2 myself

join list_2 i

save config.txt

exit me
exit myself
exit i

# exit the server process
nano config.txt
```

### Need to implement
- a failure status code must be returned if the named contact is part of an ongoing instant message in the `join` command
- a failure status code must be returned if the named contact is part of an ongoing instant message in the `exit` command