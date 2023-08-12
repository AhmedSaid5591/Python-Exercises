#1
str = "Ahmed"
print(len(str))
count = 0
for length in str :
    count = count + 1
print(count)


#2
str2 = "programmer"
if len(str2) >= 2 :
    print(str2[:2]+str2[8:])
elif len(str2) < 2 :
    print("")


#3
str3 = input("Enter Your Word : ")
if len(str3)>=3 :
    if str3.endswith("ing"):
        print(str3 + "ly")
    else:
        print(str3 + "ing")
else:
    print(str3)


#4
list_test = ["ahmed","amany","mahmoud","said"]
new_list = []
for item in list_test:
    new_list.append(len(item))
print(new_list)
max_len = max(new_list)
print(max_len)
index = new_list.index(max_len)
print("the longest word in list is {} with length {} ".format(list_test[index],max_len))

#5
str5 = "programmer"
l= list(str5)
print(l)
first_char = l[0]
last_char = l[-1]
l[0] = last_char
l[-1] = first_char
print("".join(l))


#6
str6 = "ahmed"
new_str = ""
for i in range(len(str6)):
    if i % 2 > 0 :
        new_str = new_str + str6[i]
print(new_str)


#7
str_test = "amr and ahmed are frindes but amr is the tallest"
new_list = str_test.split(" ")
print(new_list)
new_dict = dict()
for item in new_list:
    if item not in new_dict:
        new_dict[item] = 1
    else:
        new_dict[item] = new_dict[item] + 1
print(new_dict)

#8
user_input = input("enter your script : ")
print(user_input.upper())
print(user_input.lower())


#9
def reverse_string(string):
    if len(string)%4 == 0 :
        return string[::-1]
    else:
        return string
print(reverse_string("ahmed"))
string = "ahmed"
l = list(string)
new_list = l.reverse()
print(l)
if len(string)%4 == 0 :
    print("".join(l))


#10
str10 = "welcome\nahmed"
new_string = ""
for character in str10:
    if character != "\n" :
        new_string = new_string + character
print(new_string)



#11
str11 = "tamam"
print(str11.startswith("t"))

#12
text = "This is a test string."
prefix = "PREFIX: "
lines = text.split("\n")
new_lines = []
for line in lines:
   new_lines.append(prefix + line)
print("\n".join(new_lines))

#13,14,15
num = 15
print("{:.2f}".format(num))
print("{:+.2f}".format(num))
print("{:,}".format(num))


#16
str16 = "programmer"
print(str16[::-1])
def reverse_string_using_for_loop(string):
    reversed_string = ""
    for character in string :
        reversed_string = character + reversed_string
    return reversed_string

string = str16
reversed_string = reverse_string_using_for_loop(string)

print("The reversed string is:", reversed_string)



#17
str17 = "banana"
char_list = list(str17)
print(char_list)
counts = dict()
for character in char_list:
    if character not in counts:
        counts[character] = 1
    else:
        counts[character] = counts[character] + 1
print(counts)


#18
str18="character"
first_non_repated_char = ""
for char in str18:
    if char not in str18:
        first_non_repated_char = first_non_repated_char + char

print(char)

#19
str19= "hello world"
new_string = ""
for character in str19:
    if character != " " :
        new_string = new_string + character
print(new_string)


#20
text = "This is a test string."
count = 0
for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        count += 1
print(count)


#21
def swap_first_and_last_element(list):
    first_element = list[0]
    last_element = list[-1]

    list[0] = last_element
    list[-1] = first_element

    return list


list = [1, 2, 3, 4, 5]
print("The original list is:", list)
new_list = swap_first_and_last_element(list)
print("The modified list is:", new_list)


#22
list22 = [23,65,19,90]
pos2 = list22[1]
pos3 = list22[2]
list22[1] = pos3
list22[2] = pos2
print(list22)


#23
import operator
list23 = [5,6,8,3,4,7,2]
print(len(list23))
count = 0
for element in list23:
    count = count + 1
print(count)
print(operator.length_hint(list23))


#24,25,26,27,28
list24_28 = [5,6,8,3,4,7,2,5,7,2]
print(max(list24_28))
print(min(list24_28))
print(6 in list24_28)
print(list24_28.clear())
for item in list24_28:
    list24_28 = list24_28.remove(item)
print(list24_28)
print(set(list24_28))

#29
test_list = ["Gfg", 3, "is", 8]
key_list = ["name", "id"]
dic1 = dict()
dic2 = dict()
dic1[key_list[0]] = test_list[0]
dic1[key_list[1]] = test_list[1]
dic2[key_list[0]] = test_list[2]
dic2[key_list[1]] = test_list[3]

print([dic1,dic2])

#30
def count_unique_values_using_set(list_of_values):

    set_of_values = set(list_of_values)
    return len(set_of_values)


def count_unique_values_using_dictionary(list_of_values):

    dictionary = {}
    for value in list_of_values:
        dictionary[value] = dictionary.get(value, 0) +1

    return len(dictionary)


list_of_values = [1, 2, 3, 4, 5, 1, 2, 3]
print("Number of unique values using set:", count_unique_values_using_set(list_of_values))
print("Number of unique values using dictionary:", count_unique_values_using_dictionary(list_of_values))

#31
test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
new_list =[]
for item in test_list:
    if test_list.count(item) > 3 :
        if item not in new_list:
            new_list.append(item)

print(new_list)

#32
test_list = [1,2,2,3,4,5]
count = 0
new_list = []
for i in range(1,len(test_list)):
    element = test_list[i]
    if element >= test_list[count]:
        new_list.append(element)
    count = count + 1
print(new_list)

