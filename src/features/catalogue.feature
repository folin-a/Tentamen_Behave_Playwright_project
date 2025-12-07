Feature: Visa bokkatalog
    För att snabbt kunna få en överblick av böcker
    som användare
    vill jag på startsidan se katalogens lista över tillgängliga böcker
    
    Scenario: Visa 7st fördefinierade böcker i katalogen
        Given att användaren går till webbsidan
        When katalog-vyn visas
        Then ska användaren se en lista med 7st böcker
        And varje rad ska visa bokens titel och författare
        And "Katalog"-knappen är inaktiverad(disabled)
