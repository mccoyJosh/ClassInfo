
CREATE TABLE company (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL
);



CREATE TABLE employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cmp_id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    dob DATE NOT NULL,
    FOREIGN KEY (cmp_id) REFERENCES company(id) -- tells db that cmp_id MUST match an existing id from company
);



INSERT INTO company VALUES (1,'Big Ads Company', '123 Advertisement Way, LA, CA');
INSERT INTO company(name,address)  VALUES ('Big Products LLC', '096 Make Money Avenue, LA, CA');

INSERT INTO employee (cmp_id, first_name, last_name, dob)
VALUES (1, 'John', 'Smith', '1/1/1999'),
       (1, 'John', 'Smith', '1/1/1999'),
       (2, 'Bingus', 'Smingus', '1/1/1999'),
       (2, 'Walter', 'Halter', '1/1/1999'),
       (1, 'Cherish', 'Clinton', '1/1/1999');


SELECT e.first_name, e.last_name FROM employee as e
    INNER JOIN company c on c.id = e.cmp_id
    WHERE c.name = 'Big Products LLC';