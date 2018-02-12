a1=[]
a2=[]
a3=[]
a4=[]
a5=[]
a6=[]
a7=[]
a8=[]
a9=[]
a10=[]
n=0
def cpu(list1,list2,n):
        z=n+1
        if list1[n]==list1[z]:
                z=z+1
        if n==z:
                z=z+1
        if n==20:
                n=0
        if z==20:
                z=0
        print n

        while list2[n]=='*':
                if n==18:
                        n=n-18
                n=n+1
                if n==z:
                        z=z+1
        while list2[z]=='*':
                if z==18:
                        z=z-18
                z=z+1
        if len(a1)==3:
                wow=[a1[1],a1[2]]
                a1.append('a')
                return wow
        elif len(a2)==3:
                wow=[a2[1],a2[2]]
                a2.append('a')
                return wow
        elif len(a3)==3:
                wow=[a3[1],a3[2]]
                a3.append('a')
                return wow
        elif len(a4)==3:
                wow=[a4[1],a4[2]]
                a4.append('a')
                return wow
        elif len(a5)==3:
                wow=[a5[1],a5[2]]
                a5.append('a')
                return wow
        elif len(a6)==3:
                wow=[a6[1],a6[2]]
                a6.append('a')
                return wow
        elif len(a7)==3:
                wow=[a7[1],a7[2]]
                a7.append('a')
                return wow
        elif len(a8)==3:
                wow=[a8[1],a8[2]]
                a8.append('a')
                return wow
        elif len(a9)==3:
                wow=[a9[1],a9[2]]
                a9.append('a')
                return wow
        elif len(a10)==3:
                wow=[a10[1],a10[2]]
                a10.append('a')
                return wow
######################################################333                
        if len(a1)==2 and list1[n]==a1[0]:
                if a1[1]==n:
                        pass
                else:
                        a1.append(n)
        elif len(a2)==2 and list1[n]==a2[0]:
                if a2[1]==n:
                        pass
                else:
                        a2.append(n)
        elif len(a3)==2 and list1[n]==a3[0]:
                if a3[1]==n:
                        pass
                else:
                        a3.append(n)
        elif len(a4)==2 and list1[n]==a4[0]:
                if a4[1]==n:
                        pass
                else:
                        a4.append(n)
        elif len(a5)==2 and list1[n]==a5[0]:
                if a5[1]==n:
                        pass
                else:
                        a5.append(n)
        elif len(a6)==2 and list1[n]==a6[0]:
                if a6[1]==n:
                        pass
                else:
                        a6.append(n)
        elif len(a7)==2 and list1[n]==a7[0]:
                if a7[1]==n:
                        pass
                else:
                        a7.append(n)
        elif len(a8)==2 and list1[n]==a8[0]:
                if a8[1]==n:
                        pass
                else:
                        a8.append(n)
        elif len(a9)==2 and list1[n]==a9[0]:
                if a9[1]==n:
                        pass
                else:
                        a9.append(n)
        elif len(a10)==2 and list1[n]==a10[0]:
                if a10[1]==n:
                        pass
                else:
                        a10.append(n)
        else:
                if len(a1)==0:
                        a1.append(list1[n])
                        a1.append(n)
                elif len(a2)==0:
                        a2.append(list1[n])
                        a2.append(n)
                elif len(a3)==0:
                        a3.append(list1[n])
                        a3.append(n)
                elif len(a4)==0:
                        a4.append(list1[n])
                        a4.append(n)
                elif len(a5)==0:
                        a5.append(list1[n])
                        a5.append(n)
                elif len(a6)==0:
                        a6.append(list1[n])
                        a6.append(n)
                elif len(a7)==0:
                        a7.append(list1[n])
                        a7.append(n)
                elif len(a8)==0:
                        a8.append(list1[n])
                        a8.append(n)
                elif len(a9)==0:
                        a9.append(list1[n])
                        a9.append(n)
                elif len(a10)==0:
                        a10.append(list1[n])
                        a10.append(n)
