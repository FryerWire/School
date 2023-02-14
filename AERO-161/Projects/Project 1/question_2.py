
"""
Project 1: Question 2
Maxwell Seery
"""

import requests

API_KEY = "&APPID=7cab1fcaf444883263bc48dd983e6018"
URL = "https://api.openweathermap.org/data/2.5/weather?q=Ames&APPID=7cab1fcaf444883263bc48dd983e6018"

def change_the_name_of_this_function():
    """
    The Density Altitude is calculated based on the weather data obtained from the API. 
    The necessary measurements are obtained from the weather data to determine the Density Altitude.

    It then prints out all of the data measurements used and prints out the density altitude.
    """
    # API calls
    weather_data = requests.get(URL).json()
    current_temperature = weather_data.get("main").get("temp")
    current_pressure = weather_data.get("main").get("pressure")
    current_humidity = weather_data.get("main").get("humidity")

    # Calcuations from the API called variables
    temperature_C = current_temperature - 273.15
    dew_point = temperature_C - ((100 - current_humidity) / 5)
    vapor_pressure = 6.11 * (10 ** ((7.5 * dew_point) / (237.7 + dew_point)))
    virtual_temp_K = current_temperature / (1 - (vapor_pressure / current_pressure) * (1 - 0.622))
    virtual_temp_R = ((9 / 5) * (virtual_temp_K - 273.15) + 32) + 459.69
    pressure_Hg = current_pressure * 0.02953
    field_elevation = 955.6
    density_alititude = field_elevation + (145366 * (1 - (((17.326 * pressure_Hg) / virtual_temp_R) ** 0.235)))

    print(f"\nMeasurements data gathered from current weather data")
    print(52 * '-')
    print(f"Current Temperature : {round(current_temperature, 2)} [K]")
    print(f"Current Temperature : {round(temperature_C, 2)} [deg C]")
    print(f"Current Pressure    : {round(current_pressure, 2)} [mbar]")
    print(f"Current Humidity    : {round(current_humidity, 2)} [%]")
    print(f"Dew Point           : {round(dew_point, 2)} [deg C]")
    print(f"Vapor Pressure      : {round(vapor_pressure, 2)} [mbar]")
    print(f"Virtual Temperature : {round(virtual_temp_K, 2)} [K]")
    print(f"Virtual Temperature : {round(virtual_temp_R, 2)} [deg R]")
    print(f"Pressure            : {round(pressure_Hg, 2)} [in-Hg]")
    print(f"Density Altitude    : {round(density_alititude, 2)} [ft]")
    print(52 * '-')

change_the_name_of_this_function()


