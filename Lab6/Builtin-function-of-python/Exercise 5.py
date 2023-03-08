def TupleTrue():
    MyTuple = (33, False, "TV", True, 49)
    for i in MyTuple:
        if(bool(i)):
            return False
    return True