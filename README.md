# Uudenmaan luontokohteet

Helsingin Yliopiston tietokantasovelluskurssilla toteutettava sovellus, jonka tarkoituksena on tarjota käyttäjälle tarkasteltavaksi ja arvioitavaksi erilaisia ulkoilu- ja retkeilykohteita Uudenmaan alueelta.

### Sovellus

[Sovellus herokussa](https://uudenmaan-luontokohteet.herokuapp.com)

## Dokumentaatio

[Määrittelydokumentti](https://github.com/hackinen/uudenmaan-luontokohteet/blob/main/dokumentaatio/maarittelydokumentti.md)

## Sovelluksen toiminta

Uudenmaan luontokohteet -sovelluksella käyttäjä voi tarkastella erilaisia luontokohteita uudenmaan alueella, antaa niille arvioita ja lisätä niitä omalle suosikkilistalleen.

Kirjautumisen tai uuden käyttäjätunnuksen luomisen jälkeen sovellus avautuu etusivulleen, jossa näkyy kaikki luontokohteet kartalla sekä listaus tällä hetkellä suosituimmista luontokohteista. Luontokohteen suosio perustuu keskiarvoon käyttäjien antamista arvioista (1-5 tähteä). Sovelluksen yläreunasta löytyy valikko, jossa etusivun lisäksi on sivut "Kaikki kohteet", "Oma profiili" sekä "Kirjaudu ulos".

Sivulla "Kaikki kohteet" voi käyttäjä tarkastella listausta kaikista tietokannasta löytyvistä kohteista sekä hakea kohteita haluamallaan hakusanalla (esim. Lohja). Jokaisen kohteen alla näkyy kohteen saama arvio, sekä kuinka monta arviota kyseinen kohde on saanut.

Kohdetta painamalla aukeaa kyseisen kohteen oma sivu. Tällä sivulla on listaus kohteeseen kuuluvista luontopoluita ja/tai nähtävyyksistä. Käyttäjä voi myös lisätä kohteen suosikkeihinsa tai poistaa sen suosikeistaan. Sivun oikeassa reunassa on mahdollista antaa kohteelle arvio (tähdet 1-5 ja vapaaehtoinen kommentti). Arvostelulomakkeen alapuolella näkyy listaus kaikista kohteen saamista arvosteluista. Mikäli käyttäjällä on admin-oikeudet, on sivun alareunassa myös mahdollisuus poistaa kohteesta yksittäisiä polkuja/nähtävyyksiä sekä poistaa koko kohde. Lisäksi admin voi poistaa kenen tahansa antaman arvostelun.

Sivulla "Oma profiili" näkyy käyttäjän käyttäjätiedot, listaus omista suosikeista sekä käyttäjän antamat arviot. Käyttäjä voi tällä sivulla poistaa omia arvioitaan. Mikäli käyttäjä on admin, on tällä sivulla myös mahdollista lisätä uusia luontokohteita sekä lisätä uusia luontopolkuja ja nähtävyyksiä kohteiden yhteyteen.

Tietokannassa on viisi taulua: users, reviews, destinations, attractions ja favourites.


### Testikäyttäjä

Sovelluksessa on valmiina adminin oikeuksilla varustettu testikäyttäjä:

- nimimerkki: admin
- salasana: admininsalasanajeejee

Tavallista käyttäjää voi testata luomalla oman uuden käyttäjän.

### Mitä olisi voinut vielä parantaa?

Sovellukseen olisi voinut vielä toteuttaa adminille toiminnon, jolla admin voi luoda olemassa olevista käyttäjistä admineja sekä poistaa olemassa olevia käyttäjiä. Ajattelin kuitenkin, että sovellus on tarkoitettu lähinnä käyttäjän näkökulmasta käytettäväksi ja siis admineja voi hyvin sen takia luoda itse käsin tietokantaan, mikäli sille olisi tarvetta.