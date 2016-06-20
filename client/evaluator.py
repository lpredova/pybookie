import os


class Evaluator:
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    path = BASE_DIR + '/client/results'

    def __init__(self):
        pass

    @staticmethod
    def find_result(data):
        if os.path.isfile(Evaluator.path):
            f = open(Evaluator.path)

            for game in data:
                team_a = game['result'].split(' ')[0]
                team_b = game['result'].split(' ')[5]

                for line in f:
                    compare_a = line.split(' ')[0]
                    compare_b = line.split(' ')[2]

                    if (str(team_a.strip()) == str(compare_b.strip()) or str(team_a.strip()) == str(compare_a.strip())) \
                            and (str(team_b.strip()) == str(compare_b.strip()) or str(team_b.strip()) == str(
                                compare_a.strip())):
                        print line
