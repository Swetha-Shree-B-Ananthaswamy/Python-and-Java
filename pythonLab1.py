#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
# Based on code provided by Dr. De Luca in class.
print("Gennaro's Magical CLI")
print()


# In[2]:


# Seting the set of files inside the directory.
def run_ls():
    contents = os.listdir()
    for content in contents:
        print(content)


# In[3]:


# Executing the help command
def run_help():
    print(help(os))


# In[4]:


# Executing the clear command to clear the terminal
def run_clr():
    os.system('cls' if os.name == 'nt' else 'clear')
    


# In[5]:


# Executing of pause ,untill you press Enter Key.
def run_pause():
    input("Press Enter Key to Continue . . .")
    


# In[6]:


# Executing of the set command , list of the Envirolment veriable.
def run_environ():
    for k, v in os.environ.items():
        print(f'{k}={v}')


# In[7]:


# Execution of echo command 
def run_echo(input):
    stream = os.popen(input)
    output = stream.read()
    print(output)
    
        


# In[8]:


#Execution of change directory command.

def run_cd(input):
    print(os.getcwd())
    x = input.split(' ')
    os.chdir(x[1])
    
    


# In[9]:


# Execution of redirection command,to do redirection to the output file.
import sys
def run_redirection(input):
    
    if '>>' in input:
        append = input.split('>>')
        file = open(append[1] ,'a')
        response = os.popen(append[0])
        for y in response.readlines():
            file.write(y)
            
        file.close()
    elif '>' in input:
        trancate = input.split('>')
        file = open(trancate[1] ,'w')
        response = os.popen(trancate[0])
        for y in response.readlines():
            file.write(y)
            
        file.close()


# In[10]:


cwd = os.getcwd()


# In[ ]:


#Execution of the set of command to do certain opperations.
import sys
while True:
    command = input(cwd + ">")
    command = command.lower()
    if command == "quit":
        break
    elif command == "ls" or command == "dir":
        run_ls()
        print()
    elif command == "clr" or command == "cls" or command == "clear":
        run_clr()
        print()
    elif command == "help":
        run_help()
        print()
    elif command == "pause":
        run_pause()
        print()
    #works for windows    
    elif command == "set":
        run_environ()
        print()    
    elif command.startswith("echo"):
        run_echo(command)
        print()
    elif command.startswith("cd"):
        run_cd(command)
        cwd = os.getcwd()
        print()
        print()
    elif '>' in command or '>>' in command:
        run_redirection(command)
        print()
        print()
    else:
        print()
        print()
        print("'" + command + "' is not recognized as an internal or external command, operable program or batch file.\n")


# In[ ]:





# In[ ]:




