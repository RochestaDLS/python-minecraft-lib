from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#Илья ассистент
def LODKA(x,y,z):
#каркас    
   mc.setBlocks(x-5,y-2,z,x+5,y-2,z,5,2)
   mc.setBlocks(x-5,y-1,z+1,x+5,y-1,z+1,5,2)
   mc.setBlocks(x-5,y-1,z-1,x+5,y-1,z-1,5,2)
   mc.setBlock(x-6,y-1,z,5,2)
   mc.setBlock(x+6,y-1,z,5,2)
   mc.setBlocks(x-5,y+2,z+2,x+5,y,z+2,5,2)
   mc.setBlocks(x-5,y+2,z-2,x+5,y,z-2,5,2)
   mc.setBlocks(x-6,y,z-1,x-6,y+2,z-1,5,2)
   mc.setBlocks(x-6,y,z+1,x-6,y+2,z+1,5,2)
   mc.setBlocks(x+6,y,z+1,x+6,y+2,z+1,5,2)
   mc.setBlocks(x+6,y,z-1,x+6,y+2,z-1,5,2)
   mc.setBlocks(x-7,y,z,x-7,y+2,z,5,2)
   mc.setBlocks(x-6,y+1,z,x+6,y+1,z,5,2)
   mc.setBlocks(x-5,y+1,z-1,x+5,y+1,z-1,5,2)
   mc.setBlocks(x-5,y+1,z+1,x+5,y+1,z+1,5,2)
   mc.setBlock(x+6,y,z,5,2)
#щитки
   mc.setBlock(x-4,y+3,z+2,42)
   mc.setBlock(x-4,y+3,z-2,42)
   mc.setBlock(x-1,y+3,z+2,42)
   mc.setBlock(x-1,y+3,z-2,42)
   mc.setBlock(x+2,y+3,z+2,42)
   mc.setBlock(x+2,y+3,z-2,42)
   mc.setBlock(x+5,y+3,z+2,42)
   mc.setBlock(x+5,y+3,z-2,42)
#задняя часть
   mc.setBlock(x-7,y+2,z-1,5,2)
   mc.setBlock(x-7,y+2,z+1,5,2)
   mc.setBlock(x-6,y+3,z-1,85)
   mc.setBlock(x-6,y+3,z+1,85)
   mc.setBlocks(x-7,y+3,z+1,x-7,y+3,z-1,85)
#спуск в трюм
   mc.setBlock(x+4,y+1,z,96,9)
   mc.setBlock(x+4,y,z-1,5,2)
   mc.setBlocks(x+4,y,z,x+4,y-1,z,65,3)
#таран
   mc.setBlocks(x+7,y+1,z-1,x+7,y+2,z+1,41)
   mc.setBlock(x+7,y+2,z,5,2)
   mc.setBlock(x+7,y+3,z,41)
   mc.setBlocks(x+8,y+2,z,x+8,y+4,z,41)
   mc.setBlocks(x+9,y+3,z,x+9,y+4,z,41)
   mc.setBlock(x+10,y+4,z,41)
#мачта
   mc.setBlocks(x,y+2,z,x,y+14,z,85)
   mc.setBlocks(x+1,y+5,z-3,x+1,y+5,z+3,35,0)
   mc.setBlocks(x+1,y+14,z-3,x+1,y+14,z+3,35,0)
   mc.setBlocks(x+2,y+13,z-3,x+2,y+6,z+3,35,0)
   mc.setBlocks(x+3,y+12,z-2,x+3,y+7,z+2,35,0)
   mc.setBlocks(x+2,y+12,z-2,x+2,y+7,z+2,0)
   mc.setBlocks(x+3,y+8,z,x+3,y+11,z,35,14)
   mc.setBlocks(x+3,y+11,z-1,x+3,y+11,z+1,35,14)
#трюм
   mc.setBlocks(x+1,y,z-1,x+2,y,z-1,54,2)
   mc.setBlocks(x+1,y,z+1,x+2,y,z+1,54,3)
   mc.setBlocks(x-1,y,z-1,x-2,y,z-1,54,2)
   mc.setBlocks(x-1,y,z+1,x-2,y,z+1,54,3)
   mc.setBlocks(x-4,y-1,z,x-4,y,z,101)
   mc.setBlock(x-4,y,z-1,5,2)
   mc.setBlock(x-4,y,z+1,5,2)
