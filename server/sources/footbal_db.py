import json
import os

'''
TODO
get top 10 club players
get scorers
get last 10 games
'''


class FootballDB:
    groups_file = '/Users/lovro/Coding/Python/pybookie/server/sources/groups.json'
    wc_history_file = '/Users/lovro/Coding/Python/pybookie/server/sources/wc_history'

    def __init__(self):
        pass

    @staticmethod
    def evaluate():
        # https://github.com/openfootball/world-cup
        print "evaluating football db"

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

        if titles != 0:
            titles = titles[0]

        return int(titles)

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
    def get_games():
        """
        :rtype: object
        """
        data = None
        path = FootballDB.groups_file
        if os.path.isfile(path):
            with open(path, 'r') as football_teams:
                data = football_teams.read().replace('\n', '')

        return data
