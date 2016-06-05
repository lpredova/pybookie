import json


class PrintFormatter:
    def __init__(self):
        pass

    @staticmethod
    def games(games):
        games = json.loads(games)

        for group in games:
            print '\n----------------------------------'
            print '\nGroup:' + group['group']
            for team in group['teams']:
                print "%d. %s\n" % (team['id'], team['team'])

    @staticmethod
    def results(results):
        for game in results:
            print '%s \n' % game['result']