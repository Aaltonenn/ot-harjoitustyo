## Sointu-ohjelma

-*Tällä hetkellä*- sovelluksella voidaan tarkistaa muodostaako käyttäjän antamat 3 säveltä joko duuri- tai mollisoinnun. Tulevista laajennuksista löytyy lisää vaatimusmäärittelystä. 
Ohjelma pyytää antamaan 3 säveltä (säveliä ovat A, A#, B, C, C#, D, D#, E, F, F#, G, G#). Tämän jälkeen ohjelma kertoo tuottaako kyseiset 3 säveltä duuri- tai mollisoinnun. (Esimerkki duuri soinnusta on C, E, G ja esimerkki mollisoinnusta on B, D, F#). Ohjelma voidaan pysäyttää syöttämällä säveliksi numeron 0

# Dokumentaatio

[vaatimusmäärittely](https://github.com/Aaltonenn/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
\
[työaikakirjanpito](https://github.com/Aaltonenn/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
\
[changelog](https://github.com/Aaltonenn/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
\
[arkkitehtuuri](https://github.com/Aaltonenn/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

# Asennusohjeet

Ohjelmaa pyörittääksesi tulee sinun asentaa poetry invoke


# komentorivitoiminnot
- suorita ohjelma - poetry run invoke start
- ohjelman testaus - poetry run invoke test
- testien kattavuus - poetry run invoke coverage -report
- pylint testaut . poetry run invoke lint
