#!/usr/bin/env python
# coding: utf-8

# Exercise 1-1

# In[ ]:


temp_text = input("Enter temperature in Celsius: ")
temp_number = float(temp_text)
fahtemp = ((temp_number * 9)/5) + 32
print("Your temperature in F is: ")
print (fahtemp)


# In[ ]:


import sys
print(sys.argv)
print()
name = sys.argv[1]
print("temp is", name)


# Exercise 1-3

# In[ ]:


fullname = input("Please enter your full name: ")
fullnamestring = fullname.title()
count = fullname.count('j')
post = fullname.find('john')
print(fullname)
print(fullname.capitalize())
print(fullnamestring)
print(count)
print(len(fullname)- 1)
print(post)


# Exercise 2-1

# In[ ]:


while True:
    temp_text = input("Enter temperature in Celsius or q to quit:")
    if (temp_text.isdigit()):
        temp_number = float(temp_text)
        fahtemp = ((temp_number * 9)/5) + 32
        print("Your temperature in F is: ")
        print (fahtemp)
    elif temp_text == "":
        continue
    elif temp_text == "q":
        break
    


   
    
    


# Exercise 2-2

# In[ ]:


MAXVAL = 26
MINVAL = 0

while True:
    guess = (MAXVAL + MINVAL)/2
    print("Is this your number?: ", guess) 
    answer = input("Type in y if correct, h if its too high, or l if its too low")
    if answer == "y":
        print("I win, you lose")
        break
    if answer == "h":
        MAXVAL = guess
    if answer == "l":
        MINVAL = guess
        
    


# Exercise 2-3

# In[ ]:


import sys

max_value = 26
if len(sys.argv) > 1:
    max_value = int(sys.argv[1]) + 1

min_value = 0
tries = 0

while True:
    guess = (max_value + min_value) // 2
    answer = input("Is {} your number? ".format(guess))

    if answer == "q":
        break

    tries = tries + 1

    if answer == "h":
        max_value = guess
    elif answer == "l":
        min_value = guess
    elif answer == "y":
        print("I got it in {} try(ies)!".format(tries))
        break
    else:
        print("Please enter h, l, or y")


# Exercise 3-1

# In[ ]:


squares = 32
result = list(map(lambda x: 2 ** x, range(squares)))
print(result)


# Exercise 3-2 (My Solution)

# In[ ]:


ctemps = [-40, 0, 37, 75, 100]
fahtemp = [((ctemps[0] * 9)/5) + 32,((ctemps[1] * 9)/5) + 32,((ctemps[2] * 9)/5) + 32,((ctemps[3] * 9)/5) + 32,((ctemps[4] * 9)/5) + 32]
bothtemps= {ctemps[0]:fahtemp[0], ctemps[1]: fahtemp[1], ctemps[2]: fahtemp[2], ctemps[3]: fahtemp[3], ctemps[4]: fahtemp[4]}
print (bothtemps)
    


# Exercise 3-3 

# In[ ]:


fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

cleanfruits = [x.lower() for x in fruits]
cleanerfruits = [x.replace(" ","") for x in cleanfruits]
print(cleanerfruits)


# Exercise 4-1
# 

# In[ ]:


import sys

for file_name in sys.argv[1:]:
    with open(file_name) as file_in:
        for i, line in enumerate(file_in, 1):
            print("{:4d}: {}".format(i, line), end='')


# In[ ]:


with open("../DATA/alt.txt") as alt_in:
    with open("a.txt", "w") as a_out:
        with open("b.txt", "w") as b_out:
            for line in alt_in:
                if line.startswith('a'):
                    a_out.write(line)
                else:
                    b_out.write(line)


# Exercise 5-1: Open file, read content into dictionary, print out student grades and then average overall class grade

# In[ ]:


scores_by_student = {}
sum_of_scores = 0.0

with open(r"C:\Users\dveras\Downloads\py3newhire\DATA\testscores.dat") as scores_in:

    for line in scores_in:
        (name, score) = line.split(":")
        score = int(score)
        scores_by_student[name] = score
        sum_of_scores += score

for student, score in sorted(scores_by_student.items()):
    if score > 94:
        grade = 'A'
    elif score > 88:
        grade = 'B'
    elif score > 82:
        grade = 'C'
    elif score > 74:
        grade = 'D'
    else:
        grade = 'F'

    print("{:<20s} {} {}".format(student, score, grade))

average = sum_of_scores/len(scores_by_student)
print("\naverage score is  {:.2f}\n".format(average))


# Exercise 5-2: Open file, split lines, and then count amount of instances

# In[ ]:


shell_users = {}

with open(r"C:\Users\dveras\Downloads\py3newhire\DATA\passwd") as f:
    
    for line in f:
        (a,b,c,d,e,f, shell) = line.split(":")
        
        if shell == "":
            shell = "NONE"
            
        if shell in shell_users:
            shell_users[shell] = shell_users[shell] + 1
        else:
            shell_users[shell] = 1
            
for shell, count in shell_users.items():
    print("{:5d} {}".format(count, shell))

    


# Exercise 5-3: Open two different fies, compare contents, print the ones that are in both (comments show you how to create new file)

# In[ ]:


with open(r"C:\Users\dveras\Downloads\py3newhire\DATA\fruit1.txt", 'r') as file1:
    with open(r"C:\Users\dveras\Downloads\py3newhire\DATA\fruit2.txt", 'r') as file2:
        same = set(file1).intersection(file2)
        print(same)

#with open(r"C:\Users\dveras\Downloads\py3newhire\DATA\common.txt", 'w') as file_out:
   # for line in same:
    #    file_out.write(line)


# In[ ]:


from datetime import date

def mkdate(raw_date):
    if raw_date != "NONE":
        raw_year, raw_month, raw_day = raw_date.split('-')
        d = date(int(raw_year), int(raw_month), int(raw_day))
    else:
        d = None

    return d

def get_info(index):
    pres_data = {}
    with open("../DATA/presidents.txt") as pres_in:
        for line in pres_in:
            flds = line[:-1].split(":")
            if int(flds[0]) == index:
                pres_data["lastname"] = flds[1]
                pres_data["firstname"] = flds[2]

                pres_data["birthdate"] = mkdate(flds[3])
                pres_data["deathdate"] = mkdate(flds[4])

                pres_data["birthplace"] = flds[5]
                pres_data["birthstate"] = flds[6]

                pres_data["termstart"] = mkdate(flds[7])
                pres_data["termend"] = mkdate(flds[8])

                pres_data["party"] = flds[9]

                break

    return pres_data

def get_all_data():
    all_data = []
    for i in range(1, 44):
        all_data.append(get_info(i))
    return all_data


from potus import get_info

for i in range(1, 46):
    print('PRESIDENT {}:'.format(i))
    for field, value in get_info(i).items():
        print(field, value)
    print()


# Exercise 8-1: Rewriting temp converter to include error handling

# In[ ]:


try:
    temp_str = input("Enter Celsius temp: ")
    celsius = float(temp_str)
    fahrenheit = ((9 * celsius) / 5) + 32
    print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))

except Exception as err:
    print("Naughty programmer! Here's your error: ", err)


# Exercise 8-2: Including exception that is specific to the error (ValueError)

# In[ ]:


try:
    import sys
    celsius = float(sys.argv[1])
    fahrenheit = ((9 * celsius) / 5) + 32
    print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))

except ValueError as err:
    print("No that is a value error, look at this: ", err)


# Exercise 9-1: Take in user input (filename) and print out date modified

# In[ ]:


import os, time
from stat import * # ST_SIZE etc

try:
    file = input("please enter file name with path: ")
    st = os.stat(file)
except IOError:
    print ("failed to get information about: ", file)
else:
    print ("file size:", st[ST_SIZE])
    print ("file modified:", time.asctime(time.localtime(st[ST_MTIME])))


# Exercise 9-2: Take in multiple user input and print out file size

# In[ ]:


try:
    import os
    file1 = input("please enter first file name with path: ")
    file2 = input("please enter second file name with path: ")
    info1 = os.stat(file1)
    info2 = os.stat(file2)
    print(info1)
    print(info2)
    print('size of 1 is: ', info1[6])
    print('size of 1 is: ', info1.st_size)
    print('size of 2 is: ', info2[6])
    print('size of 2 is: ', info2.st_size)
except Exception as err:
    print("Naughty programmer! Here's your error: ", err)
    


# Exercise 8-2: Teacher's Solution

# In[ ]:


import sys
import os.path

for f in sys.argv[1:]:
    if os.path.isdir(f):
        print("{} is a directory".format(f))
        continue
    else:
        print(f,os.path.getsize(f))


# Exercise 10-1: Open file, take students and their scores, sort by scores (highest is top so it is descending)

# In[ ]:


scores = {}
total_of_scores = 0

with open(r"C:\Users\dveras\Downloads\py3newhire\DATA\testscores.dat") as f:
    for line in f:
        (name, score) = line.split(":")
        score = int(score)
        scores[name] = score
        total_of_scores += score

