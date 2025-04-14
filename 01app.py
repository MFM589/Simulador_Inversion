import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(
    page_title="Simulador de Inversión para Alimento Premium para Equinos",
    page_icon="🐴",
    layout="wide"
)

# Agregar CSS personalizado para estilo bancario/profesional
st.markdown("""
<style>
    .main {
        background-color: #ffffff;
    }
    .st-cb, .st-at, .st-cx, .st-cm {
        background-color: #f0f5ff !important;
        border-radius: 5px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .stButton button {
        background-color: #0066b2;
        color: white;
        border-radius: 4px;
        font-weight: 500;
        border: none;
        padding: 0.5rem 1rem;
    }
    h1, h2, h3 {
        color: #0066b2;
    }
    .title-container {
        background-color: #0066b2;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .title-container h1, .title-container h2, .title-container h3 {
        color: white;
        margin: 0;
    }
    .title-container p {
        color: #e6f2ff;
        margin: 10px 0 0 0;
    }
    .section-title {
        background-color: #e6f2ff;
        padding: 10px 15px;
        border-radius: 5px;
        margin: 20px 0 15px 0;
        border-left: 5px solid #0066b2;
    }
    .stMetric {
        background-color: #f0f5ff;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .stMetric label {
        color: #0066b2;
        font-weight: bold;
    }
    .st-info {
        background-color: #e6f2ff;
        border-left: 5px solid #0066b2;
    }
    .st-dc {
        border: 1px solid #e6e6e6;
        border-radius: 5px;
    }
    footer {
        color: #666666;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# Title and introduction - Using HTML for styled container
st.markdown("""
<div class="title-container">
    <h1>Alimento Premium para Equinos</h1>
    <h3>Balanceado Hidropónico Peletizado</h3>
    <p>Simulador de Inversión</p>
</div>
""", unsafe_allow_html=True)

# Company description
with st.expander("Acerca de Nuestra Startup Innovadora", expanded=True):
    st.write("""
    Somos una startup innovadora que desarrolla forraje verde hidropónico peletizado premium para equinos. 
    Nuestro enfoque revolucionario de la nutrición animal ofrece alimento de calidad superior con ventajas significativas:
    
    - Mayor valor nutricional que los alimentos tradicionales
    - Producción durante todo el año, independientemente de las condiciones climáticas
    - Proceso de producción ambientalmente sostenible
    - Reducción del consumo de agua en comparación con la agricultura tradicional
    - Mejor digestibilidad para los equinos
    
    Buscamos inversión a través de un modelo exclusivo de preventa de nuestro producto a precios promocionales. 
    Después del período de fabricación, nuestro equipo se encarga de todos los aspectos de ventas y distribución, 
    compartiendo los retornos con nuestros inversores.
    """)

# Product information
with st.expander("Nuestro Alimento Premium para Equinos - Balanceado Hidropónico Peletizado", expanded=True):
    st.write("""
    Nuestro forraje verde hidropónico peletizado premium es un producto revolucionario en la nutrición equina.
    
    **Beneficios Clave del Producto:**
    
    - Mayor contenido de proteínas y nutrientes esenciales
    - Mejor digestibilidad reduciendo el desperdicio de alimento
    - Mejora del brillo del pelaje y la salud general del caballo
    - Mayor vida útil en comparación con el forraje verde tradicional
    - Almacenamiento y servido convenientes
    - Calidad consistente durante todo el año
    
    Nuestro proceso de peletización preserva los beneficios nutricionales del forraje hidropónico fresco 
    mientras proporciona la comodidad del alimento tradicional.
    """)

# Investment model explanation
with st.expander("Explicación del Modelo de Inversión", expanded=True):
    st.write("""
    Nuestro modelo de inversión funciona a través de una preventa exclusiva de nuestro alimento premium para equinos a precios promocionales.
    
    **Cómo Funciona:**
    
    1. Los inversores reciben descuentos en nuestro producto basados en:
       - Monto de inversión (Pequeño, Mediano o Gran inversor)
       - Día de entrada durante nuestro período de preventa de 30 días
    
    2. El descuento total determina cuántas bolsas de 25kg de alimento compra el inversor al precio promocional
    
    3. Usamos la inversión para escalar la producción y fabricar el alimento peletizado para equinos
    
    4. Nuestro equipo se encarga de todo el marketing, ventas y distribución del alimento al precio final de mercado
    
    5. Los inversores reciben retornos basados en la diferencia entre su precio de compra con descuento y el precio final de mercado
    
    Este modelo ofrece a los inversores la propiedad del producto y retornos atractivos dentro de un período de 12 meses.
    """)

# Investment simulator
st.markdown("""
<div class="section-title">
    <h2>Simulador de Inversión</h2>
    <p>Utilice el simulador a continuación para calcular los retornos potenciales basados en su monto de inversión y día de entrada.</p>
</div>
""", unsafe_allow_html=True)

# Create columns for input
col1, col2 = st.columns(2)

# Input column
with col1:
    st.subheader("Parámetros de Inversión")
    
    # Investment amount with categories
    investment_amount = st.number_input("Monto de Inversión ($)", min_value=500, max_value=1000000, value=10000, step=500)
    
    # Determine investor category based on amount
    if investment_amount <= 5000:
        investor_category = "Pequeño Inversor"
        investor_discount = 0.05  # 5%
    elif investment_amount <= 15000:
        investor_category = "Mediano Inversor"
        investor_discount = 0.10  # 10%
    else:
        investor_category = "Gran Inversor" 
        investor_discount = 0.15  # 15%
        
    # Entry day selection (1-30 days)
    entry_day = st.slider("Día de Ingreso (período de pre-venta de 30 días)", min_value=1, max_value=30, value=1)
    
    # Determine entry day discount
    if 1 <= entry_day <= 5:
        entry_day_discount = 0.10  # 10%
        entry_period = "Entrada Temprana (Días 1-5)"
    elif 6 <= entry_day <= 12:
        entry_day_discount = 0.075  # 7.5%
        entry_period = "Entrada Media-Temprana (Días 6-12)"
    elif 13 <= entry_day <= 20:
        entry_day_discount = 0.05  # 5%
        entry_period = "Entrada Media-Tardía (Días 13-20)"
    else:  # 21-30
        entry_day_discount = 0.00  # 0%
        entry_period = "Entrada Tardía (Días 21-30)"
    
    # Price inputs (editable)
    initial_price = st.number_input("Precio Inicial de Bolsa (25kg)", min_value=10.0, max_value=200.0, value=55.0, step=0.5, format="%.2f")
    final_price = st.number_input("Precio Final de Mercado (25kg)", min_value=10.0, max_value=200.0, value=64.0, step=0.5, format="%.2f")
    
    # Escenario de producción
    scenario = st.radio(
        "Escenario de Producción",
        ["Real (12 meses)", "Optimista (9 meses)", "Pesimista (14 meses)"],
        horizontal=True
    )
    
    # Calculate total discount
    total_discount = investor_discount + entry_day_discount
    discounted_price = initial_price * (1 - total_discount)
    
    # Calculate number of bags purchased
    num_bags = investment_amount / discounted_price
    
    # Display information about investor category
    st.info(f"**Categoría de Inversor:** {investor_category} (Descuento: {investor_discount*100:.1f}%)")
    st.info(f"**Período de Entrada:** {entry_period} (Descuento Adicional: {entry_day_discount*100:.1f}%)")
    st.info(f"**Descuento Total:** {total_discount*100:.1f}%")

# Results column
with col2:
    st.subheader("Resultados de la Inversión")
    
    # Determinar el período total basado en el escenario seleccionado
    if scenario == "Optimista (9 meses)":
        total_months = 9
        production_time_text = "9 meses (escenario optimista)"
    elif scenario == "Pesimista (14 meses)":
        total_months = 14
        production_time_text = "14 meses (escenario pesimista)"
    else:  # Real (12 meses)
        total_months = 12
        production_time_text = "12 meses (escenario real)"
    
    # Ajustar el período de fabricación proporcionalmente (manteniendo aproximadamente la mitad del tiempo)
    manufacturing_period = total_months // 2  # Manufacturing period is half of total time
    
    # Calculate investment metrics
    discounted_bag_price = initial_price * (1 - total_discount)
    total_investment = num_bags * discounted_bag_price
    future_value = num_bags * final_price
    total_profit = future_value - total_investment
    
    # Calcular ROI anual, mensual y diario
    roi_percentage = (total_profit / total_investment) * 100
    
    # Ajustar ROI al período real según el escenario seleccionado
    roi_monthly_percentage = roi_percentage / total_months
    roi_daily_percentage = roi_percentage / (total_months * 30)  # aproximadamente 30 días por mes
    
    # Calcular valores monetarios del ROI
    roi_monthly_value = total_profit / total_months
    roi_daily_value = total_profit / (total_months * 30)
    
    # Calcular ROI anualizado (proyectado a 12 meses)
    roi_annualized_percentage = roi_monthly_percentage * 12
    roi_annualized_value = roi_monthly_value * 12
    
    # Adjust total investment to match exactly the input amount
    # (small differences might occur due to floating point calculations)
    total_investment = investment_amount
    
    # Display metrics
    st.metric("Precio con Descuento por Bolsa", f"${discounted_bag_price:.2f}")
    st.metric("Número de Bolsas Adquiridas", f"{num_bags:.2f}")
    st.metric("Inversión Total", f"${total_investment:,.2f}")
    st.metric("Valor Futuro en Mercado", f"${future_value:,.2f}")
    st.metric(f"Ganancia Total ({production_time_text})", f"${total_profit:,.2f}")
    
    # Mostrar ROI anual destacado
    st.markdown("""
    <style>
    .highlight-roi {
        background-color: #0066b2;
        color: white;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        font-weight: bold;
    }
    .roi-card {
        background-color: #f0f5ff;
        border: 1px solid #0066b2;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .roi-title {
        font-weight: bold;
        color: #0066b2;
        font-size: 16px;
    }
    .roi-value {
        font-size: 14px;
        margin-top: 5px;
    }
    .roi-highlight {
        background-color: #0066b2;
        color: white;
        padding: 5px;
        border-radius: 3px;
        display: inline-block;
        margin-top: 5px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # ROI Total
    st.markdown(f"""
    <div class="highlight-roi">
        ROI Total: {roi_percentage:.2f}% (${total_profit:,.2f})
    </div>
    """, unsafe_allow_html=True)
    
    # ROI Anualizado (proyectado a 12 meses)
    st.markdown(f"""
    <div class="roi-card">
        <div class="roi-title">ROI Anualizado (Proyectado a 12 Meses)</div>
        <div class="roi-value">Si este ritmo mensual se mantuviera durante un año completo, el ROI sería:</div>
        <div class="roi-highlight">{roi_annualized_percentage:.2f}% (${roi_annualized_value:,.2f})</div>
    </div>
    """, unsafe_allow_html=True)
    
    # ROI Mensual y Diario en un solo cuadro
    st.markdown(f"""
    <div class="roi-card">
        <div class="roi-title">ROI Detallado</div>
        <div class="roi-value">
            <strong>Mensual:</strong> {roi_monthly_percentage:.2f}% (${roi_monthly_value:,.2f})
            <br>
            <strong>Diario:</strong> {roi_daily_percentage:.2f}% (${roi_daily_value:,.2f})
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Shows manufacturing and sales period
    st.info(f"Los retornos se realizan cuando vendemos su alimento después del período de fabricación (comenzando aproximadamente a partir del mes {manufacturing_period})")

# Visualization of investment growth
st.markdown("""
<div class="section-title">
    <h2>Visualización del Crecimiento de la Inversión</h2>
</div>
""", unsafe_allow_html=True)

# Create data for the period
months = list(range(total_months + 1))

# Calculate monthly values
investment_values = [investment_amount] * (manufacturing_period + 1)  # No change during manufacturing
for month in range(manufacturing_period + 1, total_months + 1):
    # For simplicity, we'll use a linear growth model to the final value
    progress_percentage = (month - manufacturing_period) / (total_months - manufacturing_period)
    current_value = investment_amount + (progress_percentage * total_profit)
    investment_values.append(current_value)

# Create DataFrame for visualization
df = pd.DataFrame({
    'Month': months,
    'Value': investment_values
})

# Add manufacturing period marker to DataFrame
df['Phase'] = 'Fase de Retornos'
df.loc[df['Month'] <= manufacturing_period, 'Phase'] = 'Fase de Fabricación'

# Plot using Plotly
fig = px.line(
    df, 
    x='Month', 
    y='Value',
    color='Phase',
    title=f'Crecimiento de la Inversión Durante {total_months} Meses',
    labels={'Value': 'Valor de la Inversión ($)', 'Month': 'Mes'},
    color_discrete_map={'Fase de Fabricación': 'gray', 'Fase de Retornos': 'green'}
)

# Add initial investment marker
fig.add_trace(
    go.Scatter(
        x=[0],
        y=[investment_amount],
        mode='markers',
        marker=dict(size=10, color='blue'),
        name='Inversión Inicial'
    )
)

# Add final value marker
fig.add_trace(
    go.Scatter(
        x=[total_months],
        y=[investment_amount + total_profit],
        mode='markers',
        marker=dict(size=10, color='red'),
        name='Valor Final'
    )
)

# Customize layout
fig.update_layout(
    hovermode='x unified',
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# Comparison of different investment amounts
st.markdown("""
<div class="section-title">
    <h2>Comparación de Diferentes Montos de Inversión</h2>
    <p>Vea cómo diferentes montos de inversión se comportan con los mismos parámetros de descuento.</p>
</div>
""", unsafe_allow_html=True)

# Create comparison data
comparison_amounts = [investment_amount/2, investment_amount, investment_amount*2]
comparison_labels = [f"${amount:,.0f}" for amount in comparison_amounts]

comparison_data = []
for amount in comparison_amounts:
    # Calculate metrics for this amount
    if amount <= 5000:
        inv_discount = 0.05  # 5%
    elif amount <= 15000:
        inv_discount = 0.10  # 10%
    else:
        inv_discount = 0.15  # 15%
    
    # Use the same entry day discount
    comp_total_discount = inv_discount + entry_day_discount
    comp_discounted_price = initial_price * (1 - comp_total_discount)
    comp_num_bags = amount / comp_discounted_price
    comp_future_value = comp_num_bags * final_price
    comp_profit = comp_future_value - amount
    
    # Calculate monthly values
    values = [amount] * (manufacturing_period + 1)  # No change during manufacturing
    for month in range(manufacturing_period + 1, total_months + 1):
        progress_percentage = (month - manufacturing_period) / (total_months - manufacturing_period)
        current_value = amount + (progress_percentage * comp_profit)
        values.append(current_value)
    
    comparison_data.append(values)

# Create comparison DataFrame
comparison_df = pd.DataFrame({
    'Month': months,
    comparison_labels[0]: comparison_data[0],
    comparison_labels[1]: comparison_data[1],
    comparison_labels[2]: comparison_data[2]
})

# Melt the DataFrame for Plotly
comparison_df_melted = pd.melt(
    comparison_df, 
    id_vars=['Month'], 
    value_vars=comparison_labels,
    var_name='Monto de Inversión',
    value_name='Valor'
)

# Plot comparison
fig3 = px.line(
    comparison_df_melted,
    x='Month',
    y='Valor',
    color='Monto de Inversión',
    title=f'Comparación de Diferentes Montos de Inversión ({production_time_text})',
    labels={'Valor': 'Valor de la Inversión ($)', 'Month': 'Mes'}
)

# Add vertical line at manufacturing period end
fig3.add_vline(
    x=manufacturing_period, 
    line_dash="dash", 
    line_color="gray",
    annotation_text="Inicio de Retornos",
    annotation_position="top right"
)

fig3.update_layout(height=500)
st.plotly_chart(fig3, use_container_width=True)

# Investment breakdown visualization
st.markdown("""
<div class="section-title">
    <h2>Desglose de la Inversión</h2>
</div>
""", unsafe_allow_html=True)

# Create a pie chart showing the breakdown of bags by discounted price
fig4 = go.Figure(data=[go.Pie(
    labels=['Inversión', 'Ganancia'],
    values=[investment_amount, total_profit],
    hole=.4,
    marker_colors=['#1f77b4', '#2ca02c']
)])

fig4.update_layout(
    title_text="Desglose de Inversión vs. Ganancia",
    height=400
)

st.plotly_chart(fig4, use_container_width=True)

# FAQ section
st.markdown("""
<div class="section-title">
    <h2>Preguntas Frecuentes</h2>
</div>
""", unsafe_allow_html=True)

with st.expander("¿Cuál es el monto mínimo de inversión?"):
    st.write("""
    El monto mínimo de inversión es de U$D 500 (quinientos Dólares). Esto le permite participar en nuestro programa exclusivo de 
    pre-venta y recibir retornos en dólares basados en su inversión.
    
    Las categorías de inversión son:
    - Pequeño Inversor: U$D 500 a U$D 5,000 (descuento del 5%)
    - Mediano Inversor: U$D 5,001 a U$D 15,000 (descuento del 10%)
    - Gran Inversor: más de U$D 15,000 (descuento del 15%)
    """)

with st.expander("¿Cómo funciona el modelo de descuentos?"):
    st.write("""
    Nuestro modelo opera con dos tipos de descuentos que se suman:
    
    1. **Descuento por categoría de inversor**:
       - Pequeño Inversor: 5% de descuento
       - Mediano Inversor: 10% de descuento
       - Gran Inversor: 15% de descuento
    
    2. **Descuento por día de ingreso a la pre-venta** (período de 30 días):
       - Días 1-5: 10% de descuento adicional
       - Días 6-12: 7.5% de descuento adicional
       - Días 13-20: 5% de descuento adicional
       - Días 21-30: sin descuento adicional
    
    El descuento total se aplica al precio inicial de pre-venta de cada bolsa de 25kg, permitiéndole adquirir 
    más bolsas con su inversión.
    """)

with st.expander("¿Cómo y cuándo se distribuyen los retornos?"):
    st.write("""
    Los retornos se realizan una vez que vendemos las bolsas de alimento al precio de mercado final:
    
    1. Usted invierte y adquiere bolsas de 25kg a un precio con descuento
    2. Nosotros fabricamos el producto durante el período de producción (aproximadamente a partir del mes 6 comenzamos la producción del alimento)
    3. Luego vendemos el producto al precio final de mercado
    4. Usted recibe el valor completo de venta de sus bolsas
    
    La ganancia se genera por la diferencia entre el precio con descuento que usted pagó y el precio 
    final al que nosotros vendemos el producto en el mercado.
    """)

with st.expander("¿Qué riesgos están involucrados?"):
    st.write("""
    Como cualquier inversión, hay riesgos involucrados:
    
    - Riesgo de aceptación del mercado para productos innovadores
    - Desafíos de escalamiento de producción
    - Variables agrícolas y de cadena de suministro
    - Consideraciones regulatorias para productos de alimentación animal
    
    Mitigamos estos riesgos a través de:
    
    - Extensas pruebas de producto y certificación
    - Equipo experimentado en agricultura y producción
    - Proyecciones conservadoras en nuestros modelos financieros
    - Canales de distribución diversificados
    - Vinculaciones establecidas con Clubes Hípicos, Clubes de Polo y Clubes de Carreras que tienen una necesidad actual de alimento premium con calidad nutritiva exclusiva
    """)

with st.expander("¿Puedo aumentar mi inversión más adelante?"):
    st.write("""
    Sí, puede aumentar su monto de inversión en cualquier momento, sujeto a disponibilidad en la etapa 
    de pre-venta actual. Además, se obtienen beneficios por reinversión y fidelidad.
    
    Las inversiones adicionales pueden estar sujetas a los términos de la etapa de entrada actual, que 
    pueden ser diferentes a sus términos originales.
    
    Por favor, contacte a nuestro equipo de relaciones con inversores para discutir arreglos específicos 
    para aumentar su inversión y conocer los beneficios adicionales por reinversión y fidelidad.
    """)

with st.expander("¿Qué hace diferente a este alimento para equinos de otros en el mercado?"):
    st.write("""
    Es un alimento innovador hecho a base de Forraje Verde Hidropónico (FVH) que lo convierte único en el mercado. Nuestro forraje verde hidropónico peletizado premium representa una innovación significativa en la nutrición equina:
    
    - Mayor densidad nutricional a través de condiciones de cultivo hidropónico controladas
    - Calidad consistente durante todo el año, independientemente de las variaciones estacionales
    - Nuestro proceso de peletización patentado preserva los nutrientes biodisponibles que típicamente se pierden en el procesamiento convencional de alimentos
    - Menor impacto ambiental a través de la conservación del agua y la eliminación de pesticidas
    - Mejor digestibilidad que lleva a una mejor absorción de nutrientes y menos desperdicio
    
    Estas ventajas crean un producto premium con una demanda creciente en el mercado ecuestre.
    """)

# Contact section
st.markdown("""
<div class="section-title">
    <h2>¿Listo para invertir?</h2>
    <p>Use este simulador para explorar diferentes escenarios de inversión. Cuando esté listo para discutir
oportunidades de inversión o tenga preguntas, por favor contacte a nuestro equipo.</p>
</div>
""", unsafe_allow_html=True)

# Contact form
with st.form("contact_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Nombre Completo")
        email = st.text_input("Correo Electrónico")
    with col2:
        phone = st.text_input("Número de Teléfono (opcional)")
        investment_interest = st.selectbox(
            "Nivel de Interés en Inversión",
            ["Solo explorando", "Interesado, necesito más información", "Listo para invertir pronto", "Listo para invertir ahora"]
        )
    
    message = st.text_area("Mensaje o Preguntas")
    submitted = st.form_submit_button("Enviar Consulta")
    
    if submitted:
        st.success("¡Gracias por su consulta! Nuestro equipo de relaciones con inversores se pondrá en contacto con usted en breve.")

# Footer
st.markdown("---")
st.markdown("© 2023 Alimento Premium para Equinos | Soluciones Innovadoras de Nutrición Equina")
