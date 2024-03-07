CREATE TABLE input_catapult_threshold_sets(
load_timestamp DATETIME DEFAULT GETDATE()
,id NVARCHAR(100)
,name NVARCHAR(100)
,alert NVARCHAR(200)
,is_deleted INT
,created_at DATETIME
,modified_at DATETIME
,athlete_count	INT

 


)
