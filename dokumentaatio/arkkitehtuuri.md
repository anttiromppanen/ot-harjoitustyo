# Arkkitehtuurikuvaus

## Rakenne
![Pakkauskaavio](https://github.com/anttiromppanen/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/package.png "Pakkauskaavio")

Pakkaus ui sisältää käyttöliittymään liittyvän koodin, repositories tietokannan kanssa keskustelevan koodin, <br />
services sovelluslogiikan koodin, sekä entities sovellukseen liittyvät tietokohteet.

### Käyttöliittymä
![Käyttöliittymä](https://github.com/anttiromppanen/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/kayttoliittymaluonnos.png "Käyttöliittymä")

Käyttöliittymä sisältää 4 näkymää:
  - Kirjautuminen
  - Uuden käyttäjän luominen
  - Käyttäjän näkymä
  - Uusien salasanojen lisäys

Näkymät ovat erillisiä luokkia, ui-luokka hallitsee eri näkymiä käyttäjän toimenpiteiden perusteella.

### Sovelluslogiikka

Sovellukseen talletetaan käyttäjiä, sekä käyttäjän lisäämiä salasanoja. Käyttäjät, sekä salasanat talletetaan User-, sekä Password-olioina.

Sovelluksen sovelluslogiikasta vastaavat luokat UserService sekä PasswordService. <br />
Sovelluslogiikasta vastaavan luokan metodit kutsuvat UserRepository- sekä PasswordRepository-luokkien metodeita, <br />
jotka vastaavat tietokannan kanssa keskustelusta.

### Tietojen pysyväistallennus

Sovelluksen tiedot talletetaan SQLite-tietokantaan. Ohjelma ajettaessa ensimmäistä kertaa luodaan tiedostot db.py, sekä test_db.py. <br />
Pääsovelluksen tiedot talletetaan tiedostoon db.py. Tiedosto test_db.py toimii erillisenä tietokantana testejä varten. <br />
Tietokanta sisältää kaksi taulua: Users, sekä Passwords. 
