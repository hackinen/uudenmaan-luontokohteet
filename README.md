# Uudenmaan luontokohteet

Helsingin Yliopiston tietokantasovelluskurssilla toteutettava sovellus, jonka tarkoituksena on tarjota käyttäjälle tarkasteltavaksi ja arvioitavaksi erilaisia ulkoilu- ja retkeilykohteita Uudenmaan alueelta.

### Sovellus

[Sovellus herokussa](https://uudenmaan-luontokohteet.herokuapp.com)

## Dokumentaatio

[Määrittelydokumentti](https://github.com/hackinen/uudenmaan-luontokohteet/blob/main/dokumentaatio/maarittelydokumentti.md)

## Sovelluksen eteneminen

Sovellukseen on toteutettu suunnitellut toiminnot karttaa, hakemista ja suosikiksi lisäämistä lukuunottamatta. Etusivulta löytyy listaus suosituimmista luontokohteista ja joita painamalla pääsee kyseisen luontokohteen omalle sivulle. Vastaavasti kaikki tällä hetkellä tietokannassa olevat kohteet löytyvät välilehdeltä "Kaikki kohteet". Lisäksi on olemassa sivu "Oma profiili", josta voi tarkastella oman profiilinsa tietoja. Tällä sivulla on adminin lisäystoiminnot sekä kaikille käyttäjille näkyvä lista omista arvioistaan. Admin voi myös poistaa kohteisiin liittyviä tietoja sekä kokonaisia kohteita (nämä toiminnot löytyvät jokaisen kohteen omalta sivulta).

Tietokannassa on tällä hetkellä neljä taulua: users, reviews, destinations ja attractions. Vielä olisi tarkoitus toteuttaa käyttäjien suosikkeja listaava taulu.

Tarkempi kuvaus sovelluksen suunnitelmasta löytyy [määrittelydokumentista](https://github.com/hackinen/uudenmaan-luontokohteet/blob/main/dokumentaatio/maarittelydokumentti.md).


### Testikäyttäjä

Sovelluksessa on valmiina adminin oikeuksilla varustettu testikäyttäjä:

- nimimerkki: admin
- salasana: admininsalasanajeejee

Tavallista käyttäjää voi testata luomalla oman uuden käyttäjän.