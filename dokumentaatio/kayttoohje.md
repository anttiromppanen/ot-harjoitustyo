# Käyttöohje

Sovelluksen viimeisimmän toimivan version saat ladattua [Releases](https://github.com/anttiromppanen/ot-harjoitustyo/releases)-sivun alta.

### Sovelluksen käynnistäminen
Ohje olettaa, että käyttäjällä on poetry valmiiksi asennettuna.

#### Riippuvuuksien asennus
`poetry install`

#### Ohjelman ajaminen
`poetry run invoke start` tai `poetry run invoke start-windows`

#### Testien ajaminen
`poetry run invoke test`

#### Testikattavuusraportti
`poetry run invoke coverage-report`

Komento muodostaa kansion "htmlcov", jonka sisältä löytyy tiedosto "index.html". Avaamalla tiedoston selaimella näet ohjelman kattavuusraportin.

#### Lint
`poetry run invoke lint`

Tarkastaa src-kansion pylintin avulla.

### Sovellus

Sovellus aukeaa kirjautumisnäkymään. Käyttäjä voi kirjautua järjestelmään lisäämällään käyttäjällä.

![Kirjautuminen](https://github.com/anttiromppanen/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/login.png)

Rekisteröitymissivulla sovelluksen käyttäjä voi luoda järjestelmään uuden käyttäjän. Cancel-napilla käyttäjä ohjataan takaisin kirjautumissivulle.

![Rekisteröinti](https://github.com/anttiromppanen/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/register.png)

Käyttäjän kirjautuessa sisään toimivalla käyttäjällä, näytetään käyttäjän oma sivu. Logout-napilla käyttäjä kirjataan ulos.

![Käyttäjän sivu](https://github.com/anttiromppanen/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/userview.png)

Käyttäjän omalta sivulta käyttäjä pääsee salasanojen lisäys-sivulle. Cancel-napilla käyttäjä ohjataan takaisin käyttäjän omalle sivulle.

![Salasanojen lisäys](https://github.com/anttiromppanen/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/newpassword.png)
