# # print(range(5))
# # print(list(range(5)))
# # print(tuple(range(5)))
# # print(set(range(5)))
# # print(str(range(5)))
# def test1(a,b):
#     print('A')
#     yield a+b
#     print('B')
#     yield a*b
#     print('C')
#     yield a/b
# out= test1(5,6)
#
# for i in out:
#     print(i)
#     input()
# import time
#
# print(time.time())
class squares:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __iter__(self):
        print('A')
        return self
    def __next__(self):
        print("i am in next")
        res = self.start * self.start
        self.start = self.start + 1
        return  res

out = squares(2,5)
for i in out:
    print(i)
    input()
