CREATE TABLE weather (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    temperature NUMERIC,
    description TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	wind_speed NUMERIC,
	wind_direction VARCHAR(10),
	pressure NUMERIC,
	humidity NUMERIC,
	feelslike NUMERIC,
	uv_index NUMERIC
);
