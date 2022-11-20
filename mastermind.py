import tkinter
import random

class Mastermind:

    # computer will be choosing colours from this list
    comp = []
    # reference list of colours
    colours = ["white", "black", "green", "blue", "yellow", "red", "brown", "purple", "orange"]
   
    zoznam = [None, None, None, None, None] # my guessed colour list

    def __init__(self):
        self.canvas = tkinter.Canvas(width=410, height=600, bg='#fffad0')
        self.canvas.pack()

        self.farba = None
        self.tries = 0
          
        self.game_start()

        self.canvas.bind('<ButtonPress>', self.guess)
        self.canvas.bind('<Motion>', self.colour_move)

        tkinter.mainloop()

    def game_start(self):     
        
        self.help()

        # generate random list, first 5 colours are picked for me to be guessed
        self.comp.clear()
        for i in range(9):
            self.comp.append(self.colours[i])
      
        f = random.shuffle(self.comp)   
        for i in range(4):
            self.comp.pop()
        #print(self.comp)
        
        self.canvas.create_rectangle(3, 3, 410, 600, width = 2, outline = 'orange')

        # draw computer colours hidden behind a question mark
        x1, y1 = 30, 20
        for i in range(5):
            self.canvas.create_oval(x1, y1, x1+40, y1+40, width=1)
            self.canvas.create_text(x1+20, y1+20, text='?', font='Aerial 12')
            x1 += 50
        self.canvas.create_line(10, 70, 400, 70)

        # draw 5 circles for 1st round
        x5, y5 = 30, 80
        for i in range(5):
            self.canvas.create_oval(x5, y5, x5+40, y5+40, width=1)
            x5 += 50

        # random colour pick suggestion for 1st round
        self.canvas.create_rectangle(290, 85, 370, 115, fill='white', tag='rnd')
        self.canvas.create_text(330, 100, font='Arial 10', text='random', tag='rnd')

        # draw 9 colours we will be choosing from
        colours = ["white", "black", "green", "blue", "yellow", "red", "brown", "purple", "orange"]
        x9, y9 = 20, 550
        self.canvas.create_line(x9-10, y9-10, x9+380, y9-10)
        self.canvas.create_line(x9-10, y9+40, x9+380, y9+40)
        for i in range(9):
            self.canvas.create_oval(x9, y9, x9+30, y9+30, fill=colours[i])
            x9 += 30

        # ok button
        self.canvas.create_oval(x9+30, y9, x9+60, y9+30, fill='black', tag='OK')
        self.canvas.create_text(x9+45, y9+15, text='OK', fill='white', tag='OK')

        # help button
        self.canvas.create_oval(370, y9, 400, y9+30, fill='DimGray', tag='help')
        self.canvas.create_text(x9+95, y9+15, text='help', fill='white', tag='help')

        # start a new game button
        self.canvas.create_oval(370, 55, 400, 85, fill='LightGoldenRodYellow', tag='new')
        self.canvas.create_text(385, 69, text='new', fill='black', tag='new')


    def help(self): # getting help on how to play the game
        xa, ya, da = 205, 250, 25
        self.canvas.create_text(xa,ya, text='- PLAYING THE GAME -', font="Arial 11", tag='helping')
        ya += da
        self.canvas.create_text(xa,ya, text='please pick a colour from bellow', font="Arial 11", tag='helping')
        ya += da
        self.canvas.create_text(xa,ya, text='then click on any of the 5 circles above to insert it', font="Arial 11", tag='helping')
        ya += da
        self.canvas.create_text(xa,ya, text='and confirm with OK button once all 5 colours are selected', font="Arial 11", tag='helping')
        ya += da
        self.canvas.create_text(xa,ya, text='- ROUND EVALUATION -', font="Arial 11", tag='helping')
        ya += da
        self.canvas.create_text(xa,ya, text='black circle shows the number of colours in a correct position', font="Arial 11", tag='helping')
        ya += da
        self.canvas.create_text(xa,ya, text='white circle shows the number of colours in a wrong position', font="Arial 11", tag='helping')
        ya += da
        self.canvas.create_text(xa,ya, text='- REVEALING HIDDEN COLOURS -', font="Arial 11", tag='helping')
        ya += da
        self.canvas.create_text(xa,ya, text='you can click on any of the top 5 circles', font="Arial 11", tag='helping')
        ya += da
        self.canvas.create_text(xa,ya, text='marked with a question mark to reveal the hidden colours', font="Arial 11", tag='helping')
        ya += da
        self.canvas.create_text(xa,ya, text='at any point while playing the game', font="Arial 11", tag='helping')
        ya += da
        self.canvas.create_text(xa,ya, text='--- good luck and have fun ! ---', font="Arial 11", tag='helping')
        ya += da


    def colour_move(self, event): 
        x, y = event.x, event.y
        self.canvas.delete('moving_colour_cirle')
        self.canvas.delete('mark_circle')
        self.canvas.delete('OK_highlight')
        self.canvas.delete('rnd2')
        
        if self.tries < 9:

            if 70 < y < 540:    # colour sticks to the mouse until clicking the 'guessing' circles
                self.canvas.create_oval(x-10, y-10, x+10, y+10, fill=self.farba, width=0, tag='moving_colour_cirle')
                
                for b in range(9):  # mark with colour outline while hovering over circle
                    if self.tries == b:
                        for i in range(5):  
                            if 30+50*i < x < 70+50*i and 80+50*b < y < 120+50*b:
                                self.canvas.create_oval(30+50*i,80+50*b, 70+50*i, 120+50*b, outline=self.farba, width=2, tag = 'mark_circle')

            for i in range(5):      # mark with colour outline while hovering over top circles for solution
                if 30+50*i < x < 70+50*i and 20 < y < 60: 
                    self.canvas.create_oval(30+50*i, 20, 70+50*i, 60, width=2, outline = 'red', tag = 'mark_circle')
                    self.canvas.create_text(340, 40, text='SHOW SOLUTION', font='Arial 11', fill = 'red', tag = 'mark_circle')

            # hovering over ok button
            if 320 < x < 350 and 550 < y < 580: 
                self.canvas.create_oval(320, 550, 350, 580, fill='blue', tag='OK_highlight')
                self.canvas.create_text(335, 565, text='OK', fill='white', tag='OK_highlight')
                self.canvas.create_text(360, 530, text='confirm', font='Arial 11', fill = 'blue', tag = 'mark_circle')

            # hovering over selection colours
            x9, y9 = 20, 550
            self.canvas.delete('bottom')
            for i in range(9):
                if 20+30*i < x < 50+30*i and 550 < y < 580:
                    self.canvas.create_line(20+30*i, 582, 50+30*i, 582, width=2, fill=self.colours[i], tag='bottom')

        # hovering over new button
        if 370 < x < 400 and 55 < y < 85:
            self.canvas.create_oval(370, 55, 400, 85, fill='blue', tag='OK_highlight')
            self.canvas.create_text(385, 69, text='new', fill='white', tag='OK_highlight')
            self.canvas.create_text(340, 40, text='start a new game', font='Arial 11', fill = 'blue', tag = 'mark_circle')
         
        # hovering over help button
        if self.tries < 3:
            if 370 < x < 400 and 550 < y < 580:
                self.canvas.create_oval(370, 550, 400, 580, fill='blue', tag='OK_highlight')
                self.canvas.create_text(385, 565, text='help', fill='white', tag='OK_highlight')
                self.canvas.create_text(360, 530, text='game rules', font='Arial 11', fill = 'blue', tag = 'mark_circle')

        # random colour pick suggestion for 1st round
        if self.tries < 1:
            if 290 < x < 370 and 85 < y < 115:
                self.canvas.create_rectangle(290, 85, 370, 115, fill='blue', tag='rnd2')
                self.canvas.create_text(330, 100, font='Arial 10', fill='white', text='random', tag='rnd2')
                self.canvas.create_text(340, 20, text='generate random', font='Arial 11', fill = 'blue', tag = 'mark_circle')
                self.canvas.create_text(340, 40, text='colours', font='Arial 11', fill = 'blue', tag = 'mark_circle')


    def guess(self, event):
        
        x, y = event.x, event.y
         
        # reveal colours at anytime during the game
        for i in range(0,5):
            if 30+50*i < x < 70+50*i and 30 < y < 70:
                self.canvas.delete('end')
                # show correct colours on top
                x1, y1 = 30, 20
                for i in range(5):
                    self.canvas.create_oval(x1, y1, x1+40, y1+40, width=1, fill=self.comp[i])
                    x1 += 50
                if self.comp != self.zoznam:
                    self.canvas.create_text(340, 25, text='--- Game Over ---', font='Arial 11', tag = 'end')
                    self.canvas.create_line(10, 10, 400, 10)
                self.tries = 9

        # start a new game
        if 370 < x < 400 and 55 < y < 85:
            self.canvas.delete('all')
            self.tries = 0
            self.game_start()

        # draw 5 circles for next round
        if self.zoznam != self.comp:
            x5, y5 = 30, 80
            for i in range(5):
                self.canvas.create_oval(x5, y5, x5+40, y5+40, width=1)
                x5 += 50

        if self.tries < 9:

            if self.tries < 1:  # random colours
                if 290 < x < 370 and 85 < y < 115:
                    self.zoznam.clear()
                    for i in range(9):
                        self.zoznam.append(self.colours[i])
                    f = random.shuffle(self.zoznam)   
                    for i in range(4):
                        self.zoznam.pop()
                    
                    x5, y5 = 30, 80       # show randomly generated colours in circles
                    for i in range(5):
                        self.canvas.create_oval(x5, y5, x5+40, y5+40, width=1, fill=self.zoznam[i])
                        x5 += 50

            # player picks a colour from 9 circles at bottom
            x9 = 20
            y9 = 550
            d9 = 30

            for t in range(9):
                if x9+d9*t < x < x9+d9*(t+1) and y9 < y < y9+d9:  
                    self.farba = self.colours[t] 
             
            # mark a circle with a wider border when selected
            x9 = 20
            y9 = 550
            d9 = 30 # diameter
            self.canvas.delete('mark_bottom_circle')
            for t in range(1, 10):  # 9 colours to choose from
                if x9+d9*t-d9 < x < x9+t*d9 and y9 < y < y9+d9:
                    self.canvas.create_oval(x9+30*t-30, y9, x9+30*t+30-30, y9+30, width=2, tag='mark_bottom_circle')
                if self.tries < 3:   # help button
                    if 370 < x < 400 and y9 < y < y+30:
                        self.canvas.create_oval(370, y9, 400, y9+30, width=2, tag='mark_circle')
                if 370 < x < 400 and 55 < y < 85:   # new game button
                    self.canvas.create_oval(370, 55, 400, 85, width=2, tag='mark_circle')

        # insert colours into circles
        for b in range(9):
            if self.tries == b:
                i = 80 + b*50
                for k in range(5):
                    if 30+50*k < x < 70+50*k and i < y < i+40:
                        if self.farba == None:
                            self.canvas.create_oval(30+50*k, i, 70+50*k, i+40, fill='#fffad0')
                            self.zoznam[k] = None
                        else:
                            self.canvas.create_oval(30+50*k, i, 70+50*k, i+40, fill=self.farba)
                            self.zoznam[k] = self.farba
                            self.farba = None
               
                self.canvas.delete('same_colour_warning')
                self.canvas.delete('not_enough_colour_warning')
        
        if self.tries < 9:
            if x9+10*d9 < x < x9+11*d9 and y9 < y < y9+d9:  # hitting OK button
            
                self.canvas.delete('same_colour_warning')
                self.canvas.delete('not_enough_colour_warning')
                # if player picks less than 5 colours
                if self.zoznam[0] == None or self.zoznam[1] == None or self.zoznam[2] == None or self.zoznam[3] == None or self.zoznam[4] == None:
                    self.canvas.create_text(210, 530, text='- please select 5 colours -', fill='red', font='Arial 11', tag='not_enough_colour_warning')
                    self.canvas.delete('same_colour_warning')
                
                # if player picks the same colour more than once
                elif self.zoznam.count(self.colours[0]) > 1 or self.zoznam.count(self.colours[1]) > 1 or self.zoznam.count(self.colours[2]) > 1 or self.zoznam.count(self.colours[3]) > 1 or self.zoznam.count(self.colours[4]) > 1 or self.zoznam.count(self.colours[5]) > 1 or self.zoznam.count(self.colours[6]) > 1 or self.zoznam.count(self.colours[7]) > 1 or self.zoznam.count(self.colours[8]) > 1:
                    self.canvas.create_text(210, 530, text='- please select 5 different colours -', fill='red', font='Arial 11', tag='same_colour_warning')
                    self.canvas.delete('not_enough_colour_warning')
                
                # go ahead and evaluate the round
                else:
                    self.tries += 1
                    self.canvas.delete('same_colour_warning')
                    self.canvas.delete('not_enough_colour_warning')
                    if self.comp != self.zoznam:
                    # count how many correct colours and positions we have guessed    
                        correct = 0     # correct colour in correct position
                        for i in range(5):
                            if self.zoznam[i] == self.comp[i]:
                                correct += 1      
                        col = 0         # correct colour in wrong position
                        if self.zoznam[0] == self.comp[1] or self.zoznam[0] == self.comp[2] or self.zoznam[0] == self.comp[3] or self.zoznam[0] == self.comp[4]:
                            col += 1
                        if self.zoznam[1] == self.comp[0] or self.zoznam[1] == self.comp[2] or self.zoznam[1] == self.comp[3] or self.zoznam[1] == self.comp[4]:
                            col += 1
                        if self.zoznam[2] == self.comp[0] or self.zoznam[2] == self.comp[1] or self.zoznam[2] == self.comp[3] or self.zoznam[2] == self.comp[4]:
                            col += 1
                        if self.zoznam[3] == self.comp[0] or self.zoznam[3] == self.comp[1] or self.zoznam[3] == self.comp[2] or self.zoznam[3] == self.comp[4]:
                            col += 1
                        if self.zoznam[4] == self.comp[0] or self.zoznam[4] == self.comp[1] or self.zoznam[4] == self.comp[2] or self.zoznam[4] == self.comp[3]:
                            col += 1
                        
                    # evaluate round
                        for i in range(9):
                            if self.tries == i:
                                y5 += 50*i - 50
                                self.canvas.create_oval(x5+25, y5+5, x5+55, y5+35, fill="black")
                                self.canvas.create_text(x5+40, y5+20, text=correct, fill="white", font='Arial 12')
                                self.canvas.create_oval(x5+65, y5+5, x5+95, y5+35, fill='white')
                                self.canvas.create_text(x5+80, y5+20, text=col, fill="black", font='Arial 12')
                        
                    # draw circles for next round
                        for j in range(9):
                            if self.tries == j:
                                x5 = 30
                                y5 = 80 + 50*j
                                for k in range(5):
                                    self.canvas.create_oval(x5, y5, x5+40, y5+40, width=1)
                                    x5 += 50

                        # clear list for a new round - we do this to see if we fill all circles /empty list/ with new values / colours
                        for j in range(5):
                            self.zoznam[j] = None 
                  
                    if self.comp == self.zoznam:  # if player gets all colours and their positions right
                        self.canvas.create_text(340, 25, text='! Congratulations !', font='Arial 11', tag = 'end')
                        self.tries = 9
                        
                        # show correct colours on top
                        x1, y1 = 30, 20
                        for i in range(5):
                            self.canvas.create_oval(x1, y1, x1+40, y1+40, width=1, fill=self.comp[i])
                            x1 += 50
                        self.canvas.create_line(10, 10, 400, 10)
            
                        x5, y5 = 30, 130
                        for i in range(5):
                            self.canvas.create_oval(x5, y5, x5+40, y5+40, width=1)
                            x5 += 50

                    if self.tries == 9 and self.comp != self.zoznam: # if player fails after 9 tries
                        self.canvas.create_text(340, 25, text='--- Game Over ---', font='Arial 11', tag = 'end')
                        self.canvas.create_line(10, 10, 400, 10)

                        # show correct colours on top
                        x1, y1 = 30, 20
                        for i in range(5):
                            self.canvas.create_oval(x1, y1, x1+40, y1+40, width=1, fill=self.comp[i])
                            x1 += 50
                        
                        x5, y5 = 30, 130
                        for i in range(5):
                            self.canvas.create_oval(x5, y5, x5+40, y5+40, width=1)
                            x5 += 50
    
        # getting help on how to play the game and remove text
        if self.tries < 3:
            self.canvas.delete('helping')
            self.help()  
        if self.tries == 3:  # remove the help button after 3 rounds as it is no longer needed
            self.canvas.delete('help')
        if 370 > x or x > 400 and y9 > y or y > y+30:   # remove help lines when clicking anywhere but the help button
            self.canvas.delete('helping')

        # remove random colour generator
        if self.tries == 1:
            self.canvas.delete('rnd')
            self.canvas.delete('rnd2')

Mastermind()