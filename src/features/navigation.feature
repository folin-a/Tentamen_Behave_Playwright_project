#US1
Feature: Navigering mellan olika vyer
    För att snabbt kunna ta mig till webbsidans olika vyer
    som användare
    vill jag kunna navigera mellan Katalog-, Lägg till- och Mina böcker-vyerna

    Scenario: Visa katalogvyn som startvy
    Given att användaren inte har webbsidan öppen
    When användaren surfar till webbsidan
    Then ska vyn "Katalog" visas
    And knappen "Katalog" ska vara inaktiv (disabled)
    And knappen "Lägg till bok" ska vara aktiverad (enabled)
    And knappen "Mina böcker" ska vara aktiverad (enabled)
    And välkomsttext och bild ska visas i headern

    Scenario Outline: Navigera mellan vyer
    Given att användaren befinner sig i vyn "<startview>"
    When användaren klickar på knappen "<navbutton>"
    Then ska vyn "<targetview>" visas
    And knappen "<navbutton>" ska vara inaktiv (disabled)
    And de andra navigeringsknapparna ska vara aktiva (enabled)

    Examples:
    | startview     | navbutton     | targetview    | 
    | Katalog       | Lägg till bok | Lägg till bok |
    | Katalog       | Mina böcker   | Mina böcker   |
    | Lägg till bok | Katalog       | Katalog       |
    | Lägg till bok | Mina böcker   | Mina böcker   |
    | Mina böcker   | Katalog       | Katalog       |
    | Mina böcker   | Lägg till bok | Lägg till bok |


