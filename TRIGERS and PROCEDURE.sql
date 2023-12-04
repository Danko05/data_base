use iot_db;

DROP TRIGGER IF EXISTS prevent_double_zero;
DELIMITER //
CREATE TRIGGER prevent_double_zero
BEFORE INSERT ON actors
FOR EACH ROW
BEGIN
    IF NEW.age LIKE '%00' THEN 
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Значення стовпця age не може закінчуватися двома нулями';
    END IF;
END;
//
DELIMITER ;


DROP TRIGGER IF EXISTS correct_gender;
DELIMITER //
CREATE TRIGGER correct_gender
BEFORE INSERT ON actors 
FOR EACH ROW 
BEGIN 
	IF NOT (NEW.sex IN ('FEMALE', 'MALE')) THEN 
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Неправильний формат для стовпця sex. Використовуйте "Female" або "Male';
    END IF;
END;
// 
DELIMITER ;


DROP TRIGGER IF EXISTS prevent_row_deletion;
DELIMITER //
CREATE TRIGGER prevent_row_deletion
BEFORE DELETE ON viewer
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Видалення рядків заборонено для таблиці viewer.';
END;
//
DELIMITER ;



DROP TRIGGER IF EXISTS check_cinema_id;
DELIMITER //
CREATE TRIGGER check_cinema_id
BEFORE INSERT ON cinema_hall
FOR EACH ROW
BEGIN
    DECLARE cinema_exists INT;
    SELECT COUNT(*) INTO cinema_exists FROM cinema WHERE id = NEW.cinema_id;
    IF cinema_exists = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Невірний cinema_id. Значення не існує в таблиці cinema.';
    END IF;
END;
//
DELIMITER ;




DROP PROCEDURE IF EXISTS InsertRows;
DELIMITER $$
CREATE PROCEDURE InsertRows()
BEGIN
  DECLARE i INT DEFAULT 319;
  WHILE i <= 329 DO
    INSERT INTO film (name) VALUES (CONCAT('Film', i));
    SET i = i + 1;
  END WHILE;
END$$
DELIMITER ;

CALL InsertRows();






-- DROP TRIGGER IF EXISTS correct_name;
-- DELIMITER // 
-- CREATE TRIGGER correct_name
-- BEFORE INSERT ON viewer
-- FOR EACH ROW
-- 	BEGIN 
--         IF NOT (NEW.name REGEXP '^[AMZ]\d{5}[A-Za-z]{2}$') THEN 
--         SIGNAL SQLSTATE  '45000'
--         SET MESSAGE_TEXT = 'Неправильний формат для стовпця viewer. Використовуйте формат: A, M або Z, 5 цифр, 2 букви.';
--         END IF ;
-- 	END;
--     //
--     DELIMITER ;
--     
--     
--     DROP TRIGGER IF EXISTS correct_cinema_name;
-- 	DELIMITER // 
--     CREATE TRIGGER correct_cinema_name
--     BEFORE INSERT ON cinema
--     FOR EACH ROW 
-- 		BEGIN
-- 			DECLARE input_cinema_format VARCHAR(10);
-- 			SET input_cinema_format = NEW.name;
-- 			
-- 			IF NOT(input_cinema_format REGEXP '^[A-LN-Z]{2}-\d{3}-\d{2}$') THEN
-- 			SIGNAL SQLSTATE '45000'
--             SET MESSAGE_TEXT = 'Неправильний формат для стовпця your_column_name.';
-- 			END IF ;
-- 	END;
--     //
--     DELIMITER ;
--         


        
    
