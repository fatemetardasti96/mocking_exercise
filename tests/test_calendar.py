from unittest.mock import Mock, patch
from datetime import datetime

from src.my_calendar import get_holidays, is_weekday
import src.my_calendar as my_calendar

@patch('src.my_calendar.datetime')
def test_is_weekday(mock_datetime):
    tuesday = datetime(year=2019, month=1, day=1)
   
    mock_datetime.today.return_value = tuesday
    
    assert is_weekday()

@patch('src.my_calendar.datetime')
def test_is_not_weekday(mock_datetime):
    saturday = datetime(year=2019, month=1, day=5)
    mock_datetime.today.return_value = saturday
    
    mock_datetime.today.return_value = saturday
    assert not is_weekday()    


@patch('src.my_calendar.requests')
def test_get_holidays(mock_get):
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"value": "hello mock"}
    
    mock_get.get.return_value = mock_resp
    
    assert get_holidays() == {"value": "hello mock"}
    

@patch('src.my_calendar.requests.get')
def test_no_holiday(mock_get):
    mock_get.return_value = Mock(status_code=404)
    assert get_holidays() == None