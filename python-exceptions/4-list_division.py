#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            num1 = my_list_1[i] if i < len(my_list_1) else 0
            num2 = my_list_2[i] if i < len(my_list_2) else 1  # Use 1 as the default for division if list_2 is too short

            if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
                raise TypeError("wrong type")

            if num2 == 0:
                raise ZeroDivisionError("division by 0")

            result.append(num1 / num2)

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)

        except TypeError:
            print("wrong type")
            result.append(0)

        except IndexError:
            print("out of range")
            result.append(0)

        finally:
            pass  # Optional code to execute regardless of exceptions

    return result
