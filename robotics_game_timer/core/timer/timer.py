import time, pygame, json
from pathlib import Path
from ast import literal_eval

class Timer:
    def __init__(self):
        self.timing_periods = []
        self.timing_periods_details = {}
        self.idle_period_details = {}
        self.early_stop_sound = None
        self.stop_sound = None

        self.timer_running = False

        self._period_start_time = 0
        self._seconds_left = None
        self._loops = None
        self._current_period_index = 0

    def start(self):
        self._period_start_time = int(time.time())
        self.timer_running = True
        self._loops = len(self.timing_periods)
        self._current_period_index = 0
        self.timing_periods_details[self.timing_periods[self._current_period_index]]["start_sound"].play()

    def stop(self, early=True):
        self.timer_running = False

        self._period_start_time = 0
        self._seconds_left = None
        self._loops = None
        self._current_period_index = 0

        if early:
            # Play the stop early sound
            self.early_stop_sound.play()
        else:
            # Play the stop sound 
            self.stop_sound.play()

    def get_status(self):
        # Return background and foreground colors, and text to display
        if self.timer_running:
            seconds_elapsed = int(time.time()) - self._period_start_time
            if seconds_elapsed >= self.timing_periods_details[self.timing_periods[self._current_period_index]]["time"]:
                # Progress to the next period or end the timer
                if self._current_period_index + 1 == self._loops:
                    self.stop(early=False)
                else:
                    self._current_period_index += 1
                    self._period_start_time = int(time.time())
                    self.timing_periods_details[self.timing_periods[self._current_period_index]]["start_sound"].play()
                    
            self._seconds_left = self.timing_periods_details[self.timing_periods[self._current_period_index]]["start_time"] - seconds_elapsed
            return (
                self.timing_periods[self._current_period_index],
                str(self._seconds_left),
                self.timing_periods_details[self.timing_periods[self._current_period_index]]["background_color"],
                self.timing_periods_details[self.timing_periods[self._current_period_index]]["foreground_color"])
        else:
            return (self.idle_period_details["text"], "", self.idle_period_details["background_color"], self.idle_period_details["foreground_color"])

    def ready_timer(self, config_file_name="default.json"):
        self.load_settings(config_file_name=config_file_name)
        self.load_sounds()
        return self

    def load_sounds(self):
        pygame.mixer.init()
        # Stop sounds
        self.early_stop_sound = pygame.mixer.Sound(str(Path(self.early_stop_sound)))
        self.stop_sound = pygame.mixer.Sound(str(Path(self.stop_sound)))

        # Timing period sounds
        for x in range(len(self.timing_periods)):
            try:
                self.timing_periods_details[self.timing_periods[x]]["start_sound"] = pygame.mixer.Sound(
                    str(Path(self.timing_periods_details[self.timing_periods[x]]["start_sound"])))
            except pygame.error:
                print(f"{self.timing_periods_details[self.timing_periods[x]]['start_sound']} was not able to be loaded.")
        print("Timer sounds loaded")

    def load_settings(self, config_file_name="default.json"):
        # Load the timing periods from the configuration file

        json_file = json.load(open(Path(f"configs/timer/{config_file_name}")))

        for period in json_file["timing_periods"]:
            self.timing_periods.append(period["name"])

            period_dict = {}

            for detail in period:
                if not detail == "name":
                    if "color" in detail:
                        period_dict[detail] = literal_eval(period[detail])
                    else:
                        period_dict[detail] = period[detail]

            self.timing_periods_details[period["name"]] = period_dict

        self.idle_period_details = {
            "text": json_file["idle_period"]["text"],
            "background_color": literal_eval(json_file["idle_period"]["background_color"]),
            "foreground_color": literal_eval(json_file["idle_period"]["foreground_color"])
        }
        self.early_stop_sound = json_file["early_stop_sound"]
        self.stop_sound = json_file["stop_sound"]
        return self