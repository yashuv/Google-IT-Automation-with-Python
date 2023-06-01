'''Write the parent_directory function that returns the name of the directory that's located just above the current working directory. Remember that '..' is a relative path alias that means "go up to the parent directory".'''

import os
import re
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(os.getcwd(), '..' )
  print(relative_parent)
  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

# print(parent_directory())
print(os.path.abspath('..'))

# OR
# print(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))