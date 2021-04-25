# Uudenmaan luontokohteet

Helsingin Yliopiston tietokantasovelluskurssilla toteutettava sovellus, jonka tarkoituksena on tarjota käyttäjälle tarkasteltavaksi ja arvioitavaksi erilaisia ulkoilu- ja retkeilykohteita Uudenmaan alueelta.

### Sovellus

[Sovellus herokussa](https://uudenmaan-luontokohteet.herokuapp.com)

## Dokumentaatio

[Määrittelydokumentti](https://github.com/hackinen/uudenmaan-luontokohteet/blob/main/dokumentaatio/maarittelydokumentti.md)

## Sovelluksen eteneminen

Sovellukseen on toteutettu suunnitellut toiminnot karttaa ja hakemista lukuunottamatta. Etusivulta löytyy listaus suosituimmista luontokohteista ja joita painamalla pääsee kyseisen luontokohteen omalle sivulle. Vastaavasti kaikki tällä hetkellä tietokannassa olevat kohteet löytyvät välilehdeltä "Kaikki kohteet". Lisäksi on olemassa sivu "Oma profiili", josta voi tarkastella oman profiilinsa tietoja. Tällä sivulla voi admin lisätä uusia kohteita ja tietoja kohteisiin liittyen. Lisäksi sivulla on kaikille käyttäjille näkyvä lista omista arvioistaan sekä omista suosikkikohteistaan. Admin voi myös poistaa kohteisiin liittyviä tietoja sekä kokonaisia kohteita (nämä toiminnot löytyvät jokaisen kohteen omalta sivulta).

Tietokannassa on tällä hetkellä viisi taulua: users, reviews, destinations, attractions ja favourites.

Viimeiseen palautukseen mennessä on vielä tarkoitus ainakin saada kartta toimintaan ja mielellään myös jonkinlainen hakukenttä, mikäli aikaa riittää.

Tarkempi kuvaus sovelluksen suunnitelmasta löytyy [määrittelydokumentista](https://github.com/hackinen/uudenmaan-luontokohteet/blob/main/dokumentaatio/maarittelydokumentti.md).


### Testikäyttäjä

Sovelluksessa on valmiina adminin oikeuksilla varustettu testikäyttäjä:

- nimimerkki: admin
- salasana: admininsalasanajeejee

Tavallista käyttäjää voi testata luomalla oman uuden käyttäjän.