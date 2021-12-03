DROP TABLE bookings;
DROP TABLE members;
DROP TABLE gym_classes;


CREATE TABLE members (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE gym_classes (
  id SERIAL PRIMARY KEY,
  category VARCHAR(255),
  name VARCHAR(255)
);

CREATE TABLE bookings(
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id) ON DELETE CASCADE,   --(delete cascade)if a user is deleted, any of his visits will also be deleted
  location_id INT REFERENCES locations(id) ON DELETE CASCADE,  -- location deleted, all visits will be deleted
  review TEXT
);