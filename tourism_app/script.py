# Destinations list
destinations = ["Paris, France",
                "Shanghai, China",
                "Los Angeles, USA",
                "São Paulo, Brazil",
                "Cairo, Egypt"]

# Attractions list
attractions_list = [[], [], [], [], []]

# Test traveler who is in China at the moment
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


# A function that returns a specific destination index in the destinations list
def get_destination_index(destination):
    return destinations.index(destination)


# A function that returns the index of a specific traveler's location
# in the destinations list
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


# A function to add an attraction to the attractions list
def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions_list[destination_index]
        attractions_for_destination.append(attraction)
        return
    except ValueError:
        return


# Adding many attractions to cities
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", [
               "historical site", "monument"]])
add_attraction("Paris, France", ["Tour Eiffel", [
    "historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", [
               "garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", [
               "skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", [
               "monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


# A function to find attractions with the traveler's interests
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions_list[destination_index]
    attractions_with_interest = []
    for attraction in attractions_in_city:
        attraction_tags = attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(attraction[0])
    return attractions_with_interest


# A function that eturns a string with the attraction to visit for the
# traveler in the city where he is at the moment
def get_attractions_for_traveler(traveler):
    traveler_desination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(
        traveler_desination, traveler_interests)
    interests_str = "Hi " + traveler[0] + \
        ", we think you'll like these places around " + \
        traveler_desination + ":"
    for attraction in traveler_attractions:
        interests_str += " " + attraction + ","
    interests_str = interests_str[:-1] + "."
    return interests_str


# Will print "Hi Dereck Smill, we think you'll like these places around
# Paris, France: Arc de Triomphe, Tour Eiffel."
print(get_attractions_for_traveler(
    ['Dereck Smill', 'Paris, France', ['monument']]))
