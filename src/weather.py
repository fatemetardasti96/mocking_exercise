class WeatherService:
    def get_temperature(self, city):
        # Simulate fetching temperature data from an external service
        # In a real scenario, this would make an API call to a weather service
        raise NotImplementedError("This method should be implemented in a real WeatherService")


class WeatherReporter:
    def __init__(self, weather_service):
        self.weather_service = weather_service

    def get_current_temperature(self, city):
        temperature = self.weather_service.get_temperature(city)
        return f"The current temperature in {city} is {temperature} degrees Celsius."
