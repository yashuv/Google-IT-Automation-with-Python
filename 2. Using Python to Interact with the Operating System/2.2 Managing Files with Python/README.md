# Managing Files with Python

In this module, we'll learn about reading and writing to files and the commands that will enable us to do this. We’ll learn the importance of managing files and how we can navigate through different directories. We’ll understand how to work with files and how there is a layer of abstraction between Python and the operating system. Finally, we’ll dive into learning about CSV files and how to best utilize them.

## Learning Objectives
* Read, write, and iterate through files
* Manage files by moving, deleting, and renaming files
* Create and navigate through directories
* Define what CSV files are and read from them
* Write and make edits to CSV files within directories

## Programming with Files
We'll check out some ways you can use Python to interact with file systems. As an IT specialist, it's likely that you'll need to manipulate files and directories on a computer a lot. When you need to work on a large number of files and directories, that's when automation can be a huge help.

Operating systems like Mac OS, Windows, and Linux use file systems to organize and control how data is stored and access. Data is usually stored on a disk and saved in files which are held in containers called directories or folders. File systems are usually organized in a tree structure with directories and files nested under their parents. We know where a resource like a directory or a file is located within that tree structure by its path.

 An *absolute path* is a full path to the resource in the file system. For example, on a Windows computer, the absolute path to the folder for the user James would be `C:\Users\James`. On a Linux computer, the absolute path to the equivalent directory would be `/home/james`. We call it absolute path because it doesn't matter where in the file system our script is running, the absolute path will always lead us to the resource. <br>
 On the other hand, *relative paths* use only a portion of a path to show where the resource is located in relation to the current working directory. Relative paths are a shortcut that you can use so you don't have to write out the full file path. But keep in mind, they only makes sense relative to the current location. So for example, if we list the contents of the directory examples, we'll get different outputs depending on what the current directory is. If our current directory is `/home/james`, we'll get the contents of `/home/james/example`. But if the current directory is `/user/share/doc/python3`, we'll get the contents of `/user/share/doc/python3/examples`. 
 
### ⋅ Reading Files
In programming, we work with files all the time. It's such a useful task that most programming languages have the ability to work with files baked into the core set of features. Python is no exception. It gives us file objects which we can use to read and write to files. <br>
 The most common way to work with files in Python is to use the built-in `open()` function. This function takes two arguments, the first being the path to the file and the second being the mode in which to open the file.

```python
file = open("filename.txt", "r") # open file in read mode

content = file.read()   # reads from current pos until the end of the file
	 
line = file.readline()	 # reads a single line from current pos
	 
lines = file.readlines()   # get lines from entire file(returns a list of lines)
	 
file.close()		# close file
```

The similar operation can be done with the help of *with* keyword as shown below. With the 'with' keyword, you get better syntax and exceptions handling. 
```python
with open("filename.txt", "r") as f:

	content = file.read()
		
	line = file.readline()
		
	lines = file.readlines() 
```

There are **three main modes of file** in python:<br>
`read mode ("r")`: Used to read data from a file. The file must already exist.

`write mode ("w")`: Used to write data to a file. If the file already exists, it will be overwritten. If it does not exist, it will be created.

`append mode ("a")`: Used to add data to the end of a file. If the file does not exist, it will be created.

<img src="images/file modes.jpg"/>

### ⋅ Iterating through Files
Along with reading a single line of the file or the whole contents of the file right to the end, file objects can be iterated in the same way as other Python sequences like list or strings. This is really useful when you want to process a file line by line.<br>
The code snippet below will correctly open a file and print lines one by one without whitespace.
```python
with open("hello_world.txt") as text:
  for line in text:
	  print(line.strip()) 
```
 
 ### ⋅ Writing Files
You can use the built-in `open()` function to create a new file or open an existing one. To write data to a file, you need to call open() with a second argument specifying the write, 'w' mode. Then, you can use the file object's `write()` method to write data to the file.
If the file already exists, it will be overwritten. If it does not exist, it will be created. Finally, don't forget to close the file to make sure the data is actually written to disk.
If you open a file for writing and the file already exists, the old contents will be deleted as soon as the file is opened.

```python
with open('output.txt', 'w') as f:		# open the file in write mode
	f.write('Hello, world!')		    
```

<b>If you want to add content to a file that already exist, you can do that by using other modes like  for appending content at the end of an existing file. </b>

```python
with open('output.txt', 'a') as f:		# open the file in append mode
  f.write('\nHello, world!')			# add the content at the end of file
```
 
 So it's important to check that you're opening the right file using the right mode.

### ⋅Reading and Writing Files Cheat-Sheet
Check out the following link for more information:

