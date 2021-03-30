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
  - kirjautuminen epäonnistuu jos käyttäjätunnus sekä salasana eivät täsmää, käyttäjälle ilmoitetaan virheestä
#### Kirjautumisen jälkeen
- Käyttäjä näkee etusivulla sovellukseen lisäämänsä salasanat
- Käyttäjä voi kirjautua ulos sovelluksesta logout napilla
- Käyttäjä voi lisätä sovellukseen uusia salasanoja
  - käyttäjä siirtyy uuden lisäyksen mahdollistamaan näkymään
  - käyttäjä täyttää lomakkeeseen sivuston, käyttäjätunnuksen sekä salasanan
    - kentät eivät voi olla tyhjiä
  - käyttäjä pääsee cancel napilla takaisin päänäkymään

## Jatkokehitysideoita

- Järjestelmään voi luoda uuden käyttäjän
- Salasanojen poisto sovelluksesta
- Käyttäjätunnusten hashaus
- Lisättyjen salasanojen listaus eri kriteerien mukaan
- Salasanojen filtteröinti päänäkymässä
