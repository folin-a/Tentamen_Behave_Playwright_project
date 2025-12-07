#US5
Feature: Avmarkera bok som favorit
    För att ta bort böcker som jag inte längre är intresserad av
    som användare
    vill jag avmarkera böcker från katalog-vyn

    Background:
    Given att användaren befinner sig i "Katalog"-vyn

	Scenario: Avmarkera en favoritbok
		And att boken "Min katt är min chef" är markerad som favorit
		When användaren klickar på hjärtat på bokraden för "Min katt är min chef"
		Then ska boken "Min katt är min chef" inte vara markerad som favorit

	Scenario: Avmarkerad bok syns inte längre i favoritlistan
		And att boken "Min katt är min chef" är markerad som favorit
    	When användaren har avmarkerat "Min katt är min chef"
    	And användaren går till "Mina böcker"-vyn
    	Then ska boken "Min katt är min chef" inte visas i favoritlistan

  	Scenario: Avmarkera en bok bland flera favoritmarkerade böcker
    	And att boken "Min katt är min chef" är markerad som favorit
    	And att boken "Jag trodde det var tisdag" är markerad som favorit
   	 	When användaren klickar på hjärtat på bokraden för "Min katt är min chef"
    	And användaren går till "Mina böcker"-vyn
    	Then ska boken "Min katt är min chef" inte visas i favoritlistan
    	And ska boken "Jag trodde det var tisdag" visas i favoritlistan
