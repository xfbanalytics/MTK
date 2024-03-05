CREATE TABLE input_catapult_teams_tags(load_timestamp DATETIME DEFAULT GETDATE(),
id NVARCHAR(MAX),
tag_type_id NVARCHAR(MAX),
name NVARCHAR(MAX),
tag_type_name NVARCHAR(MAX),
tag_name NVARCHAR(MAX))