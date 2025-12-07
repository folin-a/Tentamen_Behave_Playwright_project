
from pages.base_page import BasePage

class NavigationPage(BasePage):

    CATALOGUE_VIEW = ".catalog"
    ADD_BOOK_VIEW = ".form"
    FAVOURITES_VIEW = ".favorites"
    CATALOGUE_BUTTON = '[data-testid="catalog"]'
    ADD_BOOK_BUTTON = '[data-testid="add-book"]'
    FAVOURITES_BUTTON = '[data-testid="favorites"]'
    HEADER_TEXT = 'header h1'
    HEADER_IMG = 'header img'

    def open(self):
        #Öppnar roten på webbsidan
        self.goto("/")
    
    def click_catalogue(self):
        self.page.locator(self.CATALOGUE_BUTTON).click()
    
    def click_add_book(self):
        self.page.locator(self.ADD_BOOK_BUTTON).click()
    
    def click_favourites(self):
        self.page.locator(self.FAVOURITES_BUTTON).click()

    def get_catalogue_view(self):
        return self.page.locator(self.CATALOGUE_VIEW)
    
    def get_add_book_view(self):
        return self.page.locator(self.ADD_BOOK_VIEW)
    
    def get_favourites_view(self):
        return self.page.locator(self.FAVOURITES_VIEW)
    
    def get_catalogue_button(self):
        return self.page.locator(self.CATALOGUE_BUTTON)

    def get_add_book_button(self):
        return self.page.locator(self.ADD_BOOK_BUTTON)

    def get_favourites_button(self):
        return self.page.locator(self.FAVOURITES_BUTTON)

    def get_header_text(self):
        return self.page.locator(self.HEADER_TEXT)
    
    def get_header_image(self):
        return self.page.locator(self.HEADER_IMG)

