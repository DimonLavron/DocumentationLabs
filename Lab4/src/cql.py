INSERT_DATA_SCRIPT = """
INSERT INTO shooting_incident
    (id, incident_key, occur_date, occur_time, boro, precinct, jurisdiction_code, location_desc, statistical_murder_flag,
    perp_age_group, perp_sex, perp_race, vic_age_group, vic_sex, vic_race, x_coord_cd, y_coord_cd, latitude, longitude)
VALUES
    (uuid(), '{incident_key}', '{occur_date}', '{occur_time}', '{boro}', {precinct}, {jurisdiction_code}, '{location_desc}', {statistical_murder_flag},
    '{perp_age_group}', '{perp_sex}', '{perp_race}', '{vic_age_group}', '{vic_sex}', '{vic_race}', {x_coord_cd}, {y_coord_cd}, {latitude}, {longitude})
"""

CREATE_TABLE_SCRIPT = """
CREATE TABLE IF NOT EXISTS shooting_incident (
    id uuid PRIMARY KEY,
    incident_key text,
    occur_date text,
    occur_time text,
    boro text,
    precinct int,
    jurisdiction_code int,
    location_desc text,
    statistical_murder_flag int,
    perp_age_group text,
    perp_sex text,
    perp_race text,
    vic_age_group text,
    vic_sex text,
    vic_race text,
    x_coord_cd int, 
    y_coord_cd int, 
    latitude int,
    longitude int
)
"""

DELETE_TABLE_SCRIPT = "DROP TABLE IF EXISTS shooting_incident"
