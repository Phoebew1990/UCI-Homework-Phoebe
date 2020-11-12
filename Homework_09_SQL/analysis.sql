--List the following details of each employee: employee number, last name, first name, sex, and salary.
Select e.emp_no,e.last_name,e.first_name,e.sex,s.salary
FROM Employees e left join Salaries s on e.emp_no = s.emp_no;

--List first name, last name, and hire date for employees who were hired in 1986.
SELECT first_name, last_name, hire_date
FROM Employees 
WHERE hire_date between '1986-01-01' and '1987-01-01';

--List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.

Select dm.dept_no, d.dept_name,dm.emp_no, e.last_name, e.first_name
FROM Dept_manager dm 
inner join Departments d on dm.dept_no = d.dept_no
inner join Employees e on dm.emp_no = e.emp_no;

--List the department of each employee with the following information: employee number, last name, first name, and department name.

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM Dept_emp dm 
inner join Employees e on e.emp_no = dm.emp_no
inner join Departments d on dm.dept_no = d.dept_no;

--List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."

SELECT first_name, last_name,sex
FROM Employees
Where first_name = 'Hercules' and last_name like 'B%';

--List all employees in the Sales department, including their employee number, last name, first name, and department name.

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM Dept_emp dm 
inner join Employees e on e.emp_no = dm.emp_no
inner join Departments d on dm.dept_no = d.dept_no
WHERE d.dept_name = 'Sales';

select distinct dept_name
from Departments;

--List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM Dept_emp dm 
inner join Employees e on e.emp_no = dm.emp_no
inner join Departments d on dm.dept_no = d.dept_no
WHERE d.dept_name in ( 'Sales','Development');

--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name

select last_name, count(emp_no)
FROM Employees
Group by last_name
Order by count(emp_no) Desc
