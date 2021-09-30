import json
from typing import Text
from cm_timer import cm_timer_1, cm_timer_2
from field import field
from print_result import print_result
from unique import Unique
from gen_random import gen_random
import sys

path = r"C:\Users\danib\Documents\pyton\Lab3\data_light.json"

with open(path, encoding='UTF-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return(list(sorted(Unique(field(arg,'job-name'),ignore_case=True),reverse=True)))
@print_result
def f2(arg):
    return(list(filter(  lambda x: x.startswith('Программист'), arg)))

@print_result
def f3(arg):
    return(list(map( lambda x: x + ' с опытом Python', arg ) ))
@print_result
def f4(arg):
    for i,j in zip(list(gen_random(len(arg), 100000,200000)),list(range(len(arg)))):
        arg[j]=(arg[j]+' с зарплатой '+ str(i))
    return(arg)

if __name__ == '__main__':
    with cm_timer_1():
        print(f4(f3(f2(f1(data)))))
        