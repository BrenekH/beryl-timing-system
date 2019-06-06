import time

# timing_periods = ["auto", "teleop", "endgame"]
# timing_periods_details = {
#   "auto": {
#       "time": int("seconds"),
#       "start_sound": "path_to_file", 
#       "background_color": (r, g, b), 
#       "foreground_color": (r, g, b)}}
# early_stop_sound = "path_to_file"
# idle_period_details = {
#     "text": "",
#     "background_color": (),
#     "foreground_color": ()
# }

class Timer:
    def __init__(self):
        self.timing_periods = []
        self.timing_periods_details = {}
        self.idle_period_details = {}
        self.early_stop_sound = None

        self.__start_time = None
        self.__seconds_left = None
        self.__loops = None

    def start(self):
        self.__start_time = time.time()

    def stop(self):
        pass

    def get_status(self):
        # Return background and foreground colors, and text to display
        pass

    def load_settings(self):
        # Load the timing periods from the config
        # TODO: Actually load from a config file
        self.timing_periods = ["Autonomous", "Teleop", "End"]
        self.timing_periods_details = {
            "Autonomous": {
                "time": 30,
                "start_sound": "",
                "background_color": (0, 0, 0),
                "foreground_color": (0, 0, 0)
            },
            "Teleop": {
                "time": 120,
                "start_sound": "",
                "background_color": (0, 0, 0),
                "foreground_color": (0, 0, 0)
            },
            "End": {
                "time": 30,
                "start_sound": "",
                "background_color": (0, 0, 0),
                "foreground_color": (0, 0, 0)
            }
        }
        self.idle_period_details = {
            "text": "OFF",
            "background_color": (0, 255, 0),
            "foreground_color": ()
        }
        return self