# Multi-tasking experiment
#This is a replication of Stoet et al 2013 experiment

##Necessary imports
import random
import pygame
import sys

MAX_RESPONSE_DELAY=3000
n_trials=4
multitasking_data = 'multitasking_data.csv'

##Screen Parameters
screenW=500
screenH=500
center_x = screenW // 2
center_y = screenH // 2

def create_window(width_window,height_window):
    screen = pygame.display.set_mode((width_window,height_window))
    pygame.mouse.set_visible(False)
    pygame.display.set_caption('Experiment Multitasking')
    return screen

def clear_screen(screen):
    screen.fill(pygame.Color('white'))
    pygame.display.flip()

def display_first_instruction(screen, x, y):
	dist_btw=50
	myfont = pygame.font.SysFont(pygame.font.get_fonts()[0], 15)
   
	line1 = myfont.render("In the following you will respond to various figures:", 1, pygame.Color('white'))
	line2 = myfont.render("diamonds and rectangles with a filling of 2 or 3 dots.", 1, pygame.Color('white'))
	line3 = myfont.render("You will be shown these figures in sequences of trials ", 1, pygame.Color('white'))
	line4 = myfont.render("Each time you will need to respond either with the left or the right button", 1, pygame.Color('white'))
	line5 = myfont.render("There will be 3 blocks and how exactly you need to respond will be explained before starting each block", 1, pygame.Color('white'))
	line6 = myfont.render("Press it now to start!", 1, pygame.Color('white'))
	screen.blit(line1, (10, y-150))
	screen.blit(line2, (10, y - 100))
	screen.blit(line3, (10, y - 50))
	screen.blit(line4, (10, y ))
	screen.blit(line5, (10, y + 50))
	screen.blit(line6, (10, y + 100))
	pygame.display.flip()
def instruction_shape_task(screen, x, y):
    myfont = pygame.font.SysFont(pygame.font.get_fonts()[0], 15)
    line1 = myfont.render("SHAPE TASK", 1, pygame.Color('black'))
    line2 = myfont.render("In this block, the stimulus will always shown in the upper part", 1, pygame.Color('black'))
    line3 = myfont.render("In this task when you see a diamond press left_button, when you see a rectangle press right_button", 1, pygame.Color('black'))
    line4 = myfont.render("ignore the filling (dots) of the shape", 1, pygame.Color('black'))
    line5 = myfont.render("Press a key now to start!", 1, pygame.Color('black'))
    screen.blit(line1, (10, y-150))
    screen.blit(line2, (10, y - 100))
    screen.blit(line3, (10, y - 50))
    screen.blit(line4, (10, y ))
    screen.blit(line5, (10, y + 50))
    pygame.display.flip()
def instruction_filling_task(screen, x, y):
    myfont = pygame.font.SysFont(pygame.font.get_fonts()[0], 15)
    line1 = myfont.render("FILLING TASK", 1, pygame.Color('black'))
    line2 = myfont.render("In this block, the stimulus will always shown in the bottom part", 1, pygame.Color('black'))
    line3 = myfont.render("A filling of 2 dots requires to press left_button,a filling of 3 dots requires to press right_button", 1, pygame.Color('black'))
    line4 = myfont.render("ignore the the outher shape", 1, pygame.Color('black'))
    line5 = myfont.render("Press a key now to start!", 1, pygame.Color('black'))
    screen.blit(line1, (10, y-150))
    screen.blit(line2, (10, y - 100))
    screen.blit(line3, (10, y - 50))
    screen.blit(line4, (10, y ))
    screen.blit(line5, (10, y + 50))
    pygame.display.flip()
def instruction_mixed_task(screen, x, y):
    myfont = pygame.font.SysFont(pygame.font.get_fonts()[0], 15)
    line1 = myfont.render("MIXED TASK", 1, pygame.Color('black'))
    line2 = myfont.render("If the stimulus appeared in the upper half you have to carry out the shape task", 1, pygame.Color('black'))
    line3 = myfont.render("If the stimulus appeared in the bottom half you have to carry out the filling task", 1, pygame.Color('black'))
    line4 = myfont.render("Press a key now to start!", 1, pygame.Color('black'))
    screen.blit(line1, (10, y-150))
    screen.blit(line2, (10, y - 100))
    screen.blit(line3, (10, y - 50))
    screen.blit(line4, (10, y ))
    pygame.display.flip()
