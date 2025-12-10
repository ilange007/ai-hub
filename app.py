import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import date, timedelta

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="MSI AI Transformation Hub", page_icon="🤖", layout="wide")

# --- CUSTOM CSS (Enterprise Tech Look) ---
st.markdown("""
    <style>
    .main {background-color: #0e1117;}
    h1, h2, h3 {color: #ffffff;}
    .stMetric {background-color: #262730; padding: 15px; border-radius: 8px; border: 1px solid #3b3d45;}
    div[data-testid="stMetricValue"] {font-size: 24px;}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: NAVIGATION ---
# Placeholder for Logo
st.sidebar.image("https://media.licdn.com/dms/image/v2/D4E0BAQGgD7oni35Nyw/company-logo_200_200/company-logo_200_200/0/1707945536452/msi_americas_logo?e=2147483647&v=beta&t=Q8N7elBitqKXV8YEbojVjV3MGv9wXA-yPg4JiDkE7rI", width='content') 

st.sidebar.title("Strategic Navigation")
page = st.sidebar.radio("Go to:", [
    "Roadmap & Status", 
    "Discovery Insights", 
    "Opportunity Matrix", 
    "Live Solutions"
])

st.sidebar.divider()
st.sidebar.info("📅 **Current Phase:** Workshop - Week 2\n\n🎯 **Goal:** Technical & Data Validation")
st.sidebar.caption("Client: MSI Internal Pilot")

# --- MOCK DATA (Based on your Excel Real Data) ---
data = {
    'Department': ['Finance', 'Operations', 'HR', 'Projects', 'Sales', 'NPO', 'H&S'],
    'Critical Process': ['UNBILLED Management', 'Timesheet Reconciliation', 'Contract Visa/Compliance', 'Financial Closing', 'Collections', 'Drive Test Logs', 'HSE Audits'],
    'Main Pain Point': ['Cash Flow Blockage', 'Slow Consultant Payments', 'Legal/Fine Risk', 'Manual Rework', 'Lack of Traceability', 'Outdated Equipment', 'Manual Reporting'],
    'Business Impact (1-5)': [5, 5, 5, 4, 5, 3, 4],
    'Data Viability (1-5)': [4, 3, 2, 4, 3, 5, 4], 
    'Pain Type': ['Financial Loss', 'Operational Efficiency', 'Risk & Compliance', 'Operational Efficiency', 'Financial Loss', 'Tech/Infrastructure', 'Risk & Compliance'],
    '% Manual Work': [80, 90, 100, 70, 60, 50, 80]
}
df = pd.DataFrame(data)

# --- PAGE 1: ROADMAP & STATUS ---
if page == "Roadmap & Status":
    st.title("Strategic AI Transformation Roadmap")
    st.markdown("Detailed execution plan: **Phase 1 (Discovery)** through **Phase 3 (Scale)**.")

    # Status Indicators (Aligned with PDF Weeks)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.success("✅ Week 1: Discovery")
        st.caption("Kick-off & Interviews")
    with col2:
        st.info("🔄 Week 2: Analysis (Current)")
        st.caption("Mapping & Prioritization")
    with col3:
        st.warning("⏳ Phase 2: PoC Build")
        st.caption("Implementation")
    with col4:
        st.error("🔒 Phase 3: Scale")
        st.caption("Managed Service")

    st.markdown("### Execution Timeline")
    
    # 1. Create Dataframe with Specific Steps from the PDF
    df_gantt = pd.DataFrame([
        # --- PHASE 1: WEEK 1 (Discovery) ---
        dict(Task="1. Kick-off & Stakeholder Matrix", Start='2025-12-01', Finish='2025-12-02', Phase="Phase 1: Week 1 (Discovery)", Description="Scope Definition"),
        dict(Task="2. Strategic Interviews", Start='2025-12-02', Finish='2025-12-03', Phase="Phase 1: Week 1 (Discovery)", Description="Pain Point Identification"),
        dict(Task="3. Operational Deep Dive", Start='2025-12-03', Finish='2025-12-04', Phase="Phase 1: Week 1 (Discovery)", Description="Data Collection"),
        dict(Task="4. Findings Consolidation", Start='2025-12-04', Finish='2025-12-05', Phase="Phase 1: Week 1 (Discovery)", Description="Initial Analysis"),
        
        # --- PHASE 1: WEEK 2 (Analysis - Current) ---
        dict(Task="5. Minimum Evidence Collection", Start='2025-12-08', Finish='2025-12-09', Phase="Phase 1: Week 2 (Analysis)", Description="Logs & KPIs"),
        dict(Task="6. AI Opportunity Mapping", Start='2025-12-09', Finish='2025-12-11', Phase="Phase 1: Week 2 (Analysis)", Description="Feasibility vs Value"),
        dict(Task="7. Executive Presentation", Start='2025-12-11', Finish='2025-12-12', Phase="Phase 1: Week 2 (Analysis)", Description="Final Decision"),

        # --- PHASE 2 & 3 (Future) ---
        dict(Task="8. PoC Execution (FinOps Agent)", Start='2025-12-15', Finish='2026-01-30', Phase="Phase 2: Implementation", Description="Build & Validate"),
        dict(Task="9. Managed Service (Live)", Start='2026-02-01', Finish='2026-03-30', Phase="Phase 3: Recurring Scale", Description="Monitoring & Optimization")
    ])

    # 2. Configure the Chart to look like the PDF Timeline
    fig_gantt = px.timeline(
        df_gantt, 
        x_start="Start", 
        x_end="Finish", 
        y="Task", 
        color="Phase", 
        hover_data=["Description"],
        title="AI Discovery Workshop & Implementation Flow",
        template="plotly_dark",
        color_discrete_map={
            "Phase 1: Week 1 (Discovery)": "#00CC96", 
            "Phase 1: Week 2 (Analysis)": "#636EFA", 
            "Phase 2: Implementation": "#EF553B",     
            "Phase 3: Recurring Scale": "#AB63FA"     
        }
    )

    # Iterar sobre las trazas para ocultar todas las fases excepto la actual
    current_phase_label = "Phase 1: Week 2 (Analysis)"
    # Plotly crea una traza separada para cada valor único en la columna 'color'
    # (en este caso, la columna 'Phase').
    for trace in fig_gantt.data:
        if trace.name != current_phase_label:
            # Si la fase NO es la actual, la ocultamos al inicio.
            trace.visible = 'legendonly' # 'legendonly' oculta la traza del gráfico, pero la deja visible en la leyenda para que el usuario pueda hacer clic en ella y mostrarla.
        else:
            # Si la fase ES la actual, la mostramos.
            trace.visible = True

    # 3. Formatting to match the "Step-down" look
    fig_gantt.update_yaxes(autorange="reversed") 
    fig_gantt.update_layout(
        xaxis_title="Timeline",
        height=500,
        showlegend=True,
        legend=dict(orientation="h", y=1.1, x=0)
    )

    st.plotly_chart(fig_gantt, use_container_width=True)

    st.markdown("---")
    st.info("**Current Status:** We are currently in **Step 5 & 6** (Evidence Collection & Mapping), prioritizing the *FinOps Agent* based on data viability.")

# --- PAGE 2: DISCOVERY INSIGHTS ---
elif page == "Discovery Insights":
    st.title("Diagnostic Findings (Phase 1)")
    st.markdown("Analysis of pain points collected during stakeholder interviews.")

    # Top Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Analyzed Processes", len(df))
    c2.metric("Avg. Manual Work", f"{df['% Manual Work'].mean():.0f}%")
    c3.metric("Highest Impact Area", "Finance & Ops")

    # Interactive Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Where does it hurt the most?")
        fig_pie = px.pie(df, names='Pain Type', title='Distribution by Pain Type', hole=0.4, template="plotly_dark")
        st.plotly_chart(fig_pie, use_container_width=True)

    with col2:
        st.subheader("Manual Work vs. Business Impact")
        fig_bar = px.bar(df, x='Critical Process', y='% Manual Work', color='Business Impact (1-5)', 
                         title='Most Manual & Critical Processes', template="plotly_dark")
        st.plotly_chart(fig_bar, use_container_width=True)

    with st.expander("📂 View Raw Data (Transparency)"):
        st.dataframe(df)

# --- PAGE 3: OPPORTUNITY MATRIX ---
elif page == "Opportunity Matrix":
    st.title("Opportunity Selection Matrix")
    st.markdown("Prioritization based on **Business Impact (ROI)** vs. **Technical Feasibility (Data)**.")

    # Strategic Scatter Plot
    fig_matrix = px.scatter(df, x="Data Viability (1-5)", y="Business Impact (1-5)", 
                            color="Department", size="% Manual Work", hover_name="Critical Process",
                            text="Critical Process",
                            title="PoC Prioritization Matrix",
                            labels={"Data Viability (1-5)": "Technical Feasibility (Data Availability)", "Business Impact (1-5)": "Business Impact (ROI)"},
                            range_x=[0.5, 5.5], range_y=[0.5, 5.5],
                            template="plotly_dark")
    
    fig_matrix.update_traces(textposition='top center')
    
    # Adding Quadrant Lines
    fig_matrix.add_hline(y=3.5, line_dash="dot", annotation_text="High Impact Zone")
    fig_matrix.add_vline(x=3.5, line_dash="dot", annotation_text="High Viability Zone")
    
    st.plotly_chart(fig_matrix, use_container_width=True)

    # Recommendation Box
    st.success("""
    **🏆 Winning Opportunity: FinOps Agent (UNBILLED Management)**
    
    * **Rationale:** Located in the top-right quadrant (High Impact / High Viability).
    * **Next Step:** Technical Audit of Quickbooks/Excel data sources.
    """)

# --- PAGE 4: LIVE SOLUTIONS (UPSELL) ---
elif page == "Live Solutions":
    st.title("MSI Applied AI Monitor")
    st.markdown("Simulation of the Operations Dashboard included in the **Managed Service (Phase B)**.")
    
    st.info("ℹ️ **Demo Mode:** This module activates upon subscription to the Applied AI Solution.")

    st.subheader("🟢 FinOps Agent (Status: Active)")
    
    # Real-time ROI Metrics (The reason to pay monthly)
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Invoices Processed (Today)", "142", "+12%")
    kpi2.metric("Risk Alerts", "3", "-2")
    kpi3.metric("Time Saved (Month)", "120 hrs", "positive ROI")
    kpi4.metric("Model Accuracy", "98.5%", "Stable")

    # Predictive Chart
    st.subheader("📉 Projected Cash Flow Impact (DSO Reduction)")
    chart_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'DSO (Legacy Process)': [45, 44, 46, 45, 44, 45],
        'DSO (With MSI AI)': [45, 40, 35, 30, 28, 25]
    })
    
    fig_roi = px.line(chart_data, x='Month', y=['DSO (Legacy Process)', 'DSO (With MSI AI)'], 
                      title='Impact on Cash Flow Efficiency', markers=True, template="plotly_dark")
    st.plotly_chart(fig_roi, use_container_width=True)

    st.warning("⚠️ **Predictive Alert:** 2 contracts detected with expiration risk next week. The Agent has notified Finance.")