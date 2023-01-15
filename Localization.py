class Localization:
    def __init__(self, language):
        self.language = language
        self.translations = {}

    def add_translations(self, translations):
        self.translations.update(translations)

    def get_translation(self, key):
        return self.translations.get(key, key)

class Robot:
    def __init__(self, name, inventory_number, company_name, localization):
        self.name = name
        self.inventory_number = inventory_number
        self.functions = []
        self.company_name = company_name
        self.localization = localization

    def add_function(self, function):
        self.functions.append(function)

    def list_functions(self):
        return [self.localization.get_translation(func) for func in self.functions]

    def change_name(self, new_name):
        self.name = new_name

localization_en = Localization("en")
localization_en.add_translations({"build_house": "Build House", "build_shed": "Build Shed", "add_floor": "Add Floor", "remove_top_floor": "Remove Top Floor"})

localization_ru = Localization("ru")
localization_ru.add_translations({"build_house": "Построить Дом", "build_shed": "Построить Сарай", "add_floor": "Добавить Этаж", "remove_top_floor": "Удалить Верхний Этаж"})

robot = Robot("V", "AA001221-56", "Primary_school", localization_en)
robot.add_function("build_house")
robot.add_function("build_shed")

robot.change_name("VITA")
robot.company_name = "OOO Koshmarik"
robot.add_function("add_floor")
robot.add_function("remove_top_floor")

robot.localization = localization_ru
print(robot.list_functions()) # prints ['Построить Дом', 'Построить Сарай', 'Добавить Этаж', 'Удалить Верхний Этаж']