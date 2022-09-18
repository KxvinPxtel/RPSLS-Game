#Clear Console File
#Code used to clear the console when function is called
#Kevin Patel
#Jan 18th, 2022

#Import os to interact with operating system
import os

#A function to clear the console when clearconsole command is used
def clearconsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)