for student, score in sorted(scores.items(), key=lambda e: (e[1]),
                             reverse=True):
    grade = None
    if score > 94:
        grade = 'A'
    elif score > 88:
        grade = 'B'
    elif score > 82:
        grade = 'C'
    elif score > 74:
        grade = 'D'
    else:
        grade = 'F'
    print("{:<20s} {:2d} {}".format(student, score, grade))

average = total_of_scores / len(scores)
print("\naverage score is  {:.2f}\n".format(average))


# Exercise 10-2: Open file, read, if the word starts with a then create new file and add it to it, if the word starts with b then create another new file and add it to it

# In[ ]:


a_lines = []
b_lines = []

try:
    
    with open(r"C:\Users\dveras\Downloads\py3newhire\DATA\alt.txt", 'r') as file1:
        for x in file1:
            if x.startswith("a"):
                a_lines.append(x)
            elif x.startswith("b"):
                b_lines.append(x)
    with open(r"C:\Users\dveras\Downloads\py3newhire\DATA\a.txt", 'w') as filea:
        filea.writelines(sorted(a_lines))
    
    with open(r"C:\Users\dveras\Downloads\py3newhire\DATA\b.txt", 'w') as fileb:
        fileb.writelines(sorted(b_lines))
                    
        
            
except Exception as err:
    print("Naughty programmer! Here's your error: ", err)


# Exercise 10-3: Open file, read contents, sort by different rules then print out

# In[ ]:


with open(r"C:\Users\dveras\Downloads\py3newhire\DATA\fruit.txt", 'r') as file_handle:
            fruit_lines = file_handle.readlines()

print("".join(sorted(fruit_lines)))
print("".join(sorted(fruit_lines, key=str.lower)))
print("".join(sorted(fruit_lines, key=lambda s: (len(s), s.lower()))))
print("".join(sorted(fruit_lines, key=lambda s: (s[1].lower(), s[0].lower()))))








#with open("../DATA/fruit.txt", "r") as F:
#    fruit_lines = F.readlines()

#print("".join(sorted(fruit_lines)))
#print()

#print("".join(sorted(fruit_lines, key=str.lower)))
#print()

#print("".join(sorted(fruit_lines, key=lambda s: (len(s), s.lower()))))
#print()

#print("".join(sorted(fruit_lines, key=lambda s: (s[1].lower(), s[0].lower()))))
#print()


# Exercise 10-4: Open file, split fields, print out pres first name,last name, and state sorted by the lastname then firstanme
#     My solution

# In[ ]:


with open(r"C:\Users\dveras\Downloads\py3newhire\DATA\presidents.txt", 'r') as file_handle:
    for line in file_handle:
        filelines = line.split(":")
        firstname = filelines[1]
        lastname =filelines[2]
        state = filelines[6]
        combo =(firstname,lastname,state)
        combolist = list(combo)
        sorted_by_second = sorted(combolist, key=lambda tup: tup[0])
        print(sorted_by_second)
        


# Exercise 10-4: Open file, split fields, print out pres first name,last name, and state sorted by the lastname then firstanme
#     Teacher solution

# In[ ]:


all_pres = []
with open(r"C:\Users\dveras\Downloads\py3newhire\DATA\presidents.txt", 'r') as PRES:

    for line in PRES:
        fields = line.rstrip('\n\r').split(":")
        all_pres.append(fields) # add list of fields

# sort by lname, fname
for fields in sorted(all_pres, key=lambda e: (e[1], e[2])):
    print(fields[2], fields[1], fields[6])


# Exercise 11-1

# In[ ]:


import re

s = input("Enter filename")

pattern = r'[A-Z]\d{2,3}'  # <1>

if re.search(pattern, s):  # <2>
    print("Found pattern.")
print()

m = re.search(pattern, s)  # <3>
print(m)
if m:
    print("Found:", m.group(0))  # <4>
print()

for m in re.finditer(pattern, s):  # <5>
    print(m.group())
print()

matches = re.findall(pattern, s)  # <6>
print("matches:", matches)


# Exercise 11-2: Copy contents of one file to new file, if word has more than 8 letters we surround it with asterisks

# In[ ]:


import re
#create pattern to find words with 8 or more
rx_longword = re.compile(r"\b[a-z]{8,}\b", re.I)

#if the word has 8 or more letters we add asterisks around it
def mark_word(m):
    return '**' + m.group() + '**'

