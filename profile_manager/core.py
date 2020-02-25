import datetime
import os

import ephem
import twitter


class ProfileManager:
    def __init__(self):
        CK, CSK = os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET_KEY"]
        AT, ATS = os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"]
        NAME = os.environ["SCREEN_NAME"]

        self.api = twitter.Api(
            consumer_key=CK, consumer_secret=CSK,
            access_token_key=AT, access_token_secret=ATS
        )
        self.user = self.api.GetUser(screen_name=NAME)
        self.location = self.user.location

    def update_moon(self):
        tokyo = ephem.city("Tokyo")
        tokyo.date = datetime.datetime.now().replace(
            hour=20, minute=0, second=0, microsecond=0
        )
        age = tokyo.date - ephem.previous_new_moon(tokyo.date)
        moon_chr = self.calc_moon(age)
        self.update_profile(moon_chr)

    def delete_location_moon(self):
        if self.location[-1] in [
                "🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘", "🌛", "🌜"]:
            self.location = self.location[:-1]

    def update_profile(self, moon_chr):
        self.delete_location_moon()
        if moon_chr is not None:
            self.location += moon_chr
        self.api.UpdateProfile(location=self.location)

    def calc_moon(self, n):
        age = int(n)
        if age == 0:
            text = "🌑"  # 新月
        elif age == 3:
            text = "🌒"  # 三日月
        elif 5 <= age <= 6:
            text = "🌛"
        elif age == 7:
            text = "🌓"  # 上弦の月
        elif 13 <= age <= 14:
            text = "🌔"  # 十三夜月
        elif age == 15:
            text = "🌕"  # 満月
        elif 16 <= age <= 17:
            text = "🌖"  # 寝待月
        elif age == 22:
            text = "🌗"  # 下弦の月
        elif 23 <= age <= 24:
            text = "🌜"
        elif age == 26:
            text = "🌘"  # 有明月
        else:
            text = None
        return text
