import requests


def fetchEmergencys():
    """
    Fetches the latest emergency data from the API.
    """
    try:
        response = requests.get('https://emergency.vic.gov.au/public/events-geojson.json')
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching emergency data: {e}")
        return None
    
def fetchEmergencyById(emergency_id):
    """
    Fetches a specific emergency by its ID.
    """
    data = fetchEmergencys()
    for emergency in data['features']:
        if emergency['properties']['id'] == emergency_id:
            return [emergency['properties'], emergency['geometry']]
        
print(fetchEmergencyById(102622013))