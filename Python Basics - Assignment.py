#!/usr/bin/env python
# coding: utf-8

# In[16]:


##Simple Message: Store a message in a variable, and then print that message.

a = "how are you ?"
print(a)


# In[17]:


##Store a message in a variable and print that message. 
##Then change the value of your variable to a new message and print the new message.
s = "we are very good People"
print(s)
s1 = s.replace("we","Your").replace("good","better")
print(s1)


# In[19]:


##Store a person’s name in a variable and print a message to that person. 
##Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
person_name = "Eric"
message = f"Hello {person_name}, would you like to learn some Python today?"
print(message)


# In[23]:


##Find a quote from a famous person you admire. Print the quote and the name of its author. 
##Your output should look something like the following, 
##including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”

v = "Albert Einstein once said,"
v1 = "“A person who never made a mistake never tried anything new.”"
print(v+v1)


# In[25]:


#Repeat Exercise 4, but this time store the famous person’s name in a 
##variable called famous_person. Then compose your message and store it in a new variable called message. Print your message.
famous_person = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."
message = f'{famous_person} once said, "{quote}"'
print(message)


# In[26]:


##write addition, subtraction, multiplication, and division operations that each result in the number 8. 
##Be sure to enclose your operations in print statements to see the results. You should create four lines that look like this: print (5 + 3)
##Your output should simply be four lines with the number 8 appearing once on each line

# Addition
print(5 + 3)  # Output: 8

# Subtraction
print(10 - 2)  # Output: 8

# Multiplication
print(4 * 2)  # Output: 8

# Division
print(16 / 2)  # Output: 8.0


# In[27]:


##Store your favourite number in a variable. Then, using that variable, create a message that reveals your favourite number.
##Print that message

favorite_number = 42
message = f"My favorite number is {favorite_number}."
print(message)


# In[28]:


##Choose two of the programs you’ve written and add at least one comment to each. If you don’t have anything specific to write because your programs 
#are too simple at this point, just add your name and the current date at the top of each program file. Then write one sentence describing what the program does

name = "Avinash"
current_date = "19/09/2023"
print(f"My name is {name} and current date is {current_date}")
favorite_number = 42
message = f"My favorite number is {favorite_number}."
print(message)

# Addition
print(5 + 3)  # Output: 8

# Subtraction
print(10 - 2)  # Output: 8

# Multiplication
print(4 * 2)  # Output: 8

# Division
print(16 / 2)  # Output: 8.0


# In[31]:


##Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time

names = ["Avinash","Ajit","Raju","Suraj"]

for name in names:
    print(name)


# In[34]:


##Start with the list you used in Exercise 9, but instead of just printing each person’s name, print a message to them. The text of each message should 
##be the same, but each message should be personalized with the person’s name.

names = ["Avinash","Ajit","Raju","Suraj"]

message_template = "Hello, {}! I hope you're doing good."

for name in names:
    personalized_message = message_template.format(name)
    print(personalized_message)


# In[35]:


#Think of your favourite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a 
#series of statements about these items, such as “I would like to own a Honda motorcycle.”
car_brands = ["Honda", "Toyota", "Ford", "BMW", "Tesla"]

for brand in car_brands:
    print(f"I would like to own a {brand} car.")


# In[ ]:




