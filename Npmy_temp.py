import statistics

temp_week = [22.5, 24.3, 19.8, 23.7, 21.2, 22.1, 20.5]

mean_temp = statistics.mean(temp_week)
median_temp = statistics.median(temp_week)
variance_temp = statistics.variance(temp_week)
std_dev_temp = statistics.stdev(temp_week)

print(f"Temperatures: {temp_week}")
print(f"Mean Temperature: {mean_temp:.2f}°C")
print(f"Median Temperature: {median_temp:.2f}°C")
print(f"Variance of Temperature: {variance_temp:.2f}")
print(f"Standard Deviation of Temperature: {std_dev_temp:.2f}")
