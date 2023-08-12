# 1
str1 = """Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are
"""
print(str1)

# 2
import sys
print("version of Python : " + sys.version)

# 3
print("Current date and time :\n2014-07-05 14:34:14")

# 4
from math import pi
print("welcome to calculate circle area ")
r = float(input("enter redius of the circle : "))
print("area of this circle equal : " , pi * (r**2))

# 5
fname = input("enter your first name : ")
lname = input("enter your last name : ")
print("your full name is : " , fname + " "  + lname)

# 6
user_numbers = (input("Enter your numbers : "))
list_numbers = []
tuple_numbers = ()

for num in user_numbers :
    if num !=",":
        list_numbers.append(num)

for num in user_numbers:
    if num != ",":
        tuple_numbers = tuple_numbers + (num,)

print("list of user numbers : " ,  list_numbers , "\ntuple of user numbers : " , tuple_numbers)

# 7
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + f_extns[-1])

# 8
color_list = ["Red","Green","White" ,"Black"]
print("the first color is : " + color_list[0] + "\nthe lsat color is : " + color_list[-1])

# 9
exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)

# 10
user_num = int(input("enter your num : "))
print(user_num + user_num**2 + user_num**3)

# 11
print(abs.__doc__)

# 12
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

# 13
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

# 14
date1 = (2014, 7, 2)
date2 = (2014, 7, 11)
print(date2[-1]-date1[-1])

# 15
import math
print("welcome to calculate volume of sphare")
r = 6
print("volume of sphare equal : " , (4/3) * math.pi * r**3)

# 16
num1 = int(input("enter your number : "))
num2 = 17
difference_between_num1_and_num2 = 0
if num1 <= num2:
    difference_between_num1_and_num2 = num2 - num1
else:
    difference_between_num1_and_num2 = (num1 - num2)*2
print(difference_between_num1_and_num2)

# 17
num = int(input("enter your num : "))
print(((abs(1000 - num) <= 100) or (abs(2000 - num) <= 100)))

# 18
num1 = int(input("enter your first number : "))
num2 = int(input("enter your second number : "))
num3 = int(input("enter your therd number : "))
sum = num1 + num2 + num3
if num1 == num2 and num2 == num3 and num3 ==num1:
    count = 0
    while count < 3  :
        print(sum)
        count = count +1
else:
    print(sum)

19
str1 = input("enter your string : ")
if str1.startswith("is ") :
    print(str1)
else :
    new_str = "is " + str1
    print(new_str)

# 20
def larger_string(text, n):
   result = ""
   for i in range(n):
      result = result + text
   return result
text = input("enter your text : ")
print(larger_string(text, 2))
print(larger_string(text, 3))

# 21
num = int(input("please enter your num : "))
if num%2 == 0 :
    print("your number if even")
elif num%2 > 0 :
    print("your number is odd")


# 22
list_test = [1,2,4,5,7,9]
print(list_test.index(4))

# 23
def substring_copy(text, n):
  flen = 2
  if flen > len(text):
    flen = len(text)
  substr = text[:flen]
  result = ""
  for i in range(n):
    result = result + substr
  return result
print(substring_copy('abcdef', 2))
print(substring_copy('p', 3));

# 24
char = input("enter your character : ")
if char == "a" or char == "e" or char == "i" or char == "o" or char =="u":
    print("your letter is a vowel")
else:
    print("your letter is not a vowel")

25
list_test = [1,5,3,8]
print(2 in list_test)
print(3 in list_test)


# 26
def Histogram(list_test):
    for item in list_test:
        output = ""
        times = item
        while times > 0 :
            output+= "*"
            times = times - 1
        print(output)
Histogram([5,7,3,5])

# 27
list_test = [4,6,2,3,8]
str_test = ""

for i in list_test:
    str_test+= str(i)
print(str_test)

# 28
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]
index = 0
index237 = numbers.index(237)
for i in numbers:

    if index > index237 :
        break
    elif i%2 == 0:
        print(i)
    index = index + 1

# 29
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
new_set = set()

for color in color_list_1:
    if color not in color_list_2:
        new_set = new_set.add(color)

print(new_set)

