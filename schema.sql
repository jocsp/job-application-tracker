CREATE DATABASE IF NOT EXISTS job_tracker;

USE job_tracker;

CREATE TABLE companies (
    company_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    industry VARCHAR(50),
    website VARCHAR(200),
    city VARCHAR(50),
    state VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE jobs (
    job_id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT NOT NULL,
    job_title VARCHAR(100) NOT NULL,
    job_description TEXT,
    required_skills TEXT,
    salary_min DECIMAL(10,2),
    salary_max DECIMAL(10,2),
    job_type VARCHAR(20),
    posting_url VARCHAR(500),
    date_posted DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id)
        REFERENCES companies(company_id)
);

CREATE TABLE applications (
    application_id INT AUTO_INCREMENT PRIMARY KEY,
    job_id INT NOT NULL,
    application_date DATE NOT NULL,
    status VARCHAR(30) DEFAULT 'Applied',
    resume_version VARCHAR(50),
    cover_letter_sent BOOLEAN DEFAULT FALSE,
    response_date DATE,
    interview_date DATETIME,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (job_id)
        REFERENCES jobs(job_id)
);

CREATE TABLE contacts (
    contact_id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    job_title VARCHAR(100),
    linkedin_url VARCHAR(200),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id)
        REFERENCES companies(company_id)
);

CREATE INDEX idx_job_title
ON jobs(job_title);

CREATE INDEX idx_company_type
ON jobs(company_id, job_type);

CREATE INDEX idx_app_status
ON applications(status);

CREATE INDEX idx_company_industry
ON companies(industry);
