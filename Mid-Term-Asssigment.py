class Star_Cinema:
    __hall_list = []
    def __init__(self) -> None:
        pass
    def entry_hall(self,hall):
        self.__hall_list.append(hall)
        



class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        super().__init__()
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []


    def entry_show(self,id,movie_name,time):
        __entry_tuple = (id,movie_name,time)
        self.__show_list.append(__entry_tuple)
        all_seats = [[0 for i in range(self.__cols)] for j in range(self.__rows)]
        __entry_seats = {id:all_seats}
        self.__seats.update(__entry_seats)

    def book_seats(self,show_id,seats_col,seats_row):
        if show_id in self.__seats:
            if (seats_col < 0 or seats_row < 0 )or (seats_col >= self.__cols or seats_row >= self.__rows):
               print(f'\nPLEASE ENTER CORRECT ROW AND COLUMN\n')
            else:
                if self.__seats[show_id][seats_row][seats_col]==0:
                    self.__seats[show_id][seats_row][seats_col] = 1
                    print(f'\nYOUR SEAT IS BOOKED ON SEAT: (ROW:{seats_row}, COLOUMN:{seats_col}) FOR SHOW:{show_id}\n')
                else:
                    print("\nTHIS SEAT HAS ALREADY BOOKED, PLEASE CHOOSE ANOTHER SEAT\n")
        else:
            print('\nTHIS SHOW IS NOT AVAILABLE IN THIS TIME\n')

    def view_show_list(self):
       for i,show in enumerate(self.__show_list):
           print(f'{i+1}:MOVIE NAME: {show[1]} SHOW ID:{show[0]} TIME: {show[2]}\n')
    def view_available_seats(self,show_id):
        if show_id in self.__seats:
            print(f'\nHERE IS YOUR AVAILABLE SEATS FOR HALL :{self.__hall_no}\n',)
            for i in range(self.__rows):
                for j in range(self.__cols):
                    if(self.__seats[show_id][i][j]!=1):
                        print(f'SEATS {i, j}')
            print(f'\nHERE IS THE MATRIX FORMAT OF SEATS FOR HALL : {self.__hall_no}\n')
            for i in range(self.__rows):
                print('[',end=' ')
                for j in range(self.__cols):
                        print(f' {self.__seats[show_id][i][j]} ',end=' ')       
                print(']\n')
        else:
            print('\nPLEASE ENTER CORRECT SHOW ID\n')


Star_Cinema_Hall = Star_Cinema()

Phitron_hall = Hall(5,5,5901)

Star_Cinema_Hall.entry_hall(Phitron_hall)


Phitron_hall.entry_show(13001,'Dear Comrade','Date:04/20/2024 Saturday Time : 10:00 AM - 6:00 PM')
Phitron_hall.entry_show(13002,'Asuran','Date:04/21/2024 Sunday Time : 11:00 AM - 5:00 PM')
Phitron_hall.entry_show(13003,'RRR','Date:04/22/2024 Monday Time : 9:00 AM - 8:00 PM')
Phitron_hall.entry_show(13004,'Arya','Date:04/23/2024 Tuesday Time : 8:00 AM - 4:00 PM')
Phitron_hall.entry_show(13005,'Nenokkadine','Date:04/24/2024 Wednesday Time : 9:00 AM - 7:00 PM')
Phitron_hall.entry_show(13006,'Vikram','Date:04/25/2024 Thursday Time : 11:00 AM - 8:00 PM')
Phitron_hall.entry_show(13007,'Bombay','Date:04/26/2024 Friday Time : 8:30 AM - 7:00 PM')
Phitron_hall.entry_show(13008,'Kgf','Date:04/27/2024 Saturday Time : 8:00 AM - 8:00 PM')
Phitron_hall.entry_show(13009,'Baahubali','Date:04/28/2024 Sunday Time : 10:30 AM - 5:00 PM')
Phitron_hall.entry_show(130010,'Pushpa','Date:04/29/2024 Monday Time : 9:00 AM - 7:30 PM')
Phitron_hall.entry_show(130011,'Eega','Date:04/30/2024 Tuesday Time : 12:00 AM - 9:00 PM')
while True:
    print('1. VIEW ALL SHOW')
    print('2. VIEW AVAILABLE SEATS')
    print('3. BOOK TICKET')
    print('4. EXIT')

    Option = int(input('ENTER OPTION:' ))

    if Option==1:
        Phitron_hall.view_show_list()
    elif Option==2:
        SH_ID = int(input('ENTER SHOW ID: '))
        Phitron_hall.view_available_seats(SH_ID)
    elif Option==3:
        SHOW_ID = int(input('ENTER SHOW ID: '))
        COLUMN  = int(input('ENTER COLUMN NO: '))
        ROW = int(input('ENTER ROW NO: '))
        Phitron_hall.book_seats(SHOW_ID,COLUMN,ROW)
    elif Option==4:
        break
    else:
        print('\nPLEASE ENTER A VALID OPTION FROM 1 TO 4\n')
        break
