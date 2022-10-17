from .base_page import BasePage  # из файла base_page.py импортируем класс BasePage


class MainPage(BasePage):  # MainPage является наследником класса BasePage. MainPage - это главная страница
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        # метод __init__ вызывается при создании объекта. Конструктор выше с ключевым словом super на самом деле только
        # вызывает конструктор класса предка и передает ему все те аргументы, которые мы передали в конструктор MainPage
        # вместо строки super можно написать: pass
