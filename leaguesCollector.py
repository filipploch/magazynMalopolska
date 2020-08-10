import match
import league
from datetime import datetime, timedelta


class LeaguesCollector:
    d1 = datetime.now()
    d0 = d1 + timedelta(days=-7)
    d2 = d1 + timedelta(days=7)
    dates = [d0, d1, d2]
    def run_scraper(self):
        self.dates = [self.d0, self.d1, self.d2]
        # iv_wchod = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37521.html?round=0", "IV Liga wschodnia", "liga4wschod", 1, 0, 6, self.dates)
        # iv_zachod = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37460.html?round=0", "IV Liga zachodnia","liga4zachod", 1, 0, 4, self.dates)
        # o_krakow1 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36880.html?round=0", "Kraków, Klasa Okręgowa Grupa 1", "okregowaKrakow1", 1, 1, 3, self.dates)
        o_krakow2 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36978.html?round=0", "Kraków, Klasa Okręgowa Grupa 2", "okregowaKrakow2", 1, 1, 3, self.dates)
        o_krakow3 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36735.html?round=0?round=0", "Kraków, Klasa Okręgowa Grupa 3", "okregowaKrakow3", 1, 1, 2, self.dates)
        # o_chrzanow = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37005.html?round=0", "Chrzanów, Klasa Okręgowa", "okregowaChrzanow", 1, 1, 2, self.dates)
        # o_tarnow = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37319.html?round=0", "Tarnów, Klasa Okręgowa", "okregowaTarnow", 1, 1, 2, self.dates)
        # o_bochnia = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37274.html?round=0", "Bochnia, Klasa Okręgowa Grupa 2", "okregowaBochnia", 1, 1, 2, self.dates)
        # o_nsacz = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37249.html?round=0", "Nowy Sącz, Klasa Okręgowa Grupa 1", "okregowaNSacz", 1, 1, 2, self.dates)
        # o_podhale = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36716.html?round=0", "Podhale, Klasa Okręgowa Grupa 1", "okregowaPodhale", 1, 1, 2, self.dates)
        # a_krakow1 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37410.html?round=0", "Kraków, Klasa A Grupa 1", "aklasaKrakow1", 1, 0, 2, self.dates)
        # a_krakow2 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37411.html?round=0", "Kraków, Klasa A Grupa 2", "aklasaKrakow2", 1, 0, 2, self.dates)
        # a_krakow3 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37412.html?round=0", "Kraków, Klasa A Grupa 3", "aklasaKrakow3", 1, 0, 2, self.dates)
        # a_chrzanow = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37007.html?round=0", "Chrzanów, Klasa A", "aklasaChrzanow", 1, 0, 2, self.dates)
        # a_tarnow = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37647.html?round=0", "Tarnów, Klasa A", "aklasaTarnow", 1, 0, 2, self.dates)
        # a_bochnia = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37691.html?round=0", "Bochnia, Klasa A", "aklasaBochnia", 1, 0, 2, self.dates)
        # a_gorlice = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37183.html?round=0", "Gorlice, Klasa A", "aklasaGorlice", 1, 0, 2, self.dates)
        # a_limanowa = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37010.html?round=0", "Limanowa, Klasa A", "aklasaLimanowa", 1, 0, 2, self.dates)
        # a_olkusz = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36881.html?round=0", "Olkusz, Klasa A", "aklasaOlkusz", 1, 0, 2, self.dates)
        # a_brzesko = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36844.html?round=0", "Brzesko, Klasa A", "aklasaBrzesko", 1, 0, 2, self.dates)
        # a_podhale = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36811.html?round=0", "Podhale, Klasa A", "aklasaPodhale", 1, 0, 2, self.dates)
        # a_zabno = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36760.html?round=0", "Żabno, Klasa A", "aklasaZabno", 1, 0, 2, self.dates)
        # a_myslenice = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36736.html?round=0", "Myślenice, Klasa A", "aklasaMyslenice", 1, 0, 2, self.dates)
        # a_wadowice = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,38450.html?round=0", "Wadowice, Klasa A", "aklasaWadowice", 1, 0, 2, self.dates)
        # a_oswiecim = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37391.html?round=0", "Oświęcim, Klasa A", "aklasaOswiecim", 1, 0, 2, self.dates)
        # a_wieliczka = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37193.html?round=0", "Wieliczka, Klasa A", "aklasaWieliczka", 1, 0, 2, self.dates)
        # b_myslenice = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36737.html?round=0", "Myślenice, Klasa B", "bklasaMyslenice", 1, 0, 2, self.dates)
        # b_zabno = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36776.html?round=0", "Żabno, Klasa B", "bklasaZabno", 1, 0, 2, self.dates)
        # b_brzesko = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,36877.html?round=0", "Brzesko, Klasa B", "bklasaBrzesko", 1, 0, 2, self.dates)
        # b_limanowa = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37011.html?round=0", "Limanowa, Klasa B", "bklasaLimanowa", 1, 0, 2, self.dates)
        # b_podhale1 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37119.html?round=0", "Podhale, Klasa B Grupa 1", "bklasaPodhale1", 1, 0, 2, self.dates)
        # b_podhale2 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37120.html?round=0", "Podhale, Klasa B Grupa 2", "bklasaPodhale2", 1, 0, 2, self.dates)
        # b_olkusz = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37197.html?round=0", "Olkusz, Klasa B", "bklasaPodhale2", 1, 0, 2, self.dates)
        # b_wieliczka = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37205.html?round=0", "Wieliczka, Klasa B", "bklasaWieliczka", 1, 0, 2, self.dates)
        # b_krakow1 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37413.html?round=0", "Kraków, Klasa B Grupa 1", "bklasaKrakow1", 1, 0, 2, self.dates)
        # b_krakow2 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37414.html?round=0", "Kraków, Klasa B Grupa 2", "bklasaKrakow2", 1, 0, 2, self.dates)
        # b_krakow3 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37415.html?round=0", "Kraków, Klasa B Grupa 3", "bklasaKrakow3", 1, 0, 2, self.dates)
        # b_krakow4 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37416.html?round=0", "Kraków, Klasa B Grupa 4", "bklasaKrakow4", 1, 0, 2, self.dates)
        # b_oswiecim = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37551.html?round=0", "Oświęcim, Klasa B", "bklasaOswiecim", 1, 0, 2, self.dates)
        # b_nsacz = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37829.html?round=0", "Nowy Sącz, Klasa B", "bklasaNSacz", 1, 0, 2, self.dates)
        # # # b_wadowice1 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37968.html?round=0", "Wadowice, Klasa B Grupa 1", "bklasaWadowice1", 1, 0, 2, self.dates)
        # b_wadowice2 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37969.html?round=0", "Wadowice, Klasa B Grupa 2", "bklasaWadowice2", 1, 0, 2, self.dates)
        # b_wadowice3 = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37971.html?round=0", "Wadowice, Klasa B Grupa 3", "bklasaWadowice3", 1, 0, 2, self.dates)
        # b_tarnow = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,38008.html?round=0", "Tarnów, Klasa B", "bklasaTarnow", 1, 0, 2, self.dates)
        # # # b_chrzanow = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,38552.html?round=0", "Chrzanów, Klasa B", "bklasaChrzanow", 1, 0, 2, self.dates)
        #
        # c_wieliczka = league.League("https://www.laczynaspilka.pl/rozgrywki/nizsze-ligi,37210.html?round=0", "Klasa C Wieliczka", "cklasaWieliczka", 1, 0, 2, self.dates)







