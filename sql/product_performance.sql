SELECT
    "product_title",
    "product_vendor",
    "product_type",
    "net_items_sold",
    "gross_sales",
    "discounts",
    "sales_reversed",
    "net_sales",
    "taxes",
    "total_sales",

    ROUND(
        100.0 * "sales_reversed" / NULLIF("gross_sales", 0),
        2
    ) AS reversal_rate,

    ROUND(
        100.0 * ABS("discounts") / NULLIF("gross_sales", 0),
        2
        ) AS discount_rate

FROM sales
ORDER BY "net_sales" DESC;
