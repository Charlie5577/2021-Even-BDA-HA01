import random 
import sys
prize_list = ['Empty', 'Empty', 'Prize']       
choice_list = [1,2,3]                    
prob = []

choice_list = [x-1 for x in choice_list]
count = 0

try:
    for li in sys.stdin:
        prob = []
        for j in range(int(li)):
            for i in range(1,10000):
                random.shuffle(prize_list)             
                my_choice=random.choice(choice_list)      
                ml= prize_list.copy()    
                #del ml[my_choice]                      
                if ml[0]=="Empty":
                    del ml[0]
                else:
                    del ml[1]        
                if 'Prize'== ml[0]:                     
                    #Winning_track.append(1)
                    count+=1
                else:
                    #Winning_track.append(0) 
                    count+=0
            prob=(sum(count)/len(choice_list))

        print(prob)
except e:
    print(e)
