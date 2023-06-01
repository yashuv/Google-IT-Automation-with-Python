# Managing Data and Processes
In this module, we’ll learn about reading and writing to data files based on an interaction with the user. Along the way, we’ll dive into standard streams, environment variables, and command line arguments. Next, we’ll jump into Python subprocesses, including system commands and how they can be used. We’ll review how to obtain output from a system command, and dive into subprocess management, including how to check exit values and manipulate the normal versus error exit values. Finally, we’ll rundown processing log files, and will cover what a log file is, how to filter log files using regular expressions, and how to understand the output captured from log files.
<!--In this module, we'll check out concepts that help us interact with the running operating system. We'll look at how we can get the most out of the tools available. We'll kick this off by talking about how to read user data interactively. Then we'll explore the standard input and output data streams provided by the operating system and see how we can interact with them both from Python programs and from the system programs. In a lot of our examples, we'll interact with the operating system through the command line. So we'll start familiarizing ourselves a bit more with the Linux shell. We'll also talk about how we can execute system commands from Python. -->

## Learning Objectives
* Utilize Python to interact with a user to attain certain values
* Use the input() module to interact with the user
* Describe how subprocess.run works and interacts with system commands like ping
* Describe what a log file is and interact with log files using regular expressions
* Use the get command to pull data from log files

## Reading Data interactively
We've talked before about reading and writing files. Using files to store information and then processing that data over a script is a great way to build automation. But sometimes we need to interact with the user and ask them for certain pieces of information that just can't be stored in a file. To do this Python provides a built-in function `input()`. This function allows us to prompt the user for a certain value that we can then use for our scripts. This function will read a line of input from the user and return it as a *string*.

<pre>>>> input("Enter your name: ")
Enter your name: James
'James'
</pre>

## Standard Streams
They provide a way for programs to interact with its environment.<br>
Python program connect using I/O streams. `I/O streams` are the basic mechanism for performing input and output operations in your programs. You can think of these streams as pathways between your programs and their input sources like a keyboard, or output, like the screen. I/O streams aren't just available for Python programs. When we run a system command on our terminal, I/O streams are also being used to connect that command to the terminal input and output.

There are three standard streams in python:
* *Standard input* (`stdin`) is the stream where a program reads its input data.

* *Standard output* (`stdout`) is the stream where a program writes its output data.

* *Standard error* (`stderr`) is the stream which displays output like stdout, but is used specifically as a channel to show error messages and diagnostics from the program.

<img src = "images/standard streams.jpg">

## Environment Variables
When we open a terminal application on a Linux computer, whether it's local or a remote machine, the application that reads and executes all commands is called a *shell*. A `shell` is a command line interface used to interact with your operating system. The most commonly used shell on Linux is called *Bash*. Other popular shells are Zsh and Fish, while they operate in similar ways.

 Our Python programs get executed inside a shell command-line environment. The variable set in that environment, which are called `environment variables` are another source of information that we can use in our scripts.

## Command-Line Arguments and Exit Status
Python supports command line arguments, yet another common way of providing information to our programs is through *command line arguments*. `Command line arguments` are parameters that are passed to a program when it started. It's a super common practice to make our scripts receive certain values by command line arguments. It allows a code of the script to be generic while also letting us run it automatically without requiring any interactive user input. This means that these arguments are really useful for system administration tasks. That's because we can specify the information that we want our program to use before it even starts. This lets us create more and more automation and you can't argue with that. These arguments are stored in the `sys` module's `argv` attribute as a list.

Let's check this out by executing a very simple script that just prints this value.
```python
import sys
print(sys.argv)
```
For example, if the *script* is called as follows:

```python
python script.py arg1 arg2 arg3
```

then *sys.argv* will contain the following list:

['script.py', 'arg1', 'arg2', 'arg3']

We have the concept of exit status or return code, which provides another source of information between the shell and the programs that get executed inside of it. The `exit status` is a value returned by a program to the shell. A *non-zero* exit status indicates an *error*. The actual number returned gives additional info on what kind of error the program encountered.

Standard Library Docs: 
* https://docs.python.org/3/library/functions.html#input

* https://docs.python.org/3/library/functions.html#eval

# Python Subprocesses
## Running System Commands in Python
In Python, there are several ways to run system commands. The most common way is to use the `subprocess` module. <!-- The subprocess module provides a wide range of functions and capabilities including the ability to check the return codes and output from commands. -->
The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their *return codes*. This module also allows you to access the underlying operating system’s shell.<br>
For example, to run the `ls` command, you would do the following:
```python
import subprocess 
subprocess.run(["ls"])
```
If you want to store the results of the command, you can use the `check_output()` function:
```python
import subprocess

output = subprocess.check_output(["ls", "-l"])
print(output)
```
This will store the output of the command "ls -l" as a string in the variable *output*.

Also, when using the run command of the subprocess module, `capture_output` parameter, when set to True, allows us to get and store the output of a system command that we are using.<br>
for example:
```python
import subprocess

result = subprocess.run(["ls"], capture_output=True)
print(result.returncode)
print(result.stdout)
```

## Python Subprocesses Cheat Sheet
Check out the following link for more information:

* https://docs.python.org/3/library/subprocess.html

# Processing Log Files
Log files are files that contain a record of events that happen in programs that are running on a computer system and aren't connected to terminal. Log files contain a lot of useful information so they can be processed to extract useful information about the server, such as the number of requests made to the server, the IP addresses from which the requests were made, the type of requests made, etc.<br>
Python can be used to process log files in a number of ways. To do this we'll go back to our knowledge of *regular expressions*. Using regex's in our scripts gives us a great deal of flexibility when processing log files and other texts data sources too. In a script, we can program any kind of behavior we want, so we can manipulate and process text data and get results we need.

## Filtering Log Files with Regular Expressions
As we have already worked with the *regex* to extract helpful information from text in a very flexible way. Likewise, filtering log files with regular expressions in python can be done similarly using the `re` module. The re module provides a number of functions and constants that can be used to filter log files. The most commonly used function is the `search()` function, which searches for a specified pattern in a string. The search() function *returns a Match object if the pattern is found*, or *None if the pattern is not found*.

## Conclusion
I gained all of the concepts and skills mentioned above and got a chance to put all these knowledge into practice with the help of newly acquired system programming skills to solve real world problems. Now, I feel very confident about these subjects.