# Taylor Bisset
# STEM103 SUM2024
# Rashi Goyal
# Final Project: Social Equity Awareness Program
"""
Description: Develop a program that educates users about influential individuals 
or events related to marginalized communities in history, such as Black, Indigenous, LGBT+. 
Users can learn about notable figures, achievements, 
or historical milestones through an interactive interface.
Here's a great history database offered through the EvCC Library, Gale in Context, 
US HistoryLinks to an external site. 
If you access it off campus, you will may need log in information to use it.

Requirements:
1. Create a database or list of notable figures, events, or milestones related to history.
2. Users can select a category (e.g., Black History, Native or Indigenous History, etc) and explore information.
3. Implement a quiz feature that tests users' knowledge about the selected category.
4. Make the program interactive and engaging
"""

# ==== Modules ====

import random


# ==== Databases ==== 

black_history_data = [
    {"name": "Martin Luther King Jr.",
     "description": "Baptist minister and civil rights leader in the U.S. during the mid-1950s."},
    {"name": "Rosa Parks",
     "description": "Civil rights activist whose refusal to give up her bus seat sparked the Montgomery bus boycott in 1955–56."},
    {"name": "Malcolm X",
     "description": "African American leader in the Nation of Islam who promoted race pride and Black nationalism in the early 1960s."},
    {"name": "Harriet Tubman",
     "description": "Abolitionist who escaped slavery and led others to freedom via the Underground Railroad before the Civil War."},
    {"name": "James Baldwin",
     "description": "Essayist, novelist, and playwright known for his impactful writing on race in America."}
]

native_american_history_data = [
    {"name": "Sitting Bull",
     "description": "Lakota chief who led the Sioux resistance against settlers on the northern Great Plains."},
    {"name": "Sacagawea",
     "description": "Shoshone interpreter who traveled with the Lewis and Clark Expedition from the Dakotas to the Pacific Northwest."},
    {"name": "Geronimo",
     "description": "Apache leader who defended his homeland against U.S. military forces."},
    {"name": "Tecumseh",
     "description": "Shawnee chief and military leader who organized resistance against white settlers in the Ohio River valley."},
    {"name": "Crazy Horse",
     "description": "Sioux warrior and tactician who resisted European American invasion of the northern Great Plains."}
]


# ==== Functions ==== 

def explore_history(category):
    random.shuffle(category)
    for item in category:
        print(f"Name: {item['name']}")
        print(f"Description: {item['description']}\n")

def take_quiz(category):
    # Implement logic for a quiz related to the selected category
    print("\n==== Take a Quiz ====")
    return
'''
Initialize score to zero.
Repeat the following 5 times: 
    1. Pick a random description from the category.
    2. List the names of all individuals from the category.
    3. Ask the user to type the name the matches the description.
    4. If the user's input matches the correct name, increment the score.

After all 5 questions are answered: 
    1. Calculate grade by dividing score by 5.
    2. Print the user's grade.
'''

# ==== Main Loop ==== 

while True:
    print("\n==== Social Equity Awareness Program ====")
    print("1. Explore Black American History")
    print("2. Explore Native American History")
    print("3. Take a Quiz")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"\n==== Explore Black American History ====\n")
        explore_history(black_history_data)
    elif choice == "2":
        print(f"\n==== Explore Native American History ====\n")
        explore_history(native_american_history_data)
    elif choice == "3":
        quiz_category = input("\nTake a Test \n\t1 for Black American History \n\t2 for Native American History \nEnter the category for the quiz: ")
        take_quiz(black_history_data if quiz_category == "1" else native_american_history_data)
    elif choice == "4":
        print("\n\t\tExiting the program. \n\t\tGoodbye!\n")
        break
    else:
        print(f"\tInvalid choice {choice} \n\tPlease enter a number between 1 and 4.")
