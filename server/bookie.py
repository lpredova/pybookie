from sources import footbal_db, wiki


class Bookie:

    def __init__(self):
        pass

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
