import models.ContactDatabase as ContactDB

def execute_register(args):
  return ContactDB.register_contact(args[1], args[2], args[3])

def execute_create(args):
  return ContactDB.create_contact_list(args[1])

def execute_query_lists(args):
  return ContactDB.get_lists()

def execute_join(args):
  return ContactDB.add_contact_to_list(args[1], args[2])

def execute_leave(args):
  return ContactDB.remove_contact_from_list(args[1], args[2])

def execute_exit(args):
  return ContactDB.exit(args[1])

def execute_im_start(args):
  return ContactDB.begin_instant_message(args[1], args[2])

def execute_im_complete(args):
  return ContactDB.end_instant_message(args[1], args[2])

def execute_save(args):
  return ContactDB.save_to_file(args[1])

execute_action = {
  'register': execute_register,
  'create': execute_create,
  'query-lists': execute_query_lists,
  'join': execute_join,
  'leave': execute_leave,
  'exit': execute_exit,
  'im-start': execute_im_start,
  'im-complete': execute_im_complete,
  'save': execute_save,
}

def execute_command(args):
  response = execute_action[args[0]](args)
  return response
