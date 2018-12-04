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

def randomletterarray1():
	global outputarray
	outputarray=[0]*8
	for i in range(0,8):
		numbertoletter=random.randint(1,26)
		if numbertoletter==1:
			outputarray[i]="A"
		elif numbertoletter==2:
			outputarray[i]="B"
		elif numbertoletter==3:
			outputarray[i]="C"
		elif numbertoletter==4:
			outputarray[i]="D"
		elif numbertoletter==5:
			outputarray[i]="E"
		elif numbertoletter==6:
			outputarray[i]="F"
		elif numbertoletter==7:
			outputarray[i]="G"
		elif numbertoletter==8:
			outputarray[i]="H"
		elif numbertoletter==9:
			outputarray[i]="I"
		elif numbertoletter==10:
			outputarray[i]="J"
		elif numbertoletter==11:
			outputarray[i]="K"
		elif numbertoletter==12:
			outputarray[i]="L"
		elif numbertoletter==13:
			outputarray[i]="M"
		elif numbertoletter==14:
			outputarray[i]="N"
		elif numbertoletter==15:
			outputarray[i]="O"
		elif numbertoletter==16:
			outputarray[i]="P"
		elif numbertoletter==17:
			outputarray[i]="Q"
		elif numbertoletter==18:
			outputarray[i]="R"
		elif numbertoletter==19:
			outputarray[i]="S"
		elif numbertoletter==20:
			outputarray[i]="T"
		elif numbertoletter==21:
			outputarray[i]="U"
		elif numbertoletter==22:
			outputarray[i]="V"
		elif numbertoletter==23:
			outputarray[i]="W"
		elif numbertoletter==24:
			outputarray[i]="X"
		elif numbertoletter==25:
			outputarray[i]="Y"
		elif numbertoletter==26:
			outputarray[i]="Z"


def randomletterarray2():
	global outputarray2
	outputarray2=[0]*8
	for i in range(0,8):
		numbertoletter=random.randint(1,26)
		if numbertoletter==1:
			outputarray2[i]="A"
		elif numbertoletter==2:
			outputarray2[i]="B"
		elif numbertoletter==3:
			outputarray2[i]="C"
		elif numbertoletter==4:
			outputarray2[i]="D"
		elif numbertoletter==5:
			outputarray2[i]="E"
		elif numbertoletter==6:
			outputarray2[i]="F"
		elif numbertoletter==7:
			outputarray2[i]="G"
		elif numbertoletter==8:
			outputarray2[i]="H"
		elif numbertoletter==9:
			outputarray2[i]="I"
		elif numbertoletter==10:
			outputarray2[i]="J"
		elif numbertoletter==11:
			outputarray2[i]="K"
		elif numbertoletter==12:
			outputarray2[i]="L"
		elif numbertoletter==13:
			outputarray2[i]="M"
		elif numbertoletter==14:
			outputarray2[i]="N"
		elif numbertoletter==15:
			outputarray2[i]="O"
		elif numbertoletter==16:
			outputarray2[i]="P"
		elif numbertoletter==17:
			outputarray2[i]="Q"
		elif numbertoletter==18:
			outputarray2[i]="R"
		elif numbertoletter==19:
			outputarray2[i]="S"
		elif numbertoletter==20:
			outputarray2[i]="T"
		elif numbertoletter==21:
			outputarray2[i]="U"
		elif numbertoletter==22:
			outputarray2[i]="V"
		elif numbertoletter==23:
			outputarray2[i]="W"
		elif numbertoletter==24:
			outputarray2[i]="X"
		elif numbertoletter==25:
			outputarray2[i]="Y"
		elif numbertoletter==26:
			outputarray2[i]="Z"

def randomletterarray3():
	global outputarray3
	outputarray3=[0]*8
	for i in range(0,8):
		numbertoletter=random.randint(1,26)
		if numbertoletter==1:
			outputarray3[i]="A"
		elif numbertoletter==2:
			outputarray3[i]="B"
		elif numbertoletter==3:
			outputarray3[i]="C"
		elif numbertoletter==4:
			outputarray3[i]="D"
		elif numbertoletter==5:
			outputarray3[i]="E"
		elif numbertoletter==6:
			outputarray3[i]="F"
		elif numbertoletter==7:
			outputarray3[i]="G"
		elif numbertoletter==8:
			outputarray3[i]="H"
		elif numbertoletter==9:
			outputarray3[i]="I"
		elif numbertoletter==10:
			outputarray3[i]="J"
		elif numbertoletter==11:
			outputarray3[i]="K"
		elif numbertoletter==12:
			outputarray3[i]="L"
		elif numbertoletter==13:
			outputarray3[i]="M"
		elif numbertoletter==14:
			outputarray3[i]="N"
		elif numbertoletter==15:
			outputarray3[i]="O"
		elif numbertoletter==16:
			outputarray3[i]="P"
		elif numbertoletter==17:
			outputarray3[i]="Q"
		elif numbertoletter==18:
			outputarray3[i]="R"
		elif numbertoletter==19:
			outputarray3[i]="S"
		elif numbertoletter==20:
			outputarray3[i]="T"
		elif numbertoletter==21:
			outputarray3[i]="U"
		elif numbertoletter==22:
			outputarray3[i]="V"
		elif numbertoletter==23:
			outputarray3[i]="W"
		elif numbertoletter==24:
			outputarray3[i]="X"
		elif numbertoletter==25:
			outputarray3[i]="Y"
		elif numbertoletter==26:
			outputarray3[i]="Z"

