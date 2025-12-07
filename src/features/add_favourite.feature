#US4
Feature: Lägg till bok som favorit
	För att kunna spara de boktitlar jag är intresserad av
	som en användare
	vill jag kunna markera böcker som favoriter

	Background:
	Given att användaren befinner sig i "Katalog"-vyn

	Scenario: Visa hjärt-ikon vid hover
		And att boken "Min katt är min chef" inte är markerad som favorit
		When användaren hovrar över bokraden med titeln "Min katt är min chef"
		Then ska ett svagt hjärta visas för boken "Min katt är min chef"

	Scenario: Markera en bok som favorit
		And boken "Min katt är min chef" finns tillagd i katalogen
    	When användaren klickar på hjärtat på bokraden för "Min katt är min chef"
    	Then ska bokraden "Min katt är min chef" markeras med ett ifyllt hjärta

	Scenario: Favoritmarkering är en toggle
		And att boken "Min katt är min chef" inte är markerad som favorit
		When användaren markerar boken "Min katt är min chef" som favorit
		And användaren markerar boken "Min katt är min chef" som favorit igen
		Then ska boken "Min katt är min chef" inte vara markerad som favorit

	Scenario: Favoritmarkering bevaras vid navigering
		And att boken "Min katt är min chef" är markerad som favorit
		When användaren går till "Lägg till bok"-vyn
		And användaren går tillbaka till "Katalog"-vyn
		Then ska boken "Min katt är min chef" fortfarande vara markerad som favorit