# ═══════════════════════════════════════════════════════════
#  📌 Sistema de Asistencia
#  Escuela Profesional de Ingeniería Estadística
#  Streamlit — Diseño Pastel Profesional ✨
#  pip install streamlit pandas plotly openpyxl
#  streamlit run asistencia.py
# ═══════════════════════════════════════════════════════════

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import date
import io

st.set_page_config(
    page_title="Asistencia — Ing. Estadística",
    page_icon="📌",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@400;500;600;700;800&display=swap');

/* ── FONDO ── */
.stApp { background:#EDE8F8; font-family:'DM Sans',sans-serif; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#E4DDF5,#DAE8F5);
    border-right:2px solid rgba(120,80,180,0.2);
}
[data-testid="stSidebar"] * { color:#2E1A6E !important; }
[data-testid="stSidebar"] .stat-l { color:#4A3580 !important; }

/* ── HEADER ── */
.main-header {
    background:linear-gradient(135deg,#DCC8F5,#C8DCF5);
    border:2px solid rgba(140,80,200,0.35);
    border-radius:20px; padding:28px 34px;
    margin-bottom:20px; position:relative; overflow:hidden;
    box-shadow:0 4px 20px rgba(140,100,200,0.18);
}
.main-header::after {
    content:'📌'; position:absolute; right:28px; top:50%;
    transform:translateY(-50%); font-size:80px; opacity:0.1;
}
.main-title {
    font-family:'DM Serif Display',serif;
    font-size:2.8rem; font-weight:900;
    color:#2E1A6E; letter-spacing:1px;
    text-transform:uppercase; margin:0; line-height:1.1;
}
.main-title span { color:#8020C0; }
.main-sub {
    color:#4A2D90; font-size:1.05rem; font-weight:700;
    letter-spacing:1px; text-transform:uppercase; margin-top:8px;
}

/* ── STAT BOXES ── */
.stat-box {
    background:white; border-radius:16px; padding:18px 12px;
    text-align:center; border:2px solid rgba(140,80,200,0.2);
    box-shadow:0 2px 12px rgba(140,100,200,0.1); margin-bottom:10px;
}
.stat-n {
    font-family:'DM Serif Display',serif; font-size:2.2rem;
    display:block; line-height:1; font-weight:900;
}
.stat-l {
    font-size:0.85rem; letter-spacing:1px; text-transform:uppercase;
    color:#4A3580; display:block; margin-top:6px; font-weight:700;
}

/* ── SECCIÓN HEADER ── */
.sec-hdr {
    font-family:'DM Serif Display',serif; font-size:1.35rem;
    color:#4A2D90; font-weight:900;
    border-bottom:2px solid rgba(140,80,200,0.25);
    padding-bottom:8px; margin-bottom:18px; margin-top:8px;
}

/* ── GRUPO LABEL ── */
.grupo-lbl {
    font-size:0.85rem; font-weight:800; letter-spacing:2px;
    text-transform:uppercase; margin:14px 0 8px;
    display:flex; align-items:center; gap:8px;
}
.lbl-a { color:#6A2DAA; }
.lbl-b { color:#2D6AAA; }

/* ── TARJETA ALUMNO ── */
.alumno-card {
    background:#F3EDFF; border:1.5px solid rgba(140,80,200,0.2);
    border-radius:12px; padding:13px 16px; margin-bottom:8px;
    display:flex; align-items:center; justify-content:space-between;
}
.alumno-card-b {
    background:#EDF3FF; border:1.5px solid rgba(77,122,200,0.2);
    border-radius:12px; padding:13px 16px; margin-bottom:8px;
    display:flex; align-items:center; justify-content:space-between;
}
.av {
    width:38px; height:38px; border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    font-size:13px; font-weight:800; flex-shrink:0;
}
.av-a { background:linear-gradient(135deg,#D8B8F5,#C4A8E8); color:#4A1A90; }
.av-b { background:linear-gradient(135deg,#B8D8F5,#A8C4E8); color:#1A4A90; }

/* ── NOMBRES Y TEXTOS DE ALUMNOS ── */
.a-nombre {
    font-weight:700; font-size:1rem; color:#2E1A6E;
    letter-spacing:0.2px;
}
.a-sub {
    font-size:0.82rem; color:#5A4090; margin-top:2px; font-weight:500;
}

/* ── BADGES ESTADO ── */
.badge-p { background:#C8F0D8; color:#145A30; border:2px solid #6DC898; border-radius:8px; padding:4px 13px; font-size:0.82rem; font-weight:800; }
.badge-a { background:#F5C8C8; color:#7A1010; border:2px solid #E07070; border-radius:8px; padding:4px 13px; font-size:0.82rem; font-weight:800; }
.badge-t { background:#F5E8B0; color:#6A4800; border:2px solid #D4B040; border-radius:8px; padding:4px 13px; font-size:0.82rem; font-weight:800; }
.badge-j { background:#C8DCF5; color:#102060; border:2px solid #6090D8; border-radius:8px; padding:4px 13px; font-size:0.82rem; font-weight:800; }

/* ── FILA REGISTRO ── */
.reg-row {
    background:white; border:1.5px solid rgba(140,80,200,0.18);
    border-radius:12px; padding:13px 18px; margin-bottom:8px;
    display:flex; align-items:center; justify-content:space-between;
}

/* ── BOTONES ── */
.stButton>button {
    background:linear-gradient(135deg,#D0B8F0,#B8D0F0) !important;
    color:#2E1A6E !important;
    border:2px solid rgba(130,80,200,0.4) !important;
    border-radius:12px !important;
    font-family:'DM Sans',sans-serif !important;
    font-weight:800 !important; font-size:0.95rem !important;
    padding:10px 20px !important;
}
.stButton>button:hover { border-color:#8040C0 !important; }

/* ── INPUTS ── */
.stTextInput>div>div>input,
.stNumberInput>div>div>input {
    background:white !important;
    border:2px solid rgba(130,80,200,0.3) !important;
    color:#2E1A6E !important; border-radius:10px !important;
    font-size:0.95rem !important; font-weight:500 !important;
}
.stTextInput label, .stNumberInput label {
    color:#3A2070 !important; font-size:0.95rem !important; font-weight:700 !important;
}
.stSelectbox>div>div {
    background:white !important;
    border:2px solid rgba(130,80,200,0.3) !important;
    color:#2E1A6E !important; border-radius:10px !important;
    font-size:0.95rem !important; font-weight:600 !important;
}
.stSelectbox label {
    color:#3A2070 !important; font-size:0.95rem !important; font-weight:700 !important;
}
.stDateInput>div>div>input {
    background:white !important;
    border:2px solid rgba(130,80,200,0.3) !important;
    color:#2E1A6E !important; border-radius:10px !important;
    font-size:0.95rem !important;
}
.stDateInput label {
    color:#3A2070 !important; font-size:0.95rem !important; font-weight:700 !important;
}

/* ── RADIO BUTTONS ── */
.stRadio label {
    color:#2E1A6E !important; font-size:0.92rem !important; font-weight:600 !important;
}
.stRadio > div > label {
    color:#2E1A6E !important;
}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    background:white; border-radius:14px; padding:5px; gap:5px;
    border:2px solid rgba(140,80,200,0.2);
}
.stTabs [data-baseweb="tab"] {
    background:transparent !important;
    color:#5A3D90 !important;
    border-radius:10px !important;
    font-family:'DM Sans',sans-serif !important;
    font-weight:700 !important; font-size:0.9rem !important;
}
.stTabs [aria-selected="true"] {
    background:linear-gradient(135deg,#E0C8F8,#C8E0F8) !important;
    color:#3A1A90 !important;
    border:2px solid rgba(140,80,200,0.35) !important;
}

/* ── DATAFRAME ── */
[data-testid="stDataFrame"] * { color:#2E1A6E !important; font-size:0.9rem !important; }

#MainMenu,footer,header { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

# ── CONSTANTES ──────────────────────────────────────────────
ESTADOS  = {"✅ Presente":"P","❌ Ausente":"A","⏰ Tardanza":"T","📋 Justificado":"J"}
COLOR_E  = {"P":"#2D8A5A","A":"#B03030","T":"#8A6010","J":"#2050A0"}
LABEL_E  = {"P":"Presente","A":"Ausente","T":"Tardanza","J":"Justificado"}
BADGE_E  = {"P":"badge-p","A":"badge-a","T":"badge-t","J":"badge-j"}
MATERIAS = ["Muestreo","Cálculo Integral","Estructura de Datos",
            "Defensa y Seguridad Nacional","Inglés","Distribución de Probabilidades"]
GRUPOS   = ["Grupo A","Grupo B"]

# ── ALUMNOS PRECARGADOS ──────────────────────────────────────
ALUMNOS_INICIALES = [
    # Grupo A
    {"nombre":"Chambilla Poma Jhon Brayam",   "codigo":"257091","ciclo":"IV","grupo":"Grupo A"},
    {"nombre":"Coaquira Salluca Gilma",        "codigo":"257092","ciclo":"IV","grupo":"Grupo A"},
    {"nombre":"Delgado Quispe Dina Milagros",  "codigo":"257093","ciclo":"IV","grupo":"Grupo A"},
    {"nombre":"Toledo Ramos Elias",            "codigo":"257094","ciclo":"IV","grupo":"Grupo A"},
    {"nombre":"Quispe Nuñez Jose Luis",        "codigo":"257095","ciclo":"IV","grupo":"Grupo A"},
    # Grupo B
    {"nombre":"Flores Zapana Leonardo",        "codigo":"257096","ciclo":"IV","grupo":"Grupo B"},
    {"nombre":"Ramos Vargas Luz",              "codigo":"257097","ciclo":"IV","grupo":"Grupo B"},
    {"nombre":"Mamani Chura Rosario",          "codigo":"257098","ciclo":"IV","grupo":"Grupo B"},
    {"nombre":"Huanca Turpo Kevin",            "codigo":"257099","ciclo":"IV","grupo":"Grupo B"},
    {"nombre":"Condori Larico Fiorella",       "codigo":"257100","ciclo":"IV","grupo":"Grupo B"},
]

# ── SESSION STATE ───────────────────────────────────────────
if "alumnos" not in st.session_state:
    st.session_state.alumnos = ALUMNOS_INICIALES.copy()
if "asistencias" not in st.session_state:
    st.session_state.asistencias = []

# ── HELPERS ─────────────────────────────────────────────────
def pct(codigo, materia=None):
    regs = [r for r in st.session_state.asistencias if r["codigo"]==codigo]
    if materia: regs = [r for r in regs if r["materia"]==materia]
    if not regs: return 0.0
    return round(sum(1 for r in regs if r["estado"] in ("P","T"))/len(regs)*100,1)

def color_pct(p):
    return "#2D8A5A" if p>=75 else "#8A6010" if p>=50 else "#B03030"

def bg_pct(p):
    if p>=75: return "rgba(110,200,150,0.15)","rgba(110,200,150,0.35)"
    elif p>=50: return "rgba(240,190,80,0.15)","rgba(240,190,80,0.35)"
    else: return "rgba(230,100,100,0.15)","rgba(230,100,100,0.35)"

def ya_reg(codigo, fecha, materia):
    return any(r["codigo"]==codigo and r["fecha"]==str(fecha) and r["materia"]==materia
               for r in st.session_state.asistencias)

def iniciales(nombre):
    parts = nombre.strip().split()
    return (parts[0][0]+parts[1][0]).upper() if len(parts)>=2 else nombre[:2].upper()

# ── HEADER ──────────────────────────────────────────────────
col_h1, col_h2 = st.columns([3,1])
with col_h1:
    st.markdown("""
    <div class="main-header">
        <div class="main-title">SISTEMA DE <span>ASISTENCIA</span></div>
        <div class="main-sub">ESCUELA PROFESIONAL DE INGENIERÍA ESTADÍSTICA &nbsp;·&nbsp; CONTROL DE ASISTENCIA</div>
    </div>
    """, unsafe_allow_html=True)

# ── SIDEBAR ─────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div style="font-family:DM Serif Display,serif;font-size:1.3rem;font-weight:900;color:#2E1A6E;margin-bottom:4px;">Panel General</div>', unsafe_allow_html=True)
    st.markdown('<hr style="border-color:rgba(160,108,192,0.2);">', unsafe_allow_html=True)

    total_a = len(st.session_state.alumnos)
    total_r = len(st.session_state.asistencias)
    if total_a>0 and total_r>0:
        pcts_s    = [pct(a["codigo"]) for a in st.session_state.alumnos]
        pct_g     = round(sum(pcts_s)/len(pcts_s),1)
        en_riesgo = sum(1 for p in pcts_s if p<75)
    else:
        pct_g=0.0; en_riesgo=0

    ga = sum(1 for a in st.session_state.alumnos if a["grupo"]=="Grupo A")
    gb = sum(1 for a in st.session_state.alumnos if a["grupo"]=="Grupo B")
    reg_hoy = sum(1 for r in st.session_state.asistencias if r["fecha"]==str(date.today()))

    st.markdown(f"""
    <div class="stat-box"><span class="stat-n" style="color:#8A5DC8;">{total_a}</span><span class="stat-l">Total Alumnos</span></div>
    <div style="display:flex;gap:8px;margin-bottom:10px;">
        <div class="stat-box" style="flex:1;"><span class="stat-n" style="color:#7A4DAA;font-size:1.5rem;">{ga}</span><span class="stat-l">Grupo A</span></div>
        <div class="stat-box" style="flex:1;"><span class="stat-n" style="color:#4D7AAA;font-size:1.5rem;">{gb}</span><span class="stat-l">Grupo B</span></div>
    </div>
    <div class="stat-box"><span class="stat-n" style="color:#2D8A5A;">{pct_g}%</span><span class="stat-l">Asistencia general</span></div>
    <div class="stat-box"><span class="stat-n" style="color:#B03030;">{en_riesgo}</span><span class="stat-l">En riesgo (&lt;75%)</span></div>
    """, unsafe_allow_html=True)

    st.markdown('<hr style="border-color:rgba(160,108,192,0.2);">', unsafe_allow_html=True)
    st.markdown(f'<p style="font-family:DM Serif Display,serif;color:#3A1A8E;font-size:1.15rem;font-weight:800;">{date.today().strftime("%d / %m / %Y")}</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#4A3090;font-size:0.88rem;font-weight:600;">{reg_hoy} registros hoy · {total_r} total</p>', unsafe_allow_html=True)

# ── TABS ────────────────────────────────────────────────────
tab1,tab2,tab3,tab4,tab5 = st.tabs([
    "👤 Alumnos","📌 Tomar Asistencia",
    "📋 Ver Registros","📈 Estadísticas","📥 Exportar"
])

# ════════════════════════════════════════
# TAB 1 — ALUMNOS
# ════════════════════════════════════════
with tab1:
    cf, cl = st.columns([1,1.6], gap="large")

    with cf:
        st.markdown('<div class="sec-hdr">Registrar Alumno</div>', unsafe_allow_html=True)
        nombre  = st.text_input("Nombre completo", placeholder="Ej: Mamani Quispe Juan")
        codigo  = st.text_input("Código", placeholder="Ej: 257101")
        ca,cb   = st.columns(2)
        ciclo   = ca.selectbox("Ciclo",["I","II","III","IV","V","VI","VII","VIII","IX","X"])
        grupo   = cb.selectbox("Grupo", GRUPOS)
        if st.button("➕  Agregar Alumno", use_container_width=True):
            if not nombre.strip():
                st.warning("⚠️ Escribe el nombre")
            elif not codigo.strip():
                st.warning("⚠️ Escribe el código")
            elif any(a["codigo"]==codigo.strip() for a in st.session_state.alumnos):
                st.warning("⚠️ Ese código ya existe")
            else:
                st.session_state.alumnos.append({"nombre":nombre.strip(),"codigo":codigo.strip(),"ciclo":ciclo,"grupo":grupo})
                st.success(f"✅ {nombre} agregado"); st.rerun()

    with cl:
        st.markdown('<div class="sec-hdr">Lista de Alumnos</div>', unsafe_allow_html=True)
        for grupo_nombre, av_class, lbl_class in [("Grupo A","av-a","lbl-a"),("Grupo B","av-b","lbl-b")]:
            miembros = [a for a in st.session_state.alumnos if a["grupo"]==grupo_nombre]
            if miembros:
                color_lbl = "#7A4DAA" if grupo_nombre=="Grupo A" else "#4D7AAA"
                st.markdown(f'<div class="grupo-lbl {lbl_class}">{grupo_nombre} <div style="flex:1;height:1px;background:rgba(160,108,192,0.15);"></div></div>', unsafe_allow_html=True)
                for a in miembros:
                    p  = pct(a["codigo"])
                    c  = color_pct(p)
                    bg,br = bg_pct(p)
                    ini = iniciales(a["nombre"])
                    card_cls = "alumno-card" if grupo_nombre=="Grupo A" else "alumno-card-b"
                    st.markdown(f"""
                    <div class="{card_cls}">
                        <div class="av {av_class}">{ini}</div>
                        <div style="flex:1;margin:0 12px;">
                            <div class="a-nombre">{a['nombre']}</div>
                            <div class="a-sub">📋 {a["codigo"]} · Ciclo {a["ciclo"]}</div>
                        </div>
                        <span style="background:{bg};color:{c};border:1px solid {br};border-radius:20px;padding:3px 11px;font-size:0.75rem;font-weight:700;">{p}%</span>
                    </div>
                    """, unsafe_allow_html=True)

        if st.button("🗑️  Eliminar último alumno"):
            if st.session_state.alumnos:
                e=st.session_state.alumnos.pop()
                st.success(f"Eliminado: {e['nombre']}"); st.rerun()

# ════════════════════════════════════════
# TAB 2 — TOMAR ASISTENCIA
# ════════════════════════════════════════
with tab2:
    st.markdown('<div class="sec-hdr">Tomar Asistencia del Día</div>', unsafe_allow_html=True)
    if not st.session_state.alumnos:
        st.info("👤 Primero hay alumnos registrados — ve a la pestaña Alumnos")
    else:
        c1,c2,c3 = st.columns(3)
        materia_sel = c1.selectbox("📚 Materia", MATERIAS)
        grupo_sel   = c2.selectbox("👥 Grupo",   GRUPOS)
        fecha_sel   = c3.date_input("📅 Fecha", value=date.today())

        st.markdown("---")
        miembros_sel = [a for a in st.session_state.alumnos if a["grupo"]==grupo_sel]

        if not miembros_sel:
            st.info(f"Sin alumnos en {grupo_sel} aún")
        else:
            color_g = "#7A4DAA" if grupo_sel=="Grupo A" else "#4D7AAA"
            st.markdown(f'<p style="color:{color_g};font-weight:700;font-size:0.85rem;margin-bottom:12px;">👥 {grupo_sel} — {materia_sel} — {fecha_sel.strftime("%d/%m/%Y")}</p>', unsafe_allow_html=True)

            estados_form = {}
            for a in miembros_sel:
                ya = ya_reg(a["codigo"], fecha_sel, materia_sel)
                cn,cr = st.columns([2,3])
                cn.markdown(f"""
                <div style="padding:8px 0;">
                    <div style="font-weight:700;color:#2E1A6E;font-size:1rem;">{a["nombre"]}</div>
                    <div style="color:#4A3090;font-size:0.88rem;font-weight:600;">📋 {a["codigo"]}</div>
                    {"<span style='color:#8A6010;font-size:0.72rem;'>⚠️ Ya registrado hoy</span>" if ya else ""}
                </div>""", unsafe_allow_html=True)
                estados_form[a["codigo"]] = cr.radio("", list(ESTADOS.keys()), horizontal=True,
                    key=f"e_{a['codigo']}_{fecha_sel}_{materia_sel}", label_visibility="collapsed")
                st.markdown('<hr style="border-color:rgba(160,108,192,0.1);margin:3px 0;">', unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            if st.button(f"💾  Guardar Asistencia — {grupo_sel}"):
                nuevos=0
                for a in miembros_sel:
                    if not ya_reg(a["codigo"], fecha_sel, materia_sel):
                        st.session_state.asistencias.append({
                            "nombre":  a["nombre"], "codigo": a["codigo"],
                            "grupo":   a["grupo"],  "fecha":  str(fecha_sel),
                            "materia": materia_sel, "estado": ESTADOS[estados_form[a["codigo"]]],
                        })
                        nuevos+=1
                if nuevos>0: st.success(f"✅ Guardado para {nuevos} alumno(s)"); st.balloons()
                else: st.warning("⚠️ Ya estaban todos registrados para ese día y materia")

# ════════════════════════════════════════
# TAB 3 — VER REGISTROS
# ════════════════════════════════════════
with tab3:
    st.markdown('<div class="sec-hdr">Historial de Asistencias</div>', unsafe_allow_html=True)
    if not st.session_state.asistencias:
        st.info("📌 Aún no hay asistencias registradas")
    else:
        f1,f2,f3,f4 = st.columns(4)
        fa = f1.selectbox("Alumno", ["Todos"]+[a["nombre"] for a in st.session_state.alumnos])
        fg = f2.selectbox("Grupo",  ["Todos"]+GRUPOS)
        fm = f3.selectbox("Materia",["Todas"]+MATERIAS)
        fe = f4.selectbox("Estado", ["Todos"]+list(ESTADOS.keys()))

        lista = st.session_state.asistencias.copy()
        if fa!="Todos":  lista=[r for r in lista if r["nombre"]==fa]
        if fg!="Todos":  lista=[r for r in lista if r["grupo"]==fg]
        if fm!="Todas":  lista=[r for r in lista if r["materia"]==fm]
        if fe!="Todos":  lista=[r for r in lista if r["estado"]==ESTADOS[fe]]
        lista=sorted(lista,key=lambda x:x["fecha"],reverse=True)

        st.markdown(f'<p style="color:#3A2070;font-size:0.9rem;font-weight:700;margin-bottom:10px;">{len(lista)} registro(s) encontrado(s)</p>', unsafe_allow_html=True)
        for r in lista:
            e=r["estado"]; bc=BADGE_E[e]; lb=LABEL_E[e]
            color_g = "#7A4DAA" if r.get("grupo","")=="Grupo A" else "#4D7AAA"
            st.markdown(f"""
            <div class="reg-row">
                <div>
                    <span style="font-weight:700;color:#2E1A6E;font-size:1rem;">{r["nombre"]}</span>
                    <span style="color:#4A3090;font-size:0.88rem;font-weight:600;margin-left:8px;">📋 {r["codigo"]}</span><br>
                    <span style="color:#4A3090;font-size:0.88rem;font-weight:600;">📚 {r['materia']} · 📅 {r['fecha']}</span>
                    <span style="color:{color_g};font-size:0.72rem;font-weight:600;margin-left:8px;">{r.get('grupo','')}</span>
                </div>
                <span class="{bc}">{lb}</span>
            </div>""", unsafe_allow_html=True)

# ════════════════════════════════════════
# TAB 4 — ESTADÍSTICAS
# ════════════════════════════════════════
with tab4:
    st.markdown('<div class="sec-hdr">Estadísticas de Asistencia</div>', unsafe_allow_html=True)
    if not st.session_state.asistencias:
        st.info("📈 Registra asistencias para ver estadísticas")
    else:
        g1,g2 = st.columns(2)
        with g1:
            noms  = [a["nombre"].split()[0]+" "+a["nombre"].split()[-1] for a in st.session_state.alumnos]
            pcts_g= [pct(a["codigo"]) for a in st.session_state.alumnos]
            cols_g= ["rgba(160,108,192,0.7)" if a["grupo"]=="Grupo A" else "rgba(77,122,170,0.7)" for a in st.session_state.alumnos]
            fig1=go.Figure(go.Bar(x=noms,y=pcts_g,marker_color=cols_g,
                text=[f"{p}%" for p in pcts_g],textposition="outside",
                textfont=dict(color="#4A3580",size=10)))
            fig1.add_hline(y=75,line_dash="dash",line_color="rgba(160,108,192,0.6)",
                annotation_text="Mínimo 75%",annotation_font_color="#7A4DAA")
            fig1.update_layout(
                title=dict(text="% Asistencia por Alumno",font=dict(color="#6A3DAA",size=13,family="DM Serif Display")),
                paper_bgcolor="#F0EDF8",plot_bgcolor="white",font=dict(color="#4A3580"),
                yaxis=dict(range=[0,115],gridcolor="rgba(160,108,192,0.1)"),
                xaxis=dict(gridcolor="rgba(160,108,192,0.1)",tickangle=-30),
                margin=dict(t=50,b=60,l=10,r=10),height=340)
            st.plotly_chart(fig1,use_container_width=True)

        with g2:
            cnt={"P":0,"A":0,"T":0,"J":0}
            for r in st.session_state.asistencias: cnt[r["estado"]]+=1
            fig2=go.Figure(go.Pie(
                labels=[LABEL_E[k] for k in cnt],values=list(cnt.values()),hole=0.55,
                marker=dict(colors=["#A8D8B0","#F0A8A8","#F5D898","#A8C4F0"],
                            line=dict(color="white",width=2)),
                textfont=dict(color="#3D2870",size=11)))
            fig2.update_layout(
                title=dict(text="Distribución de Estados",font=dict(color="#6A3DAA",size=13,family="DM Serif Display")),
                paper_bgcolor="#F0EDF8",font=dict(color="#4A3580"),
                legend=dict(font=dict(color="#4A3580")),height=340,margin=dict(t=50,b=20))
            st.plotly_chart(fig2,use_container_width=True)

        # Por grupo
        st.markdown('<div class="sec-hdr" style="margin-top:8px;">Comparativa por Grupo</div>', unsafe_allow_html=True)
        g3,g4 = st.columns(2)
        for col, grupo_n, color in [(g3,"Grupo A","rgba(160,108,192,0.6)"),(g4,"Grupo B","rgba(77,122,170,0.6)")]:
            with col:
                pm={}
                for mat in MATERIAS:
                    regs=[r for r in st.session_state.asistencias if r["materia"]==mat and r.get("grupo")==grupo_n]
                    pm[mat]=round(sum(1 for r in regs if r["estado"] in ("P","T"))/len(regs)*100,1) if regs else 0
                fig=go.Figure(go.Bar(y=[m[:18] for m in pm],x=list(pm.values()),orientation='h',
                    marker_color=color,text=[f"{v}%" for v in pm.values()],textposition="outside",
                    textfont=dict(color="#4A3580",size=10)))
                fig.add_vline(x=75,line_dash="dash",line_color="rgba(160,108,192,0.5)")
                fig.update_layout(
                    title=dict(text=grupo_n,font=dict(color="#6A3DAA",size=13,family="DM Serif Display")),
                    paper_bgcolor="#F0EDF8",plot_bgcolor="white",font=dict(color="#4A3580"),
                    xaxis=dict(range=[0,115],gridcolor="rgba(160,108,192,0.1)"),
                    yaxis=dict(gridcolor="rgba(160,108,192,0.1)"),
                    margin=dict(t=40,b=20,l=10,r=10),height=300)
                st.plotly_chart(fig,use_container_width=True)

        # Tabla resumen
        st.markdown('<div class="sec-hdr" style="margin-top:8px;">Resumen por Alumno</div>', unsafe_allow_html=True)
        res=[]
        for a in st.session_state.alumnos:
            ra=[r for r in st.session_state.asistencias if r["codigo"]==a["codigo"]]
            pp=pct(a["codigo"])
            res.append({"Nombre":a["nombre"],"Código":a["codigo"],"Grupo":a["grupo"],
                "Total":len(ra),
                "Presentes":sum(1 for r in ra if r["estado"]=="P"),
                "Ausentes": sum(1 for r in ra if r["estado"]=="A"),
                "Tardanzas":sum(1 for r in ra if r["estado"]=="T"),
                "Justif.":  sum(1 for r in ra if r["estado"]=="J"),
                "% Asist.": pp,
                "Estado":   "✅ Regular" if pp>=75 else "⚠️ En riesgo"})
        st.dataframe(pd.DataFrame(res),use_container_width=True,hide_index=True)

# ════════════════════════════════════════
# TAB 5 — EXPORTAR
# ════════════════════════════════════════
with tab5:
    st.markdown('<div class="sec-hdr">Exportar Reportes</div>', unsafe_allow_html=True)
    if not st.session_state.asistencias:
        st.info("📥 Sin datos para exportar aún")
    else:
        rows=[]
        for a in st.session_state.alumnos:
            ra=[r for r in st.session_state.asistencias if r["codigo"]==a["codigo"]]
            for mat in MATERIAS:
                rm=[r for r in ra if r["materia"]==mat]
                pre=sum(1 for r in rm if r["estado"]=="P")
                aus=sum(1 for r in rm if r["estado"]=="A")
                tar=sum(1 for r in rm if r["estado"]=="T")
                jus=sum(1 for r in rm if r["estado"]=="J")
                tot=len(rm)
                pp=round(((pre+tar)/tot)*100,1) if tot>0 else 0
                rows.append({"Nombre":a["nombre"],"Código":a["codigo"],"Grupo":a["grupo"],
                    "Ciclo":a["ciclo"],"Materia":mat,"Presentes":pre,"Ausentes":aus,
                    "Tardanzas":tar,"Justif.":jus,"Total":tot,"% Asist.":pp,
                    "Estado":"Regular" if pp>=75 else "En riesgo"})
        df_exp=pd.DataFrame(rows)
        st.dataframe(df_exp,use_container_width=True,hide_index=True)

        d1,d2=st.columns(2)
        with d1:
            csv=df_exp.to_csv(index=False,encoding="utf-8-sig")
            st.download_button("⬇️  Descargar CSV",data=csv,
                file_name=f"asistencia_{date.today()}.csv",
                mime="text/csv",use_container_width=True)
        with d2:
            buf=io.BytesIO()
            with pd.ExcelWriter(buf,engine="openpyxl") as w:
                df_exp.to_excel(w,index=False,sheet_name="Detalle")
                res2=[]
                for a in st.session_state.alumnos:
                    ra=[r for r in st.session_state.asistencias if r["codigo"]==a["codigo"]]
                    pp=pct(a["codigo"])
                    res2.append({"Nombre":a["nombre"],"Código":a["codigo"],"Grupo":a["grupo"],
                        "Total":len(ra),"Presentes":sum(1 for r in ra if r["estado"]=="P"),
                        "Ausentes":sum(1 for r in ra if r["estado"]=="A"),
                        "Tardanzas":sum(1 for r in ra if r["estado"]=="T"),
                        "Justificados":sum(1 for r in ra if r["estado"]=="J"),
                        "% Asistencia":pp,"Estado":"Regular" if pp>=75 else "En riesgo"})
                pd.DataFrame(res2).to_excel(w,index=False,sheet_name="Resumen")
            buf.seek(0)
            st.download_button("⬇️  Descargar Excel (.xlsx)",data=buf,
                file_name=f"asistencia_{date.today()}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True)

        st.markdown("""
        <div style="background:white;border:1.5px solid rgba(160,108,192,0.2);border-radius:13px;padding:14px 18px;margin-top:14px;">
            <p style="color:#3A2070;font-size:0.9rem;font-weight:600;margin:0;">
            📊 El Excel incluye <strong style="color:#7A4DAA;">2 hojas</strong>:
            <em>Detalle</em> con el desglose por materia y <em>Resumen</em> con el total por alumno.
            </p>
        </div>""", unsafe_allow_html=True)
