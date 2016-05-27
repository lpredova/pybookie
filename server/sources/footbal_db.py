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
    def get_games():
        """
        :rtype: object
        """
        print 'getting data about groups'

        data = None
        path = FootballDB.groups_file
        if os.path.isfile(path):
            with open(path, 'r') as file:
                data = file.read().replace('\n', '')

        return data