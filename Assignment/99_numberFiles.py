import os

files = os.listdir()
# exclude .git and .gitignore and 0
files.pop(0)
files.pop(0)
ind = 1
for file in files:
    print(f'mv {file} {ind}_{file}')
    os.system(f'mv {file} {ind}_{file}')
    ind+=1
