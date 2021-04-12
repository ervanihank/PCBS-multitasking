# Are women better than men at multi-tasking? #
# This is a replication of Stoet et al 2013 experiment
# There are 3 blocks in the experiment (Block1=Shape Task Block, Block1= Filling Task Block, Bloc3= Mixed Task Block)

##Necessary imports
import random
import pygame
import sys

##Important Parameters
n_trials_per_block=4
multitasking_data = 'multitasking_data.csv'
screenW, screenH=800, 800
center_x, center_y = screenW // 2, screenH // 2
frame_height= 3 * (screenH // 4)
frame_width=  2 * (frame_height//3)
stimulus_width,stimulus_height=screenW//5 , screenH//5

##instruction texts
general_instruct="In the following you will respond to various figures: "\
	"\n   Diamonds and Rectangles with a filling of 2 or 3 dots."\
	"\nYou will be shown these figures in sequences of trials"\
	"Each time you will need to respond either with the left or the right button"\
	"\n\nThere will be 3 blocks and how exactly you need to respond will be explained before starting each block"\
	"\n\n                         Press a key now to start!"
shape_task_instruct="        SHAPE TASK\n"\
    "\n\nIn this block, the stimulus will always shown in the UPPER PART\n"\
    "When you see a Diamond : \n   Press LEFT BUTTON \nWhen you see a Rectangle : \n   Press RIGHT BUTTON"\
    "\nIgnore the filling(dots) of the shape\n"\
    "\n\n                         Press a key now to start!"
filling_task_instruct="      FILLING TASK\n"\
    "\n\nIn this block, the stimulus will always shown in the BOTTOM PART\n"\
    "When you see a filling of 2 dots \n Press LEFT BUTTON \n When you see a filling of 3 dots \n Press RIGHT BUTTON"\
    "Ignore the the outher shape\n"\
    "\n\n                         Press a key now to start!"
mixed_task_instruct="        MIXED TASK\n"\
    "\n\nIf the stimulus appeared in the upper half \n you have to carry out the shape task\n"\
    "If the stimulus appeared in the bottom half \n you have to carry out the filling task"\
    "\n\n                         Press a key now to start!"

def create_window(width_window,height_window):
    screen = pygame.display.set_mode((width_window,height_window),pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)
    pygame.display.set_caption('Experiment Multitasking')
    return screen

def clear_screen(screen):
    screen.fill(pygame.Color('white'))
    pygame.display.flip()

def display_instruction(screen, text, pos, font, color=pygame.Color('black')):
    clear_screen(screen)
    words = [word.split(' ') for word in text.splitlines()] 
    space = font.size(' ')[0]  
    max_width, max_height = screen.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0] 
                y += word_height  
            screen.blit(word_surface, (x- (frame_width//2), y-(frame_height//3)))
            x += word_width + space
        x = pos[0] 
        y += word_height  
        pygame.display.flip()
    
def display_feedback(screen, x, y,feedback_message):
    clear_screen(screen)
    myfont = pygame.font.SysFont('Courier',screenW//20,bold=True)
    line = myfont.render(feedback_message, 1, pygame.Color('black'))
    text_width=line.get_width()
    screen.blit(line, (x-(text_width//2), y))
    pygame.display.flip()
    pygame.time.delay(1000)
    clear_screen(screen)
    pygame.time.delay(500)  

def display_frame(screen,x,y):
	pygame.draw.rect(screen, (0,0,0), (x-(frame_width//2), y-(frame_height//2), frame_width, frame_height), 3)
	pygame.draw.line(screen, (0,0,0), (x-(frame_width//2), center_y), (x + (frame_width//2), center_y), 3)
	myfont = pygame.font.SysFont('Courier',screenW//20,bold=True)
	lineshape = myfont.render('Shape', 1, pygame.Color('black'))
	linefilling = myfont.render('Filling', 1, pygame.Color('black'))
	shape_width = lineshape.get_width()
	shape_height = lineshape.get_height()
	filling_width = linefilling.get_width()
	filling_height = linefilling.get_height()
	screen.blit(lineshape, (x-(shape_width//2), y-((frame_height//2)+shape_height)))
	screen.blit(linefilling, (x-(filling_width//2), y + ((frame_height//2))))
	pygame.display.flip()

def display_stimulus(stimulus_type, stimulus_position):
    rect3=pygame.image.load("rect_three.png")
    diamond3=pygame.image.load("diamond_three.png")
    rect2=pygame.image.load("rect_two.png")
    diamond2=pygame.image.load("diamond_two.png")
    if stimulus_type=="rect_3":
        stimulus_selected=pygame.transform.scale(rect3,(stimulus_width,stimulus_height))
    if stimulus_type=="rect_2":
        stimulus_selected=pygame.transform.scale(rect2,(stimulus_width,stimulus_height))
    if stimulus_type=="diamond_2":
        stimulus_selected=pygame.transform.scale(diamond2,(stimulus_width,stimulus_height))
    if stimulus_type=="diamond_3":
        stimulus_selected=pygame.transform.scale(diamond3,(stimulus_width,stimulus_height))
    stimulus=stimulus_selected.get_rect()
    if stimulus_position =="down":
        stimulus_coordinate_y=center_y + frame_height//4 - stimulus_height//2
    elif stimulus_position =="up":
        stimulus_coordinate_y=center_y - frame_height//4 - stimulus_height//2
    screen.blit(stimulus_selected,((center_x)-(stimulus_width//2), stimulus_coordinate_y))
    pygame.display.flip()

def wait_for_keypress(quit_button=pygame.K_q):
	key_pressed = False
	while not key_pressed:
		for ev in pygame.event.get():
			if ev.type == pygame.KEYDOWN:
				if ev.key== quit_button:
					pygame.quit()
					sys.exit()
				else:
					key_pressed = True

def measure_reaction_time(max_response_delay=4000,quit_button=pygame.K_q):
    response_delay_elapsed = False
    reaction_time = 0
    pressed_key = None
    pygame.event.clear()  
    t0 = pygame.time.get_ticks()

    while not response_delay_elapsed and pressed_key is None:
        for ev in pygame.event.get():
            if ev.key == quit_button:
            	pygame.quit()
            	sys.exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_LEFT:
                    reaction_time = pygame.time.get_ticks() - t0
                    pressed_key= "leftKey"  
                elif ev.key == pygame.K_RIGHT:
                    reaction_time = pygame.time.get_ticks() - t0
                    pressed_key= "rightKey"
        if pygame.time.get_ticks() - t0 > max_response_delay:
            pressed_key = "NoResp"
            response_delay_elapsed = True
    
    return (reaction_time, pressed_key)

def measure_accuracy(stimulus_type, pressed_key, stimulus_position):
    if stimulus_position=="up":
        if pressed_key == "leftKey":
            if stimulus_type =="diamond_3" or stimulus_type=="diamond_2":
                accuracy=1 
            elif stimulus_type=="rect_3" or stimulus_type=="rect_2":
                accuracy=0
        elif pressed_key == "rightKey" :
            if stimulus_type =="diamond_3" or stimulus_type=="diamond_2":
                accuracy=0
            elif stimulus_type== "rect_3" or stimulus_type=="rect_2":
                accuracy=1
        elif pressed_key=="NoResp":
            accuracy=None
    elif stimulus_position== "down":
        if pressed_key == "leftKey":
            if stimulus_type =="rect_3" or stimulus_type=="diamond_3":
                accuracy=0
            elif stimulus_type=="rect_2" or stimulus_type=="diamond_2":
                accuracy=1
        elif pressed_key == "rightKey" :
            if stimulus_type=="rect_3" or stimulus_type=="diamond_3":
                accuracy=1
            elif stimulus_type=="rect_2" or stimulus_type=="diamond_2":
                accuracy=0
        elif pressed_key=="NoResp":
            accuracy=None
    if accuracy==0:
        display_feedback(screen, center_x, center_y,"That was the wrong answer")
    elif accuracy== None:
        display_feedback(screen, center_x, center_y,"Time is up!")


    return (accuracy)

def save_data(stim_type_shapeblock,ac_shape,rt_shape,stim_type_fillingblock,ac_filling,rt_filling,task_mixedblock,stim_type_mixedblock,ac_mixed,rt_mixed, filename):
    with open(filename, 'wt') as f:
        f.write('stim_type_shapeblock,AC_shape,RT_shape,stim_type_fillingblock,AC_filling,RT_filling,task_mixedblock,stim_type_mixedblock,AC_mixed,RT_mixed\n')
        for  stim_type_shapeblock,ac_shape, rt_shape,stim_type_fillingblock,ac_filling,rt_filling,task_mixedblock,stim_type_mixedblock,ac_mixed,rt_mixed in zip(stim_type_shapeblock,ac_shape, rt_shape,stim_type_fillingblock,ac_filling,rt_filling,task_mixedblock,stim_type_mixedblock,ac_mixed,rt_mixed):
            f.write(f"{stim_type_shapeblock},{ac_shape},{rt_shape},{stim_type_fillingblock},{ac_filling},{rt_filling},{task_mixedblock},{stim_type_mixedblock},{ac_mixed},{rt_mixed}\n")

## MAIN-EXPERIMENT ##

pygame.init()
screen = create_window(screenW,screenH)

trials= (n_trials_per_block//4) * ["rect_3","rect_2","diamond_3","diamond_2"]
random.shuffle(trials)

instruction_font = pygame.font.SysFont('Courier',screenW//36,bold=True)
display_instruction(screen, general_instruct, (center_x, center_y), instruction_font)

wait_for_keypress()
pygame.time.delay(600)

## Block_1_(Pure)_Shape_Block ##

stim_type_shapeblock= []
rt_shape = []
ac_shape = []

display_instruction(screen, shape_task_instruct, (center_x, center_y), instruction_font)
wait_for_keypress()
pygame.time.delay(600)

for i in range(n_trials_per_block):
	stimulus_type=trials[i]

	clear_screen(screen)
	display_frame(screen,center_x,center_y)
	pygame.time.delay(800)
	display_stimulus(stimulus_type, "up")

	[reaction_time,pressed_key] = measure_reaction_time()
	accuracy= measure_accuracy(stimulus_type,pressed_key,"up")

	rt_shape.append(reaction_time)
	ac_shape.append(accuracy)
	stim_type_shapeblock.append(stimulus_type)

	print(stimulus_type, reaction_time, accuracy)

## Block2_(Pure)_Filling_Block ##

stim_type_fillingblock= []
rt_filling = []
ac_filling = []

display_instruction(screen, filling_task_instruct, (center_x, center_y), instruction_font)
wait_for_keypress()
pygame.time.delay(600)

for i in range(n_trials_per_block):
	stimulus_type=trials[i]

	clear_screen(screen)
	display_frame(screen,center_x,center_y)
	pygame.time.delay(800)
	display_stimulus(stimulus_type, "down")

	[reaction_time,pressed_key] = measure_reaction_time()
	accuracy= measure_accuracy(stimulus_type,pressed_key,"down")

	rt_filling.append(reaction_time)
	ac_filling.append(accuracy)
	stim_type_fillingblock.append(stimulus_type)

	print(stimulus_type, reaction_time, accuracy)

## Block3_Mixed_Block ##

positions= (n_trials_per_block//2) * ["up","down"]
random.shuffle(positions)

task_mixedblock=[]
stim_type_mixedblock=[]
rt_mixed = []
ac_mixed = []

display_instruction(screen, mixed_task_instruct, (center_x, center_y), instruction_font)
wait_for_keypress()
pygame.time.delay(600)

for c in range(n_trials_per_block):
	stimulus_type=trials[c]
	stimulus_position= positions[c]

	if stimulus_position== "up":
		task="shape"
	elif stimulus_position== "down":
		task="filling"

	clear_screen(screen)
	display_frame(screen,center_x,center_y)
	pygame.time.delay(800)
	display_stimulus(stimulus_type, stimulus_position)

	[reaction_time,pressed_key] = measure_reaction_time()
	accuracy= measure_accuracy(stimulus_type,pressed_key,stimulus_position)

	task_mixedblock.append(task)
	stim_type_mixedblock.append(stimulus_type)
	rt_mixed.append(reaction_time)
	ac_mixed.append(accuracy)

	print(stimulus_type, reaction_time, accuracy)

save_data(stim_type_shapeblock,ac_shape, rt_shape,stim_type_fillingblock,ac_filling,rt_filling,task_mixedblock,stim_type_mixedblock,ac_mixed,rt_mixed,multitasking_data)

pygame.quit()