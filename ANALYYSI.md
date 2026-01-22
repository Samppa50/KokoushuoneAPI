1. Tekoäly teki toimivan projektin jo ensimmäisellä promptilla. Koodi on luettavaa ja sisälsi valmiiksi pyydetty toimintalogiikan error viestien kera. AI myös loi README tiedoston automaattisesti, joka selitti ohjelman käytön. AI käytti myös pyytämiäni työkaluja ja vaihtoi ongelmitta SQL databasen käytöstä in-memory muistiin pyydettäessä. Tämän lisäksi AI käytti myös hyvien tapojen mukaisesti virtuaali enviromenttia flask sovellusta kehittäessä.

2. Vaihtaessani SQL databasesta in-memory muistiin unohti AI poistaa tekemänsä käyttämättömän databasen. AI ei myöskään tehnyt pyytämälleni GET functiolle error viestiä mikäli dataa ei löytynyt. On hyvä huomioida ettei errorin puuttuminen olisi vaikuttanut ohjelman toimintaan.

3. Tekemäni muutokset olivat pieniä ja isoimmaksi tuli kahden error viestin lisääminen. Nämä eivät ole olennaisia ohjelman toiminnalle mutta käyttömukavuutta ne lisäävät.


Ohjelman testaamiseen käytin Thunder Client lisäosaa Visualstudio codessa ja pyydetyt ominaisuudet toimivat moitteetta. AI:na projektissa toimi Copilot yhdistettynä Visual Studioon, jolloin AI pystyi näkemään projektin tiedostojen sisällön luodessaan koodia. 