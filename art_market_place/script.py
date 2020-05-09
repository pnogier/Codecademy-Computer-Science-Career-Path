# Codcademy Veneer - Art Marketplace Project


# Here at Veneer, our main concern is the buying and selling of priceless
# art works. Let’s start out by building a model for these works of art.
class Art():  # Define Art class
    # The constructor takes 6 paramaters :
    # self,  artist, title, medium, year and owner
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):  # String representation
        return '{artist}. "{title}". {year}, {medium}. {owner}, {location}'\
            .format(
                artist=self.artist,
                title=self.title,
                year=self.year,
                medium=self.medium,
                owner=self.owner.name,
                location=self.owner.location
            )


# In order to buy and sell works of art, we need a marketplace that will
# maintain the responsibilities of buying, selling, listing, and delisting
# of those artworks.
class Marketplace():  # Define Marketplace class
    def __init__(self):
        self.listings = []  # The constructor creates a new empty list listings

    def add_listing(self, new_listing):  # Add a new listing
        self.listings.append(new_listing)

    def remove_listing(self, expired_listing):  # Remove a listing
        self.listings.remove(expired_listing)

    def show_listings(self):  # Show all listings
        if self.listings == []:
            print("There is no listing yet in the Marketplace...")
            return
        for listing in self.listings:  # Loop through listings
            print(listing)  # Print each listing


# Now for the most important aspect of a marketplace, clients!
class Client():  # Define Client class
    # The constructor takes 4 parameters : self, name, location and is_museum
    def __init__(self, name, location, is_museum):
        self.name = name
        if is_museum:  # Check if client is museum
            self.location = location
        else:
            self.location = "Private Collection"
        self.is_museum = is_museum

    def sell_artwork(self, artwork, price):  # Method to sell an artwork
        if self != artwork.owner:  # Check if client owns the artwork
            print("Worry, you don't own this artwork...")
            return
        listing = Listing(artwork, price, self)  # Create a new Listing
        veneer.add_listing(listing)  # Add it to the Marketplace

    def buy_artwork(self, artwork):  # Method to buy an artwork
        if self == artwork.owner:  # Check if the client doesn't already own it
            print("But... You already own this artwork !")
            return
        art_listing = None  # Setting a variable art_listing to None
        # Loop through each listings in the Marketplace
        for listing in veneer.listings:
            if listing.art == artwork:  # If the listing is in the Marketplace
                art_listing = listing  # Set the listing to the variable
                break
        if art_listing is not None:  # If we could get the listing
            art_listing.art.owner = self  # Set the new owner
            # Remove the listing from the Marketplace
            veneer.remove_listing(art_listing)


# Now that we have a marketplace to facilitate the buying and selling,
# let’s create our class to list works of art!
class Listing():
    # The constructor takes 4 parameters: self, art, price and seller
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return '{title}, {price}'.format(
            title=self.art.title,
            price=self.price
        )


veneer = Marketplace()  # Create a new Marketplace

edytta = Client("Edytta Halpirt", None, False)  # Create a new Client, Edytta
moma = Client("MOMA", "New York", True)  # Create a new Client, a museum

girl_with_mandolin = Art(  # Create a new instance of Art
    "Picasso, Pablo",
    "Girl with a Mandolin (Fanny Tellier)",
    "oil on canvas",
    1910,
    edytta
)

print(girl_with_mandolin)  # It is owned by Edytta
# Edytta wants to sell an artwork for $6M
edytta.sell_artwork(girl_with_mandolin, "$6M")
veneer.show_listings()  # Print the listings in the Marketplace
moma.buy_artwork(girl_with_mandolin)  # The MOMA buys the artwork
print(girl_with_mandolin)  # It is now owned by the MOMA
veneer.show_listings()  # There is no listing left in the Marketplace
