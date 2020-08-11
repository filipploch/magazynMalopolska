import os

class TimelineHTMLbuilder:
    init_html = ""
    body_html = ""
    end_html = ""
    file_name = ""
    pth = ""
    
    def __init__(self, file_name):
        self.file_name = file_name
        self.pth = "html\\leagues\\" + file_name + "\\"


    def set_init_html(self):
        css_global = '<link rel="stylesheet" href="css\\main.css">'
        css_specific = '<link rel="stylesheet" href="css\\'+'terminarz.css">'
        self.init_html = '<html><head>' + css_global + css_specific + '<meta charset="UTF-8"></head>\
        <body><div id="container"><div id="top"><p></p></div><div id="left_margin"></div><div id="table">\
        <table id="timeline" align="center"><tbody>'

    def get_init_html(self):
        return self.init_html

    # def set_body_html(self, section):
    #  self.body_html = section

    def set_body_html(self, one_match):
        team_a_name = one_match.team_a_name
        team_b_name = one_match.team_b_name
        team_a_score = one_match.team_a_score
        team_b_score = one_match.team_b_score
        match_date = one_match.match_date.strftime('%Y-%m-%d')
        match_time = one_match.match_time
        match_spot = one_match.match_spot
        match_queue = one_match.queue
        self.body_html += '<tr class="break"><td colspan="4"><p>1</p></td></tr>\
        <tr class="event_time"><td class="left_cell">'+match_queue+'</td>\
        <td colspan="2" class="center_cell">'+match_time+'</td><td class="right_cell">'+match_date+'</td></tr>\
        <tr class="result"><td class="team_name left_cell">' + team_a_name +'</td>\
<td class="score">' + team_a_score + '</td>\
<td class="score">' + team_b_score + '</td>\
<td class="team_name right_cell">' + team_b_name + '</td></tr>\
<tr class="match_spot"><td colspan="4" class="spot">' + match_spot + '</td></tr>'


    def get_body_html(self):
        return self.body_html

    def set_end_html(self):
        self.end_html = '</tbody></table></div><div id="right_margin"></div></div></body></html>'

    def get_end_html(self):
        return self.end_html

    def save_as_html(self, file_name, html_code):

        try:
            x = self.pth+file_name+".html"
            if os.path.isdir(self.pth) == False:
                os.mkdir(self.pth)

            with open(x,"w+", encoding='utf8') as f:
                f.write(html_code)
                f.close()

        except TypeError as valerr:
            print(valerr)
