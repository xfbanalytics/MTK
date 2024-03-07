CREATE TABLE input_catapult_events_ima_impact(load_timestamp DATETIME DEFAULT GETDATE(),
activity_id NVARCHAR(100),
period_id NVARCHAR(100),
athlete_id NVARCHAR(100),
start_time NUMERIC(12,2),
end_time NUMERIC(12,2),
version NVARCHAR(10),
impact NUMERIC(10,5),
direction NVARCHAR(50))