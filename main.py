import urllib.request


def read_player(url):
    page = str(urllib.request.urlopen(url).read())
    player_name_pos = page.find('class="player-name"')
    player_name = page[page.find('>', player_name_pos) + 1:page.find('&nbsp', player_name_pos)] if player_name_pos != -1 else ''
    player_name = player_name.replace('&#039;', '\'')
    total_pos = page.find('class="player-totals">TOTAL')
    total_all = page[page.find('</td>', total_pos) + 5:page.find('</tr>', total_pos)]
    total_all = total_all.replace('\\n', '').replace('\\t', '').replace('<td>', '').replace(',', '.')
    total_all = total_all.split('</td>')[:-1]

    COMP = float(total_all[0]) if total_pos != -1 else ''
    ATT = float(total_all[1]) if total_pos != -1 else ''
    YDS = float(total_all[3]) if total_pos != -1 else ''
    TD = float(total_all[5]) if total_pos != -1 else ''
    INT = float(total_all[6]) if total_pos != -1 else ''
    if total_pos != -1:
        a = (COMP / ATT - 0.3) * 5
        b = (YDS / ATT - 3) * 0.25
        c = (TD / ATT) * 20
        d = 2.375 - (INT / ATT * 25)
        PR = (a + b + c + d) / 6 * 100
    else:
        PR = ''

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


'''a
with open('input_minak.txt') as f:
    for url in f:
        print(read_player(url))'''
print(read_player("http://www.nfl.com/player/jordanta'amu/2562752/profile"))
