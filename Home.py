import streamlit as st
import datetime as dt

#%%
day = dt.date(year=2023, month=11, day=13)
today = dt.date.today()

#%%
i = 0
i = i+1
st.markdown(f"""
## Question {i}  
Consider the following code:

```python
a = [1,2,3]
a[1] = 4
```

What is `a`?

This code contains an error.  
a. `[1,2,3]`  
b. `[1,2,3,1]`  
c. `[4,2,3]`  
d. `[1,4,3]`  
""")

on = st.toggle(f'**Answer & Explanation {i}**', disabled=not(day==today))
if on:
    st.write('Answer: d')
    st.write('Explanation: The second line calls the 1st index of the list, where 0 is the most basic element. The equals sign is used for assignment, so 4 is assigned to the position 1 in the list.')

#%%
i = i+1
st.markdown(f"""
## Question {i}  
Consider the following code:

```python
nums = set([1, 1, 2, 2, 3, 3, 3, 4])
print(len(nums))
```
    
What does this return?

a. This code contains an error.  
b. `4`  
c. `8`  
d. `len([1, 1, 2, 2, 3, 3, 3, 4])`   
""")
on = st.toggle(f'**Answer & Explanation {i}**', disabled=not(day==today))
if on:
    st.write('Answer: c')
    st.write('Explanation: Although the `list` contains 8 elements, a `set` only contains unique elements, eliminating one `1`, one `2`, and two `3`s. Casting the list as a set eliminates repeats, leaving only `{1,2,3,4}`, containing `4` elements.')

#%%
i = i+1
st.markdown(f"""
## Question {i}  
Consider the following code:

```python
a=(1,2,3)
a[1]=4
```
    
What is `a`?

a. This code contains an error.
b. `[1,2,3]`  
c. `[1,2,3,1]`  
d. `[4,2,3]`  
e. `[1,4,3]`  
""")

on = st.toggle(f'**Answer & Explanation {i}**', disabled=not(day==today))
if on:
    st.write('Answer: a')
    st.write('Because `a` is defined with parentheses, it is a tuple, which is immutable (cannot be altered).')

#%%
i = i+1
st.markdown(f"""
## Question {i}
Consider the following code and output:

```python
a = [1,2,3]
b = a
a == b
True
a is b
True

b = a[:]
a == b
True
a is b
False
```
    
Why is the last statement false?

a. This code contains an error.  
b. `a` and `b` refer to the same object and therefore have same contents.  
c. `a` and `b` refer to different objects that have identical content.  
d. `a` and `b` refer to the same objects but have different content.  
d. `b` is an empty list.  
""")

on = st.toggle(f'**Answer & Explanation {i}**', disabled=not(day==today))
if on:
    st.write('Answer: c')
    st.write('For mutables, = makes the right object refer to the left one. In contrast, the Python shortcut with indexing `:` makes a new copy of a mutable with its containing elements. Therefore, a and b are different objects, but each with the same elements.')

#%%
i = i+1
st.markdown(f"""
## Question {i}
Again consider the code:

```python
x = "Hello, world!"
y = x[5:]
```
What is the value of y?
a. This code contains an error.  
b. 'Hello'  
c. 'Hello '  
d. ', world!'  
e. 'o, world!'  
""")

on = st.toggle(f'**Answer & Explanation {i}**', disabled=not(day==today))
if on:
    st.write('Answer: d')
    st.write('This indexing returns all characters in the position 5 or later.')

#%%
i = i+1
st.markdown(f"""
## Question {i}
Let's say you want to flip a coin until you get 10 heads. Should you use a for loop or a while loop?

a. A for loop  
b. A while loop  
""")

on = st.toggle(f'**Answer & Explanation {i}**', disabled=not(day==today))
if on:
    st.write('Answer: b')
    st.write('This process should continue until a condition is met, which has a clear definition, but not a clear number of steps. This means the coin should be flipped while fewer than ten heads arrive, which requires a while loop.')

