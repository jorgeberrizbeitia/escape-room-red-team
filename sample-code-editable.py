# %%
# GLOBAL VARIABLES

# define rooms and items

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
        "question": "Who from your class had the larger number of pets in life?",
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
#TODO ADD DESCRIPTION TO THE SCENARIOS
outside = {
    "name": "outside",
    "description": " ",
}

classroom = {
    "name": "classroom",
    "type": "scenario",
    "description": " ",
}

shoe_store = {
    "name":"shoe store",
    "type":"scenario",
    "description": " ",
}

pet_store = {
    "name":"pet store",
    "type":"scenario",
    "description": " ",
}

basketball_court = {
    "name":"basketball court",
    "type":"scenario",
    "description": " ",
}


#all_scenarios = [classroom, outside]
#all_portals = [portal_a]
#! commented from MVP as it was not used

# define which items/rooms are related

# if its a room, everything inside the room
# if its a furniture, everything inside the furniture
# if it is a door, the two rooms the door connects. From where to where!

# CODE FOR RANDOM QUESTIONS -> [ questions_dict[random.choice(list(questions_dict.keys()))]

object_relations = {
    "computer": [ questions_dict["question_4"], pill_blue], 
    "fitting area": [questions_dict["question_2"], pill_red],
    "training pads container": [questions_dict["question_3"],pill_green],
    "hot dog stand": [questions_dict["question_1"],pill_yellow],
    "classroom": [backpack, computer, portal_blue],
    "shoe store": [portal_blue, portal_red, portal_green, fitting_area],
    "pet store": [training_pads_container, grooming_supplies_stand, portal_red],
    "basketball court": [hot_dog_stand, portal_yellow, portal_green],
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

INITIAL_TIMER_VALUE = 300 # so 5 minutes

# %%
# MUSIC

#!installation music library
#%pip install pygame #! Comment if runnin on terminal and .py file
import pygame
# initialize pygame
pygame.init()
pygame.mixer.init()
# load background music
pygame.mixer.music.load(r"quiz-countdown-194417.mp3")
# set volume
pygame.mixer.music.set_volume(0.008)
# play music (-1 means loop indefinitely)
pygame.mixer.music.play(-1)



# %%
# FONT COLOR

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

# %%
# IMAGE PROCESSING

import platform # for determining userOS
import subprocess # to run extra terminal commands
import shutil  # for checking if imgcat is available

def show_image(img_path):
    """
    Starts displays an image either in the terminal or by opening an image preview
    example use: show_image("test.jpg")
    IMPORTANT: Only works on terminals (not VS code nested terminal) and by running the .py file
    in iTerm2 (for mac) it shows the image inside the terminal, in others, it opens an image preview.
    """
    os_name = platform.system() # get the user OS

    if os_name == "Darwin":  # if OS is macOS
        
        if shutil.which("imgcat"): # check if iTerm2's imgcat is available (this allows img to be displayed on terminal, but only on iTerm2)
            try:
                subprocess.run(["imgcat", img_path])  # use imgcat if iTerm2 is installed so img is displayed directly on terminal
            except Exception as e:
                print(f"Error displaying image with imgcat: {e}")
        else:
            try:
                subprocess.run(["open", img_path])  # fallback to Preview if imgcat is not found. this will open img on default image preview app.
            except Exception as e:
                print(f"Error opening image with Preview: {e}") # error handling
    
    elif os_name == "Windows":  # if OS is Windows
        try:
            subprocess.run(["start", img_path], shell=True)  # open in default image viewer
        except Exception as e:
            print(f"Error opening image: {e}") # error handling
    
    elif os_name == "Linux":  # if OS is Linux
        try:
            subprocess.run(["xdg-open", img_path])  # open in default image viewer
        except Exception as e:
            print(f"Error opening image: {e}") # error handling


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
                linebreak()
                print(f"\n{red_b}Time's up! You didn't escape in time! {cyan_b}iDavid{white} seems to {red_b}shut down...{white} \nYou are now alone in the room and all the portals have closed for good, {red_b}there is no way to leave.{white} \nYou are bound to study Data Science for the rest of your life.{white}")
                
                os._exit(0)  # Forcefully stop the entire program
            
            if (remaining_time % 30 == 0):
                # Print timer on a separate line, avoiding overlap with input. Only happends every 15 seconds
                print(f"\rSuddenly {cyan_b}iDavid{white} turns to you and reminds you that you only have: {red_b}{remaining_time} seconds{white} remaining.\n")
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
    
    print( f"The classroom has been taken over by {cyan_b}iDavid{white}, a Robot Teacher at {cyan_b}IRONHACK{white} with sinister intentions. \nHe seems to have {red_b}locked everyone{white} inside and left cryptic clues all around. \nThe lights flicker, and strange whispers echo through the air." )
    linebreak()

    print(f"But there is hope. You are the only one among your classmates who holds the power to free them. \nTo do this, you must embark on a journey through mysterious {magenta_b}scenarios{white}. \nIn each {magenta_b}scenario{white}, you need will need to find several {blue_b}pills{white}. \nThese {blue_b}pills{white} will help you open {cyan_b}portals{white} to your next challenges and bring you closer to {green_b}freeing all your classmates!{white}") 
    linebreak()

    print(f"You will have {red_b}{INITIAL_TIMER_VALUE} seconds{white} to make it to the end!\n")

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
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """

    if game_state["current_scenario"] != scenario:
        #* SCENARIO CHANGE
        game_state["current_scenario"] = scenario
        show_image(f"./images/{game_state["current_scenario"]["name"]}.jpg")
        if(game_state["current_scenario"] == game_state["target_scenario"]):
            #* GAME END
            print(f"{green_b}Congrats!{white} You answered all the questions in each scenario and {green_b}freed all your classmates!{white}. You also noticed the robot gets an update to {cyan_b}iDavid 2.0{white}, a less sinister version who celebrates with everyone!")
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
    linebreak()

def explore_scenario(scenario):
    """
    Explore a room. List all items belonging to this room.
    """
    explore_message = f"You decide to {yellow_b}'explore'{white} around and find the following: "
    for item in object_relations[scenario["name"]]:
      explore_message += magenta_b + str(item["name"]) + white + ", " # colors for the colored items and white for reset
    explore_message = explore_message[:-2]+"."
    print(explore_message)

def get_next_scenario_of_portal(portal, current_scenario):
    """
    #!From object_relations, find the two rooms connected to the given door. Return the second room. But if the second room is the current room, return the first element.
    """
    connected_scenarios = object_relations[portal["name"]]
    
    if(current_scenario == connected_scenarios[0]):
        return connected_scenarios[1]
    else:
        return connected_scenarios[0]

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
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
                    question_dict = object_relations[item["name"]][0] #It's getting the first key of the object_relations
                    user_input = safe_input(f"You find a terminal prompt with a question: {white_u}{question_dict['question']}{white} ").strip().lower()
                    if(user_input == question_dict['answer']):
                        item_found = object_relations[item["name"]].pop() #It's removing the key from the object_relations
                        game_state["pills_collected"].append(item_found)
                        output = f"You answered the question {green_b}correctly!{white} take the {magenta_b}{item_found["name"]}{white}."
                    else: 
                        output = f"You answered the question {red_b}incorrectly!{white} Try again."
                else:
                    output += f"{red_b} There isn't anything interesting about it{white}."
            print(output)
            break

    if(output is None):
        print(f"The item you requested is {red_b}not found{white} in the current scenario.")
    
    if(next_scenario and safe_input(f"{white_u}Do you want to go to the next scenario?{white} Enter {green_b}'yes'{white} or {red_b}'no'{white}: ").strip() == 'yes'):
        play_scenario(next_scenario)
    else:
        play_scenario(current_scenario)

# %%
# GAME START LOGIC
game_state = INIT_GAME_STATE.copy()

start_game()
        


