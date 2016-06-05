# coding=utf-8

import json
import os


class FootballDB:
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    groups_file = BASE_DIR + '/sources/groups.json'
    wc_history_file = BASE_DIR + '/sources/wc_history'
    wc_team_file = BASE_DIR + '/sources/squads/'

    top_teams = ['RealMadrid(ESP)', 'Barcelona(ESP)', 'Chelsea(ENG)', 'ManchesterCity(ENG)', 'ParisSaint-Germain(FRA)',
                 'BayernMunich(GER)', 'Internazionale(ITA)', 'Napoli(ITA)', 'ManchesterUnited(ENG)', 'Arsenal(ENG)',
                 'Liverpool(ENG)', 'Juventus(ITA)', 'BorussiaDortmund(GER)', 'AtléticoMadrid(ESP)']

    def __init__(self):
        pass

    @staticmethod
    def get_team_by_id(team_id):
        data = json.loads(FootballDB.get_games())
        result = None
        for group in data:
            for team in group['teams']:
                if int(team['id']) == int(team_id):
                    result = team['team']
        return result

    @staticmethod
    def get_ranking(team_name):
        return int(FootballDB.get_wc_history(team_name, 0))

    @staticmethod
    def get_wc_games_played(team_name):
        return int(FootballDB.get_wc_history(team_name, 2))

    @staticmethod
    def get_won_wc_games_played(team_name):
        return int(FootballDB.get_wc_history(team_name, 3))

    @staticmethod
    def get_draw_wc_games_played(team_name):
        return int(FootballDB.get_wc_history(team_name, 4))

    @staticmethod
    def get_lost_wc_games_played(team_name):
        return int(FootballDB.get_wc_history(team_name, 5))

    @staticmethod
    def get_goal_difference_wc_games_played(team_name):
        gd = FootballDB.get_wc_history(team_name, 6)
        gd = gd.split(':')

        goals_for = int(gd[0])
        goals_against = int(gd[1])

        return goals_for - goals_against

    @staticmethod
    def get_wc_points(team_name):
        return int(FootballDB.get_wc_history(team_name, 7))

    @staticmethod
    def get_wc_participations(team_name):
        return int(FootballDB.get_wc_history(team_name, 8))

    @staticmethod
    def get_wc_titles(team_name):
        titles = FootballDB.get_wc_history(team_name, 9)
        try:
            if titles.isalpha() and int(titles) != 0:
                titles = titles[0]
                return int(titles)
            else:
                return 0
        except Exception:
            return 0

    @staticmethod
    def get_wc_history(team, result_row_index):
        path = FootballDB.wc_history_file
        if os.path.isfile(path):
            f = open(path)

            for line in f:
                if line[0].isdigit():
                    row = line.replace('\n', '')
                    row = row.replace(' ', '')
                    row = row.split('|')
                    if row[1] == team.replace(' ', ''):
                        f.close()
                        try:
                            return row[result_row_index]
                        except BaseException:
                            return 0

    @staticmethod
    def get_wc_team_player_ratings(team):
        path = '%s%s.txt' % (FootballDB.wc_team_file, (team.replace(' ', '-')))
        path = path.lower()
        team_rating = 0
        if os.path.isfile(path):
            f = open(path)

            for line in f:
                try:
                    row = line.split('##')
                    row = row[1].replace(' ', '').split(',')

                    team_rating += int(row[0])
                    team_name = row[1].replace('\n', '')

                    if team_name in FootballDB.top_teams:
                        team_rating += 10

                except Exception:
                    pass

        return team_rating

    @staticmethod
    def get_games():
        data = None
        path = FootballDB.groups_file
        if os.path.isfile(path):
            with open(path, 'r') as football_teams:
                data = football_teams.read().replace('\n', '')

        return data
