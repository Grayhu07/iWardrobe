import urllib2, json
class Struct:
    def __init__(self, ctype, temprature, wind):
        self.ctype = ctype
        self.temperature = temprature
        self.wind = wind
    def evaluate(self):
        if self.temperature >= 77:
            choose.append(self.ctype[0])
            choose.append(self.ctype[6])
        elif 59 <  self.temperature < 77:
            choose.append(self.ctype[1])
            choose.append(self.ctype[6])
        elif 50 < self.temperature <= 59:
            choose.append(self.ctype[2])
            choose.append(self.ctype[5])
        elif 40 < self.temperature <= 50:
            choose.append(self.ctype[4])
            choose.append(self.ctype[5])
        else:
            choose.append(self.ctype[3])
            choose.append(self.ctype[5])
    def weather(self):
        mirror.append(self.temperature)
        mirror.append(self.wind)

if __name__ == "__main__":
    apikey = raw_input("Please input your API Key: ")
    key = raw_input("Please input your Zip Code: ")
    forecast_url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/" + key + "?apikey=" + apikey + "&details=true"
    respond = urllib2.Request(forecast_url)
    data = json.loads(urllib2.urlopen(respond).read())
    text_forecast = data["Headline"]["Text"]
    highest_temp = data["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]
    lowest_temp = data["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]
    day_text = data["DailyForecasts"][0]["Day"]["IconPhrase"]
    night_text = data["DailyForecasts"][0]["Night"]["IconPhrase"]
    wind_index = data["DailyForecasts"][0]["Day"]["Wind"]["Speed"]["Value"]

    location_url = "http://dataservice.accuweather.com/locations/v1/postalcodes/search?" + "apikey=" + apikey + "&q=" + key
    res_location = urllib2.Request(location_url)
    location = json.loads(urllib2.urlopen(res_location).read())
    name = location[0]["ParentCity"]["EnglishName"]
    print (
        "\nHeadline in " + name + " is: " + text_forecast +
        "\nThe Highest will be: " + str(highest_temp) + " F" +
        "\nThe Lowest will be: " + str(lowest_temp) + " F"
                                                      "\nThe Day will be: " + day_text +
        "\nThe Night will be: " + night_text +
        "\nWind: " + str(wind_index) + " " + data["DailyForecasts"][0]["Day"]["Wind"]["Speed"]["Unit"]
    )

    handler = urllib2.urlopen(respond)

    choose = []
    mirror = []
    ctype = ["T-shirt","Long-Sleeve Shirt", "Sweater", "Coat", "Jacket", "Trouser", "Shorts"]
    mid_temp = (highest_temp + lowest_temp) / 2
    closet = Struct(ctype, mid_temp, wind_index)
    closet.evaluate()
    print(
        "\nYou should wear " + choose[0] + " and " + choose[1]
    )