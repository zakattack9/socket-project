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

### Need to implement
- a failure status code must be returned if the named contact is part of an ongoing instant message in the `join` command
- a failure status code must be returned if the named contact is part of an ongoing instant message in the `exit` command