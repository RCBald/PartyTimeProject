DROP TABLE IF EXISTS Events,
DROP TABLE IF EXISTS Venues,
DROP TABLE IF EXISTS People;

CREATE TABLE Events (
    event_id INT PRIMARY KEY AUTO_INCREMENT,
    event_name VARCHAR(255) NOT NULL,
    event_date DATE NOT NULL,
    venue_id INT NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    invite TEXT,
    image_path VARCHAR(255),
    max_attendees INT,
    rental_items TEXT,
    party_notes TEXT,
    FOREIGN KEY (venue_id) REFERENCES Venues(venue_id)
)ENGINE = innodb;

CREATE TABLE Venues(
    venue_id INT PRIMARY KEY AUTO_INCREMENT,
    venue_name VARCHAR(255) NOT NULL,
    venue_address VARCHAR(255) NOT NULL,
    venue_phone VARCHAR(15),
    rental_fee DECIMAL(10, 2),
    max_attendees INT
)ENGINE = innodb;

CREATE TABLE People(
    people_id INT PRIMARY KEY AUTO_INCREMENT,
    person_name VARCHAR(255) NOT NULL,
    home_address VARCHAR(255) NOT NULL,
    email_address VARCHAR(255) NOT NULL,
    dob DATE,
    personal_phone VARCHAR(15) NOT NULL,
    role VARCHAR(20) NOT NULL
)ENGINE = innodb;


CREATE TABLE Event_attendees(
    event_id INT,
    people_id INT,
    PRIMARY KEY (event_id, people_id),
    FOREIGN KEY (event_id) REFERENCES Events (event_id),
    FOREIGN KEY (people_id) REFERENCES People (people_id)
)ENGINE = INNODB;

CREATE TABLE Event_host(
    event_id INT,
    people_id INT,
    PRIMARY KEY (event_id, people_id),
    FOREIGN KEY (event_id) REFERENCES Events(event_id),
    FOREIGN KEY (people_id) REFERENCES People(people_id)   
)ENGINE = INNODB;

CREATE TABLE Event_planner(
    event_id INT,
    people_id INT,
    PRIMARY KEY (event_id, people_id),
    FOREIGN KEY (event_id) REFERENCES Events(event_id),
    FOREIGN KEY (people_id) REFERENCES People(people_id)    
)ENGINE = INNODB;

INSERT INTO Events (event_name, event_date, venue_id, start_time, end_time, invite, image_path, max_attendees, rental_items, party_notes)
VALUES
('Birthday Bash', '2023-06-18', 4, '11:47:00', '23:07:00', 'You are invited!', 'images/birthday-party.png', 100, 'smoke machine,test speakers', NULL),
('Garden Gala', '2023-05-18', 1, '20:31:00', '15:42:00', 'You are invited!', 'images/music-concert.png', 95, 'tables,test lights', NULL),
('Midnight Soiree', '2023-04-15', 3, '08:06:00', '14:11:00', 'You are invited!', 'images/music-concert.png', 6,'PA system,test speakers', NULL),
('Masquerade Madness', '2023-04-02', 5, '16:23:00', '03:18:00', 'You are invited!', 'images/graduation-event.png', 25, 'tables,inflate balloons', NULL),
('Carnival Celebration', '2023-02-03', 2, '12:09:00', '18:01:00', 'You are invited!', 'images/birthday-party.png', 96, 'speakers,test speakers', NULL),
('Beach Bonanza', '2023-04-17', 6, '19:42:00', '20:28:00', 'You are invited!', 'images/outdoor-party.png', 5,'stage,set up streamers', NULL),
('Jacks Bday', '2023-11-02', 7, '20:49:00', '01:49:00', 'YOU SHOULD COME', 'static/images/birthday-party.png', 2,'chairs', 'get this kid laid, into this table');

INSERT INTO People (person_name, home_address, email_address, dob, personal_phone, role)
VALUES
('Xylia Emblen', '3 Delaware Terrace', 'xemblen0@tmall.com', '2018-06-19', '(322) 3807236','Planner'),
('Rosalia Lardner', '861 5th Parkway', 'rlardner1@wordpress.com', '1934-05-10', '(341) 8735710','Planner'),
('Willa Frounks', '48547 John Wall Park', 'wfrounks2@quantcast.com', '1974-04-29', '(478) 8869250','Host'),
('Fiona Drabble', '422 Coolidge Drive', 'fdrabble3@wsj.com', '1951-05-20', '(693) 1950101','Host'),
('Jeanna Oglesbee', '925 Sundown Drive', 'joglesbee4@163.com', '2014-08-04', '(342) 7719083','Attendee'),
('Franzen Beceril', '3 Bashford Hill', 'fbeceril5@ustream.tv', '1975-08-26', '(398) 8383580','Attendee'),
('koda', '401 North Jordan Avenue', 'kodabear3@gmail.com', '2021-04-08', '2036672324','Host'),
('dannette', '401 North Jordan Avenue', 'rcbaldwin77@gmail.com', '2023-10-04', '4152754148','Attendee');

INSERT INTO Venues (venue_name, venue_address, venue_phone, rental_fee, max_attendees)
VALUES
('Secret Warehouse', '282 Westend Road', '(963) 4105591', 4075.25, 172),
('The Grand Ballroom', '8199 Reindahl Place', '(416) 1107391', 4698.27, 158),
('Club X', '19158 Sherman Road', '(620) 1220128', 1372.79, 113),
('Blue Bird', '12 Doe Crossing Circle', '(990) 5138160', 1775.58, 154),
('KOK', '81646 Mayfield Avenue', '(824) 5367070', 3621.55, 125),
('Upstairs', '2265 Menomonie Court', '(704) 8587939', 1868.05, 152),
('MET Gala', 'New York New York', '(812) 537-2211', 4000.00, 465);

INSERT INTO Event_attendees (event_id, people_id)
VALUES
(8, 5),
(9, 6),
(10, 8),
(11, 5),
(12, 6),
(13, 8);

INSERT INTO Event_host (event_id, people_id)
VALUES
(1, 3),
(2, 4),
(3, 7),
(4, 3),
(5, 4),
(6, 7),
(7, 3);

INSERT INTO Event_planner (event_id, people_id)
VALUES
(1, 1),
(2, 2),
(3, 1),
(4, 2),
(5, 1),
(6, 2),
(7, 1);