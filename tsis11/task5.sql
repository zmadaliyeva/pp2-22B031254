CREATE OR REPLACE PROCEDURE delete_user(name VARCHAR, phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
  DELETE FROM contacts WHERE first_name = name OR phone_number = phone;
  END;
  $$;

  CALL delete_user('Zhanerke','87000000');