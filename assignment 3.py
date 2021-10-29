#!/usr/bin/env python
# coding: utf-8

# # Q1.Write a Python Program to implement your own myreduce() function which works exactlylike Python's built-in function reduce()
# 

# In[2]:


def myreduce(func,values):
    result=values[0]
    for i in values[1:]:
        result=func(result,i)
    return result    


# In[3]:


def func(x,y):
    return x*y


# In[7]:


list1=[2,3,4,5,6,7,8,9]
print(f"my reduce output is :  { myreduce(func,list1)} ")


# # Q2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()

# In[13]:


def myfilter(func,values):
    result=list()
    for i in values:
        if func(i):
            result.append(i)
    return result


# In[14]:


def func(x):
    if x%3==0:
        return True
    else:
        return False
    


# In[15]:


list2=[3,4,56,73,45,63,245]
print(f"my filter output is: {myfilter(func,list2)}")


# # Q3.Implement List comprehensions to produce the following lists.  
# Write List comprehensions to produce the following Lists  
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']  
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']  
# [[2], [3], [4], [3], [4], [5], [4], [5], [6],
# 
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
# 

# # 1.['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

# In[5]:


lst = ['x','y','z']
lst1 = [i*j for j in lst for i in range(1,5)]
print(lst1)


# # 2.['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']

# In[3]:


lst = ['x','y','z']
lst2 = [i*j for j in range(1,5) for i in lst]
print(lst2)


# # 3. [[2], [3], [4], [3], [4], [5], [4], [5], [6]]

# In[8]:


lst = [[a+b] for b in range(0,3) for a in range(2,5)]
print(lst)


# # 4.[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[1]:


lst = [(p, q) for q in range(1, 4) for p in range(1, 4)]
print(lst)


# In[ ]:




