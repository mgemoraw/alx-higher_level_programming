-- lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, state.name FROM cities LEFT JOIN states ON states.id = cities.state_id
ORDER BY cities.id;

