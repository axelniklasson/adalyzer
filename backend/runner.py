from autobahn.wamp import auth
from asyncio import coroutine
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
import threading
import asyncio
import persona_mappings
from personality_extraction import Personality
from location_optimisation import Location
import random


class Connection():

    history = []

    def __init__(self):
        print("Init Connection")

    def run(self):
        runner = ApplicationRunner(url=u"ws://api.interchange.ericsson.net/v1", realm=u"interchange")
        runner.run(self.Component)

    class Component(ApplicationSession):

        def __init__(self, config=None):
            ApplicationSession.__init__(self, config)
            print(config)
            print("component created")

        def onConnect(self):
            print("transport connected")
            self.join(self.config.realm, [u"wampcra"], u'3b9d29f0-c054-4a04-9f0a-fbbfbb425eb3')

        def onChallenge(self, challenge):
            print("authentication challenge received")

            if challenge.method == u"wampcra":
                print("WAMP-CRA challenge received: {}".format(challenge))

                if u'salt' in challenge.extra:
                    # salted secret
                    key = auth.derive_key(u"uSrnbKa2cjxkYu9Flom1ZMIkNYMriSZ5tKzlhVKJT6o", challenge.extra['salt'], challenge.extra['iterations'], challenge.extra['keylen'])
                else:
                    # plain, unsalted secret
                    key = u"uSrnbKa2cjxkYu9Flom1ZMIkNYMriSZ5tKzlhVKJT6o"

                # compute signature for challenge, using the key
                signature = auth.compute_wcs(key, challenge.extra['challenge'])

                # return the signature to the router for verification
                return signature

        @coroutine
        def onJoin(self, details):
            print("session joined")

            cars = yield from self.call(u"interchange.app.3b9d29f0-c054-4a04-9f0a-fbbfbb425eb3.vehicles")
            hist = []

            # RPC GET
            try:
                for car in cars:
                    data = yield from self.call(u"interchange.vehicle." + car + ".state")
                    data["id"] = car
                    hist.append(data)
                    for i in range(0,200):
                        data = self.duplicate(data)
                        hist.append(data)
                    Location.set_optimal_locations(hist)
                print("call result: {}".format(hist))
            except Exception as e:
                print("call error: {0}".format(e))

            # ???
            self.leave()

        def onLeave(self, details):
            print(details)
            print("session left")
            self.disconnect()

        def onDisconnect(self):
            print("transport disconnected")
            return

        def onCar(self, data, timestamp, *args, **kwargs):
            print("{}".format(data))

        def duplicate(self, car):
            car2 = car.copy()
            car2['positioning_system']['location']['lat'] += random.randint(-100, 100) / 100000
            car2['positioning_system']['location']['lng'] += random.randint(-100, 100) / 100000
            car2['positioning_system']['speed'] += 5
            car2['positioning_system']['heading'] += 1
            return car2
