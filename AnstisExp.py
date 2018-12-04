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
	o="O"
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
		A=numbertoletter
		return a
	elif numbertoletterperm==2:
		B=numbertoletter
		return b
	elif numbertoletter==3:
		C=numbertoletter
		return c
	elif numbertoletter==4:
		D=numbertoletter
		return d
	elif numbertoletter==5:
		E=numbertoletter
		return e
	elif numbertoletter==6:
		F=numbertoletter
		return f
	elif numbertoletter==7:
		G=numbertoletter
		return g
	elif numbertoletter==8:
		H=numbertoletter
		return h
	elif numbertoletter==9:
		I=numbertoletter
		return i
	elif numbertoletter==10:
		J=numbertoletter
		return j
	elif numbertoletter==11:
		K=numbertoletter
		return k
	elif numbertoletter==12:
		L=numbertoletter
		return l
	elif numbertoletter==13:
		M=numbertoletter
		return m
	elif numbertoletter==14:
		N=numbertoletter
		return n
	elif numbertoletter==15:
		O=numbertoletter
		return o
	elif numbertoletter==16:
		P=numbertoletter
		return p
	elif numbertoletter==17:
		Q=numbertoletter
		return q
	elif numbertoletter==18:
		R=numbertoletter
		return r
	elif numbertoletter==19:
		S=numbertoletter
		return s
	elif numbertoletter==20:
		T=numbertoletter
		return t
	elif numbertoletter==21:
		U=numbertoletter
		return u
	elif numbertoletter==22:
		V=numbertoletter
		return v
	elif numbertoletter==23:
		W=numbertoletter
		return w
	elif numbertoletter==24:
		X=numbertoletter
		return x
	elif numbertoletter==25:
		Y=numbertoletter
		return y
	elif numbertoletter==26:
		Z=numbertoletter
		return z





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

Instructions1=visual.TextStim(win=window, text='Record the letters and position of the letters that you can recall, then press the spacebar when ready to see the actual configuration', pos=(0,0))

def letterring():
	lettertext("A","B","C","D","E","F","G","H",2.0,5.0)
	lettertext("A","B","C","D","E","F","G","H",2.0,5.0)
	lettertext("A","B","C","D","E","F","G","H",2.0,5.0)
	lettertext("A","B","C","D","E","F","G","H",2.0,5.0)


def letterfunc():
	count=0
	countspace=0
	countinstruct=0
	while clock.getTime()<=20.0:
		print clock.getTime()
		if clock.getTime()<3.0:
			vline.draw()
			hline.draw()
			window.flip()
		elif event.getKeys("space"):
			print "Fuck"
			break
		elif clock.getTime()>=5.0 and clock.getTime()<=10.0:
			Instructions1.draw()
			window.flip()
		elif clock.getTime()>=3.0 and clock.getTime()<=5.0:
			if count==0:
				ring1=lettertext(letterrandomizer(),letterrandomizer(),letterrandomizer(),letterrandomizer(),letterrandomizer(),letterrandomizer(),letterrandomizer(),letterrandomizer(),1.0,1.0)
				#lettertext("H","G","F","E","D","C","B","A",2.0,3.0)
				#lettertext("A","B","C","D","E","F","G","H",3.0,5.0)
				ring2=lettertext("A","B","C","D","E","F","G","H",2.0,5.0)
				ring1perm=ring1
				ring2perm=ring2

				window.flip()
				count=1
			elif count>=1:
				count=1 
		elif clock.getTime()>=10.0 and clock.getTime()<20.0:
			#if ring2perm==lettertext("A","B","C","D","E","F","G","H",2.0,5.0):
				#print "Kill"
			ring1()
			ring2()
			window.flip()

				

			#if clock.getTime()>=20.0 and clock.getTime()<=30.0:
			#	clock.getTime()=11.0
	#		elif event.getKeys('space'):










window.flip()
clock.reset

letterfunc()