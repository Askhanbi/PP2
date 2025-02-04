# Function 1     Task 9

def vloum_sphere(radius):
    pi = 3.14
    volume = (4/3)*(pi)*radius**3
    return volume

радиус = int(input("You're radius: "))
print(vloum_sphere(радиус))