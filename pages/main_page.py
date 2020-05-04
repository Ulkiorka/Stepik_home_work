from .base_page import BasePage


class MainPage(BasePage):
    """Заглушка для пустого класса из которого все методы перенесли в другие"""
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)