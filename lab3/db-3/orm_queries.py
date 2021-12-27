from Models import *
import psycopg2
from sqlalchemy.orm import *
from sqlalchemy import create_engine




def insert_one_orm(Session,table_name,list):

    session = Session()

    if table_name == "tickets":
        table_item = tickets(t_id = list[0], num = list[1], seat = list[2], type = list[3], p_id = list[4], tr_id = list[5])
    elif table_name == "users":
        table_item = users(p_id = list[0],full_name = list[1], pass_num = list[2])
    else:
        table_item = trains(tr_id = list[0],departure_t = list[1], arrival_t = list[2])
    session.add(table_item)
    session.commit()
    session.close()



def select_all_orm(Session,table_name):
    session = Session()
    if table_name == "users":
        table_item = session.query(users).all()
    elif table_name == "trains":
        table_item = session.query(trains).all()
    else:
        table_item = session.query(tickets).all()
    session.close()

    return table_item


def delete_one_orm(Session,table_name,pr_key):
    session = Session()
    if table_name == "users":
        table_item = session.query(users).filter(users.p_id == pr_key).first()
    elif table_name == "trains":
        table_item = session.query(trains).filter(trains.tr_id == pr_key).first()
    else:
        table_item = session.query(tickets).filter(tickets.t_id == pr_key).first()
    if table_item is None:
        session.close()
        return 0

    session.delete(table_item)
    session.commit()
    session.close()

    return 1


def update_item_orm(Session,table_name,list):
    session = Session()

    if table_name == "users":
        table_item = session.query(users).filter(users.p_id == list[0]).first()
        if table_item is None:
            session.close()
            return 0
        table_item.full_name,table_item.pass_num= list[1],list[2]
    elif table_name == "trains":
        table_item = session.query(trains).filter(trains.tr_id == list[0]).first()
        if table_item is None:
            session.close()
            return 0
        table_item.departure_t,table_item.arrival_t= list[1],list[2]
    else:
        table_item = session.query(tickets).filter(tickets.t_id == list[0]).first()
        if table_item is None:
            session.close()
            return 0
        table_item.num, table_item.seat, table_item.type, table_item.p_id, table_item.tr_id = list[1],list[2],list[3],list[4],list[5]
    session.commit()
    session.close()

    return 1


def connect_to_db():
    connection = psycopg2.connect(dbname="postgres", user="postgres", password="123",
                                  host="127.0.0.1", port="5432")
    return connection


def connect_to_db_orm():
    engine = create_engine('postgresql+psycopg2://postgres:123@localhost:5432/postgres')
    session_class = sessionmaker(bind=engine)
    return session_class


def disconnect_from_db(connection,cursor):
    cursor.close()
    connection.close()
    print("Connection with PostgreSQL is closed")








