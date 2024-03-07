
CREATE TABLE input_catapult_efforts_acceleration_efforts(load_timestamp DATETIME DEFAULT GETDATE(),
activity_id NVARCHAR(100),
period_id NVARCHAR(100),
athlete_id NVARCHAR(100),
start_time NUMERIC(12,2),
end_time NUMERIC(12,2),
band NVARCHAR(10),
acceleration NUMERIC(10,2),
distance NUMERIC(10,2))

