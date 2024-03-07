
CREATE TABLE input_catapult_events_goalkeeping_v2 (
load_timestamp DATETIME DEFAULT GETDATE(),
activity_id NVARCHAR(MAX),
period_id NVARCHAR(MAX),
athlete_id NVARCHAR(MAX),
start_time NVARCHAR(MAX),
end_time NVARCHAR(MAX),
version NVARCHAR(MAX),
direction NVARCHAR(MAX),
load NVARCHAR(MAX),
time_to_feet NVARCHAR(MAX),
pre_event_load NVARCHAR(MAX),
impact_load NVARCHAR(MAX),
post_event_load NVARCHAR(MAX)

)
