from random import randint


def random_num(upper_limit):
    r_num = (randint(1, upper_limit))
    return r_num


a = random_num(100)
print(a)


b = random_num(random_num(random_num(15)))
print(b)


