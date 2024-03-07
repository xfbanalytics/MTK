CREATE TABLE input_catapult_tags(load_timestamp DATETIME DEFAULT GETDATE(),
id NVARCHAR(100),
tag_type_id NVARCHAR(100),
name NVARCHAR(100),
is_synced INT,
is_deleted INT,
created_at DATETIME,
modified_at DATETIME,
tag_name NVARCHAR(100))