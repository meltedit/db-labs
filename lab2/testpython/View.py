import Connect

class View:
    # Initialization of class View
    def __init__(self, table, records):
        self.table = table
        self.records = records

            # Method that prints the list of DB tables
    @staticmethod
    def list():
        print('''
        1 => tickets
        2 => trains
        3 => users
        ''')

    # Method that prints the list of attributes of the selected table
    @staticmethod
    def attribute_list(table):
        if table == 1:
            print('''
            1 => t_id
            2 => num
            3 => seat
            4 => type
            5 => p_id
            6 => tr_id
            ''')
        elif table == 2:
            print('''
            1 => tr_id
            2 => departure_t
            3 => arrival_t
            ''')
        elif table == 3:
            print('''
            1 => p_id
            2 => full_name
            3 => pass_num
            ''')


    # Method that prints content from a selected table
    def show(self):
        print("____________________\n")
        if self.table == 1:
            for row in self.records:
                print("t_id = ", row[0])
                print("num = ", row[1])
                print("seat = ", row[2])
                print("type = ", row[3])
                print("p_id = ", row[4])
                print("tr_id = ", row[5])
                print("____________________\n")
        elif self.table == 2:
            for row in self.records:
                print("tr_id = ", row[0])
                print("departure_t = ", row[1])
                print("arrival_t = ", row[2])
                print("____________________\n")
        elif self.table == 3:
            for row in self.records:
                print("p_id = ", row[0])
                print("full_name = ", row[1])
                print("pass_num  = ", row[2])
                print("____________________\n")
