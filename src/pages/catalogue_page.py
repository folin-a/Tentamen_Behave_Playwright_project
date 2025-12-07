

from pages.base_page import BasePage

class CataloguePage(BasePage):

    BOOK_ITEMS = '.catalog .book'
    FAV_ICON = '[data-testid="star-{}"]'
    SELECTED_HEARTS = '.star.selected'


    def get_all_books(self):
        return self.page.locator(self.BOOK_ITEMS)
    
    def get_star_by_title(self, title):
        #Titel används i data-testid="star-TITEL"
        return self.page.locator(self.FAV_ICON.format(title))
    
    def get_favourites(self):
        return self.page.locator(self.SELECTED_HEARTS)
