from pages.base_page import BasePage

class FavouritesPage(BasePage):

    FAV_LIST = '[data-testid="book-list"]'

    def get_favourite_books(self):
        return self.page.locator(f'{self.FAV_LIST} li')
    