# ═══════════════════════════════════════════════════════════
#  🎓 Sistema de Gestión de Alumnos
# ═══════════════════════════════════════════════════════════

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ── Configuración de la página ──────────────────────────────
st.set_page_config(
    page_title="Sistema de Alumnos",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── CSS personalizado — diseño dorado y esmeralda ───────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&display=swap');

/* Fondo general */
.stApp {
    background: #0A0F0D;
    font-family: 'DM Sans', sans-serif;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0D1A14 0%, #081009 100%);
    border-right: 1px solid rgba(212,175,55,0.2);
}
[data-testid="stSidebar"] * {
    color: #E8E0D0 !important;
}

/* Título principal */
.titulo-main {
    font-family: 'Playfair Display', serif;
    font-size: 2.8rem;
    font-weight: 900;
    background: linear-gradient(135deg, #D4AF37, #F5E6A3, #D4AF37);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 0;
    text-shadow: none;
    letter-spacing: -1px;
}

.subtitulo-main {
    text-align: center;
    color: rgba(212,175,55,0.6);
    font-size: 0.85rem;
    letter-spacing: 4px;
    text-transform: uppercase;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    margin-top: 4px;
    margin-bottom: 30px;
}

/* Tarjetas de stats */
.stat-card {
    background: linear-gradient(135deg, #0D1A14, #112018);
    border: 1px solid rgba(212,175,55,0.3);
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    margin-bottom: 16px;
}
.stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    font-weight: 900;
    color: #D4AF37;
    display: block;
    line-height: 1;
}
.stat-lbl {
    color: rgba(232,224,208,0.5);
    font-size: 0.75rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 4px;
    display: block;
}

/* Encabezados de sección */
.seccion-header {
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem;
    color: #D4AF37;
    border-bottom: 1px solid rgba(212,175,55,0.25);
    padding-bottom: 8px;
    margin-bottom: 20px;
    margin-top: 10px;
}

/* Tabla de alumnos */
.alumno-card {
    background: linear-gradient(135deg, #0D1A14, #0F1E16);
    border: 1px solid rgba(212,175,55,0.2);
    border-radius: 14px;
    padding: 18px 22px;
    margin-bottom: 12px;
    transition: all 0.3s;
}
.alumno-card:hover {
    border-color: rgba(212,175,55,0.5);
}
.alumno-nombre {
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    color: #F5E6A3;
    font-weight: 700;
}
.alumno-info {
    color: rgba(232,224,208,0.55);
    font-size: 0.82rem;
    margin-top: 3px;
}
.nota-badge {
    display: inline-block;
    padding: 3px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    margin: 2px;
}
.habilidad-badge {
    display: inline-block;
    background: rgba(212,175,55,0.12);
    border: 1px solid rgba(212,175,55,0.3);
    color: #D4AF37;
    padding: 3px 12px;
    border-radius: 20px;
    font-size: 0.78rem;
    margin: 2px;
}

/* Botones Streamlit */
.stButton > button {
    background: linear-gradient(135deg, #1A3A2A, #0F2A1C) !important;
    color: #D4AF37 !important;
    border: 1px solid rgba(212,175,55,0.4) !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
    padding: 8px 20px !important;
}
.stButton > button:hover {
    border-color: #D4AF37 !important;
    background: linear-gradient(135deg, #1F4A34, #142E20) !important;
}

/* Inputs */
.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: #0D1A14 !important;
    border: 1px solid rgba(212,175,55,0.25) !important;
    color: #E8E0D0 !important;
    border-radius: 10px !important;
}

/* Éxito y advertencia */
.stSuccess {
    background: rgba(52,211,153,0.1) !important;
    border: 1px solid rgba(52,211,153,0.3) !important;
    border-radius: 10px !important;
}
.stWarning {
    background: rgba(212,175,55,0.1) !important;
    border: 1px solid rgba(212,175,55,0.3) !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: #0D1A14;
    border-radius: 12px;
    padding: 4px;
    gap: 4px;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: rgba(232,224,208,0.5) !important;
    border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #1A3A2A, #112018) !important;
    color: #D4AF37 !important;
    border: 1px solid rgba(212,175,55,0.3) !important;
}

/* Ocultar elementos de Streamlit */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── MATERIAS Y HABILIDADES ──────────────────────────────────
MATERIAS = [
    "Muestreo",
    "Cálculo Integral",
    "Estructura de Datos",
    "Defensa y Seguridad Nacional",
    "Inglés",
    "Distribución de Probabilidades",
]

HABILIDADES = ["Liderazgo", "Tecnología", "Trabajo en Equipo", "Oratoria"]

# ── ESTADO INICIAL ──────────────────────────────────────────
if "alumnos" not in st.session_state:
    st.session_state.alumnos = []

# ── HELPER: color de nota ────────────────────────────────────
def color_nota(nota):
    if nota >= 17:   return "#34D399", "#052E16"   # verde brillante
    elif nota >= 14: return "#D4AF37", "#1A1200"   # dorado
    elif nota >= 11: return "#FB923C", "#1C0A00"   # naranja
    else:            return "#F87171", "#1C0000"   # rojo

# ── HELPER: promedio ─────────────────────────────────────────
def promedio(notas_dict):
    vals = [v for v in notas_dict.values() if v > 0]
    return round(sum(vals) / len(vals), 1) if vals else 0.0

# ══════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="titulo-main">🎓 Sistema de Alumnos</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo-main">Registro · Notas · Habilidades · Reportes</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# SIDEBAR — STATS
# ══════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("### 📊 Resumen General")
    st.markdown("---")

    total = len(st.session_state.alumnos)
    if total > 0:
        promedios = [promedio(a["notas"]) for a in st.session_state.alumnos]
        aprobados = sum(1 for p in promedios if p >= 11)
        prom_gral = round(sum(promedios) / total, 1)
    else:
        aprobados = 0
        prom_gral = 0.0

    st.markdown(f"""
    <div class="stat-card">
        <span class="stat-num">{total}</span>
        <span class="stat-lbl">Total Alumnos</span>
    </div>
    <div class="stat-card">
        <span class="stat-num">{aprobados}</span>
        <span class="stat-lbl">Aprobados</span>
    </div>
    <div class="stat-card">
        <span class="stat-num">{prom_gral}</span>
        <span class="stat-lbl">Promedio General</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🏆 Habilidades más comunes")
    if total > 0:
        conteo = {h: 0 for h in HABILIDADES}
        for a in st.session_state.alumnos:
            for h in a.get("habilidades", []):
                if h in conteo:
                    conteo[h] += 1
        for h, c in sorted(conteo.items(), key=lambda x: -x[1]):
            pct = int((c / total) * 100) if total > 0 else 0
            st.markdown(f"""
            <div style="margin-bottom:8px;">
                <div style="display:flex;justify-content:space-between;color:#E8E0D0;font-size:0.82rem;">
                    <span>{h}</span><span style="color:#D4AF37;">{c}</span>
                </div>
                <div style="background:rgba(212,175,55,0.12);border-radius:4px;height:5px;margin-top:3px;">
                    <div style="background:#D4AF37;width:{pct}%;height:5px;border-radius:4px;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown('<p style="color:rgba(232,224,208,0.35);font-size:0.8rem;">Sin datos aún</p>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# TABS PRINCIPALES
# ══════════════════════════════════════════════════════════════
tab1, tab2, tab3, tab4 = st.tabs([
    "➕  Registrar Alumno",
    "📋  Lista de Alumnos",
    "📈  Gráficos",
    "📄  Reportes",
])

# ══════════════════════════════════════════════════════════════
# TAB 1 — REGISTRAR ALUMNO
# ══════════════════════════════════════════════════════════════
with tab1:
    st.markdown('<div class="seccion-header">Registrar Nuevo Alumno</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("**📝 Datos Personales**")
        nombre = st.text_input("Nombre completo", placeholder="Ej: María García López")
        codigo = st.text_input("Código de alumno", placeholder="Ej: 2024-0001")

        col_a, col_b = st.columns(2)
        with col_a:
            ciclo = st.selectbox("Ciclo", ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"])
        with col_b:
            seccion = st.selectbox("Sección", ["A", "B", "C", "D"])

        st.markdown("**🌟 Habilidades y Talentos**")
        habilidades_sel = st.multiselect(
            "Selecciona habilidades",
            HABILIDADES,
            help="Puedes elegir más de una"
        )

        observacion = st.text_area(
            "Observaciones",
            placeholder="Notas adicionales sobre el alumno...",
            height=80
        )

    with col2:
        st.markdown("**📚 Notas por Materia** *(escala 0 — 20)*")
        notas = {}
        for materia in MATERIAS:
            notas[materia] = st.number_input(
                materia,
                min_value=0.0,
                max_value=20.0,
                value=0.0,
                step=0.5,
                key=f"nota_{materia}"
            )

        # Vista previa del promedio en tiempo real
        prom_actual = promedio(notas)
        color_txt, color_bg = color_nota(prom_actual)
        estado = "✅ APROBADO" if prom_actual >= 11 else "❌ DESAPROBADO"
        st.markdown(f"""
        <div style="background:{color_bg};border:1px solid {color_txt};border-radius:12px;
                    padding:14px;text-align:center;margin-top:12px;">
            <div style="font-family:'Playfair Display',serif;font-size:2rem;
                        color:{color_txt};font-weight:900;">{prom_actual}</div>
            <div style="color:{color_txt};font-size:0.75rem;letter-spacing:2px;
                        text-transform:uppercase;opacity:0.8;">{estado}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 3])

    with col_btn1:
        if st.button("💾  Guardar Alumno", use_container_width=True):
            if not nombre.strip():
                st.warning("⚠️ Escribe el nombre del alumno")
            elif not codigo.strip():
                st.warning("⚠️ Escribe el código del alumno")
            else:
                nuevo = {
                    "nombre":      nombre.strip(),
                    "codigo":      codigo.strip(),
                    "ciclo":       ciclo,
                    "seccion":     seccion,
                    "notas":       notas.copy(),
                    "habilidades": habilidades_sel,
                    "observacion": observacion.strip(),
                    "promedio":    prom_actual,
                }
                st.session_state.alumnos.append(nuevo)
                st.success(f"✅ ¡{nombre} registrado correctamente! Promedio: {prom_actual}")
                st.balloons()

    with col_btn2:
        if st.button("🗑️  Limpiar", use_container_width=True):
            st.rerun()

# ══════════════════════════════════════════════════════════════
# TAB 2 — LISTA DE ALUMNOS
# ══════════════════════════════════════════════════════════════
with tab2:
    st.markdown('<div class="seccion-header">Lista de Alumnos Registrados</div>', unsafe_allow_html=True)

    if not st.session_state.alumnos:
        st.markdown("""
        <div style="text-align:center;padding:60px 20px;color:rgba(232,224,208,0.3);">
            <div style="font-size:3rem;">🎓</div>
            <div style="font-family:'Playfair Display',serif;font-size:1.2rem;margin-top:12px;">
                Sin alumnos registrados
            </div>
            <div style="font-size:0.85rem;margin-top:6px;">
                Ve a la pestaña "Registrar Alumno" para comenzar
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Filtros
        col_f1, col_f2, col_f3 = st.columns([2, 1, 1])
        with col_f1:
            buscar = st.text_input("🔍 Buscar por nombre o código", placeholder="Escribe para buscar...")
        with col_f2:
            filtro_ciclo = st.selectbox("Filtrar por ciclo", ["Todos"] + ["I","II","III","IV","V","VI","VII","VIII","IX","X"])
        with col_f3:
            filtro_estado = st.selectbox("Estado", ["Todos", "Aprobados", "Desaprobados"])

        # Aplicar filtros
        lista = st.session_state.alumnos.copy()
        if buscar:
            lista = [a for a in lista if buscar.lower() in a["nombre"].lower() or buscar.lower() in a["codigo"].lower()]
        if filtro_ciclo != "Todos":
            lista = [a for a in lista if a["ciclo"] == filtro_ciclo]
        if filtro_estado == "Aprobados":
            lista = [a for a in lista if a["promedio"] >= 11]
        elif filtro_estado == "Desaprobados":
            lista = [a for a in lista if a["promedio"] < 11]

        st.markdown(f"<p style='color:rgba(232,224,208,0.4);font-size:0.82rem;'>{len(lista)} alumno(s) encontrado(s)</p>", unsafe_allow_html=True)

        for i, a in enumerate(lista):
            col_txt, color_bg = color_nota(a["promedio"])
            estado = "✅ Aprobado" if a["promedio"] >= 11 else "❌ Desaprobado"

            # Notas en badges
            notas_html = ""
            for mat, nota in a["notas"].items():
                c, bg = color_nota(nota)
                notas_html += f'<span class="nota-badge" style="background:{bg};color:{c};border:1px solid {c};">{mat[:8]}: {nota}</span>'

            # Habilidades
            hab_html = "".join([f'<span class="habilidad-badge">{h}</span>' for h in a.get("habilidades", [])])
            if not hab_html:
                hab_html = '<span style="color:rgba(232,224,208,0.3);font-size:0.78rem;">Sin habilidades registradas</span>'

            st.markdown(f"""
            <div class="alumno-card">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                    <div>
                        <div class="alumno-nombre">{a['nombre']}</div>
                        <div class="alumno-info">📋 {a['codigo']}  ·  Ciclo {a['ciclo']}  ·  Sección {a['seccion']}</div>
                    </div>
                    <div style="text-align:right;">
                        <div style="font-family:'Playfair Display',serif;font-size:1.8rem;
                                    color:{col_txt};font-weight:900;line-height:1;">{a['promedio']}</div>
                        <div style="color:{col_txt};font-size:0.72rem;opacity:0.8;">{estado}</div>
                    </div>
                </div>
                <div style="margin-top:10px;">{notas_html}</div>
                <div style="margin-top:8px;">{hab_html}</div>
                {'<div style="color:rgba(232,224,208,0.45);font-size:0.8rem;margin-top:6px;font-style:italic;">💬 ' + a["observacion"] + '</div>' if a.get("observacion") else ''}
            </div>
            """, unsafe_allow_html=True)

        # Botón eliminar último
        if st.button("🗑️  Eliminar último alumno"):
            if st.session_state.alumnos:
                eliminado = st.session_state.alumnos.pop()
                st.success(f"Se eliminó a {eliminado['nombre']}")
                st.rerun()

# ══════════════════════════════════════════════════════════════
# TAB 3 — GRÁFICOS
# ══════════════════════════════════════════════════════════════
with tab3:
    st.markdown('<div class="seccion-header">Gráficos y Estadísticas</div>', unsafe_allow_html=True)

    if not st.session_state.alumnos:
        st.info("📊 Registra alumnos para ver los gráficos")
    else:
        col_g1, col_g2 = st.columns(2)

        # ── Gráfico 1: Promedios por alumno ──────
        with col_g1:
            nombres = [a["nombre"].split()[0] for a in st.session_state.alumnos]
            promedios_list = [a["promedio"] for a in st.session_state.alumnos]
            colores = [color_nota(p)[0] for p in promedios_list]

            fig1 = go.Figure(go.Bar(
                x=nombres,
                y=promedios_list,
                marker_color=colores,
                marker_line_color="rgba(212,175,55,0.3)",
                marker_line_width=1,
                text=promedios_list,
                textposition="outside",
                textfont=dict(color="#D4AF37", size=12),
            ))
            fig1.add_hline(y=11, line_dash="dash", line_color="rgba(212,175,55,0.5)",
                           annotation_text="Mínimo aprobatorio (11)",
                           annotation_font_color="#D4AF37")
            fig1.update_layout(
                title=dict(text="Promedio por Alumno", font=dict(color="#D4AF37", size=16, family="Playfair Display")),
                paper_bgcolor="#0A0F0D",
                plot_bgcolor="#0D1A14",
                font=dict(color="#E8E0D0"),
                xaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
                yaxis=dict(gridcolor="rgba(255,255,255,0.05)", range=[0, 22]),
                margin=dict(t=50, b=30, l=10, r=10),
                height=350,
            )
            st.plotly_chart(fig1, use_container_width=True)

        # ── Gráfico 2: Promedio por materia ──────
        with col_g2:
            prom_materias = {}
            for mat in MATERIAS:
                vals = [a["notas"].get(mat, 0) for a in st.session_state.alumnos if a["notas"].get(mat, 0) > 0]
                prom_materias[mat] = round(sum(vals)/len(vals), 1) if vals else 0

            fig2 = go.Figure(go.Bar(
                x=list(prom_materias.values()),
                y=[m[:20] for m in prom_materias.keys()],
                orientation='h',
                marker_color=["#D4AF37" if v >= 11 else "#F87171" for v in prom_materias.values()],
                text=list(prom_materias.values()),
                textposition="outside",
                textfont=dict(color="#E8E0D0", size=11),
            ))
            fig2.update_layout(
                title=dict(text="Promedio por Materia", font=dict(color="#D4AF37", size=16, family="Playfair Display")),
                paper_bgcolor="#0A0F0D",
                plot_bgcolor="#0D1A14",
                font=dict(color="#E8E0D0"),
                xaxis=dict(gridcolor="rgba(255,255,255,0.05)", range=[0, 22]),
                yaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
                margin=dict(t=50, b=30, l=10, r=10),
                height=350,
            )
            st.plotly_chart(fig2, use_container_width=True)

        # ── Gráfico 3: Radar por alumno ───────────
        if len(st.session_state.alumnos) > 0:
            st.markdown('<div class="seccion-header" style="margin-top:20px;">Perfil de Notas — Gráfico Radar</div>', unsafe_allow_html=True)
            alumno_sel = st.selectbox(
                "Selecciona un alumno",
                [a["nombre"] for a in st.session_state.alumnos]
            )
            alumno_data = next(a for a in st.session_state.alumnos if a["nombre"] == alumno_sel)

            cats = [m[:15] for m in MATERIAS]
            vals = [alumno_data["notas"].get(m, 0) for m in MATERIAS]
            vals_closed = vals + [vals[0]]
            cats_closed = cats + [cats[0]]

            fig3 = go.Figure(go.Scatterpolar(
                r=vals_closed,
                theta=cats_closed,
                fill='toself',
                fillcolor='rgba(212,175,55,0.15)',
                line=dict(color='#D4AF37', width=2),
                marker=dict(color='#D4AF37', size=7),
            ))
            fig3.update_layout(
                polar=dict(
                    bgcolor="#0D1A14",
                    radialaxis=dict(visible=True, range=[0, 20], gridcolor="rgba(255,255,255,0.1)",
                                    tickfont=dict(color="rgba(232,224,208,0.5)", size=9)),
                    angularaxis=dict(gridcolor="rgba(255,255,255,0.08)",
                                     tickfont=dict(color="#E8E0D0", size=10)),
                ),
                paper_bgcolor="#0A0F0D",
                font=dict(color="#E8E0D0"),
                title=dict(text=f"Perfil de {alumno_sel.split()[0]}",
                           font=dict(color="#D4AF37", size=16, family="Playfair Display")),
                height=420,
                margin=dict(t=60, b=20),
            )
            st.plotly_chart(fig3, use_container_width=True)

        # ── Gráfico 4: Habilidades ─────────────
        st.markdown('<div class="seccion-header" style="margin-top:10px;">Distribución de Habilidades</div>', unsafe_allow_html=True)
        conteo_h = {h: 0 for h in HABILIDADES}
        for a in st.session_state.alumnos:
            for h in a.get("habilidades", []):
                if h in conteo_h:
                    conteo_h[h] += 1

        fig4 = go.Figure(go.Pie(
            labels=list(conteo_h.keys()),
            values=list(conteo_h.values()),
            hole=0.5,
            marker=dict(colors=["#D4AF37","#34D399","#60A5FA","#F472B6"],
                        line=dict(color="#0A0F0D", width=2)),
            textfont=dict(color="#E8E0D0", size=12),
        ))
        fig4.update_layout(
            paper_bgcolor="#0A0F0D",
            font=dict(color="#E8E0D0"),
            legend=dict(font=dict(color="#E8E0D0")),
            height=320,
            margin=dict(t=20, b=20),
        )
        st.plotly_chart(fig4, use_container_width=True)

# ══════════════════════════════════════════════════════════════
# TAB 4 — REPORTES
# ══════════════════════════════════════════════════════════════
with tab4:
    st.markdown('<div class="seccion-header">Reporte General del Aula</div>', unsafe_allow_html=True)

    if not st.session_state.alumnos:
        st.info("📄 Registra alumnos para generar el reporte")
    else:
        # Tabla resumen
        datos_tabla = []
        for a in st.session_state.alumnos:
            fila = {
                "Nombre":   a["nombre"],
                "Código":   a["codigo"],
                "Ciclo":    a["ciclo"],
                "Sección":  a["seccion"],
            }
            for mat in MATERIAS:
                fila[mat[:12]] = a["notas"].get(mat, 0)
            fila["Promedio"] = a["promedio"]
            fila["Estado"]   = "Aprobado" if a["promedio"] >= 11 else "Desaprobado"
            fila["Habilidades"] = ", ".join(a.get("habilidades", []))
            datos_tabla.append(fila)

        df = pd.DataFrame(datos_tabla)

        # Resumen ejecutivo
        total_r    = len(df)
        aprobados  = len(df[df["Estado"] == "Aprobado"])
        desaprobad = total_r - aprobados
        prom_aula  = round(df["Promedio"].mean(), 2)
        mejor      = df.loc[df["Promedio"].idxmax(), "Nombre"]
        max_nota   = df["Promedio"].max()

        col_r1, col_r2, col_r3, col_r4 = st.columns(4)
        col_r1.metric("Total Alumnos",    total_r)
        col_r2.metric("Aprobados",        aprobados,   delta=f"{round(aprobados/total_r*100)}%")
        col_r3.metric("Desaprobados",     desaprobad,  delta=f"-{round(desaprobad/total_r*100)}%")
        col_r4.metric("Promedio del Aula",prom_aula)

        st.markdown(f"""
        <div style="background:linear-gradient(135deg,#0D1A14,#112018);
                    border:1px solid rgba(212,175,55,0.3);border-radius:14px;
                    padding:16px 22px;margin:16px 0;">
            <span style="color:rgba(232,224,208,0.5);font-size:0.8rem;">🏆 MEJOR RENDIMIENTO</span><br>
            <span style="font-family:'Playfair Display',serif;font-size:1.3rem;color:#D4AF37;">{mejor}</span>
            <span style="color:rgba(232,224,208,0.5);"> — Promedio: </span>
            <span style="color:#34D399;font-weight:700;">{max_nota}</span>
        </div>
        """, unsafe_allow_html=True)

        # Tabla completa
        st.markdown("**📋 Tabla Completa**")
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Promedio": st.column_config.NumberColumn(format="%.1f"),
                "Estado":   st.column_config.TextColumn(),
            }
        )

        # Descargar CSV
        csv = df.to_csv(index=False, encoding="utf-8-sig")
        st.download_button(
            label="⬇️  Descargar reporte CSV",
            data=csv,
            file_name="reporte_alumnos.csv",
            mime="text/csv",
        )
