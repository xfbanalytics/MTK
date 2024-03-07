CREATE TABLE input_catapult_parameter_types(
load_timestamp DATETIME DEFAULT GETDATE()
,id NVARCHAR(100)
,name NVARCHAR(100)
,is_synced INT 
,is_deleted INT
,created_at DATETIME
,modified_at DATETIME
)
