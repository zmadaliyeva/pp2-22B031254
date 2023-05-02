CREATE OR REPLACE FUNCTION get_data(pattern VARCHAR)
RETURNS TABLE (id INTEGER, first_name VARCHAR, last_name VARCHAR, phone_number VARCHAR)
AS $$
begin 
  RETURN QUERY 
  SELECT *
  FROM contacts 
  WHERE contacts.first_name LIKE '%'  pattern  '%'
    OR contacts.last_name LIKE '%'  pattern  '%'
   OR contacts.phone_number LIKE '%'  pattern  '%';
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_data('zhanerke');