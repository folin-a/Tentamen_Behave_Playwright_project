
from behave import given, when, then
from playwright.sync_api import expect

from pages.navigation_page import NavigationPage
from pages.favourites_page import FavouritesPage
from pages.catalogue_page import CataloguePage

@given(u'att användaren befinner sig i "Katalog"-vyn')
def user_on_catalogue_view(context):
    context.nav = NavigationPage(context.page)
    context.nav.open()

    # Om katalogvyn inte är aktiv, gå till katalogvyn
    if context.nav.get_catalogue_button().is_enabled():
        context.nav.click_catalogue()

    context.cat = CataloguePage(context.page)
    context.fav = FavouritesPage(context.page)


@given(u'att boken "{title}" inte är markerad som favorit')
def book_not_selected_favourite(context, title):
    heart = context.cat.get_star_by_title(title)
    # Säkerhetsställer att boken inte är markerad som favorit och tar bort favoritmarkeringen om den finns
    toggle_class = heart.get_attribute("class") or ""
    if "selected" in toggle_class:
        heart.click()
    expect(heart).not_to_contain_class("selected")


@when(u'användaren hovrar över bokraden med titeln "{title}"')
def hover_on_book_row(context, title):
    # Hämtar en specifik bok och hovrar på bokraden
    book = context.cat.get_all_books().filter(has_text=title).first
    book.hover()


@then(u'ska ett svagt hjärta visas för boken "{title}"')
def weak_heart_displayed(context, title):
    heart = context.cat.get_star_by_title(title)
    # Kontrollerar synlighet med timeout för CSS animation
    expect(heart).to_be_visible()

    #Väntar kort för att garanterar att animationen ska starta/slutföras
    context.page.wait_for_timeout(500)

    # Element med opacitet 0 antas vara synliga, vi kontrollerar om det finns opacitet större än 0
    opacity = heart.evaluate('el => getComputedStyle(el).opacity')
    assert float(opacity) > 0
    expect(heart).not_to_contain_class("selected")


@given(u'boken "{title}" finns tillagd i katalogen')
def book_is_in_catalogue(context, title):
    #Kollar om boken finns i katalogen
    books = context.cat.get_all_books()
    expect(books.filter(has_text=title)).to_have_count(1)
    

@when(u'användaren klickar på hjärtat på bokraden för "{title}"')
def user_click_on_book_row(context, title):
    heart = context.cat.get_star_by_title(title)
    heart.click()


@then(u'ska bokraden "{title}" markeras med ett ifyllt hjärta')
def filled_heart_displayed(context, title):
    heart = context.cat.get_star_by_title(title)
    expect(heart).to_contain_class("selected")
    

@given(u'att boken "{title}" är markerad som favorit')
def book_selected_favourite(context, title):
    heart = context.cat.get_star_by_title(title)
    # Om boken inte är markerad som favorit, markera den
    toggle_class = heart.get_attribute("class") or ""
    if "selected" not in toggle_class:
        heart.click()
    expect(heart).to_contain_class("selected")


@when(u'användaren går till "Mina böcker"-vyn')
def go_to_my_books_view(context):
    context.nav.click_favourites()


@then(u'ska boken "{title}" visas i favoritlistan')
def book_shown_in_favourite_list(context, title):
    fav_books = context.fav.get_favourite_books()
    expect(fav_books.filter(has_text=title)).to_have_count(1)


@given(u'följande boktitlar finns tillagda i katalogen:')
def catalogue_books_displayed(context):
    books = context.cat.get_all_books()
    # Kollar att böckerna i tabellen finns i katalogen
    for row in context.table:
        title = row['title']
        expect(books.filter(has_text=title)).to_have_count(1)
    context.favourite_books = context.table
    

@when(u'användaren markerar boken "{title}" som favorit')
def user_select_book_as_favourite(context, title):
    heart = context.cat.get_star_by_title(title)
    heart.click()

@when(u'användaren klickar på knappen "Mina böcker"')
def user_click_on_my_books_view(context):
    context.nav.click_favourites()


@then(u'böckerna ska visas med titel i "Mina böcker"-vyn')
def books_shown_with_title_in_favourites(context):
    fav_books = context.fav.get_favourite_books()

    # Verifierar att antalet favoritböcker är samma som tidigare tillagd
    num_favourite_books = len(context.favourite_books.rows)
    expect(fav_books).to_have_count(num_favourite_books)

    # Verifierar att de markerade böckerna finns som favoriter
    for row in context.favourite_books:
        title = row['title']
        expect(fav_books.filter(has_text=title)).to_have_count(1)


@when(u'användaren markerar boken "{title}" som favorit igen')
def select_book_as_favourite_again(context, title):
    heart = context.cat.get_star_by_title(title)
    heart.click()


@then(u'ska boken "{title}" inte vara markerad som favorit')
def book_not_marked_as_favourite(context, title):
    heart = context.cat.get_star_by_title(title)
    expect(heart).not_to_contain_class("selected")


@when(u'användaren går till "Lägg till bok"-vyn')
def user_go_to_add_book_view(context):
    context.nav.click_add_book()


@when(u'användaren går tillbaka till "Katalog"-vyn')
def user_go_to_catalogue_view(context):
    context.nav.click_catalogue()


@then(u'ska boken "{title}" fortfarande vara markerad som favorit')
def book_still_marked_as_favourite(context, title):
    heart = context.cat.get_star_by_title(title)
    expect(heart).to_contain_class("selected")


@when(u'användaren har avmarkerat "{title}"')
def user_deselect_book_as_favourite(context, title):
    heart = context.cat.get_star_by_title(title)
    # Om boken är markerad som favorit, klicka på favoritikonen
    toggle_class = heart.get_attribute("class") or ""
    if "selected" in toggle_class:
        heart.click()


@then(u'ska boken "{title}" inte visas i favoritlistan')
def book_not_visible_in_favourites_list(context, title):
    favlist_books = context.fav.get_favourite_books()
    expect(favlist_books.filter(has_text=title)).to_have_count(0)


@given(u'att det inte finns några böcker markerade som favoriter')
def no_books_marked_as_favourites(context):
    selected_books = context.cat.get_favourites()
    expect(selected_books).to_have_count(0)


@then(u'ska favoritlistan vara tom')
def favourite_list_empty(context):
    favlist_books = context.fav.get_favourite_books()
    expect(favlist_books).to_have_count(0)


@then(u'texten "{text}" visas')
def show_no_fav_text(context, text):
    expect(context.page.locator(".favorites").filter(has_text = text)).to_be_visible()


@then(u'ska användaren se en numrerad lista med de tre böckerna')
def show_numbered_list(context):
    # OL elementet finns alltid, vi verifierar därför bara att det finns tre böcker
    favlist_books = context.fav.get_favourite_books()
    expect(favlist_books).to_have_count(3)


@given(u'katalogen visar böcker i följande ordning:')
def catalogue_show_books_in_order(context):
    context.expected_order = [row["title"] for row in context.table]


@given(u'användaren har markerat följande böcker som favoriter:')
def multiple_book_marked_favourite(context):
    for row in context.table:
        context.cat.get_star_by_title(row['title']).click()


@then(u'ska favoritlistans böcker visas i katalogens ordning')
def verify_favbooks_in_order(context):

    expected_titles = context.expected_order
    favlist_books = context.fav.get_favourite_books()

    # Verifierar att antal favoritböcker matchar förväntat värde
    expect(favlist_books).to_have_count(len(expected_titles))

    # Verifierar att böckerna är i korrekt ordning
    for index, expected_title in enumerate(expected_titles):
        expect(favlist_books.nth(index)).to_have_text(expected_title)
