#US6
Feature: Visa favoritböcker
    För att kunna hålla koll på mina favoritmarkerade böcker
    som användare
    vill jag kunna se dem i en separat vyn

    Background:
        Given att användaren befinner sig i "Katalog"-vyn

    Scenario: Visa tom favoritlista
        And att det inte finns några böcker markerade som favoriter
        When användaren går till "Mina böcker"-vyn
        Then ska favoritlistan vara tom
        And texten "När du valt, kommer dina favoritböcker att visas här." visas

    Scenario: Favoritmarkerad bok visas under "Mina böcker"-vyn
		And boken "Min katt är min chef" finns tillagd i katalogen
		And att boken "Min katt är min chef" är markerad som favorit
		When användaren går till "Mina böcker"-vyn
		Then ska boken "Min katt är min chef" visas i favoritlistan


    Scenario Outline: Visa favoritlista med tre böcker
        And att boken "<title1>" är markerad som favorit
        And att boken "<title2>" är markerad som favorit
        And att boken "<title3>" är markerad som favorit
        When användaren går till "Mina böcker"-vyn
        Then ska användaren se en numrerad lista med de tre böckerna

        Examples:
            | title1                    | title2                                    | title3                    |
            | Min katt är min chef      | 100 sätt att undvika måndagar             | Jag trodde det var tisdag |
			| Jag trodde det var tisdag | Gräv där du står – och hitta en pizzameny | Kaffekokaren som visste för mycket|

    Scenario: Ordning på favoritböckerna följer ordningen i katalogen
        And katalogen visar böcker i följande ordning:
            | title                         |
            | Min katt är min chef          |
            | 100 sätt att undvika måndagar |
            | Jag trodde det var tisdag     |
        When användaren markerar boken "Min katt är min chef" som favorit
        And användaren markerar boken "Jag trodde det var tisdag" som favorit
        And användaren markerar boken "100 sätt att undvika måndagar" som favorit
        And användaren går till "Mina böcker"-vyn
        Then ska favoritlistans böcker visas i katalogens ordning

    Scenario: Favoritordningen uppdateras vid tillägg av mellanliggande böcker
        And katalogen visar böcker i följande ordning:
            | title                                                 |
            | Hur man tappar bort sin TV-fjärr 10 gånger om dagen   |
            | Min katt är min chef                                  |
            | 100 sätt att undvika måndagar                         |
            | Jag trodde det var tisdag                             | 
        And användaren har markerat följande böcker som favoriter:
            | title                                                 |
            | Hur man tappar bort sin TV-fjärr 10 gånger om dagen   |
            | 100 sätt att undvika måndagar                         |
            | Jag trodde det var tisdag                             |
        When användaren markerar boken "Min katt är min chef" som favorit
        And användaren går till "Mina böcker"-vyn
        Then ska favoritlistans böcker visas i katalogens ordning

