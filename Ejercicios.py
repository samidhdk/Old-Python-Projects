import random
import sys
import os
from collections import defaultdict


def guessing_name():
    number = -1
    ask = random.randint(0, 100)
    print(f'--Random is: {ask}\n')
    while (number != ask):
        number = int(input("Introduce a number:"))
        if (number < ask):
            print("Number is higher")
        elif (number > ask):
            print("Number is lower")
        else:
            print("That's right!")


def my_sum(*args):
    a = 0
    for elem in args:
         a += int(elem)
    return a


def run_timing():
    time = []
    while True:
        number = (input("Minutes:"))
        if number != '':
            time.append(int(number))
        else:
            return print(f'Media de las carreras: {sum(time)/len(time)+1} Número de carreras: {len(time)+1}')


def pig_latin():
    text = input("Introduce a text:")
    if text[0] in ('a', 'e', 'i', 'o', 'u'):
        return print(text.split()[0][:]+"way")
    else:
        return print(text.split()[0][1:len(text)+1]+text[0][0]+"ay")


def alphabetical():
    text = input("Introduce a text:")
    ordenado = sorted((text.split()))
    max = 0
    name_max = ""
    for elem in ordenado:
        if len(elem)>max:
            max = len(elem)
            name_max = elem

    return print(f'Palabra de mayor longitud: {name_max}  con un total de {max} letras.\n {ordenado}')


def even_odd_sums(*args):
    even_numbers = 0
    odd_numbers = 0
    for elem in args:
        if elem % 2 == 0:
            even_numbers += elem
        else:
            odd_numbers += elem
    print(even_numbers, odd_numbers)


def plus_minus(*args):
    result = args[0]
    boolean = True
    for elem in args[1:]:
        if boolean:
            result += elem
            boolean = False
        else:
            result -= elem
            boolean = True

    print(result)


def my_zip(*args):
    min_length = len(min(args, key = len))
    result = []
    for i in range(min_length):
        result.append(tuple(item[i] for item in args))
    print(result)


def dictionary(*args):
    general = {}
    for listas in args:
        for dictionaries in listas:

            for key, value in dictionaries.items():
                if key not in general:
                    general.update({key: value})
                else:
                    general[key] = [general[key], value]
    print(f'{general}')
#dictionary([{'foo': 12, 'bar': 14}, {'moo': 52, 'car': 641}, {'doo': 6, 'tar': 84}, {'joo': 48, 'par': 28}, {'moo': 22, 'car': 123}])


