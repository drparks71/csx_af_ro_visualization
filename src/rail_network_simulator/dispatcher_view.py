import streamlit as st

from src.rail_network_simulator.network_definitions import TRV
from src.rail_network_simulator.phasing import existing_conditions, phase1A_staging

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: teal;'>AF-RO Outage Visualizer</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: green;'>Construction Phases</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>(Only select 1 box at a time)</p>", unsafe_allow_html=True)

phase0, phase1, phase2, phase3 = st.columns(4)

with phase1:
    phase1.header('Phase 1')
    phase_1_stage_1A = st.checkbox("Stage 1A", key='const_phase_1_stage_1A')
    phase_1_stage_1B = st.checkbox("Stage 1B", key='const_phase_1_stage_1B')
    phase_1_stage_1C = st.checkbox("Stage 1C", key='const_phase_1_stage_1C')
    phase_1_stage_2 = st.checkbox("Stage 2", key='const_phase_1_stage_2')
    phase_1_stage_3 = st.checkbox("Stage 3", key='const_phase_1_stage_3')

with phase2:
    phase2.header('Phase 2')
    phase_2_stage_1 = st.checkbox("Stage 1", key='const_phase_2_stage_1')
    phase_2_stage_2 = st.checkbox("Stage 2", key='const_phase_2_stage_2')

# ================================================= Staging Views =====================================================

if not any([phase_1_stage_1A, phase_1_stage_1B, phase_1_stage_1C, phase_1_stage_2, phase_1_stage_3]):
    existing_conditions()

if phase_1_stage_1A:
    phase1A_staging()

if phase_1_stage_1B:
    SlatersROMain3Closed = True
    SlatersROMain2Closed = True
    SlatersROMain0Closed = True

if phase_1_stage_1C:
    SlatersROMain1Closed = True
    SlatersROMain2Closed = True

if phase_1_stage_2:
    SlatersROMain0Closed = True
    SlatersROMain1Closed = True
    SlatersROMain2Closed = True

if phase_1_stage_3:
    SlatersROMain2Closed = True
    SlatersROMain3Closed = True

# (For Debugging)
f = TRV.show_network(figsize=(100, 20), show_links=True, show_switches=True)
f.show()

st.pyplot(TRV.show_network(figsize=(60, 30)))
