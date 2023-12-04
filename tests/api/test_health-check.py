import requests
BASE_URL = "http://localhost:8080"
HEALTH_CHECK_ENDPOINT = f"{BASE_URL}/health"


def test_health_check_endpoint():
    health_check_response = requests.get(HEALTH_CHECK_ENDPOINT)
    health_check_response_status_code = health_check_response.status_code
    assert health_check_response_status_code == 200, \
        f"Expected Status Code: 200\n" \
        f"Actual Status Code {health_check_response_status_code}"
