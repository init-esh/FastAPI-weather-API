from services import openweather_service as ows
from models.validation_error import ValidationError
import pytest
def test_validate_units():
    assert ows.validate_units("Delhi", "DL", "", "metric") == ("delhi", "dl", "us", "metric")
    assert ows.validate_units("Delhi", "DL", "IN", "standard") == ("delhi", "dl", "in", "standard")
    with pytest.raises(ValidationError):
        ows.validate_units("Delhi", "DL", "IN", "random")
    

