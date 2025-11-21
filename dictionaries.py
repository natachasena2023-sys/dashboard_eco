# dictionaries.py
"""
Diccionarios globales utilizados para normalización, colores y categorización
en el dashboard de Negocios Verdes / Basura Cero.
"""

# ---Diccionario canónico por departamento---
DEPARTMENT_CANONICAL = {
    "AMAZONAS": "AMAZONAS", "ANTIOQUIA": "ANTIOQUIA", "ARAUCA": "ARAUCA",
    "ATLANTICO": "ATLÁNTICO", "ATLÁNTICO": "ATLÁNTICO", "BOLIVAR": "BOLÍVAR",
    "BOLÍVAR": "BOLÍVAR", "BOGOTA": "BOGOTÁ, D.C.", "BOGOTA DC": "BOGOTÁ, D.C.",
    "BOGOTA D C": "BOGOTÁ, D.C.", "BOGOTA D.C": "BOGOTÁ, D.C.", "BOGOTÁ": "BOGOTÁ, D.C.",
    "BOGOTÁ D.C.": "BOGOTÁ, D.C.", "BOYACA": "BOYACÁ", "BOYACÁ": "BOYACÁ",
    "CALDAS": "CALDAS", "CAQUETA": "CAQUETÁ", "CAQUETÁ": "CAQUETÁ", "CASANARE": "CASANARE",
    "CAUCA": "CAUCA", "CESAR": "CESAR", "CHOCO": "CHOCÓ", "CHOCÓ": "CHOCÓ",
    "CORDOBA": "CÓRDOBA", "CÓRDOBA": "CÓRDOBA", "CUNDINAMARCA": "CUNDINAMARCA",
    "GUAINIA": "GUAINÍA", "GUAINÍA": "GUAINÍA", "GUAJIRA": "LA GUAJIRA",
    "LA GUAJIRA": "LA GUAJIRA", "GUAVIARE": "GUAVIARE", "HUILA": "HUILA",
    "MAGDALENA": "MAGDALENA", "META": "META", "NARINO": "NARIÑO", "NARIÑO": "NARIÑO",
    "NORTE DE SANTANDER": "NORTE DE SANTANDER", "PUTUMAYO": "PUTUMAYO",
    "QUINDIO": "QUINDÍO", "QUINDÍO": "QUINDÍO", "RISARALDA": "RISARALDA",
    "SAN ANDRES": "SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA",
    "SAN ANDRÉS": "SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA",
    "SAN ANDRES Y PROVIDENCIA": "SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA",
    "ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA":
        "SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA",
    "ARCHIPIÉLAGO DE SAN ANDRÉS PROVIDENCIA Y SANTA CATALINA":
        "SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA",
    "ARCHIPIELAGO DE SAN ANDRES, PROVIDENCIA Y SANTA CATALINA":
        "SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA",
    "ARCHIPIÉLAGO DE SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA":
        "SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA",
    "SANTANDER": "SANTANDER", "SUCRE": "SUCRE", "TOLIMA": "TOLIMA",
    "VALLE": "VALLE DEL CAUCA", "VALLE DEL CAUCA": "VALLE DEL CAUCA",
    "VAUPES": "VAUPÉS", "VAUPÉS": "VAUPÉS", "VICHADA": "VICHADA",
}

# Diccionario que almacena las coordenadas geográficas (latitud y longitud)
DEPARTMENT_COORDS = {
    "AMAZONAS": {"lat": -1.566, "lon": -72.640},
    "ANTIOQUIA": {"lat": 7.1986, "lon": -75.3412},
    "ARAUCA": {"lat": 6.5519, "lon": -70.9410},
    "ATLÁNTICO": {"lat": 10.6966, "lon": -74.8741},
    "BOGOTÁ, D.C.": {"lat": 4.6097, "lon": -74.0817},
    "BOLÍVAR": {"lat": 9.1938, "lon": -74.9120},
    "BOYACÁ": {"lat": 5.5450, "lon": -73.3678},
    "CALDAS": {"lat": 5.2983, "lon": -75.2479},
    "CAQUETÁ": {"lat": 0.8699, "lon": -73.8419},
    "CASANARE": {"lat": 5.7589, "lon": -71.5724},
    "CAUCA": {"lat": 2.4068, "lon": -76.7250},
    "CESAR": {"lat": 9.3373, "lon": -73.6536},
    "CHOCÓ": {"lat": 5.6947, "lon": -76.6583},
    "CÓRDOBA": {"lat": 8.7496, "lon": -75.8735},
    "CUNDINAMARCA": {"lat": 4.8143, "lon": -74.3540},
    "GUAINÍA": {"lat": 2.5658, "lon": -68.5247},
    "LA GUAJIRA": {"lat": 11.3548, "lon": -72.5205},
    "GUAVIARE": {"lat": 1.8537, "lon": -72.9087},
    "HUILA": {"lat": 2.9273, "lon": -75.2819},
    "MAGDALENA": {"lat": 10.2373, "lon": -74.2064},
    "META": {"lat": 3.4760, "lon": -73.7517},
    "NARIÑO": {"lat": 1.2894, "lon": -77.3570},
    "NORTE DE SANTANDER": {"lat": 7.9463, "lon": -72.8988},
    "PUTUMAYO": {"lat": 0.4416, "lon": -76.6270},
    "QUINDÍO": {"lat": 4.4610, "lon": -75.6674},
    "RISARALDA": {"lat": 4.9820, "lon": -75.6039},
    "SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA": {"lat": 12.5589, "lon": -81.7188},
    "SANTANDER": {"lat": 6.6437, "lon": -73.6531},
    "SUCRE": {"lat": 9.3164, "lon": -75.3972},
    "TOLIMA": {"lat": 4.0925, "lon": -75.1545},
    "VALLE DEL CAUCA": {"lat": 3.5297, "lon": -76.3035},
    "VAUPÉS": {"lat": 0.8554, "lon": -70.8110},
    "VICHADA": {"lat": 4.4234, "lon": -69.2878},
}

