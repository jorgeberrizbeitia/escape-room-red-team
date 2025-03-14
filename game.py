# %%
# GLOBAL VARIABLES

# FONT COLORS

# NOTE: replaced function for variables for simplicity of use and to mantain code legibility

red_b = "\033[1;31m" # RED BOLD. for incorrect prompts or actions
green_b = "\033[1;32m" # GREEN BOLD. for correct prompts or success messages
yellow_b = "\033[1;33m" # YELLOW BOLD. for possible actions the user can do
blue_b = "\033[1;34m" # BLUE BOLD. for items (things the user collects)
magenta_b = "\033[1;35m" # MAGENTA BOLD. for scenarios (things the user explores)
cyan_b = "\033[1;36m" # CYAN BOLD. for furniture, portals and decorations (things the user examines)

white = "\033[0;37m" # WHITE. all other text. Also used for RESET
white_u = "\033[1;4;37m" # WHITE BOLD UNDERLINE. for questions the user is prompted

#? how to use?

# single colored lines: start any colored print or input with the color to use in the whole message
#example: print(green_b + "Hello World in green!")

# multicolored lines: use string interpolation and add color variables before each colores word or subtext.
#example: print(f"{white}This part is white {red_b}and this part is red. {white}This part is white again ")

# QUESTIONS

questions_dict = {
    "question_1": {
        "question": "Who is the tallest person in our class?",
        "answer": "luis", 
        "type": "question"
    },

    "question_2": {
        "question": "Who has the smallest shoe size in your class?",
        "answer": "maria",
        "type": "question"
    },

    "question_3": {
        "question": "Who from your class has had the larger number of pets in life?",
        "answer": "stefano",
        "type": "question"
    },

    "question_4": {
        "question": "Who from your class lives closer to the Sagrada Familia?",
        "answer": "tay",
        "type": "question"
    },
}
# FURNITURE

backpack = {
    "name": "backpack",
    "type": "furniture",
}

training_pads_container = {
    "name": "training pads container",
    "type": "furniture",
}

grooming_supplies_stand = {
    "name": "grooming supplies stand",
    "type": "furniture",
}

hot_dog_stand = {
    "name": "hot dog stand",
    "type": "furniture",
}

computer = {
    "name": "computer",
    "type": "furniture",
}

fitting_area = {
    "name": "fitting area",
    "type": "furniture",
}

# PORTALS

portal_blue = {
    "name": "blue portal",
    "type": "portal",
}

portal_red = {
    "name": "red portal",
    "type": "portal"
}

portal_green = {
    "name": "green portal",
    "type": "portal"
}

portal_yellow = {
    "name": "yellow portal",
    "type": "portal"
}

# PILLS

pill_blue = {
    "name": "pill for the blue portal",
    "type": "pill",
    "target": portal_blue,
}

pill_red = {
    "name": "pill for the red portal",
    "type": "pill",
    "target": portal_red,
}

pill_green = {
    "name": "pill for the green portal",
    "type": "pill",
    "target": portal_green,
}

pill_yellow = {
    "name": "pill for the yellow portal",
    "type": "pill",
    "target": portal_yellow
}

# SCENARIOS
outside = {
    "name": "outside",
    "description": " ", # no description will be printed. But it needs the property to exist to prevent crash.
}

classroom = {
    "name": "classroom",
    "type": "scenario",
    "description": f"You are greeted by {cyan_b}iDavid{white} who invites you to look around. \nIt seems like a normal teaching classroom, with an amazing view of the Sagrada Familia in Barcelona. \nYou are not sure you will find your way back home, \nbut maybe some of your classmates could help you get out of here.",
}

shoe_store = {
    "name":"shoe store",
    "type":"scenario",
    "description": "\nSo many shoes around, it looks like a normal store where any of your classmates could buy one pair for themselves. \nYou start wondering if you would you be capable of choosing the perfect size for all of them",
}

pet_store = {
    "name":"pet store",
    "type":"scenario",
    "description": "\nThe store is filled with all kinds of pet items and you see several animals walking around. \nEverywhere you look, there’s something moving, chirping or wagging its tail. \nSome of your classmates would feel right at home among so many pets, while others might be a bit unsure.",
}

