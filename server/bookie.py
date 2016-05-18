from sources import db, wiki


class Bookie:
    def __init__(self):
        pass

    @staticmethod
    def evaluate_data():

        footballDb = db.FootballDB.evaluate()
        wikipedia = wiki.WikiData.evaluate()
        print "evaluating"


