# g=4
# k = 96 +g
# for i in range(1,g):
#     print(((g-i)*2)*'-',end='')
#     u_l=[]
#     for j in range(i):
#         u_l.append(chr(k-j))
#     out='-'.join(u_l)
#     print(out,end='')
#     out_l=[]
#     for d in range(0,i-1):
#         out_l.append(chr(k-d))
#     revers=[]
#     for u in out_l:
#         revers.insert(0,u)
#     out1='-'.join( revers )
#     if i>1:
#         print('-',end='')
#     print(out1)
def print_rangoli(size):
    print(size)

n = int(input())
print_rangoli(n)