immutable_var = (1, 2, [3, 4], 'a', 'b', True)
print(immutable_var)
immutable_var[2][1] = 3 # получится заменить, т.к. меняем данные внутри объекта, а не сам объект
print(immutable_var)
# immutable_var[1] = 3 -> ошибка,т.к. это кортеж, а объекты кортежа неизменны.

mutable_list = [1, 2, 'a', 'b', True]
mutable_list[1] = 3
mutable_list[3] = False
print(mutable_list)
