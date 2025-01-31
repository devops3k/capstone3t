-- Create 'persons' table (if you haven't let JPA create it automatically)
CREATE TABLE IF NOT EXISTS persons (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

-- Insert some sample data
INSERT INTO persons (first_name, last_name) VALUES
('John', 'Doe'),
('Jane', 'Smith'),
('Alice', 'Wonderland');
