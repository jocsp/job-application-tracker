
USE job_tracker;

START TRANSACTION;

INSERT INTO companies (company_name, industry, website, city, state)
VALUES
('Tech Solutions Inc', 'Technology', 'www.techsolutions.com',
'Miami', 'Florida'),
('Data Analytics Corp', 'Data Science', 'www.dataanalytics.com',
'Austin', 'Texas'),
('Cloud Systems LLC', 'Cloud Computing', 'www.cloudsystems.com',
'Seattle', 'Washington'),
('Digital Innovations', 'Software', 'www.digitalinnovations.com',
'San Francisco', 'California'),
('Smart Tech Group', 'AI/ML', 'www.smarttech.com', 'Boston',
'Massachusetts');

INSERT INTO jobs (company_id, job_title, required_skills, salary_min,
salary_max, job_type, date_posted) VALUES
(1, 'Software Developer', 'Python, SQL, Flask, Git', 70000, 90000, 'Full-time', '2025-01-15'),
(1, 'Database Administrator', 'SQL, MySQL, Linux, Database Design', 75000, 95000, 'Full-time', '2025-01-10'),
(2, 'Data Analyst', 'SQL, Python, Excel, Tableau', 65000, 85000, 'Full-time', '2025-01-12'),
(3, 'Cloud Engineer', 'AWS, Linux, Docker, Python, Networking', 80000, 100000, 'Full-time', '2025-01-08'),
(4, 'Junior Developer', 'Python, JavaScript, Git, REST APIs', 55000, 70000, 'Full-time', '2025-01-14'),
(4, 'Senior Developer', 'Python, Java, SQL, System Design', 95000, 120000, 'Full-time', '2025-01-14'),
(5, 'ML Engineer', 'Python, Machine Learning, TensorFlow, SQL', 90000, 115000, 'Full-time', '2025-01-11');

INSERT INTO applications (job_id, application_date, status,
resume_version, cover_letter_sent) VALUES
(1, '2025-01-16', 'Applied', 'v2.1', TRUE),
(3, '2025-01-13', 'Screening', 'v2.1', TRUE),
(4, '2025-01-09', 'Rejected', 'v2.0', FALSE),
(5, '2025-01-15', 'Applied', 'v2.1', TRUE),
(7, '2025-01-12', 'Screening', 'v2.1', TRUE);

INSERT INTO contacts
(company_id, first_name, last_name, email, job_title)
VALUES
(1, 'Sarah', 'Johnson', 'sjohnson@techsolutions.com', 'HR Manager'),
(2, 'Michael', 'Chen', 'mchen@dataanalytics.com', 'Technical Recruiter'),
(3, 'Emily', 'Williams', 'ewilliams@cloudsystems.com', 'Hiring Manager'),
(4, 'David', 'Brown', NULL, 'Senior Developer'),
(5, 'Lisa', 'Garcia', 'lgarcia@smarttech.com', 'Talent Acquisition');

UPDATE applications
SET status = 'Interview'
WHERE application_id = 3;

INSERT INTO jobs (company_id, job_title, required_skills, salary_min,
salary_max, job_type, date_posted) VALUES
(1, 'QA Engineer', 'Python, Selenium, API Testing, Git', 60000, 80000, 'Full-time', '2025-01-05'),
(2, 'Business Analyst', 'SQL, Excel, Tableau, Requirements Analysis', 65000, 85000, 'Full-time', '2025-01-06'),
(2, 'Data Scientist', 'Python, SQL, Machine Learning, Statistics', 85000, 110000, 'Full-time', '2025-01-07'),
(3, 'DevOps Engineer', 'Linux, Docker, Kubernetes, AWS, CI/CD', 80000, 105000, 'Full-time', '2025-01-08'),
(3, 'Security Analyst', 'Linux, Network Security, Python, SIEM', 75000, 95000, 'Full-time', '2025-01-09'),
(4, 'UI/UX Designer', 'Figma, Wireframing, Prototyping, User Research', 60000, 80000, 'Full-time', '2025-01-10'),
(5, 'Product Manager', 'Agile, Communication, Roadmapping, SQL', 90000, 120000, 'Full-time', '2025-01-11'),
(1, 'Technical Writer', 'Technical Writing, Markdown, API Documentation, Git', 55000, 75000, 'Contract', '2025-01-12'),
(2, 'Intern - Data', 'Python, SQL, Excel, Statistics', 30000, 40000, 'Internship', '2025-01-13'),
(4, 'Intern - Development', 'Python, JavaScript, Git, HTML/CSS', 32000, 42000, 'Internship', '2025-01-14');

UPDATE applications
SET status = 'Interview'
WHERE application_id = 2;

INSERT INTO companies (company_name, industry, city, state)
VALUES ('New Tech Corp', 'Technology', 'Denver', 'Colorado');

INSERT INTO jobs (company_id, job_title, required_skills, salary_min,
salary_max, job_type)
VALUES (
    (SELECT company_id FROM companies
     WHERE company_name = 'New Tech Corp'),
    'Software Architect', 'Python, Java, System Design, AWS, Microservices',
    120000, 150000, 'Full-time'
);

INSERT INTO applications (job_id, application_date, status,
resume_version, cover_letter_sent)
VALUES (6, CURDATE(), 'Applied', 'v3.0', TRUE);

UPDATE companies
SET notes = CONCAT('Applied to Senior Developer position on ', CURDATE())
WHERE company_id = 4;


INSERT INTO contacts
(company_id, first_name, last_name, email, job_title)
VALUES (4, 'Robert', 'Kim', 'rkim@digitalinnovations.com',
'Engineering Manager');

UPDATE applications
SET status = 'Offer'
WHERE application_id = 1;

COMMIT;