# 30
b = int(input("Input the base : "))
h = int(input("Input the height : "))

area = b*h/2

print("area = ", area)

# 31
def gcd(x, y):
   gcd = 1
   if x % y == 0:
       return y
   for k in range(int(y / 2), 0, -1):
       if x % k == 0 and y % k == 0:
           gcd = k
           break
   return gcd
print("GCD of 12 & 17 =",gcd(12, 17))
print("GCD of 4 & 6 =",gcd(4, 6))
print("GCD of 336 & 360 =",gcd(336, 360))

# 32
def lcm(x, y):
  if x > y:
      z = x
  else:
      z = y
  while(True):
      if((z % x == 0) and (z % y == 0)):
          lcm = z
          break
      z += 1
  return lcm
print(lcm(4, 6))
print(lcm(15, 17))

# 33
num1 = int(input("enter your first number : "))
num2 = int(input("enter your second number : "))
num3 = int(input("enter your therd number : "))

if num1 == num2 or num2 or num3 or num3 == num1:
    sum = 0
else:
    sum = num1 + num2 + num3

print(sum)

34
num1 = int(input("enter your first num : "))
num2 = int(input("enter your second num : "))
sum = num1 + num2
if sum >= 15 and sum <=20 :
    print(20)
else:
    print(sum)

# 35
num1 = int(input("enter your first num : "))
num2 = int(input("enter your second num : "))
sum = num1 + num2
diff = num1 - num2

if num1 == num2 or sum == 5 or diff == 5:
    print("True")

# 36
def add(object1,object2):
    if type(object1) is int and type(object2) is int:
        return object1 + object2

print(add(6,4))
print(add(6,"a"))
print(add("4","6"))

# 37
def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_details()

# 38
x = 4
y = 3
print((x+y)**2)

# 39
amt = 10000
int = 3.5
years = 7
future_value = amt*((1+(0.01*int)) ** years)
print(round(future_value,2))

# 40
import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)

# 41
import os.path
print(os.path.isfile('main.txt'))
print(os.path.isfile('main.py'))

# 42
import struct
print(struct.calcsize("P") * 8)

# 43
import platform
import os
print("Name of the operating system:",os.name)
print("\nName of the OS system:",platform.system())
print("\nVersion of the operating system:",platform.release())

# 44
import site
print(site.getsitepackages())

# 45
from subprocess import call
call(["ls", "-l"])

# 46
import os
print("Current File Name : ",os.path.realpath(__file__))

# 47
import multiprocessing
print(multiprocessing.cpu_count())

# 48
str_test = "367.35"
print(float(str_test))
print(int(float(str_test)))

# 49
from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('companies uses ai in egypt') if isfile(join('companies uses ai in egypt', f))]
print(files_list)

# 50
for i in range(0, 10):
    print('*',end="")

# 51
import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')


# 52
from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file = sys.stderr, **kwargs)

eprint("abc", "efg", "xyz", sep="--")

# 53
import os
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable
print(os.environ['HOME'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')

# 54
import getpass
print(getpass.getuser())

# 55
import socket
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

# 56
def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th

print('Number of columns and Rows: ',terminal_size())

# 57
import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))

# 58
num = int(input("Input a number: "))
sum_num = (num * (num + 1)) / 2
print("Sum of the first", num ,"positive integers:", sum_num)

# 59
print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm)


# 60
from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is:", c )

# 61
f_distance = int(input("enter the distance by feet : "))
print("the distance by feet equal {}f".format(f_distance))
print("the distance by inches equal {} inches".format(f_distance*12))
print("the distance by yard equal {} yard".format(f_distance/3))
print("the distance by miles equal {} mi".format(f_distance*0.0001894))

# 62
days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))

time = days + hours + minutes + seconds

print("The  amounts of seconds", time)

63
def absolute_file_path(path_fname):
    import os
    return os.path.abspath('path_fname')


print("Absolute file path: ", absolute_file_path("test.txt"))

# 64
import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("companies uses ai in egypt")))
print("Created: %s" % time.ctime(os.path.getctime("companies uses ai in egypt")))

