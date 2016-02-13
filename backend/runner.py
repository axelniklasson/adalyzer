from autobahn.wamp import auth
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner


class Connection:

    def __init__(self):
        pass

    class Component(ApplicationSession):

        def __init__(self, config=None):
            ApplicationSession.__init__(self, config)
            print("component created")

        def onConnect(self):
            print("transport connected")
            self.join(self.config.realm)

        def onChallenge(self, challenge):
            print("authentication challenge received")
            if challenge.method == u"wampcra":
                signature = auth.compute_wcs(u"uSrnbKa2cjxkYu9Flom1ZMIkNYMriSZ5tKzlhVKJT6o".encode('utf8'), challenge.extra['challenge'].encode('utf8'))
                return signature.decode('ascii')
            else:
                raise Exception("don't know how to handle authmethod {}".format(challenge.method))

        @inlineCallbacks
        def onJoin(self, details):
            print("session joined")

            # RPC GET
            try:
                historical_cars = yield self.call(u"interchange.vehicle.235ca237-7f3e-4161-bb64-3804cb157a9d.state")
                print("call result: {}".format(historical_cars))
            except Exception as e:
                print("call error: {0}".format(e))

            # SUB
            #self.subscribe(self.watson.set_cars, u'com.myapp.topic1')

            # ???
            #self.leave()

        def onLeave(self, details):
            print("session left")

        def onDisconnect(self):
            print("transport disconnected")

    def start(self):
        extra = {
            "authmethods": ["wampcra"],
            "authid": "3b9d29f0-c054-4a04-9f0a-fbbfbb425eb3"
        }
        runner = ApplicationRunner(url=u"wss://api.interchange.ericsson.net/v1", realm=u"interchange", extra=extra, debug=False)
        runner.run(self.Component)