#444444444444444444444444444444444444444444444444444444                        
        if len(a1)==2 and list1[z]==a1[0]:
                if a1[1]==z:
                        pass
                else:
                        a1.append(z)
        elif len(a2)==2 and list1[z]==a2[0]:
                if a2[1]==z:
                        pass
                else:
                        a2.append(z)
        elif len(a3)==2 and list1[z]==a3[0]:
                if a3[1]==z:
                        pass
                else:
                        a3.append(z)
        elif len(a4)==2 and list1[z]==a4[0]:
                if a4[1]==z:
                        pass
                else:
                        a4.append(z)
        elif len(a5)==2 and list1[z]==a5[0]:
                if a5[1]==z:
                        pass
                else:
                        a5.append(z)
        elif len(a6)==2 and list1[z]==a6[0]:
                if a6[1]==z:
                        pass
                else:
                        a6.append(z)
        elif len(a7)==2 and list1[z]==a7[0]:
                if a7[1]==z:
                        pass
                else:
                        a7.append(z)
        elif len(a8)==2 and list1[z]==a8[0]:
                if a8[1]==z:
                        pass
                else:
                        a8.append(z)
        elif len(a9)==2 and list1[z]==a9[0]:
                if a9[1]==z:
                        pass
                else:
                        a9.append(z)
        elif len(a10)==2 and list1[z]==a10[0]:
                if a10[1]==z:
                        pass
                else:
                        a10.append(z)
        else:
                if len(a1)==0:
                        a1.append(list1[z])
                        a1.append(z)
                elif len(a2)==0:
                        a2.append(list1[z])
                        a2.append(z)
                elif len(a3)==0:
                        a3.append(list1[z])
                        a3.append(z)
                elif len(a4)==0:
                        a4.append(list1[z])
                        a4.append(z)
                elif len(a5)==0:
                        a5.append(list1[z])
                        a5.append(z)
                elif len(a6)==0:
                        a6.append(list1[z])
                        a6.append(z)
                elif len(a7)==0:
                        a7.append(list1[z])
                        a7.append(z)
                elif len(a8)==0:
                        a8.append(list1[z])
                        a8.append(z)
                elif len(a9)==0:
                        a9.append(list1[z])
                        a9.append(z)
                elif len(a10)==0:
                        a10.append(list1[z])
                        a10.append(z)
        wow=[n,z]
        return wow

def shuffle(a):
        import random
        random.shuffle(a)
def test(l):
        for i in l:
            if i!='*':
                return False
        return True
