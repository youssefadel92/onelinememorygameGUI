
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import ctypes

    #################################################################
    #################################################################
while 1==1:
    click1 = 0
    click2 = 0
    # helper function to initialize globals
    ctypes.windll.user32.MessageBoxA(0, 'In this game, 10 characters are chosen. Each character is repeated twice. The characters are put in random order. Each player picks two numbers between 1 and 20. The two characters in these positions are shown and the rest are covered with their position number. If the two characters match, the player wins a point and these two characters are covered with * from now on. The screen is cleared and the remaining character positions are displayed for the next player. When all characters are covered with *, the game ends and the player with the biggest score wins.', "Welcome", 0)
    def new_game():
        ctypes.windll.user32.MessageBoxA(0, 'enter 10 charachters in the interpreter', "Welcome", 0)
        print 'Enter 10 Charachters'
        char=[]
        while 1==1:
            x=raw_input('enter charachter:')
            if x in char:
                print 'Enter an Unrepeated Charachter'
            elif x=='':
                print 'No Spaces allowed'
            else:
                char.append(str(x))
                char.append(str(x))
            if len(char)==20:
                print 'begin playing'
                print '--------------------------------------------------------'
                break

        global deck_cards, exposed, turns, state,score1,score2
        score1=0
        score2=0
        state = 0
        turns = 'user1'+'-'+'score:'+str(score1)
        deck_cards = char
        exposed = [False for i in range(20)]
        label.set_text("Turns = " + str(turns))
        random.shuffle(char)
        pass



    # define event handlers

    def mouseclick(pos):
        # add game state logic here
        ##############################
        global state, exposed, click1, click2, turns, deck_cards,score1,score2
        choice = int(pos[0] / 50)
        if deck_cards.count('*')==18:
            if turns=='user1'+'-'+'score:'+str(score1):
                score1=score1+1
            else:
                score2=score2+1
            if score1>score2:
                ctypes.windll.user32.MessageBoxA(0, 'Game ended and the winner is User1'+' '+'(User1:'+str(score1)+'-'+'User2:'+str(score2)+')', "Result", 0)
            elif score2>score1:
                ctypes.windll.user32.MessageBoxA(0, 'Game ended and the winner is User2'+' '+'(User1:'+str(score1)+'-'+'User2:'+str(score2)+')', "Result", 0)
            else:
                ctypes.windll.user32.MessageBoxA(0, 'Game ended and its tight'+' '+'(User1:'+str(score1)+'-'+'User2:'+str(score2)+')', "Result", 0)
            deck_cards[click1]='*'
            deck_cards[click2]='*'
        if state == 0:

            state = 1

            click1 = choice

            exposed[click1] = True

        elif state == 1:

            if not exposed[choice]:

                state = 2

                click2 = choice

                exposed[click2] = True
                if turns=='user1'+'-'+'score:'+str(score1):
                    turns='user2'+'-'+'score:'+str(score2)
                elif turns=='user2'+'-'+'score:'+str(score2):
                    turns='user1'+'-'+'score:'+str(score1)
                

        elif state == 2:
            if not exposed[choice]:

                if deck_cards[click1] == deck_cards[click2]:
                    deck_cards[click1]='*'
                    deck_cards[click2]='*'
                    if turns=='user1'+'-'+'score:'+str(score1):
                        score2=score2+1
                    elif turns=='user2'+'-'+'score:'+str(score2):
                        score1=score1+1
                    
                    pass

                else:

                    exposed[click1] = False

                    exposed[click2] = False

                click1 = choice

                exposed[click1] = True

                state = 1       

        label.set_text("Turns = " + str(turns))
        pass

        

                            

    # cards are logically 50x100 pixels in size    

    def draw(canvas):

        for i in range(20):

            if exposed[i]:

                canvas.draw_text(str(deck_cards[i]), (50*i+10, 60), 40, "Pink")

            else:

                canvas.draw_polygon([(50*i, 0), (50*i, 100), (50*i + 50, 0), (50*i + 50, 100)], 3, "White", "Grey")

        pass



    # create frame and add a button and labels

    frame = simplegui.create_frame("Memory", 1000, 100)

    frame.add_button("Reset", new_game, 150)

    label = frame.add_label("Turns = 0")

    new_game()

    # register event handlers

    frame.set_mouseclick_handler(mouseclick)

    frame.set_draw_handler(draw)


    
    # get things rolling

    frame.start()





    # Always remember to review the grading rubric
