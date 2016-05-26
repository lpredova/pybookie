# coding=utf-8
# !/usr/bin/env python
import json
import sys

import spade
from spade.ACLMessage import ACLMessage
from spade.Agent import Agent
from spade.Behaviour import ACLTemplate, MessageTemplate


class ClientAgent(Agent):
    class BookingSettings(spade.Behaviour.OneShotBehaviour):

        dialog_selection = None
        msg = None

        def _process(self):
            print "Setting booking settings"
            self.msg = self._receive(True)

            if self.msg:
                print "\nI got message from master agent" + self.msg.content

            else:
                self.show_dialog()
                self.send_preferences("Waited")

        def show_dialog(self):

            self.dialog_selection = raw_input("\n1) Make a bet\n2) Exit\n\nSelect:")
            if self.dialog_selection == '1':
                self.set_bet_preferences()

            if self.dialog_selection == '2':
                print "Chosen option 2"
                self.stop_agent()

        def stop_agent(self):
            print "Agent is dying..."
            self.kill()
            sys.exit()

        def set_bet_preferences(self):

            preferences = None
            number_of_teams = 0

            while number_of_teams == 0:
                number_of_teams = raw_input("\nNumber of teams:")
                bet_type = raw_input("\nType of the bet (1 - Risky, 2 - Mixed, 3 - Sure stuff):")
                preferences = {'number_of_teams': number_of_teams, 'bet_type': bet_type}

            self.send_preferences(json.dumps(preferences))

        def send_preferences(self, preferences):

            master_agent = spade.AID.aid(name="bookie@127.0.0.1", addresses=["xmpp://bookie@127.0.0.1"])

            self.msg = ACLMessage()
            self.msg.setPerformative("inform")
            self.msg.setOntology("booking")
            self.msg.setLanguage("eng")
            self.msg.addReceiver(master_agent)
            self.msg.setContent(preferences)
            self.myAgent.send(self.msg)

            print "\nBet preferences sent!"

    def _setup(self):
        print "\n Agent\t" + self.getAID().getName() + " is up and running "

        feedback_template = ACLTemplate()
        feedback_template.setOntology('booking')

        mt = MessageTemplate(feedback_template)
        settings = self.BookingSettings()
        self.addBehaviour(settings, mt)

        settings.show_dialog()


if __name__ == '__main__':
    p = ClientAgent('client@127.0.0.1', 'booking')
    p.start()
