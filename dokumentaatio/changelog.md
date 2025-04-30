## Viikko 3

- Käyttäjä voi avata html-tiedoston tai luoda uuden, muokata sitä ja tallentaa sen, source-muodossa
- Lisätty FileHandler luokka, joka vastaa tiedostojen käsittelystä
- Testattu, että tiedoston avaus toimii

## Viikko 4

- Aloitettu visuaalisen editorin rakentamista. Lisätty muutamat napit, jotka lisäävät html-tägejä tekstikenttään. Tässä vaiheessa tägit on vielä puhdasta htmlää eikä "WYSIWYG" tyyliä.
- Lisätty myös pikanäppäimet näitä varten (CTRL + b, i, u)
- Lisätty napit, jolla voi vaihtaa visual ja source muodon välillä
- Lisätty testit, että uusi tiedosto ja tiedoston tallentaminen toimii

## Viikko 5
- Lisätty Ctrl-z ja Ctr-Shift-z undo ja redo pikanäppäimet
- Lisätty Ctrl-o (Open), Ctrl-n (New file), Ctrl-s (Save) pikanäppäimet
- Lisätty tietokanta tiedostoille
    - FileDatabase luokka, joka vastaa tietokannasta
    - Editori ehdottaa suoraan viittä viimeksi muokattua tiedostoa, kun painetaan Open nappia
    - Kaikki editorilla muokatut tiedostot luetellaan myös popup-ikkunassa
        - Editori pitää käynnistää uudelleen, että tiedostojen lista päivittyy
- Lisätty visuaalisen editoring heading-napille lisää vaihtoehtoja dropdown-ikkunassa

## Viikko 6
- Lisätty editors-kansioon visual.py tiedosto ja VisualEditor luokka, joka vastaa tekstin mukauttamisesta visuaalisessa muodossa
    - Lisätty funktio, joka lisää/poistaa tägejä tekstikentästä sitä mukaan, kun siihen kirjoitetaan, ja muokkaa tägien sisällä olevan tekstin tyylitettyyn muotoon
- Lisätty testit tietokannan toiminnalle