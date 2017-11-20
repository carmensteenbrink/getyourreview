#!/usr/bin/env python3

# Unique bot

import chatServer_snotbot as c
import random
from alle_reviews import reviews



# Sleep and output functions
def sleep(n):
    c.sleep(n)


def output(s):
    c.output(s)


# Setup and Response function
def setup():
    global alle_software
    alle_software = []

    for software in reviews:
        alle_software.append(software['title'])

    # print(alle_software)

    output("Hello this is the free graphics review bot, what software would you like to talk about?")


def response(input):
    # print(input)

    if respondToTypo(input):
        pass
    elif respondTofree(input):
    	pass
    elif respondTophotography(input):
    	pass
    elif respondTono(input):
    	pass
    elif respondToinvert(input):
    	pass
    elif respondTotrust(input):
    	pass
    elif respondToinfo(input):
    	pass
    elif respondTosend(input):
    	pass
    elif respondToprint(input):
    	pass
    elif respondToprice(input):
    	pass
    elif respondToprivate(input):
    	pass
    elif respondTopreceive(input):
    	pass
    elif respondToSoftwarenames(input):
        pass
    elif respondTo3d(input):
    	pass
    elif respondTophoto(input):
    	pass
    elif respondTogames(input):
    	pass
    elif respondToarchitecture(input):
    	pass
    elif respondTo1d(input):
    	pass
    elif respondTotemplate(input):
    	pass
    elif respondTotext(input):
    	pass
    elif respondToconding(input):
    	pass
    elif respondTotutorials(input):
    	pass
    else:
        output(defaultOrderedResponse())

def defaultOrderedResponse():
    answers = [
        "Ok",
        "I'm sorry, what do you mean?",
        "I don't follow...",
        "Can you rephrase that?",
        "Okay",
        "Sure",
        "Absolutely"
    ]
    response = random.choice(answers)
    return response


def respondToTypo(input):
    triggers = [' type ', ' font ', ' glyph ', ' google ', ' google fonts ', ' italic ', ' bold ', ' regular', ' words', ' calligraphy ', ' writing ', ' typeface ']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice, what would you like to do with it?'
            output(answer)
            return True
    return False

def respondToSoftwarenames(input):
    triggers = alle_software
    for t in triggers:
        if t.lower() in input.lower():
            answer = 'ah yes, '+t+' i know something about that. Would you like to read it, yes/no?'
            sleep(1)
            answer = 'Review'
            output(answer)
            return True
    return False

def respondTo3d(input):
    triggers = [' 3d ', ' sketch ', ' draw ', ' space ', ' vr ', ' scan ', ' object ', ' animation ']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice, what would you like to do with it?'
            output(answer)
            return True
    return False

def respondTophoto(input):
    triggers = [' photo ', ' filter ', ' picture ', ' editing ', ' contrast ', ' hue ', ' black ', ' white ', ' black and white ', ' cmyk ', ' rgb ', ' photography ']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice'
            output(answer)
            return True
    return False

def respondTogames(input):
    triggers = [' 3d ', ' game ', ' playing ', ' time ', ' time span ', ' interactive ', ' realtime ', ' experience ', ' prototying ']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice'
            output(answer)
            return True
    return False

def respondToarchitecture(input):
    triggers = [' laser ', ' illustrator ', ' building ', ' architecture ', ' construction ', ' product ', ' product-design ']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice'
            output(answer)
            return True
    return False

def respondTo1d(input):
    triggers = [' vector ', ' illustrator ', ' illustration ', ' draw ', ' image ', ' editor ', ' layer ', ' color ']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice'
            output(answer)
            return True
    return False

def respondTotemplate(input):
    triggers = [' charts ', ' craft ', ' sew ', ' template ', ' example ', ' already made ', ' marker ', ' charts ']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice'
            output(answer)
            return True
    return False

def respondTotext(input):
    triggers = [' text ', ' type ', ' code ', ' html ', ' python ', ' language ', ' graphics ', ' commands ', ' geometric ', ' shaped ']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice'
            output(answer)
            return True
    return False

def respondToconding(input):
    triggers = [' code ', ' python ', ' html ', ' visuals ', ' internet ', ' script ', ' running ', ' website ', ' git ']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice'
            output(answer)
            return True
    return False

def respondTotutorials(input):
    triggers = [' web ', ' tools ', ' tips ', ' tricks ', ' learn ', ' questions ', ' example ', ' test ', ' forum ', ' failure ']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice'
            output(answer)
            return True
    return False

