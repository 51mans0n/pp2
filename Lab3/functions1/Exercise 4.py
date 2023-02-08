def filter_prime(my_list):
    list = []
    for i in my_list:
        counter = 0
        if(i == 2):
            list.append(i)
            continue
        elif(i == 1):
            continue
        for j in range(2, i):
            if(i % j == 0):
                counter += 1
        if(counter == 0):
            list.append(i)
    return list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_prime(my_list))