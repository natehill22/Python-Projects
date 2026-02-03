



color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'pink', 'brown', 'black', 'white']

def colorCombiner():
    favColor = input("What is you favorite color? ").lower()
    secondFave = input ("What is your second favorite color? ").lower()
    try:
        if (favColor == 'red' and secondFave == 'blue') or (favColor == 'blue' and secondFave == 'red'):
            print("Your combined favorite colors are purple!")
        elif (favColor == 'yellow' and secondFave == 'blue') or (favColor == 'blue' and secondFave == 'yellow'):
            print("Your combined favorite colors are green!")
        elif (favColor == 'yellow' and secondFave == 'red') or (favColor == 'red' and secondFave == 'yellow'):
            print("Your combined favorite colors are orange!")
        elif (favColor == 'white' and secondFave == 'red') or (favColor == 'red' and secondFave == 'white'):
            print("Your combined favorite colors are pink!")
        elif (favColor == 'white' and secondFave == 'blue') or (favColor == 'blue' and secondFave == 'white'):
            print("Your combined favorite colors are baby blue!")
        elif (favColor == 'white' and secondFave == 'violet') or (favColor == 'violet' and secondFave == 'white'):
            print("Your combined favorite colors are lavender!")
        elif (favColor == 'white' and secondFave == 'brown') or (favColor == 'brown' and secondFave == 'white'):
            print("Your combined favorite colors are tan!")
        elif (favColor == 'white' and secondFave == 'black') or (favColor == 'black' and secondFave == 'white'):
            print("Your combined favorite colors are grey!")
        elif (favColor not in color_list) or (secondFave not in color_list):
            print("Please enter a color from this list(red, orange, yellow, green, blue, violet, pink, brown, black, or white).")
    except:
        print("An unexpected error occurred.")
    finally:
        print("The program has finished running.")



if __name__ == "__main__":
    colorCombiner()
