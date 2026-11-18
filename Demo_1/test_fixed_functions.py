from buggy_functions import (
    average_response_time,
    format_alert_summary,
    get_alert_owner,
)


def test_format_alert_summary_with_integer_count():
    assert format_alert_summary(3, "critical") == "There are 3 critical alerts active."


def test_format_alert_summary_with_zero_count():
    assert format_alert_summary(0, "critical") == "There are 0 critical alerts active."


def test_get_alert_owner_with_known_team():
    assert get_alert_owner({"id": 5, "owner": "db-team"}, {"db-team": "Asha Patel"}) == "Asha Patel"


def test_get_alert_owner_with_unknown_team():
    assert get_alert_owner({"id": 5, "owner": "network-team"}, {"db-team": "Asha Patel"}) == "Unassigned"


def test_average_response_time_with_empty_list():
    result = average_response_time([])
    assert result == 0.0
    assert isinstance(result, float)


def test_average_response_time_with_values():
    assert average_response_time([1, 2, 3]) == 2.0