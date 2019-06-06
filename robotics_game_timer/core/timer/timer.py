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
        self.stop_sound = None

        self.timer_running = False

        self._period_start_time = None
        self._seconds_left = None
        self._loops = None
        self._current_period_index = None

    def start(self):
        self._period_start_time = int(time.time())
        self.timer_running = True
        self._loops = len(self.timing_periods)

    def stop(self):
        self.timer_running = False

        self._period_start_time = None
        self._seconds_left = None
        self._loops = None
        self._current_period_index = None

    def get_status(self):
        # Return background and foreground colors, and text to display
        seconds_elapsed = int(time.time()) - self._period_start_time
        if seconds_elapsed >= self.timing_periods_details[self.timing_periods[self._current_period_index]]["time"]:
            # Progress to the next period or end the timer
            if self._current_period_index + 1 == self._loops:
                pass
        
        if self.timer_running:
            self._seconds_left = self.timing_periods_details[self.timing_periods[self._current_period_index]]["time"] - seconds_elapsed
            return (
                str(self._seconds_left),
                self.timing_periods_details[self.timing_periods[self._current_period_index]]["background_color"],
                self.timing_periods_details[self.timing_periods[self._current_period_index]]["foreground_color"])
        else:
            return (self.idle_period_details["text"], self.idle_period_details["background_color"], self.idle_period_details["foreground_color"])

    def load_settings(self):
        # Load the timing periods from the config
        # TODO: Actually load from a config file
        self.timing_periods = ["AUTONOMOUS", "TELEOP", "END GAME"]
        self.timing_periods_details = {
            "AUTONOMOUS": {
                "time": 30,
                "start_sound": "",
                "background_color": (255, 0, 0),
                "foreground_color": (0, 0, 0)
            },
            "TELEOP": {
                "time": 120,
                "start_sound": "",
                "background_color": (255, 0, 0),
                "foreground_color": (0, 0, 0)
            },
            "END GAME": {
                "time": 30,
                "start_sound": "",
                "background_color": (255, 255, 0),
                "foreground_color": (0, 0, 0)
            }
        }
        self.idle_period_details = {
            "text": "OFF",
            "background_color": (0, 255, 0),
            "foreground_color": (0, 0, 0)
        }
        return self