def prepare_text_weather_forecast_message(municipality_name, three_day_forecast):
    messaggio = "Previsioni per " + municipality_name + ":\n\n" + three_day_forecast[0][0] + ":\n" + three_day_forecast[0][1] + "\n" + "Tmin:" + str(three_day_forecast[0][2]) + "°C Tmax:" + str(three_day_forecast[0][3]) + "°C\n\n" + three_day_forecast[1][0] + ":\n" + three_day_forecast[1][1] + "\n" + "Tmin:" + str(
        three_day_forecast[1][2]) + "°C Tmax:" + str(three_day_forecast[1][3]) + "°C\n\n" + three_day_forecast[2][0] + ":\n" + three_day_forecast[2][1] + "\n" + "Tmin:" + str(three_day_forecast[2][2]) + "°C Tmax:" + str(three_day_forecast[2][3]) + "°C\n\n"
    return messaggio
