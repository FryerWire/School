
"""
Project 1: Question 2
Maxwell Seery
"""

import requests

API_KEY = "&APPID=7cab1fcaf444883263bc48dd983e6018"

url = "https://api.openweathermap.org/data/2.5/weather?q=Ames&APPID=7cab1fcaf444883263bc48dd983e6018"

# API calls
weather_data = requests.get(url).json()
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
print(f"Dew Point           : {round(dew_point, 5)} [deg C]")
print(f"Vapor Pressure      : {round(vapor_pressure, 5)} [mbar]")
print(f"Virtual Temperature : {round(virtual_temp_K, 5)} [K]")
print(f"Virtual Temperature : {round(virtual_temp_R)} [R]")
print(f"Pressure            : {round(pressure_Hg)} [in-Hg]")
print(f"Density Altitude    : {round(density_alititude)} [ft]")
print(52 * '-')




