import os
from psychopy import visual, core, event
import numpy as np
import random

#Goals, same as Anstis exp lined out in text, graph size of letters (in degrees) versus eccentricity (in degrees) of where they were located, flash the letter screens
#Record all parameters, try it multiple ways, flash, dont flash, all that... design it such that the letters are equally readable due to size increasing as distance goes out

window=visual.Window(fullscr=True, monitor="testMonitor",units="deg")
hline=visual.Line(win=window,size=0.5,start=(-1.0,0.0),end=(1.0,0.0))
vline=visual.Line(win=window,size=0.5,start=(0.0,-1.0),end=(0.0,1.0))




clock = core.Clock()

#Eventually will want to streamline code so that a function takes care of all the stimuli popping up, but for now I want to get a baseline working
#def letterring:
#	window.flip()

#EIght letters in a ring...



####################################
# Randomizing the letters involved #
####################################

def letterrandomizer():
	numbertoletter=random.randint(1,26)
	a="A"
	b="B"
	c="C"
	d="D"
	e="E"
	f="F"
	g="G"
	h="H"
	i="I"
	j="J"
	k="K"
	l="L"
	m="M"
	n="N"
	p="P"
	q="Q"
	r="R"
	s="S"
	t="T"
	u="U"
	v="V"
	w="W"
	x="X"
	y="Y"
	z="Z"
	numbertoletterperm=numbertoletter
	if numbertoletterperm==1:
		return "A"
	elif numbertoletterperm==2:
		return "B"
	elif numbertoletter==3:
		return "C"
	elif numbertoletter==4:
		return "D"
	elif numbertoletter==5:
		return "E"
	elif numbertoletter==6:
		return "F"
	elif numbertoletter==7:
		return "G"
	elif numbertoletter==8:
		return "H"
	elif numbertoletter==9:
		return "I"
	elif numbertoletter==10:
		return "J"
	elif numbertoletter==11:
		return "K"
	elif numbertoletter==12:
		return "L"
	elif numbertoletter==13:
		return "M"
	elif numbertoletter==14:
		return "N"
	elif numbertoletter==15:
		return "O"
	elif numbertoletter==16:
		return "P"
	elif numbertoletter==17:
		return "Q"
	elif numbertoletter==18:
		return "R"
	elif numbertoletter==19:
		return "S"
	elif numbertoletter==20:
		return "T"
	elif numbertoletter==21:
		return "U"
	elif numbertoletter==22:
		return "V"
	elif numbertoletter==23:
		return "W"
	elif numbertoletter==24:
		return "X"
	elif numbertoletter==25:
		return "Y"
	elif numbertoletter==26:
		return "Z"





def lettertext(text1, text2, text3, text4, text5, text6, text7, text8 ,h, posi):
	one=visual.TextStim(win=window, text=text1, height=h, pos=(0.0, posi))
	two=visual.TextStim(win=window, text=text2, height=h, pos=(np.sqrt(2*(posi**2))/2,np.sqrt(2*(posi**2))/2))
	three=visual.TextStim(win=window, text=text3, height=h, pos=(posi, 0.0))
	four=visual.TextStim(win=window, text=text4, height=h, pos=(np.sqrt(2*(posi**2))/2,-np.sqrt(2*(posi**2))/2))
	five=visual.TextStim(win=window, text=text5, height=h, pos=(0.0,-posi))
	six=visual.TextStim(win=window, text=text6, height=h, pos=(-np.sqrt(2*(posi**2))/2,-np.sqrt(2*(posi**2))/2))
	seven=visual.TextStim(win=window, text=text7, height=h, pos=(-posi,0.0))
	eight=visual.TextStim(win=window, text=text8, height=h, pos=(-np.sqrt(2*(posi**2))/2,np.sqrt(2*(posi**2))/2))
	one.draw()
	two.draw()
	three.draw()
	four.draw()
	five.draw()
	six.draw()
	seven.draw()
	eight.draw()
	print text1
	print text2
	print text3

Instructions1=visual.TextStim(win=window, text='Record the letters and position of the letters that you can recall, then press the spacebar when ready to see the actual configuration', pos=(0,0))

def letterfunc():
	count=0
	while clock.getTime()<=15.0:
		if clock.getTime()<5.0:
			vline.draw()
			hline.draw()
			window.flip()
		elif clock.getTime()>=5.0 and clock.getTime()<=10.0:
			if count==0:
				lettertext(letterrandomizer(),letterrandomizer(),letterrandomizer(),letterrandomizer(),letterrandomizer(),letterrandomizer(),letterrandomizer(),letterrandomizer(),1.0,1.0)
				#lettertext("H","G","F","E","D","C","B","A",2.0,3.0)
				#lettertext("A","B","C","D","E","F","G","H",3.0,5.0)
				lettertext("A","B","C","D","E","F","G","H",2.0,5.0)
				window.flip()
				count=1
			elif count>=1:
				count=1
		elif clock.getTime()>10.0:
			Instructions1.draw()
			window.flip()
			#if clock.getTime()>=20.0 and clock.getTime()<=30.0:
			#	clock.getTime()=11.0
	#		elif event.getKeys('space'):










window.flip()
clock.reset

letterfunc()