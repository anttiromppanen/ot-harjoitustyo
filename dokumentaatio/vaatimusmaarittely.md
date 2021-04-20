# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on yksinkertainen salasanojen hallinnointipalvelu. Uusi käyttäjä voi luoda käyttäjätunnuksen, jonka jälkeen kirjautuneena käyttäjä voi lisätä sekä poistaa haluamiansa tunnuksia eri palveluihin.

## Käyttöliittymäluonnos

Sovellus koostuu neljästä eri näkymästä. Sovellus aukeaa kirjautumisnäkymään josta käyttäjä voi joko siirtyä uuden käyttäjän lisäysnäkymään tai kirjautumalla sovelluksen päänäkymään. Päänäkymässä käyttäjä voi siirtyä uuden salasanan lisäysnäkymään tai uloskirjautumalla kirjautumisnäkymään. Lisäysnäkymistä päästään edelliseen näkymään cancel-napin avulla. 

![Kayttoliittymaluonnos](./kuvat/kayttoliittymaluonnos.png "Kayttoliittymaluonnos")

## Perusversion tarjoama toiminnallisuus

#### Ennen kirjautumista
- Käyttäjä voi kirjautua sovellukseen
  - käyttäjä syöttää käyttäjätunnuksen sekä salasanan lomakkeeseen
  - käyttäjätunnuksen sekä salasanan täsmätessä käyttäjä kirjataan sovellukseen sisään
  - kirjautuminen epäonnistuu jos käyttäjätunnus sekä salasana eivät täsmää
  - järjestelmään voi luoda uuden käyttäjän	
  - uuden käyttäjän lisäyssivulta pääsee kirjautumisnäkymään cancel-napilla
#### Kirjautumisen jälkeen

  - käyttäjä siirtyy näkymään jossa näytetään käyttäjän lisäämät salasanat
  - käyttäjä siirtyy uuden lisäyksen mahdollistamaan näkymään

## Jatkokehitysideoita

- Taulu salasanoille tietokantaan
- Käyttäjä voi lisätä sovellukseen uusia salasanoja
- Käyttäjä näkee etusivulla sovellukseen lisäämänsä salasanat
- Käyttäjä voi kirjautua ulos sovelluksesta logout napilla
- Käyttäjä pääsee uuden salasanan lisäyssivulle
- Käyttäjän lisäämien salasanojen näyttäminen
- Salasanojen lisäys sovelluksen kautta
- Virheiden ilmoitus käyttäjälle sovelluksen kautta
- Salasanojen poisto sovelluksesta
- Käyttäjätunnusten hashaus
- Lisättyjen salasanojen listaus eri kriteerien mukaan
- Salasanojen filtteröinti päänäkymässä
