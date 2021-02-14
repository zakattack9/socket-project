from utils import Constants
from utils.FileWriter import FileWriter

contacts = {}
contact_lists = {}

def register_contact(contact_name, ip, port):
  if (contact_name in contacts):
    return _build_response(Constants.FAILURE_CODE_DUPLICATE_CONTACT)
  if (len(contacts) + 1 > Constants.MAX_NUM_OF_CONTACTS):
    return _build_response(Constants.FAILURE_CODE_MAX_NUM_CONTACTS)

  contacts[contact_name] = { Constants.DB_IP_KEY: ip, Constants.DB_PORT_KEY: port }
  return _build_response(Constants.SUCCESS_CODE)

def create_contact_list(list_name):
  if (list_name in contact_lists):
    return _build_response(Constants.FAILURE_CODE_DUPLICATE_LIST)
  if (len(contact_lists) + 1 > Constants.MAX_NUM_OF_CONTACT_LISTS):
    return _build_response(Constants.FAILURE_CODE_MAX_NUM_LISTS)
  
  contact_lists[list_name] = []
  return _build_response(Constants.SUCCESS_CODE)

def get_lists():
  num_lists = len(contact_lists)
  list_names = list(contact_lists.keys())

  response_str = 'Total number of contact lists: ' + str(num_lists)
  for contact_list in list_names:
    response_str += '\n' + contact_list
  return _build_response(Constants.SUCCESS_CODE, response_str)

def add_contact_to_list(list_name, contact_name):
  if (not contact_name in contacts):
    return _build_response(Constants.FAILURE_CODE_UNREGISTERED_CONTACT)
  if (not list_name in contact_lists):
    return _build_response(Constants.FAILURE_CODE_UNCREATED_LIST)
  if (contact_name in contact_lists[list_name]):
    return _build_response(Constants.FAILURE_CODE_DUPLICATE_CONTACT_IN_LIST)
  
  contact_lists[list_name].append(contact_name)
  return _build_response(Constants.SUCCESS_CODE)

def save_to_file(file_name):
  try:
    file = FileWriter(file_name)
    file.clear_contents() # overwrite same file with each save
    
    # write line containing number of contacts
    file.append_to_end(str(len(contacts)), False)
    # for each contact, append a line containing the contact's info
    for contact_name, contact_info in contacts.items():
      _save_contact_info(
        file,
        contact_name, 
        contact_info[Constants.DB_IP_KEY], 
        contact_info[Constants.DB_PORT_KEY])
      
    # append line containing number of contact lists
    file.append_line(str(len(contact_lists)))
    # for each list, append its name, number of contacts, and their respective contact info
    for list_name, list_contacts in contact_lists.items():
      # append line containing contact list name
      file.append_line(list_name)
      # append line containing number of contacts in current list
      file.append_line(str(len(list_contacts)))
      # for each contact in the current list, append a line containing the contact's info
      for contact in list_contacts:
        _save_contact_info(
          file,
          contact, 
          contacts[contact][Constants.DB_IP_KEY], 
          contacts[contact][Constants.DB_PORT_KEY])
    file.close()
  except Exception as a:
    print(str(a))
    return _build_response(Constants.FAILURE_CODE_FILE_SAVE_ERROR)
  return _build_response(Constants.SUCCESS_CODE)

# appends contact name, IP address, and port number on one line to the end of a file
def _save_contact_info(file, name, ip, port):
  file.append_line(name)
  file.append_to_end(ip)
  file.append_to_end(port)

def exit(contact_name):
  if (not contact_name in contacts):
    return _build_response(Constants.FAILURE_CODE_UNREGISTERED_CONTACT)
  
  # delete contact from list of currently active contacts
  del contacts[contact_name]
  # delete contact from all associated contact lists
  for list_contacts in contact_lists.values():
    if (contact_name in list_contacts):
      list_contacts.remove(contact_name)
  return _build_response(Constants.SUCCESS_CODE)

def _build_response(return_code, data = None):
  return (return_code, data)
