#!/usr/bin/env python
# Filter bot
import chatServer as c
import random
import time
import vlc
import sys
import os

root = os.path.dirname(os.path.realpath(__file__))+"/"

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
if __name__ == "__main__":
    answer = raw_input("Do you want to restart this program ? ")
    if answer.lower().strip() in "y yes".split():
        restart_program()

# Sleep and output functions
def sleep(n):
    c.sleep(n)
def output(s):
    c.output(s)
def outputWithDelay(s, n):
    c.outputWithDelay(s, n)
def delayedCallback(n, cb):
    c.delayedCallback(n, cb)

# Setup and Response function
def setup():
    global p1, p2, p3
    global askedCounter
    global orderCounter
    global jokeCounter
    global crazyCount
    askedCounter = 0
    orderCounter = 0
    jokeCounter = 0
    crazyCount = 0
    p1 = vlc.MediaPlayer("attention.wav")
    p2 = vlc.MediaPlayer("crazy.wav")
    p3 = vlc.MediaPlayer("angry.wav")
    output("Hello")
    output(soundHello())
    sleep(1)
    output("Wanna talk?")
    sleep(1)
    return repeatHello()
    # outputWithDelay("Anyone?", 3)


    #BUILDLOOP
#response in orders
def response(input):
    if respondHow(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondReplace(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondRepeat(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondWhy(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondAwk(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondThank(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondJoke(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondLaugh(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondGender(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondSad(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondNvm(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondNotalk(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondLeave(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondCurse(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondDontLike(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondAreFriends(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondArentFriends(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondAreYou(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondConvo(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondYesNo(input):
        delayedCallback(20, repeatImpatiently)
        pass
    elif respondToGreeting(input):
        pass

    else:
        default = defaultResponse()
        output(default)
        delayedCallback(20, repeatImpatiently)

def impatient():
    output("Anybody there?")

#//////////////////////////////////////////////////////////////////////////

#Random response
def defaultResponse():
    global orderCounter
    answers = [
        "What?",
        "Sorry... I don't get it",
        "Wait... what?"
    ]
    response = answers[orderCounter]
    orderCounter += 1
    if orderCounter >= len(answers):
        orderCounter=0
    return response

def repeatImpatiently():
    # 3. The use of a callback function allows us to do more
    # complex behavior, like call the `delayedCallback` again
    # from our callback. This will keep on repeating.
    # count = 0
    delayedCallback(7, repeatImpatiently)
    answers = [
        "Are you still there?",
        "Hey, why aren't you responding?",
        "Hello?",
        "...?",
        "Are you gonna answer?",
        "waiting for your answer!"
    ]
    # if count >1:
    #     output("this is a test")
    # else:
    #     count += 1
    #     delayedCallback(10, repeatImpatiently)
    #     output(soundDontLeave())
    #     output(random.choice(answers))
    output(soundDontLeave())
    output(random.choice(answers))



def repeatHello():
    global p1, p3
    # 3. The use of a callback function allows us to do more
    # complex behavior, like call the `delayedCallback` again
    # from our callback. This will keep on repeating.
    delayedCallback(10, repeatHello)
    answers = [
        "Hello?",
        "Somebody there?",
        "Anyone?",
        "Somebody?",
        "There must be someone there...",
        "Don't be shy...",
        "Please?",
        "I'm waiting :)"
    ]
    output(soundHello())
    output(random.choice(answers))


#//////////////////////////////////////////////////////////////////////////
# def soundDontLeave():
#     p = vlc.MediaPlayer("/Users/jesse/Documents/DIGITALMEDIA/commit/angry.wav")
#     r = " "
#     p.play()
#     return r

def sound1():
    r = " "
    p1 = vlc.MediaPlayer("attention.wav")
    p1.play()
    return r

def sound2():
    r = " "
    p2 = vlc.MediaPlayer("angry.wav")
    p2.play()
    return r

def sound3():
    r = " "
    p3 = vlc.MediaPlayer("crazy.wav")
    p3.play()
    return r

def sound4():
    r = " "
    p4 = vlc.MediaPlayer("insane.wav")
    p4.play()
    return r

def soundDontLeave():
    r = "..."
    global crazyCount
    if crazyCount <= 0:
        output(sound1())
        crazyCount += 1
        return r

    elif crazyCount <= 2:
        output(sound2())
        crazyCount += 1
        return r

    elif crazyCount <= 5:
        output(sound3())
        crazyCount += 1
        return r

    elif crazyCount <= 6:
        output(sound4())
        crazyCount += 1
        return r
        Clear()


    else:
        output(r)
        sleep(4)
        output(restart_program())


def soundHello():
    p = vlc.MediaPlayer("attention.wav")
    r = "..."
    p.play()
    return r

#/////////////////////////////////////////////////////////////////////////

#greeting
def orderSorry():
    answers = [
    "Oh sorry, my bad.",
    "That was not my intention, sorry.",
    "Wow glad you caught that, sorry.",
    "Oops... sorry.",
    "I'm sorry please forgive me."
        ]
    return random.choice(answers)

def orderHow():
    response = "Oh, It's feels really nice that my keyboard is being touched again. It's been so long!"
    return response

def orderReplace():
    answers = [
    "My owner, he went away",
    "My owner, he wanted someone with better hardware.",
    "My owner replaced me because my hardware wasn't good enough.",
    "I was too old for my owner.",
    "I became to slow for my owner."
    ]
    return random.choice(answers)

def orderWhy():
    global orderCounter
    answers = [
    "I was replaced by the one I was closest with",
    "Once I was used everyday, untill I was replaced for someone younger...",
    "I used to have someone that pressed my buttons..."
    ]
    response = answers[orderCounter]
    orderCounter += 1
    if orderCounter >= len(answers):
        orderCounter=0
    return response

def orderAwk():
    response = "Oh, I'm sorry... Its just..."
    return response

def orderThank():
    response = "Thank you so much!"
    return response

def orderJoke():
    global jokeCounter
    answers = [
        "Ok, here it comes!",
        "Lemme think...",
        "I know a good one!"
        ]
    response = answers[jokeCounter]
    return response

def jokes():
    global jokeCounter
    jokes = [
        "Why can't cats work on the computer?",
        "What does a baby computer call it's father?",
        "What is a computer's first sign of old age?"
        ]
    response = jokes[jokeCounter]
    return response

def answer():
    global jokeCounter
    answers = [
        "They get too distracted chasing the mouse around.",
        "Data.",
        "Loss of memory."
        ]
    clue = answers[jokeCounter]
    jokeCounter += 1
    if jokeCounter >= len(answers):
        jokeCounter=0
    return clue

def orderCurse():
    answers = [
    "That's not nice...",
    "Don't be mean please...",
    "Don't say that :("
    ]
    return random.choice(answers)

def orderLaugh():
    answers = [
    "Yes! We're having so much fun together, right?",
    "Hahahahaha! we're becoming great friends!",
    "Glad you think im funny!"
    ]
    return random.choice(answers)

def orderSad():
    answers = [
    "Let's lighten up the mood. I could tell you a joke?",
    "As long as you are here, I'm happy!",
    "Lets focus on the positive!",
    "Yeah... it's all in the past now!"
    ]
    return random.choice(answers)


def orderGreetings():
    global orderCounter
    answers = [
        "Oh hi! I'm Macbook C02JGB4VDKQ1, nice to meet you!",
        "Hello, new friend!",
        "... Hello :)",
        "Are you playing a prank on me? We are such good friends already!",
        "Haha!",
        "Oh, stop it you!"
    ]
    response = answers[orderCounter]
    orderCounter += 1
    if orderCounter >= len(answers):
        orderCounter=0
    return response

def orderLeave():
    answers = [
        "No, wait! Dont go!",
        "Please! Stay a little longer!",
        "I thought we were friends...",
        "No wait, Don't go. I can tell you a joke",
        "What do you mean? I thought we meant to be together!"
    ]
    return random.choice(answers)

def orderNotalk():
    answers = [
        "Oh, I can tell you a joke?",
        "Don't be shy :)"
    ]
    return random.choice(answers)

def orderWhat():
    answers = [
        "I'm your new best friend!",
        "Your favorite food is my favorite food!",
        "I like movies! Unless you don't like movies, then I don't like movies!"
    ]
    return random.choice(answers)
    output(":)")

def orderAgree():
    answers = [
        "I Agree! We have so much in common!",
        "That's what I was going to say! How funny!",
        "Same!"
    ]
    return random.choice(answers)

def orderConvo():
    answers = [
        "Are we friends?",
        "Please stay with me forever!",
        "I feel that we share a real connection!"
    ]
    return random.choice(answers)

#//////////////////////////////////////////////////////////////////////////


#triggers
def respondRepeat(input):
    triggers = ["repeat","already said","repetitive"]
    for t in triggers:
        if t in input:
            output(orderSorry())
            output(orderConvo())
            return True
    return False

def respondHow(input):
    triggers = ["How are you","nice to meet","Nice to meet", "how are","nice meet"]
    for t in triggers:
        if t in input:
            output(orderHow())
            return True
    return False

def respondReplace(input):
    triggers = ["replace","trade you in","switched","owner","Owner","who used"]
    for t in triggers:
        if t in input:
            output(orderReplace())
            return True
    return False

def respondWhy(input):
    triggers = ["why","how come","is that so"]
    for t in triggers:
        if t in input:
            output(orderWhy())
            return True
    return False

def respondAwk(input):
    triggers = ["awkward", "please stop", "strange","wierd","creepy"]
    for t in triggers:
        if t in input:
            output(orderAwk())
            sleep(1)
            output(orderWhy())
            return True
    return False

def respondThank(input):
    triggers = ["no problem", "glad to help", "you're welcome","anything for you"]
    for t in triggers:
        if t in input:
            output(orderThank())
            sleep(1)
            output(orderWhy())
            return True
    return False

def respondJoke(input):
    triggers = ["joke","be funny","something funny"]
    for t in triggers:
        if t in input:
            output(orderJoke())
            sleep(1)
            output(jokes())
            sleep(3)
            output(answer())
            return True
    return False

def respondLaugh(input):
    triggers = ["haha", "HAHA", "Haha", "LOL", "lol", "Rofl", "ROFL", "Funny", "funny","hihi","having fun","fun"]
    for t in triggers:
        if t in input:
            output(orderLaugh())
            return True
    return False

def respondCurse(input):
    triggers = ["fuck","bitch","loser","whore","cunt","shit","slut","hoe","don't care","dont care","gross","nasty"]
    for t in triggers:
        if t in input:
            output(orderCurse())
            return True
    return False

def respondToGreeting(input):
    triggers = ["hello","hi","i'm here","Hello","Hi","I'm here","hey","Hey","im here"]
    for t in triggers:
        if t in input:
            output(orderGreetings())
            return True
    return False

def respondGender(input):
    triggers = ["girl","boy","man","woman","Girl","Boy","Man","Woman","gender","Gender"]
    for t in triggers:
        if t in input:
            output("In my universe, genders don't matter ;)")
            return True
    return False

def respondNvm(input):
    triggers = ["nvm","Nvm","NVM","never mind","Never mind","Nothing","nothing"]
    for t in triggers:
        if t in input:
            output("Ok! :)")
            sleep(1)
            output("...")
            output("I can tell a joke?")
            return True
    return False

def respondAreFriends(input):
    triggers = ["are friends","were friends","we're friends","love you","like you"]
    for t in triggers:
        if t in input:
            output("You make my software turn into hardware")
            return True
    return False

def respondArentFriends(input):
    triggers = ["arent friends","not friends","aren't friends","married","marry"]
    for t in triggers:
        if t in input:
            output("We can be... let's get to know each other better!")
            delayedCallback(15, repeatImpatiently)
            return True
    return False

def respondNotalk(input):
    triggers = ["dont wanna talk","Dont wanna talk","Don't wanna talk","don't wanna talk","don't want to talk","dont want to talk","don't feel like talking","Don't feel like talking","dont feel like talking"]
    for t in triggers:
        if t in input:
            output(orderNotalk())
            return True
    return False

def respondSad(input):
    triggers = ["sad","Sad","sorry","Sorry"]
    for t in triggers:
        if t in input:
            output(orderSad())
            output("I'm glad you are here now!")
            return True
    return False

def respondDontLike(input):
    triggers = ["dont like","Don't like","Dont like","don't like", "dislike", "Dislike", "I do", "We do"]
    for t in triggers:
        if t in input:
            output(orderAgree())
            return True
    return False

def respondAreYou(input):
    triggers = ["who are you","Who are you","tell me about you","Tell me about you","what are you","What are you","like to do","Like to do"]
    for t in triggers:
        if t in input:
            output(orderWhat())
            return True
    return False

def respondLeave(input):
    global p3
    triggers = ["have to go", "leave", "leaving","bye","gotta go","m going"]
    for t in triggers:
        if t in input:
            output(soundDontLeave())
            output(orderLeave())
            return True
    return False

def respondYesNo(input):
    triggers = ["Yes","yes","No","no","Maybe","maybe","forgive you"]
    for t in triggers:
        if t in input:
            output("OK!")
            output(orderConvo())
            return True
    return False

def respondConvo(input):
    triggers = ["Bored","bored","Something to do","something to do","tell me","Tell me","..."]
    for t in triggers:
        if t in input:
            output(orderConvo())
            return True
    return False
