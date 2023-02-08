def unique(my_list):
    mydict = {}
    list = []
    for i in my_list:
        if(i not in mydict):
            mydict[i] = 1
        else:
            mydict[i] += 1
    for temp1, temp2 in mydict.items():
        if(temp2 == 1):
            list.append(temp1)
    return 