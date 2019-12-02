import urllib.request


def read_player(url):
    page = str(urllib.request.urlopen(url).read())
    player_name_pos = page.find('class="player-name"')
    player_name = page[page.find('>', player_name_pos) + 1:page.find('&', player_name_pos)]
    total_pos = page.find('class="player-totals">TOTAL')
    total_all = page[page.find('</td>', total_pos) + 5:page.find('</tr>', total_pos)]
    total_all = total_all.replace('\\n', '').replace('\\t', '').replace('<td>', '').replace(',', '.')
    total_all = total_all.split('</td>')[:-1]

    COMP = float(total_all[0])
    ATT = float(total_all[1])
    YDS = float(total_all[3])
    TD = float(total_all[5])
    INT = float(total_all[6])
    a = (COMP / ATT - 0.3) * 5
    b = (YDS / ATT - 3) * 0.25
    c = (TD / ATT) * 20
    d = 2.375 - (INT / ATT * 25)
    PR = (a + b + c + d) / 6 * 100

    player = {
        'player_name': player_name,
        'COMP': COMP,
        'ATT': ATT,
        'YDS': YDS,
        'TD': TD,
        'INT': INT,
        'PR': PR,
    }

    return player


with open('input_minak.txt') as f:
    for url in f:
        print(read_player(url))
