
from behave import given, when, then
from playwright.sync_api import expect
from pages.catalogue_page import CataloguePage
from pages.navigation_page import NavigationPage
import re


@given(u'att användaren går till webbsidan')
def user_go_to_website(context):
    context.nav = NavigationPage(context.page)
    context.nav.open()
    context.cat = CataloguePage(context.page)


@when(u'katalog-vyn visas')
def show_catalogue_view(context):
    expect(context.nav.get_catalogue_view()).to_be_visible()


@then(u'ska användaren se en lista med 7st böcker')
def list_with_books_visible(context):
    #Hämtar alla böcker på sidan
    books = context.cat.get_all_books()
    #Verifierar antal av böcker
    expect(books).to_have_count(7)


@then(u'varje rad ska visa bokens titel och författare')
def show_title_and_author_per_row(context):
    books = context.cat.get_all_books()

    #Verifierar att varje bok har två delar
    for i in range(books.count()):
        expect(books.nth(i)).to_have_text(re.compile(r'".+", .+$'))


@then(u'"Katalog"-knappen är inaktiverad(disabled)')
def catalogue_button_inactive(context):
    locator = context.nav.get_catalogue_button()
    expect(locator).to_be_disabled()
