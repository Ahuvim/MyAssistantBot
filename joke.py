import requests
from random import choice

def joke(user_input,res):


    num_jokes = res["total_jokes"]
    results = res["results"]
    if num_jokes > 1:
        return choice(results)["joke"]
    elif num_jokes == 1:
        return results[0]["joke"]
    else:
        return f"There is no joke about {user_input}"

