# Opetussovellus

Helsingin yliopiston Tietokantasovellus-kurssin harjoitustyö syksyllä 2020. Kurssi- ja opetussivusto, johon rekisteröidytään joko opettajaksi tai oppilaaksi. Yhdet ylläpitäjätunnukset syntyvät valmiiksi tietokantaa luotaessa.

### Sovelluksen toimivat toiminnallisuudet:
* Käyttäjä voi rekisteröityä tai kirjautua sovellukseen. Salasana kryptataan tietokantaan.
* Kirjautunutta käyttäjää tervehtii aloitussivu, jossa on statukseen sopiva kuva.

Opettaja voi
* luoda uusia kursseja, jotka sisältävät otsikon, tekstiä, vaikeusasteen ja avainsanan
* luoda kurssille kysymyksiä, joissa on enintään neljä vastausvaihtoehtoa, joista moni vaihtoehto voi olla oikein
* poistaa omia kurssejaan
* poistaa oppilaita kurssilta.
 
Oppilas voi
* liittyä kursseille
* nähdä omat ja saatavilla olevat kurssit listauksena etusivulla
* nähdä kurssiin liittyvät kysymykset kurssisivulla
* vastata yksittäisiin kysymyksiin kerran tai useammin ja saada välittömän palautteen, vastasiko oikein.

Ylläpitäjä voi
* nähdä kaikkien käyttäjien ja kurssien tiedot
* poistaa käyttäjiä itseään lukuun ottamatta
* poistaa kursseja
* nähdä tietoja viidestä viimeisimmästä vastauksesta, joita oppilaat ovat antaneet

Käytettävyydestä ja toimivuudesta on pyritty huolehtimaan syötteiden validoinneilla ja oikeuksia on rajoitettu esimerkiksi niin, että oppilailla ei ole mahdollisuutta nähdä oppilaslistoja eikä opettajien tai ylläpitäjien ole mahdollista vastata kysymyksiin.

** Sovelluksesta jäi toteuttamatta:**
* Oppilaiden edistymistä ei voi seurata mistään.
* Käyttäjän etusivulle olisi ollut hyvä listata vain esimerkiksi viisi tuoreinta kurssia tai käyttäjää.
* Kaikki kurssit tai käyttäjät olisivat voineet listautua omille sivuilleen, joista niitä olis voinut hakea nimellä tai avainsanalla.

Sovellusta voi testata Herokussa osoitteessa https://opetussovellus1.herokuapp.com/. Käyttäjä voi itse luoda oppilas- tai opettajatunnukset. Admin-käyttäjän tunnukset ovat: käyttäjätunnus _admin_ ja salasana _pass_ 