while 10==10:
    print 'In this game, 10 characters are chosen. Each character is repeated twice. The characters are put in random order. Each  player picks two numbers between 1 and 20. The two characters in these positions are shown and the rest are covered with their position number. If the two characters match, the player wins a point and these two characters are covered with * from now on. The screen is cleared and the remaining character positions are displayed for the next player. When all  characters are covered with *, the game ends and the player with the biggest score wins.'
    print '-------------------------------------------------------'
    print 'select 1 for multiplayer and 2 for CPU'
    cho=input('Enter your choice:')
    if cho==1:
        print 'Enter 10 Charachters'
        char=[]
        score1=0
        score2=0
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
                break
        shuffle(char)
        print '-------------------------------------------------------'
        print 'charchters will be randomly sorted and hidden'
        print 'choose 2 diffrent numbers from this list'
        list1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        print list1
        while 1==1:
            if test(list1)==True:
                break
            print 'User1'+'-'+'score:'+str(score1)
            while 1==1:
                x=input('Choose 1st num:')
                y=input('Choose 2nd num:')
                if list1[x]=='*' or list1[y]=='*':
                    print 'these charachters are deleted'
                else:
                    break
            newlist=[]
            for i in range(0,20):
                if i==x:
                    newlist.append(str(char[i]))
                elif i==y:
                    newlist.append(str(char[i]))
                else:
                    newlist.append(list1[i])
            print newlist
            if newlist[x]==newlist[y]:
                newlist[x]='*'
                newlist[y]='*'
                char[x]='*'
                char[y]='*'
                list1=newlist
                score1=score1+1
                print 'screen is cleared'
            else:
                print 'screen is cleared'
            print '-------------------------------------------------------'
            if test(list1)==True:
                break
            print 'User2'+'-'+'score:'+str(score2)
            while 1==1:
                x=input('Choose 1st num:')
                y=input('Choose 2nd num:')
                if list1[x]=='*' or list1[y]=='*':
                    print 'these charachters are deleted'
                else:
                    break
            newlist1=[]
            for i in range(0,20):
                if i==x:
                    newlist1.append(str(char[i]))
                elif i==y:
                    newlist1.append(str(char[i]))
                else:
                    newlist1.append(list1[i])
            print newlist1
            if newlist1[x]==newlist1[y]:
                newlist1[x]='*'
                newlist1[y]='*'
                list1=newlist1
                score2=score2+1
                print 'screen is cleared'
            else:
                print 'screen is cleared'
            print '-------------------------------------------------------'
        if score1>score2:
            print 'Game ended and the winner is User1'+' '+'(User1:'+score1+'-'+'User2:'+score2+')'
        elif score2>score1:
            print 'Game ended and the winner is User2'+' '+'(User1:'+score1+'-'+'User2:'+score2+')'
        else:
            print 'Game ended and its tight'+' '+'(User1:'+score1+'-'+'User2:'+score2+')'

    elif cho==2:
        print 'Enter 10 Charachters'
        char=[]
        score1=0
        score2=0
        while 1==1:
            x=raw_input('enter charachter')
            if x in char:
                print 'Enter an Unrepeated Charachter'
            elif x=='':
                print 'No Spaces allowed'
            else:
                char.append(str(x))
                char.append(str(x))
            if len(char)==20:
                break
        shuffle(char)
        print '-------------------------------------------------------'
        print 'charchters will be randomly sorted and hidden'
        print 'choose 2 diffrent numbers from this list'
        list1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        print list1
        while 1==1:
            if test(list1)==True:
                break
            print 'CPU'+'-'+'score:'+str(score2)
           # while 1==1:
            chch=cpu(char,list1,n)
            x=chch[0]
            y=chch[1]
        #        if list1[x]=='*' or list1[y]=='*':
         #           print 'these charachters are deleted'

                #          n=n+1
           #     else:
            #        break
            newlist1=[]
            for i in range(0,20):
                if i==x:
                    newlist1.append(str(char[i]))
                elif i==y:
                    newlist1.append(str(char[i]))
                else:
                    newlist1.append(list1[i])
            print newlist1
            if newlist1[x]==newlist1[y]:
                newlist1[x]='*'
                newlist1[y]='*'
                list1=newlist1
                score2=score2+1
                print 'screen is cleared'
                if n==18:
                        n=n-18
                else:
                        n=n+1                
                
            else:
                print 'screen is cleared'
                if n==18:
                        n=n-18
                else:
                        n=n+1
            print '-------------------------------------------------------'
            if test(list1)==True:
                break
            print 'User1'+'-'+'score:'+str(score1)
            while 1==1:
                x=input('Choose 1st num:')
                y=input('Choose 2nd num:')
                if list1[x]=='*' or list1[y]=='*':
                    print 'these charachters are deleted'
                else:
                    break
            newlist1=[]
            for i in range(0,20):
                if i==x:
                    newlist1.append(str(char[i]))
                elif i==y:
                    newlist1.append(str(char[i]))
                else:
                    newlist1.append(list1[i])
            print newlist1
            if newlist1[x]==newlist1[y]:
                newlist1[x]='*'
                newlist1[y]='*'
                list1=newlist1
                score1=score1+1
                print 'screen is cleared'
            else:
                print 'screen is cleared'
            print '-------------------------------------------------------'
        if score1>score2:
            print 'Game ended and the winner is User1'+' '+'(User1:'+str(score1)+'-'+'CPU:'+str(score2)+')'
        elif score2>score1:
            print 'Game ended and the winner is CPU'+' '+'(User1:'+str(score1)+'-'+'CPU:'+str(score2)+')'
        else:
            print 'Game ended and its tight'+' '+'(User1:'+str(score1)+'-'+'CPU:'+str(score2)+')'
        print '-------------------------------------------------------'
        
