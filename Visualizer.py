import Sort as s
import sys
import pygame

pygame.init()
width = 1600
height = 900
screen = pygame.display.set_mode((width,height))
screen.fill(pygame.Color("#a48be0"))

def check_quit(): # Check if the pygame window was quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

def update_screen(array, name, swapE1=None, swapE2=None, window = screen):
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
    pygame.time.delay(200)

def main():
    print("Please choose which sort you would like to visualize"
          "\n 1. Bubble Sort"
          "\n 2. Selection Sort"
          "\n 3, Insertion Sort"
          "\n 4. Merge Sort"
          "\n 5. Quick Sort")
    val = int(input("Enter your choice: "))
    test = s.Sort(val)
    while True:
        test.start_sort()
        pygame.display.update()

if __name__ == "__main__":
    main()