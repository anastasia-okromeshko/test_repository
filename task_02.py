# Создать класс Car. Атрибуты: марка, модель, год скорость(по умолчанию 0).
# Методы: увеличить скорости(скорость + 5), уменьшение
# скорости(скорость - 5), стоп(сброс скорости на 0),
# отображение скорости, разворот(изменение знака
# скорости). Все атрибуты приватные.
from typing import Union

class Car():
    def __init__(self, brand, model, year, speed = 0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed


    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new_speed):
        self.__speed = new_speed

    def clock(self:float)-> float:
        """ Displaying speed
        """
        print(self.__speed)

    def increase_speeds(self: float)-> Union[float, str]:
        """ Increases speed by 5
        """
        if self.__speed >= 0:
            print(self.__speed+5)
        else:
            print('Speed 0')

    def decrease_speed(self(self: float)-> Union[float, str]:
        """ Decreases speed by 5
        """
        if self.__speed > 4:
            print(self.__speed-5)
        else:
            print('Speed 0')

    def stop(self: float)-> Union[float, str]:
        """ Reset speed to 0
        """
        if self.__speed != 0:
            print(self.__speed == 0)
        else:
            print('You go')

    def reversal_car(self: float)-> Union[float, str]:
        """ Speed sign change
        """
        if self.__speed != 0:
            print(self.__speed * -1 )
        else:
            print('You stop')

def main():
    car_1 = Car('BMW','560', 2020, 120)
    print(car_1.increase_speeds())

if __name__=='__main__':
    main()
