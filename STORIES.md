# User stories för Läslistans webbsidan

## US1: Navigering mellan olika vyer
Som en användare <br>
vill jag kunna navigera mellan katalog-, lägg till- och mina böcker-vyn <br>
så att jag snabbt kan växla mellan webbsidans funktioner

### AK1:
- Det ska finnas tre navigeringsknappar: "Katalog", "Lägg till bok" och "Mina böcker"
- Den aktiva vyn ska markeras genom att motsvarade knapp är inaktiverad (disabled)
- När användaren klickar på en navigeringsknapp ska rätt vy visas
- Katalog-vyn är förinställd när användaren surfar till webbsidan
- Välkomsttext och bild ska visas i headern oavsett vilken vy som är aktiv

## US2: Se tillgängliga titlar i katalogen
Som en användare <br>
vill jag se en välkomstsida med befintliga böcker <br>
så att jag kan få en överblick över tillgängliga titlar<br>

### AK2:
- Det ska finnas 7st fördefinierade böcker
- Varje bok ska visas i formatet "titel", författare
- Katalogknappen ska vara den aktiva (disabled) när denna vyn är aktiv

## US3: Lägg till ny bok i katalogen
Som en användare<br>
vill jag kunna lägga till en bok med boktitel och författare<br>
så att jag kan utöka läslistans katalog med böcker.

### AK3:
- Det ska finnas en tydlig navigeringslänk till "Lägg till bok"
- När användaren klickar på navigeringsknappen "Lägg till bok" ska det visas ett formulär för att lägga till böcker
- Formulären ska ha fält för titel och författare
- När användaren fyller i en titel och en författare och sparar boken ska den läggas till längst ned i katalogen
- "Lägg till ny bok"-knappen ska vara inaktiverad(disabled) fram tills fält för både titel och författare är ifyllda
- Efter att en bok har lagts till ska formuläret tömmas automatiskt
- Ny bok ska lägga sig sista i kataloglistan i den ordning de skapas.
- Kataloglistan uppdateras direkt utan omladdning

## US4: Favoritmarkering av böcker
Som en användare <br>
vill jag kunna markera boktitlar som favoriter samt se mina favoriter separat<br>
så att jag kan hålla koll på de böcker jag är intresserad av<br>

### AK4:
- När användaren hovrar med muspekaren över en bokrad utan favoritmarkering ska ett svagt hjärta visas
- När användaren klickar på bokrad utan favoritmarkering markeras den som favorit 
- När en bok är markerad som favorit så visas ett ifyllt hjärta framför boktiteln
- När bokraden är markerad med ett hjärta så är boken sparad som favorit
- Hjärtmarkerade/Favoritmarkerade böcker ska visas under vyn "Mina böcker"
- Favoritstatus ska behållas när användaren navigerar mellan vyer

## US5: Avmarkera favoritböcker
Som en användare <br>
vill jag kunna avmarkera boktitlar som favoriter <br>
så att jag kan ta bort böcker som jag inte längre är intresserad av.

### AK5:
- När användaren klickar på ett ifyllt hjärta ska favoriten avmarkeras
- Favorit-hjärtat ska tas bort framför boktiteln
- Den omarkerade boken ska försvinna från "Mina böcker" listan
- Boktiteln med författare ska finnas kvar under "Katalog"-vyn utan favoritmarkering

## US6: Visa favoritböcker
Som en användare <br>
vill jag att favoritmarkerade böcker ska behålla sin plats i favoriterna i den ordning de finns i katalogen <br>
så att jag kan favoritmarkera i vilken ordning jag vill men ändå få samma resultat i visningen.

### AK6:
- Det ska finnas en knapp i navigeringen som tar användaren till "Mina böcker"
- "Mina böcker"-knappen ska markeras som aktiv(disabled) när vyn visas
- När inga favoritmarkerade böcker finns ska sidan visa texten "När du valt, kommer dina favoritböcker visas här"
- Om användaren har favoritmarkerat böcker ska dessa visas i numrerad lista
- Favoritmarkerade böcker ska alltid visas i samma ordning som de har i katalogen, oavsett i vilken ordning användaren favoritmarkerade dem
- De favoritmarkerade böckerna ska visas med boktitel
