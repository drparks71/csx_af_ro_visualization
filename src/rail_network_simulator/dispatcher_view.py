import streamlit as st
import matplotlib.pyplot as plt
from network_definitions import TRV
from phasing import existing_conditions, phase_1_stage_1a, phase_1_stage_1b, phase_1_stage_1c
from phasing import phase_1_stage_2a, phase_1_stage_2b, phase_1_stage_3

plt.ioff()

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: teal;'>AF-RO Outage Visualizer</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: green;'>Construction Phases</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: red;'>(Only select 1 option at a time)<br>let the diagram load before selecting another option</p>",
    unsafe_allow_html=True)

# Define Phase options
phase_1_options = ["None", "Stage 1A", "Stage 1B", "Stage 1C - Temporary Outages As-needed",
                   "Stage 2A - Temporary Outages As-needed", "Stage 2B", "Stage 3"]
phase_2_options = ["None", "Stage 1", "Stage 2"]

# Layout the phases in columns
phase0, phase1, phase2, phase3 = st.columns(4)

with phase1:
    phase1.header('Phase 1')
    phase_1_selection = st.radio("Select Phase 1 Stage", phase_1_options, key='const_phase_1')

with phase2:
    phase2.header('Phase 2')
    phase_2_selection = st.radio("Select Phase 2 Stage", phase_2_options, key='const_phase_2')

# Valid Phase 1 Stages and their corresponding functions
phase_1_stages = {
    "Stage 1A": phase_1_stage_1a,
    "Stage 1B": phase_1_stage_1b,
    "Stage 1C - Temporary Outages As-needed": phase_1_stage_1c,
    "Stage 2A - Temporary Outages As-needed": phase_1_stage_2a,
    "Stage 2B": phase_1_stage_2b,
    "Stage 3": phase_1_stage_3,
}

# ================================================= Staging Views =====================================================
if (phase_1_selection == "None") and (phase_2_selection == "None"):
    existing_conditions()

# Execute appropriate phase functions based on selection
if phase_1_selection in phase_1_stages:
    phase_1_stages[phase_1_selection]()

if phase_2_selection == "Stage 1":
    # Call phase 2 stage 1 function if it exists
    pass

if phase_2_selection == "Stage 2":
    # Call phase 2 stage 2 function if it exists
    pass

# Fetch and display network figure
fig, ax = TRV.show_network(figsize=(60, 30))
st.pyplot(fig=fig)

# # (For Debugging)
# fig = TRV.show_network(figsize=(120, 30), show_links=True, show_switches=True)
# fig.show()
