# %%
# GLOBAL VARIABLES

# define rooms and items

#todo edited by Tay:
#todo defining the questions and answers as dictionaries. Ive created a dictionary named questions_dict so we can apply a random function. 

questions_dict = {

    "question_1": {
        "question": "Who is the tallest person in our class?",
        "answer": "luis", #changed Luís for Luis
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
#todo creating the randomness of the questions
import random 

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
# ADD DESCRIPTION TO THE SCENARIOS
outside = {
    "name": "outside",
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

basketball_court = { #basketball court
    "name":"basketball court",
    "type":"scenario",
    "description": " ",
}

#todo timer for the game as a watch item

#all_scenarios = [classroom, outside]
#all_portals = [portal_a]


# define which items/rooms are related

# if its a room, everything inside the room
# if its a furniture, everything inside the furniture
# if it is a door, the two rooms the door connects. From where to where!

#todo Ive added the questions to the object_relations dictionary so we can access them in the game.
# CODE FOR RANDOM QUESTIONS -> [ questions_dict[random.choice(list(questions_dict.keys()))]

object_relations = {
    "computer": [ questions_dict["question_4"], pill_blue,], 
    "fitting area": [questions_dict["question_2"], pill_red,],
    "training pads container": [questions_dict["question_3"],pill_green],
    #"grooming supplies stand": [questions_dict["question_3"],pill_yellow], 
    "hot dog stand": [questions_dict["question_1"],pill_yellow],
    "classroom": [backpack, computer, portal_blue],
    "shoe store": [portal_blue, portal_red, portal_green, fitting_area],
    "pet store": [training_pads_container, grooming_supplies_stand, portal_red],
    "basketball court": [hot_dog_stand, portal_yellow, portal_green],
    "outside": [portal_yellow],
    "blue portal": [classroom, shoe_store],
    "red portal": [shoe_store, pet_store,shoe_store],
    "green portal": [basketball_court, shoe_store],
    "yellow portal": [basketball_court, outside ]
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_scenario": classroom,
    "pills_collected": [],
    "target_scenario": outside,
}

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

# pygame.mixer.music.stop() #! uncomment and run to stop the music

# %%
# FONT COLOR

def text_in_color(color, style, text):
    
    # ANSI color codes (foreground)
    colors = {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
        "white": 37,
        "reset": 0,  # Reset color
    }

    # ANSI style codes
    styles = {
        "regular": 0,  # Default (no styling)
        "bold": 1,
        "underline": 4,
        "italic": 3,
        "reverse": 7,
        "blink": 5,
    }

    # Get the color code
    color_code = colors.get(color.lower(), 37)  # Default to white if invalid color

    # Get the style code
    style_code = styles.get(style.lower(), 0)  # Default to regular if invalid style

    # Return the combined ANSI code
    if style == "background":
      # only for background since syntax is different and color is +10
      return f"\033[{color_code+10}m{text}\033[0m"
    else:  
      return f"\033[{style_code};{color_code}m{text}\033[0m"

#? HOW TO USE?
#* Invoke the function to get the string in color returned. Concatenate with another string or print directly.

# example =>  print( "Hello " + text_color("red", "bold", "World!") )
# ...or =>    print( f"Hello {text_color("red", "bold", "World!")}" )

#* Colors and Font Styles available:

# Colors: black, red, green, yellow, blue, magenta, cyan, white, reset
# Styles: regular, bold, underline, italic, reverse, blink, background

# %%
# IMAGE PROCESSING

import platform # for determining userOS
import subprocess # to run extra terminal commands
import shutil  # for checking if imgcat is available

def show_image(img_path):
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

#? HOW TO USE?
# Invoke function show_image and pass image path.
# Example => show_image("test.jpg")
#! IMPORTANT: Only works on terminals (not VS code nested terminal) and by running the .py file

# %%
import time

def start_timer(total_time):
    """
    Start a countdown timer for the given number of seconds.
    Returns False if time runs out, True otherwise.
    """
    print(f"Game Timer Started! You have {total_time} seconds to escape!")
    
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        remaining_time = total_time - int(elapsed_time)
        
        if remaining_time <= 0:
            print("\nTime's up! You didn't escape in time!")
            return False
        
        print(f"Time Remaining: {remaining_time} seconds", end='\r')
        time.sleep(1)  # Wait for 1 second
    
    return True


# %%
# GAME FUNCTIONS

def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    linebreak() # break lines for the game start
    print( f"The classroom has been taken over by {text_in_color("cyan", "bold", "iDavid")}, who is a Teacher at {text_in_color("cyan", "bold", "IRONHACK")} with sinister intentions. He seems to have locked everyone inside and left cryptic clues all over the classroom. The lights blink, and strange whispers echo through the air. A clock on the wall ticks loudly, counting down to something threatening." )
    linebreak()
    print(f"But there is hope. You are the only one among your classmates who holds the power to free them. To do this, you must embark on a journey through mysterious scenarios. In each scenario, you need will need to find several {text_in_color("magenta", "bold", "pills")}. These {text_in_color("magenta", "bold", "pills")} will not only open {text_in_color("cyan", "bold", "portals")} to your next challenges but will also bring you closer to {text_in_color("green", "bold", "freeing all your classmates.")}") 
    linebreak()
    user_input = input(f"{text_in_color("white", "underline", "Will you accept the challenge?")} type: {text_in_color("green", "bold", "'yes'")} or {text_in_color("red", "bold", "'no'")} ")

    if user_input == "yes":
        play_scenario(game_state["current_scenario"])
    else:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        print(f"That's too bad. {text_in_color("cyan", "bold", "iDavid")} seems to {text_in_color("red", "bold", "shut down...")} you are now alone in the room and all the portals have closed for good, {text_in_color("red", "bold", "there is no way to leave")}. You are bound to study Data Science for the rest of your life.")
        linebreak()


# game termination
def play_scenario(scenario):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """

    game_state["current_scenario"] = scenario
    if(game_state["current_scenario"] == game_state["target_scenario"]):
        print(f"{text_in_color("magenta", "bold", "Congrats!")} You answered all the questions in each scenario and {text_in_color("magenta", "bold", "freed all your classmates!")}")
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        return  

    else:
        print("You seem to be in a " + text_in_color("blue", "bold", scenario["name"]) + ". " + scenario["description"])
        intended_action = input(f"What would you like to do? Type {text_in_color("yellow", "bold", "'explore'")} or {text_in_color("yellow", "bold", "'examine'")}? ").strip().lower()
        if intended_action == "explore":
            explore_scenario(scenario)
            play_scenario(scenario)
        elif intended_action == "examine":
            examine_item(input(f"What would you like to {text_in_color("yellow", "bold", "'examine' ")}? ").strip().lower())
        else:
            print(f"{text_in_color("red", "bold", "Not sure what you mean")}. Type {text_in_color("yellow", "bold", "'explore'")} or {text_in_color("yellow", "bold", "'examine'")}.")
            play_scenario(scenario)
        linebreak()

def explore_scenario(scenario):
    """
    Explore a room. List all items belonging to this room.
    """
    explore_message = f"You decide to {text_in_color("yellow", "bold", "'explore'")} around and find the following: "
    for item in object_relations[scenario["name"]]:
      explore_message += text_in_color("magenta", "bold", str(item["name"])) + ", "
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
            output = "You examine " + text_in_color("magenta", "bold", item_name) + ". "
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
                    user_input = input(f"{text_in_color("white", "underline", question_dict['question'])} ").strip().lower()
                    if(user_input == question_dict['answer']):
                        item_found = object_relations[item["name"]].pop() #It's removing the key from the object_relations
                        game_state["pills_collected"].append(item_found)
                        output += f"You answered the question {text_in_color("green", "bold", "correctly!")} take the " + text_in_color("magenta", "bold", item_found["name"]) + "."
                    else: 
                        output += f"You answered the question {text_in_color("red", "bold", "incorrectly!")} Try again."
                else:
                    output += text_in_color("red", "bold", "There isn't anything interesting about it.")
            print(output)
            break

    if(output is None):
        print(f"The item you requested is {text_in_color("red", "bold", "not found")} in the current scenario.")
    
    if(next_scenario and input(f"Do you want to go to the next scenario? Enter {text_in_color("green", "bold", "'yes'")} or {text_in_color("red", "bold", "'no'")} ").strip() == 'yes'):
        play_scenario(next_scenario)
    else:
        play_scenario(current_scenario)

# %%
# GAME START LOGIC
game_state = INIT_GAME_STATE.copy()

start_game()

# Start the check_user_input function in a separate thread
# input_thread = threading.Thread(target=check_user_input, daemon=True)
# input_thread.start()
        


