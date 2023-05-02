## Sointu-ohjelma


-*Tällä hetkellä*- sovelluksella voidaan tarkistaa muodostaako käyttäjän antamat 3 säveltä joko duuri- tai mollisoinnun. Sovellus osaa myös kertoa mitkä kolme (3) säveltä käyttäjän anta sointu pitää sisällään. Sovellus myös tallentaa uusia kappaleita /data/songs.csv tiedostoon. Siellä on pari ennalta tallennettua kappaletta, mutta sinne voi myös sovelluksen sisältä tallentaa lisää kappaleita. Tulevista laajennuksista löytyy lisää vaatimusmäärittelystä.

-Ohjelman käynnistyttyä se kysyy mitä haluat tehdä - [1] haluatko antaa soinnun, jonka jälkeen sovellus kertoo mistä sävelistä se koostuu (esimerkki sointu voisi olla vaikka C duuri eli major), [2] antaa sovellukselle 3 säveltä (säveliä ovat A, A#, B, C, C#, D, D#, E, F, F#, G, G#) ja sovellus päättelee, muodostavatko nämä mitään sointua, [3] printata kaikki /songs.csv tiedostossa olevat kappaleet, [4] tallentaa /songs.csv tiedostoon uuden kappaleen vai [5] tutkia mitkä soinnut sopivat antamasi duurisoinnun kanssa.

-Huom ohjelmalla on graafinenkäyttöliittymä mutta sen kaikki tulostukset tulevat komentoriville

# Release

[Release](https://github.com/Aaltonenn/ot-harjoitustyo/releases/tag/viikko5newest)


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
- testien kattavuus - poetry run invoke coverage-report
- pylint testaut . poetry run invoke lint
