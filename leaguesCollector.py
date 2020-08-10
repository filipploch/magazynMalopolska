import match
import league
from datetime import datetime, timedelta


class LeaguesCollector:
    d1 = datetime.now()
    d0 = d1 + timedelta(days=-7)
    d2 = d1 + timedelta(days=+7)
    dates = [d0, d1, d2]
    def run_scraper(self):
        iv_wchod = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37521.html", "IV Liga wschodnia", "liga4wschod", 1, 0, 6, self.dates)
        iv_zachod = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37460.html", "IV Liga zachodnia","liga4zachod", 1, 0, 4, self.dates)
        o_krakow1 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36880.html", "Kraków, Klasa Okręgowa Grupa 1", "okregowaKrakow1", 1, 1, 3, self.dates)
        o_krakow2 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36978.html", "Kraków, Klasa Okręgowa Grupa 2", "okregowaKrakow2", 1, 1, 3, self.dates)
        o_krakow3 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36735.html", "Kraków, Klasa Okręgowa Grupa 3", "okregowaKrakow3", 1, 1, 2, self.dates)
        o_chrzanow = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37005.html", "Chrzanów, Klasa Okręgowa", "okregowaChrzanow", 1, 1, 2, self.dates)
        o_tarnow = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37319.html", "Tarnów, Klasa Okręgowa", "okregowaTarnow", 1, 1, 2, self.dates)
        o_bochnia = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37274.html", "Bochnia, Klasa Okręgowa Grupa 2", "okregowaBochnia", 1, 1, 2, self.dates)
        o_nsacz = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37249.html", "Nowy Sącz, Klasa Okręgowa Grupa 1", "okregowaNSacz", 1, 1, 2, self.dates)
        o_podhale = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36716.html", "Podhale, Klasa Okręgowa Grupa 1", "okregowaPodhale", 1, 1, 2, self.dates)
        a_krakow1 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37410.html", "Kraków, Klasa A Grupa 1", "aklasaKrakow1", 1, 0, 2, self.dates)
        a_krakow2 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37411.html", "Kraków, Klasa A Grupa 2", "aklasaKrakow2", 1, 0, 2, self.dates)
        a_krakow3 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37412.html", "Kraków, Klasa A Grupa 3", "aklasaKrakow3", 1, 0, 2, self.dates)
        a_chrzanow = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37007.html", "Chrzanów, Klasa A", "aklasaChrzanow", 1, 0, 2, self.dates)
        a_tarnow = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37647.html", "Tarnów, Klasa A", "aklasaTarnow", 1, 0, 2, self.dates)
        a_bochnia = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37691.html", "Bochnia, Klasa A", "aklasaBochnia", 1, 0, 2, self.dates)
        a_gorlice = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37183.html", "Gorlice, Klasa A", "aklasaGorlice", 1, 0, 2, self.dates)
        a_limanowa = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37010.html", "Limanowa, Klasa A", "aklasaLimanowa", 1, 0, 2, self.dates)
        a_olkusz = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36881.html", "Olkusz, Klasa A", "aklasaOlkusz", 1, 0, 2, self.dates)
        a_brzesko = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36844.html", "Brzesko, Klasa A", "aklasaBrzesko", 1, 0, 2, self.dates)
        a_podhale = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36811.html", "Podhale, Klasa A", "aklasaPodhale", 1, 0, 2, self.dates)
        a_zabno = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36760.html", "Żabno, Klasa A", "aklasaZabno", 1, 0, 2, self.dates)
        a_myslenice = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36736.html", "Myślenice, Klasa A", "aklasaMyslenice", 1, 0, 2, self.dates)
        a_wadowice = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,38450.html", "Wadowice, Klasa A", "aklasaWadowice", 1, 0, 2, self.dates)
        a_oswiecim = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37391.html", "Oświęcim, Klasa A", "aklasaOswiecim", 1, 0, 2, self.dates)
        a_wieliczka = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37193.html", "Wieliczka, Klasa A", "aklasaWieliczka", 1, 0, 2, self.dates)
        b_myslenice = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36737.html", "Myślenice, Klasa B", "bklasaMyslenice", 1, 0, 2, self.dates)
        b_zabno = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36776.html", "Żabno, Klasa B", "bklasaZabno", 1, 0, 2, self.dates)
        b_brzesko = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36877.html", "Brzesko, Klasa B", "bklasaBrzesko", 1, 0, 2, self.dates)
        b_limanowa = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37011.html", "Limanowa, Klasa B", "bklasaLimanowa", 1, 0, 2, self.dates)
        b_podhale1 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37119.html", "Podhale, Klasa B Grupa 1", "bklasaPodhale1", 1, 0, 2, self.dates)
        b_podhale2 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37120.html", "Podhale, Klasa B Grupa 2", "bklasaPodhale2", 1, 0, 2, self.dates)
        b_olkusz = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37197.html", "Olkusz, Klasa B", "bklasaPodhale2", 1, 0, 2, self.dates)
        b_wieliczka = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37205.html", "Wieliczka, Klasa B", "bklasaWieliczka", 1, 0, 2, self.dates)
        b_krakow1 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37413.html", "Kraków, Klasa B Grupa 1", "bklasaKrakow1", 1, 0, 2, self.dates)
        b_krakow2 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37414.html", "Kraków, Klasa B Grupa 2", "bklasaKrakow2", 1, 0, 2, self.dates)
        b_krakow3 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37415.html", "Kraków, Klasa B Grupa 3", "bklasaKrakow3", 1, 0, 2, self.dates)
        b_krakow4 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37416.html", "Kraków, Klasa B Grupa 4", "bklasaKrakow4", 1, 0, 2, self.dates)
        b_oswiecim = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37551.html", "Oświęcim, Klasa B", "bklasaOswiecim", 1, 0, 2, self.dates)
        b_nsacz = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37829.html", "Nowy Sącz, Klasa B", "bklasaNSacz", 1, 0, 2, self.dates)
        # # b_wadowice1 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37968.html", "Wadowice, Klasa B Grupa 1", "bklasaWadowice1", 1, 0, 2, self.dates)
        b_wadowice2 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37969.html", "Wadowice, Klasa B Grupa 2", "bklasaWadowice2", 1, 0, 2, self.dates)
        b_wadowice3 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37971.html", "Wadowice, Klasa B Grupa 3", "bklasaWadowice3", 1, 0, 2, self.dates)
        b_tarnow = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,38008.html", "Tarnów, Klasa B", "bklasaTarnow", 1, 0, 2, self.dates)
        # # b_chrzanow = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,38552.html", "Chrzanów, Klasa B", "bklasaChrzanow", 1, 0, 2, self.dates)

        c_wieliczka = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37210.html", "Klasa C Wieliczka", "cklasaWieliczka", 1, 0, 2, self.dates)







