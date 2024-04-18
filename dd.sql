use hbnb_dev_db;
show tables;

-- drop TABLE amenities, place_amenity, places, reviews, states, users;
CREATE TABLE place_amenity (
        place_id VARCHAR(60) NOT NULL,
        PRIMARY KEY (place_id),
        FOREIGN KEY(place_id) REFERENCES places (id))

