# Zero salt rounds
---
Sovellus on yksinkertainen salasanojen hallinnointipalvelu. Uusi käyttäjä voi luoda käyttäjätunnuksen, jonka jälkeen kirjautuneena käyttäjä voi lisätä sekä poistaa haluamiansa tunnuksia eri palveluihin.

Sovellus on testattu Python-versioilla 3.8.2 sekä 3.6.9. Sovelluksen tulisi toimia kaikilla Python-versioilla 3.6.0 lähtien.
### Dokumentaatio
---
[vaatimusmäärittely](https://github.com/anttiromppanen/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)<br />
[tuntikirjanpito](https://github.com/anttiromppanen/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)<br />
[arkkitehtuuri](https://github.com/anttiromppanen/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

### Asennus
---
Ohje olettaa, että käyttäjällä on poetry valmiiksi asennettuna.

#### Riippuvuuksien asennus
`poetry install`

#### Ohjelman ajaminen
`poetry run invoke start` tai `poetry run invoke start-windows`

`käyttäjänimi: root`

`salasana: root`

Huomaa, että (väliaikaiseksi) sovellusta avattaessa tietokanta tyhjennetään sekä alustetaan kyseisellä käyttäjällä.

#### Testien ajaminen
`poetry run invoke test`

#### Testikattavuusraportti
`poetry run invoke coverage-report`

Komento muodostaa kansion "htmlcov", jonka sisältä löytyy tiedosto "index.html". Avaamalla tiedoston selaimella näät ohjelman kattavuusraportin.

#### Lint
`poetry run invoke lint`

Tarkastaa src-kansion pylintin avulla.