def LODKA1(x,y,z):
#каркас    
    mc.setBlocks(x-5,y-2,z,x+5,y-2,z,5,2)
    mc.setBlocks(x-5,y-1,z+1,x+5,y-1,z+1,5,2)
    mc.setBlocks(x-5,y-1,z-1,x+5,y-1,z-1,5,2)
    mc.setBlock(x-6,y-1,z,5,2)
    mc.setBlock(x+6,y-1,z,5,2)
    mc.setBlocks(x-5,y+2,z+2,x+5,y,z+2,5,2)
    mc.setBlocks(x-5,y+2,z-2,x+5,y,z-2,5,2)
    mc.setBlocks(x-6,y,z-1,x-6,y+2,z-1,5,2)
    mc.setBlocks(x-6,y,z+1,x-6,y+2,z+1,5,2)
    mc.setBlocks(x+6,y,z+1,x+6,y+2,z+1,5,2)
    mc.setBlocks(x+6,y,z-1,x+6,y+2,z-1,5,2)
    mc.setBlocks(x-7,y,z,x-7,y+2,z,5,2)
    mc.setBlocks(x-6,y+1,z,x+6,y+1,z,5,2)
    mc.setBlocks(x-5,y+1,z-1,x+5,y+1,z-1,5,2)
    mc.setBlocks(x-5,y+1,z+1,x+5,y+1,z+1,5,2)
    mc.setBlock(x+6,y,z,5,2)
#щитки
    mc.setBlock(x-4,y+3,z+2,42)
    mc.setBlock(x-4,y+3,z-2,42)
    mc.setBlock(x-1,y+3,z+2,42)
    mc.setBlock(x-1,y+3,z-2,42)
    mc.setBlock(x+2,y+3,z+2,42)
    mc.setBlock(x+2,y+3,z-2,42)
    mc.setBlock(x+5,y+3,z+2,42)
    mc.setBlock(x+5,y+3,z-2,42)
#задняя часть
    mc.setBlock(x-7,y+2,z-1,5,2)
    mc.setBlock(x-7,y+2,z+1,5,2)
    mc.setBlock(x-6,y+3,z-1,85)
    mc.setBlock(x-6,y+3,z+1,85)
    mc.setBlocks(x-7,y+3,z+1,x-7,y+3,z-1,85)
#спуск в трюм
    mc.setBlock(x+4,y+1,z,96,9)
    mc.setBlock(x+4,y,z-1,5,2)
    mc.setBlocks(x+4,y,z,x+4,y-1,z,65,3)
#таран
    mc.setBlocks(x+7,y+1,z-1,x+7,y+2,z+1,41)
    mc.setBlock(x+7,y+2,z,5,2)
    mc.setBlock(x+7,y+3,z,41)
    mc.setBlocks(x+8,y+2,z,x+8,y+4,z,41)
    mc.setBlocks(x+9,y+3,z,x+9,y+4,z,41)
    mc.setBlock(x+10,y+4,z,41)
#мачта
    mc.setBlocks(x,y+2,z,x,y+14,z,85)
    mc.setBlocks(x+1,y+5,z-3,x+1,y+5,z+3,35,0)
    mc.setBlocks(x+1,y+14,z-3,x+1,y+14,z+3,35,0)
    mc.setBlocks(x+2,y+13,z-3,x+2,y+6,z+3,35,0)
    mc.setBlocks(x+3,y+12,z-2,x+3,y+7,z+2,35,0)
    mc.setBlocks(x+2,y+12,z-2,x+2,y+7,z+2,0)
    mc.setBlocks(x+3,y+8,z,x+3,y+11,z,35,14)
    mc.setBlocks(x+3,y+11,z-1,x+3,y+11,z+1,35,14)
