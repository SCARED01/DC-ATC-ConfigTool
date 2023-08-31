import json
import os
import time
import sys
import tkinter as tk
from tkinter import filedialog
from rich.console import Console
from rich.style import Style
from rich.color import Color
import re


os.system('cls' if os.name == 'nt' else 'clear')
with open('paths.json', 'r+') as u:
        paths = json.load(u)
filepath = paths[0]["electronic_flight_strips_config"]
if filepath == "":
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename(title="Select Config.json for Electronic Flight Strips tool.")
    paths[0]["electronic_flight_strips_config"] = filepath
    os.remove('paths.json')
    with open('paths.json', 'w') as u:
        json.dump(paths, u, indent=4)
with open(filepath, 'r+') as f:
    data = json.load(f)



# INOP
# def draw_menu(entries=[], headline1=None, headline2=None):
#     if headline1 != None:
#         print(headline1)
#     if headline2 != None:
#         print(headline2)
#     menu = """"""
#     for idx in range(len(entries)):
#         menu = menu + "    "+ str(idx) +". " + entries[idx] + "\n"
#     print(menu + "Select Entry: ", end="")

def write_config():
    try:
        os.remove(filepath)
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
    except KeyboardInterrupt:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
def exit_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
 ________             __     __  __            ___                    _             __  __   _       __            ____
/_  __/ /  ___ ____  / /__   \ \/ /__  __ __  / _/__  ____  __ _____ (_)__  ___ _  / /_/ /  (_)__   / /____  ___  / / /
 / / / _ \/ _ `/ _ \/  '_/    \  / _ \/ // / / _/ _ \/ __/ / // (_-</ / _ \/ _ `/ / __/ _ \/ (_-<  / __/ _ \/ _ \/ /_/ 
/_/ /_//_/\_,_/_//_/_/\_\     /_/\___/\_,_/ /_/ \___/_/    \_,_/___/_/_//_/\_, /  \__/_//_/_/___/  \__/\___/\___/_(_)  
                                                                          /___/                                        
""")
    print("""
                    Any issues? Open an issue on github:
                    https://github.com/SCARED01/DC-ATC-ConfigTool/issues
          """)
    exit()


menu = """    0. Go back
    1. Profile Name
    2. Callsing
    3. IP Address
    4. Port
    5. Strip Defaults
    6. Color Menu
Select entry: """

def profile_select():
    os.system("mode 121,30" if os.name == "nt" else "resize 30 121")
    while True:
        print("""
   ___  _      _ __       __  _____          __           ____       _        ___ ___________   ______          __  
  / _ \(_)__ _(_) /____ _/ / / ___/__  ___  / /________  / / /__ ___( )___   / _ /_  __/ ___/__/_  __/__  ___  / /__
 / // / / _ `/ / __/ _ `/ / / /__/ _ \/ _ \/ __/ __/ _ \/ / / -_) __//(_-<  / __ |/ / / /__/___// / / _ \/ _ \/ (_-<
/____/_/\_, /_/\__/\_,_/_/  \___/\___/_//_/\__/_/  \___/_/_/\__/_/   /___/ /_/ |_/_/  \___/    /_/  \___/\___/_/___/
       /___/____          ____                    __  _             ______          __                              
          / ___/__  ___  / _(_)__ ___ _________ _/ /_(_)__  ___    /_  __/__  ___  / /                              
         / /__/ _ \/ _ \/ _/ / _ `/ // / __/ _ `/ __/ / _ \/ _ \    / / / _ \/ _ \/ /                               
         \___/\___/_//_/_//_/\_, /\_,_/_/  \_,_/\__/_/\___/_//_/   /_/  \___/\___/_/                                
                            /___/                                                                                   
""")
        print("""
            Welcome! This is a commandline based configuration tool for the Electronic Flight Strips tool by the 
            Digital Controllers: https://github.com/Digital-Controllers/DCS-ATC-Tools
              
            Version 0.1
            
            If at any point you want to exit this tool, instead of selecting an option type exit.
              
            Any Issues? Open an issue on github:  https://github.com/SCARED01/DC-ATC-ConfigTool/issues
""")
        print("What profile do you want to edit? \n")
        for i in range(len(data)):
            sys.stdout.write(str(i+1) +"." + data[i]["profile_name"] + "\n")
        print(f"{len(data)+1}" + ".Configure")
        print("Select option: ", end ="")
        selected_profile = input("")
        try:
            selected_profile_int = int(selected_profile)
        except:
            print(f"Please Enter a number from 1 to {len(data)+1}")
        if selected_profile == str(len(data)+1):
            os.system('cls' if os.name == 'nt' else 'clear')
            configuration_menu()
        elif selected_profile == "exit":
            write_config()
            exit_screen()
            
        else:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                main_menu(selected_profile_int)
                break
            except Exception as e:
                print("Nothing selected try again!")
                print("Im there")
                selected_profile = None
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
def main_menu(selected_profile):

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("what do you want to edit?")

        print("Selected Profile: " + str(selected_profile) +". " + data[selected_profile-1]["profile_name"])
        print(menu, end="")
        menu_select = input("")
        try:
            menu_select = int(menu_select)
        except Exception as e:
            if menu_select == "exit":
                write_config()
                exit_screen()
            else:
                menu_select = None
                print(e)
                print("Nothing selected try again! Enter a valid number from 1 to 6!")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
        if menu_select is not None:
            if menu_select > len(menu.split("\n"))-2:
                print("This number is unavailable!")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            elif menu_select == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                profile_select()
                break
            elif menu_select == 1:
                # Profile Name
                os.system('cls' if os.name == 'nt' else 'clear')
                old_name = data[selected_profile-1]["profile_name"]
                print("Selction: 1. Profile name")
                print("Current profile name: "+ data[selected_profile-1]["profile_name"])
                print("""
                    

    Entern new Profile Name: """, end = "")
                try:
                    new_profile_name = input("")
                    if new_profile_name == "exit":
                        write_config()
                        exit_screen()
                    else:
                        data[selected_profile-1]["profile_name"] = new_profile_name
                        write_config()
                        print(f"Sucessfully changed profile name from {old_name} to {new_profile_name}!")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                except Exception as e:
                    print(e)

            elif menu_select == 2:
                # Callsign
                os.system('cls' if os.name == 'nt' else 'clear')
                old_callsign = data[selected_profile-1]["callsign"]
                print("Selction: 2. Callsign")
                print("Current callsign: "+ data[selected_profile-1]["callsign"])
                print("""
                    

    Entern new Callsign: """, end = "")
                try:
                    new_callsign = input("")
                    if new_callsign == "exit":
                        write_config()
                        exit_screen()
                    else:
                        data[selected_profile-1]["callsign"] = new_callsign
                        write_config()
                        print(f"Sucessfully changed callsign from {old_callsign} to {new_callsign}!")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                except Exception as e:
                    print(e)
            elif menu_select == 3:
                # IP Address
                os.system('cls' if os.name == 'nt' else 'clear')
                old_address = data[selected_profile-1]["ip"]
                print("Selction: 3. IP Address")
                print("Current IP Address: "+ data[selected_profile-1]["ip"])
                print("""
                    

    Entern new IP Address: """, end = "")
                try:
                    new_address= input("")
                    if new_address == "exit":
                        write_config()
                        exit_screen()
                    else:
                        data[selected_profile-1]["ip"] = new_address
                        write_config()
                        print(f"Sucessfully changed IP Address from {old_address} to {new_address}!")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                except Exception as e:
                    print(e)
            elif menu_select == 4:
                # Port
                os.system('cls' if os.name == 'nt' else 'clear')
                old_port = data[selected_profile-1]["port"]
                print("Selction: 4. Port")
                print("Current Port: "+ str(data[selected_profile-1]["port"]))
                print("""
                    

    Enter new Port: """, end = "")
                new_port= input("")
                if new_port == "exit":
                    write_config()
                    exit_screen()
                else:
            # try:
                #     new_port_int = int(new_port)
                # except:
                #     print("Please enter a valid Port!")
                    try:
                        new_port_int = int(new_port)
                    except:
                        print("Invalid Port! Please enter a valid port (ex. 6002)")
                    try:

                        data[selected_profile-1]["port"] = new_port_int
                        write_config()
                        print(f"Sucessfully changed port from {old_port} to {new_port}!")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                    except Exception as e:
                        print(e)
            elif menu_select == 5:
                # Defaults
                os.system('cls' if os.name == 'nt' else 'clear')
                strip_default_menu(selected_profile)
                break
            elif menu_select == 6:
                # Defaults
                os.system('cls' if os.name == 'nt' else 'clear')
                color_menu(selected_profile)
                break
                
def strip_default_menu(selected_profile):
    # This menu configures the Flight Strip defaults that are assigned to every newly created flight strip
    while True:
        print("Selection 5. Strip Defaults \n")
        strip_default = """
        Here you can set the defaults this profile applies to every newly created Flight Strip.

            0. Go back
            1. Default Callsing(Ex. Hawk 1-1)
            2. Default Flight Rules(IFR/VFR)
            3. Default Service
            4. Default Category (Departuring/Arriving)
            5. Default Type (F16,F18)
            6. Default Flight Size(X-Ship)
            7. Default Heading (HXXX)
            8. Default Altitude (AXXX)
            9. Default Speed (SXXX)
            10.Default Flight Plan (Route/Equipment)
            
"""
        print(strip_default)
        print("Select Entry: ", end="")
        strip_default_select = input("")
        try:
            #test for user input is number
            strip_default_select = int(strip_default_select)
        except Exception as e:
            if strip_default_select == "exit":
                write_config()
                exit_screen()
            else:
                # incase user selcts nothing
                print(e)
                strip_default_select = None
                print("Nothing selected try again!")
                print("Im here")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
        if strip_default_select == 0:
            # back one menu
            os.system('cls' if os.name == 'nt' else 'clear')
            main_menu(selected_profile)

            break
        if strip_default_select == 1:
            # default callsign for every flight strip that is created
            os.system('cls' if os.name == 'nt' else 'clear')
            old_default_callsign = data[selected_profile-1]["strip_defaults"]["callsign"]
            print("1. Default Callsign")
            print("Current default callsign: " + old_default_callsign)
            print("""
                

Entern default callsign: """, end = "")
            try:
                #take user input, and clear screen
                new_default_callsign= input("")
                if new_default_callsign == "exit":
                    write_config()
                    exit_screen()
                else:
                    data[selected_profile-1]["strip_defaults"]["callsign"] = new_default_callsign
                    write_config()
                    print(f"Sucessfully changed default callsign from {old_default_callsign} to {new_default_callsign}!")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
            except Exception as e:
                print(e)

        if strip_default_select == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            old_default_flight_rules = data[selected_profile-1]["strip_defaults"]["flight_rules"]
            print("2. Default Flight Rules")
            print("Current Default Flight Rules: " + old_default_flight_rules)
            print("""
    Select the default Flight Rules for new Flight Strips:
            1.VFR
            2.IFR                    
""", end = "")
            try:
                new_default_flight_rules= input("Select Entry: ")
                if new_default_flight_rules == "exit":
                    write_config()
                    exit_screen()
                else:
                    if new_default_flight_rules == "1":
                        data[selected_profile-1]["strip_defaults"]["flight_rules"] = "VFR"
                        new_default_flight_rules = "VFR"
                    if new_default_flight_rules == "2":
                        data[selected_profile-1]["strip_defaults"]["flight_rules"] = "IFR"
                        new_default_flight_rules = "IFR"
                    else:
                        print("Invalid Input. Please select one of the options above!")
                        data[selected_profile-1]["strip_defaults"]["service"] = old_default_flight_rules
                    if new_default_flight_rules == "1" or new_default_flight_rules == "2":
                        write_config()
                    print(f"Sucessfully changed default Flight Rules from {old_default_flight_rules} to {new_default_flight_rules}!")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
            except Exception as e:
                print(e)
        if strip_default_select == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            old_default_service = data[selected_profile-1]["strip_defaults"]["service"]
            print("3. Default Service")
            print("Current Default Service: " + old_default_service)
            print("""
    Select the default Service for new Flight Strips:
                    1.N
                    2.Y                  
""", end = "")
            
            try:
                new_default_service= input("Select Entry: ")
                if new_default_service == "exit":
                    write_config()
                    exit_screen()
                else:
                    if new_default_service == "1":
                        data[selected_profile-1]["strip_defaults"]["service"] = "N"
                        new_default_service = "N"
                    if new_default_service == "2":
                        data[selected_profile-1]["strip_defaults"]["service"] = "Y"
                        new_default_service = "Y"
                    else:
                        print("Invalid input. Please select one of the options above!")
                        data[selected_profile-1]["strip_defaults"]["service"] = old_default_service
                    if new_default_service == "1" or new_default_service == "2":
                        write_config()
                    print(f"Sucessfully changed default Service from {old_default_service} to {new_default_service}!")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
            except Exception as e:
                print(e)
        if strip_default_select == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            old_default_category = data[selected_profile-1]["strip_defaults"]["service"]
            print("""
    Select the default Catergory for new Flight Strips:
                    1.Departing
                    2.Arriving               
""", end = "")
            
            try:
                new_default_category= input("Select Entry: ")
                if new_default_category == "exit":
                    write_config()
                    exit_screen()
                else:
                    if new_default_category == "1":
                        data[selected_profile-1]["strip_defaults"]["category"] = "Departing"
                        new_default_category = "Departing"
                    if new_default_category == "2":
                        data[selected_profile-1]["strip_defaults"]["category"] = "Arriving"
                        new_default_category = "Arriving"
                    else:
                        print("Invalid input. Please select one of the options above!")
                        data[selected_profile-1]["strip_defaults"]["service"] = old_default_category
                    if new_default_service == "1" or new_default_service == "2":
                        write_config()
                    print(f"Sucessfully changed default Service from {old_default_category} to {new_default_category}!")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
            except Exception as e:
                print(e)
        if strip_default_select == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            old_type = data[selected_profile-1]["strip_defaults"]["type"]
            print("""
    Select the default Type for new Flight Strips:  
                0. What types are available?
                        
""", end = "")
            try:
                new_type= input("Enter Type: ")
                if new_type == "exit":
                    write_config()
                    exit_screen()
                else:
                    if new_type == "0":
                        #open browser
                        pass
                    data[selected_profile-1]["strip_defaults"]["type"] = new_type
                    write_config()
                    print(f"Sucessfully changed default Service from {old_type} to {new_type}!")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
            except Exception as e:
                print(e)
        if strip_default_select == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            old_flight_size = data[selected_profile-1]["strip_defaults"]["flight_size"]
            print("""
    Select the default Flight Size for new Flight Strips:
                        
""", end = "")
            try:
                new_flight_size= input("Enter Flight Size: ")
                if new_flight_size == "exit":
                    write_config()
                    exit_screen()
                else:
                    data[selected_profile-1]["strip_defaults"]["fligt_size"] = new_flight_size
                    write_config()
                    print(f"Sucessfully changed default flight size from {old_flight_size} to {new_flight_size}!")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
            except Exception as e:
                print(e)
        if strip_default_select == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("""
    Select the default Heading for new Flight Strips:
    Format: HXXX (Ex.: H250)
    (Headings are specified in increments of 5)
    000 is 360
                  
    Quick Access:
        1. HXXX(Undifined/To be assigned)
        2. HRWY (Runway Heading)
""", end = "")
            old_headign = data[selected_profile-1]["strip_defaults"]["hdg"]
            try:
                new_heading= input("Enter Heading: ")
                if new_heading == "exit":
                    write_config()
                    exit_screen()
                else:
                    if new_alt == "1":
                        data[selected_profile-1]["strip_defaults"]["hdg"] = "HXXX"
                    if new_alt == "2":
                        data[selected_profile-1]["strip_defaults"]["hdg"] = "HRWY"
                    if new_heading.startswith("H"):
                        try:
                            new_heading_int = int(new_heading.split("H"))
                        except:
                            pass
                        if new_heading.split("H")[1] == "XXX" or new_heading.split("H")[1] == "RWY" or new_heading_int % 5 == 0:
                            data[selected_profile-1]["strip_defaults"]["hdg"] = new_heading
                            write_config()
                            print(f"Sucessfully changed default heading from {old_headign} to {new_heading}!")
                            time.sleep(1)
                            os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            print("Invalid heading please use the correct format!")
                            time.sleep(1)
                            os.system('cls' if os.name == 'nt' else 'clear')
                    else:
                        print("Invalid heading please use the correct format!")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
            except Exception as e:
                print("Invalid heading please use the correct format!")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
        if strip_default_select == 8:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("""
    Select the default Altitute for new Flight Strips:
    Format: AXXX (Ex.: A250 *FL250*)
    Quick Access:
        1. AXXX(Undifined/To be assigned)
        2. AGLS(Ground Level)
""", end = "")
            old_alt = data[selected_profile-1]["strip_defaults"]["alt"]
            try:
                new_alt= input("Enter Altitude: ")
                if new_alt == "exit":
                    write_config()
                    exit_screen()
                else:
                    if new_alt == "1":
                        data[selected_profile-1]["strip_defaults"]["alt"] = "AXXX"
                    if new_alt == "2":
                        data[selected_profile-1]["strip_defaults"]["alt"] = "AGLS"
                    try:
                        new_alt_int = int(new_heading.split("A"))
                    except:
                        pass
                    if new_alt.startswith("A"):
                        if new_alt.split("A")[1] == "XXX" or new_alt.split("A")[1] == "GLS" or new_alt_int % 5 == 0:
                            data[selected_profile-1]["strip_defaults"]["alt"] = new_alt
                            write_config()
                            print(f"Sucessfully changed default altitude from {old_alt} to {new_alt}!")
                            time.sleep(1)
                            os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            print("Invalid altitude please use the correct format!")
                            time.sleep(1)
                            os.system('cls' if os.name == 'nt' else 'clear')
                    else:
                        print("Invalid altitude please use the correct format!")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
            except Exception as e:
                print("Invalid altitude please use the correct format!")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
        if strip_default_select == 9:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("""
    Select the default speed for new Flight Strips:
    Format: SXXX (Ex.: S250 *250kts*)
    Quick Access:
        1. SXXX(Undifined/To be assigned)
""", end = "")
            old_spd = data[selected_profile-1]["strip_defaults"]["alt"]
            try:
                new_spd= input("Enter Altitude: ")
                if new_spd == "exit":
                    write_config()
                    exit_screen()
                else:
                    if new_spd == "1":
                        data[selected_profile-1]["strip_defaults"]["alt"] = "SXXX"
                    try:
                        new_spd_int = int(new_heading.split("S"))
                    except:
                        pass
                    if new_spd.startswith("S"):
                        if new_spd.split("S")[1] == "XXX" or new_spd_int % 5 == 0:
                            data[selected_profile-1]["strip_defaults"]["alt"] = new_alt
                            write_config()
                            print(f"Sucessfully changed default speed from {old_spd} to {new_spd}!")
                            time.sleep(1)
                            os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            print("Invalid speed please use the correct format!")
                            time.sleep(1)
                            os.system('cls' if os.name == 'nt' else 'clear')
                    else:
                        print("Invalid speed please use the correct format!")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
            except Exception as e:
                print("Invalid speed please use the correct format!")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
        if strip_default_select == 10:
            os.system('cls' if os.name == 'nt' else 'clear')
            default_flight_plan(selected_profile)
            break

def default_flight_plan(selected_profile):
    while True:
        print("""10./6. Flight Plan defaults
              
                    1. Departure Airport
                    2. Arrival Airport
                    3. Route
                    4. Equipment
                    5. Altitude
              """)
        print("Select entry: ", end ="")
        entry = input("")
        if entry == "exit":
            write_config()
            exit_screen()
        if entry == "1":
            print("""
    Select the default departure airport for new Flight Strips:
                  Recomended to input ICAO code for Airport
                  Ex. Anapa Vityazevo Code: URKA
                  
""", end = "")
            departure = input("Enter Departure Airport: ")
            if departure == "exit":
                write_config()
                exit_screen()
            else:
                data[selected_profile-1]["strip_defaults"]["flight_plan"]["departure"] = departure.upper()
                write_config()
        if entry == "2":
            print("""
    Select the default arrival airport for new Flight Strips:
                  Recomended to input ICAO code for Airport
                  Ex. Anapa Vityazevo Code: URKA
                  
""", end = "")
            arrival = input("Enter Arrical Airport: ")
            if arrival == "exit":
                write_config()
                exit_screen()
            else:
                data[selected_profile-1]["strip_defaults"]["flight_plan"]["arrival"] = arrival.upper()
                write_config()
        if entry == 3:
            print("""
    Select the default route for new Flight Strips:
                  Ex. Anapa to Gelendzhig: TUNO1E TUNOT W343 DOROL DORO4A
                  Seperate Waypoints with spaces
                  
""", end = "")           
            route = input("Enter Route: ")
            if route == "exit":
                write_config()
                exit_screen()
            else:
                data[selected_profile-1]["strip_defaults"]["flight_plan"]["route"] = route.upper()
                write_config()
        if entry == 4:
            print("""
    Select the default equipment for new Flight Strips:
                  (ICAO Equipment codes)
                  Ex. Tacan: T, ILS: L, INS: I
                  Combine with no spaces (Ex. TLI)
                  
""", end = "")           
            equipment = input("Enter Equipment: ")
            if equipment == "exit":
                write_config()
                exit_screen()
            else:
                data[selected_profile-1]["strip_defaults"]["flight_plan"]["equipment"] = equipment.upper()
                write_config()
        if entry == 5:
            print("""
    Select the default planned cruise altitude for new Flight Strips:
                  
""", end = "")           
            altitude = input("Enter default planned cruise altitude: ")
            if altitude == "exit":
                write_config()
                exit_screen()
            else:
                try:
                    alt_int=int(altitude)
                except:
                    print("Altitude can only be a number")
                # needs fixing to only write valid altitude
                data[selected_profile-1]["strip_defaults"]["flight_plan"]["altitude"] = altitude
                write_config()
def configuration_menu():

    print("CONFIGURATION MENU")
    print("__________________")
    print("""
        1. Select Electronic client config file. (In the same folder as the .exe there is a file name config.json. Select this file and load your existing config)

""")
    # root = tk.Tk()
    # root.withdraw()
    # file_path = filedialog.askopenfilepath()

    # paths[0]["electronic_flight_strips_config"] = file_path
    # os.remove('paths.json')
    # with open('paths.json', 'w') as u:
    #     json.dump(paths, u, indent=4)

    # ------------------------------------------------------------------

    selection = input("Select Option: ")
    root = tk.Tk()
    root.withdraw()
    if selection == "exit":
        write_config()
        exit_screen()
    if selection == "1":
        file_path = filedialog.askopenfilename(title="Select Config.json for Electronic Flight Strips tool.")
        paths[0]["electronic_flight_strips_config"] = file_path
        os.remove('paths.json')
        with open('paths.json', 'w') as u:
            json.dump(paths, u, indent=4)
def draw_coloured_square(hex_string):
    """
    Returns a coloured square that you can print to a terminal.
    """

    hex_string = hex_string.strip("#")
    assert len(hex_string) == 6
    red = int(hex_string[:2], 16)
    green = int(hex_string[2:4], 16)
    blue = int(hex_string[4:6], 16)

    style = Style(color=Color.from_rgb(red, green, blue))
    console = Console()
    console.print("█", style=style)

# Example usage
def color_menu(selected_profile):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        background = data[selected_profile-1]["background_color"]
        text = data[selected_profile-1]["text_color"]
        arriving = data[selected_profile-1]["categories"]["Arriving"]
        departing = data[selected_profile-1]["categories"]["Departing"]
        emerg = data[selected_profile-1]["emer_color"]
        print("7. Colour Menu")
        sys.stdout.write("     1. Background Color ")
        draw_coloured_square(background)
        sys.stdout.write("     2. Text Color       ")
        draw_coloured_square(text)
        sys.stdout.write("     3. Arriving Color   ")
        draw_coloured_square(arriving)
        sys.stdout.write("     4. Departing Color  ")
        draw_coloured_square(departing)
        sys.stdout.write("     5. Emergency Color  ")
        draw_coloured_square(emerg)
        user_select = input("Select Option: ")
        if user_select == "exit":
            write_config()
            exit_screen()
        if user_select == "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            main_menu(selected_profile)
            break
        if user_select == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("1. Background Color ")
            print("Current Hex Code: " + background)
            sys.stdout.write("Current color: ")
            draw_coloured_square(background)
            print("""
                Enter a new Hex code or use 0 to go back one page.
                
    """)
            new_hex = input("Enter hex code: ")
            if new_hex == "exit":
                write_config()
                exit_screen()
            else:
                if new_hex == "0":
                    pass
                elif re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', new_hex):
                    data[selected_profile-1]["background_color"] = new_hex
                    write_config()
                else:
                    print("Invalid Input! Please enter valid hex color code or return to previous menu with 0.")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
        if user_select == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("1. Text Color ")
            print("Current Hex Code: " + text)
            sys.stdout.write("Current color: ")
            draw_coloured_square(text)
            print("""
                Enter a new Hex code or use 0 to go back one page.
                
    """)
            new_hex = input("Enter hex code: ")
            if new_hex == "exit":
                write_config()
                exit_screen()
            else:
                if new_hex == "0":
                    pass
                elif re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', new_hex):
                    data[selected_profile-1]["text_color"] = new_hex
                    write_config()
                else:
                    print("Invalid Input! Please enter valid hex color code or return to previous menu with 0.")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
        if user_select == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.stdout.write("1. Arriving Color ")
            print("Current Hex Code: " + arriving)
            sys.stdout.write("Current color: ")
            draw_coloured_square(arriving)
            print("""
                Enter a new Hex code or use 0 to go back one page.
                
    """)
            new_hex = input("Enter hex code: ")
            if new_hex == "exit":
                write_config()
                exit_screen()
            else:
                if new_hex == 0:
                    pass
                elif re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', new_hex):
                    data[selected_profile-1]["categories"]["Arriving"] = new_hex
                    write_config()
                else:
                    print("Invalid Input! Please enter valid hex color code or return to previous menu with 0.")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
        if user_select == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("1. Departing Color ")
            print("Current Hex Code: " + departing)
            sys.stdout.write("Current color: ")
            draw_coloured_square(departing)
            print("""
                Enter a new Hex code or use 0 to go back one page.
                
    """)
            new_hex = input("Enter hex code: ")
            if new_hex == "exit":
                write_config()
                exit_screen()
            else:
                if new_hex == "0":
                    pass
                elif re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', new_hex):
                    data[selected_profile-1]["categories"]["Arriving"] = new_hex
                    write_config()
                else:
                    print("Invalid Input! Please enter valid hex color code or return to previous menu with 0.")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
        if user_select == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("1. Emergency Color ")
            print("Current Hex Code: " + emerg)
            sys.stdout.write("Current color: ")
            draw_coloured_square(emerg)
            print("""
                Enter a new Hex code or use 0 to go back one page.
                
    """)
            new_hex = input("Enter hex code: ")
            if new_hex == "exit":
                write_config()
                exit_screen()
            else:
                if new_hex == "0":
                    pass
                elif re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', new_hex):
                    data[selected_profile-1]["emer_color"] = new_hex
                    write_config()
                else:
                    print("Invalid Input! Please enter valid hex color code or return to previous menu with 0.")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    profile_select()
