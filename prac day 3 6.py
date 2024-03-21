def reverse_number(num):
    return int(str(num)[::-1])

def is_mirror(num):
    return num == reverse_number(num)

def find_mirror_number(num):
    reversed_num = reverse_number(num)
    if is_mirror(reversed_num):
        return reversed_num
    else:
        return "No mirror number exists"

num = input("Enter the number: ")
mirror_num = find_mirror_number(num)
print("Mirror image:", mirror_num)
