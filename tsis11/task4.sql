CREATE OR REPLACE FUNCTION get_users_with_limit(limitt INTEGER, offset INTEGER)
RETURNS SETOF contacts
AS $$
BEGIN 
   RETURN QUERY SELECT * FROM contacts LIMIT limitt OFFSET offsett;
END;
$$
LANGUAGE plpgsql;

SELECT * FROM get_users_with_limit(3,6);