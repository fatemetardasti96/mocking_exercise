from unittest.mock import Mock, patch

from src.weather import WeatherReporter

def test_get_current_temp_from_weather_report():
    service = Mock()
    service.get_temperature.return_value = 7
    
    assert WeatherReporter(service).get_current_temperature('Berlin') == f"The current temperature in Berlin is 7 degrees Celsius."