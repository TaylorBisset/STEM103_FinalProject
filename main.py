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

""" ==== Databases ==== """

black_history_data = [
    {"name": "Martin Luther King Jr.", "description": "Civil rights leader and advocate for nonviolent protest."},
    {"name": "Rosa Parks", "description": "Civil rights activist known for her role in the Montgomery bus boycott."},
    # Add more entries as needed
]

native_american_history_data = [
    {"name": "Sitting Bull", "description": "Hunkpapa Lakota leader who led his people during years of resistance to United States government policies."},
    {"name": "Sacagawea", "description": "Shoshone woman who helped the Lewis and Clark Expedition."},
    # Add more entries as needed
]

""" ==== Functions ==== """

def explore_history(category):
    # Implement logic to display information based on the selected category


def take_quiz(category):
    # Implement logic for a quiz related to the selected category


""" ==== Main Loop ==== """

while True:
    print("\n==== Social Equity Awareness Program ====")
    print("1. Explore Black History")
    print("2. Explore Native American History")
    print("3. Take a Quiz")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        explore_history(black_history_data)
    elif choice == "2":
        explore_history(native_american_history_data)
    elif choice == "3":
        quiz_category = input("Enter the category for the quiz (1 for Black History, 2 for Native American History): ")
        take_quiz(black_history_data if quiz_category == "1" else native_american_history_data)
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
