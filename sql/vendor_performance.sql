SELECT
    "product_vendor",
    COUNT(*) AS product_count,
    SUM("net_items_sold") AS total_item_sold,
    SUM("net_sales") AS total_net_sales,
    ROUND(AVG("net_sales"), 2) AS avg_product_sales

FROM sales
GROUP BY "product_vendor"
ORDER BY total_net_sales DESC;