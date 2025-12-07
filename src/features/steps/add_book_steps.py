
from behave import given, when, then
from playwright.sync_api import expect
from pages.navigation_page import NavigationPage
from pages.add_book_page import AddBookPage
from pages.catalogue_page import CataloguePage

@given(u'användaren är på "Lägg till bok"-vyn')
def user_on_add_books_page(context):
    context.nav = NavigationPage(context.page)
    context.nav.open()
    context.nav.click_add_book()
    context.add = AddBookPage(context.page)


@when(u'användaren fyller i titel "{title}"')
def user_input_title(context, title):
    if title == "<ingen>":
        context.add.fill_title("")
        context.last_title = ""
    else:
        context.add.fill_title(title)
        #Används för att visa rätt i katalogvyn
        context.last_title = title


@when(u'användaren fyller i författare "{author}"')
def user_input_author(context, author):
    if author == "<ingen>":
        context.add.fill_author("")
        #Används för att visa rätt i katalogvyn
        context.last_author = ""
    else:
        context.add.fill_author(author)
        #Används för att visa rätt i katalogvyn
        context.last_author = author


@then(u'ska "Lägg till ny bok" knappen vara aktiverad')
def submit_button_check_enabled(context):
    expect(context.add.submit_button()).to_be_enabled()


@when(u'klickar på knappen "Lägg till ny bok"')
def click_submit_button(context):
    context.add.click_submit()


@then(u'ska formuläret tömmas')
def form_cleared(context):
    expect(context.add.title_input()).to_be_empty()
    expect(context.add.author_input()).to_be_empty()


@then(u'ska "Lägg till ny bok" knappen vara inaktiv')
def submit_button_disabled(context):
    expect(context.add.submit_button()).to_be_disabled()


@then(u'ska boken visas under "Katalog"-vyn')
def book_shown_in_catalogue_view(context):
    context.nav.click_catalogue()

    catalogue = CataloguePage(context.page)
    books = catalogue.get_all_books()

    expected_text = f'"{context.last_title}", {context.last_author}'
    
    matching_book = books.filter(has_text=expected_text)

    expect(matching_book).to_have_count(1)


@given(u'användaren har fyllt i titel, "{title}"')                                       
def user_has_input_title(context, title):
    context.add.fill_title(title)


@given(u'användaren har fyllt i författare, "{author}"')
def user_has_input_author(context, author):
    context.add.fill_author(author)
        

@given(u'"Lägg till ny bok" knappen är aktiv')
def submit_button_is_enabled(context):
    expect(context.add.submit_button()).to_be_enabled()


@when(u'användaren tömmer titel-fältet')
def user_empty_title(context):
    context.add.clear_title()


@when(u'användaren lägger till titeln "{title}" med författare "{author}"')
def user_add_title_and_author(context, title, author):
    context.add.fill_title(title)
    context.add.fill_author(author)
    context.add.click_submit()


@when(u'användaren klickar på "Katalog"-knappen')
def user_click_catalogue_button(context):
    context.nav.click_catalogue()


@then(u'ska böckerna visas i den ordningen de lades till')
def show_books_in_added_order(context):
    catalogue = CataloguePage(context.page)
    books = catalogue.get_all_books()
    context.books = books

    #Räknar antal böcker på sidan
    count = books.count()
    assert count >=3 , "Det finns mindre än 3 böcker"

    #Verifierar att böckerna är i korrekt ordning
    expect(books.nth(count - 3)).to_contain_text('"Boken", Linda Ros')
    expect(books.nth(count - 2)).to_contain_text('"Boken 2", Linda Ros')
    expect(books.nth(count - 1)).to_contain_text('"Boken 3", Linda Ros')


@then(u'de ska ligga längst ned i listan')
def added_books_last_on_list(context):
    books = context.books

    #Räknar antal böcker på sidan
    count = books.count()
    assert count >=3 , "Det finns mindre än 3st böcker"

    #Verifiera att boken är sist på listan
    expect(books.last).to_contain_text('"Boken 3", Linda Ros')
