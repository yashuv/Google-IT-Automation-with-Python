#!/usr/bin/env python3
import sys
import subprocess

f = open(sys.argv[1], "r")

for line in f.readlines():
    old_substring = line.strip()
    new_substring = old_substring.replace("jane", "jdoe")
    subprocess.run(["mv", old_substring, new_substring])
    
f.close()