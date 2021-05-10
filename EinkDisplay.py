import pygame

# Define Desired ColorCodes
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
MediumGray =(128, 128, 128)
Aqua =(0, 128, 128)
Cream = (255, 255, 204)
Blue = (0, 0, 255)


# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 2
HEIGHT = 2

EINK_HEIGHT = 295
EINK_WIDTH = 295

# This sets the margin between each cell
MARGIN = 0

def Eink_show( data ):
   print("BarcodeSet")
   grid = []
   for row in range(128):
       # Add an empty array that will hold each cell
       # in this row
       grid.append([])
       for column in range(296):
           grid[row].append(0)  # Append a cell

   # Set row 1, cell 5 to one. (Remember rows and
   # column numbers start at zero.)
   i = 0
   j = 0
   #if False:
   # print("Length Of GRID :",len(grid))
   for row in data:
       for cell in row:
           # print(i, ',', j)
           if cell == 0:
               grid[i][j] = 0
           else:
               grid[i][j] = 1
           i = i + 1
       j = j + 1
       i = 0
   grid[1][5] = 1

   # Initialize pygame
   pygame.init()
   # Set the HEIGHT and WIDTH of the screen
   WINDOW_SIZE = [600, 600]  # [889,385]#, 592]
   screen = pygame.display.set_mode(WINDOW_SIZE)

   # Set title of screen
   pygame.display.set_caption("Eink 296x296")

   # Loop until the user clicks the close button.
   done = False

   # Used to manage how fast the screen updates
   clock = pygame.time.Clock()

   # Set the screen background
   # screen.fill(BLACK)
   screen.fill(WHITE)

   # Draw the grid
   for row in range(128):
       for column in range(296):
           color = BLACK
           if grid[row][column] == 1:
               # print('1', end=' ')
               # color = RED
               color = WHITE
           else:
               # print('0')
               print('0',end=' ')
           pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                             (MARGIN + HEIGHT) * row + MARGIN,
                             WIDTH,
                             HEIGHT])

   # Limit to 60 frames per second
   clock.tick(60)

   # Go ahead and update the screen with what we've drawn.
   pygame.display.flip()
   while not done:
       for event in pygame.event.get():  # User did something
           if event.type == pygame.QUIT:  # If user clicked close
               done = True  # Flag that we are done so we exit this loop
           elif event.type == pygame.MOUSEBUTTONDOWN:
               # User clicks the mouse. Get the position
               pos = pygame.mouse.get_pos()
               # Change the x/y screen coordinates to grid coordinates
               column = pos[0] // (WIDTH + MARGIN)
               row = pos[1] // (HEIGHT + MARGIN)
               if row > EINK_HEIGHT:
                   row = EINK_HEIGHT
               if column > EINK_WIDTH:
                   column = EINK_WIDTH
               # Set that location to one
               # print(row, column)
               grid[row][column] = 1
               # print("Click ", pos, "Grid coordinates: ", row, column)
   # Be IDLE friendly. If you forget this line, the program will 'hang'
   # on exit.
   pygame.quit()
   return

pygame.quit()