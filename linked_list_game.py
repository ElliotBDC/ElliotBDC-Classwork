import pygame
pygame.init()

#Colours
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

score = 0

#Window Title
pygame.display.set_caption("Linked list game")
size = (1920, 1080)
colour = 0, 0, 0

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
player_image = pygame.image.load("Untitled.png").convert()
credits_image = pygame.image.load("WIN_20200514_14_01_32_Pro.jpg").convert()
class Player():
    def __init__(self):
        self.x = 0
        self.y = pygame.display.get_window_size()[1]
        self.width = 20
        self.height = 20
    def draw(self):
        pygame.draw.rect(screen, WHITE, [self.x, self.y-30, self.width, self.height])

players = []
class Invader():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 10
        self.height = 10
        self.lives = 3
    def draw(self):
        screen.blit(player_image, [self.x, self.y])
        #self.x = x
        #self.y = y
    def move(self, diff_x, diff_y):
        self.x = self.x + diff_x
        self.y = self.y + diff_y
        screen.blit(player_image, [self.x, self.y])
    def detectCollision(self):
        if len(bullets) > 0:
            for index, bullet in enumerate(bullets):
                if self.y < bullet.y < (self.y + player_image.get_height()) and (self.x < bullet.x < (self.x + player_image.get_width())):
                    bullets.pop(index)
                    self.lives = self.lives - 1
                    if self.lives == 0:
                        for index in range(0, len(objects)):
                            if objects[index].x == self.x:
                                objects.pop(index)
                                break
                    return True
        return False

def detectCollision(objects, objects2):
    if len(objects2) > 0:
        for index, object in enumerate(objects):
            for index2, object2 in enumerate(objects2):
                if objects2.y < object.y: #and objects2.y > object2.y + object2.y:
                    return True
