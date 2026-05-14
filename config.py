##config
from datetime import datetime
from datetime import date
columnas_eliminar = {'df_obra_pron':['Fecha Real Inicio OC','Tipo Cimentación','Fecha Repro Dinamica Dia Ultima Actividad','Fecha Real Ultima Actividad OC', 'Fecha Dinamica Ultima Actividad OC', 'Dias Acumulados Al Dia de Hoy OC', 'Festivos OC', 'Clima Total OC validado',
                                    'rango2','rango','Fecha Repro Original Ultima Acticidad','Dia Real','Estatus','Estatus Dias','Fecha Plan Inicio OC','SEM OC',
                   'Clima Total OC sin validar','TC Objetivo OC','TC OC','TC Proyectado OC','Fecha Termino Primera Actividad OC','Fecha Termino Ultima Actividad OC'
                   ,'Fecha Real Inicio AC','Fecha Real Ultima Actividad AC','Fecha Dinamica Ultima Actividad AC','Dias Acumulados Al Dia de Hoy AC','SEM AC','Festivos AC',
                   'Clima total AC sin validad','Clima total AC validado','TC Objetivo AC','TC AC','TC Proyectado AC','Fecha Plan Inicio CT','Fecha Real Inicio CT','Fecha Real Ultima Actividad CT'
                   ,'Fecha Dinamica Ultima Actividad CT','KipID','SEM CT','Festivos CT','Clima total CT sin validad','Clima total CT validado','TC Objetivo CT','TC CT'
                   ,'TC General Objetivo','TC General','TC Objetivo dias','Fecha Plan Inicio AC','Dias Acumulados Al Dia de Hoy CT','TC Proyectado CT'
                   ,'TC Proyectado','Fecha Proyectada','Dias Restantes','Festivos General','num sem okct','Fecha CT Plan']
          ,'df_ac_pron':['Fecha Real Inicio OC','Tipo Cimentación', 'Fecha Real Inicio AC', 'Fecha Real Ultima Actividad AC', 'Fecha Dinamica Ultima Actividad AC', 'Dias Acumulados Al Dia de Hoy AC', 'Festivos AC', 'Clima total AC validado', 'Festivos General',
                         'Fecha Repro Dinamica Dia Ultima Actividad','rango2','rango','Fecha Repro Original Ultima Acticidad','Dia Real','Estatus','Estatus Dias','Fecha Plan Inicio OC','SEM OC',
                   'Clima Total OC sin validar','TC Objetivo OC','TC OC','TC Proyectado OC','Fecha Termino Primera Actividad OC','Fecha Termino Ultima Actividad OC'
                   ,'Fecha Real Ultima Actividad OC','Fecha Dinamica Ultima Actividad OC','Dias Acumulados Al Dia de Hoy OC','SEM AC','Festivos OC'
                   ,'Clima total AC sin validad','Clima Total OC sin validar','Clima Total OC validado','TC Objetivo AC','TC AC','TC Proyectado AC','Fecha Plan Inicio CT','Fecha Real Inicio CT','Fecha Real Ultima Actividad CT'
                   ,'Fecha Dinamica Ultima Actividad CT','KipID','SEM CT','Festivos CT','Clima total CT sin validad','Clima total CT validado','TC Objetivo CT','TC CT'
                   ,'TC General Objetivo','TC General','TC Objetivo dias','Fecha Plan Inicio AC','Dias Acumulados Al Dia de Hoy CT','TC Proyectado CT'
                   ,'TC Proyectado','Fecha Proyectada','Dias Restantes','num sem okct','Fecha CT Plan']
          ,'df_ct_pron':['Tipo Cimentación','Fecha Real Inicio OC', 'Fecha Real Inicio CT', 'Fecha Real Ultima Actividad CT', 'Fecha Dinamica Ultima Actividad CT', 'Dias Acumulados Al Dia de Hoy CT', 'Festivos CT', 'Clima total CT validado', 'Festivos General',
                         'Fecha Repro Dinamica Dia Ultima Actividad','rango2','rango','Fecha Repro Original Ultima Acticidad','Dia Real','Estatus','Estatus Dias','Fecha Plan Inicio OC','SEM OC',
                   'Clima Total OC sin validar','TC Objetivo OC','TC OC','TC Proyectado OC','Fecha Termino Primera Actividad OC','Fecha Termino Ultima Actividad OC'
                   ,'Fecha Real Ultima Actividad OC','Fecha Dinamica Ultima Actividad OC','Dias Acumulados Al Dia de Hoy OC','SEM AC','Festivos OC'
                   ,'Clima total AC sin validad','Clima Total OC sin validar','Clima Total OC validado','TC Objetivo AC','TC AC','TC Proyectado AC','Fecha Plan Inicio CT'
                   ,'Fecha Dinamica Ultima Actividad AC','KipID','SEM CT','Festivos AC','Clima total CT sin validad','Clima total AC validado','TC Objetivo CT','TC CT'
                   ,'TC General Objetivo','TC General','TC Objetivo dias','Fecha Plan Inicio AC','Dias Acumulados Al Dia de Hoy AC','TC Proyectado CT','Fecha Real Ultima Actividad AC','Sem AC Pron'
                   ,'TC Proyectado','Fecha Proyectada','Dias Restantes','Fecha CT Plan','num sem okct', 'Fecha Real Inicio AC','Sem OC Pron','Clima total AC sin validad']
          ,'ct_semas':['Fecha Repro Dinamica Dia Ultima Actividad','Fecha Repro Original Ultima Acticidad','Dia Real','Estatus','Estatus Dias','Fecha Plan Inicio OC',
                   'Fecha Real Ultima Actividad OC','Fecha Dinamica Ultima Actividad OC','Dias Acumulados Al Dia de Hoy OC','SEM OC','Festivos OC',
                   'Clima Total OC sin validar','Clima Total OC validado','TC Objetivo OC','TC OC','TC Proyectado OC','Fecha Termino Primera Actividad OC','Fecha Termino Ultima Actividad OC'
                   ,'Fecha Real Inicio AC','Fecha Real Ultima Actividad AC','Fecha Dinamica Ultima Actividad AC','Dias Acumulados Al Dia de Hoy AC','SEM AC','Festivos AC',
                   'Clima total AC sin validad','Clima total AC validado','TC Objetivo AC','TC AC','TC Proyectado AC','Fecha Plan Inicio CT','Fecha Real Inicio CT','Fecha Real Ultima Actividad CT'
                   ,'Fecha Dinamica Ultima Actividad CT','KipID','SEM CT','Festivos CT','Clima total CT sin validad','Clima total CT validado','TC Objetivo CT','TC CT'
                   ,'TC General Objetivo','TC General','TC Objetivo dias','Fecha Plan Inicio AC','Dias Acumulados Al Dia de Hoy CT','TC Proyectado CT'
                   ,'TC Proyectado','Fecha Proyectada','Dias Restantes','rango','Ultima Actividad Avanzada']
          ,'obra':['Fecha Repro Original Ultima Acticidad','Dia Real','Estatus','Estatus Dias','Fecha Plan Inicio OC','Fecha Repro Dinamica Dia Ultima Actividad',
                   'Clima Total OC sin validar','TC Objetivo OC','TC Proyectado OC','Fecha Termino Primera Actividad OC','Fecha Termino Ultima Actividad OC','Dias Acumulados Al Dia de Hoy OC'
                   ,'Fecha Real Inicio AC','Fecha Real Ultima Actividad AC','Fecha Dinamica Ultima Actividad OC','Fecha Dinamica Ultima Actividad AC','Dias Acumulados Al Dia de Hoy AC','SEM AC','Festivos AC',
                   'Clima total AC sin validad','Clima total AC validado','TC Objetivo AC','TC AC','TC Proyectado AC','Fecha Plan Inicio CT','Fecha Real Inicio CT','Fecha Real Ultima Actividad CT'
                   ,'Fecha Dinamica Ultima Actividad CT','KipID','SEM CT','Festivos CT','Clima total CT sin validad','Clima total CT validado','TC Objetivo CT','TC CT','Festivos OC', 'Clima Total OC validado'
                   ,'TC General Objetivo','TC General','TC Objetivo dias','Fecha Plan Inicio AC','Dias Acumulados Al Dia de Hoy CT','TC Proyectado CT'
                   ,'TC Proyectado','Fecha Proyectada','Dias Restantes','Festivos General','Climana General','Fecha Ultima Check Real','num sem okct','Fecha CT Plan']
          ,'ac':['Fecha Repro Original Ultima Acticidad','Dia Real','Estatus','Estatus Dias','Fecha Plan Inicio OC','Fecha Repro Dinamica Dia Ultima Actividad',
                   'Clima Total OC sin validar','TC Objetivo OC','TC Proyectado OC','Fecha Termino Primera Actividad OC','Fecha Termino Ultima Actividad OC','Dias Acumulados Al Dia de Hoy OC'
                   ,'Fecha Real Inicio OC','Fecha Real Ultima Actividad OC','Fecha Dinamica Ultima Actividad OC','Fecha Dinamica Ultima Actividad AC','Dias Acumulados Al Dia de Hoy AC','SEM OC','Festivos AC',
                   'Clima total AC sin validad','Clima total AC validado','TC Objetivo AC','TC OC','TC Proyectado AC','Fecha Plan Inicio CT','Fecha Real Inicio CT','Fecha Real Ultima Actividad CT'
                   ,'Fecha Dinamica Ultima Actividad CT','KipID','SEM CT','Festivos CT','Clima total CT sin validad','Clima total CT validado','TC Objetivo CT','TC CT','Festivos OC', 'Clima Total OC validado'
                   ,'TC General Objetivo','TC General','TC Objetivo dias','Fecha Plan Inicio AC','Dias Acumulados Al Dia de Hoy CT','TC Proyectado CT'
                   ,'TC Proyectado','Fecha Proyectada','Dias Restantes','Festivos General','Climana General','Fecha Ultima Check Real','num sem okct','Fecha CT Plan']
          ,'ct':['Fecha Repro Original Ultima Acticidad','Dia Real','Estatus','Estatus Dias','Fecha Plan Inicio OC',
                 'Fecha Repro Dinamica Dia Ultima Actividad',
                   'Clima Total OC sin validar','TC Objetivo OC','TC Proyectado OC','Fecha Termino Primera Actividad OC',
                 'Fecha Termino Ultima Actividad OC','Dias Acumulados Al Dia de Hoy OC'
                   ,'Fecha Real Inicio OC','Fecha Real Ultima Actividad OC','Fecha Dinamica Ultima Actividad OC',
                 'Fecha Dinamica Ultima Actividad AC','Dias Acumulados Al Dia de Hoy AC','SEM OC','Festivos AC',
                   'Clima total AC sin validad','Clima total AC validado','TC Objetivo AC','TC AC','TC Proyectado AC',
                 'Fecha Plan Inicio CT','Fecha Real Inicio AC','Fecha Real Ultima Actividad AC'
                   ,'Fecha Dinamica Ultima Actividad CT','KipID','SEM AC','Festivos CT','Clima total CT sin validad','Clima total CT validado',
                 'TC Objetivo CT','TC OC','Festivos OC', 'Clima Total OC validado'
                   ,'TC General Objetivo','TC General','TC Objetivo dias','Fecha Plan Inicio AC','Dias Acumulados Al Dia de Hoy CT','TC Proyectado CT'
                   ,'TC Proyectado','Fecha Proyectada','Dias Restantes','Festivos General','Climana General','Fecha Ultima Check Real',
                 'num sem okct','Fecha CT Plan']
          ,'paros':['Proyecto','Tipo Cimentación','Festivos','Festivos General','Fecha Repro Original Ultima Acticidad','Dia Real','Estatus','Estatus Dias',
    'Fecha Plan Inicio OC','Fecha Repro Dinamica Dia Ultima Actividad',
    'Clima Total OC sin validar','TC Objetivo OC','TC Proyectado OC',
    'Fecha Termino Primera Actividad OC','Fecha Termino Ultima Actividad OC',
    'Dias Acumulados Al Dia de Hoy OC','Fecha Real Inicio OC',
    'Fecha Real Ultima Actividad OC','Fecha Dinamica Ultima Actividad OC',
    'Fecha Dinamica Ultima Actividad AC','Dias Acumulados Al Dia de Hoy AC',
    'SEM OC','Festivos AC','Clima total AC sin validad','Clima total AC validado',
    'TC Objetivo AC','TC AC','TC Proyectado AC','Fecha Plan Inicio CT',
    'Fecha Real Inicio CT','Fecha Real Ultima Actividad CT',
    'Fecha Dinamica Ultima Actividad CT','KipID','SEM AC','Festivos CT',
    'Clima total CT sin validad','Clima total CT validado','TC Objetivo CT',
    'TC OC','Festivos OC', 'Clima Total OC validado','TC General Objetivo',
    'TC General','TC Objetivo dias','Fecha Plan Inicio AC',
    'Dias Acumulados Al Dia de Hoy CT','TC Proyectado CT','TC Proyectado',
    'Fecha Proyectada','Dias Restantes','SEM CT','rango','num sem okct',
    'Fecha CT Plan','Fecha Real Inicio AC','Fecha Real Ultima Actividad AC','TC CT']}

