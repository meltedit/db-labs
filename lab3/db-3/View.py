class View(object):

    @staticmethod
    def table_name_select_display():
        print("Select table name:\n")
        print("1---users\n2---trains\n3---tickets\n")

    @staticmethod
    def action_select_display():
        print("Select action(number):\n")
        print("1---Show table items\n2---Update table item\n3---Insert new table item\n"
        "4---Delete table item\n")

    @staticmethod
    def enter_cortege_item_display(item):
        print("Enter {}".format(item))

    @staticmethod
    def table_rows_display(items):
        cursor = items
        row = items.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()

    @staticmethod
    def table_rows_display_orm(items):
        for item in items:
            print(item.__repr__())

    @staticmethod
    def question_about_end_display():
        print("Continue to work with Database?(Y/N)\n")

    @staticmethod
    def message_print(message):
        print(message)

    @staticmethod
    def question_about_local_end_display():
        print("Enter data again?(Y/N)\n")