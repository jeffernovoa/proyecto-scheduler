def calcular_metricas(procesos):
    tiempos = {
        'respuesta': [],
        'retorno': [],
        'espera': []
    }

    for p in procesos:
        respuesta = p.tiempo_inicio - p.tiempo_llegada
        retorno = p.tiempo_fin - p.tiempo_llegada
        espera = retorno - p.duracion

        tiempos['respuesta'].append(respuesta)
        tiempos['retorno'].append(retorno)
        tiempos['espera'].append(espera)

    return {
        'respuesta_prom': sum(tiempos['respuesta']) / len(procesos),
        'retorno_prom': sum(tiempos['retorno']) / len(procesos),
        'espera_prom': sum(tiempos['espera']) / len(procesos)
    }
