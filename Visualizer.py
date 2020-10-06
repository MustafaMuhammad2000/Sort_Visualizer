import Sort as s
import sys
import pygame
import pygame_menu
#Intialize pygame as well as create base screen
pygame.init()
width = 1200
height = 800
screen = pygame.display.set_mode((width,height))
screen.fill(pygame.Color("#a48be0"))
id = 1
speed = 200
numberofvalues = 50
# https://pygame-menu.readthedocs.io/en/latest/
# Menu to start visualizer
# Start game button
def start_game():
    print(id)
    test = s.Sort(id,numberofvalues,speed)
    while True:
        test.start_sort()
        pygame.display.update()
# Select which sort
def select_sort(value, sortID):
    global id
    id = sortID
# Select speed
def select_speed(value, speedS):
    global speed
    speed = speedS
# Set numbr of data points
def set_numberofvalues(text):
    global numberofvalues
    if text != "" and text != '0':
        numberofvalues = int(text)
    if numberofvalues == 0:
        numberofvalues = 50;
# Check if the pygame window was quit
def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

# Updates the current state of the screen, highlights which two indices are being swapped
def update_screen(array, name, speed, swapE1=None, swapE2=None, window = screen):
    window.fill(pygame.Color("#a48be0"))
    pygame.display.set_caption("Sorting Visualizer: "+name)
    bar_width = width/len(array)
    maxnum = max(array)
    for i in range(len(array)):
        colour = (124, 194, 205)
        if swapE1 == i:
            colour = (219,179,33)
        elif swapE2 == i:
            colour = (219, 33, 61)
        height_scale = (array[i]/maxnum)*height*0.75
        pygame.draw.rect(window, colour, (i * bar_width, height, bar_width, -height_scale))
    check_quit()
    pygame.display.update()
    pygame.time.delay(speed)

acceptable_chars = [0,1,2,3,4,5,6,7,8,9]
# Setting up menu widgets
menu = pygame_menu.Menu(600, 800, 'Welcome', theme=pygame_menu.themes.THEME_SOLARIZED)
menu.add_button('Play', start_game)
menu.add_selector('Sort Algorithim :', [('Bubble', 1),('Selection', 2),('Insertion', 3),('Merge', 4),('Quick', 5)], onchange=select_sort)
menu.add_text_input('Number of Values: ', default='150', onchange = set_numberofvalues, valid_chars = acceptable_chars, maxchar = 6)
menu.add_selector('Set Speed :', [('Slow', 200),('Middle', 100),('Fast', 10),('Full Speed',1)], onchange=select_speed)
menu.add_button('Quit', pygame_menu.events.EXIT)

def main():
    menu.mainloop(screen)

if __name__ == "__main__":
    main()