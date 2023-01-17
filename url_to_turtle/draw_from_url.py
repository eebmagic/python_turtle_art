import turtle
import requests

url = input("Paste a url: ")
response = requests.get(url)
text = response.text

t = turtle.Turtle()
t.speed("fastest")
t.hideturtle()

last_was_move = False
for char in text:
	for axis in t.pos():
		if axis > 150:
			t.penup()
			t.home()
			t.pendown()

	print(f"{char} = {ord(char)}")

	# Alternate between moving or turning
	if last_was_move:
		t.left(ord(char))
		last_was_move = False
	else:
		t.fd(ord(char) / 5)
		last_was_move = True
