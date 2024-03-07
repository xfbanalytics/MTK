CREATE TABLE input_catapult_parameters(load_timestamp DATETIME DEFAULT GETDATE(),
id NVARCHAR(100),
parameter_type_id NVARCHAR(100),
name NVARCHAR(100),
original_name NVARCHAR(100),
slug NVARCHAR(100),
calculation NVARCHAR(500),
ctr_order INT,
created_at DATETIME,
modified_at DATETIME,
unit_type NVARCHAR(50))