#DB생성
CREATE DATABASE pyweb;

USE pyweb;

SHOW TABLES;
SELECT * FROM board_board;
SELECT * FROM board_comment;
DESC board_board;
DESC board_comment;

#페이지 나누기를 위한 저장 프로시저 작성
DELIMITER $$
DROP PROCEDURE if EXISTS loopInsert$$

CREATE PROCEDURE loopInsert()
BEGIN
	DECLARE i INT DEFAULT 1;
	DELETE FROM board_board;
	while i <= 991 do
		INSERT INTO board_board (idx, writer, title, content, hit, post_date, filesize, down)
			VALUE (i, CONCAT('kim', i), CONCAT('제목', i), CONCAT('내용', i), 0, NOW(), 0, 0);
		SET i = i + 1;
	END while;
END$$
DELIMITER $$

CALL loopInsert

SELECT * FROM board_board;