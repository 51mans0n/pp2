def reverseSentence(str):
    str = str.split(" ")
    mylist = list(str)
    mylist.reverse()
    for i in mylist:
        print(i, end = ' ')
reverseSentence("We are ready")