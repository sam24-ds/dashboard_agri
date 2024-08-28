import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# Charger les données
df = pd.read_csv("ObservationData_dghnvqe.csv")

# Dictionnaire de coordonnées 
coordinates = {
    "BENIN": [6.2322, 2.3158],  # Coordonnées du Bénin
    "ALIBORI": [11.1234, 2.5678],  # coordonnées pour Alibori
    "BANIKOARA": [10.9876, 2.1234],  # coordonnées pour Banikoara
    "GOGOUNOU": [10.5432, 1.2345],  # coordonnées pour Gogounou
    "KANDI": [10.5432, 1.2345],  # coordonnées pour Kandi
    "KARIMAMA": [10.5432, 1.2345],  # coordonnées pour Karimama
    "MALANVILLE": [10.5432, 1.2345],  # coordonnées pour Malanville
    "SEGBANA": [10.5432, 1.2345],  # coordonnées pour Segbana
    "ATACORA": [10.5432, 1.2345],  # coordonnées pour Atacora
    "BOUKOMBE": [10.5432, 1.2345],  # coordonnées pour Boukombe
    "COBLY": [10.5432, 1.2345],  # coordonnées pour Cobly
    "KEROU": [10.5432, 1.2345],  # coordonnées pour Kerou
    "KOUANDE": [10.5432, 1.2345],  # coordonnées pour Kouande
    "MATERI": [10.5432, 1.2345],  # coordonnées pour Materi
    "NATITINGOU": [10.5432, 1.2345],  # coordonnées pour Natitingou
    "OUASSA-PEHUNCO": [10.5432, 1.2345],  # coordonnées pour Ouassa-Pehunco
    "TANGUIETA": [10.5432, 1.2345],  # coordonnées pour Tanguieta
    "TOUCOUNTOUNA": [10.5432, 1.2345],  # coordonnées pour Toucountouna
    "ATLANTIQUE": [10.5432, 1.2345],  # coordonnées pour Atlantique
    "ABOMEY CALAVI": [10.5432, 1.2345],  # coordonnées pour Abomey Calavi
    "ALLADA": [10.5432, 1.2345],  # coordonnées pour Allada
    "KPOMASSE": [10.5432, 1.2345],  # coordonnées pour Kpomasse
    "OUIDAH": [10.5432, 1.2345],  # coordonnées pour Ouidah
    "SO AVA": [10.5432, 1.2345],  # coordonnées pour So Ava
    "TOFFO": [10.5432, 1.2345],  # coordonnées pour Toff
    "TORI BOSSITO": [10.5432, 1.2345],  # coordonnées pour Tori Bossito
    "ZE": [10.5432, 1.2345],  # coordonnées pour Zé
    "BORGOU": [10.5432, 1.2345],  # coordonnées pour Borgou
    "BEMBEREKE": [10.5432, 1.2345],  # coordonnées pour Bembereke
    "KALALE": [10.5432, 1.2345],  # coordonnées pour Kalalé
    "NDALI": [10.5432, 1.2345],  # coordonnées pour Ndali
    "NIKKI": [10.5432, 1.2345],  # coordonnées pour Nikki
    "PARAKOU": [10.5432, 1.2345],  # coordonnées pour Parakou
    "PERERE": [10.5432, 1.2345],  # coordonnées pour Pèrèrè
    "SINENDE": [10.5432, 1.2345],  # coordonnées pour Sinendé
    "TCHAOUROU": [10.5432, 1.2345],  # coordonnées pour Tchaourou
    "COLLINES": [10.5432, 1.2345],  # coordonnées pour Collines
    "BANTE": [10.5432, 1.2345],  # coordonnées pour Banté
    "DASSA ZOUME": [10.5432, 1.2345],  # coordonnées pour Dassa-Zoumé
    "GLAZOUE": [10.5432, 1.2345],  # coordonnées pour Glazoué
    "OUESSE": [10.5432, 1.2345],  # coordonnées pour Ouèssé
    "SAVALOU": [10.5432, 1.2345],  # coordonnées pour Savalou
    "SAVE": [10.5432, 1.2345],  # coordonnées pour Savè
    "COUFFO": [10.5432, 1.2345],  # coordonnées pour Couffo
    "APLAHOUE": [10.5432, 1.2345],  # coordonnées pour Aplahoué
    "DJAKOTOMEY": [10.5432, 1.2345],  # coordonnées pour Djakotomey
    "DOGBO": [10.5432, 1.2345],  # coordonnées pour Dogbo
    "KLOUEKANMEY": [10.5432, 1.2345],  # coordonnées pour Klouékanmey
    "LALO": [10.5432, 1.2345],  # coordonnées pour Lalo
    "TOVIKLIN": [10.5432, 1.2345],  # coordonnées pour Toviklin
    "DONGA": [10.5432, 1.2345],  # coordonnées pour Donga
    "BASSILA": [10.5432, 1.2345],  # coordonnées pour Bassila
    "COPARGO": [10.5432, 1.2345],  # coordonnées pour Copargo
    "DJOUGOU": [10.5432, 1.2345],  # coordonnées pour Djougou
    "OUAKE": [10.5432, 1.2345],  # coordonnées pour Ouaké
    "LITTORAL": [10.5432, 1.2345],  # coordonnées pour Littoral
    "COTONOU": [10.5432, 1.2345],  # coordonnées pour Cotonou
    "MONO": [10.5432, 1.2345],  # coordonnées pour Mono
    "ATHIEME": [10.5432, 1.2345],  # coordonnées pour Athiémé
    "BOPA": [10.5432, 1.2345],  # coordonnées pour Bopa
    "COME": [10.5432, 1.2345],  # coordonnées pour Comè
    "GRAND POPO": [10.5432, 1.2345],  # coordonnées pour Grand Popo
    "HOUEYOGBE": [10.5432, 1.2345],  # coordonnées pour Houéyogbé
    "LOKOSSA": [10.5432, 1.2345],  # coordonnées pour Lokossa
    "OUEME": [10.5432, 1.2345],  # coordonnées pour Ouémé
    "ADJARRA": [10.5432, 1.2345],  # coordonnées pour Adjarra
    "ADJOHOUN": [10.5432, 1.2345],  # coordonnées pour Adjohoun
    "AGUEGUES": [10.5432, 1.2345],  # coordonnées pour Aguégués
    "AKPRO MISSERETE": [10.5432, 1.2345],  # coordonnées pour Akpro-Missérété
    "AVRANKOU": [10.5432, 1.2345],  # coordonnées pour Avrankou
    "BONOU": [10.5432, 1.2345],  # coordonnées pour Bonou
    "DANGBO": [10.5432, 1.2345],  # coordonnées pour Dangbo
    "PORTO NOVO": [10.5432, 1.2345],  # coordonnées pour Porto-Novo
    "SEME PODJI": [10.5432, 1.2345],  # coordonnées pour Sèmè-Podji
    "PLATEAU": [10.5432, 1.2345],  # coordonnées pour Plateau
    "ADJA OUERE": [10.5432, 1.2345],  # coordonnées pour Adja-Ouèrè
    "IFANGNI": [10.5432, 1.2345],  # coordonnées pour Ifangni
    "KETOU": [10.5432, 1.2345],  # coordonnées pour Kétou
    "POBE": [10.5432, 1.2345],  # coordonnées pour Pobè
    "SAKETE": [10.5432, 1.2345],  # coordonnées pour Sâkété
    "ZOU": [10.5432, 1.2345],  # coordonnées pour Zou
    "ABOMEY": [10.5432, 1.2345],  # coordonnées pour Abomey
    "AGBANGNIZOUN": [10.5432, 1.2345],  # coordonnées pour Agbangnizoun
    "BOHICON": [10.5432, 1.2345],  # coordonnées pour Bohicon
    "COVE": [10.5432, 1.2345],  # coordonnées pour Covè
    "DJIDJA": [10.5432, 1.2345],  # coordonnées pour Djidja
    "OUINHI": [10.5432, 1.2345],  # coordonnées pour Ouinhi
    "ZAGNANADO": [10.5432, 1.2345],  # coordonnées pour Zagnanado
    "ZA KPOTA": [10.5432, 1.2345],  # coordonnées pour Za-Kpota
    "ZOGBODOMEY": [10.5432, 1.2345],  # coordonnées pour Zogbodomey
}

