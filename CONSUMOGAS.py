df=[]
import pandas as pd
df = pd.read_excel("ConsumoGasolina.xlsx")

print(df)

print(df["Modelo"].mean())
print(df["Potencia(HP)"].max())
print(df["R. Comb.(kh/l)"].min())
print(df["R. Comb. (km/l)"].describe())
print(df[df["Modelo"]>2015])