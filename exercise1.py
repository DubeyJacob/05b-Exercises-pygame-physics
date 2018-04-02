#!/usr/bin/env python
'''

Choose values for gravity, friction, and air_resistance (lines 25–27). Try to find a combination that seems realistic

For every line in the update method (lines 41-66), please add a comment describing what it does. 

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do a few lines for you as an example


'''
import sys, logging, random, pygame
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

screen_size = (1080,800) #Give the screen_size size of width and height
FPS = 60 #Defines FPS as the integer 60, to be later used at the framerate
black = (0,0,0) #Defines black as the tuple for the colour black
gravity = 0 #Sets gravity to 0 so there is no vertical motion of the balls
friction = 0 #Defines friction as 0 so there will be no loss in motion when contacting a surface.
air_resistance = 0 #Defines air_resistance as 0 so that there is no force acting on the ball that would change velocity

class Ball(pygame.sprite.Sprite):
	def __init__(self, i, size, color, position, direction):
		pygame.sprite.Sprite.__init__(self)
		self.size = size
		self.image = pygame.Surface(size)
		self.rect = self.image.get_rect()
		pygame.draw.ellipse(self.image, color, self.rect)
		self.image.set_colorkey((0,0,0))
		(self.rect.x,self.rect.y) = position
		self.direction = direction
		self.id = i

	def update(self):
		(dx,dy) = self.direction	# get the current velocity
		self.rect.x += dx		# move the sprite horizontally
		self.rect.y += dy		#move thee sprite vertically

		dy = dy + gravity #Adds current velocity to gravity, but since gravity is 0 the sprite doesn't fall
		dx *= (1.0-air_resistance) #Horizontal velocity multiplied by air resistance, which is 0 so velocity is consistant
		dy *= (1.0-air_resistance) #Vertical velocity multiplied by air resistance, which is 0 so velocity is consistant
		
		(WIDTH,HEIGHT) = screen_size #Sets the width and height set to the values equal to the numbers in the tuple for screen_size
		if self.rect.right >= WIDTH: #Condition on if the sprite moving right in position greater than or equal to the width:
			self.rect.right = WIDTH #The sprite in then in position equal to the width
			dx = dx * -1 * (1.0-friction) #Current position moves in opposite direction with consideration of friction
		if self.rect.left <= 0: #Condition on if the sprite in moving left and approaches the edge of the screen
			self.rect.left = 0 #The sprite is then in a position equal to the left side of the screen
			dx = dx * -1 * (1.0-friction) #Horizontal motion changes direction with consideration of friction
		if self.rect.top <= 0: #Same as above but with vertical motion moving up
			self.rect.top = 0 #Same as above but with vertical motion moving up
			dy = dy * -1 * (1.0-friction) #Same as above but with vertical motion moving up
		if self.rect.bottom >= HEIGHT: #Same as above but with vertical motion moving down
			self.rect.bottom = HEIGHT #Same as above but with vertical motion moving down
			dx = dx * -1 * (1.0-friction) #Same as above but with vertical motion moving down
			dy = dy * -1 * (1.0-friction) #Same as above but with vertical motion moving down
			if abs(dy) < 1:			# a hack to keep it from bouncing forever
				dy = 0 #The sprite will stop moving
		self.direction = (dx,dy) #direction of the object set to the position of an x and y coordinate


def main(): #Main game loop
	pygame.init() #Runs the loop immediately
	screen = pygame.display.set_mode(screen_size) #defines the screen as this function to set screen size
	clock = pygame.time.Clock() #Defines the internal clock of the function

	balls = pygame.sprite.Group() #defines balls as the group of sprites
	for i in range(random.randrange(10,50)): #condition of a range on objects between 10 and 50
		size = random.randrange(10,50) #sets size to a random number between 10 and 50
		color = (random.randrange(255),random.randrange(255),random.randrange(255)) #sets random colours
		initial_position = (random.randrange(25,screen_size[0]-25),random.randrange(25,screen_size[1]-25)) #Sets the ball at a random position
		initial_velocity = (random.randrange(-10,10),0) #Sets the velocity to a random value so the balls move at different speeds.
		ball = Ball(i,(size,size),color,initial_position,initial_velocity) #Assigns all the atributes to previously defined parameters
		balls.add(ball) #adds more balls to the screen?

	while True: #Conditional while loops
		clock.tick(FPS) #Prevents the game from exceeding 60 FPS
		screen.fill(black) #displays a black screen

		for event in pygame.event.get(): #Condition for the events in the function
			if event.type == pygame.QUIT: #if what the player does is exit the game:
				pygame.quit() #pygame will stop
				sys.exit(0) #The program as a whole will stop

		balls.update() #balls will update and have new values for each iteration of the program
		balls.draw(screen) #draws the balls on the screen
		pygame.display.flip() #Sets up everything in the screen first, and then displays it all at once

if __name__ == '__main__': #
	main()