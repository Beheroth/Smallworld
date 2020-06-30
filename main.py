from flask import Flask, render_template, redirect, session
import pygame
import pygame.examples.midi

import gamestate


app = Flask(__name__)

@app.route('/')
def root():
	return render_template("root.html")

def main():
	pygame.init()
	pygame.display.set_caption("Smallworld")
	screen = pygame.display.set_mode((240, 180))
	running = True
	while(running):
		e = pygame.event.wait()

		for event in pygame.event.get():
			# only do something if the event is of type QUIT
			if event.type == pygame.QUIT:
				# change the value to False, to exit the main loop
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				print(pygame.mouse.get_pos())
				print(pygame.mouse.get_cursor())
	pygame.display.quit()

if __name__ == '__main__':
	#state = gamestate.GameState()
	#pygame.examples.midi.main()
	main()
