# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on yksinkertainen salasanojen hallinnointipalvelu. Uusi käyttäjä voi luoda käyttäjätunnuksen, jonka jälkeen kirjautuneena käyttäjä voi lisätä sekä poistaa haluamiansa tunnuksia eri palveluihin.

## Käyttöliittymäluonnos

Sovellus koostuu neljästä eri näkymästä. Sovellus aukeaa kirjautumisnäkymään josta käyttäjä voi joko siirtyä uuden käyttäjän lisäysnäkymään tai kirjautumalla sovelluksen päänäkymään. Päänäkymässä käyttäjä voi siirtyä uuden salasanan lisäysnäkymään tai uloskirjautumalla kirjautumisnäkymään. Lisäysnäkymistä päästään edelliseen näkymään cancel-napin avulla. 

![Kayttoliittymaluonnos](./kuvat/kayttoliittymaluonnos.png "Kayttoliittymaluonnos")

## Perusversion tarjoama toiminnallisuus

#### Ennen kirjautumista
- :heavy_check_mark: Käyttäjä voi kirjautua sovellukseen
  - :heavy_check_mark: käyttäjä syöttää käyttäjätunnuksen sekä salasanan lomakkeeseen
  - :heavy_check_mark: käyttäjätunnuksen sekä salasanan täsmätessä käyttäjä kirjataan sovellukseen sisään
  - :heavy_check_mark: kirjautuminen epäonnistuu jos käyttäjätunnus sekä salasana eivät täsmää
  - :heavy_check_mark: järjestelmään voi luoda uuden käyttäjän	
  - :heavy_check_mark: uuden käyttäjän lisäyssivulta pääsee kirjautumisnäkymään cancel-napilla

#### Kirjautumisen jälkeen

  - :heavy_check_mark: käyttäjä siirtyy näkymään jossa näytetään käyttäjän lisäämät salasanat
  - :heavy_check_mark: käyttäjä siirtyy uuden lisäyksen mahdollistamaan näkymään

## Jatkokehitysideoita

- :heavy_check_mark: Taulu salasanoille tietokantaan
- :heavy_check_mark: Käyttäjä voi lisätä sovellukseen uusia salasanoja
- :heavy_check_mark: Käyttäjä näkee etusivulla sovellukseen lisäämänsä salasanat
- :heavy_check_mark: Käyttäjä voi kirjautua ulos sovelluksesta logout napilla
- :heavy_check_mark: Käyttäjä pääsee uuden salasanan lisäyssivulle
- :heavy_check_mark: Salasanojen lisäys sovelluksen kautta
- :heavy_check_mark: Virheiden ilmoitus käyttäjälle sovelluksen kautta
- Salasanojen poisto sovelluksesta
- Käyttäjätunnusten hashaus
- Lisättyjen salasanojen listaus eri kriteerien mukaan
- Salasanojen filtteröinti päänäkymässä
