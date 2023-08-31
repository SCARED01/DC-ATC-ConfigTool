import json
import os
import time
import sys
import tkinter as tk
from tkinter import filedialog
os.system('cls' if os.name == 'nt' else 'clear')
with open('paths.json', 'r+') as u:
        paths = json.load(u)
filepath = paths[0]["electronic_flight_strips_config"]
if filepath == "":
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilepath()
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




menu = """    0. Go back
    1. Profile Name
    2. Callsing
    3. IP Address
    4. Port
    5. Strip Defaults
Select entry: """

def profile_select():
    while True:
        print("What profile do you want to edit? \n")
        for i in range(len(data)):
            sys.stdout.write(str(i+1) +"." + data[i]["profile_name"] + "\n")
        print(f"{len(data)+1}" + ".Configure")
        print("Select option: ", end ="")
        selected_profile = input("")
        if selected_profile == str(len(data)+1):
            os.system('cls' if os.name == 'nt' else 'clear')
            configuration_menu()
        else:
            try:
                selected_profile = int(selected_profile)
                os.system('cls' if os.name == 'nt' else 'clear')
                main_menu(selected_profile)
                break
            except Exception as e:
                print("Nothing selected try again!")
                selected_profile = None
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
def main_menu(selected_profile):

    while True:
        print("what do you want to edit?")

        print("Selected Profile: " + str(selected_profile) +". " + data[selected_profile-1]["profile_name"])
        print(menu, end="")
        menu_select = input("")
        try:
            menu_select = int(menu_select)
        except Exception as e:
            menu_select = None
            print("Nothing selected try again!")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        if menu_select is not None:
            if menu_select not in range(len(menu.split("\n"))+1):
                print("This number is unavailable!")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            if menu_select == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                profile_select()
                break
            if menu_select == 1:
                # Profile Name
                os.system('cls' if os.name == 'nt' else 'clear')
                old_name = data[selected_profile-1]["profile_name"]
                print("Selction: 1. Profile name")
                print("Current profile name: "+ data[selected_profile-1]["profile_name"])
                print("""
                    

    Entern new Profile Name: """, end = "")
                try:
                    new_profile_name = input("")
                    data[selected_profile-1]["profile_name"] = new_profile_name
                    os.remove(filepath)
                    with open(filepath, 'w') as f:
                        json.dump(data, f, indent=4)
                    print(f"Sucessfully changed profile name from {old_name} to {new_profile_name}!")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                except Exception as e:
                    print(e)

            if menu_select == 2:
                # Callsign
                os.system('cls' if os.name == 'nt' else 'clear')
                old_callsign = data[selected_profile-1]["callsign"]
                print("Selction: 2. Callsign")
                print("Current callsign: "+ data[selected_profile-1]["callsign"])
                print("""
                    

    Entern new Callsign: """, end = "")
                try:
                    new_callsign = input("")
                    data[selected_profile-1]["callsign"] = new_callsign
                    os.remove(filepath)
                    with open(filepath, 'w') as f:
                        json.dump(data, f, indent=4)
                    print(f"Sucessfully changed callsign from {old_callsign} to {new_callsign}!")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                except Exception as e:
                    print(e)
            if menu_select == 3:
                # IP Address
                os.system('cls' if os.name == 'nt' else 'clear')
                old_address = data[selected_profile-1]["ip"]
                print("Selction: 3. IP Address")
                print("Current IP Address: "+ data[selected_profile-1]["ip"])
                print("""
                    

    Entern new IP Address: """, end = "")
                try:
                    new_address= input("")
                    data[selected_profile-1]["ip"] = new_address
                    os.remove(filepath)
                    with open(filepath, 'w') as f:
                        json.dump(data, f, indent=4)
                    print(f"Sucessfully changed IP Address from {old_address} to {new_address}!")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                except Exception as e:
                    print(e)
            if menu_select == 4:
                # Port
                os.system('cls' if os.name == 'nt' else 'clear')
                old_port = data[selected_profile-1]["port"]
                print("Selction: 3. Port")
                print("Current Port: "+ data[selected_profile-1]["port"])
                print("""
                    

    Entern new Port: """, end = "")
                try:
                    new_port= input("")
                    data[selected_profile-1]["port"] = new_port
                    os.remove(filepath)
                    with open(filepath, 'w') as f:
                        json.dump(data, f, indent=4)
                    print(f"Sucessfully changed port from {old_port} to {new_port}!")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                except Exception as e:
                    print(e)
            if menu_select == 5:
                # Defaults
                os.system('cls' if os.name == 'nt' else 'clear')
                strip_default_menu(selected_profile)
                break
                
