'''Write file_date function that creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. '''

import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename,'w') as f:
    pass
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  dt = str(datetime.datetime.fromtimestamp(timestamp))
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{date}".format(date=dt[:10]))


print(file_date("newfile.txt"))  # Should be today's date in the format of yyyy-mm-dd
