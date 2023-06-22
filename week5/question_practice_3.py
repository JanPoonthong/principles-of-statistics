from statsmodels.stats.proportion import proportion_confint

interval = proportion_confint(280, 400, method="normal")
print(interval)

interval = proportion_confint(410, 1000, method="normal")
print(interval)

interval = proportion_confint(590, 1000, method="normal")
print(interval)
