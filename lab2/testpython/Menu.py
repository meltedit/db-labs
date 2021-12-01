from Model import Model

class Menu:
    # Main Method that calls main manu of the  controller
    @staticmethod
    def mainmenu():
        exit = False
        while not exit:
            print('''
            Main menu
            0 => Show one table
            1 => Show all table
            2 => Insert data
            3 => Delete data
            4 => Update data
            5 => Search by p_id and ticket type
            6 => Randomize data in users and trains
            7 => Exit''')
            choice = input('\nMake your choice => ')
            if choice == '0':
                Model.showOneTable()
                pass
            elif choice == '1':
                Model.showAllTables()

            elif choice == '2':
                end_insert = False
                while not end_insert:
                    Model.insert()
                    incorrect = True
                    while incorrect:
                        num = input('\nContinue insertion? 1 - Yes; 2 - No =>')
                        if num == '2':
                            end_insert = True
                            incorrect = False
                        elif num == '1':
                            incorrect = False
                            pass
                        else:
                            print('\nIncorrect input, try again.')

            elif choice == '3':
                end_delete = False
                while not end_delete:
                    Model.delete()
                    incorrect = True
                    while incorrect:
                        num = input('\nContinue deletion? 1 - Yes; 2 - No =>')
                        if num == '2':
                            end_delete = True
                            incorrect = False
                        elif num == '1':
                            incorrect = False
                            pass
                        else:
                            print('\nIncorrect input, try again.')

            elif choice == '4':
                end_update = False
                while not end_update:
                    Model.update()
                    incorrect = True
                    while incorrect:
                        num = input('\nContinue updation? 1 - Yes; 2 - No =>')
                        if num == '2':
                            end_update = True
                            incorrect = False
                        elif num == '1':
                            incorrect = False
                            pass
                        else:
                            print('\nIncorrect input, try again.')

            elif choice == '5':
                end_search = False
                while not end_search:
                    Model.search()
                    incorrect = True
                    while incorrect:
                        num = input('\nContinue to find? 1 - Yes; 2 - No =>')
                        if num == '2':
                            end_search = True
                            incorrect = False
                        elif num == '1':
                            incorrect = False
                            pass
                        else:
                            print('\nIncorrect input, try again.')

            elif choice == '6':
                end_random = False
                while not end_random:
                    Model.random()
                    incorrect = True
                    while incorrect:
                        num = input('\nContinue randomizition? 1 - Yes; 2 - No =>')
                        if num == '2':
                            end_random = True
                            incorrect = False
                        elif num == '1':
                            incorrect = False
                        else:
                            print('\nIncorrect input, try again.')

            elif choice == '7':
                #exit = True
                break

            else:
                print('\nIncorrect input, try again.')

            incorrect = True
            while incorrect:
                end = input('\nContinue work with DB? 1 - Yes; 2 - No. = >')
                if end == '2':
                    incorrect = False
                    exit = True
                elif end == '1':
                    incorrect = False
                else:
                    print('\nIncorrect input, try again.')
