
function [] = DensityAltCalculator()
    %{
        The Density Altitude is calculated based on the weather data obtained from the API. 
        The necessary measurements are obtained from the weather data to determine the Density Altitude.
        It then prints out all of the data measurements used and prints out the density altitude.
    %}

    % API calls
    key = '7cab1fcaf444883263bc48dd983e6018';
    options = weboptions('ContentType','json');
    url=['https://api.openweathermap.org/data/2.5/weather?q=','Ames','&APPID=',key];
    weather_data = webread(url, options);

    current_temperature = weather_data.main.temp;
    current_pressure = weather_data.main.pressure;
    current_humidity = weather_data.main.humidity;

    % Calcuations from the API called variables
    temperature_C = current_temperature - 273.15;
    dew_point = temperature_C - ((100 - current_humidity) / 5);
    vapor_pressure = 6.11 * (10 ^ ((7.5 * dew_point) / (237.7 + dew_point)));
    virtual_temp_K = current_temperature / (1 - (vapor_pressure / current_pressure) * (1 - 0.622));
    virtual_temp_R = ((9 / 5) * (virtual_temp_K - 273.15) + 32) + 459.69;
    pressure_Hg = current_pressure * 0.02953;
    field_elevation = 955.6;
    density_alititude = field_elevation + (145366 * (1 - (((17.326 * pressure_Hg) / virtual_temp_R) ^ 0.235)));

    dashes = "----------------------------------------------------";

    fprintf("\nMeasurements data gathered from current weather data\n")
    disp(dashes)
    fprintf("Current Temperature : %f [K]", round(current_temperature, 2))
    fprintf("\nCurrent Temperature : %f [deg C]", round(temperature_C, 2))
    fprintf("\nCurrent Pressure    : %f [mbar]", round(current_pressure, 2))
    fprintf("\nCurrent Humidity    : %f [%]", round(current_humidity, 2))
    fprintf("\nDew Point           : %f [deg C]", round(dew_point, 2))
    fprintf("\nVapor Pressure      : %f [mbar]", round(vapor_pressure, 2))
    fprintf("\nVirtual Temperature : %f [K]", round(virtual_temp_K, 2))
    fprintf("\nVirtual Temperature : %f [deg R]", round(virtual_temp_R, 2))
    fprintf("\nPressure            : %f [in-Hg]", round(pressure_Hg, 2))
    fprintf("\nDensity Altitude    : %f [ft]\n", round(density_alititude, 2))
    disp(dashes)

end