#трюм
    mc.setBlocks(x+1,y,z-1,x+2,y,z-1,54,2)
    mc.setBlocks(x+1,y,z+1,x+2,y,z+1,54,3)
    mc.setBlocks(x-1,y,z-1,x-2,y,z-1,54,2)
    mc.setBlocks(x-1,y,z+1,x-2,y,z+1,54,3)
    mc.setBlocks(x-4,y-1,z,x-4,y,z,101)
    mc.setBlock(x-4,y,z-1,5,2)
    mc.setBlock(x-4,y,z+1,5,2)
    mc.setBlock(x,y,z-2,85)
    mc.setBlock(x,y,z+2,85)
    mc.setBlock(x-3,y,z-2,85)
    mc.setBlock(x-3,y,z+2,85)
    mc.setBlock(x+3,y,z-2,85)
    mc.setBlock(x+3,y,z+2,85)
#Тимофей
def setShip1(x,y,z):
    #дно
    mc.setBlocks(x-9,y,z-3,x+9,y,z+3,5,5)
    #борты
    mc.setBlocks(x-10,y+1,z-4,x+9,y+1,z-4,5,5)
    mc.setBlocks(x+10,y+1,z-3,x+10,y+1,z+3,5,5)
    mc.setBlocks(x-10,y+1,z+4,x+9,y+1,z+4,5,5)
    mc.setBlocks(x-10,y+1,z-4,x-10,y+1,z+4,5,5)
    #Парус
    mc.setBlocks(x+2,y+9,z-4,x+2,y+5,z+4,35)
    #мачта
    mc.setBlocks(x+1,y+10,z,x+1,y,z,162,1)
    mc.setBlocks(x+1,y+9,z-4,x+1,y+9,z+4,162,1)
    #рубка
    mc.setBlocks(x-10,y+3,z-4,x-7,y+1,z+4,5,5)
    mc.setBlocks(x-10,y+1,z-4,x-10,y+1,z+4,0)
    #рубка/лестница
    mc.setBlocks(x-4,y+1,z+3,x-4,y+1,z+4,5,5)
    mc.setBlocks(x-4,y+1,z-3,x-4,y+1,z-4,5,5)
    mc.setBlocks(x-5,y+1,z+3,x-5,y+2,z+4,5,5)
    mc.setBlocks(x-5,y+1,z-3,x-5,y+2,z-4,5,5)
    mc.setBlocks(x-6,y+1,z+3,x-6,y+3,z+4,5,5)
    mc.setBlocks(x-6,y+1,z-3,x-6,y+3,z-4,5,5)
    #рубка/борты
    mc.setBlocks(x-6,y+4,z-4,x-10,y+4,z-4,5,5)
    mc.setBlocks(x-6,y+4,z+4,x-10,y+4,z+4,5,5)
    mc.setBlocks(x-10,y+4,z-3,x-10,y+4,z+3,5,5)
    #рубка/штурвал
    mc.setBlocks(x-7,y+4,z,x-7,y+4,z,85)
    mc.setBlocks(x-7,y+5,z,x-7,y+5,z,5,3)
