def len_str(text):
    return len(text)


def combine_strings(text1, text2):
    return text1 + text2

def square_number (num):
    return num ** 2

def sum_numbers (num1, num2):
    return num1 + num2

def divide_numbers(num1, num2):
    whole_part = num1 // num2
    remainder = num1 % num2
    return whole_part, remainder

def average (list1):
    return sum(list1)/len(list1)

def common_elements (list1, list2):
    result = []

    for num in list1:
        if num in list2:
            result.append(num)
    return result

def print_keys (dictionary):
    for key in dictionary:
        print(key)

def merge_dictionaries(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

def union_sets(set1, set2):
    return set1.union(set2)

def is_subset(set1, set2):
    return set1.issubset(set2)

def even_or_odd (num1):
    if num1 % 2 == 0:
        print('Even')
    else:
        print('Odd')

def only_even (list1):
    even_list = []
    for num in list1:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

even_or_odd2 = lambda num: "even" if num % 2 == 0 else "odd"


