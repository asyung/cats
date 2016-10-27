# our program will only take pics with one person
from sys import argv
import APIcaller as api
from PIL import Image

# Save command-line arg as image URL
urlImage = argv[1]

# save the JSON response as variable person
# contains everything about their age, gender, facial attributes, etc. 
person = api.returnResult(urlImage)

# Prepare cats: old cat, baby cat, big eyes cat, regular cat
baby = Image.open('catphotos/baby.jpg')
bigeyes = Image.open('catphotos/bigeyes.jpeg')
old = Image.open('catphotos/old.jpg')
regular = Image.open('catphotos/regular.jpeg')

# AGE
age = person[0]['faceAttributes']['age']

# FACE SIZE 
height = width = person[0]['faceRectangle']['height']

# EYE SIZE
eyeBottom = person[0]['faceLandmarks']['eyeLeftBottom']
eyeTop = person[0]['faceLandmarks']['eyeLeftTop']
eyeInner = person[0]['faceLandmarks']['eyeLeftInner']
eyeOuter = person[0]['faceLandmarks']['eyeLeftOuter']
eyeHeight = (eyeBottom['y'] - eyeTop['y'])/height
eyeWidth = (eyeInner['x'] - eyeOuter['x'])/width

# Map facial attributes to cat attributes
if (age < 13):
	baby.show() 		
	print('We are showing a baby kitten because this person looks %d years old' % age)
elif (age > 60):
	old.show()
	print('We are showing an old cat because this person looks %d years old' % age)
elif (eyeHeight > 0.064 and eyeWidth > 0.15):
	bigeyes.show()
	print('We are showing a big-eyed cat because this person has ... big eyes')
else:
	regular.show()
	print('the average joe/sally')
