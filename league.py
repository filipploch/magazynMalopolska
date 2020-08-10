import bs4 as bs
import urllib.request
import match, team, timelineHtmlBuilder, tableHtmlBuilder, leaguesCollector
from datetime import datetime, timedelta

class League:
    file_name = ""
    matches = []
    teams_number = int
    start_date = datetime
    middle_date = datetime
    end_date = datetime
    def __init__(self, url, name, file_name, promotion, playoff, degradation, dates):
        source = urllib.request.urlopen(url)
        soup = bs.BeautifulSoup(source, 'lxml')
        tables = soup.find('table')
        section = soup.find('section', {'class': 'season__games'})
        site_table = tables
        articles = soup.find_all('article', {'class': 'season__game'})
        league_table = site_table.find_all('tr')
        #site_timeline = tables[1]
        #league_matches = site_timeline.find_all('tr', {'class':'terminarze-spotkanie'})
        league_name = name
        self.file_name = file_name
        #test_match = match.Match(league_matches[0])
        # self.set_auto_time(datetime.now())
        self.start_date = dates[0]
        self.middle_date = dates[1]
        self.end_date = dates[2]

        #MAKING HTML TABLE
        table_builder = tableHtmlBuilder.TableHTMLbuilder(self.file_name)
        table_builder.set_init_html()
        table_builder.set_end_html()

        tr_classes = ""
        for i in range(1, len(league_table)):
            one_team = team.Team(league_table[i])
            # Check if position is odd or even
            if i%2 == 0:
                tr_classes += " even"
            else:
                tr_classes += " odd"
            # Check if position is "promotion"
            if i < promotion + 1:
                tr_classes += " promotion"
            # Check if position is "playoff"
            if playoff > 0:
                if i >= promotion + 1 and i < 3 + promotion + playoff:
                    tr_classes += " playoff"
            # Check if position is "degradation"
            if i > len(league_table) - degradation - 1:
                tr_classes += " degradation"

            table_builder.set_body_html(one_team, tr_classes)
            tr_classes = ""

        html_code = table_builder.get_init_html()+table_builder.get_body_html()+table_builder.get_end_html()
        table_builder.save_as_html("tabela", html_code)

        # #MAKING HTML TIMELINE
        timeline_builder = timelineHtmlBuilder.TimelineHTMLbuilder(self.file_name)
        timeline_builder.set_init_html()
        # timeline_builder.set_body_html(section)
        timeline_builder.set_end_html()

        print(len(articles))
        for i in range(0, len(articles)):

            one_match = match.Match(articles[i])
        #     x = one_match.match_date
        #     y = self.middle_date
        #     z = x < y
            print("one match date", one_match.match_date)
            print("one start date", self.start_date)
            print("one middle date", self.middle_date)
            if one_match.match_date >= self.start_date and one_match.match_date <= self.middle_date:
                timeline_builder.set_body_html(one_match)
        #         # print(timeline_builder.get_body_html())
        #         # self.matches.append(one_match)
        #         # print(one_match.team_a_name, one_match.team_a_score, one_match.team_b_score, one_match.team_b_name)
        #
        a = str(timeline_builder.get_init_html())
        b = str(timeline_builder.get_body_html())
        c = str(timeline_builder.get_end_html())
        html_code = a + b + c
        print("TU", b)
        timeline_builder.save_as_html("terminarz", html_code)
        # games = len(league_matches) * 2
        # self.teams_number = int(games**(.5))

    def set_auto_time(self, datetime_now):
        self.middle_date = datetime_now
        self.start_date = self.middle_date + timedelta(days=-7)
        self.end_date = self.middle_date + timedelta(days=7)

    def set_start_date(self, datetime):
        self.start_date = datetime