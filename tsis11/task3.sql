CREATE OR REPLACE PROCEDURE add_users(user_list VARCHAR[])
LANGUAGE plpgsql
AS $$ 
DECLARE
  name VARCHAR;
  phone VARCHAR;
  incorrect_phones VARCHAR[];
BEGIN 
  FOREACH name IN ARRAY user_list
  LOOP
   phone := substring(name from '8\d{10}$');
   IF phone IS NULL THEN
    incorrect_phones := array_append(incorrect_phones, name);
   ELSE 
    INSERT INTO contacts(first_name, phone_number) VALUES(substring(name from '^[^\d]+'), phone);
   END IF;
  END LOOP; 
  IF array_length(incorrect_phones, 1) IS NOT NULL THEN
    RAISE NOTICE 'Incorret phone numbers: %', incorrect_phones;
  END IF;
END;
$$;

CALL add_users(ARRAY['Misha 870007276950', 'Danik 87751003322']);
sex pex narkotiki scandal