basketball_court = {
    "name":"basketball court",
    "type":"scenario",
    "description": "\nThe court is huge, with loud music and full with food and drink stands. \nAll the players are really tall, taller than everyone in your class. Or maybe not everyone?",
}

# SECRET
idavid = {
    "name": "idavid", # lowercase to match input.lower()
    "type": "secret",
    "messages": {
        "classroom": f"You spot {cyan_b}iDavid{white} at the whiteboard, lost in thought, mumbling about ‘overfitting in real life.’ \nHe suddenly writes: 'Too much studying, not enough living'… then erases it quickly, looking around suspiciously.",
        "shoe store": f"You see {cyan_b}iDavid{white} analyzing the shoe inventory, \nscribbling in a notebook: 'If I apply k-means clustering… I can find the optimal sneaker for a Data Scientist!' \nHe then tries on a pair, nodding as if they improve his coding skills.",
        "pet store": f"{cyan_b}iDavid{white} is sitting inside a dog pen, surrounded by puppies. \nHe’s holding a notepad, muttering, 'If I had enough data points, \nI could predict which puppy will fetch the ball first... But they keep eating my notes!",
        "basketball court": f"You notice {cyan_b}iDavid{white} is watching a game intensely, whispering, \n'If I track every player's shooting percentage, I can predict the MVP…' \nHe then gets hit by a stray ball and mutters, 'Outlier detected.'",
    }
}

#all_scenarios = [classroom, outside]
#all_portals = [portal_a]
#! commented from MVP as it was not used

# define which items/scenario are related

# if its a scenario, everything inside the scenario
# if its a furniture, everything inside the furniture
# if it is a door, the two scenarios the door connects. From where to where!

# CODE FOR RANDOM QUESTIONS -> [ questions_dict[random.choice(list(questions_dict.keys()))]

object_relations = {
    "computer": [ questions_dict["question_4"], pill_blue], 
    "fitting area": [questions_dict["question_2"], pill_red],
    "training pads container": [questions_dict["question_3"],pill_green],
    "hot dog stand": [questions_dict["question_1"],pill_yellow],
    "classroom": [backpack, computer, portal_blue, idavid],
    "shoe store": [portal_blue, portal_red, portal_green, fitting_area, idavid],
    "pet store": [training_pads_container, grooming_supplies_stand, portal_red, idavid],
    "basketball court": [hot_dog_stand, portal_yellow, portal_green, idavid],
    "outside": [portal_yellow],
    "blue portal": [classroom, shoe_store],
    "red portal": [shoe_store, pet_store,shoe_store],
    "green portal": [basketball_court, shoe_store],
    "yellow portal": [basketball_court, outside]
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "initial_scenario": classroom, # this allows the first game image to be shown when the current_scenario changes
    "current_scenario": None, # this makes sense, the user doesn't start anywhere until a scenario is assigned
    "pills_collected": [],
    "target_scenario": outside,
}

INITIAL_TIMER_VALUE = 420 # so 7 minutes

# %%
# MUSIC

#!installation music library
#%pip install pygame #! Comment if runnin on terminal and .py file
import pygame
# initialize pygame
pygame.init()
pygame.mixer.init()
# load background music
pygame.mixer.music.load(r"./audio/quiz-countdown-194417.mp3")
# set volume
pygame.mixer.music.set_volume(0.008)
# play music (-1 means loop indefinitely)
pygame.mixer.music.play(-1)



# %%
# IMAGE PROCESSING

import platform  # For determining user OS
import subprocess  # To run extra terminal commands
import shutil  # For checking available terminal utilities

def show_image(img_path):
    """
    Displays an image in the terminal (iTerm2 for Mac) or opens it in an external viewer (other terminals and OS)
    Works only in standalone Python scripts (not VS Code's nested terminal).
    """
    os_name = platform.system()  # Get the user OS
    
    try:
        if os_name == "Darwin":  # macOS
            if shutil.which("imgcat"):  # Check if iTerm2's imgcat is available
                subprocess.run(["imgcat", img_path])  # Show image in iTerm2 terminal
            else:
                subprocess.run(["open", img_path])  # Open image in macOS Preview app

        elif os_name == "Windows":  # Windows
            if shutil.which("powershell"):  # Use PowerShell if available
                subprocess.run(["powershell", "-c", f"Start-Process '{img_path}'"], shell=True)
            else:  # Fallback to explorer (works better for Git Bash)
                subprocess.run(["explorer", img_path], shell=True)

        elif os_name == "Linux":  # Linux
            subprocess.run(["xdg-open", img_path])  # Open in default image viewer

    except Exception as e:
        print(f"Error displaying image: {e}")  # Generic error handling


