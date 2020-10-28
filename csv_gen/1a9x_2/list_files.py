import os
import re

files = [file for file in os.listdir(".")] 


for file in sorted(files,key=os.path.getmtime):
    print(file)
