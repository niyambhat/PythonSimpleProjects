list = [1,2,3]

def add_to_list():
    newList = list.copy()
    newList.append(4)
    return newList

print(add_to_list())