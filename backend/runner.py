from autobahn.wamp import auth
from asyncio import coroutine
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner


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

        @coroutine
        def onJoin(self, details):
            print("session joined")

            # RPC GET
            try:
                historical_cars = yield from self.call(u"interchange.app.3b9d29f0-c054-4a04-9f0a-fbbfbb425eb3.vehicles")
                hist = []
                for car in historical_cars:
                    info = yield from self.call(u"interchange.vehicle." + car + ".state")
                    hist.append(info)
                print("call result: {}".format(hist))
            except Exception as e:
                print("call error: {0}".format(e))

            # SUB
            self.subscribe(self.onCar, u'interchange.vehicle.be26169d-be28-44fe-834b-568a7780758a.stream')

            # ???
            #self.leave()

        def onLeave(self, details):
            print(details)
            print("session left")

        def onDisconnect(self):
            print("transport disconnected")

        def onCar(self, data=None):
            try:
                print("hej")
                print(data)
            except Exception as e:
                print("call error: {0}".format(e))

    def start(self):
        runner = ApplicationRunner(url=u"wss://api.interchange.ericsson.net/v1", realm=u"interchange", debug=False)
        runner.run(self.Component)
