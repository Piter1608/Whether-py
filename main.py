import eel
import pyowm

owm = pyowm.OWM("4fb93515287d980c29ab520ea5c514d4")

@eel.expose
def get_weather(place):  
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)
    w = observation.weather

    temp = w.temperature('celsius')['temp']
    
    return "В місті  "+ city +" зараз " + str(temp) +" градусів"



#eel.init("web")

#eel.start("main.html",size=(700,700))