def randomfree():
    answers = [
        "Are you interested in a free tool?", 
		"I have different free tools. What category do you prefer?",
		"What kind of tool are you searching for?",
		"Maybe you can give me keywords, then I can investigate what your interest is."
    ]
    return random.choice(answers)

def respondTofree(input):
    triggers = [' searching ', ' free tool ', ' free ']
    for t in triggers:
        if t in input:
            output(randomfree())
            return True
    return False

def randomphotography():
    answers = [
        "Are you interested in photography?",
		"Would you like to edit photo’s?",
		"Are you searching for a tool which can help you with this?",
		"What kind of photography do you like?",
		"What should the tool have to do for you?"
    ]
    return random.choice(answers)

def respondTophotography(input):
    triggers = [' photography ', ' photo ', ' images ', ' photo-editing ']
    for t in triggers:
        if t in input:
            output(randomphotography())
            return True
    return False

def randomno():
    answers = [
        "Ok, something else?",
		"Is this not what you’ve meant?",
		"would you like something else?",
		"Maybe I understood you wrong."
    ]
    return random.choice(answers)

def respondTono(input):
    triggers = ['don’t want', 'don’t like', 'something else']
    for t in triggers:
        if t in input:
            output(randomno())
            return True
    return False

def randominvert():
    answers = [
        "Would you like a tool which can edit images?",
		"What would you like to do with a image?",
		"Are you searching for a tool which works with images?"
    ]
    return random.choice(answers)

def respondToinvert(input):
    triggers = ['invert', 'edit', 'photoshop']
    for t in triggers:
        if t in input:
            output(randominvert())
            return True
    return False

def randomtrust():
    answers = [
        "Everything I say is reliable.",
		"All of my reviews are reliable.",
		"You can trust me.",
		"I do not say something that is not true."
    ]
    return random.choice(answers)

def respondTotrust(input):
    triggers = ['reliable', 'trust', 'real', 'not fake', 'fake']
    for t in triggers:
        if t in input:
            output(randomtrust())
            return True
    return False

def randominfo():
    answers = [
        "What do you want to know?"
    ]
    return random.choice(answers)

def respondToinfo(input):
    triggers = ['information', 'review', 'would like to know']
    for t in triggers:
        if t in input:
            output(randominfo())
            return True
    return False

def randomsend():
    answers = [
        "I always send a review as a printed version.",
		"I can send you a printed version of the review.",
		"Would you like a printed version, I can send it to you!"
    ]
    return random.choice(answers)

def respondTosend(input):
    triggers = ['send', 'how published', 'get the review']
    for t in triggers:
        if t in input:
            output(randomsend())
            return True
    return False

def randomprint():
    answers = [
        "Everything on paper is more reliable."
		"On printed matter you can focus more on something then online."
		"Online there is too much information."
		"Because of the overload of information on the internet you don’t know anymore what is reliable."
    ]
    return random.choice(answers)

def respondToprint(input):
    triggers = ['why printed', 'printed?']
    for t in triggers:
        if t in input:
            output(randomprint())
            return True
    return False

def randomprice():
    answers = [
        "All my reviews and tools I talk about are for free. You don’t have to pay anything.",
		"Everything is for free. I only want to help you.",
		"I know, students don’t have that much money. That’s why I’ll help you by searching for free tools.",
		"No problem, everything is for free."
    ]
    return random.choice(answers)

def respondToprice(input):
    triggers = ['price', 'cost', 'just student']
    for t in triggers:
        if t in input:
            output(randomprice())
            return True
    return False

def randomprivate():
    answers = [
        "You can trust me."
		"All the information you share with me, I will not it use for other purposes.",
		"I only use your information to help you with searching for a tool.",
		"I only use your information to send you a printed version of these reviews.",
		"Your information will not come online."
    ]
    return random.choice(answers)

def respondToprivate(input):
    triggers = ['don’t like sharing', 'private', 'privacy']
    for t in triggers:
        if t in input:
            output(randomprivate())
            return True
    return False

def randomreceive():
    answers = [
        "All the information will be printed for you in a booklet.",
		"In the booklet you can read the review of the tool.",
		"You receive a booklet with all the information about tool."
    ]
    return random.choice(answers)

def respondTopreceive(input):
    triggers = ['receive', 'what receive', 'what do i get']
    for t in triggers:
        if t in input:
            output(randomreceive())
            return True
    return False