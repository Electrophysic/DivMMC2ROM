# -*- coding: utf-8 -*-

TRDOS=1<<0
BASIC=1<<1
EXIT=1<<2
BIT_E3h=1<<3
BIT_E7h=1<<4
BIT_EBh=1<<5
hex77=1<<6
IOGE=1<<7

romdata=[]
for addr in range (65536):
        #данные на селектор точек входа divmmc
        dataout=0xff^(IOGE)
                  
        #точки входа
        if ((addr==0)|(addr==0x8)|(addr==0x38)|(addr==0x66)|(addr==0x4c6)|(addr==0x562)):
            dataout^=BASIC#включение по окончании выборки первой команды
        #точка входа TRDOS
        if ((addr&0xff00)==0x3d00):
            dataout^=TRDOS#включение в том же такте
        #точка выхода
        if ((addr&0xfff8)==0x1ff8):         
            dataout^=EXIT #выключение
        
        #порты
        addr8=addr&0xff
        if (addr8==0xe3):
            dataout^=BIT_E3h
            dataout|=IOGE
        if (addr8==0xe7):
            dataout^=BIT_E7h
            dataout|=IOGE           
        if ((addr8==0xEB)|((addr&0x00ff)==0x57)):
            dataout^=BIT_EBh
            dataout|=IOGE
        if ((addr&0x00ff)==0x77):
            dataout^=hex77
            dataout|=IOGE          
        
        romdata.append(dataout)

f=open("AdrDivZ2card.bin","wb")  
f.write(bytes(romdata))
f.close()
exit(0)
