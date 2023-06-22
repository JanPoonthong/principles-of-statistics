import pandas as pd
from scipy.stats import ttest_ind

data = pd.read_csv(
    r"C:\Users\User\Desktop\University\Statistics\Finals\Project.csv"
)

# Male Belgium Data
belgium_data = data[data.Country == "Belgium"]
male_belgium = belgium_data[belgium_data.Gender == "Male"]
male_belgium_avgspend = list(male_belgium["Avg_Spend"])

# Female Belgium Data
female_belgium = belgium_data[belgium_data.Gender == "Female"]
female_belgium_avgspend = list(female_belgium["Avg_Spend"])

# Belgium Data Test
alpha = 0.05
tscore, pvalue = ttest_ind(male_belgium_avgspend, female_belgium_avgspend)
print("T statistics (Belgium):", tscore)
print("P value (Belgium):", pvalue)
if pvalue < alpha:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")
print()

# -------------------------------------------------------------------------------------------

# Male Austria Data
austria_data = data[data.Country == "Austria"]
male_austria = austria_data[austria_data.Gender == "Male"]
male_austria_avgspend = list(male_austria["Avg_Spend"])

# Female Austria Data
female_austria = austria_data[austria_data.Gender == "Female"]
female_austria_avgspend = list(female_austria["Avg_Spend"])

# Austria Data Test
alpha = 0.05
tscore, pvalue = ttest_ind(male_austria_avgspend, female_austria_avgspend)
print("T statistics (Austria):", tscore)
print("P value (Austria):", pvalue)
if pvalue < alpha:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")
