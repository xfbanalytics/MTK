
CREATE TABLE input_catapult_periods(
load_timestamp DATETIME DEFAULT GETDATE()
,id NVARCHAR(100)
,activity_id NVARCHAR(100)
,period_depth_id NVARCHAR(100)
,name NVARCHAR(100)
,start_time INT
,start_centiseconds INT
,end_time INT
,end_centiseconds INT
,lft INT
,rgt INT
,is_synced INT
,is_deleted INT
,is_injected INT 
,created_at DATETIME
,modified_at DATETIME
,user_id NVARCHAR(100)
--,tags
)