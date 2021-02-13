class FileWriter:
  def __init__(self, file_name):
    self.file_name = file_name
    self.file = open(file_name, 'at')
  
  # appends a string on a new line to the end of the file
  def append_line(self, str):
    self.file.write('\n' + str)

  # appends a string [with a preceding space] to the end of the file
  def append_to_end(self, str, precede_space = True):
    prefix = ' ' if precede_space else ''
    self.file.write(prefix + str)

  def clear_contents(self):
    open(self.file_name, 'w').close()

  def close(self):
    self.file.close()
