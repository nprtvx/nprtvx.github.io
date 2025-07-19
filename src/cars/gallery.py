images = [
  "https://images.pexels.com/photos/2927538/pexels-photo-2927538.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  "https://images.pexels.com/photos/1729993/pexels-photo-1729993.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  "https://images.pexels.com/photos/33062758/pexels-photo-33062758/free-photo-of-black-and-white-restaurant-scene-with-diners.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
  "https://images.pexels.com/photos/33059167/pexels-photo-33059167/free-photo-of-vibrant-tokyo-night-street-with-neon-signs.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
]

image_elements = list()

for img in images:
  image_elements.append(f"<img src='{img}' class='gallery-image'>")

