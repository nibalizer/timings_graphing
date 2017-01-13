
import sc2reader
from sc2reader.engine.plugins import ContextLoader, APMTracker
from sc2reader.engine.plugins import SelectionTracker
import time



class TimingsTracker():
    def __init__(self):
        self.name = "TimingsTracker"

    def handleEvent(self, event, replay):
        pass

    def handleUnitBornEvent(self, event, replay):
        #print event.name
        #print event.unit
        if str(event.unit).startswith("CommandCenter"):
            if event.frame != 0:
                print "Command Center Created"
                print event.frame

        pass

    def handleControlGroupEvent(self, event, replay):
        #print event.frame
        pass

        #time.sleep(0.1)

    def handleTargetAbilityEvent(self, event, replay):
        pass

# sc2reader.engine.register_plugin(Plugin1())
# sc2reader.engine.register_plugin(Plugin2())

replay = sc2reader.load_replay(
    'Innovation vs Stats map 1.SC2Replay',
    engine=sc2reader.engine.GameEngine(plugins=[
        ContextLoader(),
        APMTracker(),
        TimingsTracker(),
        SelectionTracker(),
    ])
)

