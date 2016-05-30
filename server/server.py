# coding=utf-8
# !/usr/bin/env python
import json
import sys

import spade
from spade.ACLMessage import ACLMessage
from spade.Agent import Agent, os
from spade.Behaviour import ACLTemplate, Behaviour

from bookie import Bookie

os.path.dirname(os.path.realpath(__file__))


class MasterBettingAgent(Agent):
    class Booking(Behaviour):
        msg = None

        def _process(self):
            self.msg = self._receive(True)

            if self.msg:
                request = json.loads(self.msg.content)

                if request['request_type'] == 'games':
                    bookie = Bookie()
                    self.send_message(json.dumps({'request_type': 'games', 'data': bookie.get_games()}))

                if request['request_type'] == 'team_selection':
                    bookie = Bookie()
                    self.send_message(json.dumps(
                        {'request_type': 'game_evaluation', 'data': bookie.make_evaluation(request['teams'])}))

                else:
                    print request['request_type']

            else:
                print 'random'

            if json.loads(self.msg.content)['request_type'] == 'bet':
                params = json.loads(self.msg.content)
                print params['bet_type']

                bookie = Bookie()
                bookie.evaluate_data()

                self.send_message('Booking results')

        def stop_agent(self):
            print "Agent is dying..."
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
            print "\nBet evaluation sent to:" + client + " !"

    def _setup(self):
        print 'Main booking agent is running...'

        template = ACLTemplate()
        template.setOntology('booking')

        behaviour = spade.Behaviour.MessageTemplate(template)
        booking = self.Booking()
        self.addBehaviour(booking, behaviour)


if __name__ == "__main__":
    mba = MasterBettingAgent('bookie@127.0.0.1', 'booking')
    mba.start()
