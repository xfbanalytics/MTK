CREATE TABLE input_catapult_efforts(load_timestamp DATETIME DEFAULT GETDATE(),
activity_id NVARCHAR(100),
period_id NVARCHAR(100),
athlete_id NVARCHAR(100),
device_id INT,
player_id NVARCHAR(100),
athlete_first_name NVARCHAR(100),
athlete_last_name NVARCHAR(100),
jersey NVARCHAR(100),
team_id NVARCHAR(100),
team_name NVARCHAR(100),
data NVARCHAR(500))


