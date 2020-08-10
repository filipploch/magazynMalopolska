import bs4 as bs

class Team():
    position = int
    name = ""
    matches = int
    points = int
    goals_scored = int
    goals_lost = int
    wins = int
    ties = int
    loses = int

    def __init__(self, tr):
        strtr = str(tr)
        code = "<html><head></head><body><table><tr>" + strtr + "</tr></table></body></html>"
        soup = bs.BeautifulSoup(code, 'lxml')
        td = soup.find_all('td')
        self.position = td[1].text
        self.name = td[3].text
        self.matches = td[4].text
        self.points = td[5].text
        goals = td[9].text
        self.goals_spliter(goals)
        self.wins = td[6].text
        self.ties = td[7].text
        self.loses = td[8].text


    def goals_spliter(self, goals):
        if ":" in goals:
            #delete all spaces
            # score = goals.replace('\n', '').replace('\r', '')
            scores = goals.split(":")
            self.goals_scored = scores[0]
            self.goals_lost = scores[1]
            # print(self.team_a_score,":",self.team_b_score)
        else:
            self.goals_scored = "?"
            self.goals_scored = "?"