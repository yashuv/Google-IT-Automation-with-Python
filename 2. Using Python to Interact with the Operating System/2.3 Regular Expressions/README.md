# Regular Expressions
In this module, we’ll learn about what a regular expression is and why you would use one. We’ll dive into the basics of regular expressions and give examples of wildcards, repetition qualifiers, escapare characters, and more. Next up, we’ll explore advanced regular expressions and deep dive on repetition qualifiers. We’ll tackle new exercises like capturing groups and extracting PIDs using regexes. Finally, we’ll provide a cheat sheet to serve as your go-to guide for regular expressions.

## Learning Objectives
* Define what a regular expression is and describe why it is useful
* Use basic regular expressions including simple matching, wildcard, and character classes
* Explain repetition qualifiers
* Use advanced regular expressions

## Intro
In this module, we'll take our data processing abilities one step further and learn about regular expressions, which are a very powerful tool to add to your IT toolbox. With regular expressions, we'll be able to find and operate on text in a more flexible way than we have up until this point.

## What are regular expressions?
A `regular expression`, also known as `regex` or `regexp`, is essentially a search query for text that's expressed by string pattern. Regular expressions allow us to search a text for strings matching a specific pattern. When you run a search against a particular piece of text, anything that matches a regular expression pattern you specified, is returned as a result of the search. Knowing about regular expressions can be useful for anyone who needs to perform text processing.<br>
We'll explore the Python module that deals with regular expressions. We'll check out how we can apply the regexs to processing, parsing and extracting meaning from texts read by our scripts. And we'll look at a bunch of different examples where we can use regular expressions to solve some real world problems.

## Why use regular expressions?
Regular expressions are both powerful and flexible tools. It has more processing power than just looking for strings in a text that we already know. Regular expressions can be used to perform complex operations on text with less overhead.

## Basic Matching with grep
Matching is the process of determining whether a pattern exists within a piece of text. The `grep` command in linux is widely used tool that allows you to search for patterns in text files  and print them to the screen.
  * grep "pattern" /path/to/file <br>
  return all lines in a file that contain the *specified pattern*(case sensitive)

  * grep -i "pattern" /path/to/file<br>
   return all lines in a file that contain the *specified pattern*, regardless of case

  * grep -r "pattern" /path/to/directory/<br>
   search for a pattern in all files in a directory

The special character `dot` is a *wildcard* that can be replaced by any other character in the results, `circumflex` (or `carat`)  indicates the *beginning*, and the `dollar sign` indicates the *end* of the line. 

	* grep ^abc /path/to/directory/
	- return a line that begins with abc
	
	* grep xyz$ /path/to/directory/
	- return a line that ends with xyz
	
	* grep a.cde /path/to/directory/
	- search for pattern with dot replaced by any character in result

The `findstr` command is a *Windows grep equivalent* in a *Windows command-line prompt (CMD)*.
In a *Windows PowerShell*, the alternative for grep is the `Select-String` command.

## Regular Expressions Cheat-Sheet
Check out the following links for more information:

* https://docs.python.org/3/howto/regex.html

* https://docs.python.org/3/library/re.html

* https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy

Shout out to <a href="regex101.com">regex101.com</a>, which will explain each stage of a regex. 
<details><summary><b>Click here for All Practice Quiz Solution</b></summary>

*Practice Quiz: Basic Regular Expressions*<br>
1.The check_web_address function checks if the text passed qualifies as a top-level web address, meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape characters, wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.

```python
import re
def check_web_address(text):
  pattern = r"^[\w\._-]+\.[A-Za-z]*$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True
```

2. The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case. Fill in the regular expression to do that. How many of the concepts that you just learned can you use here?
```python
import re
def check_time(text):
  pattern = r"^(1[0-2]|0?[1-9]):([0-5][0-9])( ?([AaPp][mM]))?"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
```

3. The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded by parentheses, with at least the first character in uppercase (if it's a letter), returning True if the condition is met, or False otherwise. For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" should return True since (IM) satisfies the match conditions." Fill in the regular expression in this function:
```python 
import re
def contains_acronym(text):
  pattern = r'\([A-Z0-9][a-zA-Z]+\)'
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True
```

4. Fill in the code to check if the text passed includes a possible U.S. zip code, formatted as follows: exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits. The zip code needs to be preceded by at least one space, and cannot be at the start of the text.
```python
import re
def check_zip_code (text):
  result = re.search(r"\s\d{5}(-\d{4})?", text)
  return result != None
  # result = re.search(r" \d{5}| \d{5}-\d{4}", text)  # OR

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False
```

5. Fix the regular expression used in the rearrange_name function so that it can match middle names, middle initials, as well as double surnames.
```python
import re
def rearrange_name(name):
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name = rearrange_name("Kennedy, John F.")
print(name)
```

6. The long_words function returns all words that are at least 7 characters. Fill in the regular expression to complete this function.
```python
import re
def long_words(text):
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []
```

7. Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis, after the process id.
```python
import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]:\s?(\w+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
```
**Practice Quiz: Advanced Regular Expressions**<br>
8. We're working with a CSV file, which contains employee information. Each record has a name field, followed by a phone number field, and a role field. The phone number field contains U.S. phone numbers, and needs to be modified to the international format, with "+1-" in front of the phone number. Fill in the regular expression, using groups, to use the transform_record function to do that.
```python
import re
def transform_record(record):
  new_record = re.sub(r',(\d{3})', r',+1-\1', record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer
```

9. The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that.
```python
import re
def multi_vowel_words(text):
  pattern = r'\w+[aeiou]{3,}\w+'
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []
```

10. The transform_comments function converts comments in a Python script into those usable by a C compiler. This means looking for text that begins with a hash mark (#) and replacing it with double slashes (//), which is the C single-line comment indicator. For the purpose of this exercise, we'll ignore the possibility of a hash mark embedded inside of a Python command, and assume that it's only used to indicate a comment. We also want to treat repetitive hash marks (##), (###), etc., as a single comment indicator, to be replaced with just (//) and not (#//) or (//#). Fill in the parameters of the substitution method to complete this function: 
```python
import re
def transform_comments(line_of_code):
  result = re.sub(r'\#{1,}', r'//', line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"
```

11. The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits), and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. Fill in the regular expression to complete this function.
```python
import re
def convert_phone_number(phone):
  result = re.sub(r'\b(\d{3})-(\d{3})-(\d{4})\b', r'(\1) \2-\3', phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300
```
</details>
<br>

## Conclusion:
I have gone from knowing nothing about regular expressions to being able to do complex search and replacing in different kinds of text.