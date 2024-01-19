import os

path = input(r'enter the path:')
file_name = input('enter the file_name')
print(file_name)
for root_dictory,directories,files in os.walk(path):
    if file_name in files:
        p = os.path.join(root_dictory,file_name)
        print(p)
        print('done')
