from tkinter import *
from time import *
import threading
import locale
import time
import requests


degree_sign = u'\N{DEGREE SIGN}'

LOCALE_LOCK = threading.Lock()

def read_weather_key():
    with open('weather-key.txt', 'r') as read1:
        lines = read1.readlines()
        return lines[0].strip()

def read_steam_key():
    with open('steam-key.txt', 'r') as read2:
        lines = read2.readlines()
        return lines[0].strip()

def read_location():
    with open('location.txt', 'r') as read3:
        lines = read3.readlines()
        return lines[0].strip()

def read_steam_id():
    with open('steam-id.txt', 'r') as read4:
        lines = read4.readlines()
        return lines[0].strip()

weather_key = read_weather_key()
steam_key = read_steam_key()
location = read_location()
steam_id = read_steam_id()

def setlocale(name):
    with LOCALE_LOCK:
        saved = locale.setlocale(locale.LC_ALL)
        try:
            yield locale.setlocale(locale.LC_ALL, name)
        finally:
            locale.setlocale(locale.LC_ALL, saved)


class Time_and_Day(Frame):

    def __init__(self, master):
        Frame.__init__(self, master, background="BLACK")
        self.time1 = ""
        self.label_time = Label(self, font="dreams 40", bg="BLACK", fg="WHITE")
        self.label_time.pack(side=TOP, anchor="e")
        
        self.day1 = ""
        self.label_day = Label(self, font="dreams 28", bg="BLACK", fg="WHITE")
        self.label_day.pack(side=TOP, anchor="e")
        
        self.day_of_the_week1 = ""
        self.label_day_of_the_week = Label(self, font="dreams 28", bg="BLACK", fg="WHITE")
        self.label_day_of_the_week.pack(side=TOP, anchor="e")
        
        self.update_time()
        
    def update_time(self):
        time2 = strftime("%I:%M:%S %p")
        day2 =  strftime("%B %d, %Y")
        day_of_the_week2 = strftime("%A")
        if self.time1 != time2:
            self.time1 = time2
            self.label_time.config(text=time2)
        if self.day1 != day2:
            self.day1 = day2
            self.label_day.config(text=day2)
        if self.day_of_the_week1 != day_of_the_week2:
            self.day_of_the_week1 = day_of_the_week2
            self.label_day_of_the_week.config(text=day_of_the_week2)
        self.after(200, self.update_time)

class Weather(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, background="BLACK")
        
        self.temperature1 = ""
        self.label_temperature = Label(self, font="dreams 45", bg="BLACK", fg="WHITE")
        self.label_temperature.pack(side=TOP, anchor="w")
        
        self.description1 = ""
        self.label_description = Label(self, font = "dreams 15", bg="BLACK", fg="WHITE")
        self.label_description.pack(side=TOP, anchor="w")
        
        self.precipitation1 = ""
        self.label_precipitation = Label(self, font="dreams 13", bg="BLACK", fg="WHITE")
        self.label_precipitation.pack(side=TOP, anchor="w")
        
        self.extra_description1 = ""
        self.label_extra_description = Label(self, font = "dreams 10", bg="BLACK", fg="WHITE")
        self.label_extra_description.pack(side=TOP, anchor="w")
        
        self.no_weather_data1 = "Error, I will try to fix this"
        self.label_no_weather_data = Label(self, font="dreams 10", bg="BLACK", fg="WHITE")
        self.label_no_weather_data.pack(side=TOP, anchor="w")
        
        self.update_weather()
        
    def update_weather(self):
        url_weather = "https://api.apixu.com/v1/forecast.json?key=" + weather_key + "&q=" + location
        weather_get = requests.get(url_weather)
        if weather_get.status_code == 200:
            weather = weather_get.json()
            
            temperature2 = str(weather['current']['temp_f'])
            description2 = str(weather['current']['condition']['text'])
            precipitation2 = str(weather['forecast']['forecastday'][0]['day']['totalprecip_mm'])
            extra_description2 = str(weather['forecast']['forecastday'][0]['day']['condition']['text'])
            
            if self.temperature1 != temperature2:
                self.temperature1 = temperature2
                self.label_temperature.config(text=temperature2 + degree_sign)
            if self.description1 != description2:
                self.description1 = description2
                self.label_description.config(text=description2)
            if self.precipitation1 != precipitation2:
                self.precipitation1 = precipitation2
                self.label_precipitation.config(text=precipitation2 + " mm of precip.!")
            if self.extra_description1 != extra_description2:
                self.extra_description2 = extra_description2
                self.label_extra_description.config(text=extra_description2)

        else:
            self.label_no_weather_data.config(text=self.no_weather_data1)
        self.after(600000, self.update_weather)
        
