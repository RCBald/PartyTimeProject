from flask import Flask, render_template, request, redirect, url_for
import csv
from flaskapp import database 
app = Flask(__name__)

def check_attendees(attendees):
    """Def checks to see if there are any attendees present
    returns string if there are none"""
    if not attendees:
        return "There is no one attending this event"

def check_new_venue(venue_name, venue_address, venue_phone, venue_fee, venue_capacity):
    """Function to prevent form from crashing"""
    error=""
    msg = []
    if not venue_name:
        msg.append("Name missing! ")
    if len(venue_name) > 255:
        msg.append("name is too long")
    if not venue_address:
        msg.append("address missing")
    if len(venue_address) > 255:
        msg.append("address is too long")
    if not venue_phone:
        msg.append("Phone number missing! ")
    if len(venue_phone) > 255:
        msg.append("phone number is too long")
    if not venue_fee:
        msg.append("Fee missing! ")
    if len(venue_fee) > 12:
        msg.append("Fee is too long")
    if not venue_capacity:
        msg.append("Capacity missing! ")
    if venue_capacity is not int:
        msg.append("Capacity is not a number")
    if len(msg) > 0:
        error="\n".join(msg)
    return error

def check_new_person(person_name, person_address, person_email, person_phone, person_dob, person_role):
    """Prevents new person form from crashing"""
    error=""
    msg = []
    if not person_name:
        msg.append("name missing")
    if len(person_name) >255:
        msg.append("name is too long")
    if not person_address:
        msg.append("address missing")
    if len(person_name) >255:
        msg.append("name is too long")
    if not person_email:
        msg.append("email missing")
    if len(person_email) >255:
        msg.append("email is too long")
    if not person_phone:
        msg.append("phone missing")
    if len(person_phone) >15:
        msg.append("phone is too long")
    if not person_dob:
        msg.append("Date of Birth missing")
    if not person_role:
        msg.append("role missing")
    if len(person_name) >255:
        msg.append("role is too long")
    if len(msg)> 0:
        error-"\n".join(msg)
    return error

def check_new_event(event_name, event_date, event_start_time, event_end_time, event_venue, event_invitation, event_max_attendees, event_rentals, event_notes, event_image ):
    """Prevents new person form from crashing"""
    error=""
    msg = []
    if not event_name:
        msg.append("event missing")
    if len(event_name) >255:
        msg.append("name is too long")
    if not event_date:
        msg.append("date missing")
    if not event_start_time:
        msg.append("Start time missing")
    if not event_end_time:
        msg.append("end time missing")
    if not event_venue:
        msg.append("venue missing")
    if event_venue is not int:
        msg.append("venue id is not a number")
    if not event_invitation:
        msg.append("invitation missing")
    if len(event_invitation) > 100000:
        msg.append("invitation is too long")
    if not event_max_attendees:
        msg.append("attendees missing")
    if event_max_attendees is not int:
        msg.append("attendees is not number")
    if not event_rentals:
        msg.append("rental info is missing")
    if not event_notes:
        msg.append("notes missing")
    if not event_image:
        msg.append("image missing")
    if len(event_image) > 255:
        msg.append("image path too long")
    if len(msg)> 0:
        error-"\n".join(msg)
    return error

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/venues/")
def venues():
    """retrieves venue information"""
    all_venues = database.get_venues()
    return render_template("venues.html", venues=all_venues) 

@app.route("/add_venue", methods=['GET','POST'])
def add_venue():
        #POST - form submit button is clicked
    if request.method == 'POST':
        venue_name = request.form['venue_name']
        venue_address = request.form['venue_address']
        venue_phone = request.form['venue_phone']
        venue_fee = request.form['venue_fee']
        venue_capacity = request.form['venue_capacity']

        error = check_new_venue(venue_name, venue_address, venue_phone, venue_fee, venue_capacity)
        #error code for possible over flowing and missing values in form
        if error:
            return render_template("venues_form.html", error=error)
        #otherwise adds new venue
        database.add_venue(venue_name, venue_address, venue_phone, venue_fee, venue_capacity)

        return redirect(url_for("venues"))
    else:
    #GET - User wants to go to the form
        return render_template("venues_form.html")
    


@app.route("/people/")
def people():
    all_people = database.get_people()
    return render_template("people.html", peoples=all_people)