#Никита
def setShip2(x,y,z):
   n = 10
   m = 35,8
   mc.setBlocks(x+2,y-1,z+4,x-2,y-1,z-4-n,5,5)
   mc.setBlocks(x+3,y,z+4,x-3,y,z-4-n,5,5)
   mc.setBlocks(x+3,y+1,z+5,x-3,y+1,z-5-n,5,5)
   mc.setBlocks(x+3,y+2,z+5,x-3,y+2,z-6-n,5,5)
   mc.setBlocks(x+3,y+3,z+6,x-3,y+3,z-7-n,5,5)
   mc.setBlocks(x+3,y+4,z+6,x-3,y+4,z-8-n,5,5)
   mc.setBlocks(x,y+4,z-7,x,y+4,z-10-n,5,5)
   mc.setBlocks(x+2,y+4,z+5,x-2,y+4,z-7-n,0)
   mc.setBlocks(x+2,y+3,z+5,x-2,y+3,z-5-n,0)
   mc.setBlocks(x+4,y+3,z+6,x-4,y+4,z-4-n,0)
   mc.setBlocks(x-3,y+3,z+2,x+3,y+5,z+6,5,5)
   mc.setBlocks(x-2,y+3,z+1,x+2,y+4,z+5,0)
   mc.setBlocks(x-2,y+4,z+6,x+2,y+4,z+6,102)
   mc.setBlocks(x+2,y+4,z+2,x-1,y+3,z+2,5,5)
   mc.setBlocks(x-2,y+3,z+2,x-2,y+3,z+2,183)
   mc.setBlocks(x+4,y+3,z+1,x+4,y+3,z-4-n,190)
   mc.setBlocks(x-4,y+3,z+1,x-4,y+3,z-4-n,190)
   mc.setBlocks(x-3,y+4,z-4-n,x-3,y+4,z-7-n,190)
   mc.setBlocks(x+3,y+4,z-4-n,x+3,y+4,z-7-n,190)
   mc.setBlocks(x+2,y+1,z+4,x-2,y+1,z-4-n,0)
   mc.setBlocks(x+2,y,z+3,x-2,y,z-3-n,0)
   mc.setBlocks(x+4,y+2,z+1,x-4,y+2,z-14,5,5)
   mc.setBlocks(x+4,y+1,z-13,x+4,y+1,z,5,5)
   mc.setBlocks(x-4,y+1,z-13,x-4,y+1,z,5,5)
   mc.setBlocks(x+3,y+3,z-14,x+3,y+3,z-14,190)
   mc.setBlocks(x-3,y+3,z-14,x-3,y+3,z-14,190)
   mc.setBlocks(x+3,y+3,z-14,x+3,y+4,z-14,190)
   mc.setBlocks(x,y+3,z-4,x,y+20,z-4,5,5)
   mc.setBlocks(x+5,y+17,z-5,x-5,y+17,z-5,5,5)
   mc.setBlocks(x+4,y+8,z-5,x-4,y+8,z-5,5,5)
   mc.setBlocks(x,y+3,z-12,x,y+13,z-12,5,5)
   mc.setBlocks(x-3,y+6,z-12,x+3,y+6,z-12,5,5)
   mc.setBlocks(x-4,y+11,z-13,x+4,y+11,z-13,5,5)
   mc.setBlocks(x-5,y+15,z-6,x+5,y+17,z-6,m)
   mc.setBlocks(x-4,y+11,z-7,x+4,y+14,z-7,m)
   mc.setBlocks(x-3,y+8,z-6,x+3,y+10,z-6,m)
   mc.setBlocks(x-4,y+8,z-14,x+4,y+10,z-14,m)
   mc.setBlocks(x-3,y+6,z-13,x+3,y+7,z-13,m)
   mc.setBlocks(x+3,y+3,z-17,x+3,y+5,z-18,0)
   mc.setBlocks(x-3,y+3,z-17,x-3,y+5,z-18,0)
   mc.setBlocks(x+2,y+4,z-18,x+2,y+5,z-18,0)
   mc.setBlocks(x-2,y+4,z-18,x-2,y+5,z-18,0)
   mc.setBlocks(x+2,y+4,z-17,x+2,y+4,z-17,5,5)
   mc.setBlocks(x-2,y+4,z-17,x-2,y+4,z-17,5,5)
   mc.setBlocks(x,y+5,z-20,x,y+5,z-22,5,5)
   mc.setBlocks(x,y+6,z+3,x,y+6,z+3,192)
   mc.setBlocks(x,y+7,z+3,x,y+7,z+3,96)
   mc.setBlocks(x+3,y+6,z+2,x+3,y+6,z+6,190)
   mc.setBlocks(x+3,y+6,z+6,x-3,y+6,z+6,190)
   mc.setBlocks(x-3,y+6,z+2,x-3,y+6,z+6,190)
   mc.setBlocks(x+1,y,z+1,x+1,y,z+1,5,5)
   mc.setBlocks(x,y,z+1,x,y+2,z+1,5,5)
   mc.setBlocks(x+2,y,z+3,x+1,y,z+3,54)
   mc.setBlocks(x-2,y,z+3,x-1,y,z+3,54)
   mc.setBlocks(x-2,y,z-11,x-1,y,z-2,171,14)
   mc.setBlocks(x-1,y,z-11,x-1,y,z-2,171)
   mc.setBlocks(x-3,y+1,z-7,x-3,y+1,z-2,50)
   mc.setBlocks(x+3,y+1,z-7,x+3,y+1,z-7,50)
   mc.setBlocks(x+1,y+3,z+4,x+0,y+3,z+4,171,14)
   mc.setBlocks(x+1,y+3,z+5,x+0,y+3,z+5,171)
   mc.setBlocks(x-1,y+3,z+5,x-2,y+3,z+5,54)
   mc.setBlocks(x,y+2,z+1,x+3,y+2,z+1,0)
   mc.setBlocks(x+1,y+3,z-1,x+2,y+3,z-1,5,5)
   mc.setBlocks(x+1,y+4,z,x+2,y+4,z,5,5)
   mc.setBlocks(x+1,y+5,z+1,x+2,y+5,z+1,5,5)
   mc.setBlocks(x+2,y+3,z+5,x+2,y+3,z+5,47)
