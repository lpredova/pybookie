# coding=utf-8
# !/usr/bin/env python
import json
import sys

import spade
from spade.ACLMessage import ACLMessage
from spade.Agent import Agent
from spade.Behaviour import ACLTemplate, Behaviour

from bookie import Bookie


class MasterBettingAgent(Agent):
    class Booking(Behaviour):
        msg = None

        def _process(self):
            print "Master betting agent up and running"

            self.msg = self._receive(True)

            if self.msg is not None:
                print self.msg.content
                params = json.loads(self.msg.content)
                print params
                print params['bet_type']

                bookie = Bookie()
                bookie.evaluate_data()

                self.send_message('Booking reveived')

        def stop_agent(self):
            print "Agent organizator se gasi..."
            self.send_message("stop")
            self.kill()
            sys.exit()

        def send_message(self, message):
            client = "client@127.0.0.1"
            address = "xmpp://" + client

            receiver = spade.AID.aid(name=client, addresses=[address])

            self.msg = ACLMessage()
            self.msg.setPerformative("inform")
            self.msg.setOntology("booking")
            self.msg.setLanguage("eng")
            self.msg.addReceiver(receiver)
            self.msg.setContent(message)

            self.myAgent.send(self.msg)
            print "\nposlao sam poruku agentu klijentu " + client + " !"

    def _setup(self):
        print 'Main booking agent is alive'

        template = ACLTemplate()
        template.setOntology('booking')

        behaviour = spade.Behaviour.MessageTemplate(template)
        booking = self.Booking()
        self.addBehaviour(booking, behaviour)


if __name__ == "__main__":
    mba = MasterBettingAgent('bookie@127.0.0.1', 'booking')
    mba.start()
