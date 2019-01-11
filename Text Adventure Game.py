# Setup of the controls of the game
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]


# Introduction to the game and the story
name = input("Who are you?\n")
print("Hello, " + name + ". Let us begin.")
print("You begin your journey on the edge of a mysterious and ominous darkness that lingers not far from your family home. You've always been curious about what lies beyond it. Today; you take that bold first step.")
print("Can you find your path to the other side of the darkness and find what lies beyond?\n")

# The game's beginning
response = ""
while response not in yes_no:
    response = input("Will you step into the darkness?\nyes/no\n")
    if response == "yes":
        print("You head into the darkness. Ominous whispers attempt to crawl their way into your mind.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else:
        print("I'm sorry, what?\n")

# Main bulk of the game with all the different paths mapped out
response = ""
while response not in directions:
    print("To your left, you see a monster.")
    print("To your right, the darkness grows.")
    print("A door beckons you to step forwards")
    print("Behind you, the light seems to glow softly, calling you out of the dark.")
    response = input("What direction do you move? left/right/forward/backward")
    if response == "left":
        print("The monster chases you back out of the darkness. You decide that your curiosity isn't worth the risk and never venture into the darkness again.")
        quit()
    elif response == "right":
        print("You head deeper into the dark.\n")
        print ("To your left, a red light glows in the distance.")
        print ("To your right, strange voices call out to you.")
        print ("Ahead of you, a slow moving monster skulks around, you might be able to sneak past it.")
        print ("Behind you, you can return to where you came and travel in a different direction.")
        response = input("What direction do you move?\nleft/right/forward/backward\n")
        if response == "left":
                print ("as you move closer, you see a shape start to form of what the red glow belonged to. A giant wolf leaps out at you, chasing you back out of the dark. YOu vow never to enter it again and live out your life in peace")
                quit()
        elif response == "right":
            print ("The voice lures you further into the dark. You feel your body becomming lighter and a persistent want to follow the sound. It lures you into the dark and leaves you stranded, lost and alone in the dark. THis is where your journey ends")
            quit()
        elif response == "forward":
            print ("You move slowly and carefully manage to sneak past the beast without it noticing you")

    elif response == "forward":
        print("The door appears to be locked.\n")
        print ("To your left, something shimmers in the distance")
        print ("To your right, howls can be heard from deeper in the darkness")
        print ("behind you takes you back to where you came, maybe you can explore a different path")
        response = input ("What direction do you move?\nleft/right/backward\n")
        if response == "left":
            print ("You approach the object and discover it to be a key. I wonder if it will fit in that door... You put the key in your pocket.")
            print ("To your left, the beginning of your journey greets you")
            print ("To your right, voices whisper to you in the distance")
            print ("Ahead of you, an active monster patrols the area")
            print ("Behind you, the door beckons your return")
            response = input ("What direction do you move?\nleft/right/forward/backward\n")
            if response == "backward":
                print ("You insert the key in the door and open it. On the other side you are greeted by green fields of grass and sheep with a beautiful summer sun shining down. You have made it out of the darkness")
                quit()
    elif response == "backward":
        print("You flee the dark, returning to your dull, but safe life.")
        quit()
    else:
        print("I'm sorry, what?\n")
