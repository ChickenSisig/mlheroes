import pandas as pd
import plotly as p
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Heroes", 
                   page_icon=":bar_chart:",
                   layout="wide"
)

df = pd.read_excel(
    io = 'MLBB_Hero_Database.xlsx',
    engine = 'openpyxl',
    sheet_name = 'HEROES',
    skiprows = 1,
    usecols = 'B:N',
    nrows = 1000,
)

#SIDEBAR
st.sidebar.header("Filter here:")
year_release = st.sidebar.multiselect(
    "Select the Year of Release:",
    options=df["year_release"].unique(),
    default=df["year_release"].unique()
)

role_ID = st.sidebar.multiselect(
    "Select the Role:",
    options=df["role_ID"].unique(),
    default=df["role_ID"].unique()
)

region_origin_ID = st.sidebar.multiselect(
    "Select the Region Origin:",
    options=df["region_origin_ID"].unique(),
    default=df["region_origin_ID"].unique()
)

df_selection = df.query(
    "year_release == @year_release & role_ID == @role_ID & region_origin_ID == @region_origin_ID"
)

st.header(":dizzy: Heroes")
st.dataframe(df_selection)

#MAIN
st.header(":bar_chart: Stats")
st.markdown("##")

#HIGHEST HP
highest_hp_row = df_selection.loc[df_selection["base_HP"].idxmax()]
highesthp_hero = highest_hp_row["hero_name"]
highest_hp = highest_hp_row["base_HP"]

#HIGHEST PHYSICAL ATTACK
highest_phyatk_row = df_selection.loc[df_selection["base_physical_ATK"].idxmax()]
highestphyatk_hero = highest_phyatk_row["hero_name"]
highest_phyatk = highest_phyatk_row["base_physical_ATK"]

#HIGHEST PHYSICAL DEFENSE
highest_phydef_row = df_selection.loc[df_selection  ["base_physical_DEF"].idxmax()]
highestphydef_hero = highest_phydef_row["hero_name"]
highest_phydef = highest_phydef_row["base_physical_DEF"]

#HIGHEST MAGIC DEFENSE
highest_magdef_row = df_selection.loc[df_selection["base_magic_DEF"].idxmax()]
highestmagdef_hero = highest_magdef_row["hero_name"]
highest_magdef = highest_magdef_row["base_magic_DEF"]

#HIGHEST BASE MANA
highest_mana_row = df_selection.loc[df_selection["base_mana"].idxmax()]
highestmana_hero = highest_mana_row["hero_name"]
highest_mana = highest_mana_row["base_mana"]

#HIGHEST ATTACK SPEED
highest_atkspd_row = df_selection.loc[df_selection["base_ATK_speed"].idxmax()]
highest_atkspd_hero = highest_atkspd_row["hero_name"]
highest_atkspd = highest_atkspd_row["base_ATK_speed"]

#HIGHEST BASE HP REGEN
highest_hpregen_row = df_selection.loc[df_selection["base_HP_regen"].idxmax()]
highest_hpregen_hero = highest_hpregen_row["hero_name"]
highest_hpregen = highest_hpregen_row["base_HP_regen"]

#HIGHEST MANA REGEN
highest_manaregen_row = df_selection.loc[df_selection["base_mana_regen"].idxmax()]
highest_manaregen_hero = highest_manaregen_row["hero_name"]
highest_manaregen = highest_manaregen_row["base_mana_regen"]

#AVERAGE PHYSICAL ATTACK
base_phy_atk = round(df_selection["base_physical_ATK"].mean(), 1)
ave_phy_atk = ":star:" * int(round(base_phy_atk, 0))

#AVERAGE PHYSICAL DEFENSE
base_phy_def = round(df_selection["base_physical_DEF"].mean(), 1)
ave_phy_def = ":star:" * int(round(base_phy_def, 0))

#AVERAGE MAGIC DEFENSE
base_mag_def = round(df_selection["base_magic_DEF"].mean(),1)
ave_mag_def = ":star:" * int(round(base_mag_def, 0))

#AVERAGE MANA
base_mana = round(df_selection["base_mana"].mean(),1)
ave_mana = ":star:" * int(round(base_mana, 0))

#AVERAGE HP REGEN
base_hp_regen = round(df_selection["base_HP_regen"].mean(),1)
ave_hp = ":star:" * int(round(base_hp_regen, 0))

left, right = st.columns(2)
with left:
    st.subheader("Hero with the most physical attack:")
    st.subheader(f"{highestphyatk_hero}: {highest_phyatk}")
    st.markdown("#")

    st.subheader("Hero with the most physical defense:")
    st.subheader(f"{highestphydef_hero}: {highest_phydef}")
    st.markdown("#")

    st.subheader("Hero with the most magic defense:")
    st.subheader(f"{highestmagdef_hero}: {highest_magdef}")
    st.markdown("#")

    st.subheader("Hero with the most base HP:")
    st.subheader(f"{highesthp_hero}: {highest_hp}")
    st.markdown("#")

    st.subheader("Hero with the most base Mana:")
    st.subheader(f"{highestmana_hero}: {highest_mana}")
    st.markdown("#")    

    st.subheader("Hero with the highest Attack Speed:")
    st.subheader(f"{highest_atkspd_hero}: {highest_atkspd}")
    st.markdown("#")

    st.subheader("Hero with the highest HP Regen:")
    st.subheader(f"{highest_hpregen_hero}: {highest_hpregen}")
    st.markdown("#")

    st.subheader("Hero with the most Mana Regen:")
    st.subheader(f"{highest_manaregen_hero}: {highest_manaregen}")

with right:
    st.subheader("Average Base Physical Attack:")
    st.subheader(f"{base_phy_atk} {ave_phy_atk}")
    st.markdown("#")

    st.subheader("Average Base Physical Defense:")
    st.subheader(f"{base_phy_def} {ave_phy_def}")
    st.markdown("#")

    st.subheader("Average Basic Magic Defense:")
    st.subheader(f"{base_mag_def} {ave_mag_def}")
    st.markdown("#")

    st.subheader("Average Base HP Regen:")
    st.subheader(f"{base_hp_regen} {ave_hp}")
    st.markdown("#")

    st.subheader("Average Base Mana:")
    st.subheader(f"{base_mana} {ave_mana}")

st.markdown("---")

#HERO LINE
hero_hp = (
    df_selection.groupby(by=["hero_name"]).sum()[["base_HP"]].sort_values(by="base_HP")
)
fig_hero = px.bar(
    hero_hp,
    x = "base_HP",
    y = hero_hp.index,
    orientation = "h",
    title = "<b> Hero HP </b>",
    color_discrete_sequence = ["#3572EF"] * len(hero_hp),
    template = "plotly_white"
)

fig_hero.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)",
    xaxis = (dict(showgrid = False))
)

st.plotly_chart(fig_hero)
