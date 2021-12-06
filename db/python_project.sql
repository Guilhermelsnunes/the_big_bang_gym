DROP TABLE bookings;
DROP TABLE members;
DROP TABLE gym_classes;


CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT
);

CREATE TABLE gym_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date VARCHAR(255),
    duration INT
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    gym_class_id INT REFERENCES gym_classes(id) ON DELETE CASCADE
);

--Including records for testing
INSERT INTO members (first_name, last_name, age) VALUES ('Guilherme', 'Nunes', 18);
INSERT INTO members (first_name, last_name, age) VALUES ('David', 'Cipriano', 38);
INSERT INTO members (first_name, last_name, age) VALUES ('Luigi', 'Cipriano', 15);

INSERT INTO gym_classes (name, date, duration) VALUES ('Jiu-Jitsu', '15/12/2021 18:00:00', 60);
INSERT INTO gym_classes (name, date, duration) VALUES ('Capoeira', '20/12/2021 15:30:00', 45);
INSERT INTO gym_classes (name, date, duration) VALUES ('Judo', '06/12/2021 11:25:00', 90);

INSERT INTO  bookings (member_id, gym_class_id) VALUES (1,1);
INSERT INTO  bookings (member_id, gym_class_id) VALUES (1,2);
INSERT INTO  bookings (member_id, gym_class_id) VALUES (1,3);
INSERT INTO  bookings (member_id, gym_class_id) VALUES (2,3);
INSERT INTO  bookings (member_id, gym_class_id) VALUES (3,2);
INSERT INTO  bookings (member_id, gym_class_id) VALUES (3,1);