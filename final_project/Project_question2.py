import pandas as pd
from scipy.stats import ttest_1samp

df = pd.read_csv(
    r"C:\Users\User\Desktop\University\Statistics\Finals\Project.csv"
)

# Austria data
austria_data = df[df.Country == "Austria"]
avg_list = list(austria_data["Avg_Spend"])
spend = 50
alpha = 0.05
tscore, pvalue = ttest_1samp(avg_list, spend)
print("T statistics (Austria):", tscore)
print("P value (Austria):", pvalue)
if pvalue < alpha:
    print("Reject Null Hypothesis")
else:
    print("Fail to reject Null Hypothesis")

print()

# ---------------------------------------------------------------------------------------

# Belgium data
belgium_data = df[df.Country == "Belgium"]
avg_list2 = list(belgium_data["Avg_Spend"])
tscore2, pvalue2 = ttest_1samp(avg_list2, spend)
print("T statistics (Belgium):", tscore2)
print("P value (Belgium):", pvalue2)
if pvalue2 < alpha:
    print("Reject Null Hypothesis")
else:
    print("Fail to reject Null Hypothesis")
