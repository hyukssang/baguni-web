CREATE TABLE User(
	username VARCHAR(20) NOT NULL,
	firstname VARCHAR(20) NOT NULL,
	lastname VARCHAR(20) NOT NULL,
	password VARCHAR(256) NOT NULL,
	email VARCHAR(256),
	phone VARCHAR(10) NOT NULL,
	PRIMARY KEY (username)
);

CREATE TABLE Baguni(
	username VARCHAR(20),
	baguniid INTEGER NOT NULL AUTO_INCREMET,
	title VARCHAR(20),
	PRIMARY KEY (baguniid),
	FOREIGN KEY (username) REFERENCES User(username) ON DELETE CASCADE
);

CREATE TABLE BaguniAccess(
	username VARCHAR(20) NOT NULL,
	baguniid INTEGER NOT NULL,
	FOREIGN KEY (baguniid) REFERENCES Baguni(baguniid) ON DELETE CASCADE
	FOREIGN KEY (username) REFERENCES User(username) ON DELETE CASCADE
);

CREATE TABLE Item(
	baguniid INTEGER NOT NULL,
	itemid INTEGER NOT NULL AUTO_INCREMET,
	originalurl VARCHAR(256),
	imageurl VARCHAR(256),
	price DECIMAL(7,2),
	brandname VARCHAR(20),
	itemname VARCHAR(40),
	quantity TINYINT(3),
	size VARCHAR(10),
	selected TINYINT(1),
	PRIMARY KEY (itemid),
	FOREIGN KEY (baguniid) REFERENCES Baguni(baguniid) ON DELETE CASCADE
);

CREATE TABLE ItemAccess(
	baguniid INTEGER NOT NULL,
	itemid INTEGER NOT NULL,
	FOREIGN KEY (baguniid) REFERENCES Baguni(baguniid) ON DELETE CASCADE
	FOREIGN KEY (itemid) REFERENCES Item(itemid) ON DELETE CASCADE
);

