from pages.base_page import BasePage

class AddBookPage(BasePage):

    TITLE_INPUT ='[data-testid="add-input-title"]'
    AUTHOR_INPUT ='[data-testid="add-input-author"]'
    SUBMIT_BUTTON ='[data-testid="add-submit"]' 

    def clear_title(self):
        self.page.locator(self.TITLE_INPUT).fill("")
    
    def click_submit(self):
        self.page.locator(self.SUBMIT_BUTTON).click()

    def submit_button(self):
        return self.page.locator(self.SUBMIT_BUTTON)
    
    def title_input(self):
        return self.page.locator(self.TITLE_INPUT)
    
    def author_input(self):
        return self.page.locator(self.AUTHOR_INPUT)
    
    def fill_title(self, title):
        self.title_input().fill(title)

    def fill_author(self, author):
        self.author_input().fill(author)