# %%
# HELPER FUNCTIONS

def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def safe_input(prompt):
    """
    This function ensures that input prompts are displayed properly
    without being overwritten by background thread prints.
    """
    try:
        return input(f"\n{prompt}\n> ")
    except EOFError:
        return ""

# %%
# TIMER

import time
import threading
import os  # Import os for forced exit on game end via timer threading.

def start_timer(total_time):
    """
    Starts a countdown timer in a separate thread.
    Prints remaining time every second without interfering with input.
    """
    def countdown():
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            remaining_time = total_time - int(elapsed_time)
            
            if remaining_time <= 0:
                # linebreak()
                print(f"\n{red_b}Time's up! You didn't escape in time! {cyan_b}iDavid{white} seems to {red_b}shut down...{white} \nYou are now alone in the room and all the portals have closed for good, {red_b}there is no way to leave.{white} \nYou are bound to study Data Science for the rest of your life.{white}")
                
                os._exit(0)  # Forcefully stop the entire program
            
            if (remaining_time % 60 == 0):
                # Print timer on a separate line, avoiding overlap with input. Only happends every 15 seconds
                print(f"\rSuddenly {cyan_b}iDavid{white} turns to you and reminds you that you only have: {red_b}{int(remaining_time/60)} minutes{white} remaining.\n")
                # sys.stdout.flush()

            time.sleep(1)
    
    # Run the timer in a separate thread
    timer_thread = threading.Thread(target=countdown, daemon=True)
    timer_thread.start()


# %%
# GAME FUNCTIONS

def start_game():
    """
    Start the game
    """

    linebreak()
    linebreak()
    linebreak()
    linebreak()
    
    print( f"The classroom has been taken over by {cyan_b}iDavid{white}, a Robot Teacher at {cyan_b}IRONHACK{white} with sinister intentions. \nHe seems to have {red_b}locked everyone{white} inside and left cryptic clues all around. \nThe lights flicker, and strange whispers echo through the air." )
    linebreak()

    print(f"But there is hope. You are the only one among your classmates who holds the power to free them. \nTo do this, you must embark on a journey through mysterious {magenta_b}scenarios{white}. \nIn each {magenta_b}scenario{white}, you need will need to find several {blue_b}pills{white}. \nThese {blue_b}pills{white} will help you open {cyan_b}portals{white} to your next challenges and bring you closer to {green_b}freeing all your classmates!{white}") 
    linebreak()

    print(f"You will have {red_b}{int(INITIAL_TIMER_VALUE/60)} minutes{white} to make it to the end!\n")

    user_input = safe_input(f"{white_u}Will you accept the challenge?{white} type: {green_b}'yes{white}' or {red_b}'no'{white}: ")

    if user_input.strip().lower() == "yes":
        start_timer(INITIAL_TIMER_VALUE - 1) # -1 so it doesn't print at the start
        play_scenario(game_state["initial_scenario"])
    else:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        linebreak()
        print(f"That's too bad. {cyan_b}iDavid{white} seems to {red_b}shut down...{white} \nYou are now alone in the room and all the {magenta_b}portals{white} have closed for good, {red_b}there is no way to leave.{white} \nYou are bound to study Data Science alone for the rest of your life.{white}")
        linebreak()