#%%
i = i+1
st.markdown(f"""
## Question {i}
Let's say you want to flip a coin 10 times and count the number of heads. Should you use a for loop or a while loop?

a. A for loop  
b. A while loop  
""")

on = st.toggle(f'**Answer & Explanation {i}**', disabled=not(day==today))
if on:
    st.write('Answer: a')
    st.write('In this case, we know the number of steps beforehand. This is a situation for which a for loop is appropriate.')

#%%
i = i+1
st.markdown(f"""
## Question {i}
Consider the following code and output:

```python      
x = 1
while x < 5:
    x *= 2
```
    
What is the final value of x?
a. This code contains an error.  
b. 2  
c. 5  
d. 8  
e. 10  
""")

on = st.toggle(f'**Answer & Explanation {i}**', disabled=not(day==today))
if on:
    st.write('Answer: d')
    st.write('x will be doubled starting with 1 until it reaches or exceeds 5. 8 is the number that meets this criterion.')

#%%
i = i+1
st.markdown(f"""
## Question {i}
Consider the following code and output:

```python      
for integer in (-1,3,5):
    if integer < 0:
    	print("negative")
    else:
    	print("non-negative")
```
    
How many lines of text does this print?

This code contains an error.

a. 0  
b. 1  
c. 2  
d. 3  
""")

on = st.toggle(f'**Answer & Explanation {i}**', disabled=not(day==today))
if on:
    st.write('Answer: c')
    st.write('This code will print either "negative" or "non-negative" for each element in the tuple, of which there are three total.')

#%%
i = i+1
st.markdown(f"""
## Question {i}
Which data structure would best represent average latitude and longitude for each city in a group of cities, accessible by city name?

a. A tuple of string city names, latitudes, and longitudes.  
b. A list of tuples, each containing a string city name, and a float for both latitude and longitude.  
c. A set of string city names, latitudes, and longitudes.  
d. A dict with string city name keys and tuple latitude/longitude values.  
""")

on = st.toggle(f'**Answer & Explanation {i}**', disabled=not(day==today))
if on:
    st.write('Answer: d')
    st.write('A dict allows for values to be of any type, with keys that are immutable. A natural choice for city names is strings, and their latitude and longitude can be represented by an iterable (such as a tuple), making a dict an appropriate data type.')

#%%
i = i+1
st.markdown(f"""
## Question {i}
Consider the following code and output:

```python      
x = 'String'
y = 10
z = 5.0
print(x + x) # print command 1
print(y + y) # print command 2
print(y + x) # print command 3
print(y + z) # print command 4
```
            
Which of the following print commands will work?  

a. None: this code contains an error.  
b. 1  
c. 1; 2  
d. 1; 2; 3  
e. 1; 2; 4  
f. 1; 2; 3; 4  
""")

on = st.toggle(f'**Answer & Explanation {i}**', disabled=not(day==today))
if on:
    st.write('Answer: e')
    st.write('Addition (`+`) is polymorphic for two strings, and pairs of many numeric types. However, + is not defined for strings and numeric values.')

#%%
i = i+1
st.markdown(f"""
## Question {i}
Again consider the code:

```python
y = [x**2 for x in range(5)]
```
    
What is the value of y?

a. This code contains an error.  
b. [0, 2, 4, 6, 8]  
c. [2, 4, 6, 8, 10]  
d. [0, 1, 4, 9, 16]  
e. [1, 4, 9, 16, 25]  
""")

on = st.toggle(f'**Answer & Explanation {i}**', disabled=not(day==today))
if on:
    st.write('Answer: d')
    st.write('This is an example of a list comprehension, in which a list is created containing elements specified in the inside expression (i.e., `x**2`), performed for each element in the iterable (i.e., `range(5)`).')

#%%
i = i+1
st.markdown(f"""
## Question {i}
Consider the following code and output:

```python      
x = 1
def my_function():
    x = 2
    print(x)
print(x)
my_function()
print(x)
```
    
What will be printed?
Note that here, we separate lines of output with ";".

a. This code contains an error.
b. 1; 2; 1  
c. 2; 2; 2  
d. 1; 2; 2  
""")

