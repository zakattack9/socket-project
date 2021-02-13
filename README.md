### Server port number
Group 42
Lower bound port number: 42/2 * 1000 + 1000 = 22000
Upper bound port number: 42/2 * 1000 + 1499 = 22499
Client port range: [22000, 22499]

Server commands are sent from the client to the contact server as one string delimited by the string "-_-"

Commands to be implemented for milestone:
- `register`
- `create`
- `query-lists`
- `join`
- `save`
- `exit` (partial functionality)

[user1, user2, user3]
contacts = {
  user1: {
    ip: ipv4,
    port: 22000
  },
  user2: {
    ip: ipv4,
    port: 22001
  }
}
contact_list = {
  list1: [user1, user2]
  list2: [user2, user3]
}

### Need to implement
- a failure status code must be returned if the named contact is part of an ongoing instant message in the `join` command
- a failure status code must be returned if the named contact is part of an ongoing instant message in the `exit` command