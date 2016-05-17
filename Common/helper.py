import sys


class Helper:
    def __init__(self):
        pass

    @staticmethod
    def stop_agent(self):
        print "Agent is dying..."
        self.kill()
        sys.exit()
