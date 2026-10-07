import pandas as pd
import sys

print(sys.executable)
print(pd.__version__)

df = pd.read_csv(
    "C:/Users/LENOVO 11E/Desktop/Chronos/Python Essentials/Projects/Employee Churn Analysis/data/Employee.csv"
)

print(df.head())
print(df.shape)
print(df.columns)
df.info()
print(df.isnull().sum())

# LeaveOrNot analysis
print(df["LeaveOrNot"].value_counts())
print(df["LeaveOrNot"].value_counts(normalize=True) * 100)

#Data types and duplicates
print("Nombre de doublons :", df.duplicated().sum())
print(df.dtypes)

print("Education :", df["Education"].unique())
print("City :", df["City"].unique())
print("Gender :", df["Gender"].unique())
print("EverBenched :", df["EverBenched"].unique())

print("LeaveOrNot :", df["LeaveOrNot"].unique())

print(df.describe())

# City wise attrition
print(df.groupby("City")["LeaveOrNot"].sum())

city_attrition = pd.crosstab(
    df["City"],
    df["LeaveOrNot"],
    normalize="index"
) * 100

print(city_attrition)

# Joining year wise attrition
print(
    pd.crosstab(
        df["JoiningYear"],
        df["LeaveOrNot"]
    )
)

 #joining year wise attrition percentage
joining_year_attrition = pd.crosstab(
    df["JoiningYear"],
    df["LeaveOrNot"],
    normalize="index"
) * 100

print(joining_year_attrition)

#Attrition analysis for Pune city
pune_departures = df[
    (df["City"] == "Pune") &
    (df["LeaveOrNot"] == 1)
]

print(pune_departures["JoiningYear"].value_counts().sort_index())

#Age analysis grouping
print(df["Age"].describe())

print(df["Age"].value_counts().sort_index())

bins = [0, 25, 35, 45, 55, 100]

labels = [
    "<25",
    "25-34",
    "35-44",
    "45-54",
    "55+"
]

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)

#Age group wise attrition
print(df[["Age", "AgeGroup"]].head(20))

print(df["AgeGroup"].value_counts().sort_index())

#Age group wise attrition percentage
age_attrition = pd.crosstab(
    df["AgeGroup"],
    df["LeaveOrNot"],
    normalize="index"
) * 100

print(age_attrition)

#Experience in current domain analysis
print(df["ExperienceInCurrentDomain"].describe())

#Experience in current domain wise attrition
print(
    pd.crosstab(
        df["AgeGroup"],
        df["ExperienceInCurrentDomain"]
    )
)

#Experience in current domain wise attrition percentage
print( df.groupby("AgeGroup")["ExperienceInCurrentDomain"].mean())

#Experience in current domain and attrition analysis
print(
    df.groupby("AgeGroup")[
        ["ExperienceInCurrentDomain", "LeaveOrNot"]
    ].mean()
)

#Age group and joining year wise attrition percentage
print(
    pd.crosstab(
        df["AgeGroup"],
        df["JoiningYear"],
        values=df["LeaveOrNot"],
        aggfunc="mean"
    ) * 100
)

#Attrition analysis for young employees who joined in 2017 and 2018
young_2017_2018 = df[
    (df["Age"] < 25) &
    (df["JoiningYear"].isin([2017, 2018]))
]

print(young_2017_2018.shape)

print(
    young_2017_2018["LeaveOrNot"].value_counts()
)

print(
    young_2017_2018["LeaveOrNot"].value_counts(normalize=True) * 100
)

#Attrition analysis for young employees who joined in 2017 and 2018 grouped by joining year
print(
    young_2017_2018.groupby("JoiningYear")["LeaveOrNot"].agg(
        ["count", "sum", "mean"]
    )
)

#Attrition analysis for young employees who joined in 2017 and 2018 grouped by joining year and age group
print(
    df[df["JoiningYear"] == 2018][
        ["Age", "AgeGroup", "ExperienceInCurrentDomain", "Gender", "Education", "City", "LeaveOrNot"]
    ]
)

