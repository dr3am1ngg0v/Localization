import os

os.system('cls')

class Robot:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.name = "V"
            cls.__instance.inventory_number = "AA001221-56"
            cls.__instance.operating_company = None
            cls.__instance.functions = []
            cls.__instance.language = "English"
        return cls.__instance

    def set_name(self, new_name):
        self.name = new_name

    def set_operating_company(self, new_operating_company):
        self.operating_company = new_operating_company

    def set_language(self, new_language):
        self.language = new_language

    def get_info(self):
        if self.language == "English":
            return f"Name: {self.name}, Inventory Number: {self.inventory_number}, Operating Company: {self.operating_company}, Functions: {self.functions}"
        elif self.language == "Russian":
            return f"Имя: {self.name}, Инвентарный номер: {self.inventory_number}, Операционная компания: {self.operating_company}, Функции: {self.functions}"
        else:
            return f"Invalid Language. Try another."

class RobotDecorator:
    def __init__(self, robot):
        self.robot = robot

    def build_house(self):
        self.robot.functions.append("build_house")
        if self.robot.language == "Russian":
            self.robot.functions[-1] = "построить дом"

    def build_shed(self):
        self.robot.functions.append("build_shed")
        if self.robot.language == "Russian":
            self.robot.functions[-1] = "построить сарай"

    def add_floor(self):
        self.robot.functions.append("add_floor")
        if self.robot.language == "Russian":
            self.robot.functions[-1] = "добавить этаж"

    def remove_floor(self):
        self.robot.functions.append("remove_floor")
        if self.robot.language == "Russian":
            self.robot.functions[-1] = "снести этаж"

if __name__ == "__main__":
    robot = Robot()
    robot_decorator = RobotDecorator(robot)
    print("1.", robot.get_info())
    # Name: V, Inventory Number: AA001221-56, Operating Company: None, Functions: []

    robot_decorator.build_house()
    robot_decorator.build_shed()
    print("2.", robot.get_info())
    # Name: V, Inventory Number: AA001221-56, Operating Company: None, Functions: ['build_house', 'build_shed']

    robot.set_name("VITA")
    robot.set_operating_company("OOO Koshmarik")
    print("3.", robot.get_info())
    # Name: VITA, Inventory Number: AA001221-56, Operating Company: OOO Koshmarik, Functions: ['build_house', 'build_shed']

    robot_decorator.add_floor()
    robot_decorator.remove_floor()
    print("4.", robot.get_info())
    # Name: VITA, Inventory Number: AA001221-56, Operating Company: OOO Koshmarik, Functions: ['build_house', 'build_shed', 'add_floor', 'remove_floor']

    robot.set_name("Vitaliy")
    robot.set_operating_company("OOO Koshmarik")
    print("5.", robot.get_info())
    # Name: Vitaliy, Inventory Number: AA001221-56, Operating Company: OOO Koshmarik, Functions: ['build_house', 'build_shed', 'add_floor', 'remove_floor']