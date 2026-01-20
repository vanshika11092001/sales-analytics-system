def fetch_product_info(product_id):
    mock_api_data = {
        "P101": {"category": "Laptop"},
        "P102": {"category": "Accessories"},
        "P103": {"category": "Accessories"},
        "P104": {"category": "Monitor"},
        "P105": {"category": "Accessories"},
        "P106": {"category": "Audio"},
        "P107": {"category": "Cables"},
        "P108": {"category": "Storage"},
        "P109": {"category": "Accessories"},
        "P110": {"category": "Chargers"}
    }
    return mock_api_data.get(product_id, {"category": "Unknown"})
