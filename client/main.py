# coding=utf-8
# !/usr/bin/env python
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
            self.show_dialog()

            if self.msg:
                print "I got message from client"
                Helper.stop_agent()

            else:
                self.send_preferences("Waited")

        def show_dialog(self):

            self.dialog_selection = raw_input("\n1)Predlozi sastanak\n2)Odustani od pregovaranja\n\nOdabir:")

            if self.dialog_selection == '1':
                print "Chosen option 1"

            if self.dialog_selection == '2':
                print "Chosen option 2"
                self.stop_agent()

        def stop_agent(self):
            print "Agent is dying..."
            self.kill()
            sys.exit()

        def send_preferences(self, response):

            master_agent = spade.AID.aid(name="bookie@127.0.0.1", addresses=["xmpp://bookie@127.0.0.1"])

            self.msg = ACLMessage()
            self.msg.setPerformative("inform")
            self.msg.setOntology("povratna_informacija")
            self.msg.setLanguage("eng")
            self.msg.addReceiver(master_agent)
            self.msg.setContent(response)
            self.myAgent.send(self.msg)

            print "\nAgent je poslao sam poruku agentu organizatoru %s\n!" % response

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
