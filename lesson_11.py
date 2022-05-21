# 1
class Data:

    def __init__(self):
        self.date = None

    def set_date(self, date):
        if Data.validation(Data.str_to_int(date)):
            self.date = date

    @classmethod
    def str_to_int(cls, date):
        res = list(map(int, date.split('-')))

        return res

    @staticmethod
    def validation(res):
        day, month, year = res
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 9999 >= year >= 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


print(Data.validation(Data.str_to_int("20-02-2002")))
print(Data.validation(Data.str_to_int("29-05-1996")))
print(Data.validation(Data.str_to_int("45-02-2022")))
print()
today = Data()
today.set_date("10-05-2022")
print(today.date)
print()
a = Data()
a.set_date("45-02-2022")
print(a.date)

#2.


class ZeroDivision(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return 'ERROR: ZeroDivision\n {0}'.format(self.message) if self.message else 'ZeroDivision has been raised.'


while True:
    dividend = input('Введите чило (делимое): ')
    if dividend == 'q':
        break
    divisor = input('Введите второе число (делитель): ')
    if divisor == 'q':
        break

    try:
        dividend = int(dividend)
        divisor = int(divisor)

        if divisor == 0:
            raise ZeroDivision("На ноль делить нельзя")

    except ValueError:
        print('введите числовое значение.')
    except ZeroDivision as err:
        print(err)
    else:
        print(f'результат: {dividend / divisor}')



# 3

class ElementError(Exception):
    def __init__(self, el):
        self.message = el if el else None

    def __str__(self):
        return f'Error: ElementError\n {self.message}' if self.message else 'Error: ElementError'


user_list = []


def get_num(x):
    if x[0] in '+-':
        return x[1:]


while True:
    user_inp = input('Enter a number: ')
    if user_inp == 'stop':
        break
    try:
        if user_inp.isdigit() or get_num(user_inp):
            user_list.append(int(user_inp))
        else:
            raise ElementError('Your number must be a digit.')
    except ElementError as e:
        print(e)
    else:
        print(f"Your number {user_inp} has been added to the list")

print(user_list)



#4,5,6

import re


class WrongSerialNum(Exception):
    def __init__(self, txt):
        self.txt = txt if txt else None

    def __str__(self):
        return f'Error: WrongSerialNum\n {self.txt}' if self.txt else 'Error: WrongSerialNum'


class Warehouse:
    """Учет всей техники ведется по серийным номерам"""
    storage = {'printers': [], 'scanners': [], 'copiers': []}

    all_stored_serial_nums = []
    printer_amount = 0
    copier_amount = 0
    scanner_amount = 0
    equipment_amount = 0

    @classmethod
    def goes_in(cls, equipment):
        if isinstance(equipment, Printer):
            try:
                if equipment.serial_number in cls.all_stored_serial_nums:
                    raise WrongSerialNum('This equipment already exists.')
            except WrongSerialNum as err:
                print(err)
            else:
                cls.storage['printers'].append({equipment.serial_number: equipment.__dict__})
                cls.all_stored_serial_nums.append(equipment.serial_number)
                cls.equipment_amount += 1
                cls.printer_amount += 1
        if isinstance(equipment, Scanner):
            try:
                if equipment.serial_number in cls.all_stored_serial_nums:
                    raise WrongSerialNum('This equipment already exists.')
            except WrongSerialNum as err:
                print(err)
            else:
                cls.storage['scanners'].append({equipment.serial_number: equipment.__dict__})
                cls.all_stored_serial_nums.append(equipment.serial_number)
                cls.equipment_amount += 1
                cls.scanner_amount += 1
        if isinstance(equipment, Copier):
            try:
                if equipment.serial_number in cls.all_stored_serial_nums:
                    raise WrongSerialNum('This equipment already exists.')
            except WrongSerialNum as err:
                print(err)
            else:
                cls.storage['copiers'].append({equipment.serial_number: equipment.__dict__})
                cls.all_stored_serial_nums.append(equipment.serial_number)
                cls.equipment_amount += 1
                cls.copier_amount += 1

    @classmethod
    def goes_out(cls, equipment):
        if equipment.__class__ == Printer:
            cls.all_stored_serial_nums.remove(equipment.serial_number)
            cls.equipment_amount -= 1
            cls.printer_amount -= 1
            for el in cls.storage['printers']:
                if equipment.serial_number in el:
                    cls.storage['printers'].remove(el)
            print(f'{equipment.model} is out. ')

        if equipment.__class__ == Scanner:
            cls.all_stored_serial_nums.remove(equipment.serial_number)
            cls.equipment_amount -= 1
            cls.printer_amount -= 1
            for el in cls.storage['scanners']:
                if equipment.serial_number in el:
                    cls.storage['scanners'].remove(el)
            print(f'{equipment.model} is out. ')

        if equipment.__class__ == Copier:
            cls.all_stored_serial_nums.remove(equipment.serial_number)
            cls.equipment_amount -= 1
            cls.printer_amount -= 1
            for el in cls.storage['copiers']:
                if equipment.serial_number in el:
                    cls.storage['copiers'].remove(el)
            print(f'{equipment.model} is out. ')


class OfficeEquipment:

    def __init__(self, model, color, serial_number):
        self.model = model
        self.color = color
        try:
            if OfficeEquipment.validate_serial(serial_number):
                self.serial_number = serial_number

            else:
                raise WrongSerialNum('Serial number is incorrect')
        except WrongSerialNum as err:
            print(err)

    def __str__(self):
        return f"Info:\n Model: {self.model}\nColor: {self.color}\nSerial number: {self.serial_number}"

    @staticmethod
    def validate_serial(arg):
        """Проверка серийного номера"""

        re_serial = re.compile(r'^[A-Z]{4}[0-9]{4}$')
        if re_serial.match(arg):
            return bool(re_serial.match(arg))


class Printer(OfficeEquipment):
    p = 0

    def __init__(self, model, color, serial_number, print_technology, print_speed):
        super().__init__(model, color, serial_number)
        self.print_technology = print_technology
        self.print_speed = int(print_speed)
        Printer.p += 1

    def get_amount_p(self):
        return self.p

    def __str__(self):
        return f"Info:\nModel: {self.model}\nColor: {self.color}\nSerial number: {self.serial_number}\n" \
               f"Print technology: {self.print_technology}\nPrint speed: {self.print_speed}"


class Scanner(OfficeEquipment):
    s = 0

    def __init__(self, model, color, serial_number, scan_technology, scanner_type):
        super().__init__(model, color, serial_number)
        self.scan_technology = scan_technology
        self.scanner_type = scanner_type
        Scanner.s += 1

    def __str__(self):
        return f"Info:\nModel: {self.model}\nColor: {self.color}\nSerial number: {self.serial_number}\n" \
               f"Scan technology: {self.scan_technology}\nScanner type: {self.scanner_type}"


class Copier(OfficeEquipment):
    c = 0

    def __init__(self, model, color, serial_number, copy_speed):
        super().__init__(model, color, serial_number)
        self.copy_speed = int(copy_speed)
        Copier.c += 1

    def __str__(self):
        return f"Info:\nModel: {self.model}\nColor: {self.color}\nSerial number: {self.serial_number}\n" \
               f"Copy speed: {self.copy_speed}"


print(Warehouse.equipment_amount, Warehouse.printer_amount, Warehouse.scanner_amount, Warehouse.copier_amount,
      Warehouse.storage, sep='\n')
printer1 = Printer("HP DeskJet 2710e", 'white', 'FGHK2582', 'inkjet', 25)
printer2 = Printer("EPSON 800", 'black', 'JING1101', 'laser', 22)
scanner1 = Scanner('HP ScanJet Pro 2500 f1', 'white', 'QWER8546', 'CMOS CIS', 'Flatbed')
copier1 = Copier('Panasonic T8100', 'pink', 'COUR4569', 22)
Warehouse.goes_in(printer1)
Warehouse.goes_in(scanner1)
Warehouse.goes_in(copier1)
Warehouse.goes_in(printer2)
print(Warehouse.storage)
print('X' * 250)
print(Warehouse.equipment_amount, Warehouse.printer_amount, Warehouse.scanner_amount, Warehouse.copier_amount,
      Warehouse.storage, sep='\n')
Warehouse.goes_out(printer1)
Warehouse.goes_out(copier1)
print('X' * 250)
print(Warehouse.equipment_amount, Warehouse.printer_amount, Warehouse.scanner_amount, Warehouse.copier_amount,
      Warehouse.storage, sep='\n')

#  7.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        # self.z = f'{self.a} + {self.b}i'

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __str__(self):
        if self.a != 0:
            if self.b > 0:
                if self.b != 1:
                    return f'{self.a}+{self.b}i'
                else:
                    return f'{self.a}+i'
            elif self.b == 0:
                return f'{self.a}'
            else:
                return f'{self.a}{self.b}i'
        else:
            if self.b == 0:
                return f'0'
            else:
                return f'{self.b}i'


complex_num1 = ComplexNumber(10, -2)
complex_num2 = ComplexNumber(6, 3)
sum_complex = complex_num1 + complex_num2
print(sum_complex)
mult_complex = complex_num1 * complex_num2
print(mult_complex)