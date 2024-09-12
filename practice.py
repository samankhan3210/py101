def non_mutating_delete(lst):
    lst_2 = lst[:]
    lst_2.pop()
    return lst_2

lst = [1, 2, 3]

print(non_mutating_delete(lst) == [1, 2]) #=> True
print(lst == [1, 2, 3]) #=> True