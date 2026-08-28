with product_performance AS (
    SELECT
        "product_title",
        "product_type",
        "net_sales",
        "net_items_sold",

    ROUND(
        100.0 * "net_sales" /
        (SELECT SUM("net_sales") FROM sales),
        2
    ) AS revenue_share_pct,

    RANK() OVER (
        ORDER BY "net_sales" DESC
    ) AS sales_rank

    FROM sales
)

SELECT
    *,
    CASE
        WHEN sales_rank <= 10 THEN 'Top 10'
        WHEN revenue_share_pct >= 1 THEN 'Strong Performer'
        ELSE 'Lower Performer'
    END AS performance_group

FROM product_performance
ORDER BY sales_rank;