# 65
t_seconds = int(input("enter time by seconds : "))
print("time by minutes equal {} minute".format(t_seconds/60))
print("time by hours equal {} hour".format(t_seconds/3600))
print("time by days equal {} day".format(t_seconds/(3600*24)))

# 66
height = float(input("Input your height in Feet: "))
weight = float(input("Input your weight in Kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))

# 67
kpa = float(input("Input pressure in in kilopascals> "))
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325
print("The pressure in pounds per square inch: %.2f psi"  % (psi))
print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
print("Atmosphere pressure: %.2f atm." % (atm))

# 68
user_numbers = (input("Enter your numbers : "))
list_numbers = []
sum = 0

for num in user_numbers :
    if num !=",":
        num = int(num)
        list_numbers.append(num)

for i in list_numbers:
    sum = sum + i
print(sum)

# 69
list_nums = [5,6,8,3]
new = sorted(list_nums)
print(new)

# 70
import glob
import os

files = glob.glob("companies uses ai in egypt")
files.sort(key=os.path.getmtime)
print("\n".join(files))

# 71
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time

dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'

data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)

data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))

for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))

# 72
import math
for item in dir(math):
    print(item)

# 73
start_point = int(input("enter start point of line : "))
final_point = int(input("enter final point of line : "))
print("midpoint line equal " ,(start_point+final_point)/2)

# 74
soundex = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4, 5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2]

word = input("Input the word be hashed: ")

word = word.upper()

coded = word[0]

for a in word[1:len(word)]:
    i = 65 - ord(a)
    coded = coded + str(soundex[i])

print("\nThe coded word is: " + coded)

# 75
import sys
print("\nPython Copyright Information")
print(sys.copyright)

# 76
import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))

# 77
import sys
print()
if sys.byteorder == "little":
    print("Little-endian platform.")
else:
    print("Big-endian platform.")
print()

# 78
import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))

# 79
import sys
str1 = "one"
x = 0
L = [1, 2, 3, 'Red', 'Black']
T = ("Red", [8, 4, 6], (1, 2, 3))
S = {'apple', 'orange', 'apple', 'pear'}
D = {'Name': 'David', 'Age': 6, 'Class': 'First'}

print("Size of ",str1,"=",str(sys.getsizeof(str1))+ " bytes")
print("Size of",x,"=",str(sys.getsizeof(x))+ " bytes")
print("Size of",L,"=",sys.getsizeof(L)," bytes")
print("Size of",T,"=",sys.getsizeof(T)," bytes")
print("Size of",S,"=",sys.getsizeof(S)," bytes")
print("Size of",D,"=",sys.getsizeof(S)," bytes")

# 80
import sys

print("\nCurrent value of the recursion limit:")
print(sys.getrecursionlimit())

# 81
list_of_colors = ['Red', 'White', 'Black']
colors = '-'.join(list_of_colors)
print("All Colors: "+colors)

# 82
def sum(var):
    sum = 0
    for i in var:
        if type(var) == dict:
            sum = sum + var[i]
        else:
            sum = sum + i

    return sum

list_nums = [5,6,7,9,3]
set_nums  = {6,8,3,4,9}
dict_nums = {"ahmed":3,"mohamed":5,"karim":6}
tuple_nums = (5,7,8,3,4)

print(sum(list_nums))
print(sum(set_nums))
print(sum(dict_nums))
print(sum(tuple_nums))

# 83
list_test = [6,3,8,7,3,4,0,1,2]
index = 0
for i in list_test:
    if i > 2:
        print("number of index {} is greater than 2".format(index))
    elif i == 2:
        print("number of index {} is equal 2".format(index))
    else:
        print("number of index {} is less 2".format(index))
    index = index + 1

# 84
str_test = "banana"
char_list = list(str_test)
print(char_list)
counts = dict()
for character in char_list:
    if character not in counts:
        counts[character] = 1
    else:
        counts[character] = counts[character] + 1
print(counts)

# 85
import os
path="companies uses ai in egypt"
if os.path.isdir(path):
    print("\nIt is a directory")
elif os.path.isfile(path):
    print("\nIt is a normal file")
else:
    print("It is a special file (socket, FIFO, device file)" )

