#!/usr/bin/env python
# coding: utf-8

# In[71]:


def check_email(name):
    #print(name)
    count=0
    upper=0
    spaces=0
    for i in name:
        if(i.isupper()):
            upper+=1
        if (i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="7" or i=="8" or i=="9"):
            count+=1
        if(i==" "):
            spaces+=1
    if(upper>0):
            print("Upper case is not allow")
    if(count>4 or count<4):
        print("Enter 4 number")        
    if(spaces>0):
        print("spaces are not allowed ")
        return 0
    nums=len(name)-count
    alfa= name[:nums]
    number=name[num:]
    for i in alfa:
         if (i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="7" or i=="8" or i=="9"):
                print(" gmail not contain number in between name ")
                print(" enter again")
                

        
string=input(" Enter gmail ID :")
num=len(string)-10
name=string[:num]
n=string[num:]
if n!="@gmail.com":
    print(" Invalid gmail ID")
else:
    g=check_email(name)
    
if(g!=0):
    print(string)
    



# In[ ]:





# In[ ]:




