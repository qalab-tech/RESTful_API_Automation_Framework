import requests


# /GET API Request
def get_api_request(api_url, uri, auth=None, params=None, headers=None):
    url = "{}{}".format(api_url, uri)
    try:
        response = requests.get(url, headers=headers, auth=auth, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        json_response = response.json() if 'application/json' in response.headers.get('Content-Type',
                                                                                      '') else response.text
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    return response.status_code, json_response


# /POST API Request:

def post_api_request(api_url, uri, auth=None, params=None, headers=None, payload=None):
    url = "{}{}".format(api_url, uri)
    try:
        response = requests.post(url, auth=auth, params=params, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses
        json_response = response.json() if 'application/json' in response.headers.get('Content-Type',
                                                                                      '') else response.text
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    return response.status_code, json_response


# /PUT API Request:

def put_api_request(api_url, uri, auth=None, params=None, headers=None, payload=None):
    url = "{}{}".format(api_url, uri)
    try:
        response = requests.put(url, auth=auth, params=params, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses
        json_response = response.json() if 'application/json' in response.headers.get('Content-Type',
                                                                                      '') else response.text
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    return response.status_code, json_response


# /DELETE TS API Request:

def delete_api_request(api_url, uri, auth=None, params=None, headers=None, payload=None):
    url = "{}{}".format(api_url, uri)
    try:
        response = requests.delete(url, auth=auth, params=params, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses
        json_response = response.json() if 'application/json' in response.headers.get('Content-Type',
                                                                                      '') else response.text
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    return response.status_code, json_response

