import bs4 as bs
from datetime import date, time, datetime
class Match:
    match_number = int
    match_date = datetime
    match_time = ""
    team_a_name = ""
    team_a_score = ""
    team_b_name = ""
    team_b_score = ""
    match_spot = ""
    x = 0

    def __init__(self, tr):
        strtr = str(tr)
        code = "<html><head></head><body><table><tr>" + strtr + "</tr></table></body></html>"
        soup = bs.BeautifulSoup(code, 'lxml')
        teams_name = soup.find_all('a', {'class': 'team'})
        t_names = []
        for i in teams_name:
            t_names += i.contents
        # self.match_number = td[0].text
        self.team_a_name = t_names[0]
        self.team_b_name = t_names[1]
        scores = soup.find('span', class_='score')
        if scores == None:
            pass
        else:
            score = scores.text
            # s = score.replace(" ","")
            self.match_score(score)
        match_date_div = soup.find('div', {'class': 'season__game-data'})
        self.set_match_date_and_time(match_date_div)

        match_spot = soup.find('span', {'class': 'spot'})
        self.set_match_spot(match_spot)

    def set_match_spot(self, match_spot):
        self.match_spot = match_spot.text

    def set_match_date_and_time(self, match_date_div):
        str_div = str(match_date_div)
        code = "<html><head></head><body>" + str_div + "</body></html>"
        soup = bs.BeautifulSoup(code, 'lxml')
        spans = soup.find_all('span')
        day_span = spans[0].contents
        day = str(day_span[0])
        month_year = spans[1].contents
        split_month_year = month_year[0].split("/")
        month = str(split_month_year[0])
        year = str(split_month_year[1])
        date = year + "-" + month + "-" + day
        self.match_date = datetime.strptime(date, '%Y-%m-%d')
        time_span = spans[2].contents
        time = str(time_span[0])
        self.match_time = time
    #     splitted_date = match_date.split("-")
    #     year = int(splitted_date[0])
    #     if splitted_date[1].startswith("0"):
    #         month = splitted_date[1]
    #         mon = int(month[1:])
    #     else: mon = int(splitted_date[1])
    #
    #     if splitted_date[2].startswith("0"):
    #         day = splitted_date[2]
    #         d = int(day[1:])
    #     else: d = int(splitted_date[2])
    #
    #     self.match_date(year=year, month=mon, day=d)

    def match_score(self, score):
        if ":" in score:
            #delete all spaces
            score = score.replace('\n', '').replace('\r', '')
            scores = score.split(":")
            self.team_a_score = scores[0]
            self.team_b_score = scores[1]
            # print(self.team_a_score,":",self.team_b_score)
        else:
            self.team_a_score = ""
            self.team_b_score = ""

