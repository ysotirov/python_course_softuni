"DICTIONARIES"      # values - mutable - променлив. може да се добавя променя ...
                    # keys - immutable
                    # референтен тип данни

classes = {'1A': ["Ines", "Georgi", "Pesho"], '1B': ["Ivan", "Tosho", "Maria"]}   # един ключ може да садържа множество велюта
students = {'№1': {'name': 'Pesho', 'ages': 12}, '№2': {'name': 'Ivan', 'ages': 11}}
my_dict = {'a': 25, 'b': "Pesho", 2: 33}
num_dict = {'a': 1, 'b': 2, 'c': 3}
letter_dict = {'A': 4, 'C': 3, 'B': 1, 'D': 2}
names_ages = {"Ines": 27,
              "Georgi": 43,
              "Pesho": 40,
              "Marieta": 37,
              "Tosho": 46,
              "Maria": 52}      # така е по PEP стандарт


"ДОБАВЯНЕ В РЕЧНИКА"
# my_dict["eyes color"] = "green"
# print(my_dict)

# names = classes["1A"]             # дава ни достъп до вложения лист
# names.append("appended name")     # както обикновен лист
# print(classes)

# for key in classes:
#     classes[key].append("from the loop")
# print(classes)

# for key in num_dict:
#     num_dict[key] *= 2
# print(num_dict)


"ПРОМЯНА В РЕЧНИКА"
# my_dict["eyes color"] = "green"
# print(my_dict)
# my_dict["b"] = 30
# print(my_dict)

# names = classes["1A"]             # дава ни достъп до листа и вече работим с него
# names.append("appended name")     # както обикновен лист
# print(classes)

# for key in classes:
#     classes[key].append("from the loop")
# print(classes)

# for key in num_dict:
#     num_dict[key] *= 2
# print(num_dict)


"ИЗВИКВАНЕ ПО ВЛОЖЕН РЕЧНИК"
# print(classes['1A'][1])
# print(students['№1']['name'])


"ИЗВИКВАНЕ НА VALUE ПО КЛЮЧ"
# print(my_dict["b"])       # вика ключ 2, тук индекси няма, гарми ако индекса го няма

# print(my_dict.get(2))
# print(my_dict.get(3))


"ВРЪЩА СПИСЪК С VALUE"
# print(list(num_dict.values()))


"ВРЪЩА СПИСЪК СУМАТА НА VALUE"
# print(sum(num_dict.values()))


"ПРЕМАХВА K-V ДВОЙКА"
# my_dict.pop("b")        # премахва по ключ
# print(my_dict)
#
# my_dict.popitem()       # премахва последната двойка
# print(my_dict)

# print(my_dict)
# del my_dict['a']
# print(my_dict)

# dictionary = my_dict
# del dictionary          # трие цялата променлива


"СОРТИРАНЕ"
# print(sorted(num_dict))         # принтва лист със сортирани само ключовете

# print(sorted(letter_dict.items(), key=lambda x: x[0]))   #за sorte с key lambda прави for-цикъл за всяко „x“ от x[0]
# print(sorted(letter_dict.items(), key=lambda x: x[0], reverse=True))      # подрежда по value
# print(sorted(num_dict.items(), key=lambda x: - x[1]))                     # обръща реда на int

# print(sorted(names_ages.items(), key=lambda x: (x[0], - x[1])))     # сортира по два параметъра


"ВРЪЩА VALUE"       # a
# print(my_dict.pop("b"))   # връща value по ключ
# print(my_dict.popitem())    # връща последната двойка като тюпъл


"ИЗВИКВАНЕ VALUE ПО ИНДЕКС"
# names = classes['1A']
# print(names[0])
# print(names[0][0])
# print(type(names))


"ОБХОЖДАНЕ - ИТЕРИРАНЕ"
# print(classes.keys())
# print(classes.values())
# print(my_dict.values())
# print(my_dict.items())      # връща tupple

# for key in my_dict:
    # print(key)

# for _ in my_dict.values():
#     print(_)
# for key, value in classes.items():
#     print(f"key is {key}, and value is {value}")


"DICT COMPREHENSION"
# print({value: key for key, value in names_ages.items() if value % 2 == 0})

# data = [("Peter", 22), ("Amy", 18), ("George", 35)]     # връща dict от тюпъли
# print({key: value for (key, value) in data})
# print(dict(data))

# num_list = [1, 2, 3, 4]
# print({num: num ** 3 for num in num_list})    # от лист връща dict със стойноста на 3та степен


# even_years = {}
# for key, value in names_ages.items():
#     if value % 2 == 0:
#         even_years[key] = value
# print(even_years)


"ПРЕВЪРЩА СПИСЪЦИ В РЕЧНИК"     #
# keys = ['a', 'b', 'c', 'd']
# values = [1, 2, 3]
# print(dict(zip(keys, values)))
# print(dict(zip(values, keys)))

# my_dict = {}        # листовете трябва да са еднакво дълги
# for index in range(len(keys)):
#     my_dict[keys[index]] = values[index]
# print(my_dict)


"ДАВА БРОЙКАТА НА KEY"
# print(len(my_dict))


"ТЪРСИ В РЕЧНИКА"
# print("a" in num_dict)      # търси в ключа
# print("f" in num_dict)
#
# print(3 in num_dict.values())   # търси в value


"ИЗПРАЗВАНЕ НА РЕЧНИКА"
# print(my_dict.clear())


"КОПИРА РЕЧНИКА"
# b = my_dict.copy()

"ВРЪЩА СПИСЪК С ТЮПЪЛИ"
# print(num_dict.items())
