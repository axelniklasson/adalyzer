from autobahn.wamp import auth
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner


class Connection:

    def __init__(self):
        pass

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

        @inlineCallbacks
        def onJoin(self, details):
            print("session joined")

            cars = yield self.call(u"interchange.app.3b9d29f0-c054-4a04-9f0a-fbbfbb425eb3.vehicles")
            hist = []

            # RPC GET
            try:
                for car in cars:
                    data = yield self.call(u"interchange.vehicle." + car + ".state")
                    hist.append(data)
                    for i in range(0,100):
                        data = self.duplicate(data)
                        hist.append(data)
                #location_optimisation.preprocess(hist)
                print("call result: {}".format(hist))
            except Exception as e:
                print("call error: {0}".format(e))

            # SUB
            try:
                for car in cars:
                    subscription = yield self.subscribe(self.onCar, u'interchange.vehicle.' + car + '.stream')
                    print("Subscribed with subscription ID {}".format(subscription.id))
                print("call result: {}".format(hist))
            except Exception as e:
                print("call error: {0}".format(e))

            # ???
            #self.leave()

        def onLeave(self, details):
            print(details)
            print("session left")

        def onDisconnect(self):
            print("transport disconnected")

        @inlineCallbacks
        def onCar(self, data, timestamp, *args, **kwargs):
            print("timestamp: " + timestamp)
            print("data: {}".format(data))
            #location_optimisation.update(data)

        def duplicate(self, car):
            car2 = car.deepcopy()
            for v in car2['positioning_system']:
                v += 0.001
            return car2

    def start(self):
        runner = ApplicationRunner(url=u"wss://api.interchange.ericsson.net/v1", realm=u"interchange", debug=False)
        runner.run(self.Component)