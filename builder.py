import pandas as pd
from datetime import datetime
from datetime import date
class  dfbuilder:

  def __init__(self, df, config, columnas_eliminar=None, semana=None):
    self.df = df
    self.config = config
    self.semana = semana
    self.columnas_eliminar = columnas_eliminar or {}
    self.hoy = pd.Timestamp.today().normalize()
    self.ops = dfops()

  def filter(self, df, semana=None, anio=None, func=None, **kwargs):
    if func is None:
        return df
    return func(df, semana, anio)

  def limpiar_fechas(self, df, semana=None, anio=None, cols=None, **kwargs):
    if not cols:
        return df

    for col in cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    return df


  def sumar_festivos(self, df, semana=None, anio=None, festivos=None, clima=None, col_resultado=None, **kwargs):
    if not festivos or not clima:
        return df

    col_resultado = col_resultado or festivos

    df[col_resultado] = (
        df[festivos].fillna(0) +
        df[clima].fillna(0)
    )

    return df.drop(columns=[clima], errors='ignore')


  def drop_columnas(self, df, semana=None, anio=None, key=None, **kwargs):
    columnas = self.columnas_eliminar.get(key, [])
    columnas_existentes = [c for c in columnas if c in df.columns]

    no_encontradas = [c for c in columnas if c not in df.columns]

    #print("✔️ EXISTENTES:", len(columnas_existentes))
    #print("❌ NO ENCONTRADAS:", no_encontradas[:5])  # solo primeras 5
    #print("KEY:", key)
    #print("DICT:", self.columnas_eliminar)
    return df.drop(columns=columnas_existentes)
  def calcular_rango(self, df, semana=None, anio=None, inicio=None, fin=None, col_resultado=None, **kwargs):
    if not inicio or not fin or not col_resultado:
        return df

    df[col_resultado] = df.apply(
        lambda row: pd.date_range(
            row[inicio],
            self.hoy if fin == 'hoy' else row[fin]
        ).tolist()
        if (
            pd.notna(row[inicio]) and
            pd.notna(self.hoy if fin == 'hoy' else row[fin]) and
            row[inicio] <= (self.hoy if fin == 'hoy' else row[fin])
        )
        else [],
        axis=1
    )

    return df


  def calcular_semana(self, df, semana=None, anio=None, fecha_ultima=None, col_resultado=None, **kwargs):
    if not fecha_ultima or not col_resultado:
        return df

    df[col_resultado] = df[fecha_ultima].dt.isocalendar().week.astype('Int64')
    return df


  def contar_dias(self, df, semana=None, anio=None, col_rango=None, col_resultado=None, col_festivos=None, **kwargs):
    if not col_rango or not col_resultado:
        return df

    df[col_resultado] = df[col_rango].apply(
        lambda x: sum(d.dayofweek != 6 for d in x) if isinstance(x, list) else 0
    )

    if col_festivos:
        df[col_resultado] = df[col_resultado] - df[col_festivos].fillna(0)

    return df

  def build(self, reporte, semana=None, anio=None):

    reporte_config = self.config[reporte]
    resultados = {}

    for nombre_df, df_config in reporte_config.items():

        if nombre_df == "requires":
            continue

        df_temp = self.df.copy()
        reportes = {}

        for step in df_config["pipeline"]:

            step_type = step.get("step", "transform")

            if step_type == "transform":
                df_temp = self._execute_step(step, df_temp, semana, anio)

            elif step_type == "report":
                nombre = step.get("name", step.get("func"))
                resultado = self._execute_step(step, df_temp, semana, anio)
                reportes[nombre] = resultado

        resultados[nombre_df] = {
            "df": df_temp,
            "reportes": reportes
        }

    return resultados
    
  def _execute_step(self, step, df, semana, anio):
    func_name = step.get("func")
    args = step.get("args", {})

    if not func_name:
        raise ValueError(f"Step sin 'func': {step}")

    if hasattr(self, func_name):
        metodo = getattr(self, func_name)

    elif hasattr(self.ops, func_name):
        metodo = getattr(self.ops, func_name)

    else:
        raise ValueError(f"Función no implementada: {func_name}")

    return metodo(df, semana=semana, anio=anio, **args)
  

class dfops:

  def ordenar(self, df, columna=None, asc=True, **kwargs):
    if columna is None:
        raise ValueError("Se requiere 'columna' para ordenar")

    return df.sort_values(by=columna, ascending=asc)

  def conteo_distinto(self, df, columna=None, **kwargs):
    if columna is None:
        raise ValueError("Se requiere 'columna'")

    conteo = (
        df[columna]
        .value_counts()
        .reset_index()
        .rename(columns={'index': columna, columna: f'conteo_{columna}'})
    )

    return conteo

  def media_agrupada(self, df, columna=None, por=None, **kwargs):
    if columna is None or por is None:
        raise ValueError("Se requieren 'columna' y 'por'")

    media = (
        df.groupby(por)[columna]
        .mean()
        .reset_index(name=f"media_{columna}"))

    return media
  def diferencia_conteos(self, df,
                       semana=None,
                       anio=None,
                       func_a=None,
                       func_b=None,
                       **kwargs):

    if func_a is None or func_b is None:
        raise ValueError("Se requieren ambos filtros")

    total_a = len(func_a(df, semana, anio))
    total_b = len(func_b(df, semana, anio))

    return total_a - total_b

  
  def contar_filtrado(self, df, semana=None, anio=None,
                     func=None,
                     **kwargs):

    if func is None:
        raise ValueError("Se requiere func")

    df_filtrado = func(df, semana, anio)

    return len(df_filtrado)