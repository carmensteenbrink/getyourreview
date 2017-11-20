
from __future__ import print_function
import sys
import mysql.connector
# import snotbot/uniquebot.py as information


#Configuration van data ophalen en waarmee inloggen


config = {
  'user': 'root',
  'password': 'Carmpie23!',
  'host': '127.0.0.1',
  'database': 'sys',
  'raise_on_warnings': True,
  'use_unicode': False,
  'buffered': True,
  'raw': True
}

"""
(Open txt file en lees alle informatie dat gescheiden is door kommas, waardoor hij weet dat het bij iets nieuws hoort)

information = {

'Postcode' : (postcode informatie vanuit txt)
'Klantnaam' : (Klantnaam informatie vanuit txt)
'Stad' : (Stad informatie vanuit txt)
'Land' : (Land informatie vanuit txt)
'Straat' : (Straat informatie vanuit txt)
'Huisnummer' : (Huisnummer informatie vanuit txt)

}

"""

#Opent connectie en maakt cursor aan
cnx = mysql.connector.connect(**config)
cur = cnx.cursor(buffered=True)
"""
add_information = ("INSERT INTO chatbot_print",
                "(name, adress, number, postal_code, city, country)",
                "VALUES (%s, %s, %s, %s, %s, %s)")


"""
cnx.commit()
cnx.close()





