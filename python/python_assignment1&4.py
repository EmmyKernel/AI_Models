def reverse_name(name):
    return name[::-1]

def change_list_val(List, index, new_value):
    List[index] = new_value
    return List


if __name__ == "__main__":
    name = input('Enter string: ')
    print('Q1:', reverse_name(name))
    print(change_list_val([10,20,30,40,50],0,900))

    