def drawRow():
    for i in range(0, len(objects)):
        #objects[i].draw(i*30, objects[i].y, 20, 20)
        width_per = (screen.get_width()//17)
        objects[i].y
        objects[i].x = i * width_per
        #objects[i].draw(i*width_per, object.y)

class Bullet():
    def __init__(self, x, y):
        self.x = x+5
        self.y = y
    def draw(self):
        pygame.draw.rect(screen, RED, [self.x, self.y, 10, 15])
    def move(self, diff_y):
        self.y = self.y + diff_y

print(pygame.display.get_window_size())
# Loop until the user clicks the close button.
done = False
objects = []
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
GAME_STATE = "GAME_STATE"
MENU_STATE = "MENU_STATE"
LINKED_STATE = "LINKED_STATE"
current_state = "MENU_STATE"
CREDIT_STATE = "CREDIT_STATE"
USERNAME_STATE = "USERNAME_STATE"

#TEXT

title_font = pygame.font.Font('space_invaders.ttf', 50)
menu_title_text = title_font.render("Space Invader & Linked List", True, WHITE)
text_font = pygame.font.Font('space_invaders.ttf', 25)
exit_font = pygame.font.Font('space_invaders.ttf', 15)
to_play_text = text_font.render("Press the space bar to play space invaders", True, WHITE)
play_linked_text = text_font.render("Press # to play the linked list game!", True, WHITE)
exit_text = exit_font.render("Press TAB to exit!" + " " * 10 + "Press 0 to view credits" + " " * 10 + "Press 9 to return from a game!", True, WHITE)
return_text = exit_font.render("Press 9 to return from a game!", True, WHITE)
credits_text = exit_font.render("Press 0 to view credits", True, WHITE)
linked_title = title_font.render('Linked List Game', True, WHITE)
enter_text = text_font.render("Enter name: ", True, WHITE)

#LINKED LIST

class LinkedList:
    listNodes = [None]
    size = 0
    def __init__(self):
        self.nextFree = 0
        self.start = None

    def __repr__(self) -> str:
        return f'{self.listNodes}'

    def add(self, name):
        if self.start != None:
            try:
                self.listNodes[self.nextFree] = Node(name, None)
            except:
                self.listNodes.append(Node(name, None))
            self.findNewPos(self.listNodes[self.nextFree])
            self.nextFree = self.findNextFree()
            self.size = self.size + 1
        if self.start is None:
            self.listNodes[self.nextFree] = (Node(name, -1)) #Pointer None means its the end of the list
            self.start = 0
            self.nextFree = self.nextFree + 1

    def findNextFree(self):
        for i in range(0, len(self.listNodes)):
            if self.listNodes[i] is None:
                self.nextFree = i
                break
            elif i == len(self.listNodes)-1:
                self.nextFree = i+1
        return self.nextFree

    def findNewPos(self, newNode):
        for pointer in range(0, len((self.listNodes))):
            for i in range(0, len(self.listNodes)):
                if self.listNodes[i].pointer == self.listNodes.index(self.listNodes[pointer]):
                    break
            if self.listNodes[pointer].pointer == -1:
                if self.listNodes[pointer].name < newNode.name:
                    newNode.setPointer(-1)
                    self.listNodes[pointer].pointer = self.listNodes.index(newNode)
                    break

            if pointer == 0:
                node = self.listNodes[self.start]

                if self.listNodes[self.start].name > newNode.name:
                    self.start = self.listNodes.index(newNode)
                    newNode.setPointer(self.listNodes.index(node))
                    break

            elif self.listNodes[pointer].name > newNode.name and self.listNodes[i].name < newNode.name:
                newNode.setPointer(self.listNodes.index(self.listNodes[pointer]))
                for i in range(0, len(self.listNodes)):
                    if self.listNodes[i].pointer == self.listNodes.index(self.listNodes[pointer]):
                        break
                self.listNodes[i].setPointer(self.listNodes.index(newNode))
                break

    def remove(self, name):
        for index in range(0, len(self.listNodes)):
            if self.listNodes[index].name == name:
                for i in range(0, len(self.listNodes)):
                    if self.listNodes[i].pointer == index:
                        break
                self.listNodes[i].pointer = self.listNodes[index].pointer
                self.size = self.size - 1
    def printAlphabetically(self):
        endLoop = True
        self. pointers = []
        self.pointers = [1, 5, 5, 4, -1, 3]
        self.pointer = self.start
        self.count = 1
        while endLoop == True:
            if self.pointer != -1:
                print(f"Position: {self.count}:", self.listNodes[self.pointer].name)
                self.pointer = self.pointers[self.pointer]
                self.count = self.count + 1
            else:
                endLoop = False

class Node:
    def __init__(self, name, pointer):
        self.name = name
        self.pointer = pointer

    def __repr__(self) -> str:
        return f'( {self.name} --> {self.pointer} )'

    def setPointer(self, pointer):
        self.pointer = pointer

    def getPointer(self):
        return self.pointer


newLinked = LinkedList()
""""
newLinked.add("Haider")
newLinked.add("Otto")
newLinked.add("Salman")
newLinked.add("Oliver")
newLinked.add("Matthew")

newLinked.remove("Haider") #Haider is not deleted from the linked list, however he is skipped.

print(f"NextFree: {newLinked.nextFree}, Start: {newLinked.start}")
print("-------|----------|---------")
print("Index  --  Name  --  Pointer")
print("-------|----------|---------")
for i in range(0, len(newLinked.listNodes)):
    freespace = 6 - len(newLinked.listNodes[i].name)
    print(str(i) + "    --    " + newLinked.listNodes[i].name +" "*freespace + "    --    " + str(newLinked.listNodes[i].pointer))

print(" ")
newLinked.printAlphabetically()
"""
def addScore(time, username):
    file = open("highscores.text", 'a')
    file.write(f"{username} {time}")
    file.close()
list_of_names = []
time_elapsed = 0
count = 0
# -------- Main Program Loop -----------
bullets = []
import time
x_velocity = 0
string_text = " "
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                current_state = "GAME_STATE"
            if event.key == pygame.K_TAB:
                done = True
            if event.key == pygame.K_LEFT:
                x_velocity = -4
            if event.key == pygame.K_RIGHT:
                x_velocity = 4
            if event.key == pygame.K_UP:
                newBullet = Bullet(player.x, player.y)
                bullets.append(newBullet)
            if event.key == pygame.K_HASH:
                current_state = "LINKED_STATE"
            if event.key == pygame.K_9:
                current_state = "MENU_STATE"
            if event.key == pygame.K_0:
                current_state = "CREDIT_STATE"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                ...
            else:
                x_velocity = 0
        if current_state == "LINKED_STATE":
            if event.type == pygame.KEYDOWN:
                character = event.unicode
                if len(character) == 1:
                    if 122 >= ord(character) >= 97:
                        string_text = string_text + character
                if event.key == pygame.K_RETURN:
                    newLinked.add(string_text)
                    list_of_names.append(string_text)
                    string_text = " "
                elif event.key == pygame.K_BACKSPACE:
                    string_text = string_text[0:len(string_text)-1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(mouse[0])
                print(mouse[1])
                for index in range(0, 5):
                    if (250+(index*200)+100) < mouse[0] < (250+(index*200)+100) + 350:
                        print("SIUEEEY")
                        if 0.65 * screen.get_height() < mouse[1] < 0.65 * screen.get_height() + 30:
                            print("SIU")
                            newLinked.listNodes.remove(newLinked.listNodes[index])
    if current_state == MENU_STATE:
        pygame.display.set_mode((1536, 864),pygame.FULLSCREEN)
        screen.fill(BLACK)
        screen.blit(menu_title_text, [screen.get_width()//2-menu_title_text.get_width()//2, 0.1*screen.get_height()])
        screen.blit(to_play_text, [screen.get_width()//2-to_play_text.get_width()//2, 0.5*screen.get_height()])
        screen.blit(play_linked_text, [screen.get_width()//2-play_linked_text.get_width()//2, 0.65*screen.get_height()])
        screen.blit(exit_text, [screen.get_width()//2-exit_text.get_width()//2, 0.9*screen.get_height()])
    elif current_state == LINKED_STATE:
        screen.fill(BLACK)
        size = 1536, 864
        pygame.display.set_mode(size, pygame.FULLSCREEN)
        start_text = text_font.render(f"Start: {newLinked.start}", True, WHITE)
        nextFree_text = text_font.render(f"Nextfree: {newLinked.nextFree}", True, WHITE)
        screen.blit(start_text, [0, 0])
        screen.blit(nextFree_text, [0, start_text.get_height()+10])
        string_text_text = title_font.render(str(string_text), True, WHITE)
        screen.blit(linked_title, [screen.get_width()//2-linked_title.get_width()//2, 0.1*screen.get_height()])
        screen.blit(enter_text, [screen.get_width()//2-enter_text.get_width()//2, 0.45*screen.get_height()])
        input_box = pygame.draw.rect(screen, WHITE, [screen.get_width()//2-125, 0.5*screen.get_height(), 250, 75], 5)
        for i in range(0, 5):
            pygame.draw.rect(screen, WHITE, [250+(i*200), 0.7*screen.get_height(), 200, round(0.05*screen.get_height())], 1)
            pygame.draw.rect(screen, WHITE, [250+(i*200), 0.75*screen.get_height(), 200, 200], 1)
            pygame.draw.rect(screen, WHITE, [250+(i*200), 0.65*screen.get_height(), 200, round(0.05*screen.get_height())], 1)
        screen.blit(string_text_text, [screen.get_width()//2-120, 441])
        if newLinked.listNodes[0] != None:
            for i in range(0, len(newLinked.listNodes)):
                text = text_font.render(str(list_of_names[i]), True, WHITE)
                pointer = text_font.render(str(newLinked.listNodes[i].pointer), True, WHITE)
                remove = text_font.render(str("Remove Item"), True, WHITE)
                #pointer = text_font.render("Pointer: " + newLinked.listNodes[newLinked.listNodes.index(str(list_of_names[i]))].pointer, True, WHITE)
                screen.blit(text, [(250+(i*200)+100)-text.get_width()//2, (0.75*screen.get_height()+100)-(text.get_height()//2)])
                screen.blit(pointer, [(250+(i*200)+100)-pointer.get_width()//2, (0.7*screen.get_height()+0.05*screen.get_height())-(pointer.get_height())])
                screen.blit(remove, [(250+(i*200)+100)-remove.get_width()//2, (0.65*screen.get_height()+0.05*screen.get_height())-(remove.get_height())])
        if len(list_of_names) == 5:
            message = title_font.render("You successfully created a linked list!", True, GREEN)
            screen.blit(message, [screen.get_width()//2-(message.get_width()//2), 0.35*screen.get_height()])
        list_size_text = text_font.render(f"List size: 5", True, WHITE)
        isFull_text = text_font.render(f"Full?:    {len(newLinked.listNodes)==5}", True, WHITE)
        screen.blit(list_size_text, [start_text.get_width() + 80, 0])
        screen.blit(isFull_text, [start_text.get_width()+ 80 , start_text.get_height()+10])

    elif current_state == "CREDIT_STATE":
        pygame.display.set_mode([credits_image.get_width(), credits_image.get_height()])
        screen.fill(BLACK)
        screen.blit(credits_image, [0,0])
    elif current_state == "USERNAME_STATE":
        screen.fill(BLACK)
        size = 1536, 864
        pygame.display.set_mode(size, pygame.FULLSCREEN)
    elif current_state == GAME_STATE:
        pygame.display.set_mode([1200, 700])
        pygame.display.set_caption("Space Invaders by Elliot")
        screen.fill(BLACK)
        score_text = text_font.render(f"SCORE: {score}", True, RED)
        if len(players) == 0:
            player = Player()
            players.append(player)
        player.x = player.x + x_velocity
        player.draw()
        if len(bullets) > 0:
            #Updating bullet postiions and removing bullets when they leave the frame

            for index, bullet in enumerate(bullets):
                if (bullet.y > 0) == False:
                    bullets.pop(index)
                else:
                    bullet.draw()


        #Player
        if len(objects) == 16 or len(objects) == 0:
            for object in range(0, 17):
                object = Invader()
                objects.append(object)

            if time_elapsed > 0:
                print(time.time()-start_time)
                addScore(round(time.time()-start_time, 3), "Elliot")
            else:
                start_time = time.time()
            #for i in range(0, len(objects)):
            #objects[i].draw(i*30, objects[i].y, 20, 20)
            width_per = (screen.get_width()//17)
            #    objects[i].draw(i*width_per, 10)
            drawRow()
        else:
            for object in objects:
                object.draw()
        #for i in range(0, len(objects)):
         #   objects[i].draw(i*width_per, objects[i].y)
        count = count + 1
        if round(time.time()) % 2 == 0:
            for i in range(0, len(objects)):
                objects[i].move(0, 0.2)
        #Increasing time elapsed
        time_elapsed = time.time()-start_time
        print(round(time_elapsed, 3))
        #Displaying the score at the end, so it has the highest priority
        screen.blit(score_text, [5, 5])
    #Not in if loop -> To prevent unnecessary repeated code
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    if len(bullets) > 0:
        for index in range(0, len(bullets)):
            bullets[index].move(-5)
    for object in objects:
        if object.detectCollision():
            score = score + 100
    # --- Limit to 60 frames per second
    clock.tick(60)
