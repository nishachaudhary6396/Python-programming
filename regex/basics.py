import re
text = "I am learning Python"
x = re.search("Python", text)
print(x)

text1 = "nisha deepti xyz"
i = re.findall("is",text1)
print(i)

text2 = "Python is easy"
j = re.match("Python", text2)
print(j.group())


text3 = "cat cot cut"
print(re.findall("c.t", text3))

print(re.findall("^Hello","Hello Nisha what are you doing??"))

print(re.findall("world$", "Hello world"))

print(re.findall("ab*", "a ab abb abbb"))   # 0 or more b

print(re.findall("ab+", "a ab abb"))  # one or more b

print(re.findall("ab?", "a ab abb"))    #0 or 1 

text5 = "hello"
print(re.findall("[aeiou]", text5))

print(re.findall(r"\d", "a1b2c3"))  #any digit from 1 to 9

print(re.findall(r"\d+", "abc123555555xyz45abb1"))  # it group the number togetherr

print(re.findall(r"\w", "hi_123ijkl"))   # check all digit,letter , _

print(re.findall(r"\s", "hi nisha "))   # check space