def randomletterarray4():
	global outputarray4
	outputarray4=[0]*8
	for i in range(0,8):
		numbertoletter=random.randint(1,26)
		if numbertoletter==1:
			outputarray4[i]="A"
		elif numbertoletter==2:
			outputarray4[i]="B"
		elif numbertoletter==3:
			outputarray4[i]="C"
		elif numbertoletter==4:
			outputarray4[i]="D"
		elif numbertoletter==5:
			outputarray4[i]="E"
		elif numbertoletter==6:
			outputarray4[i]="F"
		elif numbertoletter==7:
			outputarray4[i]="G"
		elif numbertoletter==8:
			outputarray4[i]="H"
		elif numbertoletter==9:
			outputarray4[i]="I"
		elif numbertoletter==10:
			outputarray4[i]="J"
		elif numbertoletter==11:
			outputarray4[i]="K"
		elif numbertoletter==12:
			outputarray4[i]="L"
		elif numbertoletter==13:
			outputarray4[i]="M"
		elif numbertoletter==14:
			outputarray4[i]="N"
		elif numbertoletter==15:
			outputarray4[i]="O"
		elif numbertoletter==16:
			outputarray4[i]="P"
		elif numbertoletter==17:
			outputarray4[i]="Q"
		elif numbertoletter==18:
			outputarray4[i]="R"
		elif numbertoletter==19:
			outputarray4[i]="S"
		elif numbertoletter==20:
			outputarray4[i]="T"
		elif numbertoletter==21:
			outputarray4[i]="U"
		elif numbertoletter==22:
			outputarray4[i]="V"
		elif numbertoletter==23:
			outputarray4[i]="W"
		elif numbertoletter==24:
			outputarray4[i]="X"
		elif numbertoletter==25:
			outputarray4[i]="Y"
		elif numbertoletter==26:
			outputarray4[i]="Z"

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

Instructions1=visual.TextStim(win=window, text='Record the letters and position of the letters that you can recall, then press the f key to see the actual configuration, press the spacebar to exit the screen at any time', pos=(0,0))




def letterfunc():
	randomletterarray1()
	randomletterarray2()
	randomletterarray3()
	randomletterarray4()
	countinstruct=0
	while clock.getTime()<=40.0:
		if clock.getTime()<3.0:
			vline.draw()
			hline.draw()
			window.flip()
		elif event.getKeys("space"):
			break
		elif event.getKeys("f"):
			countinstruct=1
			lettertext(outputarray[0],outputarray[1],outputarray[2],outputarray[3],outputarray[4],outputarray[5],outputarray[6],outputarray[7],1.0,1.0)
			lettertext(outputarray2[0],outputarray2[1],outputarray2[2],outputarray2[3],outputarray2[4],outputarray2[5],outputarray2[6],outputarray2[7],2.0,4.0)
			lettertext(outputarray3[0],outputarray3[1],outputarray3[2],outputarray3[3],outputarray3[4],outputarray3[5],outputarray3[6],outputarray3[7],3.0,7.0)
			lettertext(outputarray4[0],outputarray4[1],outputarray4[2],outputarray4[3],outputarray4[4],outputarray4[5],outputarray4[6],outputarray4[7],3.0,10.0)
			window.flip()
		elif clock.getTime()>=5.0 and clock.getTime()<=30.0 and countinstruct==0:
			Instructions1.draw()
			window.flip()
		elif clock.getTime()>=3.0 and clock.getTime()<=5.0:
			lettertext(outputarray[0],outputarray[1],outputarray[2],outputarray[3],outputarray[4],outputarray[5],outputarray[6],outputarray[7],1.0,1.0)
			lettertext(outputarray2[0],outputarray2[1],outputarray2[2],outputarray2[3],outputarray2[4],outputarray2[5],outputarray2[6],outputarray2[7],2.0,4.0)
			lettertext(outputarray3[0],outputarray3[1],outputarray3[2],outputarray3[3],outputarray3[4],outputarray3[5],outputarray3[6],outputarray3[7],3.0,7.0)
			lettertext(outputarray4[0],outputarray4[1],outputarray4[2],outputarray4[3],outputarray4[4],outputarray4[5],outputarray4[6],outputarray4[7],4.0,10.0)
			window.flip()


window.flip()
clock.reset

letterfunc()