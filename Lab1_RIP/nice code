import sys
import math

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
       
    # Переводим строку в действительное число
    while not is_number(coef_str):
        print('Некоректное число, повторите ввод: ')
        coef_str = input()

    coef = float(coef_str)
    return coef
def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        if root == 0:
            result.append(root)
        elif root>0:
             root1=math.sqrt(root)
             root2=-math.sqrt(root)
             result.append(root1)
             result.append(root2)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root_1 = (-b + sqD) / (2.0*a)
        root_2 = (-b - sqD) / (2.0*a)
        if root_1>0:
            root1=math.sqrt(root_1)
            root2=-math.sqrt(root_1)
            result.append(root1)
            result.append(root2)
        if root_2>0:
            root3=math.sqrt(root_2)
            root4=-math.sqrt(root_2)
            result.append(root3)
            result.append(root4)
        if root_1==0 or root_2==0:
            result.append(0.0)
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)

    ''' 
     Можно, не меняя функцию, добавить эти строки, и программа тоже будет считать биквадратное уравнение
     if len_roots == 1 :
         roots = get_roots(1,0,-roots[0])
    elif len_roots == 2:
        roots = get_roots(1,0,-roots[0])+get_roots(1,0,-roots[1])
    len_roots = len(roots)'''

    if len_roots == 0:
        print ('Корней нет')
    elif len_roots == 1:
        print('Один корень: {} '.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} и {} и {}'.format(roots[0], roots[1],roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {} и {} и {} и {}'.format(roots[0], roots[1],roots[2],roots[3]))

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