* <a href="https://docs.python.org/3/library/functions.html#open">https://docs.python.org/3/library/functions.html#open</a>

 ## Managing Files and Directories
 There's plenty of other things we might need to do when working with files in our scripts. We may need to delete, rename or move files, or we might need information about a file, like the time it was last modified or its current size. Let's explore some of the many things that we can do with files in Python. We'll be using functions provided by the `OS module` to perform all sorts of file operations. Let's start by importing the OS module.

### ⋅ Creating Directory
To create a directory, we can use the `os.mkdir()` function.
```python
import os

os.mkdir("newdir")
```
This will create the directory named `newdir` to the current working directory.

### ⋅ Deleting Files

To delete a file, we can use the `os.remove()` function. This function takes the name of the file that we want to delete as an argument. Let's try it out.

```python
import os

os.remove("file_to_delete.txt")
```
This will delete the file named `file_to_delete.txt` from the current working directory.

### ⋅ Deleting Empty Directories
We can also delete folders using the `os.rmdir()` function. This function takes the name of the folder that we want to delete as an argument. Let's try it out.
```python
import os

os.rmdir("dir_to_delete")
```
This will delete the folder named `folder_to_delete` from the current working directory.

If we try to remove a directory that has files in it, we get an error. We need to first delete all the files and sub-directories in that directory before we can actually remove it.

But we can we find out what contents are in that directory using `os.listdir()` function.
```python
import os

list_of_items = os.listdir("dir_of_contents")
```
This will returns a list of all the files and sub-directories in a given directory.

### ⋅ Change Directories
We can also change directories in your program by using the `os.chdir()` function and passing the directory that we like to change to as a parameter.
```python
import os

os.chdir("new_dir")
```
This will change the current working directory to the `new_dir`.

### ⋅ Current Working Directory
We can also get our currently working directory using the `os.getcwd()` function.
```python
import os

os.getcwd("new_dir")
```

### ⋅ Renaming Files
We can rename files using the `os.rename()` function. This function takes two arguments. The first is the name of the file to be renamed, and the second is the new name for the file. Let's try it out.

```python
import os

os.rename("old_name.txt", "new_name.txt")
```

This will rename the file named `old_name.txt` to `new_name.txt`.

### ⋅ Moving Files

We can move files using the `os.rename()` function. This function takes two arguments. The first is the name of the file to be moved, and the second is the new path for the file. Let's try it out.

```python
import os

os.rename("old_name.txt", "new_path/new_name.txt")
```

This will move the file named `old_name.txt` to the folder named `new_path` and rename it to `new_name.txt`.

### ⋅ Getting File Information

We can get information about a file using the `os.stat()` function. This function takes the name of the file as an argument and returns an object that contains information about the file. Let's try it out.

```python
import os

file_info = os.stat("file_to_check.txt")
```

This will store information about the file named `file_to_check.txt` in the `file_info` variable. We can access the various pieces of information using attributes of the `file_info` object. For example, we can get the time that the file was last modified using the `st_mtime` attribute.

```python
import os

file_info = os.stat("file_to_check.txt")
last_modified = file_info.st_mtime
```

This will store the time that the file was last modified in the `last_modified` variable.

We can using the `fromtimestamp()` method of the `datetime` class inside the `datetime` module. It makes the date far easier for us to understand. 
```python
import os
import datetime

filename = 'file.txt'

modification_time = os.path.getmtime(filename)

print(datetime.datetime.fromtimestamp(modification_time))
```

### ⋅ Checking for Files
We can check for the existence of a file using the `os.path.exists()` function. This function takes the name of the file as an argument and returns `True` if the file exists and `False` if it does not. Let's try it out.

```python
import os

if os.path.exists("file_to_check.txt"):
    print("The file exists.")
else:
    print("The file does not exist.")
```
We can also check using `os.path.isfile()` method.
```python
if os.path.isfile('file.txt'):
  print('The file exists.')
else:
  print('The file does not exist.')
```
This will print `The file exists.` if the file named `file_to_check.txt` exists and `The file does not exist.` if it does not.

### ⋅ Checking for Folders
We can check for the existence of a folder using the `os.path.isdir()` function. This function takes the name of the folder as an argument and returns `True` if the folder exists and `False` if it does not. Let's try it out.

```python
import os

if os.path.isdir("folder_to_check"):
    print("The folder exists.")
else:
    print("The folder does not exist.")
```

This will print `The folder exists.` if the folder named `folder_to_check` exists and `The folder does not exist.` if it does not.

### ⋅ Checking for Empty Files
We can check for the existence of an empty file using the `os.path.getsize()` function. This function takes the name of the file as an argument and returns `0` if the file exists and is empty, and `-1` if the file does not exist. Let's try it out.

