thonimport json

# Function to parse flight data from raw JSON
def parse_flight_data(raw_data):
    parsed_flights = []
    
    for flight in raw_data:
        parsed_flight = {
            "origin": flight['origin'],
            "target": flight['target'],
            "depart": flight['depart'],
            "airlines": flight['airlines'],
            "price": flight['price'],
            "departure_time": flight['departure_time'],
            "arrival_time": flight['arrival_time']
        }
        parsed_flights.append(parsed_flight)
    
    return parsed_flights

# Example usage
if __name__ == "__main__":
    with open('data/sample_flights.json', 'r') as f:
        raw_flights = json.load(f)
    
    parsed_flights = parse_flight_data(raw_flights)
    print(f"Parsed {len(parsed_flights)} flights")