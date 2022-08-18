ddrsm =open('ddr.sm')
piusm =open('piu.sm','w+')

SMLine =ddrsm.readline()



while(SMLine!=''):
    
    while(len(SMLine)==5):   
        piusm.write(SMLine[0:2]+'0'+SMLine[2:5])
        SMLine =ddrsm.readline()
    
    piusm.write(SMLine.replace('dance','pump'))
    SMLine =ddrsm.readline()


ddrsm.close()
piusm.close()
