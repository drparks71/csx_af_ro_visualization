import streamlit as st

from src.rail_network_simulator.network_definitions import TRV
from src.rail_network_simulator.phasing import existing_conditions, phase_1_stage_1a, phase_1_stage_1b, phase_1_stage_1c
from src.rail_network_simulator.phasing import phase_1_stage_2a, phase_1_stage_2b, phase_1_stage_3

import matplotlib.pyplot as plt
plt.ioff()

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: teal;'>AF-RO Outage Visualizer</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: green;'>Construction Phases</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>(Only select 1 box at a time)</p>", unsafe_allow_html=True)

phase0, phase1, phase2, phase3 = st.columns(4)

with phase1:
    phase1.header('Phase 1')
    phase_1_stage_1A_status = st.checkbox("Stage 1A", key='const_phase_1_stage_1A')
    phase_1_stage_1B_status = st.checkbox("Stage 1B", key='const_phase_1_stage_1B')
    phase_1_stage_1C_status = st.checkbox("Stage 1C", key='const_phase_1_stage_1C')
    phase_1_stage_2A_status = st.checkbox("Stage 2A", key='const_phase_1_stage_2A')
    phase_1_stage_2B_status = st.checkbox("Stage 2B", key='const_phase_1_stage_2B')
    phase_1_stage_3_status = st.checkbox("Stage 3", key='const_phase_1_stage_3')

with phase2:
    phase2.header('Phase 2')
    phase_2_stage_1_status = st.checkbox("Stage 1", key='const_phase_2_stage_1')
    phase_2_stage_2_status = st.checkbox("Stage 2", key='const_phase_2_stage_2')

# ================================================= Staging Views =====================================================

if not any([phase_1_stage_1A_status, phase_1_stage_1B_status, phase_1_stage_1C_status, phase_1_stage_2A_status,
            phase_1_stage_2B_status, phase_1_stage_3_status]):
    existing_conditions()

if phase_1_stage_1A_status:
    phase_1_stage_1a()

if phase_1_stage_1B_status:
    phase_1_stage_1b()

if phase_1_stage_1C_status:
    phase_1_stage_1c()

if phase_1_stage_2A_status:
    phase_1_stage_2a()

if phase_1_stage_2B_status:
    phase_1_stage_2b()

if phase_1_stage_3_status:
    phase_1_stage_3()


st.pyplot(TRV.show_network(figsize=(60, 30)))

# # (For Debugging)
# fig = TRV.show_network(figsize=(120, 30), show_links=True, show_switches=True)
# fig.show()
