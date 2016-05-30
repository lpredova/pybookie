from sources import footbal_db, wiki


class Bookie:

    def __init__(self):
        pass

    @staticmethod
    def make_evaluation(data):
        print data
        for team in data:
            team_a = footbal_db.FootballDB.get_team_by_id(team['teamA'])
            team_b = footbal_db.FootballDB.get_team_by_id(team['teamB'])

            print team_a
            print team_b





    @staticmethod
    def evaluate_data():
        footballDb = footbal_db.FootballDB.evaluate()
        wikipedia = wiki.WikiData.evaluate()
        print "evaluating"

    @staticmethod
    def get_games():
        print 'get games bookie'
        games = footbal_db.FootballDB.get_games()

        return games
