class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self,owner,model,color,engine_power):
        self.owner = owner #владелец
        self.__model = model #модель транспорта
        self.__engine_power = engine_power #мощность двигателя
        self.__color = color #цвет

    def get_model(self):
        return f"Модель: {self.__model}" # возвращает строку: "Модель: <название модели транспорта>"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}" #возвращает строку: "Мощность двигателя: <мощность>"

    def get_color(self):
        return f"Цвет: {self.__color}" #возвращает строку: "Цвет: <цвет транспорта>"

    def print_info(self): # результаты методов
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in (color.lower() for color in Vehicle.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5 #в седан может поместиться только 5 пассажиров

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

vehicle2 = Sedan('Denis', 'Nissan Skyline', 'white', 1000)
# Изначальные свойства
vehicle1.print_info()
vehicle2.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle2.set_color('Brown')
vehicle2.set_color('RED')
vehicle2.owner = 'Maks'

# Проверяем что поменялось
vehicle1.print_info()
vehicle2.print_info()