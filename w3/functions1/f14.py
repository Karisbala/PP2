from f1 import grams_to_ounces
from f2 import cel_to_far
from f9 import sphere_vol
from f12 import histogram
from f13 import guesser

ans = True

while ans:
    print ("""
    ==========================================================
    =============== 1.Convert Grams To Ounces =================
    ==========================================================
    ============ 2.Convert Celsius To Fahrenheit ==============
    ==========================================================
    ============ 3.Calculate Volume Of The Sphere =============
    ==========================================================
    =================== 4.Draw a Histogram ====================
    ==========================================================
    ============== 5.Play game "Guess The Number" =============
    ==========================================================
    ========================= 6.Exit ==========================
    ==========================================================
    """)

    ans = input("What would you like to do? Pick a number: ") 

    if ans == "1":
        print("What is amount of grams?", end = " ")
        grams = float(input())
        ounces = grams_to_ounces(grams)
        print("{} grams is equal to {} ounces!".format(grams, ounces)) 
    elif ans == "2":
        print("How much Celsius?", end = " ")
        cel = float(input())
        far = cel_to_far(cel)
        print("{} Celsius is equal to {} Fahrenheits!".format(cel, far)) 
    elif ans == "3":
        print("What is the radius of the sphere?", end = " ")
        r = float(input())
        vol = sphere_vol(r)
        print("The Volume of {} radius sphere is equal to {}!".format(r, vol)) 
    elif ans == "4":
        print("Please input your values separeted by spaces:", end = " ")
        histogram()
    elif ans == "5":
        guesser()
    elif ans == "6":
        print("\nGoodbye!")  
        ans = False
    else:
        print("\nNot Valid Choice Try again!") 