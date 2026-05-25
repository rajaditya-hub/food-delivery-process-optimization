/* =========================================================
   FOOD DELIVERY PROCESS OPTIMIZATION — BUSINESS SQL ANALYSIS
   ========================================================= */


/* =========================================================
   1. OVERALL DELIVERY PERFORMANCE
   ========================================================= */

SELECT 
    AVG(delivery_time_min) AS avg_delivery_time
FROM final_zomato_dataset;

/*
Insight:
The average delivery time provides a high-level overview of operational efficiency.
This KPI helps evaluate how effectively the delivery network performs across all orders.
A consistently lower delivery time generally indicates better logistics coordination
and improved customer experience.
*/


/* =========================================================
   2. TRAFFIC DENSITY IMPACT ON DELIVERY TIME
   ========================================================= */

SELECT 
    traffic_density,
    AVG(delivery_time_min) AS avg_delivery_time
FROM final_zomato_dataset
GROUP BY traffic_density
ORDER BY avg_delivery_time DESC;

/*
Insight:
This analysis highlights how traffic conditions influence delivery performance.
Higher traffic density is directly associated with increased delivery delays.
The results can help optimize rider allocation and route planning during peak hours.
*/


/* =========================================================
   3. WEATHER IMPACT ANALYSIS
   ========================================================= */

SELECT 
    weather,
    AVG(delivery_time_min) AS avg_delivery_time
FROM final_zomato_dataset
GROUP BY weather
ORDER BY avg_delivery_time DESC;

/*
Insight:
Weather conditions significantly affect delivery operations.
Extreme weather scenarios such as storms or fog tend to increase delivery duration.
This insight can support operational planning during adverse environmental conditions.
*/


/* =========================================================
   4. CITY-WISE DELIVERY PERFORMANCE
   ========================================================= */

SELECT 
    city,
    AVG(delivery_time_min) AS avg_delivery_time
FROM final_zomato_dataset
GROUP BY city
ORDER BY avg_delivery_time DESC;

/*
Insight:
This query identifies cities with relatively slower delivery performance.
The analysis helps detect operational bottlenecks and region-specific inefficiencies.
Such insights can support better city-level logistics optimization strategies.
*/


/* =========================================================
   5. VEHICLE PERFORMANCE ANALYSIS
   ========================================================= */

SELECT 
    vehicle_type,
    AVG(delivery_time_min) AS avg_delivery_time
FROM final_zomato_dataset
GROUP BY vehicle_type
ORDER BY avg_delivery_time;

/*
Insight:
Different vehicle types contribute differently to delivery efficiency.
This analysis helps identify the most effective delivery vehicle for faster order fulfillment.
The findings can support fleet optimization and operational decision-making.
*/


/* =========================================================
   6. DELAYED DELIVERY ANALYSIS
   ========================================================= */

SELECT 
    city,
    COUNT(*) AS delayed_orders
FROM final_zomato_dataset
WHERE delivery_time_min > 40
GROUP BY city
ORDER BY delayed_orders DESC;

/*
Insight:
This query identifies cities experiencing the highest number of delayed deliveries.
The results help pinpoint operationally challenging regions that may require
additional delivery resources or process improvements.
*/


/* =========================================================
   7. PEAK ORDER HOUR ANALYSIS
   ========================================================= */

SELECT 
    HOUR(order_time) AS order_hour,
    COUNT(*) AS total_orders
FROM final_zomato_dataset
GROUP BY order_hour
ORDER BY total_orders DESC;

/*
Insight:
This analysis identifies peak customer ordering hours across the platform.
Understanding demand patterns can help optimize rider scheduling,
resource planning, and delivery allocation during high-volume periods.
*/


/* =========================================================
   8. MULTIPLE DELIVERY IMPACT
   ========================================================= */

SELECT 
    multiple_deliveries,
    AVG(delivery_time_min) AS avg_delivery_time
FROM final_zomato_dataset
GROUP BY multiple_deliveries
ORDER BY avg_delivery_time DESC;

/*
Insight:
Handling multiple deliveries within a single trip may impact delivery efficiency.
This analysis helps evaluate whether batch deliveries improve operational productivity
or contribute to longer customer waiting times.
*/


/* =========================================================
   9. VEHICLE CONDITION ANALYSIS
   ========================================================= */

SELECT 
    vehicle_condition,
    AVG(delivery_time_min) AS avg_delivery_time
FROM final_zomato_dataset
GROUP BY vehicle_condition
ORDER BY avg_delivery_time DESC;

/*
Insight:
Vehicle condition plays an important role in delivery efficiency.
Poor vehicle conditions may contribute to increased delivery delays
and operational inefficiencies across the fleet.
*/


/* =========================================================
   10. DELIVERY CATEGORY DISTRIBUTION
   ========================================================= */

SELECT 
    CASE
        WHEN delivery_time_min <= 20 THEN 'Fast'
        WHEN delivery_time_min <= 40 THEN 'Moderate'
        ELSE 'Delayed'
    END AS delivery_status,

    COUNT(*) AS total_orders

FROM final_zomato_dataset

GROUP BY delivery_status;

/*
Insight:
This query segments deliveries into Fast, Moderate, and Delayed categories.
It provides a simplified overview of service quality and operational consistency.
The results help evaluate customer experience performance across the platform.
*/


/* =========================================================
   11. HIGH-RATED RIDER PERFORMANCE
   ========================================================= */

SELECT 
    AVG(delivery_time_min) AS avg_delivery_time,
    AVG(rider_rating) AS avg_rider_rating
FROM final_zomato_dataset
WHERE rider_rating >= 4.5;

/*
Insight:
This analysis evaluates the relationship between rider ratings
and delivery efficiency.
The findings may help determine whether highly rated riders
consistently contribute to improved operational performance.
*/


/* =========================================================
   12. FESTIVAL IMPACT ON OPERATIONS
   ========================================================= */

SELECT 
    festival,
    AVG(delivery_time_min) AS avg_delivery_time
FROM final_zomato_dataset
GROUP BY festival;

/*
Insight:
Festival periods often lead to increased order volume and operational pressure.
This analysis helps understand how festival demand affects delivery efficiency
and overall logistics performance.
*/