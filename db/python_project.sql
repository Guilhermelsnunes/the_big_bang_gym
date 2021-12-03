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
    date INT,
    duration INT
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    gym_class_id INT REFERENCES gym_classes(id) ON DELETE CASCADE
);