class Alert(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, background="BLACK")
        
        self.alert1 = ""
        self.label_alert = Label(self, font="dreams 25", bg="BLACK", fg="WHITE")
        self.label_alert.pack(side=TOP)
        
        self.update_alert()
    def update_alert(self):
        url_alert = "https://api.apixu.com/v1/forecast.json?key=" + weather_key + "&q=" + location
        alert_get = requests.get(url_alert)
        if alert_get.status_code == 200:
            alert = alert_get.json()
            try:
                full_alert = str(alert['alert']['headline'])
                alert2 = full_alert.replace("at", "\nat")
                if self.alert1 != alert2:
                    self.alert1 = alert2
                    self.label_alert.config(text=alert2)
                
            except:
                pass

        else:
            pass
        self.after(600000, self.update_alert)
class CSGO_STATS(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, background="BLACK")
        
        self.headshots1 = ""
        self.label_headshots = Label(self, font="dreams 20", bg="BLACK", fg="WHITE")
        self.label_headshots.pack(side=BOTTOM, anchor="w")
        
        self.wins1 = ""
        self.label_wins = Label(self, font="dreams 20", bg="BLACK", fg="WHITE")
        self.label_wins.pack(side=BOTTOM, anchor="w")
        
        self.kills1 = ""
        self.deaths1 = ""
        self.kill_death_ratio1 = ""
        self.label_kill_death_ratio = Label(self, font="dreams 20", bg="BLACK", fg="WHITE")
        self.label_kill_death_ratio.pack(side=BOTTOM, anchor="w")
        
        self.no_stats1 = ""
        self.label_no_stats = Label(self, font="dreams 20", bg="BLACK", fg="WHITE")
        self.label_no_stats.pack(side=BOTTOM, anchor="w")
        
        self.label_csgo_title = Label(self, text="Your CS:GO stats:", font="dreams 20", bg="black", fg="WHITE")
        self.label_csgo_title.pack(side=BOTTOM, anchor="w")
        
        self.update_stats()
    
    def update_stats(self):
        url_stats = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=" + steam_key + "&steamid=" + steam_id
        stats_get = requests.get(url_stats)
        if stats_get.status_code == 200:
            stats = stats_get.json()
            kills2 = stats['playerstats']['stats'][0]['value']
            deaths2 = stats['playerstats']['stats'][1]['value']
            kill_death_ratio2 = str(round(kills2/deaths2, 4))
            wins2 = str(stats['playerstats']['stats'][5]['value'])
            headshots2 = str(stats['playerstats']['stats'][24]['value'])
            
            if self.kills1 != kills2 or self.deaths1 != deaths2 or self.kill_death_ratio1 != kill_death_ratio2:
                self.kills1 = kills2
                self.deaths1 = deaths2
                self.kill_death_ratio1 = kill_death_ratio2
                self.label_kill_death_ratio.config(text="K's: " + str(kills2) + "  D's: " + str(deaths2) + "  K/D: " + kill_death_ratio2)
                
            if self.wins1 != wins2:
                self.wins1 = wins2
                self.label_wins.config(text="You have a total of " + wins2 + " wins! ")
            if self.headshots1 != headshots2:
                self.headshots1 = headshots2
                self.label_headshots.config(text="You have " + headshots2 + " heashots!")
        else:
            no_stats2 = "Unfortunately, I cannot get that information at the moment. I will tell you as quick as I can!"
            self.label_no_stats.config(text=no_stats2)
        self.after(5000, self.update_stats)
        
class Final:
    def __init__(self):
        self.root = Tk()
        self.root.configure(bg="BLACK")
        self.state = False
        
        self.top = Frame(self.root, bg="BLACK")
        self.top.pack(side=TOP, fill=BOTH)
        self.bottom = Frame(self.root, bg="BLACK")
        self.bottom.pack(side=BOTTOM, fill=BOTH)
        
        self.time = Time_and_Day(self.top)
        self.time.pack(side=RIGHT, anchor=N, pady=60)
        
        self.weather_show = Weather(self.top)
        self.weather_show.pack(side=LEFT, anchor=N, padx=50, pady=60)
        
        self.greeting = Label(self.root, text="Hello Sreekara", font="Arial 65", bg="BLACK", fg="WHITE")
        self.greeting.pack(pady=375)
        
        self.alert_show = Alert(self.root)
        self.alert_show.pack(padx=100)
        
        self.stats_show = CSGO_STATS(self.bottom)
        self.stats_show.pack(side=LEFT, anchor=S, padx=50, pady=60)
        
        self.root.bind("<Return>", self.toggle_fullscreen)
        self.root.bind("<Escape>", self.end_fullscreen)
        
        self.root.mainloop()
    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.root.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.root.attributes("-fullscreen", False)
        return "break"
if __name__ == "__main__":
    start = Final()
    start.root.mainloop()
