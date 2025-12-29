

color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'pink', 'brown', 'black', 'white']

def colorCombiner():
    favColor = input("What is you favorite color? ").lower
    secondFave = input ("What is your second favorite color? ").lower
    try:
        print(x)
        (favColor and secondFave) not in color_list 
    except:
        print("Please enter a color from this list(red, orange, yellow, green, blue, violet, pink, brown, black, or white).")
    finally:
        print("You know what...whatever. Let's leave it all behind us, huh?")

if __name__ == "__main__":
    colorCombiner()