#---Diccionario de colores por departamento---
DEPARTMENT_COLORS = {
    "AMAZONAS": "#A6CEE3", "ANTIOQUIA": "#1F78B4", "ARAUCA": "#B2DF8A",
    "ATLÁNTICO": "#33A02C", "BOLÍVAR": "#FB9A99", "BOYACÁ": "#E31A1C",
    "CALDAS": "#FDBF6F", "CAQUETÁ": "#FF7F00", "CASANARE": "#CAB2D6",
    "CAUCA": "#6A3D9A", "CESAR": "#FFFF99", "CHOCÓ": "#B15928",
    "CÓRDOBA": "#8DD3C7", "CUNDINAMARCA": "#FFFFB3", "GUAINÍA": "#BEBADA",
    "GUAVIARE": "#FB8072", "HUILA": "#80B1D3", "LA GUAJIRA": "#FDB462",
    "MAGDALENA": "#B3DE69", "META": "#FCCDE5", "NARIÑO": "#D9D9D9",
    "NORTE DE SANTANDER": "#BC80BD", "PUTUMAYO": "#CCEBC5",
    "QUINDÍO": "#FFED6F", "RISARALDA": "#1B9E77",
    "SAN ANDRÉS, PROVIDENCIA Y SANTA CATALINA": "#D95F02",
    "SANTANDER": "#7570B3", "SUCRE": "#E7298A", "TOLIMA": "#66A61E",
    "VALLE DEL CAUCA": "#E6AB02", "VAUPÉS": "#A6761D", "VICHADA": "#666666",
}

#---Diccionario de colores por región---
REGION_COLORS = {
    "CARIBE": "#FFD92F", "ANDINA": "#1F78B4",
    "PACÍFICO": "#33A02C", "ORINOQUÍA": "#FB9A99",
    "AMAZONÍA": "#B2DF8A",
}

# --- Diccionario para inferir región desde autoridad ambiental ---
MAPEO_REGION = {
    "AMVA": "ANDINA", "CAM": "ANDINA", "CAR": "ANDINA", "CARDER": "ANDINA",
    "CARDIQUE": "CARIBE", "CARSUCRE": "CARIBE", "CAS": "ANDINA",
    "CDA": "AMAZONÍA", "CDMB": "ANDINA", "CODECHOCÓ": "PACÍFICO",
    "CORALINA": "INSULAR", "CORANTIOQUIA": "ANDINA",
    "CORMACARENA": "ORINOQUÍA", "CORNARE": "ANDINA", "CORPAMAG": "CARIBE",
    "CORPOAMAZONÍA": "AMAZONÍA", "CORPOBOYACÁ": "ANDINA",
    "CORPOCALDAS": "ANDINA", "CORPOCESAR": "CARIBE",
    "CORPOCHIVOR": "ANDINA", "CORPOGUAJIRA": "CARIBE",
    "CORPOGUAVIO": "ANDINA", "CORPOMOJANA": "CARIBE",
    "CORPONARIÑO": "PACÍFICO", "CORPONOR": "CARIBE",
    "CORPORINOQUÍA": "ORINOQUÍA", "CORPOURABÁ": "PACÍFICO",
    "CORTOLIMA": "ANDINA", "CRA": "CARIBE", "CRC": "PACÍFICO",
    "CRQ": "ANDINA", "CSB": "CARIBE", "CVC": "PACÍFICO", "CVS": "CARIBE",
    "DADSA": "ANDINA", "DAGMA": "ANDINA",
    "EPA BARRANQUILLA VERDE": "CARIBE",
    "EPA BUENAVENTURA": "PACÍFICO",
    "EPA CARTAGENA": "CARIBE", "SDA": "ANDINA",
}

# Diccionario de categorías y palabras clave detectables
categorias_basura_cero = {
    "Reciclaje/Reutilización": ["recicl", "reutiliz", "reuso", "aprovech"],
    "Compostaje/Biomasa": ["compost", "orgánic", "biomasa", "abono"],
    "Producción limpia": ["producción limpia", "transformación sostenible",
                          "ecodiseño", "eficiencia"],
    "Economía circular": ["economía circular", "ciclo cerrado", "remanufactura"],
    "Bioinsumos/Bioproductos": ["bioinsumo", "biodegrad", "biofertiliz",
                                "bioproduct"],
    "Energía renovable": ["energía solar", "energía renovable", "biogás",
                          "panel solar", "fotovoltaic"],
    "Agroecología/Sostenibilidad rural": [
        "agroecolog", "agroindustria sostenible", "sostenible", "ecológica"
    ],
}
