3.4
- Luotu sointujentunnistus-osan alkurakenteet (services/service.py class Service), jotka tunnistaa onko kyseessä duuri- tai mollisointu.
- tasks.py tiedostoon luotu start, test ja coverage komennot.
- Sointujen tunnistukselle luotu oma käyttöliittymä determine_chord.py.
- Luotu testit tarkkailemaan, että service toimii - testien coverage ei ole vielä 100%.

15.4
- testikattavuutta ja testien mielekkyyttä parannettu
- koodia paranneltu huomattavasti pylint ystävällisemmäksi
- nyt chord_determination osaa myös sanoa mikä sointu on kyseessä (esim C major) (ennen se osasi vain sanoa että major)
- invoke lint lisätty
- ui.py tehty kattavammaksi ja selkeämmäksi
- chord_determination tunnistaa nyt myös lowercase kirjaimet sekä alennetut sävelet esim C#=Db
- luotu GiveNotes luokka, joka kertoo mistä sävelistä käyttäjän antama sointu koostuu.
- GiveNotesille luotu oma käyttöliittymä ja kaikki tarvittavat testit