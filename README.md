# Simple Python Weather App
Program enables user to search basic weather conditions all over the globe.

## Cautions
Do not separate files from its primary folder since, for example, graphical assets are sourced from `/images` folder, thus any modification of the paths might result in errors or may prevent the app form running.
Its worth to mention that an Internet connection has to be established in order to use the app properly.

If you want to use this app, unfortunately, you have to generate your own API key from `https://openweathermap.org/current` and paste it into `.env` file, assign it to `APIkey` variable.

## Manual installation, set-up
To directly run the app from source, you will need to run following commands:
```
$ git clone https://github.com/mieszkoP13/weatherAPP && cd weatherAPP
$ pip3 install -r requirements.txt
$ python3 main.py
```

## Used technologies, modules, programs
Open Weather Map API
  SQLite database for storing weather search history
  Numerous Python modules for geolocation, time, date, GUI, security etc.
