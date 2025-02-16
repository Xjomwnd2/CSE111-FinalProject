# test_weather_data.py
import pytest
from weather_data import parse_weather_data, format_weather_report
from datetime import datetime
@pytest.fixture
def sample_weather_data():
    return {
        "name": "London",
        "main": {
            "temp": 15.7,
            "humidity": 76
        },
        "weather": [
            {
                "description": "scattered clouds"
            }
        ],
        "wind": {
            "speed": 3.6
        },
        "dt": 1645564800  # Example timestamp
    }
def test_parse_weather_data(sample_weather_data):
    """Test that weather data is parsed correctly"""
    result = parse_weather_data(sample_weather_data)
    
    assert result["city"] == "London"
    assert result["temperature"] == 15.7
    assert result["humidity"] == 76
    assert result["description"] == "scattered clouds"
    assert result["wind_speed"] == 3.6
    assert isinstance(result["timestamp"], str)
def test_parse_weather_data_invalid():
    """Test parsing with invalid data"""
    invalid_data = {"name": "London"}  # Missing required fields
    result = parse_weather_data(invalid_data)
    assert result is None
def test_format_weather_report():
    """Test weather report formatting"""
    parsed_data = {
        "city": "London",
        "temperature": 15.7,
        "humidity": 76,
        "description": "scattered clouds",
        "wind_speed": 3.6,
        "timestamp": "2024-02-09 12:00:00"
    }
    
    result = format_weather_report(parsed_data)
    
    assert "London" in result
    assert "15.7°C" in result
    assert "76%" in result
    assert "Scattered clouds" in result
    assert "3.6 m/s" in result
    assert "2024-02-09 12:00:00" in result
def test_format_weather_report_invalid():
    """Test formatting with invalid data"""
    result = format_weather_report(None)
    assert "Unable to generate weather report" in result

