
def estadisticas_a_df(df_extraer, df_guardar, columnas, local = False, visitante = False):
    """
    Función para rellenar el dataframe, según sea local o visitante, con el resto de estadísticas que nos interesan.
    df_extraer: el dataframe del que se van a extraer los datos.
    df_guardar: el dataframe en el que se van a guardar esos datos.
    columnas: las columnas del df_extraer que se quieren guardar en df_guardar.
    local, visitante: poner en 'True' según corresponda, si son estadísticas locales o visitantes.

    """
    if local:
        equipo = "HomeTeam"
    else:
        equipo = "AwayTeam"

    for x in columnas:
        df_guardar[x] = df_extraer.groupby(equipo)[x].sum()



def calcular_rentabilidad_HDA(row, amm=10, result=""):
    """
    Función para calcular la rentabilidad de apostar a Home, Draw o Away en un dataframe
    amm: es la cantidad apostada en cada partido
    result: los valores son 'H' para 'Home', 'D' para 'Draw' y 'A' para 'Away'

    """
    if result == "H":
        if row["FullTimeResult"] == "H":
            return amm * row["MarketMaxHomeTeam"] - amm
        else:
            return -amm
    elif result == "D":
        if row["FullTimeResult"] == "D":
            return amm * row["MarketMaxDraw"] - amm
        else:
            return -amm
    elif result == "A":
        if row["FullTimeResult"] == "A":
            return amm * row["MarketMaxAwayTeam"] - amm
        else:
            return -amm
    else:
        return 0
