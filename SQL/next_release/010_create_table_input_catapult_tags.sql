CREATE TABLE input_catapult_tags(load_timestamp DATETIME DEFAULT GETDATE(),
id NVARCHAR(MAX),
tag_type_id NVARCHAR(MAX),
name NVARCHAR(MAX),
is_synced NVARCHAR(MAX),
is_deleted NVARCHAR(MAX),
created_at NVARCHAR(MAX),
modified_at NVARCHAR(MAX),
tag_name NVARCHAR(MAX))