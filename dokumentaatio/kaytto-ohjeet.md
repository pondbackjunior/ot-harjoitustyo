# Käyttöohjeet

Tämä on yksinkertainen HTML-tiedostojen editori, jolla on kaksi muotoa (Source ja Visual) ja muutamia tekstieditorien yleisiä toimintoja.

## Napit

Open:
- Listaa 5 uusinta tiedostoa, jota on muokattu tällä sovelluksella (päivittyy aina sovelluksen käynnistyessä)
- Kaikki tiedostot jota on muokattu tällä sovelluksella listataan erillisesä ikkunassa, jos painaa "All files"
- Voi myös valita tietokoneelta uuden tiedoston painamalla "Select file"

New file:
- Tyhjentää tekstikentän ja aloittaa uuden tiedoston

Save:
- Tallentaa tiedoston joko nykyiseen tiedostoon mitä käsitellään tai uuteen tiedostoon

Preview:
- Avaa tekstikentän sisällön oletusselamiessa, jotta sitä voi esikatsella "luonnossa".

Source / Visual:
- Vaihtaa source-muodon ja visual-muodon välillä

Vasemman palkin napit:
- Lisää tekstiin automaattisesti muutamia yleisiä html-tägejä.
  - Jos tekstiä ei ole valittu, se lisää pelkät tägit ja siirtää hiiren tägien keskelle
  - Jos tekstiä on valittu, se laittaa tägit valitun tekstin ympärille

## Hakutoiminto

Editorin alareunassa on kaksi tekstikenttää. Vasemmanpuoleiseen voi laittaa hakusanan, ja editori korostaa ne tekstistä. Oikeanpuolimmaiseen voi laittaa korvaustekstin, ja joko korvata aina hakutermille ensimmäisen löydön, tai kaikki löydetyt hakusanat tekstistä.

## Muotoilu

Source-muoto korostaa pelkästään html-tägit, ja viual-muoto automaattisesti päivittää tekstin ulkoasua muutamien html-tägien perusteella, jotta se vaikuttaa olevan suoraan editorissa lähempänä sitä, miltä se näyttää todellisuudessa.

Visual editorissa:
- `<b>` tägien sisällä oleva teksti on lihavoitu
- `<i>` tägien sisällä oleva teksti on kursivoitu
- `<u>` tägien sisällä oleva teksti on alleviivattu
- `<h1>` - `<h5>` tägien sisällä oleva teksti on suurennettu otsikon koon perusteella
- Html-tägit yleisesti on himmeällä, jotta ne eivät sekoitu visuaaliseen muotoiluun.

Molemmissa editoreissa säilyy sisennys, eli jos kirjoitetaan esim. 4 välilyönnin päähän, seuraava rivi alkaa myös kirjoittamaan 4 välilyönnin päähän.

## Pikanäppäimet

- `Ctr-b` Lihavointi
- `Ctrl-i` Kursiivi
- `Ctrl-u` Alleviivaus
- `Ctrl-a` Valitse kaikki
- `Ctrl-z` Kumoa
- `Ctrl-Shift-z` Tee uudelleen
- `Ctrl-n` Uusi tiedosto
- `Ctrl-o` Avaa tiedosto
- `Ctrl-s` Tallenna tiedosto