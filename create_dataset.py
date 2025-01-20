import numpy as np
import pandas as pd

# Parameters for the new dataset
start_year = 2018
end_year = 2023
date_range = pd.date_range(start=f"{start_year}-01-01", end=f"{end_year}-12-31", freq='D')

# Simulate seasonal revenue patterns with annual growth
np.random.seed(42)  # For reproducibility
seasonal_pattern = np.sin(2 * np.pi * date_range.dayofyear / 365) * 1000  # Seasonal fluctuation
yearly_growth = (date_range.year - start_year + 1) * 200  # Revenue grows by $200 per year
base_revenue = 3000 + yearly_growth + seasonal_pattern  # Base revenue

# Add random noise to simulate real-world variations
noise = np.random.normal(0, 200, len(date_range))
# Correct the clipping issue
revenue = np.maximum(base_revenue + noise, 1000)  # Ensure no negative revenue

# Generate monthly discount and coupon rates
monthly_discount_rate = {
    month: np.round(np.random.uniform(0.05, 0.5), 4) for month in range(1, 13)
}
discount_rate = [monthly_discount_rate[date.month] for date in date_range]

monthly_coupon_rate = {
    month: np.round(np.random.uniform(0.02, 0.2), 4) for month in range(1, 13)
}
coupon_rate = [monthly_coupon_rate[date.month] for date in date_range]

# Create the DataFrame
time_series_practice_data = pd.DataFrame({
    'date': date_range,
    'revenue': revenue.astype(int),  # Integer revenue for practical analysis
    'discount_rate': discount_rate,
    'coupon_rate': coupon_rate
})

# # Save the dataset to a CSV file
practice_file_path = "daily_revenue.csv"
time_series_practice_data.to_csv(practice_file_path, index=False)
