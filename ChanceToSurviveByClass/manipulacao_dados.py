import pandas as pd

df = pd.read_csv("titanic_survival.csv")

# Calcula a média de idade por classe de passageiro
survive_by_class = df.groupby('pclass')['survived'].mean() * 100


data = {
    "pclass": survive_by_class.index.tolist(),
    "survival_rate": survive_by_class.values.tolist()
}


df_attr = pd.DataFrame(data)
print(df_attr.to_string(index=False))
df_attr.to_csv("survival_rate_by_class.csv", index=False)