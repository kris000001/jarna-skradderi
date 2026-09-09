from PIL import Image

def get_hours():
    """Returns the opening hours."""
    weekday = "09:30 – 18:00"
    hours = {
        "Måndag": weekday,
        "Tisdag": weekday,
        "Onsdag": weekday,        
        "Torsdag": weekday,
        "Fredag": weekday,
        "Lördag": "10:00 – 14:00",
        "Söndag": "Stängt"
    }
    return hours

def get_images():
    """Reads and returns the shop images."""
    img1 = Image.open("imgFar.jpg")
    img2 = Image.open("imgClose.jpg")
    img3 = Image.open("imgSuit.jpg")
    return [img1, img2, img3]

def get_address():
    """Returns the physical address of the shop."""
    return "Storgatan 1A, 153 30 Järna"

def get_reviews():
    """Returns a list of customer reviews."""
    reviews = [
        {"name": "Anna S.", "text": "Fantastisk service och jättefint resultat!", "rating": "⭐⭐⭐⭐⭐"},
        {"name": "Johan M.", "text": "Snabbt, proffsigt och väldigt trevligt bemötande.", "rating": "⭐⭐⭐⭐⭐"},
        {"name": "Eva L.", "text": "Bästa kemtvätten i Järna. Räddade min favoritskjorta.", "rating": "⭐⭐⭐⭐⭐"}
    ]
    return reviews