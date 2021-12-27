
class Controller(object):
    def __init__(self, model, view):
        self._model = model
        self._view = view

    @property
    def model(self):
        return self._model

    @property
    def view(self):
        return self._view

    def show_items(self):
        items = self.model.read_items()
        if self.model.orm_session is not None:
            if items.count:
                self.view.table_rows_display_orm(items)
                return
        elif items.rowcount:
            self.view.table_rows_display(items)
            return
        self.view.message_print("This table was already empty\n")

    def enter_items(self, table_item_names):
        return_array = []
        for name in table_item_names:
            while True:
                self.view.enter_cortege_item_display(name)
                inp = str(input())
                return_array.append(inp)
                break
        return return_array

    def table_type_select(self):
        self.view.table_name_select_display()
        while True:
            table_type = str(input())
            if (table_type == "users" or table_type == "trains" or table_type == "tickets"):
                self.model.present_table_type = table_type
                return
            self.view.message_print("Error:enter one of suggested table names\n")

    def action_select(self):
        self.view.action_select_display()
        while True:
            action = str(input())
            if action == "1":
                self.show_items()
            elif action == "2":
                self.update_item()
            elif action == "3":
                self.insert_item()
            elif action == "4":
                self.delete_item()
            else:
                self.view.message_print("Error:Enter number from 1-4\n")
                continue
            break


    def question_about_end(self):
        self.view.question_about_end_display()
        while True:
            inp = str(input())
            if inp == "Y":
                return True
            elif inp == "N":
                return False
            else:
                self.view.message_print("""Error:enter "Y" or "N"\n """)

    def disconnect_from_db(self):
        self.model.disconnect_from_db()

    def insert_item(self):
        while True:
            if self.model.present_table_type == 'users':
                list = self.enter_items(("p_id", "full_name", "pass_num"))
            elif self.model.present_table_type == 'trains':
                list = self.enter_items(("tr_id", "departure_t", "arrival_t"))
            else:
                list = self.enter_items(("t_id", "num", "seat", "type", "p_id", "tr_id"))
            try:
                self.model.create_item(list)
                self.view.message_print("Row was inserted successfully\n")
                break
            except Exception as error:
                print(error)
                self.view.question_about_local_end_display()
                while True:
                    answer = str(input())
                    if answer == "N":
                        return
                    elif answer == "Y":
                        break
                    else:
                        self.view.message_print("Enter Y or N \n")

    def update_item(self):
        while True:
            if self.model.present_table_type == 'users':
                list = self.enter_items(("p_id", "full_name", "pass_num"))
            elif self.model.present_table_type == 'trains':
                list = self.enter_items(("tr_id", "departure_t", "arrival_t"))
            else:
                list = self.enter_items(("t_id", "num", "seat", "type", "p_id", "tr_id"))
            try:
                if self.model.update_item(list):
                    self.view.message_print("Row was updated successfully\n")
                else:
                    self.view.message_print("There isn't element with such ID in table\n")
                break
            except Exception as error:
                print(error)
                self.model.connection.commit()
                self.view.question_about_local_end_display()
                while True:
                    answer = str(input())
                    if answer == "N":
                        return
                    elif answer == "Y":
                        break
                    else:
                        self.view.message_print("Enter Y or N \n")

    def delete_item(self):
        if self.model.present_table_type == 'users':
            list = self.enter_items(["p_id"])
        elif self.model.present_table_type == 'trains':
            list = self.enter_items(["tr_id"])
        else:
            list = self.enter_items(["t_id"])
        if self.model.delete_item(list[0]):
            self.view.message_print("Row was deleted successfully\n")
        else:
            self.view.message_print("There isn't row for deleting with such attribute value\n")


    
