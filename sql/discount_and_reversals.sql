SELECT
    "product_title",
    "product_type",
    "gross_sales",
    "discounts",
    "sales_reversed",
    "net_sales",

    ROUND(
        100.0 * "sales_reversed" / NULLIF("gross_sales", 0),
        2
    ) AS reversal_rate,

    ROUND(
        100.0 * ABS("discounts") / NULLIF("gross_sales", 0),
        2
    ) AS discount_rate

FROM sales
WHERE "gross_sales" > 0
ORDER BY discount_rate DESC;

