print('Как вас зовут?')
name = input()
print ('Здравйвуйте,', name)
print('Сколько вам лет?')
A = input ()
print ('Ваш любимый цвет? (1 – красный, 2 – зеленый, 3 – синий)')
color = int (input())
print ('Ваша любимая музыка? (1 – классика, 2 – поп-музыка, 3 – рок)')
music = int (input())
print ("Ваше любимое время года? (1 – осень, 2 – зима, 3 – весна, 4 – лето")
time = int (input())
if (color == 2) and (music == 1 or music == 2) and (time == 2):
    print ('Мы с вами подружимся!')
else:
    print ('Мы с вами не подружимся!')