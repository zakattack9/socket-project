def validate_register(args):
  if (args.arg1 == None):
    print_missing_arg('client contact name')
  elif (args.arg2 == None):
    print_missing_arg('client ip address')
  elif (args.arg3 == None):
    print_missing_arg('client port number')
  elif (not args.arg3.isDigit()):
    print('Please enter a valid port number')
  else:
    return True
  return False

def validate_create(args):
  if (args.arg1 == None):
    print_missing_arg('contact list name')
  else:
    return True
  return False

def validate_query_lists(args):
  return True

def validate_join(args):
  return verify_contact_list_and_name(args)

def validate_leave(args):
  return verify_contact_list_and_name(args)

def validate_exit(args):
  if (args.arg1 == None):
    print_missing_arg('client contact name')
  else:
    return True
  return False

def validate_im_start(args):
  return verify_contact_list_and_name(args)

def validate_im_complete(args):
  return verify_contact_list_and_name(args)

def validate_sav(args):
  if (args.arg1 == None):
    print_missing_arg('save filename')
  else:
    return True
  return False

def print_missing_arg(missing_arg):
  print('Please specify the ' + missing_arg)

def verify_contact_list_and_name(args):
  if (args.arg1 == None):
    print_missing_arg('contact list name')
  elif (args.arg2 == None):
    print_missing_arg('client contact name')
  else:
    return True
  return False
