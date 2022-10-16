import db
import logger


def get_value_name():
    global name
    name = str(input('Введите имя абонента, name= '))
    return name


def get_value_surname():
    global surname
    surname = str(input('surname= '))
    return surname


def get_value_mobile():
    global mobile
    mobile = str(input('mobile= '))
    return mobile


def type_of_operation():
    global result
    result = logger.write()
    return result

def var_of_operation():
    global var
    var = input('какую операцию вы хотите сделать в справочнике (w/f)?:   ')
    # if op == 'w':
    #     var = math_f.write()
    # elif op == 'f':
    #      result = math_f.read()
    return var