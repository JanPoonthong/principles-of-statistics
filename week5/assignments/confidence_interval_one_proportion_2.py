from statsmodels.stats.proportion import proportion_confint

# a
interval = proportion_confint(142, 400, method="normal")
print(interval)

# b
interval = proportion_confint(122, 500, method="normal")
print(interval)