#33
test_list = [1,2,3]
for i in range(len(test_list)):
    for j in range(len(test_list)):
        for k in range(len(test_list)):
            if( i!=j and j!=k and k!=i):
                print(test_list[i],test_list[j],test_list[k])

#34
test_list = [1,2,3]
compaination = []

for i in test_list:
    compaination.append([i])

for j in test_list:
    for k in test_list:
        if j != k and (j == 1 or j == 2 and k !=1):
            compaination.append([j,k])

for l in test_list:
    for m in test_list:
        for n in test_list:
            if l == 1 and m == 2 and n == 3:
                compaination.append([l,m,n])

print(compaination)


#35
list_1 = ["a", "b"]
list_2 = [1, 2]
unique_combinations = []
for element1 in list_1:
    for element2 in list_2:
        combination = (element1, element2)
        if combination not in unique_combinations:
            unique_combinations.append(combination)
print(unique_combinations)


#36
test_list = [1,1,2,3,4,5,1,2,1]
new_list = []
element = 1
for item in test_list:
    if item != element :
        new_list.append(item)
print(new_list)

#37
test_list1 = ["Gfg","is","best"]
test_list2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]
new_list = []
for item in test_list2:
    item = test_list1[item]
    new_list.append(item)
print(new_list)

#38
def retain_records_with_n_occurrences_of_k(test_list, k, n):

  retained_records = []
  for record in test_list:
    count = 0
    for element in record:
      if element == k:
        count += 1
    if count == n:
      retained_records.append(record)

  return retained_records

test_list = [(4, 5, 5, 4), (5, 4, 3)]
k = 5
n = 2
print(retain_records_with_n_occurrences_of_k(test_list, k, n))


#39
array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
column0 = sorted_array = sorted(array, key=lambda x: x[0])
column1 = sorted_array = sorted(array, key=lambda x: x[1])
column2 = sorted_array = sorted(array, key=lambda x: x[2])
print(column0)
print(column1)
print(column2)

#40
dict1 = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
print("sorted by value : ",sorted([(v,k) for k,v in dict1.items()]))
print("sorted by key : ",sorted([(k,v) for k,v in dict1.items()]))

#41
test_dict = {"Gfg" : 3, "is" : 7, "best" : 10, "for" : 6, "geeks" : "CS"}
K = 7
new_dict = {}
for key , value in test_dict.items():
    if value < K :
        new_dict[key] = value
print(new_dict)


#42
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
new_dic= dic1.copy()
new_dic.update(dic2)
new_dic.update(dic3)
print(new_dic)

#43
dict_test = {"ahmed" : 2 ,"karim": 1 , "islam": 4}
for key,value in dict_test.items():
    print("key: " , key , ", value :",value)

#44
dic1={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
dic2 = {"Gfg" : 3, "is" : 7, "best" : 10, "for" : 6, "geeks" : "CS"}
new_dic = dic1.copy()
new_dic.update(dic2)
print(new_dic)

#45
dic1={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
print("maximum value in dic : ",max(dic1.values()))
print("minimum value in dic : ",min(dic1.values()))

#46
dic = {'c1': 'Red', 'c2': 'Green', 'c3': None}
del dic["c3"]
print(dic)

#47
tuple1 = (5,6,8,3,4,5)
print(tuple1[3])

#48
tuple1 = (4,5,7,2,7)
x,y,z,l,m = tuple1
print ("x = " , x ,"\ny = ",z,"\nz = ",z,"\nl = ",l, "\nm = ",m)


#49
tuple = (5,7,2,3,9)
new_tuple = tuple + (4,)
print(new_tuple)


#50
tuple = ("a","c","b","d")
new_str = ""
for item in tuple :
    new_str = new_str + item
print(new_str)


#51
list51 = [4,6,8,3,9,0]
new_tuple = ()
for item in list51:
    new_tuple = new_tuple + (item,)
print(new_tuple)

#52
tuple_test = (4,7,9,3,4)
new_tuple = ()
for item in tuple_test:
    new_tuple = (item ,) + new_tuple
print(new_tuple)

#53
list_test =[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
last_value = list_test[2]
list_test[2] = (70, 80, 100)
print(list_test)


#54
str_test = "python 3.0"
new_tuple = ()
for item in str_test:
    new_tuple = new_tuple + (item,)
print(new_tuple)


#55
tuple_test = (5,8,3,1,5,8)
sum = 0
for item in tuple_test:
    sum = sum + item
print(sum)
print("averge value of the numbers in a given tuple of tuples = " ,sum/len(tuple_test) )


#56
set_test = {5,7,3,5,9}
number_we_need_to_add = 8
set_test.add(number_we_need_to_add)
print(set_test)

#57
set_test = {5,7,3,5,9}
number_to_remove = 3
if number_to_remove in set_test:
    set_test.remove(number_to_remove)
    print(set_test)
    print("The number 3 has been removed from the set.")
else:
     print("The number 3 is not in the set.")


#58
set_1 = {1, 2, 3, 4, 5}
set_2 = {2, 3, 4, 6, 7}
intersection = set_1 & set_2
union = set_1 | set_2
difference = set_1 - set_2
symmetric_difference = set_1 ^ set_2
print("The intersection of the sets is:", intersection)
print("The union of the sets is:", union)
print("The difference of the sets is:", difference)
print("The symmetric difference of the sets is:", symmetric_difference)

#59
set_test = {5,7,3,5,9}
print("maximum value in set = " ,max(set_test) ,"\nminimum value in set = ", min(set_test))


#60
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 10
pairs = []
for i in range(len(list_of_numbers)):
    for j in range(i+1 , len(list_of_numbers)):
        if list_of_numbers[i]+list_of_numbers[j] == target_sum:
            pairs.append((list_of_numbers[i] , list_of_numbers[j]))
print(pairs)