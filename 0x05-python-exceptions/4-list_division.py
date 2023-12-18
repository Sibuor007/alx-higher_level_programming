#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element
    Args:
    my_list_1 (list): first list.
    my_list_2 (list): second list.
    list_length (int): number of elements
    Returns: A new list
    """
    other_list = []
    for item in range(0, list_length):
        try:
            result = my_list_1[item] / my_list_2[item]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            other_list.append(result)
        return (other_list)
