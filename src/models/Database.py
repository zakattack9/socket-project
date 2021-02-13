from utils import Constants
from utils import FileWriter

class Database:
  def __init__(self):
    self.contacts = {}
    self.contact_list = {}
  
  def register_contact(self, contact_name, ip, port):
    if (contact_name in self.contacts):
      return Constants.FAILURE_CODE_DUPLICATE_CONTACT
    if (len(self.contacts) + 1 > Constants.MAX_NUM_OF_CONTACTS):
      return Constants.FAILURE_CODE_MAX_NUM_CONTACTS

    self.contacts[contact_name] = { 'ip': ip, 'port': port }
    return Constants.SUCCESS_CODE

  def create_contact_list(self, list_name):
    if (list_name in self.contact_list):
      return Constants.FAILURE_CODE_DUPLICATE_LIST
    if (len(self.contact_list) + 1 > Constants.MAX_NUM_OF_CONTACT_LISTS):
      return Constants.FAILURE_CODE_MAX_NUM_LISTS
    
    self.contact_list[list_name] = []
    return Constants.SUCCESS_CODE
  
  def get_lists(self):
    num_lists = len(contact_list)
    list_names = contact_list.keys()
    return (num_lists, list_names)

  def add_contact_to_list(self, list_name, contact_name):
    if (not contact_name in self.contacts):
      return Constants.FAILURE_CODE_UNREGISTERED_CONTACT
    if (not list_name in self.contact_list):
      return Constants.FAILURE_CODE_UNCREATED_LIST
    if (contact_name in self.contact_list[list_name]):
      return Constants.FAILURE_CODE_DUPLICATE_CONTACT_IN_LIST
    
    self.contact_list[list_name].append(contact_name)
    return Constants.SUCCESS_CODE
  
  def save_to_file(self, file_name):
    try:
      file = FileWriter(file_name)
      file.clear_contents() # overwrite same file with each save
      
      # write line containing number of contacts
      file.append_to_end(len(self.contacts), False)
      # for each contact, append a line containing the contact's info
      for contact_name, contact_info in self.contacts.items():
        self.__save_contact_info(contact_name, contact_info['ip'], contact_info['port'])
        
      # append line containing number of contact lists
      file.append_line(len(self.contact_list))
      # for each list, append its name, number of contacts, and their respective contact info
      for list_name, contacts_list in self.contact_list.items():
        # append line containing contact list name
        file.append_line(list_name)
        # append line containing number of contacts in current list
        file.append_line(len(contacts_list))
        # for each contact in the current list, append a line containing the contact's info
        for contact in contacts_list:
          self.__save_contact_info(contact, self.contacts[contact]['ip'], self.contacts[contact]['port'])
      
      file.close()
    except:
      return Constants.FAILURE_CODE_FILE_SAVE_ERROR
    return Constants.SUCCESS_CODE

  # appends contact name, IP address, and port number on one line to the end of a file
  def __save_contact_info(self, file, name, ip, port):
    file.append_line(name)
    file.append_to_end(ip)
    file.append_to_end(port)

  def exit(self, contact_name):
    