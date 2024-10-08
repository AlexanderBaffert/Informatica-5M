-- Every invoice
SELECT * FROM invoices;

-- Every invoice ordered by total invoice amount ("total")
SELECT * FROM invoices ORDER BY total DESC;

-- Every invoice with a total greater than 10
SELECT * FROM invoices WHERE total > 10;

-- The 10 most expensive invoices
SELECT * FROM invoices ORDER BY total DESC LIMIT 10;

-- The 15 most recent invoices
SELECT * FROM invoices ORDER BY invoice_date DESC LIMIT 15;

-- The 15 oldest invoices
SELECT * FROM invoices ORDER BY invoice_date LIMIT 15;

-- The 10 most expensive invoices from the US
SELECT * FROM invoices WHERE billing_country = "USA" ORDER BY total DESC LIMIT 10;

-- The 10 least expensive invoices from the US
SELECT * FROM invoices WHERE billing_country = "USA" ORDER BY total LIMIT 10;

-- The 10 most expensive invoices from outside the US
SELECT * FROM invoices WHERE billing_country != "USA" ORDER BY total DESC LIMIT 10;

-- A list of all the invoices worth more than $5.00 from Chicago, IL
SELECT * FROM invoices WHERE billing_city = "Chicago" AND billing_state = "IL" AND billing_country = "USA" AND total > 5;

-- The billing addresses of the 5 most valuable invoices from Mountain View CA
SELECT billing_address, billing_city, billing_state, billing_country FROM invoices WHERE billing_city = "Mountain View" AND billing_state = "CA" ORDER BY total DESC LIMIT 5;

-- A list of the 10 most valuable invoices made before January 1st, 2010
SELECT * FROM invoices WHERE invoice_date < "2010-01-01" ORDER BY total DESC LIMIT 10;

-- A list of the top 5 countries by number of invoices 
SELECT billing_country, COUNT(*) FROM invoices GROUP BY billing_country ORDER BY COUNT(*) DESC LIMIT 5;

-- A list of the top 5 countries by gross/total invoice size
SELECT billing_country, SUM(total) FROM invoices GROUP BY billing_country ORDER BY SUM(total) DESC LIMIT 5;

-- A lisst of the top 5 countries by average invoice size
SELECT billing_country, AVG(total) FROM invoices GROUP BY billing_country ORDER BY AVG(total) DESC LIMIT 5;
