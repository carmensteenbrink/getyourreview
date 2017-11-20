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
    """
    el(if/se):
        Respondtopostcode(input)
        input = postcodeingelezen
        (doe voor alles alleen dan andere variabeles)
    """


"""
def Schrijfnaartxtbestand
"""



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
    triggers = ['type ', 'font', 'glyph', 'google', 'google fonts', 'italic', 'bold', 'regular', 'words', 'calligraphy', 'writing', 'typeface']
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
            answer = 'ah yes, '+t+' i know something about that...'
            output(answer)
            return True
    return False

def respondTo3d(input):
    triggers = ['3d', 'sketch', 'draw', 'space', 'vr', 'scan', 'object', 'animation']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice, what would you like to do with it?'
            output(answer)
            return True
    return False

def respondTophoto(input):
    triggers = ['photo', 'filter', 'picture', 'editing', 'contrast', 'hue', 'black', 'white', 'black and white', 'cmyk', 'rgb']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice'
            output(answer)
            return True
    return False

def respondTogames(input):
    triggers = ['3d', 'game', 'playing', 'time', 'time span', 'interactive', 'realtime', 'experience', 'prototying']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice'
            output(answer)
            return True
    return False

def respondToarchitecture(input):
    triggers = ['laser', 'illustrator', 'building', 'architecture', 'construction', 'product', 'product-design']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice'
            output(answer)
            return True
    return False

def respondTo1d(input):
    triggers = ['vector', 'illustrator', 'illustration', 'draw', 'image', 'editor', 'layer', 'color']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice'
            output(answer)
            return True
    return False

def respondTotemplate(input):
    triggers = ['charts', 'craft', 'sew', 'template', 'example', 'already made', 'marker', 'charts']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice'
            output(answer)
            return True
    return False

def respondTotext(input):
    triggers = ['text', 'type', 'code', 'html', 'python', 'language', 'graphics', 'commands', 'geometric', 'shaped']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice'
            output(answer)
            return True
    return False

def respondToconding(input):
    triggers = ['code', 'python', 'html', 'visuals', 'internet', 'script', 'running', 'website', 'git']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice'
            output(answer)
            return True
    return False

def respondTotutorials(input):
    triggers = ['web', 'tools', 'tips', 'tricks', 'learn', 'questions', 'example', 'test', 'forum', 'failure']
    for t in triggers:
        if t in input:
            answer = 'yes '+t+' is nice'
            output(answer)
            return True
    return False
