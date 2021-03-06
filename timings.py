import os

import sc2reader
from sc2reader.engine.plugins import ContextLoader, APMTracker
from sc2reader.engine.plugins import SelectionTracker


def frame_to_time(frame):
    # note for future python3 work
    game_seconds = frame / 16

    minutes = game_seconds / 60
    seconds = game_seconds - (60 * minutes)
    return '{0}:{1:02d}'.format(minutes, seconds)


class TimingsTracker():
    def __init__(self, sup):
        self.name = "TimingsTracker"
        self.sup = sup

    def handleEvent(self, event, replay):
        pass

    def handleUnitTypeChangeEvent(self, event, replay):
        if event.unit.name == "Lair":
            # print "Lair Created"
            # print event.frame, frame_to_time(event.frame)
            self.sup.lair_timings.append(event.frame)

    def handleUnitDoneEvent(self, event, replay):
        # print event.name
        # print event.unit
        if str(event.unit).startswith("CommandCenter"):
            # if event.frame != 0:
            f = [i for i in event.unit.owner.units if "Command" in str(i)]
            if len(f) < 3:
                # print "Command Center Created"
                # print event.frame, frame_to_time(event.frame)
                self.sup.command_center_timings.append(event.frame)

        if str(event.unit).startswith("Nexus"):
            # if event.frame != 0:
            f = [i for i in event.unit.owner.units if "Nexus" in str(i)]
            if len(f) == 3:
                # print "Third Nexus Created, (", f, ")"
                # print event.frame, frame_to_time(event.frame)
                self.sup.third_nexus_timings.append(event.frame)

        if str(event.unit).startswith("SpawningPool"):
            # print "SpawningPool Created"
            # print event.frame, frame_to_time(event.frame)
            self.sup.spawning_pool_timings.append(event.frame)

    def handleControlGroupEvent(self, event, replay):
        pass

    def handleTargetAbilityEvent(self, event, replay):
        pass


class Analyzer():
    def __init__(self, debug=False):
        self.debug = debug
        self.command_center_timings = []
        self.spawning_pool_timings = []
        self.lair_timings = []
        self.third_nexus_timings = []

        # find all replay files in 'replays' dir and add theem to an array
        self.replay_files = []
        self.error_replays = []
        for root, dirs, files in os.walk("replays"):
            path = root.split('/')
            for file in files:
                if file.endswith(".SC2Replay"):
                    self.replay_files.append(root + "/" + file)
        if debug:
            print self.replay_files

    def process(self):
        try:
            for file in self.replay_files:
                replay = sc2reader.load_replay(
                    file,
                    engine=sc2reader.engine.GameEngine(plugins=[
                        ContextLoader(),
                        APMTracker(),
                        TimingsTracker(self),
                        SelectionTracker(),
                    ])
                )
        except:
            self.error_replays.append(file)

    def print_output(self):

        print "CC timings", self.command_center_timings
        print "pool timings", self.spawning_pool_timings
        print "lair timings", self.lair_timings
        print "third nexus timings", self.third_nexus_timings
        if self.debug:
            print "Error replays found in: ", self.error_replays
