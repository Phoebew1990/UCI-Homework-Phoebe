--Drop tables
DROP TABLE IF EXISTS Dept_emp;
DROP TABLE IF EXISTS Dept_manager;
DROP TABLE IF EXISTS Salaries;
DROP TABLE IF EXISTS Titles;
DROP TABLE IF EXISTS Departments;
DROP TABLE IF EXISTS Employees;

--Create tables
CREATE TABLE Departments (
    "dept_no" Varchar   NOT NULL,
    "dept_name" Varchar   NOT NULL,
    CONSTRAINT "pk_Departments" PRIMARY KEY (
        "dept_no"
     )
);

CREATE TABLE Dept_emp (
    "emp_no" int   NOT NULL,
    "dept_no" Varchar   NOT NULL
);


CREATE TABLE Dept_manager (
    "dept_no" Varchar   NOT NULL,
    "emp_no" int   NOT NULL
);

CREATE TABLE Employees (
    "emp_no" int   NOT NULL,
    "emp_title_id" Varchar   NOT NULL,
    "birth_date" date   NOT NULL,
    "first_name" Varchar   NOT NULL,
    "last_name" Varchar   NOT NULL,
    "sex" Varchar   NOT NULL,
    "hire_date" date   NOT NULL,
    CONSTRAINT "pk_Employees" PRIMARY KEY (
        "emp_no"
     )
);



CREATE TABLE Salaries (
    "emp_no" int   NOT NULL,
    "salary" int   NOT NULL
);

CREATE TABLE Titles (
    "title_id" Varchar   NOT NULL,
    "title" Varchar   NOT NULL,
    CONSTRAINT "pk_Titles" PRIMARY KEY (
        "title_id"
     )
);

ALTER TABLE Dept_emp ADD CONSTRAINT "fk_Dept_emp_dept_no" FOREIGN KEY("dept_no")
REFERENCES Departments ("dept_no");

ALTER TABLE Dept_emp ADD CONSTRAINT "fk_Dept_emp_emp_no" FOREIGN KEY("emp_no")
REFERENCES Employees ("emp_no");

ALTER TABLE Dept_manager ADD CONSTRAINT "fk_Dept_manager_dept_no" FOREIGN KEY("dept_no")
REFERENCES Departments ("dept_no");

ALTER TABLE Dept_manager ADD CONSTRAINT "fk_Dept_manager_emp_no" FOREIGN KEY("emp_no")
REFERENCES Employees ("emp_no");

ALTER TABLE Salaries ADD CONSTRAINT "fk_Salaries_emp_no" FOREIGN KEY("emp_no")
REFERENCES Employees ("emp_no");




SELECT * FROM Departments;
--SELECT * FROM dept_emp;
--SELECT * FROM dept_manager;
--SELECT * FROM employees;
--SELECT * FROM salaries;
--SELECT * FROM titles;