#Age group wise attrition analysis for employees who joined in 2018
print(df[df["JoiningYear"] == 2018]["AgeGroup"].value_counts())

#Age group wise attrition analysis for employees who joined in 2018
print(
    df[df["JoiningYear"] == 2018]
    .groupby("AgeGroup")["LeaveOrNot"]
    .agg(["count", "sum", "mean"])
)

#Joining year wise attrition analysis
print(df["JoiningYear"].value_counts().sort_index())

#Joining year wise attrition analysis for employees who joined in 2018
print(
    df[df["JoiningYear"] == 2018]
    .shape
)

#Attrition analysis for employees who joined in 2018
print(
    df[df["JoiningYear"] == 2018]["LeaveOrNot"]
    .value_counts()
)

#Attrition analysis for employees who joined in 2018 normalized
print(
    df[df["JoiningYear"] == 2018]["LeaveOrNot"]
    .value_counts(normalize=True) * 100
)

#Joining year wise attrition analysis
joining_analysis = df.groupby("JoiningYear")["LeaveOrNot"].agg(
    Effectif="count",
    Départs="sum",
    Taux_depart="mean"
)

joining_analysis["Taux_depart"] *= 100

print(joining_analysis)

#Education wise attrition analysis
print(df["Education"].value_counts())
print(df["Education"].unique())

print(
    df.groupby("Education")["LeaveOrNot"].agg(
        Effectif="count",
        Départs="sum",
        Taux_depart="mean"
    )
)

education_analysis = df.groupby("Education")["LeaveOrNot"].agg(
    Effectif="count",
    Départs="sum",
    Taux_depart="mean"
)

education_analysis["Taux_depart"] *= 100

print(education_analysis)

#Education wise attrition analysis for employees who joined in 2018
education_year = pd.crosstab(
    df["Education"],
    df["JoiningYear"],
    values=df["LeaveOrNot"],
    aggfunc="mean"
) * 100

print(education_year)

#Education wise attrition analysis for employees who joined in 2018
print(
    df[df["JoiningYear"] == 2018]
    .groupby("Education")["LeaveOrNot"]
    .agg(
        Effectif="count",
        Départs="sum",
        Taux_depart="mean"
    )
)

#Education wise attrition analysis for employees who joined in 2018 in percentage
education_2018 = (
    df[df["JoiningYear"] == 2018]
    .groupby("Education")["LeaveOrNot"]
    .agg(
        Effectif="count",
        Départs="sum",
        Taux_depart="mean"
    )
)

education_2018["Taux_depart"] *= 100

print(education_2018)

#Experience in current domain analysis
print(df["ExperienceInCurrentDomain"].describe())

#Experience in current domain wise attrition analysis
print(df["ExperienceInCurrentDomain"].value_counts().sort_index())

#Experience in current domain wise attrition analysis
experience_analysis = df.groupby("ExperienceInCurrentDomain")["LeaveOrNot"].agg(
    Effectif="count",
    Départs="sum",
    Taux_depart="mean"
)

experience_analysis["Taux_depart"] *= 100

print(experience_analysis)

#Experience in current domain wise attrition analysis for employees who joined in 2018
experience_2018 = (
    df[df["JoiningYear"] == 2018]
    .groupby("ExperienceInCurrentDomain")["LeaveOrNot"]
    .agg(
        Effectif="count",
        Départs="sum",
        Taux_depart="mean"
    )
)

experience_2018["Taux_depart"] *= 100

print(experience_2018)

#Gender wise attrition analysis
gender_analysis = df.groupby("Gender")["LeaveOrNot"].agg(
    Effectif="count",
    Départs="sum",
    Taux_depart="mean"
)

gender_analysis["Taux_depart"] *= 100

print(gender_analysis)

#Gender wise attrition analysis for employees who joined in 2018
gender_2018 = (
    df[df["JoiningYear"] == 2018]
    .groupby("Gender")["LeaveOrNot"]
    .agg(
        Effectif="count",
        Départs="sum",
        Taux_depart="mean"
    )
)

gender_2018["Taux_depart"] *= 100

print(gender_2018)


print(experience_analysis)