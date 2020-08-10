import os


class TableHTMLbuilder:
    init_html = ""
    body_html = ""
    body_html_even = ""
    end_html = ""
    file_name = ""
    pth = ""

    def __init__(self, file_name):
        self.file_name = file_name
        self.pth = "html\\leagues\\" + file_name + "\\"

    def set_init_html(self):
        css_global = '<link rel="stylesheet" href="css\\main.css">'
        css_specific = '<link rel="stylesheet" href="css\\' + 'tabela.css">'
        self.init_html = '<html><head>' + css_global + css_specific + '<meta charset="UTF-8"></head>\
        <body><div id="container"><div id="top"><p></p></div><div id="left_margin"></div><div id="table">\
        <table id="timeline" align="center"><tbody><tr class="header"><td colspan="2"><p></p></td><td id="matches">M</td>\
        <td id="wins">Z</td><td id="ties">R</td><td id="loses">P</td><td id="goals_scored">B+</td><td id="goals_lost">B-</td>\
        <td id="goals_difference">+/-</td><td id="points">P</td></tr>'

    def get_init_html(self):
        return self.init_html

    def set_body_html(self, one_team, tr_classes):
        position = one_team.position
        name = one_team.name
        matches = one_team.matches
        points = one_team.points
        goals_scored = one_team.goals_scored
        goals_lost = one_team.goals_lost
        goals_difference = int(goals_scored) - int(goals_lost)
        #goals_difference = int(goals_scored) - int(goals_lost)
        wins = one_team.wins
        ties = one_team.ties
        loses = one_team.loses
        self.body_html += '<tr class="table' + tr_classes + '"><td class="position">' + position + '</td>\
            <td class="name">' + name + '</td>\
            <td class="matches">' + matches + '</td>\
            <td class="wins">' + wins + '</td>\
            <td class="ties">' + ties + '</td>\
            <td class="loses">' + loses + '</td>\
            <td class="goals_scored">' + goals_scored + '</td>\
            <td class="goals_lost">' + goals_lost + '</td>\
            <td class="goals_difference">' + str(goals_difference) + '</td>\
            <td class="points">' + str(points) + '</td></tr>'


    def get_body_html(self):
        return self.body_html


    def set_end_html(self):
        self.end_html = '</tbody></table></div><div id="right_margin"></div></div></body></html>'

    def get_end_html(self):
        return self.end_html

    def save_as_html(self, file_name, html_code):

        try:
            x = self.pth + file_name + ".html"
            if os.path.isdir(self.pth) == False:
                os.mkdir(self.pth)

            with open(x, "w+", encoding='utf8') as f:
                f.write(html_code)
                f.close()

        except TypeError as valerr:
            print(valerr)
