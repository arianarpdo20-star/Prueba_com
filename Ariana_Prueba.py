import streamlit as st

st.set_page_config(page_title="Prueba de Negocios Digitales", page_icon="💻")

PREGUNTAS = [
    {
        "pregunta": "¿Qué mide la tasa de conversión en un e-commerce?",
        "opciones": [
            "El porcentaje de visitantes que realizan una compra",
            "El costo de cada clic en un anuncio",
            "El número de seguidores en redes sociales",
            "El tiempo que un usuario pasa en la web",
        ],
        "correcta": 0,
        "explicacion": "La tasa de conversión es el porcentaje de visitas que terminan en una acción deseada, normalmente una compra.",
    },
    {
        "pregunta": "¿Qué significa CAC en marketing digital?",
        "opciones": [
            "Costo de Adquisición de Cliente",
            "Clic Antes de Compra",
            "Canal de Atención al Cliente",
            "Calidad Acumulada del Contenido",
        ],
        "correcta": 0,
        "explicacion": "CAC (Customer Acquisition Cost) es lo que cuesta, en promedio, conseguir un nuevo cliente.",
    },
    {
        "pregunta": "¿Qué es el LTV de un cliente?",
        "opciones": [
            "El valor total que un cliente genera para la empresa durante toda su relación",
            "El monto de su primera compra",
            "El número de veces que visitó la web",
            "El descuento máximo que se le aplica",
        ],
        "correcta": 0,
        "explicacion": "LTV (Lifetime Value) es el ingreso total esperado de un cliente a lo largo de su relación con la empresa.",
    },
    {
        "pregunta": "¿Qué modelo de negocio cobra una suscripción periódica por acceder a un software en la nube?",
        "opciones": [
            "SaaS",
            "Dropshipping",
            "Marketplace de comisiones",
            "Venta de licencias perpetuas",
        ],
        "correcta": 0,
        "explicacion": "SaaS (Software as a Service) entrega software en la nube mediante pagos recurrentes, generalmente mensuales o anuales.",
    },
    {
        "pregunta": "¿Qué indica una tasa de rebote (bounce rate) alta en una página web?",
        "opciones": [
            "Que muchos usuarios salen de la página sin interactuar con ella",
            "Que la página tiene muchas compras",
            "Que el sitio carga demasiado rápido",
            "Que el tráfico proviene solo de redes sociales",
        ],
        "correcta": 0,
        "explicacion": "El bounce rate mide las sesiones de una sola página. Un valor alto suele indicar contenido poco relevante o una mala experiencia de usuario.",
    },
]

st.title("💻 Prueba de Negocios Digitales")
st.write("Responde las preguntas y presiona **Verificar respuestas** para conocer tu puntaje.")

with st.form("prueba"):
    respuestas = {}
    for i, p in enumerate(PREGUNTAS):
        st.markdown(f"**{i + 1}. {p['pregunta']}**")
        respuestas[i] = st.radio(
            "Selecciona una opción",
            options=range(len(p["opciones"])),
            format_func=lambda j, ops=p["opciones"]: ops[j],
            index=None,
            key=f"preg_{i}",
            label_visibility="collapsed",
        )
        st.write("")
    enviado = st.form_submit_button("Verificar respuestas", type="primary")

if enviado:
    if any(r is None for r in respuestas.values()):
        st.warning("Responde todas las preguntas antes de verificar.")
    else:
        correctas = 0
        for i, p in enumerate(PREGUNTAS):
            if respuestas[i] == p["correcta"]:
                correctas += 1
                st.success(f"✅ Pregunta {i + 1}: correcta. {p['explicacion']}")
            else:
                st.error(
                    f"❌ Pregunta {i + 1}: incorrecta. La respuesta correcta es "
                    f"**{p['opciones'][p['correcta']]}**. {p['explicacion']}"
                )
        total = len(PREGUNTAS)
        st.subheader(f"Puntaje: {correctas} de {total}")
        st.progress(correctas / total)
