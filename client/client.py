# coding=utf-8
# !/usr/bin/env python
import json
import sys

import spade
from spade.ACLMessage import ACLMessage
from spade.Agent import Agent
from spade.Behaviour import ACLTemplate, MessageTemplate

from print_formatter import PrintFormatter


class ClientAgent(Agent):
    class BookingSettings(spade.Behaviour.OneShotBehaviour):

        dialog_selection = None
        msg = None
        games = None

        def _process(self):
            self.msg = self._receive(True)

            if self.msg:
                request = json.loads(self.msg.content)
                if request['request_type'] == 'games':
                    self.games = request['data']
                    self.show_dialog()

        def show_dialog(self):
            self.dialog_selection = raw_input("\n1) Make a Free bet\n2) Generate bet\n3) Exit\n\nSelect:")
            if self.dialog_selection == '1':
                self.set_free_bet_preferences()

            if self.dialog_selection == '2':
                self.set_bet_preferences()

            if self.dialog_selection == '3':
                print "Chosen option 2"
                self.stop_agent()

        def stop_agent(self):
            print "Agent is dying..."
            self.kill()
            sys.exit()

        def set_bet_preferences(self):
            if self.games:
                PrintFormatter.games(self.games)

            preferences = None
            number_of_teams = 0

            while number_of_teams == 0:
                number_of_teams = raw_input("\nNumber of teams:")
                bet_type = raw_input("\nType of the bet (1 - Risky, 2 - Mixed, 3 - Sure stuff):")
                preferences = {'request_type': 'bet', 'number_of_teams': number_of_teams, 'bet_type': bet_type}

            self.send_message(json.dumps(preferences))

        def set_free_bet_preferences(self):
            if self.games:
                PrintFormatter.games(self.games)

            teams = []
            number_of_teams = input("\nNumber of gamse:")

            for i in range(0, int(number_of_teams)):
                print "GAME %d. \n" % (i + 1)
                team_a = raw_input("\nTeam A id: ")
                team_b = raw_input("\nTeam B id: ")

                teams.append({'teamA': team_a, 'teamB': team_b})

            result = json.dumps({'request_type': 'team_selection', 'teams': teams})
            self.send_message(result)

        def send_message(self, content):
            master_agent = spade.AID.aid(name="bookie@127.0.0.1", addresses=["xmpp://bookie@127.0.0.1"])
            self.msg = ACLMessage()
            self.msg.setPerformative("inform")
            self.msg.setOntology("booking")
            self.msg.setLanguage("eng")
            self.msg.addReceiver(master_agent)
            self.msg.setContent(content)
            self.myAgent.send(self.msg)
            print 'Msg sent to master agent ' + content

    def _setup(self):
        print "\n Agent\t" + self.getAID().getName() + " is up and running "

        feedback_template = ACLTemplate()
        feedback_template.setOntology('booking')

        mt = MessageTemplate(feedback_template)
        settings = self.BookingSettings()
        self.addBehaviour(settings, mt)

        settings.send_message(json.dumps({'request_type': 'games'}))


if __name__ == '__main__':
    p = ClientAgent('client@127.0.0.1', 'booking')
    p.start()
