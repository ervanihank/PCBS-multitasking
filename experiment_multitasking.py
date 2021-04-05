# Multi-tasking experiment

#This is a replication of Stoet et al 2013 experiment
##Necessary imports
import random
import pygame


def parameters():
	##Colors
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	# Parameters of the window
	W=500
	H=500  
	center_x_window = W // 2
	center_y_window = H // 2

	##Parameters of the frame
	width_frame=250
	height_frame=300
	left_frame=center_x_window- width_frame//2
	top_frame=center_y_window- height_frame//2
	color_frame=BLACK
	w_frame=3
	line_width=w_frame
	line_length=width_frame
	line_color=BLACK
	line_start_x=left_frame
	line_stop_x=left_frame + width_frame
	line_y=center_y_window

	##Parameters of the stimulus
	#rectangle
	width_rect=width_frame//4
	height_rect=width_frame//4
	left_rect= (center_x_window) - (width_rect//2)
	up_rect_y=top_frame + (height_frame//8)
	down_rect_y=top_frame + (5* (height_frame//8))
	w_rect=3
	color_rect=BLACK
	#circle
	two_circle_up= (up_rect_y) + (2*(width_rect//8))
	two_circle_down= (down_rect_y) + (2*(width_rect//8))
	three_circle_up= (up_rect_y) + ((3 * (width_rect//9))//2)
	three_circle_down= (down_rect_y) + ((3 * (width_rect//9))//2)
	dist_btw_circ= 2*(width_rect//8)
	circ_radius=0
	surface=8


def rectangle(position_Shape,circle_Num,shape):
	parameters()
	if cirle_Num==2:
		if position_Shape==1: 
			top_rect=up_rect_y
			circ_start=two_circle_up
		elif position_Shape==0:
			top_rect=down_rect_y
			circ_start=two_circle_down
	elif cirle_Num==3:
		if position_Shape==1:
			top_rect=up_rect_y
			circ_start=three_circle_up
		elif position_Shape==0:
			top_rect=down_rect_y
			circ_start=three_circle_down
	for i in range (circle_Num):
		circ_start= circ_start + dist_btw_circ
		pygame.draw.circle(surface, BLACK , (center_x_window, circ_start), circ_radius)
	if shape==1:
		pygame.draw.rect(screen, BLACK , (left_rect, top_rect, width_rect, height_rect),w_rect)
	elif shape==2:
		pygame.draw.polygon(screen,BLACK , (left_rect+(width_rect//2),top_rect), (left_rect+(width_rect//2), top_rect+height_rect),(left_rect, top_rect+(height_rect//2)),(left_rect+width_rect, top_rect+ (height_rect//2),w_rect)


pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption('experimentmultitasking')

screen.fill(WHITE)  
pygame.draw.rect(screen, color_frame, (left_frame, top_frame, width_frame, height_frame),w_frame)
pygame.draw.line(screen, line_color, (line_start_x, line_y), (line_stop_x, line_y), line_width)
rectangle(1,2,2)

pygame.display.flip()

quit_button_pressed = False
while not quit_button_pressed:
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_button_pressed = True

pygame.quit()