#slimeballwe
def SetShip3(x,y,z):
   mc.setBlocks(x+7,y-1,z,x+14,y-1,z+15,8)
   mc.setBlocks(x+8,y,z+1,x+13,y+3,z+14,5)
   mc.setBlocks(x+9,y+1,z+2,x+12,y+2,z+13,0)
   mc.setBlocks(x+9,y+1,z,x+12,y+3,z,5)
   mc.setBlocks(x+9,y+1,z+15,x+12,y+3,z+15 ,5)
   mc.setBlocks(x+10,y+2,z-1,x+11,y+3,z+16 ,5)
   mc.setBlocks(x+10,y+4,z-5,x+11,y+4,z+20 ,5)
   mc.setBlocks(x+10,y+4,z,x+12,y+4,z+15 ,0)
   mc.setBlocks(x+10,y+4,z+3,x+11,y+11,z+4 ,5)
   mc.setBlocks(x+10,y+4,z+10,x+11,y+11,z+11 ,5)
   mc.setBlocks(x+7,y+12,z+3,x+15,y+12,z+4 ,5)
   mc.setBlocks(x+7,y+12,z+10,x+15,y+12,z+11 ,5)
   mc.setBlocks(x+7,y+11,z+2,x+15,y+11,z+2 ,35)
   mc.setBlocks(x+7,y+7,z+1,x+15,y+10,z+1 ,35)
   mc.setBlocks(x+7,y+6,z+2,x+15,y+6,z+2 ,35)
   mc.setBlocks(x+7,y+11,z+9,x+15,y+11,z+9,35)
   mc.setBlocks(x+7,y+7,z+8,x+15,y+10,z+8,35)
   mc.setBlocks(x+7,y+6,z+9,x+15,y+6,z+9,35)
   mc.setBlocks(x+10,y+3,z+5,x+11,y+3,z+7,0)
   mc.setBlocks(x+9,y+1,z+2,x+12,y+2,z+13,0)
   mc.setBlocks(x+10,y+2,z+7,x+11,y+2,z+7,5)
   mc.setBlocks(x+10,y+1,z+6,x+11,y+1,z+6,5)
   mc.setBlocks(x+9,y,z+1,x+9,y,z+14,0)
   mc.setBlocks(x+14,y,z+1,x+14,y,z+14,0)