```python
import os

if os.path.getsize("file_to_check.txt") == 0:
    print("The file is empty.")
else:
    print("The file is not empty.")
```
This will print `The file is empty.` if the file named `file_to_check.txt` is empty and `The file is not empty.` if it is not.
### ⋅ Simple example program
Q. Write the `file_date` function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of `yyyy-mm-dd`.
```python
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

# Should be today's date in the format of yyyy-mm-dd
print(file_date("newfile.txt"))  
```

### ⋅ Files and Directories Cheat-Sheet
Check out the following links for more information:

* <a href="https://docs.python.org/3/library/os.html">https://docs.python.org/3/library/os.html</a>

* <a href="https://docs.python.org/3/library/os.path.html">https://docs.python.org/3/library/os.path.html</a>

* <a href="https://en.wikipedia.org/wiki/Unix_time">https://en.wikipedia.org/wiki/Unix_time</a>

## ⋅ Reading and Writing CSV Files
If we have data in a format we understand, then when we read the file we know how to parse it to get the information that we want. `Parsing` a file means analyzing its content to correctly structure the data. We use a bunch of different file formats to structure, store, and transport data. You might be familiar with some already. For example, `HTML` is a markup format which defines the content of a webpage. `JSON` is a data interchange format commonly used to pass data between computers on networks, especially the internet. `CSV` or comma separated values is a very common data format used to store data as segment of text separated by commas.

### ⋅ What is CSV file?
A  `CSV (comma-separated values)` file is a file that stores tabular data in a text format. Each line in a CSV file represents a row (single data record) in the table, and each field in a line is separated by a comma.
For example, the CSV file:<br>
Name,Age,City<br>
Mark,40,New York<br>
Elon,50,London<br>

would represent the following table:
<!-- <table>
  <tr>
    <th>Name</th>
    <th>Age</th> 
    <th>City</th>
  </tr>
  <tr>
    <td>John</td>
    <td>21</td> 
    <td>New York</td>
  </tr>
  <tr>
    <td>Jane</td>
    <td>32</td> 
    <td>London</td>
  </tr>
</table> -->
Name | Age | City
-----|-----|------
Mark | 40  | New York
Elon | 50  | London

Python standard library includes a module which lets us read, create and manipulate CSV files. The module name is `csv`.

### ⋅ Reading CSV
The `reader` object is an iterator. It returns one row at a time as a list. The first row is the header row.
The `next()` function returns the next row in the file as a list.
```python
import csv

with open('user_record.csv', 'r') as csv_file:
  reader = csv.reader(csv_file)
  header = next(reader)
  for row in reader:
    name, age, city = row
    print("Name: {}, Age: {}, City: {}".format(name,age,city))
```
### ⋅ Writing CSV
The `writer` object has a `writerow` method for writing single rows and a `writerows` method for writing multiple rows. The example below writes the header row and the data to the CSV file.
```python
import csv 
data = [['Mark', 40, 'New York'],['Elon', 50, 'London']]
with open("details.txt", 'w') as csv_file:
  writer = csv.writer(csv_file)
  writer.writerow(['Name', 'Age', 'City']) 
  writer.writerows(data)
```
### ⋅ Reading and Writing CSV Files with Dictionaries
You will learn how to read and write CSV files using dictionaries.
In order to read a CSV file as a dictionary, we need to specify the *field names*. We can do this using the `DictReader` class.
```python
import csv

with open('user_record.csv') as csv_file: 
    reader = csv.DictReader(csv_file) 
    for row in reader:
        print(row['Name'], row['Age'],row['City'])
```
The `csv.writer()` function will create a writer object that can be used to write data to a CSV file. The writer object has a `writerow()` method that can be used to write a single row to the CSV file, whereas `writerows()` method is used to write multiple rows(or records) to CSV file. The `writeheader()` method can be used to write the header row to the CSV file.
```python
import csv

users = [{"Name":"Syam","Age":56,"City":"Kathmandu"}, {"Name":"Jason","Age":35,"City":"NYC"}]
keys = ["Name", "Age", "City"]

with open('users.csv', 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
```

### ⋅ CSV Files Cheat Sheet
Check out the following links for more information:

* <a href="https://docs.python.org/3/library/csv.html">https://docs.python.org/3/library/csv.html</a>

* <a href="https://realpython.com/python-csv/">https://realpython.com/python-csv/</a>

## Conclusion
Files are one of the most important ways of storing and transmitting information in IT. I learned and practiced how to read and write both texts and CSV files and how to manage files and directories with Python. I got a chance to use Qwiklabs to simulate a real-life scenario. Overall, it was a great learning experience.