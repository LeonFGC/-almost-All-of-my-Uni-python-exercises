
lst = list(range(5))
print(lst)

mtx = [list(range(5)) for _ in range(5)]
print(mtx)


lst = [list(range(x)) for x in range(5)]
print(lst)

cols_B=2
rows_A=3
lst =  [[0 for row in range(cols_B)] for col in range(rows_A)]
print(lst)