#Антон
def setShip4(x,y,z):
    mc.setBlocks(x+10,y-1,z-10,x-10,y+20,z+10,0)
    mc.setBlocks(x+20,y-1,z-20,x-20,y-10,z+20,9)
    mc.setBlocks(x+20,y-1,z-20,x+20,y-10,z+20,1)
    mc.setBlocks(x-20,y-1,z-20,x-20,y-10,z+20,1)
    mc.setBlocks(x+20,y-1,z-20,x-20,y-10,z-20,1)
    mc.setBlocks(x+20,y-1,z+20,x-20,y-10,z+20,1)
    mc.setBlocks(x+20,y-10,z-20,x-20,y-10,z+20,1)
    mc.setBlock(x+11,y+1,z,5,3)
    mc.setBlocks(x+10,y+1,z+1,x+9,y+1,z+1,5,3)
    mc.setBlocks(x+10,y+1,z-1,x+9,y+1,z-1,5,3)
    mc.setBlocks(x+8,y+1,z+2,x+6,y+1,z+2,5,3)
    mc.setBlocks(x+8,y+1,z-2,x+6,y+1,z-2,5,3)
    mc.setBlocks(x+5,y+1,z+3,x+3,y+1,z+3,5,3)
    mc.setBlocks(x+5,y+1,z-3,x+3,y+1,z-3,5,3)
    mc.setBlocks(x+2,y+1,z+4,x,y+1,z+4,5,3)
    mc.setBlocks(x+2,y+1,z-4,x,y+1,z-4,5,3)
    mc.setBlocks(x-1,y+1,z-5,x-5,y+1,z-5,5,3)
    mc.setBlocks(x-1,y+1,z+5,x-5,y+1,z+5,5,3)
    mc.setBlocks(x-6,y+1,z-4,x-8,y+1,z-4,5,3)
    mc.setBlocks(x-6,y+1,z+4,x-8,y+1,z+4,5,3)
    mc.setBlocks(x-9,y+1,z-3,x-9,y+1,z-2,5,3)
    mc.setBlocks(x-9,y+1,z+3,x-9,y+1,z+2,5,3)
    mc.setBlocks(x-10,y+1,z+1,x-10,y+1,z-1,5,3)
    mc.setBlock(x-10,y,z,5,3)
    mc.setBlocks(x-9,y,z+1,x-9,y,z-1,5,3)
    mc.setBlocks(x-8,y,z+3,x-6,y,z+2,5,3)
    mc.setBlocks(x-8,y,z-3,x-6,y,z-2,5,3)
    mc.setBlocks(x-5,y,z+4,x-1,y,z+3,5,3)
    mc.setBlocks(x-5,y,z-4,x-1,y,z-3,5,3)
    mc.setBlocks(x,y,z+3,x+2,y,z+2,5,3)
    mc.setBlocks(x,y,z-3,x+2,y,z-2,5,3)
    mc.setBlocks(x+3,y,z+2,x+5,y,z+1,5,3)
    mc.setBlocks(x+3,y,z-2,x+5,y,z-1,5,3)
    mc.setBlocks(x+6,y,z+1,x+8,y,z-1,5,3)
    mc.setBlocks(x+9,y,z,x+10,y,z,5,3)
    mc.setBlocks(x+4,y-1,z,x+6,y-1,z,5,3)
    mc.setBlocks(x+3,y-1,z,x+3,y-1,z,5,3)
    mc.setBlocks(x,y-1,z-1,x+2,y-1,z+1,5,3)
    mc.setBlocks(x-1,y-1,z-2,x-5,y-1,z+2,5,3)
    mc.setBlocks(x-6,y-1,z-1,x-8,y-1,z+1,5,3)
    mc.setBlock(x+11,y+2,z,50)
    mc.setBlock(x-3,y+2,z-5,50)
    mc.setBlock(x-3,y+2,z+5,50)
    mc.setBlock(x-9,y+2,z-3,76)
    mc.setBlock(x-9,y+2,z+3,76)
    mc.setBlocks(x-1,y,z,x-1,y+10,z,192)
    mc.setBlocks(x-1,y+10,z-4,x-1,y+10,z+4,192)
    mc.setBlocks(x,y+10,z-4,x,y+10,z+4,35,11)
    mc.setBlocks(x,y+5,z-4,x,y+5,z+4,35,11)
    mc.setBlocks(x+1,y+6,z-4,x+1,y+9,z+4,35,11)
    mc.setBlock(x-6,y+1,z-3,58)
    mc.setBlock(x-7,y+1,z-3,61)
    mc.setBlock(x-8,y+1,z-3,116)
    mc.setBlock(x-6,y+1,z+3,130)
    mc.setBlock(x-7,y+1,z+3,54)
    mc.setBlock(x-8,y+1,z+3,54)
    mc.setBlocks(x-9,y+1,z-1,x-9,y+1,z+1,47)
