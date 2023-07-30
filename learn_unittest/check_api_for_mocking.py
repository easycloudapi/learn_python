import requests


# def _call_api_genderize(name):
#     base_url = "https://api.genderize.io/"
#     params = dict()
#     params["name"] = name
#     # headers = {"Content-Type": ""}
#     response = requests.get(url=base_url, params=params)
#     out = response.json()
#     return out


# def _call_api_nationalize(name):
#     base_url = "https://api.nationalize.io/"
#     params = dict()
#     params["name"] = name
#     response = requests.get(url=base_url, params=params)
#     out = response.json()
#     return out


def _call_api_randomjoke():
    out = "no joke"
    base_url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url=base_url)
    if response.status_code == 200:
        out = response.json()
    else:
        raise Exception("No response from joke api")
    return out

def _get_only_joke():
    dict_obj = _call_api_randomjoke()
    only_joke = dict_obj["setup"] + ", " + dict_obj["punchline"]
    return only_joke


if __name__ == "__main__":
    # name = "indra"
    # out_genderize = _call_api_genderize(name)
    # out_nationalize = _call_api_nationalize(name)
    # print(f"out_genderize: {out_genderize}\nout_nationalize: {out_nationalize}")

    random_joke = _get_only_joke()
    print(f"random_joke: {random_joke}")
