import json
import os


class FootballDB:
    groups_file = '/Users/lovro/Coding/Python/pybookie/server/sources/groups.json'

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
        print data
        for group in data:
            for team in group['teams']:
                if int(team['id']) == int(team_id):
                    result = team['team']
        return result

    ## TODO
    '''
    get titles
    get wins
    get num of caps
    get top 10 club players
    get fifa ranking
    get scorers
    get last 10 games
    '''

    @staticmethod
    def get_games():
        """
        :rtype: object
        """
        print 'getting data about groups'

        data = None
        path = FootballDB.groups_file
        if os.path.isfile(path):
            with open(path, 'r') as football_teams:
                data = football_teams.read().replace('\n', '')

        return data