on = st.toggle(f'**Answer & Explanation {i}**', disabled=not(day==today))
if on:
    st.write('Answer: b')
    st.write('`x` is first defined globally, with value `1`. Then, my_function creates a variable x with local scope. Therefore, its value does not extend beyond its use in the function.')

#%%
i = i+1
st.markdown(f"""
## Question {i}  
Consider the following code:

```python      
import math
print(math.cos(math.pi))
-1.0
```
    
What type of object is math.pi?  
a. `int` (integer)  
b. `float` (real number)  
c. function  
d. string  
""")

on = st.toggle(f'**Answer & Explanation {i}**', disabled=not(day==today))
if on:
    st.write('Answer: b')
    st.write('Explanation: `math.pi` is an floating point approximation to `π` (a real number).')

#%%
i = i+1
st.markdown(f"""
## Question {i}  
Again consider the code:

```python      
import math
print(math.cos(math.pi))
-1.0
```
    
what type of object is `math.cos`?  
a. `int` (integer)  
b. `float` (real number)  
c. function  
d. string  
""")
on = st.toggle(f'**Answer & Explanation {i}**', disabled=not(day==today))
if on:
    st.write('Answer: c')
    st.write('Explanation: `math.cos` takes in numeric values (in radians) as input and returns its cosine as output.')
#%%
i = i+1
st.markdown(f"""
## Question {i}: Pick One

Define a procedure, `pick_one`, that takes three inputs: a Boolean  and two other values. If the first input is True, it should return the second input. If the first input is False, it should return the third input.

```python
print pick_one(True, 37, 'hello')
>>> 37

print pick_one(False, 37, 'hello')
>>> hello

print pick_one(True, 'red pill', 'blue pill')
>>> red pill

print pick_one(False, 'sunny', 'rainy')
>>> rainy
```
""")

on = st.toggle(f'**Solution {i}**', disabled=not(day==today))
if on:
    st.markdown("""
```python
def pick_one(Flag, val_1st, val_2nd):
    if Flag == True:
        return val_1st
    return val_2nd
```
""")

#%%
i = i+1
st.markdown(f"""
## Question {i}: Triangular Numbers

The triangular numbers are the numbers 1, 3, 6, 10, 15, 21, ...  
They are calculated as follows.

1  
1 + 2 = 3   
1 + 2 + 3 = 6  
1 + 2 + 3 + 4 = 10  
1 + 2 + 3 + 4 + 5 = 15

Write a procedure, triangular, that takes as its input a positive integer `n` and returns the nth triangular number.
            
```python
print triangular(1)
>>>1

print triangular(3)
>>> 6

print triangular(10)
>>> 55
```
""")

on = st.toggle(f'**Solution {i}**', disabled=not(day==today))
if on:
    st.markdown("""
```python
def triangular(n):
    cnt = 0
    for i in range(0, n+1):
        cnt += i
    return cnt
```
""")

#%%
i = i+1    
st.markdown(f"""
## Question {i}: Linear Time

For the procedures below, check the procedures whose running time scales linearly with the length of the input in the worst case. You may assume the elements in input_list are fairly small numbers.
            
```python
def proc1(input_list):
    maximum = None
    for element in input_list :
        if not maximum or maximum < element:
            maximum = element
    return maximum

def proc2(input_list):
    sum = 0
    while len(input_list) > 0:
        sum = sum + input_list[0]   # Assume input_list[0] is constant time
        input_list = input_list[1:]  # Assume input_list[1:] is constant time
    return sum

def proc3(input_list):
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list)):
            if input_list[i] == input_list[j] and i != j:
                return False
    return True
```
""")

on = st.toggle(f'**Solution {i}**', disabled=not(day==today))
if on:
    st.markdown("""1, 2""")