def SetShip5(x,y,z):
   mc.setBlocks(x+7,y-1,z,x+14,y-1,z+15,8)
   mc.setBlocks(x+8,y,z+1,x+13,y+3,z+14,5)
   mc.setBlocks(x+9,y+1,z+2,x+12,y+2,z+13,0)
   mc.setBlocks(x+9,y+1,z,x+12,y+3,z,5)
   mc.setBlocks(x+9,y+1,z+15,x+12,y+3,z+15 ,5)
   mc.setBlocks(x+10,y+2,z-1,x+11,y+3,z+16 ,5)
   mc.setBlocks(x+10,y+4,z-5,x+11,y+4,z+20 ,5)
   mc.setBlocks(x+10,y+4,z,x+12,y+4,z+15 ,0)
   mc.setBlocks(x+10,y+4,z+3,x+11,y+11,z+4 ,5)
   mc.setBlocks(x+10,y+4,z+10,x+11,y+11,z+11 ,5)
   mc.setBlocks(x+6,y+12,z+3,x+15,y+12,z+4 ,5)
   mc.setBlocks(x+6,y+12,z+10,x+15,y+12,z+11 ,5)
   mc.setBlocks(x+6,y+11,z+2,x+15,y+11,z+2 ,35)
   mc.setBlocks(x+6,y+7,z+1,x+15,y+10,z+1 ,35)
   mc.setBlocks(x+6,y+6,z+2,x+15,y+6,z+2 ,35)
   mc.setBlocks(x+6,y+11,z+9,x+15,y+11,z+9,35)
   mc.setBlocks(x+6,y+7,z+8,x+15,y+10,z+8,35)
   mc.setBlocks(x+6,y+6,z+9,x+15,y+6,z+9,35)
   mc.setBlocks(x+10,y+3,z+5,x+11,y+3,z+7,0)
   mc.setBlocks(x+9,y+1,z+2,x+12,y+2,z+13,0)
   mc.setBlocks(x+10,y+2,z+7,x+11,y+2,z+7,5)
   mc.setBlocks(x+10,y+1,z+6,x+11,y+1,z+6,5)
   mc.setBlocks(x+8,y,z+1,x+8,y,z+14,0)
   mc.setBlocks(x+13,y,z+1,x+13,y,z+14,0)
   mc.setBlocks(x+7,y+2,z+4,x+6,y+2,z+4,1,6)
   mc.setBlocks(x+7,y+2,z+7,x+6,y+2,z+7,1,6)
   mc.setBlocks(x+7,y+2,z+10,x+6,y+2,z+10,1,6)
   mc.setBlocks(x+7,y+2,z+13,x+6,y+2,z+13,1,6)
   mc.setBlocks(x+14,y+2,z+4,x+15,y+2,z+4,1,6)
   mc.setBlocks(x+14,y+2,z+7,x+15,y+2,z+7,1,6)
   mc.setBlocks(x+14,y+2,z+10,x+15,y+2,z+10,1,6)
   mc.setBlocks(x+14,y+2,z+13,x+15,y+2,z+13,1,6)
   mc.setBlocks(x+8,y+2,z+4,x+8,y+2,z+4,126)
   mc.setBlocks(x+8,y+2,z+7,x+8,y+2,z+7,126)
   mc.setBlocks(x+8,y+2,z+10,x+8,y+2,z+10,126)
   mc.setBlocks(x+8,y+2,z+13,x+8,y+2,z+13,126)
   mc.setBlocks(x+13,y+2,z+4,x+13,y+2,z+4,126)
   mc.setBlocks(x+13,y+2,z+7,x+13,y+2,z+7,126)
   mc.setBlocks(x+13,y+2,z+10,x+13,y+2,z+10,126)
   mc.setBlocks(x+13,y+2,z+13,x+13,y+2,z+13,126)
   mc.setBlocks(x+10,y+2,z,x+11,y+2,z,169)
   mc.setBlocks(x+10,y+2,z+1,x+11,y+2,z+1,20)
   mc.setBlocks(x+10,y+2,z+15,x+11,y+2,z+14,20)
   mc.setBlocks(x+10,y+2,z+15,x+11,y+2,z+15,169)
   mc.setBlock(x+7,y+11,z+4,85)
   mc.setBlock(x+7,y+10,z+4,169)
   mc.setBlock(x+15,y+11,z+4,85)
   mc.setBlock(x+15,y+10,z+4,169)
   mc.setBlock(x+8,y+11,z+11,85)
   mc.setBlock(x+8,y+10,z+11,169)
   mc.setBlock(x+15,y+11,z+11,85)
   mc.setBlock(x+15,y+10,z+11,169)