# game termination
def play_scenario(scenario):
    """
    Play a scenario. First check if the scenario being played is the target scenario.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this scenario) or examine an item found here.
    """

    if game_state["current_scenario"] != scenario:
        #* SCENARIO CHANGE
        game_state["current_scenario"] = scenario
        show_image(f"./images/{game_state["current_scenario"]["name"].replace(" ", "-")}.jpg") # replace is due to img names not having spaces.
        if(game_state["current_scenario"] == game_state["target_scenario"]):
            #* GAME END
            linebreak()
            print(f"{green_b}Congrats!{white} You answered all the questions in each scenario and {green_b}freed all your classmates!{white}. \nYou also noticed the robot gets an update to {cyan_b}iDavid 2.0{white}, a less sinister version who celebrates with everyone!")
            linebreak()
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            return # END THE GAME
        
        print(f"You find youself in a {blue_b}{scenario["name"]}{white}. {scenario["description"]}") # message if the user enters scenario first time
    else:
        print(f"You are still in the {blue_b}{scenario["name"]}{white}.") # message if the user is still in the same scenario as before


    #* GAME CONTINUES
    intended_action = safe_input(f"{white_u}What would you like to do?{white} Type {yellow_b}'explore'{white} or {yellow_b}'examine'{white}? ").strip().lower()
    if intended_action == "explore":
        explore_scenario(scenario)
        play_scenario(scenario)
    elif intended_action == "examine":
        examine_item(safe_input(f"What would you like to {yellow_b}'examine'{white} ? ").strip().lower())
    else:
        print(f"{red_b}Not sure what you mean{white}. Type {yellow_b}'explore'{white} or {yellow_b}'examine'{white}.")
        play_scenario(scenario)
    # linebreak()

def explore_scenario(scenario):
    """
    Explore a scenario. List all items belonging to this scenario.
    """
    explore_message = f"You decide to {yellow_b}'explore'{white} around and find the following: "
    for item in object_relations[scenario["name"]]:
      # SECRET. Below conditional, so iDavid is not visible in explore
      if item["type"] == "secret": 
        continue
      explore_message += magenta_b + str(item["name"]) + white + ", " # colors for the colored items and white for reset
    explore_message = explore_message[:-2]+"."
    print(explore_message)

def get_next_scenario_of_portal(portal, current_scenario):
    """
    From object_relations, find the two scenarios connected to the given portal.
    If current_scenario is the first scenario, return the second scenario, and viceversa.
    """
    connected_scenarios = object_relations[portal["name"]]
    
    if(current_scenario == connected_scenarios[0]):
        return connected_scenarios[1]
    else:
        return connected_scenarios[0]

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current scenario.
    Then check if the item is a door. Tell player if pill hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    scenario. If the item is not a door, then check if it contains pills.
    Collect the pill if found and update the game state. At the end,
    play either the current or the next scenario depending on the game state
    to keep playing.
    """
    current_scenario = game_state["current_scenario"]
    next_scenario = ""
    output = None
    
    for item in object_relations[current_scenario["name"]]:
        if(item["name"] == item_name):
            output = f"You examine {magenta_b}{item_name}{white}."
            if(item["type"] == "portal"):
                have_key = False
                for key in game_state["pills_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "The portal is open, good luck!!!"
                    next_scenario = get_next_scenario_of_portal(item, current_scenario)
                else:
                    output += "It is blocked, you will need to find the pill first"
            elif(item["type"] == "furniture"):
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0): #if the item exist inside the object relations and if it has any relations
                    question_dict = object_relations[item["name"]][0] #It's getting the first pill of the object_relations
                    user_input = safe_input(f"You find a terminal prompt with a question: {white_u}{question_dict['question']}{white} ").strip().lower()
                    if(user_input == question_dict['answer']):
                        item_found = object_relations[item["name"]].pop() #It's removing the pill from the object_relations
                        game_state["pills_collected"].append(item_found)
                        output = f"You answered the question {green_b}correctly!{white} take the {magenta_b}{item_found["name"]}{white}."
                    else: 
                        output = f"You answered the question {red_b}incorrectly!{white} Try again."
                else:
                    output += f"{red_b} There isn't anything interesting about it{white}."
            # SECRET. check for idavid special item and print the special iDavid message for each scenario
            elif(item["type"] == "secret" and item["name"] == "idavid"):
                output = item["messages"][current_scenario["name"]]
            print(output)
            break

    if(output is None):
        print(f"The item you requested is {red_b}not found{white} in the current scenario.")
    
    linebreak()
    if(next_scenario and safe_input(f"{white_u}Do you want to go to the next scenario?{white} Enter {green_b}'yes'{white} or {red_b}'no'{white}: ").strip() == 'yes'):
        play_scenario(next_scenario)
    else:
        play_scenario(current_scenario)

# %%
# GAME START LOGIC
game_state = INIT_GAME_STATE.copy()

start_game()
        