#open og file, copy contents, add asterisks, write new one
with open(r"C:\Users\dveras\Downloads\py3newhire\DATA\parrot.txt" , "r") as p_in:
    with open(r"C:\Users\dveras\Downloads\py3newhire\DATA\bigwords.txt" , "w") as p_out:
        for line in p_in:
            new_line = rx_longword.sub(mark_word, line)
            p_out.write(new_line)


# Exercise 11-3: Open file, find entries with phone numbers, print only those

# In[ ]:


import re

rx_phonenumber = re.compile(r"\b\d{3}-\d{4}\b")

with open(r"C:\Users\dveras\Downloads\py3newhire\DATA\custinfo.dat" , "r") as p_in:
    for x in p_in:
        if rx_phonenumber.search(x):
            print(x, end='')


# In[ ]:


Exercise 11-4: Read file, separate lines to word using regex pattern, normalize to lowercase, include frequency of word use


# In[ ]:


import sys
import re

rx_unc = re.compile(r"[^\w']+")
for file_name in sys.argv[1:]:
    with open(r"C:\Users\dveras\Downloads\py3newhire\DATA\presidents.txt") as file_in:
        found = {}
        for line in file_in:
            words = rx_unc.split(line)
            for word in words:
                if word == '' or word == "'":
                    continue
                word = word.lower()
                found[word] = found.get(word, 0) + 1

    for word, count in sorted(found.items()):
        print("{:<16s} {:4d}".format(word, count))


# Exercise 12-1: Create a new XML file containing all the words that start with 'x' from words.txt. 

# In[ ]:


import xml.etree.ElementTree as ET

words = open(r"C:\Users\dveras\Downloads\py3newhire\DATA\words.txt")
xwords = [word.rstrip() for word in words if word.startswith('x')]
words.close()

root = ET.Element('words')

for word in xwords:
    ET.SubElement(root, 'word').text = word

tree = ET.ElementTree(root)
tree.write(r"C:\Users\dveras\Downloads\py3newhire\DATA\xwords.xml")


# Exercise 12-2: Use ElementTree parse presidents.xml. Loop and print out each president’s first and last names and their state of birth.

# In[ ]:


try:
    from xml.etree import ElementTree as ET
    presroot = ET.parse(r'C:\Users\dveras\Downloads\py3newhire\DATA\presidents.xml')
    for pres in presroot.findall("president"):
        name = pres.findtext('name/last') + ', ' + pres.findtext('name/first')
        state = pres.findtext('birthstate')
        print('{0:40s} {1:30s}'.format(name, state))
except Exception as err:
    print("Naughty programmer! Here's your error: ", err)


# In[ ]:


Exercise 12-3: Rewrite xpresidents.py to parse presidents.json using the json module.


# In[ ]:


try:
    import json
    with open(r'C:\Users\dveras\Downloads\py3newhire\DATA\presidents.json') as PRES:
        p = json.load(PRES)
        
        for pres in p['presidents']:
            name = pres['lname'] + ', ' + pres['fname']
            state = pres['birthstate']
            print('{0:40s} {1:30s}'.format(name, state))
        
except Exception as err:
    print("Naughty programmer! Here's your error: ", err)


# Exercise 12-4: Rewrite first couple exercises to parse csv file instead of json

# In[ ]:


try:
    import csv
    with open(r'C:\Users\dveras\Downloads\py3newhire\DATA\presidents.csv') as PRES:
        p = csv.reader(PRES)
        for row in p:
           print('{:25s} {:12s} {}'.format(row[1],row[2], row[-1]))

except Exception as err:
    print("Naughty programmer! Here's your error: ", err)


# Exercise 15-1: Create a DataFrame columns named 'Test1', 'Test2', up to 'Test6'
#     Fill the DataFrame with random values.
#     Print only columns 'Test3' and 'Test5'
#     Print the dataframe with every value multiplied by 3.6

# In[ ]:


import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randint(0,100,size=(10, 6)), columns=['Test 1','Test 2','Test 3', 'Test 4','Test 5','Test 6'])
print(df[['Test 3', 'Test 5']])
print(df * 3.6)


# Exercise 15-2: Create DataFrame from file and select only content with shannondiversity score equal to or above 1.0

# In[ ]:


import pandas as pd
import numpy as np
dp = pd.read_csv(r'C:\Users\dveras\Downloads\py3newhire\DATA\parasite_data.csv')
df = pd.DataFrame(dp)
lowdiv = df[df['ShannonDiversity' ]>= 1.0]
print(lowdiv)
print(lowdiv.values)


# In[ ]:




