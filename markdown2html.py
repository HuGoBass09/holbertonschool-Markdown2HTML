#!/usr/bin/python3
'''Script that takes an argument 2 strings:
First argument is the name of the .md file
Second argument is the output file name
Script converts the .md file to .html file
The script will convert the following markdown syntax:
- Headers: Any number of #s at the start of a line
- Unordered listing: Lines that start with a dash (-)
- Ordered listing: Lines that start with a star (*)
- Text in double asterisks (**) is bold
- Text in double underscores (__) is italic
- Text in double brackets (()) is hashed
- Text in double parentheses (()) is case insensitive
The script will convert the markdown file to HTML and write it to the output file
If the markdown file does not exist, the script will print Missing <filename> and exit(1)
The script will exit(1) if the process is completed successfully 
'''

import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    if not os.path.exists(sys.argv[1]):
        sys.stderr.write("Missing " + sys.argv[1])
        exit(1)
    
        