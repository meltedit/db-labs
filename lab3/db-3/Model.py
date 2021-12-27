import orm_queries


class ModelPostgreSQL(object):
    def __init__(self,orm = True):
        self._orm_session = orm_queries.connect_to_db_orm()
        self._present_table_type = ''

    @property
    def orm_session(self):
        return self._orm_session

    @property
    def present_table_type(self):
        return self._present_table_type

    @present_table_type.setter
    def present_table_type(self,new_present_table_type):
        self._present_table_type = new_present_table_type

    def create_item(self,cortage):
        return orm_queries.insert_one_orm(self.orm_session,self.present_table_type,cortage)


    def read_items(self):    
        return orm_queries.select_all_orm(self.orm_session,self.present_table_type)
       

    def update_item(self, list):
        return orm_queries.update_item_orm(self.orm_session,self.present_table_type,list)


    def delete_item(self,pr_key):
        return orm_queries.delete_one_orm(self.orm_session,self.present_table_type,pr_key)



