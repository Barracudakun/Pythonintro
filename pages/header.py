from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, '')
    SEARCH_ICON = (By. ID, '')

    def input_search(self):
        self.input_text('', *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_FIELD)


