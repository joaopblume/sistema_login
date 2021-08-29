USE USERS;
SHOW DATABASES;

CREATE TABLE users(
	id INT NOT NULL PRIMARY KEY auto_increment,
    log VARCHAR(20) NOT NULL,
    pswd VARCHAR(20) NOT NULL
);

/* criando um usuario e senha para testes*/

INSERT INTO users(log, pswd) VALUES("joao", "123456");

SELECT * FROM users;
