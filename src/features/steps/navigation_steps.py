from behave import given, when, then
from pages.navigation_page import NavigationPage
from playwright.sync_api import expect


@given(u'att användaren inte har webbsidan öppen')
def no_page_open(context):
    #Säkerhetsställer att ingen sida är öppnad än
    context.page.goto("about:blank")


@when(u'användaren surfar till webbsidan')
def user_goto_website(context):
    #Initiera Page object
    context.nav = NavigationPage(context.page)
    context.nav.open()


@then(u'ska vyn "{targetview}" visas')
def check_view(context, targetview):
    #Verifierar att rätt vy visas
    if targetview == "Katalog":
        locator = context.nav.get_catalogue_view()
    elif targetview == "Lägg till bok":
        locator = context.nav.get_add_book_view()
    elif targetview == "Mina böcker":
        locator = context.nav.get_favourites_view()
    else:
        raise Exception(f"Okänd vy: {targetview}")
    expect(locator).to_be_visible()


@then(u'knappen "{navbutton}" ska vara inaktiv (disabled)')
def show_navbutton_disabled(context, navbutton):
    #Verifierar att rätt knapp har rätt status
    if navbutton == "Katalog":
        locator = context.nav.get_catalogue_button()
    elif navbutton == "Lägg till bok":
        locator = context.nav.get_add_book_button()
    elif navbutton == "Mina böcker":
        locator = context.nav.get_favourites_button()
    else:
        raise Exception(f"Okänd knapp: {navbutton}")
    expect(locator).to_be_disabled()


@then(u'knappen "{navbutton}" ska vara aktiverad (enabled)')
def show_navbutton_enabled(context, navbutton):
    #Verifierar att rätt knapp har rätt status
    if navbutton == "Katalog":
        locator = context.nav.get_catalogue_button()
    elif navbutton == "Lägg till bok":
        locator = context.nav.get_add_book_button()
    elif navbutton == "Mina böcker":
        locator = context.nav.get_favourites_button()
    else:
        raise Exception(f"Okänd knapp: {navbutton}")
    expect(locator).to_be_enabled()


@then(u'välkomsttext och bild ska visas i headern')
def header_img_and_text_visible(context):
    expect(context.nav.get_header_image()).to_be_visible()
    expect(context.nav.get_header_text()).to_be_visible()


@given(u'att användaren befinner sig i vyn "{startview}"')
def user_is_on_startview(context, startview):
    context.nav = NavigationPage(context.page)
    context.nav.open()

    #Går till rätt vy 
    if startview == "Katalog":
        pass
    elif startview == "Lägg till bok":
        context.nav.click_add_book()
    elif startview == "Mina böcker":
        context.nav.click_favourites()
    else:
        raise Exception(f"Okänd vy: {startview}")


@when(u'användaren klickar på knappen "{navbutton}"')
def click_nav_button(context, navbutton):

    #Klickar på navigationsknapparna
    if navbutton == "Katalog":
        context.nav.click_catalogue()
    elif navbutton == "Lägg till bok":
        context.nav.click_add_book()
    elif navbutton == "Mina böcker":
        context.nav.click_favourites()
    else:
        raise Exception(f"Okänd knapp: {navbutton}")


@then(u'de andra navigeringsknapparna ska vara aktiva (enabled)')
def other_navbuttons_enabled(context):
    buttons = [
        context.nav.get_catalogue_button(),
        context.nav.get_add_book_button(),
        context.nav.get_favourites_button(),
    ]
    #Hittar den första inaktiva knappen
    current_button = next(btn for btn in buttons if not btn.is_enabled())
    #Skapar lista av de andra knapparna
    other_buttons = [btn for btn in buttons if btn != current_button]
    #Verifierar antal aktiva knappar
    assert len(other_buttons) == 2
    for button in other_buttons:
        expect(button).to_be_enabled()

