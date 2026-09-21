def build_request(Hero_name):
    return {
        "endpoint": "/hero",
        "query": {
            "name": Hero_name
        }
    }

def choose_display_values(respone_data):
    current = respone_data["current"]
    return {
        "name": current["name"],
        "power": current["power"],
        "speed": current["speed"]
    }

request_data = build_request("Sonic_the_Hedgehog")
simulated_response = {
    "current": {
        "name": "Sonic_the_Hedgehog",
        "power": 95, 
        "speed": "343 m/s"
    }
}

display_values = choose_display_values(simulated_response)  
print("request_endpoint:", request_data["endpoint"])
print("query_name:", request_data["query"]["name"])
print("selected values", display_values)