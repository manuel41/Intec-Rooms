from datetime import date as date
import time
from RoomScraper import GetRooms

main_loop = True
rooms = GetRooms()

while(main_loop):
    selected_time = 0
    free_room = []
    time_loop = True

    while(time_loop):
        print('Desea buscar un aula a esta hora o una hora específica?')
        option = input('[1]A esta hora\n[2]A una hora especifica\nOpcion: ')
        if option == '1':
            t = time.localtime()
            selected_time = time.strftime("%H", t)
            time_loop = False
        elif option == '2':
            selected_time = input('Inserte la hora que desea: ')
            time_loop = False
        else:
            print('Opcion invalida, favor intente de nuevo')

    print(f'Hora seleccionada: {selected_time}')

    day_loop = True
    while(day_loop):
        day = input('Que dia desea?\n[1]Hoy\n[2]Lunes\n[3]Martes\n[4]Miercoles\n[5]Jueves\n[6]Viernes\n[7]Sabado\nOpcion: ')
        if day == '1':
            weekday = date.today().weekday()
            day_loop = False
        elif day == '2':
            weekday = 0
            day_loop = False
        elif day == '3':
            weekday = 1
            day_loop = False
        elif day == '4':
            weekday = 2
            day_loop = False
        elif day == '5':
            weekday = 3
            day_loop = False
        elif day == '6':
            weekday = 4
            day_loop = False
        elif day == '7':
            weekday = 5
            day_loop = False
        else:
            print('Opcion invalida, favor intente de nuevo')
    print(f'Dia seleccionado: {weekday}')

    for x in range(len(rooms)):
        if int(selected_time) not in rooms[x].monday and weekday == 0:
            free_room.append(rooms[x].name)
        if int(selected_time) not in rooms[x].tuesday and weekday == 1:
            free_room.append(rooms[x].name)
        if int(selected_time) not in rooms[x].wednesday and weekday == 2:
            free_room.append(rooms[x].name)
        if int(selected_time) not in rooms[x].thursday and weekday == 3:
            free_room.append(rooms[x].name)
        if int(selected_time) not in rooms[x].friday and weekday == 4:
            free_room.append(rooms[x].name)
        if int(selected_time) not in rooms[x].saturday and weekday == 5:
            free_room.append(rooms[x].name)

    free_room.sort()
    print(free_room)
    exit = input('\nDesea salir?\n[1]Si\n[2]No\nOpcion: ')

    if exit == '1':
        main_loop = False

for x in range(len(rooms)):
    if(rooms[x].name == 'GC211'):
        print(rooms[x].monday)
        break