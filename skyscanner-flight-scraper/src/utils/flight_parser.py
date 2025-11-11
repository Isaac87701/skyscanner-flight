thonimport json

def parse_flight_data(flight_data):
    parsed_flights = []
    for flight in flight_data:
        parsed_flights.append({
            "origin": flight["origin"],
            "destination": flight["target"],
            "departure_date": flight["depart"],
            "return_date": flight["return"],
            "price": flight["flight_price"]
        })
    return parsed_flights