use iot_db;

-- Значення певного стовпця не може закінчувати двома нулями
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


-- Заборонити видалення стрічок з таблиці
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


-- Додати до БД 1 додаткову довільну таблицю і зв’язати з іншою існуючою таблицею зв’язком  1:M.
-- Однак для забезпечення цілісності значень використати тригери замість фізичного зовнішнього ключа.
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



-- Створити пакет, який вставляє 10 стрічок у довільну таблицю БД у форматі < Noname+№> , наприклад: Noname5, Noname6, Noname7 і т.д.
DROP PROCEDURE IF EXISTS InsertRows;
DELIMITER //
CREATE PROCEDURE InsertRows()
BEGIN
  DECLARE i INT DEFAULT 396;
  WHILE i <= 406 DO
    INSERT INTO film (name) VALUES (CONCAT('Film', i));
    SET i = i + 1;
  END WHILE;
END;
// DELIMITER ;

CALL InsertRows();



-- Написати користувацьку функцію, яка буде шукати Max, Min, Sum чи Avg для стовпця довільної таблиці у БД.
-- Написати процедуру, яка буде у SELECT викликати цю функцію.
DROP FUNCTION IF EXISTS GetMaxRating;
DELIMITER //
CREATE FUNCTION GetMaxRating()
RETURNS DECIMAL(5,2)
DETERMINISTIC
BEGIN
    DECLARE max_score DECIMAL(5,2);
    SELECT MAX(score) INTO max_score FROM rating;
    RETURN max_score;
END ;
// DELIMITER ;

DROP PROCEDURE IF EXISTS CallGetMaxRating;
DELIMITER //
CREATE PROCEDURE CallGetMaxRating()
BEGIN
    DECLARE max_result DECIMAL(5,2);
    SET max_result = GetMaxRating();
    SELECT CONCAT('The maximum score is: ', max_result) AS Result;
END;
// DELIMITER ;

CALL CallGetMaxRating();






-- Забезпечити параметризовану вставку нових значень у довільну таблицю.
DROP PROCEDURE IF EXISTS insert_box_office_fees;
DELIMITER //
CREATE PROCEDURE insert_box_office_fees(
  IN revenu Float(12,2)
)
BEGIN
  INSERT INTO box_office_fees(revenu)VALUES
  (revenu);
END ;
// DELIMITER ;

CALL insert_box_office_fees(32456732);



DROP PROCEDURE IF EXISTS Cursor1;
DELIMITER //
CREATE PROCEDURE Cursor1()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE NameT CHAR(25);
    DECLARE Cursor10 CURSOR FOR SELECT name FROM viewer WHERE name IS NOT NULL;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN Cursor10;

    myLoop: LOOP
        FETCH Cursor10 INTO NameT;

        IF done = TRUE THEN
            LEAVE myLoop;
        END IF;

        SET @temp_query = CONCAT('CREATE DATABASE IF NOT EXISTS ', NameT);
        PREPARE myquery FROM @temp_query;
        EXECUTE myquery;
        DEALLOCATE PREPARE myquery;
    END LOOP;

    CLOSE Cursor10;
END //
DELIMITER ;

CALL Cursor1();

DELIMITER //
CREATE PROCEDURE InsertRandomTables()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE NameT CHAR(25);
    DECLARE i INT;
    DECLARE tableName CHAR(25);
    DECLARE Cursor10 CURSOR FOR SELECT name FROM viewer WHERE name IS NOT NULL;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN Cursor10;

    myLoop: LOOP
        FETCH Cursor10 INTO NameT;

        IF done = TRUE THEN
            LEAVE myLoop;
        END IF;

        SET i = FLOOR(1 + RAND() * 9);

        WHILE i > 0 DO
            SET tableName = CONCAT(NameT, '_', i);
            SET @temp_query = CONCAT('CREATE TABLE IF NOT EXISTS ', NameT, '.', tableName, ' (id INT)');

            PREPARE myquery FROM @temp_query;
            EXECUTE myquery;
            DEALLOCATE PREPARE myquery;

            SET i = i - 1;
        END WHILE;
    END LOOP;

    CLOSE Cursor10;
END //
DELIMITER ;

CALL InsertRandomTables();










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


        
    
