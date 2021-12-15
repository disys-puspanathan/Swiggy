hotel = {"Venu Biriyani":
        {"chicken briyani":350,"mutton briyani":450,"prawn biriyani":250,"fish biriyani":300,"chicken gravy":100,"mutton gravy":120,"pepper mutton chukka":170,"nandu soup":100,},
         "Thattu kadai":
        {"chicken briyani":180,"mutton briyani":280,"parotta":10,"egg parotta":80,"chicken parotta":100,"full grill":100,"half grill":55,"leg fry":100,"egg kuruma":100,"chicken wings":200},
         "WoW Veg":
        {" vegbriyani":150,"veg aviyal":80,"veg curry":100," vegparotta":25,"chilli parotta":70,"veg meals":90,"carrot rice":45,"beetroot rice":100,"spinach rice":80,"beabs rice":55},
         "Semma Biriyani":
        {"chicken briyani":150,"muttonbriyani(boneless)":180,"muttonbriyani(bone in)":280,"prawn briyani":120,"fish briyani":150,"beef briyani":150," turkey briyani":190},
         "Buhar":
        {"chicken briyani":150," mutton briyani":80,"fish briyani":100,"fish fry":55,"Fish curry":50,"fish fried rice":90,"chicken fried rice":145,"mutton fried rice":150,"egg fried rice":80},
         "Kutty suvai":
        {"chicken briyani":80,"mutton briyani":200," veechu parotta":10,"egg veechu parotta":80,"chicken veechu parotta":100,"full meals(veg)":100,"half meals(veg)":55,"full meals(non veg)":100},
         "C":
        {"plain briyani":150," mushroom briyani":180,"fish briyani":180,"naan":25,"chilli chicken":90,"green chicken":90,"mutton chukka":145,"chicken chukka":150,"leaf parotta":140,"oil parotta":20}}


def search():
    print("SEARCH HOTELS")
    print(hotel)
    yesno=input("continue y/n ?")
    if(yesno == 'y'):
           menu()
    else:
            exit()

def order():
    print("ORDER FOOD")
    bir = input("select hotel")
    for i in hotel:
        print ("Selected Hotel is: " + str(hotel))

def menu():
    print("""
    1.Available Hotel
    2.Order Food
    3.Exit Contact App
    """)

    select = int(input("Select options"))
    print("\n")
    if(select == 1):
        pc = search()
    elif(select == 2):
        order()
    elif(select == 3):
        print("Left")
        exit()

menu()