@app.route("/add_people", methods=['GET','POST'])
def add_people():
    #POST - form submit button is clicked
    if request.method == 'POST':

        person_name = request.form['person_name']
        person_address = request.form['person_address']
        person_email = request.form['person_email']
        person_phone = request.form['person_phone']
        person_dob = request.form['person_dob']
        person_role = request.form['person_role']
        #error anticipation for an overlfower form
        error = check_new_person(person_name, person_address, person_email, person_phone, person_dob, person_role)
        if error:
            return render_template("people_form.html", error=error)
        #otherwise adds new person and redirects to people page 
        database.add_person(person_name, person_address, person_email, person_dob, person_phone, person_role)

        return redirect(url_for("people"))
    else:
    #GET - User wants to go to the form
        return render_template("people_form.html")


@app.route("/events")
def events():
    #retrieves information for all events
    all_events = database.get_events()
    return render_template("events.html", events=all_events)

@app.route("/event/")
@app.route('/event/<int:event_id>/')
def event(event_id=None):
    #retrieves information for a specific event
    get_peoples=database.get_possible_attendees()
    all_events=database.get_events()
    if event_id:
        get_event = database.get_event(event_id)
        get_attendees = database.get_attendees(event_id)
        error = check_attendees(get_attendees)
        if error:
            return render_template("event.html", event=get_event, attendees = get_attendees, error=error)
        return render_template("event.html", event= get_event, attendees = get_attendees, )
    return render_template('events.html', events=all_events, peoples=get_peoples)


@app.route('/delete_attendee/<int:event_id>/<int:attendee_id>', methods=['GET','POST'])
def delete_attendee(event_id, attendee_id):
    """removes attendee from event registration"""
    if request.method == 'POST':
        database.remove_attendee_event(event_id, attendee_id)
        get_event = database.get_event(event_id)
        get_attendees = database.get_attendees(event_id)
        error = check_attendees(get_attendees)
        if error:
            return render_template("event.html", event=get_event, attendees = get_attendees, error=error)
        return render_template("event.html")
    else:
        return render_template("event.html")
    
@app.route('/add_attendee/<int:event_id>',methods=['GET','POST'])
def add_attendee(event_id):
    """Adds new attendee to event via drop down menu and button"""
    get_peoples = database.get_possible_attendees()
    if request.method=="POST":
        people_id = request.form['people_id']
        database.add_attendee_event(event_id, people_id)
    else:
        return render_template("event.html", peoples=get_peoples)

@app.route("/add_event", methods=['GET','POST'])
def add_event():
    #POST - form submit button is clicked
    get_host = database.get_host()
    get_planner = database.get_planner()
    get_venues = database.get_venues()

    if request.method == 'POST':

        event_name = request.form['event_name']
        event_venue = request.form['event_venue']
        event_date = request.form['event_date']
        event_start_time = request.form['event_start_time']
        event_end_time = request.form['event_end_time']
        event_max_attendees = request.form['event_max_attendees']
        event_invitation = request.form['event_invitation']
        event_attendees = request.form['event_attendees']
        event_planner = request.form['event_planner']
        event_host = request.form['event_host']
        event_rentals = request.form['event_rentals']
        event_image = request.form['event_image']
        event_notes = request.form['event_notes']
        #error anticipation for an over flow or missing values in the form
        error = check_new_event(event_name, event_date, event_start_time, event_end_time, event_venue, event_invitation, event_max_attendees, event_rentals, event_notes, event_image)
        if error:
                return render_template("event_form.html", error=error)
        
        event_id = database.add_event(event_name, event_date, event_start_time, event_end_time, event_venue, event_invitation, event_max_attendees, event_rentals, event_notes, event_image )

        database.add_attendee_event(event_id, event_attendees)
        database.set_planner(event_planner, event_id) 
        database.set_host(event_host, event_id)


        return redirect(url_for("events"))
    else:
    #GET - User wants to go to the form
        return render_template("event_form.html", hosts=get_host, planners=get_planner, venues=get_venues)



#steps to deploy
#1. push all the code to github main branch
#2. logon to your luddy server (ssh username@silo.luddy.indiana.edu)
#3. change your current working directory to cgi-pub (cd cgi-pub)
#4. change your current working directory to i211 project (cd i211_project)
#5. git pull (enter your iu username and password)
#6 open your git repo and click on the link and verify booom