# 86
print(ord('a'))
print(ord('A'))
print(ord('1'))
print(ord('@'))

# 87
file = open("companies uses ai in egypt")
print("\nThe size of abc.txt is :",file.__sizeof__(),"Bytes")

# 88
x = 20
y = 30
sum = x + y
print("{} + {} = {}".format(x,y,sum))

# 89
num = float(input("enter a number: "))
if (num == 1):
   print("First day of a Month!")

# 90
def file_copy(src, dest):
    with open(src) as f, open(dest, 'w') as d:
        d.write(f.read())
        file_copy("task 1 solutions.py", "important.py")
        with open('important.py', 'r') as filehandle:
            for line in filehandle:
                print(line, end = '')

# 91
a = 5
b = 7
print("variable before swaping a = {} , b = {}".format(a,b))
a,b = b,a
print("variable after swaping a = {} , b = {}".format(a,b))

# 92
print("\#{'}${\"}@/")
print("\#{'}${"'"'"}@/")
print(r"""\#{'}${"}@/""")
print('\#{\'}${"}@/')
print('\#{'"'"'}${"}@/')
print(r'''\#{'}${"}@/''')

# 93
x = 34
print("\nIdentity: ",x)
print("\nType: ",type(x))
print("\nValue: ",id(x))

# 94
x = b'Abc'
print("\nConvert bytes of the said string to a list of integers:")
print(list(x))

# 95
str_test = "785ad26r9"
print(str_test.isnumeric())

for i in str_test:
    if not i.isdigit():
        print("{} is not numeric".format(i))
    else :
        print("{} is numeric".format(i))

# 96
import traceback
print()
def f1():return abc()
def abc():traceback.print_stack()
f1()

# 97
s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
print()
print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )
print()

# 98
import time
print(time.ctime())

# 99
import os
import time

os.system("ls")
time.sleep(2)

os.system('clear')

# 100
import socket
host_name = socket.gethostname()
print("Host name:", host_name)

# 101
from http.client import HTTPConnection
conn = HTTPConnection("example.com")
conn.request("GET", "/")
result = conn.getresponse()
contents = result.read()
print(contents)

# 102
import subprocess
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
print("dir command to list file and directory")
print(returned_text)

# 103
import os

print(os.path.basename('D:\pythonprojects\python exercises\companies uses ai in egypt.py'))

# 104
import os
print("\nEffective group id: ", os.getegid())
print("Effective user id: ", os.geteuid())
print("Real group id: ", os.getgid())
print("List of supplemental group ids: ", os.getgroups())

# 105
import os

print(os.environ)

# 106
import os.path

for path in ['test.txt', 'filename', '/user/system/test.txt', '/', '']:
    print('"%s" :' % path, os.path.splitext(path))

# 107
import os.path
import time

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))

# 108
import os.path

for file in [ __file__, os.path.dirname(__file__), '/', './broken_link']:
    print('File        :', file)
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))

# 109
import os.path

def find_path(path_name):

  if os.path.isfile(path_name):
    return os.path.realpath(path_name)
  elif os.path.isdir(path_name):
    return os.path.realpath(os.path.join(os.getcwd(), path_name))
  else:
    return None


def main():
  path_name = "companies uses ai in egypt"
  print(find_path(path_name))

# 110
num_list = [45, 55, 60, 37, 100, 105, 220]

result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers divisible by 15 are",result)

# 111
import glob
file_list = glob.glob('*.*')
print(file_list)

print(glob.glob('*.py'))
print(glob.glob('./[0-9].*'))

# 112
list_test = [6,4,7,9,3]
list_test.remove(6)
print(list_test)

# 113
user_input = int(input("enter your number : "))
try:
    print("the number that user entered equal : ",user_input)
except ValueError:
    print("error")

# 114
list_test = [5,8,6,4,-2,-6,-5]
list_positive_integer = list(filter(lambda x:x>0 , list_test))
print(list_positive_integer)

# 115
import math
list_test = [4,6,8,4,8]
print(math.prod(list_test))

# 116
str_test = "Unicode"
for char in str_test:
    print(char)

