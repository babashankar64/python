# import re
#
# inp = input()
# for i in range(int(inp)):
#     input1 = input()
#     try:
#         re.compile(input())
#         print(True)
#     except Exception:
#         print(False)


def outer_func(x):
    def inner_func():
        return x
    x=x + 5
    return inner_func()
results = outer_func(6)
print(results)
