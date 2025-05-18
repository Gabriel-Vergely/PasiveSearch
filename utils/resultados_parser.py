def unir_resultados(*resultados: str) -> str:
    """
    Recibe varios textos de análisis y los concatena en un único reporte con separadores.
    """
    separador = "\n\n" + "="*40 + "\n\n"
    reporte_completo = separador.join(resultados)
    return reporte_completo