#%%
i = i+1
st.markdown(f"""
## Question {i}: Remove Tags
When we add our words to the index, we don't really want to include html tags such as <body>, <head>, <table>, <a href="..."> and so on.  
Write a procedure, remove_tags, that takes as input a string and returns a list of words, in order, with the tags removed. Tags are defined to be strings surrounded by < >. Words are separated by whitespace or tags. You may assume the input does not include any unclosed tags, that is, there will be no '<' without a following '>'.

```python
print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
>>> []

print remove_tags("This is plain text.")
>>> ['This', 'is', 'plain', 'text.']
```
""")

on = st.toggle(f'**Solution {i}**', disabled=not(day==today))
if on:
    st.markdown("""
```python
def remove_tags(s):
    first_pos = []
    second_pos = []
    tag_less = []
    for i in range(len(s)):
        if s[i] == '<':
            first_pos.append(i)
        if s[i] == '>':
            second_pos.append(i)    
    if first_pos and second_pos:
        tag_less += s[:first_pos[0]].split()
        
        for i, j in zip(second_pos[:-1], first_pos[1:]):
            tag_less += s[i+1: j].split()
        tag_less += s[second_pos[-1]+1: ].split()
        return tag_less
    else:
        return s.split()
```
""")

#%%
i = i+1    
st.markdown(f"""
## Question {i}: Date Converter  
Write a procedure date_converter which takes two inputs. The first is  a dictionary and the second a string. The string is a valid date in the format month/day/year. The procedure should return the date written in the form <day> <name of month> <year>.
""")

st.markdown("""
```python
english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj", 
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober", 
11:"november", 12:"december"}            

print(date_converter(english, '5/11/2012'))
>>> 11 May 2012

print(date_converter(english, '5/11/12'))
>>> 11 May 12

print(date_converter(swedish, '5/11/2012'))
>>> 11 maj 2012

print(date_converter(swedish, '12/5/1791'))
>>> 5 december 1791
```

Hint: int('12') converts the string '12' to the integer 12.
""")

on = st.toggle(f'**Solution {i}**', disabled=not(day==today))
if on:
    st.markdown("""
```python
def date_converter(country, date):
    date = date.split('/')
    if (1 <= int(date[0]) <= 12) and (1 <= int(date[1]) <= 31):
        date = date[1] +  ' ' + country[int(date[0])] + ' ' + date[2]
    else:
        return 'Invalid date'
    return date
```
""")

#%%
i = i+1    
st.markdown(f"""
## Question {i}: Termination  
For each of the procedures defined below, check the box if the procedure always terminates for all inputs that are natural numbers (1,2,3...).

```python
def proc_01(n):
    while True:
        n = n-1
        if n == 0:
            break
    return 3

def proc_02(n):
    if n == 0:
        return n
    return 1 + proc_02(n-2)

def proc_03(n):
    if n <= 3:
        return 1
    return proc_03(n-1) + proc_03(n-2) + proc_03(n-3)    
```

Hint: int('12') converts the string '12' to the integer 12.
""")

on = st.toggle(f'**Solution {i}**', disabled=not(day==today))
if on:
    st.write('Answer: proc_01')

st.markdown("""
## Question 22: Longest Repetition

Define a procedure, longest_repetition, that takes as input a  list, and returns the element in the list that has the most consecutive repetitions. If there are multiple elements that have the same number of longest repetitions, the result should be the one that appears first. If the input list is empty, it should return None.
            
```python
print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
>>> 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
>>> b

print longest_repetition([1,2,3,4,5])
>>> 1

print longest_repetition([])
>>> None   
```
""")

on = st.toggle('**Solution 22**', disabled=not(day==today))
if on:
    st.markdown("""
```python
def longest_repetition(itr):
    if itr:
        cur = itr[0]
        cnt = 0
        longest = 1
        char = cur
        for i in range(1, len(itr)):
            if cur == itr[i]:
                cnt += 1
                cur = itr[i]
            else:
                cur = itr[i]
                if cnt >= longest:
                    longest = cnt
                    char = itr[i-1]
                    cnt = 0
    else:
        return None
    if cnt > longest:
        longest = cnt
        char = itr[i-1]
        cnt = 0            
    return char
```
""")

#%%

