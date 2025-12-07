#Konfigurerar Playwright

from playwright.sync_api import sync_playwright

def before_all(context):
    #Sätter upp playwright före alla test
    context.play = sync_playwright().start()

def before_scenario(context, scenario):
    #Sätter upp en browser sida innan varje scenario
    context.browser = context.play.chromium.launch(headless=True)
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    #Stänger sidan och browsern
    context.page.close()
    context.browser.close()

def after_all(context):
    #Stoppar playwright
    context.play.stop()