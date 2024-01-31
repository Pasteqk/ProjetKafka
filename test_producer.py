import pytest
from producer import send_gps_data

def test_gps_data_format():
    data = send_gps_data('IP1')
    assert 'ip' in data
    assert -90 <= data['latitude'] <= 90
    assert -180 <= data['longitude'] <= 180
    assert isinstance(data['timestamp'], float)
