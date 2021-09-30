import random
def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield(random.randint(begin, end))
a=gen_random(5, 1, 3)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
   