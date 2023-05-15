from TravelAgent import TravelAgent


def main():
    travel_agent = TravelAgent("Go XEU")
    trip_info1 = travel_agent.set_trip_one_city_one_way(
        "DAC", "PRA", "5/7/2024")
    # print("aircraft", trip_info1.aircraft, "\nprice", trip_info1.price)
    trip_cities = ["DUB", 'LHR', 'SYD', 'JFK', 'ORD', 'DAC']
    trip_info2 = travel_agent.set_trip_multi_city_flexible_route(
        trip_cities, "05/4/2564")
    print('price: ', trip_info2[1])
    for trip in trip_info2[0]:
        print(trip)


if __name__ == "__main__":
    main()