# Filtrer les données
st.sidebar.header("Filtres")
culture = st.sidebar.multiselect(
    "Culture", df["culture"].unique(), default=["Igname"]
)  # Multi-sélection des cultures
zone = st.sidebar.multiselect(
    "Zone géographique", df["zones-géographiques"].unique(), default=["BENIN"]
)  # Multi-sélection des zones géographiques

# Filtre flexible :
df_filtered = df[
    (df["culture"].isin(culture))
    & (df["zones-géographiques"].str.lower().isin([z.lower() for z in zone]))
]

# KPI
st.header(f"Exploitations et Producteurs")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Nombre total d'exploitations",
        df_filtered[df_filtered["indicateurs"].str.contains("Nombre d'exploitations")]["Value"].sum(),
    )

with col2:
    st.metric(
        "Nombre total de producteurs",
        df_filtered[df_filtered["indicateurs"].str.contains("Nombre de producteurs")]["Value"].sum(),
    )

with col3:
    try:
        taux_production = (
            df_filtered[df_filtered["indicateurs"].str.contains("Nombre de producteurs")]["Value"].sum()
            / df_filtered[df_filtered["indicateurs"].str.contains("Nombre d'exploitations")]["Value"].sum()
        )
        st.metric("Taux de production", round(taux_production, 2))
    except ZeroDivisionError:
        st.metric("Taux de production", "NaN")

# Mappemonde interactif
st.header(f"Répartition géographique des exploitations")

m = folium.Map(location=coordinates["BENIN"], zoom_start=6)  # Coordonnées du Bénin

# Ajouter des marqueurs sur la carte
for index, row in df_filtered[df_filtered["indicateurs"].str.contains("Nombre d'exploitations")].iterrows():
    # Récupérer les coordonnées de la zone géographique
    lat, lon = coordinates[row["zones-géographiques"]]
    folium.Marker(location=[lat, lon], popup=row["zones-géographiques"], tooltip=row["zones-géographiques"]).add_to(m)

folium_static(m)

# Graphiques
st.header(f"Visualisation des données")

# graphique à barres empilées
st.bar_chart(
    df_filtered[df_filtered["indicateurs"].str.contains("Nombre d'exploitations")]
    .groupby(["culture", "zones-géographiques"])["Value"]
    .sum()
    .unstack()
)

# graphique en secteurs (pie chart)
fig, ax = plt.subplots()
df_filtered[df_filtered["indicateurs"].str.contains("Nombre d'exploitations")].groupby("culture")["Value"].sum().plot(kind='pie', autopct='%1.1f%%', ax=ax)
st.pyplot(fig)