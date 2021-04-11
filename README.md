# Uudenmaan luontokohteet

Helsingin Yliopiston tietokantasovelluskurssilla toteutettava sovellus, jonka tarkoituksena on tarjota käyttäjälle tarkasteltavaksi ja arvioitavaksi erilaisia ulkoilu- ja retkeilykohteita Uudenmaan alueelta.

### Sovellus

[Sovellus herokussa](https://uudenmaan-luontokohteet.herokuapp.com)

## Dokumentaatio

[Määrittelydokumentti](https://github.com/hackinen/uudenmaan-luontokohteet/blob/main/dokumentaatio/maarittelydokumentti.md)

## Sovelluksen eteneminen

Sovellukseen on toteutettu kirjatumis- ja rekisteröintitoiminnot kokonaisuudessaan sekä käyttöliittymää on aloitettu. Tällä hetkellä sovelluksella pystyy tarkastelemaan valmiiksi määritettyjä luontokohteita välilehdeltä "Kaikki kohteet".

Tietokannassa on tällä hetkellä kaksi taulua: users ja destinations. Seuraavana tauluna on tarkoitus toteuttaa yksitäisiä luontopolkuja/nähtävyyksiä kuvaava taulu, jossa aina jokainen polku/nähtävyys linkittyy johonkin kohteseen. Taulun avulla voidaan jokaisen kohteen alle listata sen polut ja nähtävyydet. 

Tarkempi kuvaus sovelluksen suunnitelmasta löytyy [määrittelydokumentista](https://github.com/hackinen/uudenmaan-luontokohteet/blob/main/dokumentaatio/maarittelydokumentti.md).


### Testikäyttäjä

Sovelluksessa on valmiina adminin oikeuksilla varustettu testikäyttäjä (vielä mitään admin-toimintoja ei ole toteutettu):

- nimimerkki: admin
- salasana: admininsalasanajeejee
