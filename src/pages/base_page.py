#Använd page-files för att abstrahera UI-interaktionen/användarinteraktionen

class BasePage:
    base_url = "https://tap-vt25-testverktyg.github.io/exam--reading-list/"

    def __init__(self, page):
        self.page = page 

    def goto(self, path="/"):
        self.page.goto(self.base_url + path)
