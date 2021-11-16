playing = True

while playing:
    rocket_speed = 0
    rocket_fuel = 0
    rocket_height = 0
    rocket_num_engines = 0
    print("Let's set up your spaceship!")
    rocket_fuel = int(input("\tHow many kilograms of fuel (2,000 - 100,000): "))
    rocket_num_engines = int(input("\tHowmany engines (1 - 10): "))
    print("\tHere we go! 3...2...1...Blast off!")
    while rocket_fuel > 0:
        rocket_speed += (10 * rocket_num_engines)
        rocket_speed -= rocket_num_engines
        rocket_speed -= (rocket_fuel / 1000)
        rocket_fuel = rocket_fuel - (100 * rocket_num_engines)
        rocket_height += rocket_speed
        if rocket_speed < 0:
            rocket_fuel = 0
            rocket_speed = 0
            rocket_height = 0
        else:
            print("\t\t\tspeed: " + str(rocket_speed) + "m/s, height: " + str(rocket_height) + "m")
    if rocket_height >= 50000 and rocket_speed >= 2000:
        print("\t!!!!YOU REACHED ORBIT!!!!!") 
    else:
        print("\tYou didn't reach orbit")
    print("\tship height: " + str(rocket_height) + " meters")
    print("\tship speed: " + str(rocket_speed) + " m/s") 
    if input("Play again? yes/no: ") == "no":
        playing = False 