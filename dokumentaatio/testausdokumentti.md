# Testausdokumentti

Sovellusta on testattu unittestillä sekä käyttöliittymää käsin tapahtuvalla järjestelmätestauksella.

## Yksikkö- sekä integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikan luokkia <code>UserService</code> ja <code>PasswordService</code> testataan testiluokilla <code>TestUserService</code> sekä <code>TestPasswordService</code>.
Luokille injektoidaan testeissä päätietokannan sijaan testitietokanta, joka luodaan tarvittaessa tiedostoon <code>test_db.py</code>.

### Repositorio-luokat

Luokkia <code>UserRepository</code> ja <code>PasswordRepository</code> testataan testiluokilla <code>TestUserRepository</code> sekä <code>TestPasswordRepository</code>.
Luokille injektoidaan testeissä päätietokannan sijaan testitietokanta, joka luodaan tarvittaessa tiedostoon <code>test_db.py</code>.

## Testauskattavuus

Käyttöliittymä poisluettuna sovelluksen testauksen haarautumakattavuus on 90%

![Coverage report](https://github.com/anttiromppanen/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/coverage.png)

Testaamatta jäi tietokannan alustuksesta vastaava luokka <code>initialize_db.py</code>

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu käsin.
