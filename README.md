# Opetussovellus

Helsingin yliopiston Tietokantasovellus-kurssin harjoitustyö syksyllä 2020. Kurssi- ja opetussivusto, johon rekisteröidytään joko opettajaksi tai oppilaaksi. Yhdet ylläpitäjätunnukset syntyvät valmiiksi tietokantaa luotaessa.

Sovelluksen toimivat toiminnallisuudet:
* Käyttäjä voi rekisteröityä tai kirjautua sovellukseen. Salasana kryptataan tietokantaan.
* Kirjautunutta käyttäjää tervehtii aloitussivu, jossa on statukseen sopiva kuva.
* Aloitussivulta on opettajalla mahdollisuus luoda uusi kurssi, joka sisältää otsikon, tekstiä, vaikeusasteen ja avainsanan. Aloitussivulle myös listautuvat kaikki omat kurssit.
* Kurssilistauksen kautta opettajan on mahdollista päästä kurssisivulle, josta voi luoda kysymyksiä kurssiin liittyen. Kysymykset ja vastausvaihtoehdot tallentuvat tietokantaan, vaikka vastausvahtoehdot eivät vielä listaudu kysymysten alle.
* Oppilas voi liittyä kursseille ja omat kurssit näkyvät listauksena etusivulla. Liityttyään kurssille oppilas voi nähdä kurssin sisällön ja kysymykset.
* Ylläpitäjä näkee kaikkien käyttäjien ja kurssien tiedot ja voi poistaa käyttäjiä ja kursseja.

Vielä tekemättä:
* Ulkoasuun ei ole vielä panostettu
* Kaikki kursseihin liittyvät hakutoiminnot on toteuttamatta: kurssien hakeminen nimellä tai avainsanalla.
* Kysymysten vastausvaihtoehdot eivät ole näkyvissä eikä niihin pysty vastaamaan
* Oppilaiden edistymistä ei voi seurata vielä mistään.

Sovellusta voi testata Herokussa osoitteessa https://opetussovellus1.herokuapp.com/. Käyttäjä voi itse luoda oppilas- tai opettajatunnukset. Admin-käyttäjän tunnukset ovat: käyttäjätunnus _admin_ ja salasana _pass_ 

