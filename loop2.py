# data = "baba shankar"
# for i in data:
#     print(i,end=' ')


# colors = ['red','blue','green','yellow']
# for color in colors:
#     print(color)
#     for i in color:
#         print('[',i,']',end=',')
#     print('\n')
# k = int(input())
# if k<=1:
#     print('not prime')
# elif k==2:
#     print('prime')
# elif k>=2:
#     for i in range(2, k):
#         if k % i == 0:
#             print('its not prime')
#             break
#
#         else:
#             print('prime')
#             break

k = int(input('enter'))

for j in range(2,k):
    for i in range(2,j):
            if j % i == 0:
                continue

            elif j % i != 0:
                print(i,j)
data = ['ind','usa','uk']
print('M')
for i in data:
    print('A')
    print(i[0])
print('C')