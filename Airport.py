class Airport:
    def __init__(self, code, name, city, country, lat, lon, rate) -> None:
        self.name = name
        self.code = code
        self.city = city
        self.country = country
        self.lat = float(lat)
        self.lon = float(lon)
        self.rate = float(rate)

    def __repr__(self) -> str:
        return f"Airport: code:{self.code} name: {self.name} city:{self.city} country:{self.country} lat:{self.lat} lon: {self.lon} rate: {self.rate}"
