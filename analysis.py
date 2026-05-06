import pandas as pd
df=pd.read_csv("gene analysis.csv")
df.columns=df.columns.str.strip()
print(df)
#so we have BRCA1 TP53 EGFR and MYC genes in gene column, healthy and disease conditions in condition column and values in expression column
print(df.groupby("gene")["condition"].sum())
print(df.groupby(["gene", "condition"])["expression"].mean())
#how risky is these expressions
df["risk_level"]=pd.qcut(df["expression"], q=3, labels=["low","medium", "high"])
print(df["risk_level"])

#pivot table

pivot=df.pivot(
index="gene",
columns="condition",
values="expression"
)
pivot["difference"]=pivot["healthy"]-pivot["disease"]
#difference is negative because these genes are apparently more diseased than healthy
print(pivot["difference"].sort_values(ascending= False))8
