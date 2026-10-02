# Micro-Business Sales & Profit Margin Analyzer

A lightweight financial data cleaning and ledger analytics script built using Python, Pandas, and NumPy. This repository functions as a technical portfolio project demonstrating fundamental data engineering workflows.

## 📈 Project Motivation
In micro-commerce platforms (such as Depop, Vinted, or eBay), raw sales values often mask true operational profitability due to varying shipping overheads and scaling platform fees. This program ingests flat-file transaction data, executes statistical median data imputation for missing expense logs, and utilizes vectorized matrix algorithms to compute localized product margins and financial metrics.

## 🛠️ Core Analytical Operations

### 1. Element-Wise Vector Arithmetic
Rather than processing sales entries through computational iteration loops, transactions are extracted into linear NumPy arrays. Deductions for platform margins (10%) and distribution overheads are resolved simultaneously across entire arrays using vectorized arithmetic primitives:
⁠ python
prices = df['Selling_Price'].to_numpy()
shipping = df['Shipping_Cost'].to_numpy()
net_profits = prices - (prices * 0.10) - shipping
 ⁠

### 2. Median Value Data Imputation
Real-world tracking structures frequently contain unrecorded fields. This pipeline handles missing values (⁠ NaN ⁠) within shipping inputs by replacing them with the column's statistical median, stabilizing computational arrays before downstream vector logic occurs:
⁠ python
df['Shipping_Cost'] = df['Shipping_Cost'].fillna(df['Shipping_Cost'].median())
 ⁠
### 3. Structural Segment Clustering
By combining Pandas categorical structures (⁠ .groupby() ⁠) with foundational evaluation tools, the ledger groups net metrics by item segment. This extracts high-level strategic intelligence regarding which product verticals offer optimal returns.

## 🚀 Deployment Instructions

1.⁠ ⁠Clone the project locally:
   ⁠ bash
   git clone https://github.com
   cd micro-business-sales-analyzer
    ⁠

2.⁠ ⁠Run the main evaluation pipeline script:
   ⁠ bash
   python src/sales_analyzer.py
    ⁠

## 📊 Summary Outputs
When run, the application transforms raw rows into specific financial evaluations printed to the terminal console:
•⁠  ⁠*Total Portfolio Revenue*: Total cash intake values (£)
•⁠  ⁠*True Operational Net Profit*: Yield after variable platform and logistics subtractions (£)
•⁠  ⁠*Categorical Breakdown*: Identification of individual category profitability performance
