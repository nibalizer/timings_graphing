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
    def __init__(self):
        self.name = "TimingsTracker"

    def handleEvent(self, event, replay):
        pass

    def handleUnitDoneEvent(self, event, replay):
        # print event.name
        # print event.unit
        if str(event.unit).startswith("CommandCenter"):
            # if event.frame != 0:
            f = [i for i in event.unit.owner.units if "Command" in str(i)]
            if len(f) < 3:
                print "Command Center Created"
                print event.frame, frame_to_time(event.frame)
                command_center_timings.append(event.frame)

    def handleControlGroupEvent(self, event, replay):
        pass


    def handleTargetAbilityEvent(self, event, replay):
        pass


if __name__ == "__main__":
    debug = False
    command_center_timings = []

    # find all replay files in 'replays' dir and add theem to an array
    replay_files = []
    error_replays = []
    for root, dirs, files in os.walk("replays"):
        path = root.split('/')
        for file in files:
            if file.endswith(".SC2Replay"):
                replay_files.append(root + "/" + file)
    if debug:
        print replay_files

    try:
        for file in replay_files:
            replay = sc2reader.load_replay(
                file,
                engine=sc2reader.engine.GameEngine(plugins=[
                    ContextLoader(),
                    APMTracker(),
                    TimingsTracker(),
                    SelectionTracker(),
                ])
            )
    except:
        error_replays.append(file)

    print command_center_timings
    if debug:
        print "Error replays found in: ", error_replays
