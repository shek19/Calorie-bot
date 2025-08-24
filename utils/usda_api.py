import requests
from config import USDA_API_KEY,BASE_URL

def search_food(query, page_size=1):
    """
    Search for food items in the USDA database.
    """

    url = f"{BASE_URL}/foods/search"
    params = {
        "api_key" : USDA_API_KEY,
        "query" : query,
        "pageSize" : page_size
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if "foods" not in data or len(data["foods"]) == 0:
        return None
    
    foods = data["foods"][0]

    nutrients = {}

    if "foodNutrients" in foods:
        for n in foods["foodNutrients"]:
            name = n.get("nutrientName")
            value = n.get("value")
            unit = n.get("unitName")

            if name and value:
                nutrients[name] = f"{value} {unit}"
    
    return {
        "description": foods.get("description", "Unknown"),
        "fdcId": foods.get("fdcId"),
        "nutrients": nutrients
    }

    