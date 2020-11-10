# Decorators 2 - Name Directory

def person_lister(func):
    def inner(people):
        return [ func(p) for p in sorted(people, key = lambda x: (int(x[2])))]
    return inner


# Validating phone numbers

import re
n = int(input().strip())

for _ in range(n):
    tel = input().strip()
    pattern = '^[789][0-9]{9}$'
    print("{}".format("YES" if bool(re.match(pattern, tel)) else "NO"))


# Validating and Parsing Email Addresses

import re
t = int(input().strip())
for _ in range(t):
    name, email = input().strip().split()
    
    if re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', email):
        print("{} {}".format(name, email))


# Hex Color Code

import re

n = int(input().strip())
inside = False
for _ in range(n):
    line = input()
    
    for el in line.split(' '):
        if el == "{":
            inside = True
            continue
        elif el == "}":
            inside = False
            continue
        elif inside:
            found = re.search(r'\#[0-9a-fA-F]{3,6}', el)
            if found:
                print(found.group(0))


# HTML Parser - Part 1

import re
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start".ljust(6) + ":", tag)
        for at in attrs:
            print("-> {} > {}".format(at[0], at[1]))
    def handle_endtag(self, tag):
        print("End".ljust(6) + ":", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty".ljust(6) + ":", tag)
        for at in attrs:
            print("-> {} > {}".format(at[0], at[1]))

if __name__ == "__main__":
    parser = MyHTMLParser()
    n = int(input().strip())
    for _ in range(n):
        line = input()
        parser.feed(line)
