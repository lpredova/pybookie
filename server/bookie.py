from sources import footbal_db, wiki


class Bookie:
    def __init__(self):
        pass

    @staticmethod
    def make_evaluation(data):
        for team in data:

            team_a = footbal_db.FootballDB.get_team_by_id(team['teamA'])
            team_b = footbal_db.FootballDB.get_team_by_id(team['teamB'])

            if team_a == team_b:
                return 0

            team_a_sum = footbal_db.FootballDB.get_wc_titles(team_a)
            team_b_sum = footbal_db.FootballDB.get_wc_titles(team_b)

            team_a_sum += footbal_db.FootballDB.get_ranking(team_b)
            team_b_sum += footbal_db.FootballDB.get_ranking(team_a)

            team_a_sum += footbal_db.FootballDB.get_wc_games_played(team_a)
            team_b_sum += footbal_db.FootballDB.get_wc_games_played(team_b)

            team_a_sum += footbal_db.FootballDB.get_won_wc_games_played(team_a) * 3
            team_b_sum += footbal_db.FootballDB.get_won_wc_games_played(team_b) * 3

            team_a_sum += footbal_db.FootballDB.get_draw_wc_games_played(team_a)
            team_b_sum += footbal_db.FootballDB.get_draw_wc_games_played(team_b)

            team_a_sum -= footbal_db.FootballDB.get_lost_wc_games_played(team_a) * 3
            team_b_sum -= footbal_db.FootballDB.get_lost_wc_games_played(team_b) * 3

            team_a_sum += footbal_db.FootballDB.get_goal_difference_wc_games_played(team_a)
            team_b_sum += footbal_db.FootballDB.get_goal_difference_wc_games_played(team_b)

            team_a_sum += footbal_db.FootballDB.get_wc_points(team_a)
            team_b_sum += footbal_db.FootballDB.get_wc_points(team_b)

            team_a_sum += footbal_db.FootballDB.get_wc_participations(team_a)
            team_b_sum += footbal_db.FootballDB.get_wc_participations(team_b)

            total_sum = team_a_sum + team_b_sum

            print '%s : %d %%- %s : %d %%' % (
            team_a, float(team_a_sum) / float(total_sum) * 100, team_b, float(team_b_sum) / float(total_sum) * 100)

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
