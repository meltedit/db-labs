import random
import Connect
from View import View
import datetime
tables = {
    1: 'tickets',
    2: 'trains',
    3: 'users',
}

class Model:
    # Method that checks valid of the number of table that user input and returns it
    @staticmethod
    def validTable():
        incorrect = True
        while incorrect:
            table = input('Choose table number => ')
            if table.isdigit():
                table = int(table)
                if table >= 1 and table <= 3:
                    incorrect = False
                else:
                    print('Incorrect input, try again.')
            else:
                print('Incorrect input, try again.')
        return table

            # Method that prints all table of DB

    @staticmethod
    def showAllTables():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        for table in range(1, 4):
            table_name = '''"''' + tables[table] + '''"'''
            print(tables[table])

            show = 'select * from public.{}'.format(table_name)

            print("SQL query => ", show)
            print('')
            cursor.execute(show)
            records = cursor.fetchall()
            obj = View(table, records)
            obj.show()
        cursor.close()
        Connect.closeConnect(connect)

    @staticmethod
    def showOneTable():
        View.list()
        connect = Connect.makeConnect()
        cursor = connect.cursor()

        table = Model.validTable()

        table_name = '''"''' + tables[table] + '''"'''
        print(tables[table])

        show = 'select * from public.{}'.format(table_name)

        print("SQL query => ", show)
        print('')
        cursor.execute(show)
        records = cursor.fetchall()
        obj = View(table, records)
        obj.show()
        cursor.close()
        Connect.closeConnect(connect)

    @staticmethod
    def delete():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        restart = True
        while restart:
            View.list()
            table = Model.validTable()

            if table == 1:
                scname = input('Delete ticket with ID = ')
                delete = 'delete from "tickets" where "t_id"= {}'.format(scname)
                restart = False
            elif table == 2:
                clname = input('Delete train with ID = ')
                delete = 'delete from "trains" where "tr_id"=  {}'.format(clname)
                restart = False
            elif table == 3:
                dsname = input('Delete user with ID = ')
                delete = 'delete from "users" where "p_id"= {}'.format(dsname)
                restart = False
            else:
                print('\nIncorrect input, try again.')
        print(tables[table])
        print("SQL query => ", delete)
        cursor.execute(delete)
        connect.commit()
        print('Data deleted successfully!')
        cursor.close()
        Connect.closeConnect(connect)

    @staticmethod
    def insert():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        restart = True
        while restart:
            View.list()
            table = Model.validTable()
            if table == 1: #tickets
                t_id = input("Ticket ID = ")
                num = input("Car number = ")
                seat = input("Seat number = ")
                car_type = input('Car type = ')
                while 1:
                    val = car_type
                    if val == 'first' or val == 'second':
                        break
                    else:
                        print("bad input")
                        car_type = input('Car type = ')

                p_id = input('Passanger ID = ')
                tr_id = input('Train ID = ')

                insert = 'insert into "tickets" ("t_id", "num", "seat", "type", "p_id", "tr_id") values ({}, {}, {}, \'{}\', {}, {})'.format(
                    t_id, num, seat, car_type, p_id,tr_id)

                restart = False
            elif table == 2: #trains
                tr_id = input('Train ID = ')
                departure_t = input('Departure Time (YYYY-MM-DD HH:MM) = ')
           
                arrival_t = input('Arrival Time (YYYY-MM-DD HH:MM) = ')
                
                while 1:
                    a = departure_t.split()[0].split('-')+departure_t.split()[1].split(':')
                    b = datetime.datetime(int(a[0]),int(a[1]),int(a[2]),int(a[3]),int(a[4]))
                    #print(b)
                    c = arrival_t.split()[0].split('-')+arrival_t.split()[1].split(':')
                    d = datetime.datetime(int(c[0]),int(c[1]),int(c[2]),int(c[3]),int(c[4]))
                    
                    #b = arrival_t.split()[0].split('-')+arrival_t.split()[1].split(':')
                    #b = datetime.datetime(int(a[0]),int(a[1]),int(a[2]),int(a[3]),int(a[4]))
                    
                    if b<d:
                        break
                    else:
                        print("bad input")
                        departure_t = input('Departure Time (YYYY-MM-DD HH:MM) = ')
           
                        arrival_t = input('Arrival Time (YYYY-MM-DD HH:MM) = ')
                    
                insert = 'insert into "trains" ("tr_id", "departure_t", "arrival_t") values ({}, \'{}\', \'{}\')'.format(
                    tr_id, departure_t, arrival_t)

                restart = False
            elif table == 3: #users
                p_id = input('User ID = ')
                full_name = input('Full name = ')
                while 1:
                    a = full_name.split(' ')
                    if len(a) ==2 and (a[0].isalpha() and a[1].isalpha()):
                        a[0] = a[0].lower()
                        a[0] = a[0].capitalize()
                        a[1] = a[1].lower()
                        a[1] = a[1].capitalize()
                        #print(a)
                        full_name = a[0] + ' ' + a[1]
                        #print(full_name)
                        break
                    else:
                        print('bad input')
                        full_name = input('Full name = ')
                pass_num = input('Passport number = ')
               


                insert = 'insert into "users" ("p_id", "full_name", "pass_num") values ({}, \'{}\', {})'.format(p_id, full_name, pass_num)

                restart = False
            else:
                print('\nIncorrect input, try again.')
        print(tables[table])
        print('SQl query => ', insert)
        cursor.execute(insert)
        connect.commit()
        print('Data added successfully!')
        cursor.close()
        Connect.closeConnect(connect)

    @staticmethod
    def update():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        restart = True
        while restart:
            View.list()
            table = Model.validTable()
            if table == 1:
                show = 'select * from public.tickets'
                cursor.execute(show)
                records = cursor.fetchall()
                obj = View(table, records)
                obj.show()
                #for row in obj.records:
                #    print(row[0])
                scname = "'" + input('Change row with t_id = ') + "'"
                
                View.attribute_list(1)
                
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"t_id"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"num"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"seat"= {}'.format(value)
                        in_restart = False
                    elif num == '4':
                        set = '"type"= {}'.format(value)
                        in_restart = False
                    elif num == '5':
                        set = '"p_id"= {}'.format(value)
                        in_restart = False
                    elif num == '6':
                        set = '"tr_id"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "tickets" set {} where "t_id"= {} returning t_id'.format(set, scname)
                restart = False
                pass
            elif table == 2:
                show = 'select * from public.trains'
                cursor.execute(show)
                records = cursor.fetchall()
                obj = View(table, records)
                obj.show()
                #for row in obj.records:
                #    print(row[0])
                clname = "'" + input('Change row with tr_id = ') + "'"
                
                View.attribute_list(2)
                
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"tr_id"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"departure_t"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"arrival_t"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "trains" set {} where "tr_id"= {} returning tr_id'.format(set, clname)
                restart = False
                pass
            elif table == 3:
                show = 'select * from public.users'
                cursor.execute(show)
                records = cursor.fetchall()
                obj = View(table, records)
                obj.show()
                #for row in obj.records:
                #    print(row[0])
                vroom = "'" + input('Change row with p_id = ') + "'"
                
                View.attribute_list(3)
                
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"p_id"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"full_name"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"pass_num"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "users" set {} where "p_id"= {} returning p_id'.format(set, vroom)
                restart = False
                pass

            else:
                print('\nIncorrect input, try again.')
        print(tables[table])
        print("SQL query => ", update)
        
        
        cursor.execute(update)
        if cursor.rowcount == 0:
            print('No such id in the table, data unchanged')
        else:
            connect.commit()
            print('Data updeted successfully!')
            cursor.close()
            Connect.closeConnect(connect)
            pass

    @staticmethod
    def random():
        connect = Connect.makeConnect()
        cursor = connect.cursor()

        incorrect = True
        while incorrect:
            num = input('How many users to random? => ')
            if num.isdigit():
                num = int(num)
                if num >= 1:
                    incorrect = False
                else:
                    print('Incorrect input, try again.')
            else:
                print('Incorrect input, try again.')
        
        insert = '''
        insert into "users" (p_id, full_name, pass_num)
        select (300*random())::integer+4,

        substr(md5(random()::text), 1, 10),
        (random() * 70 + 10)::integer
        FROM generate_series(1, {});

        '''.format(num)

        print("SQL query => ", insert)
        cursor.execute(insert)
        connect.commit()

        insert = '''
        insert into "trains" (tr_id, departure_t, arrival_t)
        select (300*random())::integer+4,

        DATE '2018-01-01' + (random() * 700)::integer,


        DATE '2018-01-01' + (random() * 700)::integer
        FROM generate_series(1, {});

        '''.format(num)

        print("SQL query => ", insert)
        cursor.execute(insert)
        connect.commit()

        print('Data randomed successfully!')
        cursor.close()
        Connect.closeConnect(connect)

    @staticmethod
    def search():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        restart = True
        while restart:
            incorrect = True
            while incorrect:
                mode = input('''
                1 -- mode 1
                2 -- test
                Choose mode = > ''')
                if mode.isdigit():
                    mode = int(mode)
                    if mode >= 1 and mode <= 2:
                        incorrect = False
                    else:
                        print('Incorrect input, try again.')
                else:
                    print('Incorrect input, try again.')
            if mode == 1:
                print("Find by id and ticket type")
                inp = input("id > ")
                inp = int(inp)
                inp1 = input("type > ")
                restart = False
                text_search = "select * from users join tickets on (users.p_id=tickets.p_id) where users.p_id={} and tickets.type = \'{}\'".format(inp, inp1)
            elif mode == 2:
                pass
            else:
                print('\nIncorrect input, try again.')

        #print(tables[table])
        print('SQL query => ', text_search)
        cursor.execute(text_search)
        #records = cursor.fetchall()
        #obj = View(table, records)
        #obj.show()
        rows = cursor.fetchall()
        print(rows)
        print('Data searched successfully!')
        cursor.close()
        Connect.closeConnect(connect)