USE job_tracker;

-- Run once on an existing database before using the Job Match feature.
ALTER TABLE jobs
ADD COLUMN required_skills TEXT AFTER job_description;
