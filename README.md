# Uudenmaan luontokohteet

Helsingin Yliopiston tietokantasovelluskurssilla toteutettava sovellus, jonka tarkoituksena on tarjota käyttäjälle tarkasteltavaksi ja arvioitavaksi erilaisia ulkoilu- ja retkeilykohteita Uudenmaan alueelta.

### Sovellus

[Sovellus herokussa](https://uudenmaan-luontokohteet.herokuapp.com)

## Dokumentaatio

[Määrittelydokumentti](https://github.com/hackinen/uudenmaan-luontokohteet/blob/main/dokumentaatio/maarittelydokumentti.md)

## Sovelluksen eteneminen

Sovellukseen on toteutettu kirjatumis- ja rekisteröintitoiminnot kokonaisuudessaan sekä käyttöliittymää on aloitettu. Etusivulta löytyy listaus suosituimmista luontokohteista ja joita painamalla pääsee kyseisen luontokohteen omalle sivulle. Vastaavasti kaikki tällä hetkellä tietokannassa olevat kohteet löytyvät välilehdeltä "Kaikki kohteet". Lisäksi on luotu sivu "Oma profiili", josta voi tarkastella oman profiilinsa tietoja. Tänne on tarkoitus tulla kaikki admintoiminnot sekä kaikille käyttäjille ainakin lista omista suosikkikohteista (ja ehkä omista annetuista arvioista).

Tietokannassa on tällä hetkellä kolme taulua: users, reviews ja destinations. Näistä reviews on vielä vaiheessa, eikä sitä vielä käytetä. Seuraavana tauluna on tarkoitus toteuttaa yksitäisiä luontopolkuja/nähtävyyksiä kuvaava taulu, jossa aina jokainen polku/nähtävyys linkittyy johonkin kohteseen. Taulun avulla voidaan jokaisen kohteen alle listata sen polut ja nähtävyydet. 

Tarkempi kuvaus sovelluksen suunnitelmasta löytyy [määrittelydokumentista](https://github.com/hackinen/uudenmaan-luontokohteet/blob/main/dokumentaatio/maarittelydokumentti.md).


### Testikäyttäjä

Sovelluksessa on valmiina adminin oikeuksilla varustettu testikäyttäjä (vielä mitään admin-toimintoja ei ole toteutettu):

- nimimerkki: admin
- salasana: admininsalasanajeejee

Tavallista käyttäjää voi testata luomalla oman uuden käyttäjän, tosin tssä vaiheessa eroa adminin ja tavallisen käyttäjän välillä ei ole.