config = {'cts':{'requires':{
    'semana':True,
    'anio':True
},'Reporte CT´s':{'pipeline':[
                             {'step':'transform',
                              'func':'limpiar_fechas',
                              'args':{
                              'cols':['Fecha Ultima Check Real',
                                      'Fecha Real Inicio OC']}},
                             {'step':'transform',
                              'func':'calcular_semana',
                              'args':{
                              'fecha_ultima':'Fecha Ultima Check Real',
                              'col_resultado':'num sem okct'}},
                             {'step':'transform',
                              'func':'sumar_festivos',
                              'args':{
                              'festivos':'Festivos General',
                              'clima':'Climana General',
                              'col_resultado':'Festivos'}},
                             {'step':'transform',
                              'func':'calcular_rango',
                              'args':{
                              'inicio':'Fecha Real Inicio OC',
                              'fin': 'Fecha Ultima Check Real',
                              'col_resultado':'rango'}},
                             {'step':'transform',
                              'func':'contar_dias',
                              'args':{
                              'col_rango':'rango',
                              'col_festivos':'Festivos',
                              'col_resultado':'dias totales'}},
                             {'step':'transform',
                              'func':'filter',
                              'args':{'func': lambda df, semana, anio: df[
                                  (df['num sem okct'] == semana) & (df['Ultima Actividad Avanzada'] == "OK CT") & (df['Fecha Ultima Check Real'].dt.isocalendar().year == anio)
                              ]}},
                             {'step':'transform',
                              'func':'drop_columnas',
                              'args':{'key':'ct_semas'}},
                             {'step':'transform',
                              'func':'ordenar',
                              'args':{'columna':'Fecha Ultima Check Real'}},
                             {'step':'report',
                              'func':'media_agrupada',
                              'args':{'columna':'dias totales',
                                      'por':'Modelo'}},
                             {'step':'report',
                              'func':'conteo_distinto',
                              'args':{'columna':'Modelo'}}]}},
          'especialidad':{'requires':
                          {'semana':True,
                           'anio':True},'OBRA CIVIL':{'pipeline':[
                             {'step':'transform',
                              'func':'limpiar_fechas',
                              'args':{
                              'cols':['Fecha Real Ultima Actividad OC']}},
                             {'step':'transform',
                              'func':'filter',
                              'args':{'func': lambda df, semana, anio: df[
                                  (df['Fecha Real Ultima Actividad OC'].dt.year == anio) & (df['Fecha Real Ultima Actividad OC'].notna()) & (df['SEM OC'] == semana)
                              ]}},
                             {'step':'transform',
                              'func':'drop_columnas',
                              'args':{'key':'obra'}},
                             {'step':'transform',
                              'func':'ordenar',
                              'args':{'columna':'Fecha Real Ultima Actividad OC'}},
                             {'step':'report',
                              'func':'media_agrupada',
                              'args':{'columna':'TC OC',
                                      'por':'Modelo'}},
                             {'step':'report',
                              'func':'conteo_distinto',
                              'args':{'columna':'Modelo'}}]},
                         'ACABADOS':{'pipeline':[
                             {'step':'transform',
                              'func':'limpiar_fechas',
                              'args':{
                                  'cols':['Fecha Real Ultima Actividad AC']}},
                             {'step':'transform',
                              'func':'filter',
                              'args':{'func': lambda df, semana, anio: df[
                                  (df['Fecha Real Ultima Actividad AC'].dt.year == anio) & (df['Fecha Real Ultima Actividad AC'].notna()) & (df['SEM AC'] == semana)
                              ]}},
                             {'step':'transform',
                              'func':'drop_columnas',
                              'args':{'key':'ac'}},
                             {'step':'transform',
                              'func':'ordenar',
                              'args':{'columna':'Fecha Real Ultima Actividad AC'}},
                             {'step':'report',
                              'func':'media_agrupada',
                              'args':{'columna':'TC AC',
                                      'por':'Modelo'}},
                             {'step':'report',
                              'func':'conteo_distinto',
                              'args':{'columna':'Modelo'}}]},
                         'CT´s':{'pipeline':[
                             {'step':'transform',
                              'func':'limpiar_fechas',
                              'args':{
                                  'cols':['Fecha Real Ultima Actividad CT']}},
                             {'step':'transform',
                              'func':'filter',
                              'args':{'func': lambda df, semana, anio: df[
                                  (df['Fecha Real Ultima Actividad CT'].dt.year == anio) & (df['Fecha Dinamica Ultima Actividad CT'].notna()) & (df['SEM CT'] == semana)
                              ]}},
                             {'step':'transform',
                              'func':'drop_columnas',
                              'args':{'key':'ct'}},
                             {'step':'transform',
                              'func':'ordenar',
                              'args':{'columna':'Fecha Real Ultima Actividad CT'}},
                             {'step':'report',
                              'func':'media_agrupada',
                              'args':{'columna':'TC CT',
                                      'por':'Modelo'}},
                             {'step':'report',
                              'func':'conteo_distinto',
                              'args':{'columna':'Modelo'}}]}},
          'paros':{'requires':{'semana':False,
                               'anio':True},'Paros de proceso':{'pipeline':[
                             {'step':'transform',
                              'func':'limpiar_fechas',
                              'args':{
                                  'cols':['Fecha Ultima Check Real']}},
                             {'step':'transform',
                              'func':'sumar_festivos',
                              'args':{
                                  'festivos':'Festivos General',
                                  'clima':'Climana General',
                                  'col_resultado':'Festivos'}},
                             {'step':'transform',
                              'func':'calcular_rango',
                              'args':{'inicio':'Fecha Ultima Check Real',
                                      'fin': 'hoy',
                                      'col_resultado':'rango'}},
                             {'step':'transform',
                              'func':'contar_dias',
                              'args':{'col_rango':'rango',
                                      'col_resultado':'Dias Paros'}},
                             {'step':'report',
                              'func':'contar_filtrado',
                              'args':{
     'func': lambda df, semana, anio: df[
         (df['SEM CT'].isna()) &
         (df['Ultima Actividad Avanzada'] != 'OK CT') &
         (df['Fecha Ultima Check Real'].notna()) &
         (df['Fecha Ultima Check Real'].dt.isocalendar().year == anio)]}},
                             {'step':'report',
                              'func':'diferencia_conteos',
                              'args':{
     'func_a': lambda df, semana, anio: df[
         (df['SEM CT'].isna()) &
         (df['Ultima Actividad Avanzada'] != 'OK CT') &
         (df['Fecha Ultima Check Real'].notna()) &
         (df['Fecha Ultima Check Real'].dt.isocalendar().year == anio)],
     'func_b': lambda df, semana, anio: df[
         (df['Dias Paros'] > 2) &
         (df['SEM CT'].isna()) &
         (df['Ultima Actividad Avanzada'] != 'OK CT') &
         (df['Fecha Ultima Check Real'].notna()) &
         (df['Fecha Ultima Check Real'].dt.isocalendar().year == anio)
     ]}},
                             {'step':'transform',
                              'func':'filter',
                              'args':{'func': lambda df,semana, anio: df[
                                  (df['Dias Paros'] > 2) & (df['SEM CT'].isna()) & (df['Ultima Actividad Avanzada'] != 'OK CT') & (df['Fecha Ultima Check Real'].notna()) & (df['Fecha Ultima Check Real'].dt.isocalendar().year == anio)
                              ]}},
                             {'step':'transform',
                              'func':'ordenar',
                              'args':{'columna':'Fecha Ultima Check Real'}},
                             {'step':'transform',
                              'func':'drop_columnas',
                              'args':{'key':'paros'}}]}},
          'pronosticos':{'requires':{'semana':True,'anio':True},'Pronostico OC':{'pipeline':[
                             {'step':'transform',
                              'func':'limpiar_fechas',
                              'args':{
                                  'cols':['Fecha Ultima Check Real','Fecha Real Inicio OC','Fecha Dinamica Ultima Actividad OC','Fecha Repro Dinamica Dia Ultima Actividad']}},
                             {'step':'transform',
                              'func':'calcular_semana',
                              'args':{
                                  'fecha_ultima':'Fecha Dinamica Ultima Actividad OC',
                                  'col_resultado':'Sem OC Pron'}},
                             {'step':'transform',
                              'func':'calcular_rango',
                              'args':{
                                  'inicio':'Fecha Real Inicio OC',
                                  'fin': 'Fecha Dinamica Ultima Actividad OC',
                                  'col_resultado':'rango'}},
                             {'step':'transform',
                              'func':'sumar_festivos',
                              'args':{'festivos':'Festivos General',
                                      'clima':'Climana General',
                                      'col_resultado':'Festivos'}},
                             {'step':'transform',
                              'func':'contar_dias',
                              'args':{'col_rango':'rango',
                                      'col_festivos':'Festivos',
                                      'col_resultado':'Dias OC Pron'}},
                             {'step':'transform',
                              'func':'calcular_rango',
                              'args':{
                                  'inicio':'Fecha Real Inicio OC',
                                  'fin': 'Fecha Repro Dinamica Dia Ultima Actividad',
                                  'col_resultado':'rango2'}},
                             {'step':'transform',
                              'func':'contar_dias',
                              'args':{'col_rango':'rango2',
                                      'col_festivos':'Festivos',
                                      'col_resultado':'TC Pron'}},
                             {'step':'transform',
                              'func':'filter',
                              'args':{'func': lambda df, semana, anio: df[(df['Ultima Actividad Avanzada'] != 'OK CT') & (df['Fecha Real Ultima Actividad OC'].isna()) &
                               (df['Sem OC Pron'] == semana) & (df['Fecha Ultima Check Real'].dt.isocalendar().year == anio)]}},
                             {'step':'transform',
                              'func':'ordenar',
                              'args':{'columna':'Fecha Dinamica Ultima Actividad OC'}},
                             {'step':'transform',
                              'func':'drop_columnas',
                              'args':{'key':'df_obra_pron'}},
                            {'step':'report',
                              'func':'media_agrupada',
                              'args':{'columna':'Dias OC Pron',
                                      'por':'Modelo'}},
                             {'step':'report',
                              'func':'conteo_distinto',
                              'args':{'columna':'Modelo'}}]},
                         'Pronostico AC':{
                             'pipeline':[
                             {'step':'transform',
                              'func':'limpiar_fechas',
                              'args':{
                                  'cols':['Fecha Ultima Check Real','Fecha Real Inicio AC','Fecha Dinamica Ultima Actividad AC','Fecha Repro Dinamica Dia Ultima Actividad','Fecha Real Inicio OC']}},
                             {'step':'transform',
                              'func':'calcular_semana',
                              'args':{
                                  'fecha_ultima':'Fecha Dinamica Ultima Actividad AC',
                                  'col_resultado':'Sem AC Pron'}},
                             {'step':'transform',
                              'func':'calcular_rango',
                              'args':{
                                  'inicio':'Fecha Real Inicio AC',
                                  'fin': 'Fecha Dinamica Ultima Actividad AC',
                                  'col_resultado':'rango'}},
                             {'step':'transform',
                              'func':'sumar_festivos',
                              'args':{'festivos':'Festivos General',
                                      'clima':'Climana General',
                                      'col_resultado':'Festivos'}},
                             {'step':'transform',
                              'func':'contar_dias',
                              'args':{'col_rango':'rango',
                                      'col_festivos':'Festivos',
                                      'col_resultado':'Dias AC Pron'}},
                             {'step':'transform',
                              'func':'calcular_rango',
                              'args':{
                                  'inicio':'Fecha Real Inicio OC',
                                  'fin': 'Fecha Repro Dinamica Dia Ultima Actividad',
                                  'col_resultado':'rango2'}},
                             {'step':'transform',
                              'func':'contar_dias',
                              'args':{'col_rango':'rango2',
                                      'col_festivos':'Festivos',
                                      'col_resultado':'TC Pron'}},
                             {'step':'transform',
                              'func':'filter',
                              'args':{'func': lambda df, semana, anio: df[(df['Ultima Actividad Avanzada'] != 'OK CT') & (df['Fecha Real Ultima Actividad AC'].isna()) &
                               (df['Sem AC Pron'] == semana) & (df['Fecha Ultima Check Real'].dt.isocalendar().year == anio)]}},
                             {'step':'transform',
                              'func':'ordenar',
                              'args':{'columna':'Fecha Dinamica Ultima Actividad AC'}},
                             {'step':'transform',
                              'func':'drop_columnas',
                              'args':{'key':'df_ac_pron'}},
                             {'step':'report',
                              'func':'media_agrupada',
                              'args':{'columna':'Dias AC Pron',
                                      'por':'Modelo'}},
                             {'step':'report',
                              'func':'conteo_distinto',
                              'args':{'columna':'Modelo'}}]},
                         'Pronostico CT':{
                             'pipeline':[
                             {'step':'transform',
                              'func':'limpiar_fechas',
                              'args':{
                                  'cols':['Fecha Ultima Check Real','Fecha Real Inicio CT','Fecha Dinamica Ultima Actividad CT','Fecha Repro Dinamica Dia Ultima Actividad','Fecha Real Inicio OC']}},
                             {'step':'transform',
                              'func':'calcular_semana',
                              'args':{
                                  'fecha_ultima':'Fecha Dinamica Ultima Actividad CT',
                                  'col_resultado':'Sem CT Pron'}},
                             {'step':'transform',
                              'func':'calcular_rango',
                              'args':{
                                  'inicio':'Fecha Real Inicio CT',
                                  'fin': 'Fecha Dinamica Ultima Actividad CT',
                                  'col_resultado':'rango'}},
                             {'step':'transform',
                              'func':'sumar_festivos',
                              'args':{'festivos':'Festivos General',
                                      'clima':'Climana General',
                                      'col_resultado':'Festivos'}},
                             {'step':'transform',
                              'func':'contar_dias',
                              'args':{'col_rango':'rango',
                                      'col_festivos':'Festivos',
                                      'col_resultado':'Dias CT Pron'}},
                             {'step':'transform',
                              'func':'calcular_rango',
                              'args':{
                                  'inicio':'Fecha Real Inicio OC',
                                  'fin': 'Fecha Repro Dinamica Dia Ultima Actividad',
                                  'col_resultado':'rango2'}},
                             {'step':'transform',
                              'func':'contar_dias',
                              'args':{'col_rango':'rango2',
                                      'col_festivos':'Festivos',
                                      'col_resultado':'TC Pron'}},
                             {'step':'transform',
                              'func':'filter',
                              'args':{'func': lambda df, semana,anio: df[(df['Ultima Actividad Avanzada'] != 'OK CT') & (df['Fecha Real Ultima Actividad CT'].isna()) &
                               (df['Sem CT Pron'] == semana) & (df['Fecha Ultima Check Real'].dt.isocalendar().year == anio)]}},
                             {'step':'transform',
                              'func':'ordenar',
                              'args':{'columna':'Fecha Dinamica Ultima Actividad CT'}},
                             {'step':'transform',
                              'func':'drop_columnas',
                              'args':{'key':'df_ct_pron'}},
                             {'step':'report',
                              'func':'media_agrupada',
                              'args':{'columna':'Dias CT Pron',
                                      'por':'Modelo'}},
                             {'step':'report',
                              'func':'conteo_distinto',
                              'args':{'columna':'Modelo'}}]}}

}