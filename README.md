# Uudenmaan luontokohteet

Helsingin Yliopiston tietokantasovelluskurssilla toteutettava sovellus, jonka tarkoituksena on tarjota käyttäjälle tarkasteltavaksi ja arvioitavaksi erilaisia ulkoilu- ja retkeilykohteita Uudenmaan alueelta.

## Sovelluksen kuvaus

Sovellus on tarkoitus toteuttaa hyvin vastaavalla tavalla kuin esimerkkiaiheissa annettu ravintolasovellus. Sovellukseen on tarkoitus toteuttaa karttaa, jossa näkyy luontokohteiden sijainnit. Kohteesta painamalla avautuu lisää tietoa.

Sovellukseen toteutetaan myös käyttäjäkirjautuminen ja käyttäjätyyppejä on kaksi: tavallinen käyttäjä sekä ylläpitäjä. Tavallinen käyttäjä voi antaa luontokohteille arvion (0-5 tähteä) sekä merkitä niitä suosikeiksi. Käyttäjä voi myös hakea luontokohteita kunnittain tai kohteen nimellä sekä tarkastella listausta, jossa kohteet on järjestetty niiden suosion mukaan (perustuu käyttäjien antamiin arvioihin).

Ylläpitäjä voi taas lisätä ja poistaa luontokohteita sekä muokata niiden tietoja. Ylläpitäjä voi myös poistaa käyttäjien antamia arvioita.

### Käyttöliittymäluonnos

Alla on sovelluksen karkea käyttöliittymäluonnos: 

<img src="https://github.com/hackinen/uudenmaan-luontokohteet/blob/main/dokumentaatio/misc/kayttoliittymaluonnos.jpg" width="600">

Vielä on hieman epäselvää, että päivitetäänkö tarkasteltavan luontokohteen tiedot ainoastaan sivupalkkiin, vai olisiko parempi olla oma näkymä aina tiettyä tarkasteltavaa luonotkohdetta kohti. Ehkä parasta olisi, jos kartasta painamalla kohteen perustiedot, kuten nimi ja tähtien määrä, näkyisivät sivupalkissa ja mikäli käyttäjä haluaa tarkastella kohdetta enemmän, voi sivupalkista painamalla siirtyä tarkempaan näkymään.