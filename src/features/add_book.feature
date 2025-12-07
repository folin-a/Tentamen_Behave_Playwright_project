#US3
Feature: Lägg till bok
    För att kunna utöka katalogen
    som en användare
    vill jag kunna lägga till nya böcker via ett formulär

    Background:
    Given användaren är på "Lägg till bok"-vyn

    Scenario: Lyckad tilläggning av ny bok
        When användaren fyller i titel "Min dag på torget"
        And användaren fyller i författare "Dag Skorsson"
        And klickar på knappen "Lägg till ny bok"
        Then ska boken visas under "Katalog"-vyn

    Scenario: Automatisk tömning av formulär
        When användaren fyller i titel "Boken"
        And användaren fyller i författare "Linda Ros"
        And klickar på knappen "Lägg till ny bok"
        Then ska formuläret tömmas
        And ska boken visas under "Katalog"-vyn

    Scenario Outline: Inaktiverad "lägg till"- knapp vid ofullständig inmatning
        When användaren fyller i titel "<title>"
        And användaren fyller i författare "<author>"
        Then ska "Lägg till ny bok" knappen vara inaktiv

        Examples:
            | title                 | author        | 
            | Min mamma och håret   | <ingen>       |
            | <ingen>               | Frans Hairdo  |

    Scenario: Inaktiverad "lägg till"-knapp vid manuell tömning av formulärsfält
        And användaren har fyllt i titel, "Boken"
        And användaren har fyllt i författare, "Linda Ros"
        And "Lägg till ny bok" knappen är aktiv
        When användaren tömmer titel-fältet
        Then ska "Lägg till ny bok" knappen vara inaktiv

    Scenario: Lägga till flera böcker efter varandra
        When användaren lägger till titeln "Boken" med författare "Linda Ros"
        And användaren lägger till titeln "Boken 2" med författare "Linda Ros"
        And användaren lägger till titeln "Boken 3" med författare "Linda Ros"
        And användaren klickar på "Katalog"-knappen
        Then ska böckerna visas i den ordningen de lades till
        And de ska ligga längst ned i listan