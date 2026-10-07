import pandas as pd
import matplotlib.pyplot as plt


# =========================
# 1. CHARGEMENT DES DONNÉES
# =========================

df = pd.read_csv(
    "C:/Users/LENOVO 11E/Desktop/Chronos/Python Essentials/Projects/Employee Churn Analysis/data/Employee.csv"
)


# =========================
# 2. PRÉPARATION DES GROUPES
# =========================

# Groupes d'âge
bins = [0, 25, 35, 45, 55, 100]
labels = ["<25", "25-34", "35-44", "45-54", "55+"]

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)


# =========================
# 3. VISUALISATION
# =========================

# --- 3.1 Taux de départ par ville ---

city_rate = (
    df.groupby("City")["LeaveOrNot"]
    .mean()
    .sort_values(ascending=False) * 100
)

city_rate.plot(kind="bar")

plt.title("Taux de départ par ville")
plt.xlabel("Ville")
plt.ylabel("Taux de départ (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("C:/Users/LENOVO 11E/Desktop/Chronos/Python Essentials/Projects/Employee Churn Analysis/outputs/Figures/1_City_Attrition")
plt.show()


# --- 3.2 Taux de départ par groupe d'âge ---

age_rate = (
    df.groupby("AgeGroup", observed=True)["LeaveOrNot"]
    .mean()
    .sort_values(ascending=False) * 100
)

age_rate.plot(kind="bar")

plt.title("Taux de départ par groupe d'âge")
plt.xlabel("Groupe d'âge")
plt.ylabel("Taux de départ (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("C:/Users/LENOVO 11E/Desktop/Chronos/Python Essentials/Projects/Employee Churn Analysis/outputs/Figures/2_Age_group_Attrition")
plt.show()


# --- 3.3 Taux de départ par niveau d'éducation ---

education_rate = (
    df.groupby("Education")["LeaveOrNot"]
    .mean()
    .sort_values(ascending=False) * 100
)

education_rate.plot(kind="bar")

plt.title("Taux de départ par niveau d'éducation")
plt.xlabel("Niveau d'éducation")
plt.ylabel("Taux de départ (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("C:/Users/LENOVO 11E/Desktop/Chronos/Python Essentials/Projects/Employee Churn Analysis/outputs/Figures/3_Education_Attrition")
plt.show()


# --- 3.4 Taux de départ selon l'expérience ---

experience_rate = (
    df.groupby("ExperienceInCurrentDomain")["LeaveOrNot"]
    .agg(["count", "mean"])
)

# On retire les groupes avec trop peu d'observations
experience_rate = experience_rate[
    experience_rate["count"] >= 20
]

experience_rate["mean"] *= 100

experience_rate["mean"].plot(kind="bar")

plt.title("Taux de départ selon l'expérience")
plt.xlabel("Années d'expérience")
plt.ylabel("Taux de départ (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("C:/Users/LENOVO 11E/Desktop/Chronos/Python Essentials/Projects/Employee Churn Analysis/outputs/Figures/4_Experience_Attrition")
plt.show()


# --- 3.5 Taux de départ par genre ---

gender_rate = (
    df.groupby("Gender")["LeaveOrNot"]
    .mean()
    .sort_values(ascending=False) * 100
)

gender_rate.plot(kind="bar")

plt.title("Taux de départ par genre")
plt.xlabel("Genre")
plt.ylabel("Taux de départ (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("C:/Users/LENOVO 11E/Desktop/Chronos/Python Essentials/Projects/Employee Churn Analysis/outputs/Figures/5_Gender_Attrition")
plt.show()


# --- 3.6 Taux de départ selon l'année d'entrée ---

year_rate = (
    df.groupby("JoiningYear")["LeaveOrNot"]
    .mean() * 100
)

year_rate.plot(kind="bar")

plt.title("Taux de départ selon l'année d'entrée")
plt.xlabel("Année d'entrée")
plt.ylabel("Taux de départ (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("C:/Users/LENOVO 11E/Desktop/Chronos/Python Essentials/Projects/Employee Churn Analysis/outputs/Figures/6_Joining_year_Attrition")
plt.show()