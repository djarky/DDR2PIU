import random


ddrsm =open('piu.sm')
piusm =open('piufixed.sm','w+')

SMAntLine='00000\n'
note_index='01234'

def rand_index(s):
    l = list(s)
    random.shuffle(l)
    result = ''.join(l)
    print(result)
    return result

def pseudo_rand_step(s_step):
    s_step=s_step[0:5]
    r_step =list(s_step)
    i=0
    for note in s_step:
        r_step[int(note_index[i])] = s_step[i]
        i=i+1
    result = ''.join(r_step)
    return result+'\n'		


#main


SMLine =ddrsm.readline()

while(SMLine!=''):
    
    while(len(SMLine)==6):
        piusm.write(str(pseudo_rand_step(SMLine)))
        if (SMAntLine!='00000\n'):
            SMAntLine =SMLine

        SMLine =ddrsm.readline()
        
    
    piusm.write(SMLine)
    SMLine =ddrsm.readline()
    note_index=rand_index(note_index) 

ddrsm.close()
piusm.close()

