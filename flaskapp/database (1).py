from pymysql import connect
from pymysql.cursors import DictCursor

from flaskapp.config import DB_HOST, DB_USER, DB_PASS, DB_DATABASE

# Make sure you have data in your tables. You should have used auto increment for
# primary keys, so all primary keys should start with 1


def get_connection():
    return connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_DATABASE,
        cursorclass=DictCursor,
    )

def get_events():
    """Returns a list of dictionaries representing all of the event data"""
    sql = "select * from Events sort by event_name;"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            events=cursor.fetchall()
            return events

def get_event(event_id):
    """Takes a event_id, returns a single dictionary containing the data for the event with that id"""
    sql = "select * from Events where id = %s;"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (event_id))
            return cursor.fetchone()

def add_event(name,event_date,start_time,end_time,venue,invitation,maximum_attendees,planner,rental_items,note,image_path):
    """Takes as input all of the data for a event. Inserts a new event into the event table"""
    sql = "INSERT INTO Events(event_name, event_date, venue_id, start_time, end_time, invite, image_path, max_attendees, person_name, rental_items, party_notes)VALUES(%s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s); "
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,(name,event_date,venue,start_time,end_time,invitation,image_path,maximum_attendees,planner,rental_items,note))
        conn.commit()

def update_event(event_id, name,event_date,start_time,end_time,venue,invitation,maximum_attendees,planner,rental_items,note,image_path):
    """Takes a event_id and data for a event. Updates the event table with new data for the event with event_id as it's primary key"""
    sql ="UPDATE Events SET event_name =%s , event_date=%s,venue_id= %s,start_time=%s,end_time=%s ,invite= %s,image_path=%s,max_attendees=%s ,person_name=%s ,rental_items=%s ,party_notes= %s WHERE event_id=%s;"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,(name,event_date,venue,start_time,end_time,invitation,image_path, maximum_attendees,planner,rental_items,note, event_id))
        conn.commit()

def get_people():
    """returns a list of dictionaries representing all of people data"""
    sql = "SELECT * FROM People SORT BY people_id;"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            people=cursor.fetchall()
            return people

def add_person(name,address,email,dob,phone,role):
    """Takes as input all of the data for a person and adds a new person to the person table"""
    sql = "INSERT INTO People(person_name, home_address, email_address, dob, persona_phone, role)VALUES(%s,%s, %s, %s, %s, %s); "
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,(name,address,email,dob,phone,role))
        conn.commit()

def delete_person(person_id):
    """Takes a person_id and deletes the person with that person_id from the person table"""
    sql = "DELETE FROM People WHERE people_id = %s;"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (person_id))
        conn.commit()

def get_attendees(event_id):
    """Returns a list of dictionaries representing all of the data for people attending a particular event"""
    sql = "SELECT ea.people_id, p.person_name FROM event_attendees as ea JOIN People as p ON ea.person_id = p.people_id WHERE ea.event_id = %s;"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (event_id))
            attendees=cursor.fetchall()
            return attendees    

def add_attendee_event(event_id, attendee_id):
    """Takes as input a event_id and a attendee_id and inserts the appropriate data into the database that indicates the attendee with attendee_id as a primary key is attending the event with the event_id as a primary key"""
    sql = "INSERT INTO Event_attendees(event_id, people_id)VALUES(%s,%s); "
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,(event_id, attendee_id))
        conn.commit()   

def remove_attendee_event(event_id, attendee_id):
    """Takes as input a event_id and a attendee_id and deletes the data in the database that indicates that the attendee with attendee_id as a primary key
    is attending the event with event_id as a primary key."""
    sql = "DELETE FROM Event_attendees Where event_id=%s AND people_id=%s;"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (event_id, attendee_id))
        conn.commit()    

def get_host(event_id):
    """Takes a event_id and returns a dictionary of the data for the host of the event with
    event_id as its primary key"""
    sql = "SELECT eh.people_id, p.person_name FROM Event_host AS eh JOIN People AS p ON eh.people_id=p.people_id WHERE eh.people_id =%s;"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (event_id))
            host=cursor.fetchall()
            return host
    
def set_host(person_id, event_id):
    """Sets the person with primary key person_id as the host of the event with event_id as its primary key"""
    sql = "INSERT INTO Event_host(event_id, people_id)VALUES(%s,%s); "
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,(event_id, person_id))
        conn.commit() 

def get_planner(event_id):
    """Takes a event_id and returns a dictionary of the data for the planner of the event with
    event_id as its primary key"""
    sql = "SELECT ep.people_id, p.person_name FROM Event_planneras ep JOIN People as p ON ep.people_id = p.people_id WHERE ep.event_id=%s;"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, (event_id))
            host=cursor.fetchall()
            return host


def set_planner(person_id, event_id):
    """Sets the person with primary key person_id as the planner of the event with event_id as its primary key"""
    sql = "INSERT INTO Event_planner(event_id, people_id)VALUES(%s,%s); "
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,(event_id, person_id))
        conn.commit()

def get_venues():
    """Returns a list of dictionaries representing all of the venues data"""
    sql = "SELECT * FROM Venues SORT BY venue_id;"
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            venues=cursor.fetchall()
            return venues

def add_venue(name,address,phone,fee,capacity):
    """Takes as input all of the data for a venue. Inserts a new venue into the event table"""
    sql = "INSERT INTO Venues(venue_name, venue_address, venue_phone, rental_fee, max_attendees)VALUES(%s,%s, %s, %s, %s); "
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql,(name,address,phone,fee,capacity))
        conn.commit()    


if __name__ == "__main__":
    # Add test code here to make sure all your functions are working correctly

    print(f"All events: {get_events()}")
    print(f"Event info for event_id 1: {get_event(1)}")
    print(f"All people: {get_people()}")
    print(f"All attendees attending the event with event_id 1: {get_attendees(1)}")
