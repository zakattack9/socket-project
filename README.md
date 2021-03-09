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

Commands to be implemented for final submission:
- `leave`
- `exit` (exit the peer program)
- `im-start`
- `im-complete`

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
contact_lists = {
  'list1': ['user1', 'user2']
  'list2': ['user2', 'user3']
}
ongoing_ims = {
  'list1': ['user1']
}
```

### im-start
- every contact list will have an integer indicating how many ongoing instant messages are being sent within that list
- this integer must be 0 in order for a contact to be added or removed from the list (performs check when doing `join`, `leave`, `exit`)
- upon starting an instant message within a contact list, the contact list has its integer incremented by 1 to indicate that at least one instant message is occurring within the group
- upon receiving an `im-complete` for a group, the specified contact list's integer is decremented by 1

### Threading
- each UDPClient spawns two threads:
  - the first thread listens only for responses from the UDPServer and ignores any other traffic; it performs the necessary tasks of parsing server commands and displaying any return data from the server
  - the second thread listens only for response that aren't from the UDPServer (i.e. im-start messages) ignoring any other traffic; this thread has the simple job of displaying, then propagating the message to the next UDPClient in the P2P client list; upon receiving its own broadcasted message back, it displays a message saying im-complete should be executed

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

[MILESTONE DEMO VIDEO LINK](https://youtu.be/V6trnoBKt0s)
```bash
# run on all terminals (allows use of py alias)
source ~/.bashrc
cd socket_project/src

py UDPServer.py 22000
py UDPClient.py 10.120.70.145 22000
py UDPClient.py 10.120.70.145 22000
py UDPClient.py 10.120.70.145 22000
# py UDPClient.py 10.120.70.106 22000

register me '10.120.70.106' 22000
register myself '10.120.70.106' 22001
register i '10.120.70.106' 22002

register me "10.120.70.106" 22000
register myself '10.120.70.106' 22002
register i 10.120.70.145 22001

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

[FINAL DEMO VIDEO LINK](https://youtu.be/7PJ86fVAsjo)
```bash
# run on all terminals (allows use of py alias)
source ~/.bashrc
cd socket_project/src

# general4
py UDPServer.py 22000
py UDPClient.py 10.120.70.145 22000
# general3
py UDPClient.py 10.120.70.145 22000
py UDPClient.py 10.120.70.145 22000
# general5
py UDPClient.py 10.120.70.145 22000
py UDPClient.py 10.120.70.145 22000

# general3
register Me 10.120.70.106 22000
register Myself 10.120.70.106 22002
# general4
register I 10.120.70.145 22001
# general5
register Foo 10.120.70.117 22000
register Bar 10.120.70.117 22002

# contains all five contacts
create list_1
# contains Me, Myself, and I
create list_2
# contains Foo and Bar
create list_3
# contains Foo
create list_4

# run on any client terminal
query-lists

join list_1 Me
join list_2 Me

join list_1 Myself
join list_2 Myself

join list_1 I
join list_2 I

join list_1 Foo
join list_3 Foo
join list_4 Foo

join list_1 Bar
join list_3 Bar

# demonstrates use of same group list across multiple im's
# also demonstrates intersecting contact list
im-start list_1 Me
  Hello

im-start list_1 Me
  World

# demonstrates that contacts can receive message from different groups
# also demonstrates disjoint contact list
im-start list_2 Myself
  Hi list_2

# show that leave can't be executed due to ongoing im
leave list_1 Me
# show that for each im-start there must be a corresponding im-complete
im-complete list_1 Me
im-complete list_1 Me
# show that each im-complete must correspond to an im-start
im-complete list_1 Me
# show that leave function works after executing required im-complete's
leave list_1 Me

# demonstrate disjoint contact list
im-start list_3 Foo
  Hi Bar

im-start list_3 Bar
  Hi Foo

im-complete list_3 Foo
im-complete list_3 Bar

# demonstrate im-start on contact list with only one contact (no machine should receive the message)
im-start list_4 Foo
  Anyone here?

# show that join can't be executed due to ongoing im
join list_4 Me

im-complete list_4 Foo

# save current config to file
# particularly, Me should be missing from list_1
save config.txt

# show that exit can't be executed due to ongoing im
exit Myself
im-complete list_2 Myself
# show that Myself can now execute exit after completing im
exit Myself

exit Me
exit I
exit Foo
exit Bar

# exit the server process
nano config.txt
```

### Need to implement
- a failure status code must be returned if the named contact is part of an ongoing instant message in the `join` command
- a failure status code must be returned if the named contact is part of an ongoing instant message in the `exit` command

### Need to fix
- inputted commands with string arguments that include spaces are not parsed properly
  - `create "list 1"` => created in database as `"list`
