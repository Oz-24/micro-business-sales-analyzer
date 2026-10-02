import os
import numpy as np
import pandas as pd


def generate_raw_sales_data(filename="data/sales_ledger.csv"):
    """Simulates a realistic micro-commerce transaction ledger."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Set seed for reproducible matrix data generation
    np.random.seed(24)

    items = [
        "Hero",
        "Fanta",
        "Meat Pie",
        "Life",
        "Jameson",
        "Aquarafa",
        "Castilo",
        "Eva",
        "Fish Roll",
        "Sprite",
    ]

    categories = [
        "Bear",
        "Soda",
        "Snacks",
        "Bear",
        "Vodka",
        "Yorgut",
        "Vodka",
        "Water",
        "Snacks",
        "Soda",
    ]

    # Generate random selling prices between £15 and £120
    selling_prices = np.random.randint(15, 121, size=len(items)).astype(float)

    # Generate standard shipping costs between £3 and £8
    shipping_costs = np.random.randint(3, 9, size=len(items)).astype(float)

    # Introduce missing data: 2 items have missing shipping records (forgot to log them)
    shipping_costs[2] = np.nan
    shipping_costs[6] = np.nan

    # Build structural data frame
    df = pd.DataFrame(
        {
            "Item_Name": items,
            "Category": categories,
            "Selling_Price": selling_prices,
            "Shipping_Cost": shipping_costs,
        }
    )

    df.to_csv(filename, index=False)
    print(f"Raw transaction ledger saved to: {filename}")


def analyze_business_performance(filename="data/sales_ledger.csv"):
    """Ingests data, completes empty arrays, and runs optimized scalar calculations."""
    # 1. Pandas: Ingest raw matrix records
    df = pd.read_csv(filename)

    # 2. Pandas: Impute Missing Data
    # Fallback to the median shipping cost for transactions with missing records
    median_shipping = df["Shipping_Cost"].median()
    df["Shipping_Cost"] = df["Shipping_Cost"].fillna(median_shipping)

    # 3. NumPy: Vectorized Financial Modeling
    # Assume platform takes a flat 10% fee on Selling Price.
    # Convert series to NumPy arrays to process as an algebraic vector.
    prices = df["Selling_Price"].to_numpy()
    shipping = df["Shipping_Cost"].to_numpy()

    platform_fee_rate = 0.10

    # Calculate net profit array using element-wise vector arithmetic
    net_profits = prices - (prices * platform_fee_rate) - shipping
    df["Net_Profit"] = net_profits

    # Calculate individual margin percentages using array broadcasting
    df["Profit_Margin_Pct"] = (net_profits / prices) * 100

    # 4. NumPy: Summary Evaluation Statistics
    portfolio_metrics = {
        "Total Revenue Generated": np.sum(prices),
        "Total Net Profit": np.sum(net_profits),
        "Average Profit Margin per Sale": np.mean(df["Profit_Margin_Pct"].to_numpy()),
    }

    # 5. Pandas: Structural Categorical Splits
    # Group by category to find average profit per product type
    category_summary = df.groupby("Category")["Net_Profit"].mean().to_dict()

    return df, portfolio_metrics, category_summary


if __name__ == "__main__":
    # Execute data engineering pipeline
    generate_raw_sales_data()
    processed_df, summary_stats, cat_splits = analyze_business_performance()

    print("\n--- PROCESSED COMMERCE METRICS ---")
    print(
        processed_df[
            [
                "Item_Name",
                "Category",
                "Selling_Price",
                "Shipping_Cost",
                "Net_Profit",
                "Profit_Margin_Pct",
            ]
        ]
    )

    print("\n--- PORTFOLIO TOTALS ---")
    for key, val in summary_stats.items():
        print(f"{key}: £{val:.2f}" if "Margin" not in key else f"{key}: {val:.2f}%")

    print("\n--- AVG NET PROFIT BY PRODUCT CATEGORY ---")
    for category, profit in cat_splits.items():
        print(f"{category}: £{profit:.2f}")
