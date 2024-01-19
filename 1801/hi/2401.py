import os

for i,j,k in os.walk(r'I:'):
    if "Chapter_2.txt" in k:
        p= os.path.join(r'I:',i,"Chapter_2.txt")
        print(p)