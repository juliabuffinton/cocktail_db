import json
import numpy as np

with open('cocktails.json','r') as f:
    cocktail_list = json.load(f)

def prompt():
    name= input("Enter the name of your cocktail: ")
    link = input("Where did you find this cocktail? Press enter if unknown.")
    tried = input("Have you tried this cocktail before? ")
    if 'y' in tried or 'Y' in tried:
        rating = float(input("What would you rate it on a scale of 1-5? "))
        tried = True
        date = input("When did you first try it? ")
    else:
        tried = False
        rating = np.nan
        date = ""
    glass = input("What time of glass should it be in? ")
    origin = input("In which country did it originate? Press enter if unknown. ")
    year = input("In which year did it originate? Press enter if unknown. ")
    strength = input("How strong is it? Non-alcoholic. Light, Medium, Strong, Extreme Strong. ")
    tags = input("What tags would you like to use? Separate by space. ")
    
    more = True
    ingreds = {}

    while more: 
        ingred, amt, more = input("Enter the ingredient and the amount in oz separated by a comma. If you have more to enter, say more. Otherwise do not type anything. ").split(",")
        ingreds[ingred.strip()] = float(amt.strip())
        
        if 'more' in more or 'More' in more:
            more = True
        else:
            more = False

    correct = input(f"You would like to add the {name} cocktail to the database. Is that correct? Review the details below and enter 0 if that is correct. Otherwise, type anything and you can re-enter the information. \n Link: {link}\n It goes in a {glass}\n It originated in {origin} in {year}\n It is {strength} \n It has these tags: {tags} \n It contains: {ingreds}. \nEnter 0 if this is correct: ")



    if not int(correct):
        output_dict = {name : {
            "link" : link,
            "tried": tried,
            "ingredients" : ingreds,
            "rating" : rating,
            "date" : date,
            "glass type" : glass,
            "origin" : origin, 
            "year" : year,
            "strength" : strength,
            "tags" : tags.split(" ")
                }}
        return True, output_dict
    else:
        return False, {}

def main():

    another = True
    while another: 

        correct,cocktail = prompt()

        if correct:
            cocktail_list.update(cocktail)

        another = input("Would you like to enter another cocktail? ")

        if 'y' in another or 'Y' in another:
            another = True
        else:
            another = False

        with open('cocktails.json','w') as f:
            json.dump(cocktail_list, f)


if __name__ == "__main__":
    main()