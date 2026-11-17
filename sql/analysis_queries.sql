
-- 1. View all retail market records
SELECT *
FROM palghar_retail_demo_data;

-- 2. Total estimated monthly footfall by locality
SELECT
    locality,
    SUM(estimated_monthly_footfall) AS total_footfall
FROM palghar_retail_demo_data
GROUP BY locality
ORDER BY total_footfall DESC;

-- 3. Average customer spending by locality
SELECT
    locality,
    AVG(average_spend_inr) AS avg_spending
FROM palghar_retail_demo_data
GROUP BY locality
ORDER BY avg_spending DESC;

-- 4. Estimated sales potential by locality
SELECT
    locality,
    SUM(estimated_monthly_footfall * average_spend_inr)
        AS estimated_sales_potential
FROM palghar_retail_demo_data
GROUP BY locality
ORDER BY estimated_sales_potential DESC;

-- 5. Average monthly rent by locality
SELECT
    locality,
    AVG(estimated_monthly_rent_inr) AS avg_monthly_rent
FROM palghar_retail_demo_data
GROUP BY locality
ORDER BY avg_monthly_rent;
