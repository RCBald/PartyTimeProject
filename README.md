
**# Event Planner App**

This repository contains the code for a Python-based event planning application, built using Flask and MySQL.

**## Features**

- **Manage events:** Create, view, edit, and delete events.
- **Organize attendees:** Add attendees to events, manage their roles, and track attendance.
- **Handle venues:** Create, view, and manage venue information.
- **Assign planners and hosts:** Assign individuals as event planners and hosts.
- **Track essential details:** Store event dates, times, rental items, notes, and images.

**## Setup**

1. **Install dependencies:**
   ```bash
   pip install flask pymysql
   ```
2. **Create the database:**
   - Import the SQL file provided in the repository to create the necessary tables and initial data.
   - Configure database connection details in `flaskapp/config.py`.
3. **Run the application:**
   ```bash
   python app.py
   ```

**## Usage**

- Access the application in your web browser at `http://localhost:5000/`.
- Use the provided routes to interact with the application's features:
   - `/events`: View all events.
   - `/event/<int:event_id>`: View a specific event.
   - `/add_event`: Create a new event.
   - `/venues`: View all venues.
   - `/people`: View all people (attendees, planners, hosts).
   - `/add_venue`: Add a new venue.
   - `/add_people`: Add a new person.

**## Additional Information**

- **Database Structure:** The `database.sql` file contains the SQL statements for creating the database tables and initial data.
- **Database Connection:** The `flaskapp/config.py` file contains placeholders for database connection credentials.
- **Flask Routes:** The `app.py` file defines the Flask routes for handling different application functionalities.

**## Contributing**

This is a personal project, but feel free to fork and contribute if you have suggestions or improvements.