def instruction_feedback(screen, x, y,feedback):
    clear_screen(screen)
    myfont = pygame.font.SysFont(pygame.font.get_fonts()[0], 32)
    line1 = myfont.render(feedback, 1, pygame.Color('black'))
    screen.blit(line1, (x, y))
    pygame.display.flip()
    pygame.time.delay(1000)

def display_frame(screen,width, height, center_x, center_y):
    pygame.draw.rect(screen, (0,0,0), ((center_x)-width//2, (center_y)-height//2, width, height), 3)
    pygame.draw.line(screen, (0,0,0), ((center_x)-width//2, center_y), ((center_x)+ width//2, center_y), 3)
    myfont = pygame.font.SysFont(pygame.font.get_fonts()[0], 28)
    line1 = myfont.render('Shape', 1, pygame.Color('black'))
    screen.blit(line1, (((center_x)-width//4)+30, ((center_y)-height//2)-40))
    line2 = myfont.render('Filling', 1, pygame.Color('black'))
    screen.blit(line2, (((center_x)-width//4)+30, ((center_y)+ height//2)+10))
    pygame.display.flip()
    
def present_stimulus(type, x, a):
    rect3=pygame.image.load("rect_three.png")
    diamond3=pygame.image.load("diamond_three.png")
    rect2=pygame.image.load("rect_two.png")
    diamond2=pygame.image.load("diamond_two.png")
    if type=="rect_3":
        obj=pygame.transform.scale(rect3,(100,100))
    if type=="rect_2":
        obj=pygame.transform.scale(rect2,(100,100))
    if type=="diamond_2":
        obj=pygame.transform.scale(diamond2,(100,100))
    if type=="diamond_3":
        obj=pygame.transform.scale(diamond3,(100,100))
    stimulus=obj.get_rect()
    if a=="down":
        stimulus_y=270
    elif a=="up":
        stimulus_y=120
    screen.blit(obj,(x-50,stimulus_y))
    pygame.display.flip()

def wait_for_keypress():
    key_pressed = False
    while not key_pressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_pressed = True

def measure_reaction_time(max_response_delay=4000):
    button_pressed = False
    escape = False
    response_delay_elapsed = False
    reaction_time = 0
    pressed_key=0
    pygame.event.clear()  
    t0 = pygame.time.get_ticks()

    while not button_pressed and not escape and not response_delay_elapsed:
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                escape = True
                break
            if ev.type == pygame.QUIT:
                escape = True
                break
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_LEFT:
                    reaction_time = pygame.time.get_ticks() - t0
                    pressed_key= "leftKey"  
                    button_pressed = True
                elif ev.key == pygame.K_RIGHT:
                    reaction_time = pygame.time.get_ticks() - t0
                    pressed_key= "rightKey"
                    button_pressed = True
                else:
                    continue
        if pygame.time.get_ticks() - t0 > MAX_RESPONSE_DELAY:
            pressed_key = "NoResp"
            response_delay_elapsed = True
    
    return (reaction_time, pressed_key,escape)

def measure_accuracy(type,key,position):
    if position=="up":
        if key == "leftKey":
            if type =="diamond_3" or type=="diamond_2":
                accuracy=1 
            elif type=="rect_3" or type=="rect_2":
                accuracy=0
        elif key == "rightKey" :
            if type =="diamond_3" or type=="diamond_2":
                accuracy=0
            elif type== "rect_3" or type=="rect_2":
                accuracy=1
        elif key=="NoResp":
            accuracy=None
    elif position== "down":
        if key == "leftKey":
            if type =="rect_3" or type=="diamond_3":
                accuracy=0
            elif type=="rect_2" or type=="diamond_2":
                accuracy=1
        elif key == "rightKey" :
            if type=="rect_3" or type=="diamond_3":
                accuracy=1
            elif type=="rect_2" or type=="diamond_2":
                accuracy=0
        elif key=="NoResp":
            accuracy=None

    return (accuracy)

def save_data(ac_shape,rt_shape,ac_filling,rt_filling,ac_mixed,rt_mixed, filename):
    with open(filename, 'wt') as f:
        f.write('AC_shape,RT_shape,AC_filling,RT_filling,AC_mixed,RT_mixed\n')
        for  ac_shape, rt_shape,ac_filling,rt_filling,ac_mixed,rt_mixed in zip(ac_shape,rt_shape,ac_filling,rt_filling,ac_mixed,rt_mixed):
            f.write(f"{ac_shape},{rt_shape},{ac_filling},{rt_filling},{ac_mixed},{rt_mixed}\n")

##MAIN-EXPERIMENT

pygame.init()

screen = create_window(screenW,screenH)

##Block1_Pure_Shape_Task

trials= (n_trials//4) * ["rect_3","rect_2","diamond_3","diamond_2"]
random.shuffle(trials)
rt_shape = []
ac_shape = []
pressed_key= []
display_first_instruction(screen, center_x, center_y)
wait_for_keypress()
clear_screen(screen)
instruction_shape_task(screen, center_x, center_y)
wait_for_keypress()
clear_screen(screen)
pygame.time.delay(1000)

for i in trials:
    clear_screen(screen)
    display_frame(screen,250,300,center_x,center_y)
    present_stimulus(i, center_x, "up")
    [reaction_time,pressed_key,escape] = measure_reaction_time()
    if escape == True:  # escape pressed
        break
    rt_shape.append(reaction_time)
    accuracy= measure_accuracy(i,pressed_key,"up")
    ac_shape.append(accuracy)
    print(i, reaction_time, accuracy)
    if accuracy==0:
        instruction_feedback(screen, 40, center_y,"That was the wrong answer")
    elif accuracy== None:
        instruction_feedback(screen, 40, center_y,"Time is up!")
    else:
        continue
   

##Block2_Pure_Filling_Task

rt_filling = []
ac_filling = []
pressed_key= []
clear_screen(screen)
instruction_filling_task(screen, center_x, center_y)
wait_for_keypress()
clear_screen(screen)
pygame.time.delay(1000)

for i in trials:
    clear_screen(screen)
    display_frame(screen,250,300,center_x,center_y)
    present_stimulus(i, center_x, "down")
    [reaction_time,pressed_key,escape] = measure_reaction_time()
    if escape == True:  # escape pressed
        break
    rt_filling.append(reaction_time)
    accuracy= measure_accuracy(i,pressed_key,"down")
    ac_filling.append(accuracy)
    print(i, reaction_time, accuracy)
    if accuracy==0:
        instruction_feedback(screen, 40, center_y,"That was the wrong answer")
    elif accuracy== None:
        instruction_feedback(screen, 40, center_y,"Time is up!")
    else:
        continue


## Block3_Mixed_Task

positions= (n_trials//2) * ["up","down"]
random.shuffle(positions)
rt_mixed = []
ac_mixed = []
pressed_key= []
clear_screen(screen)
instruction_mixed_task(screen, center_x, center_y)
wait_for_keypress()
clear_screen(screen)
pygame.time.delay(1000)

for c in range(n_trials):
    i=trials[c]
    a= positions[c]
    clear_screen(screen)
    display_frame(screen,250,300,center_x,center_y)
    present_stimulus(i, center_x, a)
    [reaction_time,pressed_key,escape] = measure_reaction_time()
    if escape == True:  # escape pressed
        break
    rt_mixed.append(reaction_time)
    accuracy= measure_accuracy(i,pressed_key,a)
    ac_mixed.append(accuracy)
    print(i, reaction_time, accuracy)
    if accuracy==0:
        instruction_feedback(screen, 40, center_y,"That was the wrong answer!")
    elif accuracy== None:
        instruction_feedback(screen, 40, center_y,"Time is up!")
    else:
        continue

save_data(ac_shape,rt_shape,ac_filling,rt_filling,ac_mixed,rt_mixed,multitasking_data)

pygame.quit()