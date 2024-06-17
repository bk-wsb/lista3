import requests


def test_api(endpoint, expected_keys):
    url = f"https://my-json-server.typicode.com/bk-wsb/lista3/{endpoint}"
    try:
        response = requests.get(url)
        status_code = response.status_code

        if status_code != 200:
            return f"Test {endpoint}: FAILED (Status Code {status_code})"

        json_data = response.json()

        for key in expected_keys:
            if key not in json_data:
                return f"Test {endpoint}: FAILED (Missing key '{key}')"

        return f"Test {endpoint}: PASSED"

    except requests.RequestException as e:
        return f"Test {endpoint}: FAILED (Request Exception: {str(e)})"


def main():
    tests = [
        ("posts/1", ["userId", "id", "title", "body"]),
        ("comments/1", ["postId", "id", "name", "email", "body"]),
        ("users/1", ["id", "name", "username", "email"]),
    ]

    for endpoint, expected_keys in tests:
        result = test_api(endpoint, expected_keys)
        print(result)


if __name__ == "__main__":
    main()