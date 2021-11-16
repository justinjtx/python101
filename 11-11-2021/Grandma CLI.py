speak_to_grandma = input("Say something to grandma: ")

while (speak_to_grandma != "BYE"):

    if (speak_to_grandma.islower()):
        print("HUH?! SPEAK UP, SONNY!")
    elif (speak_to_grandma.isupper()):
        print("NO, NOT SINCE 1983! ")
    speak_to_grandma = input("say something to grandma: ")