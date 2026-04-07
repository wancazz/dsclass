#!/usr/bin/env python
# coding: utf-8

# In[4]:


def nameAge(name,age):
    print("Hi, I am " + name)
    print("My age is " + str(age))


# In[3]:


def make_pizza(size, *toppings): #the arbitrary argument must be placed last and only one arbitrary number of arguments can be used
    """Summarise the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