def strip_default_menu(selected_profile):
    # This menu configures the Flight Strip defaults that are assigned to every newly created flight strip
    while True:
        print("Selection 5. Strip Defaults \n")
        strip_default = """
        Here you can set the defaults this profile applies to every newly created Flight Strip.
        
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
            # incase user selcts nothing
            print(e)
            strip_default_select = None
            print("Nothing selected try again!")
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
                data[selected_profile-1]["strip_defaults"]["callsign"] = new_default_callsign
                os.remove(filepath)
                with open(filepath, 'w') as f:
                    json.dump(data, f, indent=4)
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
                    os.remove(filepath)
                    with open(filepath, 'w') as f:
                        json.dump(data, f, indent=4)
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
                    os.remove(filepath)
                    with open(filepath, 'w') as f:
                        json.dump(data, f, indent=4)
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
                    os.remove(filepath)
                    with open(filepath, 'w') as f:
                        json.dump(data, f, indent=4)
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
                if new_type == "0":
                    #open browser
                    pass
                data[selected_profile-1]["strip_defaults"]["type"] = new_type
                os.remove(filepath)
                with open(filepath, 'w') as f:
                    json.dump(data, f, indent=4)
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
                data[selected_profile-1]["strip_defaults"]["fligt_size"] = new_flight_size
                os.remove(filepath)
                with open(filepath, 'w') as f:
                    json.dump(data, f, indent=4)
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
                        os.remove(filepath)
                        with open(filepath, 'w') as f:
                            json.dump(data, f, indent=4)
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
                        os.remove(filepath)
                        with open(filepath, 'w') as f:
                            json.dump(data, f, indent=4)
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
                if new_spd == "1":
                    data[selected_profile-1]["strip_defaults"]["alt"] = "SXXX"
                try:
                    new_spd_int = int(new_heading.split("S"))
                except:
                    pass
                if new_spd.startswith("S"):
                    if new_spd.split("S")[1] == "XXX" or new_spd_int % 5 == 0:
                        data[selected_profile-1]["strip_defaults"]["alt"] = new_alt
                        os.remove(filepath)
                        with open(filepath, 'w') as f:
                            json.dump(data, f, indent=4)
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

        if entry == "1":
            print("""
    Select the default departure airport for new Flight Strips:
                  Recomended to input ICAO code for Airport
                  Ex. Anapa Vityazevo Code: URKA
                  
""", end = "")
            departure = input("Enter Departure Airport: ")
            data[selected_profile-1]["strip_defaults"]["flight_plan"]["departure"] = departure.upper()
            os.remove(filepath)
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=4)
        if entry == "2":
            print("""
    Select the default arrival airport for new Flight Strips:
                  Recomended to input ICAO code for Airport
                  Ex. Anapa Vityazevo Code: URKA
                  
""", end = "")
            arrival = input("Enter Arrical Airport: ")
            data[selected_profile-1]["strip_defaults"]["flight_plan"]["arrival"] = arrival.upper()
            os.remove(filepath)
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=4)
        if entry == 3:
            print("""
    Select the default route for new Flight Strips:
                  Ex. Anapa to Gelendzhig: TUNO1E TUNOT W343 DOROL DORO4A
                  Seperate Waypoints with spaces
                  
""", end = "")           
            route = input("Enter Route: ")
            data[selected_profile-1]["strip_defaults"]["flight_plan"]["route"] = route.upper()
            os.remove(filepath)
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=4)
        if entry == 4:
            print("""
    Select the default equipment for new Flight Strips:
                  (ICAO Equipment codes)
                  Ex. Tacan: T, ILS: L, INS: I
                  Combine with no spaces (Ex. TLI)
                  
""", end = "")           
            equipment = input("Enter Equipment: ")
            data[selected_profile-1]["strip_defaults"]["flight_plan"]["equipment"] = equipment.upper()
            os.remove(filepath)
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=4)
        if entry == 5:
            print("""
    Select the default planned cruise altitude for new Flight Strips:
                  
""", end = "")           
            altitude = input("Enter default planned cruise altitude: ")
            try:
                alt_int=int(altitude)
            except:
                print("Altitude can only be a number")
            data[selected_profile-1]["strip_defaults"]["flight_plan"]["altitude"] = altitude
            os.remove(filepath)
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=4)
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
    if selection == "1":
        file_path = filedialog.askopenfilepath()
        paths[0]["electronic_flight_strips_config"] = file_path
        os.remove('paths.json')
        with open('paths.json', 'w') as u:
            json.dump(paths, u, indent=4)
if __name__ == "__main__":
    profile_select()


    # data['id'] = 134 # <--- add `id` value.
