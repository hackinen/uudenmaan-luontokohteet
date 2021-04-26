# Uudenmaan luontokohteet

Helsingin Yliopiston tietokantasovelluskurssilla toteutettava sovellus, jonka tarkoituksena on tarjota käyttäjälle tarkasteltavaksi ja arvioitavaksi erilaisia ulkoilu- ja retkeilykohteita Uudenmaan alueelta.

### Sovellus

[Sovellus herokussa](https://uudenmaan-luontokohteet.herokuapp.com)

## Dokumentaatio

[Määrittelydokumentti](https://github.com/hackinen/uudenmaan-luontokohteet/blob/main/dokumentaatio/maarittelydokumentti.md)

## Sovelluksen eteneminen

Sovellukseen on toteutettu suunnitellut toiminnot hakemista lukuunottamatta. Etusivulta löytyy kartta kaikista luontokohteista, sekä listaus suosituimmista luontokohteista, joita painamalla pääsee kyseisen luontokohteen omalle sivulle. Kaikki tällä hetkellä tietokannassa olevat kohteet löytyvät listauksena välilehdeltä "Kaikki kohteet". Lisäksi on olemassa sivu "Oma profiili", josta voi tarkastella oman profiilinsa tietoja, takastella omia arvioita (sekä poistaa niitä) ja tarkastella omia suosikkikoteitaan. Lisäksi tällä sivulla voi admin lisätä uusia kohteita ja tietoja kohteisiin liittyen. Admin voi myös poistaa kohteisiin liittyviä tietoja sekä kokonaisia kohteita (nämä toiminnot löytyvät jokaisen kohteen omalta sivulta).

Tietokannassa on tällä hetkellä viisi taulua: users, reviews, destinations, attractions ja favourites.

Viimeiseen palautukseen mennessä on vielä tarkoitus parannella ulkoasua sekä saada toimintaan jonkinlainen hakukenttä, mikäli aikaa riittää.

Tarkempi kuvaus sovelluksen suunnitelmasta löytyy [määrittelydokumentista](https://github.com/hackinen/uudenmaan-luontokohteet/blob/main/dokumentaatio/maarittelydokumentti.md).


### Testikäyttäjä

Sovelluksessa on valmiina adminin oikeuksilla varustettu testikäyttäjä:

- nimimerkki: admin
- salasana: admininsalasanajeejee

Tavallista käyttäjää voi testata luomalla oman uuden käyttäjän.