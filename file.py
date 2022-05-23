# task 2.1
def greeter(func):
    def inner(*args):
        return "Aloha " + func(*args).title()
    return inner


# task 2.2
def sums_of_str_elements_are_equal(func):
    def wrapper(*args, **kwargs):
        number_list = func(*args, **kwargs).split()
        first_number = second_number = 0

        for n in number_list[0]:
            if n != "-":
                first_number += int(n)
        if number_list[0][0] == "-":
            first_number *= -1

        for n in number_list[1]:
            if n != "-":
                second_number += int(n)
        if number_list[1][0] == "-":
            second_number *= -1

        if first_number == second_number:
            return str(first_number) + " == " + str(second_number)
        else:
            return str(first_number) + " != " + str(second_number)
    return wrapper


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
