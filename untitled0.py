# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 17:29:20 2022

@author: 786
"""

def prime_finder(n):
  # Write your code here
  my_list=[]
  for i in range(2,n+1):
   check = 1
   for j in range(2,i):
    if i%j==0: 
      check=0
      break
  
   if check==1:
    print(i)
    my_list.append(i)

  return my_list
  


 
print(prime_finder(11))