#1.

from time import sleep


class TrafficLight():

    def __init__(self):
        self.__color = (('Red', 5), ('Yellow', 2), ('Green', 5))

    def running(self):
        for color, sec in (self.__color):
            print(color, '(wait {} sec)'.format(sec))
            sleep(sec)


traffic_ligth = TrafficLight()
traffic_ligth.running()

#2.

class Road():
    def __init__(self, leght, width):
        self.__legth = leght
        self.__width = width

    def mass(self):
        mass = self.__legth * self.__width * 25 * 5 / 1000
        return mass


road_mass = Road(20, 5000)
print(road_mass.mass())

# 3.

worker_income = {'оклад': 150000, 'премия': 25555}


class Worker():

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = worker_income


class Position(Worker):
    def worker_method(self):
        get_full_name = (self.name + self.surname)
        get_local_incom = (self.position + str(self._income))
        print(get_full_name)
        print(get_local_incom)


my_worker = (Position('Иван ', 'Алексеев ', 'рабочий ', worker_income))
my_worker.worker_method()


# 4.

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print('The car is go')

    def stop(self):
        print('The car is stop')

    def tern(self, direction):
        print(f'The car turn to the' + direction)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            print('Attention, too fast!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            print('Attention, too fast!')


class PoliceCar(Car):
    pass


town_car = TownCar(60, 'Black', 'TownCar', False)
sport_car = SportCar(200, 'Yellow', 'SportCar', False)
work_car = WorkCar(30, 'White', 'WorkCar', False)
police_car = PoliceCar(220, 'Alternative', 'PoliceCar', True)

town_car.show_speed()
sport_car.show_speed()
work_car.show_speed()
police_car.show_speed()


# 5.


class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Ручка пишет')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш чертит')


class Handle(Stationery):
    def draw(self):
        print('Маркер рисует')

pen = Pen('Ручка')
pen.draw()
pencil = Pencil('Карандаш')
pencil.draw()
handle = Handle ('Маркер')
handle.draw()