def alphabetize_names():
    PEOPLE = [{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
              {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
              {'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'}]

    new_list =  sorted(PEOPLE, key = lambda i: (i['first'], i['last']))
    print(new_list)


def letras_repetidas(texto):
     splitted = str(texto).split()
     diccionario = {}
     contador = 0
     cuenta = 0
     palabra = ""
     for word in splitted:
        diccionario.clear()
        cuenta = 0
        for char in word:
            key = char
            if char in diccionario:
                cuenta+=1
            else:
                diccionario.update({char: 0})
        if cuenta > contador:
            contador = cuenta
            palabra = word
     print(f'palabra: {palabra} contador: {contador}')


def format_sort_records(*args):

    for person in args:
        for data in person:
            surname_spaces = (10 - len(str(data[0]))) * " "
            name_spaces = (10 - len(str(data[1]))) * " "
            hour_spaces = (5 - len(str(format(data[2], ".2f")))) * " "
            print(f'{data[1]} {name_spaces}{data[0]}{surname_spaces} {hour_spaces}{format(data[2],".2f")}')


PEOPLE = [('Donald', 'Trump', 7.85), ('Vladimir', 'Putin', 3.626), ('Jinping', 'Xi', 10.603)]
#format_sort_records(PEOPLE)


def restaurante():
    menu = {'pasta': 8,'agua': 1,'helado': 3,'pescado': 5}
    cuenta = 0

    while True:
        pedido = str(input("Order: ").lower())
        if not pedido:
            print(f"Your total is {cuenta}")
            break
        else:
            if pedido in menu:
                cuenta += menu[pedido]
                print(f"{pedido} costs {menu[pedido]}, total is {cuenta}")
            else:
                print(f"Sorry we are fresh out of {pedido} today")


def dictdiff(dict1, dict2):
    myDict = {}
    for key in dict1:
        if key not in dict2:
            myDict.update({key: [dict1[key], None]})
        elif  dict1[key] != dict2[key]:
            myDict.update({key: [dict1[key], dict2[key]]})
    for key in dict2:
        if key not in dict1:
            myDict.update({key: [None, dict2[key]]})
    print({key: val for key, val in sorted(myDict.items(), key=lambda ele: ele[0])})

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}
d3 = {'a': 1, 'b': 2, 'd': 3}
d4 = {'a': 1, 'b': 2, 'c': 4}
d5 = {'a': 1, 'b': 2, 'd': 4}
#dictdiff(d3,d4)


def extensiones(directorio):
    extension_list = []
    for file in os.listdir(directorio):
        if not os.path.isdir(directorio+"/"+file):
            root_ext = os.path.splitext(file)
            if root_ext[1] not in extension_list:
                extension_list.append(root_ext[1])

    print(extension_list)
#extensiones("D:/URJC/Tercero/DSE")


def tail(fichero):
    with open (fichero) as file:
        lines = (file.readlines())
        last_lines = lines[-10:]
        print(last_lines)

def read_sum(fichero):
    suma = 0
    with open(fichero) as file:
        for lines in file:
            for char in lines:
                if char.isdigit():
                    suma += int(char)
    print(suma)
#read_sum("D:\PyCharm\Ejercicios\sumaNumeros")


def passwd_to_dict(passwd):
    myDict = {}
    with open(passwd) as file:
        for line in file:
            if line.strip():
                if line[0] != "#":
                    name = line.strip().split(":")[0]
                    user_id = line.strip().split(":")[2]
                    myDict.update({name: user_id})
        print(myDict)
#passwd_to_dict("D:\PyCharm\Ejercicios\passwd")


def encrypt(fichero):
    with open (fichero, "r") as file:
        encrypted_document = ""
        document = file.readlines()
        for line in document:
            for char in line:
                encrypted_document += "" + str(ord(char))
    file.close()
    with open(fichero, "w") as file:
        file.write(encrypted_document)
    file.close()

    with open(fichero, "r") as file:
        smt = file.read()
        text = [smt[i:i+2] for i in range(0, len(smt), 2)]
        for word in text:
            print(chr(int(word)), end = '')

# A LOT OF TEXT TO ENCRYPT OR SOMETHING IDK MAN
#encrypt("D:/PyCharm/Ejercicios/toEncrypt")


def myxml(*args):
    if len(args) == 1:
        print(f"<"+args[0]+"><"+args[0]+"/>")
    elif len(args) == 2:
        print(f"<" + args[0] + ">"+args[1]+"<" + args[0] + "/>")
    elif len(args) > 2:
        print(f'<' + args[0] + " "+' '.join(''.join(b[0:2] + '"' + b[2] + '"' for b in str(a).split()) for a in args[2:]) + '>' + args[1] + '<' + args[0] + '/>')


#myxml('foo', 'bar', 'a=1', 'b=2', 'c=3')


def copyfile(*args):
    copia = args[0]
    rutas = args[1:]
    algo = ""
    with open(copia, "r") as c:
        document = c.readlines()
        for line in document:
            algo = algo.join(line)
        c.close()
    for ruta in rutas:
        open(ruta, 'w').close()
        with open(ruta, 'w') as file:
            file.write(algo)
        file.close()


#copyfile('C:/Users/PC/Desktop/testPython/abc.txt', 'C:/Users/PC/Desktop/testPython/123.txt','C:/Users/PC/Desktop/testPython/234.txt', 'C:/Users/PC/Desktop/testPython/345.txt')


class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    max_scoop_number = 3

    def __init__(self):
        self.scoops_in = []

    def add_scoops(self, *scoop):
        for one_scoop in scoop:
            if len(self.scoops_in) < self.max_scoop_number:
                self.scoops_in.append(one_scoop)




        #self.scoops_in.extend(scoop)

    def __str__(self):
        return "This Bowl contains the following flavors:\n- "+ "\n- ".join(f.flavor for f in self.scoops_in)

class Big_Bowl(Bowl):
    max_scoop_number = 5

def create_scoops():
        scoops =[Scoop("Chocolate"), Scoop("Vainilla"), Scoop("Menta")]
        for f in scoops:
            print(f.flavor)

def pedido():
    s1 = Scoop("Chocolate")
    s2 = Scoop("Vainilla")
    s3 = Scoop("Menta")
    b = Big_Bowl()
    b.add_scoops(s1, s2)
    b.add_scoops(s3)
    b.add_scoops(s3, s2)
    print(b)


class Animal:
    def __init__(self,color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __str__(self):
        return f"{self.color} {self.species}, {self.number_of_legs} legs"

class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)
class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

wolf = Wolf('black')
sheep = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')

class Cage:

    def __init__(self, id):
        self.id = id
        self.animals = []
    def add_animals(self, *animals):
        self.animals.extend(animals)
    def __repr__(self):
        output = f'Cage {self.id}\n'
        output += '\n'.join('\t' + str(animal)
                            for animal in self.animals)
        return output


c1 = Cage(1)
c1.add_animals(wolf, sheep)
c2 = Cage(2)
c2.add_animals(snake, parrot)

class Zoo:
    def __init__(self):
        self.cages = []
    def add_cages(self, *cages):
        self.cages.extend(cages)
    def __repr__(self):

        return "Cages:\n" + "\n".join(str(k) for k in self.cages)

    def animals_by_color(self, color):
        list_color = []
        for cage in self.cages:
            for animal in cage.animals:
                if animal.color == color:
                    list_color.append(animal.species)
        return list_color

    def animals_by_legs(self, legs):
        list_legs = []
        for cage in self.cages:
            for animal in cage.animals:
                if animal.number_of_legs == legs:
                    list_legs.append(animal.species)
        return list_legs

    def number_of_legs(self):
        legs = 0
        for cage in self.cages:
            for animal in cage.animals:
                legs += animal.number_of_legs
        return legs

z = Zoo()
z.add_cages(c1, c2)
print(z)
print(z.animals_by_color('white'))
print(z.animals_by_legs(4))
print(z.number_of_legs())