# 117
str1 = "ahmed"
str2 = "ahmed"
print(hex(id(str1)))
print(hex(id(str2)))

# 118
list_test = [4,6,8,4,8]
print(bytearray(list_test))

# 119
num = 135.76
print("%f"%num)
print("%.2f"%num)

#120
str_test = input("enter your string : ")
length = len(str_test)
print("length of your string = {}".format(length))

# 121
try :
    x = 2
except NameError:
    print("variable is not defined")
else:
    print("variable is defined")
try :
    y
except NameError:
    print("variable is not defined")
else:
    print("variable is defined")

# 122
d= {"x":200}
n = 20
print(type(n)())
print(type(d)())

# 123
list_float = [5.6,224.7,898.5,23.6,876.7]
list_int = [4,7,2,8,6,7,9,3]
print(max(list_float))
print(max(list_int))

# 124
x=5
y=5
z=5
if x == y and y == z and z == x:
    print("variables x , y , z have the same value ")

# 125
num = [2, 2, 4, 6, 6, 8, 6, 10, 4]
print(len(num))

# 126
from inspect import getmodule
from math import sqrt
print(getmodule(sqrt))

# 127
x = 20
if x.bit_length() <= 63:
    print((2**63).bit_length())

# 128
str_test = "AHMEd"
print(any(c.islower() for c in str_test))

# 129
str_test = "ahmed"
print(str_test.ljust(6,"0"))
print(str_test.rjust(8,"0"))

# 130
import json
print(json.dumps({'Alex': 1, 'Suresh': 2, 'Agnessa': 3}))

# 131
var_list = ['a', 'b', 'c', 'd', 'e']
v, w, x, y, z = var_list
print(v, w, x, y, z)

# 132
import os.path
print(os.path.expanduser('~'))

# 133
from timeit import default_timer
def timer(n):
    start = default_timer()
    for row in range(0,n):
        print(row)
    print(default_timer() - start)
timer(5)
timer(15)

# 134
num1 = int(input())
num2 = int(input())
print( num1 , num2)

# 135
x = 39
print('"{}"'.format(x))

# 136
import os
print([f for f in os.listdir('D:\pythonprojects\python exercises') if os.path.isfile(os.path.join('D:\pythonprojects\python exercises', f))])

# 137
d = {'Red':'Green'}
(c1, c2), = d.items()
print(c1)
print(c2)

# 138
x = 'true'
x = int(x == 'true')
print(x)
x = 'abcd'
x = int(x == 'true')
print(x)

# 139
import socket
addr = '127.0.0.2561'
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")

# 140
x = 12
print(format(x, '08b'))
print(format(x, '010b'))

# 141
x = 30
print(format(x, '02x'))
x = 4
print(format(x, '02x'))

# 142
# def test(str1):
#     while '01' in str1:
#         str1 = str1.replace('01', '')
#     return len(str1) == 0
#
# str1 = "01010101"
print("Original sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "00"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "000111000111"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "00011100011"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))

# 143
import struct
print(struct.calcsize("P") * 8)

# 144
var1 = 5
var2 = "5"
var3 = "a"

print(type(var3))
print(type(var2))
print(type(var1))

# 145
var1 = [3,6,8,4]
var2 = (4,6,8,4)
var3 = {5,8,4}

print(type(var1))
print(type(var2))
print(type(var3))

# 146
import os
print("\nList of directories in os module:")
print(os.path)
print("\nList of directories in sys module:")
import sys
print(sys.path)

# 147
num1 = 8
num2 = 2
print(num1%num2 == 0)

# 148
def max_min(list):
    return(max(list),min(list))
print(max_min([5,7,3,9,7]))

# 149
def sums(num):
    sum = 0
    num = num -1
    while num > 0:
        sum = sum + num**3
        num = num -1
    return sum
print(sums(4))

# 150
def odd_product(nums):
  for i in range(len(nums)):
    for j in range(len(nums)):
      if  i != j:
        product = nums[i] * nums[j]
        if product & 1:
          return True
  return False
dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
dt3 = [1, 3, 5, 7, 9]
print(dt1, odd_product(dt1))
print(dt2, odd_product(dt2))
print(dt3, odd_product(dt3))
