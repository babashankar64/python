list1 = [1, 2, 3, [4, 5, 6], 4, [5, [6, 7]]]


def sum_list(list1):
    sum_all = 0
    for i in list1:
        if isinstance(i,int):
            sum_all = sum_all + i
        else:
            sum_all = sum_all + sum_list(i)
    return sum_all
out = sum_list(list1)
print(out)