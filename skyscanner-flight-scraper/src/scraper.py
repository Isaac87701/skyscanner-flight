thonimport requests
from bs4 import BeautifulSoup
import json

class SkyscannerScraper:
    def __init__(self, origin, target, depart, return_date=None):
        self.origin = origin
        self.target = target
        self.depart = depart
        self.return_date = return_date
        self.base_url = "https://www.skyscanner.com"

    def fetch_flight_data(self):
        url = f"{self.base_url}/flights/{self.origin}/{self.target}/{self.depart}"
        if self.return_date:
            url += f"/{self.return_date}"
        
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Failed to retrieve data")
        
        return self.parse_flights(response.text)

    def parse_flights(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        flights = []
        for flight in soup.find_all('div', class_="flight-card"):
            flight_data = {
                "origin": self.origin,
                "target": self.target,
                "depart": self.depart,
                "return": self.return_date,
                "flight_price": flight.find('span', class_="price").text
            }
            flights.append(flight_data)
        return flights

    def save_to_file(self, data, filename="flights.json"):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

if __name__ == "__main__":
    scraper = SkyscannerScraper("Jakarta", "London", "2022-10-17", "2022-10-20")
    flights = scraper.fetch_flight_data()
    scraper.save_to_file(flights)