# https://pastebin.com/rPqgpEVV

my_list = []

for _ in range(3):
    data = input()
    my_list.append(data)

my_list[0], my_list[2] = my_list[2], my_list[0]    #slap -ване: смяна на местата в листа

print(my_list)
