import streamlit as st

from src.rail_network_simulator.rail_simulator import *

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: teal;'>AF-RO Outage Visualizer</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: green;'>Construction Phases</h1>", unsafe_allow_html=True)

phase1, phase2, phase3, phase4 = st.columns(4)

with phase1:
    phase1.header('Phase 1')
    phase_1_opt_1 = st.checkbox("Option 1", key='const_phase_1_opt_1')

with phase2:
    phase2.header('Phase 2')
    phase_2_opt_1 = st.checkbox("Option 1", key='const_phase_2_opt_1')

with phase3:
    phase3.header('Phase 3')
    phase_3_opt_1 = st.checkbox("Option 1", key='const_phase_3_opt_1')

with phase4:
    phase4.header('Phase 4')
    phase_4_opt_1 = st.checkbox("Option 1", key='const_phase_4_opt_1')


# Outage Selection Overrides
st.markdown("<h1 style='text-align: center; color: green;'>Outage Selection Override</h1>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    col1.header('After RO')
    Main2AfterRO = st.checkbox("Main 2 Outage", key='After_RO_main2_disabled')
    Main3AfterRO = st.checkbox("Main 3 Outage", key='After_RO_main3_disabled')

with col2:
    col2.header('RO-Slaters Lane')
    SlatersROMain0Closed = st.checkbox("Main 0 Outage", key='Slaters_RO_main0_disabled')
    SlatersROMain1Closed = st.checkbox("Main 1 Outage", key='Slaters_RO_main1_disabled')
    SlatersROMain2Closed = st.checkbox("Main 2 Outage", key='Slaters_RO_main2_disabled')
    SlatersROMain3Closed = st.checkbox("Main 3 Outage", key='Slaters_RO_main3_disabled')

with col3:
    col3.header('Slaters Lane-AF')
    AFSlatersMain0Closed = st.checkbox("Main 0 Outage", key='AF_Slaters_main0_disabled')
    AFSlatersMain1Closed = st.checkbox("Main 1 Outage", key='AF_Slaters_main1_disabled')
    AFSlatersMain2Closed = st.checkbox("Main 2 Outage", key='AF_Slaters_main2_disabled')
    AFSlatersMain3Closed = st.checkbox("Main 3 Outage", key='AF_Slaters_main3_disabled')

with col4:
    col4.header('Before AF')
    option1 = st.checkbox("Yard 1 Outage", key='pre_AF_yard1_disabled')
    option2 = st.checkbox("Yard 2 Outage", key='pre_AF_yard2_disabled')
    option3 = st.checkbox("Yard 3 Outage", key='pre_AF_yard3_disabled')
    option4 = st.checkbox("Main 3 Outage", key='pre_AF_main3_disabled')
    option5 = st.checkbox("Main 2 Outage", key='pre_AF_main2_disabled')
    option6 = st.checkbox("Main 1 Outage", key='pre_AF_main1_disabled')
    option7 = st.checkbox("NS Outage",     key='pre_AF_ns_disabled')


# Create the World Object
TRV = World(
    name="TRV",
    deltan=1,
    tmax=1000,
    print_mode=1, save_mode=0, show_mode=1,
    random_seed=0
)


# =====================================   RO - Definitions     ========================================================
# Define Southern (Low MP) Origins
TRV.addNode("Main 0_RO", 30, 12, label_color='white', voffset=.4)          # 0
TRV.addNode("Main 1_RO", 30, 10, label_color='white', voffset=.4)          # 1
TRV.addNode("Main 2_RO", 30, 8, label_color='white', voffset=.4)           # 2
TRV.addNode("Main 3_RO", 30, 6, label_color='white', voffset=.4)           # 3

# Define Northern (High MP) Origins
TRV.addNode("Existing 2_RO", 0, 12, label_color='white', voffset=.4)       # 4
TRV.addNode("Existing 3_RO", 0, 10, label_color='white', voffset=.4)       # 5
TRV.addNode("Proposed_2_org_RO", 6, 8)                                     # 6
TRV.addNode("Proposed_3_org_RO", 10, 6)                                    # 7

# Define Switch Points
TRV.addNode("1_S_RO", 10, 12)                                              # 8
TRV.addNode("3_S_RO", 12, 10)                                              # 9
TRV.addNode("5_S_RO", 16, 10)                                              # 10
TRV.addNode("7_S_RO", 18, 12)                                              # 11
TRV.addNode("9_S_RO", 4, 10)                                               # 12
TRV.addNode("11_S_RO", 20, 10)                                             # 13
TRV.addNode("13_S_RO", 22, 8)                                              # 14
TRV.addNode("15_S_RO", 8, 8)                                               # 15

# Define Links
TRV.addLink("Ex 2_RO", "Existing 2_RO", "1_S_RO", length=20)                    # 0
TRV.addLink("0_1_RO", "1_S_RO", "7_S_RO", length=20)                            # 1
TRV.addLink("Main 0_RO", "7_S_RO", "Main 0_RO", length=20)                      # 2
TRV.addLink("Ex 3_RO", "Existing 3_RO", "9_S_RO", length=20)                    # 3
TRV.addLink("1_1_RO", "9_S_RO", "3_S_RO", length=20)                            # 4
TRV.addLink("1_2_RO", "3_S_RO", "5_S_RO", length=20)                            # 5
TRV.addLink("1_3_RO", "5_S_RO", "11_S_RO", length=20)                           # 6
TRV.addLink("Main 1_RO", "11_S_RO", "Main 1_RO", length=20)                     # 7
TRV.addLink("9_S_RO", "9_S_RO", "Proposed_2_org_RO", length=20)                 # 8
TRV.addLink("2_1_RO", "Proposed_2_org_RO", "15_S_RO", length=20)                # 9
TRV.addLink("2_2_RO", "15_S_RO", "13_S_RO", length=20)                          # 10
TRV.addLink("Main 2_RO", "13_S_RO", "Main 2_RO", length=20)                     # 11
TRV.addLink("15_S_RO", "15_S_RO", "Proposed_3_org_RO", length=20)               # 12
TRV.addLink("Main 3_RO", "Proposed_3_org_RO", "Main 3_RO", length=20)           # 13

# Define X-Overs
TRV.addLink("1-3_RO", "1_S_RO", "3_S_RO", length=20)                            # 14
TRV.addLink("5-7_RO", "5_S_RO", "7_S_RO", length=20)                            # 15
TRV.addLink("11-13_RO", "11_S_RO", "13_S_RO", length=20)                        # 16

# ======================================= Slaters Lane - Definitions ==================================================

# Define Southern (Low MP) Origins
TRV.addNode("RO-Slaters Main 0", 30, 12, label_color='white', voffset=.4)        # 16
TRV.addNode("RO-Slaters Main 1", 30, 10, label_color='white', voffset=.4)        # 17
TRV.addNode("RO-Slaters Main 2", 30, 8, label_color='white', voffset=.4)         # 18
TRV.addNode("RO-Slaters Main 3", 30, 6, label_color='white', voffset=.4)         # 19

# Define Northern (High MP) Origins
TRV.addNode("OOS_NS", 58.5, 14, label_color='white', voffset=.4, hoffset=-.5)     # 20
TRV.addNode("Slaters-AF Main 0", 60, 12, label_color='white', voffset=.4)         # 21
TRV.addNode("Slaters-AF Main 1", 60, 10, label_color='white', voffset=.4)         # 22
TRV.addNode("Slaters-AF Main 2", 60, 8, label_color='white', voffset=.4)          # 23
TRV.addNode("Slaters-AF Main 3", 60, 6, label_color='white', voffset=.4)          # 24

# Define Switch Points
TRV.addNode("NS_OOS", 54, 14)             # 25
TRV.addNode("3_S", 52, 12)                # 26
TRV.addNode("5_S", 54, 6)                 # 27
TRV.addNode("7_S", 52, 8)                 # 28
TRV.addNode("9_S", 45, 8)                 # 29
TRV.addNode("11_S", 43, 10)               # 30
TRV.addNode("13_S", 50, 10)               # 31
TRV.addNode("15_S", 48, 12)               # 32
TRV.addNode("17_S", 38, 12)               # 33
TRV.addNode("19_S", 36, 10)               # 34
TRV.addNode("21_S", 38, 8)                # 35
TRV.addNode("23_S", 36, 6)                # 36

# Track Segments
TRV.addLink("PepCo  Lead", "OOS_NS", "NS_OOS", length=50)              # 17
TRV.addLink("3_S", "NS_OOS", "3_S", length=50)                         # 18
TRV.addLink("0_0", "Slaters-AF Main 0", "3_S", length=50)              # 19
TRV.addLink("0_1", "3_S", "15_S", length=50)                           # 20
TRV.addLink("0_2", "15_S", "17_S", length=50)                          # 21
TRV.addLink("0_3", "17_S", "RO-Slaters Main 0", length=50)             # 22
TRV.addLink("1_0", "Slaters-AF Main 1", "13_S", length=50)             # 23
TRV.addLink("1_1", "13_S", "11_S", length=50)                          # 24
TRV.addLink("1_2", "11_S", "19_S", length=50)                          # 25
TRV.addLink("1_3", "19_S", "RO-Slaters Main 1", length=50)             # 26
TRV.addLink("2_0", "Slaters-AF Main 2", "7_S", length=50)              # 27
TRV.addLink("2_1", "7_S", "9_S", length=50)                            # 28
TRV.addLink("2_2", "9_S", "21_S", length=50)                           # 29
TRV.addLink("2_3", "RO-Slaters Main 2", "21_S", length=50)             # 30
TRV.addLink("3_0", "Slaters-AF Main 3", "5_S", length=50)              # 31
TRV.addLink("3_1", "5_S", "23_S", length=50)                           # 32
TRV.addLink("3_2", "23_S", "RO-Slaters Main 3", length=50)             # 33

# Cross Overs
TRV.addLink("13_15X", "13_S", "15_S", length=20)                       # 34
TRV.addLink("5_7X", "5_S", "7_S", length=20)                           # 35
TRV.addLink("9_11X", "9_S", "11_S", length=20)                         # 36
TRV.addLink("17_19X", "17_S", "19_S", length=20)                       # 37
TRV.addLink("21_23X", "21_S", "23_S", length=20)                       # 38

# =========================================== AF - Definitions ========================================================

# Define Southern (Low MP) Origins
TRV.addNode("NS Horn Track 1_AF", 90, 1, label_color='white', voffset=.4, hoffset=1)        # 0
TRV.addNode("y1e_AF", 84, 1)                                                                # 1
TRV.addNode("NS Horn Track 2_AF", 90, 3.5, label_color='white', voffset=.4, hoffset=1)      # 2
TRV.addNode("NS Horn Track 3_AF", 90, 6, label_color='white', voffset=.4, hoffset=1)        # 3
TRV.addNode("Ex Main 3_AF", 90, 8, label_color='white', voffset=.4, hoffset=.5)             # 4
TRV.addNode("Ex Main 2_AF", 90, 10, label_color='white', voffset=.4, hoffset=.5)            # 5
TRV.addNode("Ex Main 1_AF", 90, 12, label_color='white', voffset=.4, hoffset=.5)            # 6
TRV.addNode("NS_org_AF", 76, 14)                                                            # 7
TRV.addNode("NS_yard_AF", 90, 14, label_color='white', voffset=.4, hoffset=.25)             # 8
TRV.addNode("Setoff_org_AF", 68, 14)                                                        # 9
TRV.addNode("Setoff Track_AF", 61, 14, label_color='white', voffset=.4, hoffset=1)          # 10

# Define Switches
TRV.addNode("1_S_AF", 86.5, 3.5)            # 11
TRV.addNode("3_S_AF", 84, 6)                # 12
TRV.addNode("5_S_AF", 82, 6)                # 13
TRV.addNode("6_S_AF", 79, 6)                # 14
TRV.addNode("7_S_AF", 80, 8)                # 15
TRV.addNode("9_S_AF", 80, 10)               # 16
TRV.addNode("11_S_AF", 78, 12)              # 17
TRV.addNode("13_S_AF", 78, 8)               # 18
TRV.addNode("19_S_AF", 76, 10)              # 19
TRV.addNode("21_S_AF", 75, 10)              # 20
TRV.addNode("23_S_AF", 73, 8)               # 21
TRV.addNode("25_S_AF", 74, 10)              # 22
TRV.addNode("27_S_AF", 74, 12)              # 23
TRV.addNode("29_S_AF", 72, 12)              # 24
TRV.addNode("31_S_AF", 71, 12)              # 25
TRV.addNode("33_S_AF", 69, 10)              # 26
TRV.addNode("35_S_AF", 70, 12)              # 27
TRV.addNode("37_S_AF", 68, 10)              # 28
TRV.addNode("39_S_AF", 66, 12)              # 29
TRV.addNode("41_S_AF", 70, 8)               # 30
TRV.addNode("43_S_AF", 68, 6)               # 31
TRV.addNode("45_S_AF", 67, 10)              # 32
TRV.addNode("47_S_AF", 65, 8)               # 33

# Add Destinations
TRV.addNode("Main 0_AF", 60, 12, label_color='white', voffset=.4)     # 34
TRV.addNode("Main 1_AF", 60, 10, label_color='white', voffset=.4)     # 35
TRV.addNode("Main 2_AF", 60, 8, label_color='white', voffset=.4)      # 36
TRV.addNode("Main 3_AF", 60, 6, label_color='white', voffset=.4)      # 37

# Define links between Values
# Crossovers
TRV.addLink("1-3X_AF", "1_S_AF", "3_S_AF", length=50, free_flow_speed=30, number_of_lanes=1)      # 0
TRV.addLink("5-7X_AF", "5_S_AF", "7_S_AF", length=50, free_flow_speed=30, number_of_lanes=1)      # 1
TRV.addLink("9-11X_AF", "9_S_AF", "11_S_AF", length=50, free_flow_speed=30, number_of_lanes=1)    # 2
TRV.addLink("13-19X_AF", "13_S_AF", "19_S_AF", length=50, free_flow_speed=30, number_of_lanes=1)  # 3
TRV.addLink("21-23X_AF", "21_S_AF", "23_S_AF", length=50, free_flow_speed=30, number_of_lanes=1)  # 4
TRV.addLink("25-29X_AF", "25_S_AF", "29_S_AF", length=50, free_flow_speed=30, number_of_lanes=1)  # 5
TRV.addLink("31-33X_AF", "31_S_AF", "33_S_AF", length=50, free_flow_speed=30, number_of_lanes=1)  # 6
TRV.addLink("37-39X_AF", "37_S_AF", "39_S_AF", length=50, free_flow_speed=30, number_of_lanes=1)  # 7
TRV.addLink("41-43X_AF", "41_S_AF", "43_S_AF", length=50, free_flow_speed=30, number_of_lanes=1)  # 8
TRV.addLink("45-47X_AF", "45_S_AF", "47_S_AF", length=50, free_flow_speed=30, number_of_lanes=1)  # 9

# Yard Segments
TRV.addLink("yard1_AF", "NS Horn Track 1_AF", "y1e_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)             # 10
TRV.addLink("y1_2_AF", "y1e_AF", "6_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)                          # 11
TRV.addLink("yard2_AF", "NS Horn Track 2_AF", "1_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)             # 12
TRV.addLink("NS_AF", "NS_org_AF", "27_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)                        # 13
TRV.addLink("NS Yard_AF", "NS_yard_AF", "NS_org_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)                # 14
TRV.addLink("Setoff_Track_AF", "Setoff Track_AF", "Setoff_org_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)  # 15
TRV.addLink("Setoff Track_AF", "35_S_AF", "Setoff_org_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)          # 16

# Main 0 Segments
TRV.addLink("0_0_AF", "Ex Main 1_AF", "11_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)  # 17
TRV.addLink("0_1_AF", "11_S_AF", "27_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)       # 18
TRV.addLink("0_2_AF", "27_S_AF", "29_S_AF", length=50, free_flow_speed=50, number_of_lanes=1)                           # 19
TRV.addLink("0_3_AF", "29_S_AF", "31_S_AF", length=50, free_flow_speed=50, number_of_lanes=1)                           # 20
TRV.addLink("0_4_AF", "31_S_AF", "35_S_AF", length=50, free_flow_speed=50, number_of_lanes=1)                           # 21
TRV.addLink("0_5_AF", "35_S_AF", "39_S_AF", length=50, free_flow_speed=50, number_of_lanes=1)                           # 22
TRV.addLink("0_6_AF", "39_S_AF", "Main 0_AF", length=50, free_flow_speed=50, number_of_lanes=1)                         # 23

# Main 1 Segments
TRV.addLink("1_0_AF", "Ex Main 2_AF", "9_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)    # 24
TRV.addLink("1_1_AF", "9_S_AF", "19_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)         # 25
TRV.addLink("1_2_AF", "19_S_AF", "21_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)        # 26
TRV.addLink("1_3_AF", "21_S_AF", "25_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)        # 27
TRV.addLink("1_4_AF", "25_S_AF", "33_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)        # 28
TRV.addLink("1_5_AF", "33_S_AF", "37_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)        # 29
TRV.addLink("1_6_AF", "37_S_AF", "45_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)        # 30
TRV.addLink("1_7_AF", "45_S_AF", "Main 1_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)      # 31

# Main 2 Segments
TRV.addLink("2_0_AF", "Ex Main 3_AF", "7_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)    # 32
TRV.addLink("2_1_AF", "7_S_AF", "13_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)         # 33
TRV.addLink("2_2_AF", "13_S_AF", "23_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)        # 34
TRV.addLink("2_3_AF", "23_S_AF", "41_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)        # 35
TRV.addLink("2_4_AF", "41_S_AF", "47_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)        # 36
TRV.addLink("2_5_AF", "47_S_AF", "Main 2_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)      # 37

# Main 3 Segments
TRV.addLink("3_0_AF", "NS Horn Track 3_AF", "3_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)  # 38
TRV.addLink("3_1_AF", "3_S_AF", "5_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)              # 39
TRV.addLink("3_2_AF", "5_S_AF", "6_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)              # 40
TRV.addLink("3_3_AF", "6_S_AF", "43_S_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)             # 41
TRV.addLink("3_4_AF", "43_S_AF", "Main 3_AF", length=50, free_flow_speed=50, number_of_lanes=1, merge_priority=0.1)          # 42


# ================================= Signal Controls - RO ===========================================================

if Main2AfterRO & Main3AfterRO:
    for link in TRV.LINKS:
        link.color = 'red'
    for node in TRV.NODES:
        node.color = 'red'

if Main2AfterRO:
    TRV.LINKS[0].color = 'red'     # Existing 2_RO
    TRV.LINKS[1].color = 'red'     # 0_1_RO
    TRV.LINKS[14].color = 'red'    # 1-3_RO

    TRV.NODES[4].color = 'red'     # Existing 2_RO
    TRV.NODES[8].color = 'red'     # 1_S_RO

elif Main3AfterRO:
    TRV.LINKS[3].color = 'red'   # Ex 3_RO
    TRV.LINKS[4].color = 'red'   # 1_1_RO
    TRV.LINKS[8].color = 'red'   # 9_S_RO
    TRV.LINKS[9].color = 'red'   # 2_1_RO
    TRV.LINKS[10].color = 'red'  # 2_2_RO
    TRV.LINKS[12].color = 'red'  # 15_S_RO
    TRV.LINKS[13].color = 'red'  # Main 3_RO

    TRV.NODES[5].color = 'red'   # Existing 3_RO
    TRV.NODES[6].color = 'red'   # Proposed_2_org_RO
    TRV.NODES[7].color = 'red'   # Proposed_3_org_RO
    TRV.NODES[12].color = 'red'  # 9_S_RO
    TRV.NODES[15].color = 'red'  # 15_S_RO

# Update the graph depending on what routes are closed
# 1 combination with all 4 tracks closed
if SlatersROMain3Closed and SlatersROMain2Closed and SlatersROMain1Closed and SlatersROMain0Closed:
    for link in TRV.LINKS:
        link.color = 'red'
    for node in TRV.NODES:
        node.color = 'red'

# 4 combos of 3 tracks closed
elif SlatersROMain0Closed and SlatersROMain1Closed and SlatersROMain2Closed:
    TRV.LINKS[0].color = 'red'   # Ex 2_RO
    TRV.LINKS[1].color = 'red'   # 0_1_RO
    TRV.LINKS[2].color = 'red'   # Main 0_RO
    TRV.LINKS[4].color = 'red'   # 1_1_RO
    TRV.LINKS[5].color = 'red'   # 1_2_RO
    TRV.LINKS[6].color = 'red'   # 1_3_RO
    TRV.LINKS[7].color = 'red'   # Main 1_RO
    TRV.LINKS[10].color = 'red'  # 2_2_RO
    TRV.LINKS[11].color = 'red'  # Main 2_RO
    TRV.LINKS[14].color = 'red'  # 1-3_RO
    TRV.LINKS[15].color = 'red'  # 5-7_RO
    TRV.LINKS[16].color = 'red'  # 11-13_RO

    TRV.NODES[0].color = 'red'   # Main 0_RO
    TRV.NODES[1].color = 'red'   # Main 1_RO
    TRV.NODES[2].color = 'red'   # Main 2_RO
    TRV.NODES[4].color = 'red'   # Exisiting 2_RO
    TRV.NODES[8].color = 'red'   # 1_S_RO
    TRV.NODES[9].color = 'red'   # 3_S_RO
    TRV.NODES[10].color = 'red'  # 5_S_RO
    TRV.NODES[11].color = 'red'  # 7_S_RO
    TRV.NODES[13].color = 'red'  # 11_S_RO
    TRV.NODES[14].color = 'red'  # 13_S_RO

elif SlatersROMain0Closed and SlatersROMain1Closed and SlatersROMain3Closed:
    TRV.LINKS[1].color = 'red'   # 0_1_RO
    TRV.LINKS[2].color = 'red'   # Main 0_RO
    TRV.LINKS[7].color = 'red'   # Main 1_RO
    TRV.LINKS[12].color = 'red'  # 15_S_RO
    TRV.LINKS[13].color = 'red'  # Main 3_RO
    TRV.LINKS[15].color = 'red'  # 5-7_RO

    TRV.NODES[0].color = 'red'    # Main 0_RO
    TRV.NODES[1].color = 'red'    # Main 1_RO
    TRV.NODES[3].color = 'red'    # Main 3_RO
    TRV.NODES[7].color = 'red'    # Proposed_3_org_RO
    TRV.NODES[11].color = 'red'   # 7_S_RO

elif SlatersROMain0Closed and SlatersROMain2Closed and SlatersROMain3Closed:
    TRV.LINKS[1].color = 'red'    # 0_1_RO
    TRV.LINKS[2].color = 'red'    # Main 0_RO
    TRV.LINKS[8].color = 'red'    # 9_S_RO
    TRV.LINKS[9].color = 'red'    # 2_1_RO
    TRV.LINKS[10].color = 'red'   # 2_2_RO
    TRV.LINKS[11].color = 'red'   # Main 2_RO
    TRV.LINKS[12].color = 'red'   # 15_S_RO
    TRV.LINKS[13].color = 'red'   # Main 3_RO
    TRV.LINKS[15].color = 'red'   # 5-7_RO
    TRV.LINKS[16].color = 'red'   # 11-13_RO

    TRV.NODES[0].color = 'red'    # Main 0_RO
    TRV.NODES[2].color = 'red'    # Main 2_RO
    TRV.NODES[3].color = 'red'    # Main 3_RO
    TRV.NODES[6].color = 'red'    # Proposed_2_org_RO
    TRV.NODES[7].color = 'red'    # Proposed_3_org_RO
    TRV.NODES[11].color = 'red'   # 7_S_RO
    TRV.NODES[14].color = 'red'   # 13_S_RO
    TRV.NODES[15].color = 'red'  # 15_S_RO

elif SlatersROMain1Closed and SlatersROMain2Closed and SlatersROMain3Closed:
    TRV.LINKS[6].color = 'red'    # 1_3_RO
    TRV.LINKS[7].color = 'red'    # Main 1_RO
    TRV.LINKS[8].color = 'red'    # 9_S_RO
    TRV.LINKS[9].color = 'red'    # 2_1_RO
    TRV.LINKS[10].color = 'red'   # 2_2_RO
    TRV.LINKS[11].color = 'red'   # Main 2_RO
    TRV.LINKS[12].color = 'red'   # 15_S_RO
    TRV.LINKS[13].color = 'red'   # Main 3_RO
    TRV.LINKS[14].color = 'red'   # 1-3_RO
    TRV.LINKS[16].color = 'red'   # 11-13_RO

    TRV.NODES[1].color = 'red'    # Main 1_RO
    TRV.NODES[2].color = 'red'    # Main 2_RO
    TRV.NODES[3].color = 'red'    # Main 3_RO
    TRV.NODES[6].color = 'red'    # Proposed_2_org_RO
    TRV.NODES[7].color = 'red'    # Proposed_3_org_RO
    TRV.NODES[13].color = 'red'   # 11_S_RO
    TRV.NODES[14].color = 'red'   # 13_S_RO
    TRV.NODES[15].color = 'red'   # 15_S_RO

# 6 combos of 2 tracks closed
elif SlatersROMain0Closed and SlatersROMain1Closed:
    TRV.LINKS[1].color = 'red'  # 0_1_RO
    TRV.LINKS[2].color = 'red'  # Main 0_RO
    TRV.LINKS[7].color = 'red'    # Main 1_RO
    TRV.LINKS[15].color = 'red'   # 5-7_RO

    TRV.NODES[0].color = 'red'    # Main 0_RO
    TRV.NODES[1].color = 'red'    # Main 1_RO
    TRV.NODES[11].color = 'red'   # 7_S_RO

elif SlatersROMain0Closed and SlatersROMain2Closed:
    TRV.LINKS[1].color = 'red'    # 0_1_RO
    TRV.LINKS[2].color = 'red'    # Main 0_RO
    TRV.LINKS[10].color = 'red'   # 2_2_RO
    TRV.LINKS[11].color = 'red'   # Main 2_RO
    TRV.LINKS[15].color = 'red'   # 5-7_RO
    TRV.LINKS[16].color = 'red'   # 11-13_RO

    TRV.NODES[0].color = 'red'    # Main 0_RO
    TRV.NODES[2].color = 'red'    # Main 2_RO
    TRV.NODES[11].color = 'red'   # 7_S_RO
    TRV.NODES[14].color = 'red'   # 13_S_RO

elif SlatersROMain0Closed and SlatersROMain3Closed:
    TRV.LINKS[1].color = 'red'    # 0_1_RO
    TRV.LINKS[2].color = 'red'    # Main 0_RO
    TRV.LINKS[12].color = 'red'   # 15_S_RO
    TRV.LINKS[13].color = 'red'   # Main 3_RO
    TRV.LINKS[15].color = 'red'   # 5-7_RO

    TRV.NODES[0].color = 'red'    # Main 0_RO
    TRV.NODES[3].color = 'red'    # Main 3_RO
    TRV.NODES[7].color = 'red'    # Proposed_3_org_RO
    TRV.NODES[11].color = 'red'   # 7_S_RO

elif SlatersROMain1Closed and SlatersROMain2Closed:
    TRV.LINKS[6].color = 'red'    # 1_3_RO
    TRV.LINKS[7].color = 'red'    # Main 1_RO
    TRV.LINKS[10].color = 'red'   # 2_2_RO
    TRV.LINKS[11].color = 'red'   # Main 2_RO
    TRV.LINKS[14].color = 'red'   # 1-3_RO
    TRV.LINKS[16].color = 'red'   # 11-13_RO

    TRV.NODES[1].color = 'red'    # Main 1_RO
    TRV.NODES[2].color = 'red'    # Main 2_RO
    TRV.NODES[13].color = 'red'   # 11_S_RO
    TRV.NODES[14].color = 'red'   # 13_S_RO

elif SlatersROMain1Closed and SlatersROMain3Closed:
    TRV.LINKS[12].color = 'red'   # 15_S_RO
    TRV.LINKS[13].color = 'red'   # Main 3_RO
    TRV.LINKS[7].color = 'red'    # Main 1_RO

    TRV.NODES[1].color = 'red'    # Main 1_RO
    TRV.NODES[3].color = 'red'    # Main 3_RO
    TRV.NODES[7].color = 'red'    # Proposed_3_org_RO

elif SlatersROMain3Closed and SlatersROMain2Closed:
    TRV.LINKS[8].color = 'red'    # 9_S_RO
    TRV.LINKS[9].color = 'red'    # 2_1_RO
    TRV.LINKS[10].color = 'red'   # 2_2_RO
    TRV.LINKS[11].color = 'red'   # Main 2_RO
    TRV.LINKS[12].color = 'red'   # 15_S_RO
    TRV.LINKS[13].color = 'red'   # Main 3_RO
    TRV.LINKS[16].color = 'red'   # 11-13_RO

    TRV.NODES[2].color = 'red'    # Main 2_RO
    TRV.NODES[3].color = 'red'    # Main 3_RO
    TRV.NODES[6].color = 'red'    # Proposed_2_org_RO
    TRV.NODES[7].color = 'red'    # Proposed_3_org_RO
    TRV.NODES[14].color = 'red'   # 13_S_RO
    TRV.NODES[15].color = 'red'   # 15_S_RO

# 4 versions of 1 track closed (0,0,0,0 is 16th possible combo and not included since it's the default state)
elif SlatersROMain3Closed:
    TRV.LINKS[12].color = 'red'   # 15_S_RO
    TRV.LINKS[13].color = 'red'   # Main 3_RO

    TRV.NODES[3].color = 'red'    # Main 3_RO
    TRV.NODES[7].color = 'red'    # Proposed_3_org_RO

elif SlatersROMain2Closed:
    TRV.LINKS[10].color = 'red'   # 2_2_RO
    TRV.LINKS[11].color = 'red'   # Main 2_RO
    TRV.LINKS[16].color = 'red'   # 11-13_RO

    TRV.NODES[2].color = 'red'    # Main 2_RO
    TRV.NODES[14].color = 'red'   # 13_S_RO

elif SlatersROMain1Closed:
    TRV.LINKS[7].color = 'red'    # Main 1_RO

    TRV.NODES[1].color = 'red'    # Main 1_RO

elif SlatersROMain0Closed:
    TRV.LINKS[1].color = 'red'    # 0_1_RO
    TRV.LINKS[2].color = 'red'    # Main 0_RO
    TRV.LINKS[15].color = 'red'   # 5-7_RO

    TRV.NODES[0].color = 'red'    # Main 0_RO
    TRV.NODES[11].color = 'red'   # 7_S_RO

# Determine if the Routes are open or closed on either side of the interlocking
TRV.signal_attributes_high = {
    # Origin Values (color, position, opp end color)
    'Existing 2': (TRV.LINKS[0].color, (3, 10.75), TRV.LINKS[2].color),
    'Existing 3': (TRV.LINKS[3].color, (3, 8.75), TRV.LINKS[7].color),
}

TRV.signal_attributes_low = {
    # Destinations
    'Proposed 0': (TRV.LINKS[2].color, (22.5, 12.75), TRV.LINKS[0].color),
    'Proposed 1': (TRV.LINKS[7].color, (22.5, 10.75), TRV.LINKS[3].color),
    'Proposed 2': (TRV.LINKS[11].color, (22.5, 8.75), TRV.LINKS[3].color),
    'Proposed 3': (TRV.LINKS[13].color, (22.5, 6.75), TRV.LINKS[3].color)
}

# ================================= Signal Controls - Slaters =========================================================


# Either of all 4 tracks closed on either side
if (AFSlatersMain0Closed and AFSlatersMain1Closed and AFSlatersMain2Closed and AFSlatersMain3Closed) \
        or (SlatersROMain0Closed and SlatersROMain1Closed and SlatersROMain2Closed and SlatersROMain3Closed):
    for link in TRV.LINKS:
        link.color = 'red'
    for node in TRV.NODES:
        node.color = 'red'

# All combos of 2 closed tracks
elif SlatersROMain0Closed & SlatersROMain1Closed:
    TRV.LINKS[17].color = 'red'   # Pepco Lead
    TRV.LINKS[18].color = 'red'   # 3_S
    TRV.LINKS[19].color = 'red'   # 0_0
    TRV.LINKS[20].color = 'red'   # 0_1
    TRV.LINKS[21].color = 'red'   # 0_2
    TRV.LINKS[23].color = 'red'   # 1_0
    TRV.LINKS[24].color = 'red'   # 1_1
    TRV.LINKS[25].color = 'red'   # 1_2
    TRV.LINKS[34].color = 'red'  # 13_15X
    TRV.LINKS[36].color = 'red'  # 9_11X
    TRV.LINKS[37].color = 'red'  # 17_19X

    TRV.NODES[4].color = 'red'   # OOS_NS
    TRV.NODES[5].color = 'red'  # Slaters-AF Main 0
    TRV.NODES[6].color = 'red'  # Slaters-AF Main 1
    TRV.NODES[9].color = 'red'   # NS_OOS
    TRV.NODES[10].color = 'red'  # 3_S
    TRV.NODES[14].color = 'red'  # 11_S
    TRV.NODES[15].color = 'red'  # 13_S
    TRV.NODES[16].color = 'red'  # 15_S
    TRV.NODES[17].color = 'red'  # 17_S
    TRV.NODES[18].color = 'red'  # 18_S

elif SlatersROMain0Closed & SlatersROMain2Closed:
    # Comment to collapse in IDE
    TRV.LINKS[34].color = 'red'  # 13_15X

elif SlatersROMain0Closed & SlatersROMain3Closed:
    TRV.NODES[20].color = 'red'  # 23_S

    TRV.LINKS[34].color = 'red'  # 13_15X
    TRV.LINKS[38].color = 'red'  # 21_23X
    TRV.LINKS[32].color = 'red'  # 3_1

elif SlatersROMain1Closed & SlatersROMain2Closed:
    TRV.LINKS[24].color = 'red'   # 1_1
    TRV.LINKS[25].color = 'red'   # 1_2
    TRV.LINKS[35].color = 'red'  # 5_7X
    TRV.LINKS[36].color = 'red'  # 9_11X
    TRV.LINKS[37].color = 'red'  # 17_19X

    TRV.NODES[14].color = 'red'  # 11_S
    TRV.NODES[18].color = 'red'  # 19_S

elif SlatersROMain1Closed & SlatersROMain3Closed:
    TRV.LINKS[24].color = 'red'   # 1_2
    TRV.LINKS[25].color = 'red'   # 1_1
    TRV.LINKS[36].color = 'red'  # 9_11X
    TRV.LINKS[20].color = 'red'  # 17_19X
    TRV.LINKS[38].color = 'red'  # 21_23X
    TRV.LINKS[32].color = 'red'  # 3_1

    TRV.NODES[14].color = 'red'  # 11_S
    TRV.NODES[18].color = 'red'  # 19_S
    TRV.NODES[20].color = 'red'  # 23_S

elif SlatersROMain2Closed & SlatersROMain3Closed:
    TRV.LINKS[29].color = 'red'  # 2_2
    TRV.LINKS[32].color = 'red'  # 3_1
    TRV.LINKS[38].color = 'red'  # 21_23X

    TRV.NODES[19].color = 'red'  # 21_S
    TRV.NODES[20].color = 'red'  # 23_S

elif SlatersROMain0Closed & AFSlatersMain0Closed:
    TRV.LINKS[17].color = 'red'   # Pepco Lead
    TRV.LINKS[18].color = 'red'  # 3_S
    TRV.LINKS[20].color = 'red'  # 0_1
    TRV.LINKS[21].color = 'red'  # 0_2
    TRV.LINKS[37].color = 'red'  # 17_19X
    TRV.LINKS[34].color = 'red'  # 13_15X

    TRV.NODES[10].color = 'red'  # 3_S
    TRV.NODES[16].color = 'red'  # 15_S
    TRV.NODES[17].color = 'red'  # 17_S
    TRV.NODES[4].color = 'red'   # OOS_NS
    TRV.NODES[9].color = 'red'   # NS_OOS

elif SlatersROMain0Closed & AFSlatersMain1Closed:
    TRV.LINKS[24].color = 'red'   # 1_1
    TRV.LINKS[34].color = 'red'  # 13_15X

    TRV.NODES[15].color = 'red'  # 13_S


# AF/Slaters Closed
elif AFSlatersMain0Closed & AFSlatersMain1Closed:
    TRV.LINKS[17].color = 'red'  # Pepco Lead
    TRV.LINKS[18].color = 'red'  # 3_S
    TRV.LINKS[20].color = 'red'  # 0_1
    TRV.LINKS[21].color = 'red'  # 0_2
    TRV.LINKS[22].color = 'red'  # 0_3
    TRV.LINKS[24].color = 'red'  # 1_1X
    TRV.LINKS[34].color = 'red'  # 13_15X
    TRV.LINKS[37].color = 'red'  # 17_19X

    TRV.NODES[0].color = 'red'   # RO-Slaters Main 0
    TRV.NODES[4].color = 'red'   # OOS_NS
    TRV.NODES[9].color = 'red'   # NS_OOS
    TRV.NODES[10].color = 'red'  # 3_S
    TRV.NODES[15].color = 'red'  # 13_S
    TRV.NODES[16].color = 'red'  # 15_S
    TRV.NODES[17].color = 'red'  # 17_S

elif AFSlatersMain0Closed & AFSlatersMain2Closed:
    TRV.LINKS[20].color = 'red'  # 0_1
    TRV.LINKS[37].color = 'red'  # 17_19X

    TRV.NODES[10].color = 'red'  # 3_S
    TRV.NODES[17].color = 'red'  # 17_S

elif AFSlatersMain0Closed & AFSlatersMain3Closed:
    TRV.LINKS[20].color = 'red'   # 0_1
    TRV.LINKS[32].color = 'red'  # 3_1
    TRV.LINKS[35].color = 'red'  # 5_7X
    TRV.LINKS[37].color = 'red'  # 17_19X

    TRV.NODES[10].color = 'red'  # 3_S
    TRV.NODES[11].color = 'red'  # 5_S
    TRV.NODES[17].color = 'red'  # 17_S

elif AFSlatersMain1Closed & AFSlatersMain2Closed:
    TRV.LINKS[24].color = 'red'  # 1_1
    TRV.LINKS[34].color = 'red'  # 13_15X

    TRV.NODES[15].color = 'red'  # 13_S

elif AFSlatersMain1Closed & AFSlatersMain3Closed:
    TRV.LINKS[24].color = 'red'   # 1_1
    TRV.LINKS[22].color = 'red'  # 3_1
    TRV.LINKS[34].color = 'red'  # 13_15X
    TRV.LINKS[35].color = 'red'  # 5_7X

    TRV.NODES[11].color = 'red'  # 5_S
    TRV.NODES[15].color = 'red'  # 13_S

elif AFSlatersMain2Closed & AFSlatersMain3Closed:
    TRV.LINKS[28].color = 'red'  # 2_1
    TRV.LINKS[29].color = 'red'  # 2_2
    TRV.LINKS[30].color = 'red'  # 2_3
    TRV.LINKS[32].color = 'red'  # 3_1
    TRV.LINKS[33].color = 'red'  # 3_2
    TRV.LINKS[35].color = 'red'  # 5_7X
    TRV.LINKS[36].color = 'red'  # 9_11X
    TRV.LINKS[38].color = 'red'  # 21_23X

    TRV.NODES[2].color = 'red'  # RO-Slaters Main 2
    TRV.NODES[3].color = 'red'  # RO-Slaters Main 3
    TRV.NODES[11].color = 'red'  # 5_S
    TRV.NODES[12].color = 'red'  # 7_S
    TRV.NODES[13].color = 'red'  # 9_S
    TRV.NODES[19].color = 'red'  # 21_S
    TRV.NODES[20].color = 'red'  # 23_S

elif AFSlatersMain1Closed & SlatersROMain1Closed:
    TRV.LINKS[24].color = 'red'   # 1_1
    TRV.LINKS[25].color = 'red'   # 1_2
    TRV.LINKS[34].color = 'red'  # 13_15X
    TRV.LINKS[36].color = 'red'  # 9_11X
    TRV.LINKS[37].color = 'red'  # 17_19X

    TRV.NODES[14].color = 'red'  # 11_S
    TRV.NODES[18].color = 'red'  # 19_S
    TRV.NODES[15].color = 'red'  # 13_S

elif AFSlatersMain2Closed & SlatersROMain2Closed:
    TRV.LINKS[27].color = 'red'  # 2_1
    TRV.LINKS[29].color = 'red'  # 2_2
    TRV.LINKS[35].color = 'red'  # 5_7X
    TRV.LINKS[36].color = 'red'  # 9_11X
    TRV.LINKS[38].color = 'red'  # 21_23X

    TRV.NODES[12].color = 'red'  # 7_S
    TRV.NODES[13].color = 'red'  # 9_S
    TRV.NODES[19].color = 'red'  # 21_S

elif AFSlatersMain3Closed & SlatersROMain3Closed:
    TRV.LINKS[32].color = 'red'  # 3_1
    TRV.LINKS[35].color = 'red'  # 5_7X
    TRV.LINKS[38].color = 'red'  # 21_23X

    TRV.NODES[11].color = 'red'  # 5_S
    TRV.NODES[20].color = 'red'  # 23_S

# 1 track of RO-Slaters Closed
elif SlatersROMain0Closed and not (AFSlatersMain2Closed or AFSlatersMain3Closed):
    # Comment to make the statement collapsible in IDE
    TRV.LINKS[34].color = 'red'  # 13_15X

elif SlatersROMain1Closed:
    TRV.LINKS[24].color = 'red'   # 1_2
    TRV.LINKS[25].color = 'red'   # 1_1
    TRV.LINKS[36].color = 'red'  # 9_11X
    TRV.LINKS[37].color = 'red'  # 17_19X

    TRV.NODES[14].color = 'red'  # 11_S
    TRV.NODES[18].color = 'red'  # 19_S

elif SlatersROMain2Closed:
    # Handled by the associated track segment logic alone
    pass

elif SlatersROMain3Closed:
    TRV.LINKS[38].color = 'red'  # 21_23X
    TRV.LINKS[32].color = 'red'  # 3_1

    TRV.NODES[20].color = 'red'  # 23_S


# 1 Track of AF - SlatersMain closed
elif AFSlatersMain0Closed:
    TRV.LINKS[20].color = 'red'   # 0_1
    TRV.NODES[10].color = 'red'   # 3_S

elif AFSlatersMain1Closed:
    TRV.LINKS[24].color = 'red'   # 1_1X
    TRV.LINKS[32].color = 'red'  # 13_15X

    TRV.NODES[15].color = 'red'  # 13_S

elif AFSlatersMain2Closed:
    # Handled by the associated track segment logic alone
    pass

elif AFSlatersMain3Closed:
    TRV.LINKS[32].color = 'red'  # 3_1
    TRV.LINKS[35].color = 'red'  # 5_7X

    TRV.NODES[11].color = 'red'  # 5_S

# Determine if the Routes are open or closed on either side of the interlocking
slaters_signals_1 = {
    # Slaters RO (color, position, opp end color)
    'slaters_Proposed 0_1': (TRV.LINKS[22].color, (34, 10.75), TRV.LINKS[19].color),
    'slaters_Proposed 1_2': (TRV.LINKS[26].color, (34, 8.75), TRV.LINKS[23].color),
    'slaters_Proposed 2_3': (TRV.LINKS[30].color, (34, 6.75), TRV.LINKS[27].color),
    'slaters_Proposed 3_4': (TRV.LINKS[33].color, (34, 4.75), TRV.LINKS[31].color)
}

TRV.signal_attributes_high.update(slaters_signals_1)

slaters_signals_2 = {
    # AF to Slaters
    'slaters_OOS_NS_5': (TRV.LINKS[17].color, (54.5, 14.75), 'yard'),
    'slaters_Proposed 0_6': (TRV.LINKS[19].color, (54.5, 12.75), TRV.LINKS[22].color),
    'slaters_Proposed 1_7': (TRV.LINKS[23].color, (54.5, 10.75), TRV.LINKS[26].color),
    'slaters_Proposed 2_8': (TRV.LINKS[27].color, (54.5, 8.75), TRV.LINKS[30].color),
    'slaters_Proposed 3_9': (TRV.LINKS[31].color, (54.5, 6.75), TRV.LINKS[33].color)
}

TRV.signal_attributes_low.update(slaters_signals_2)


# ==================================== Signal Controls - AF ===========================================================

# Update the graph depending on what routes are closed
# 1 combination with all 4 tracks closed
if AFSlatersMain0Closed and AFSlatersMain1Closed and AFSlatersMain2Closed and AFSlatersMain3Closed:
    for link in TRV.LINKS:
        link.color = 'red'
    for node in TRV.NODES:
        node.color = 'red'

# 4 combos of 3 tracks closed
elif AFSlatersMain0Closed and AFSlatersMain1Closed and AFSlatersMain2Closed:
    # Example of closing main 0/1/2
    TRV.LINKS[1].color = 'red'   # 25-29X_AF
    TRV.LINKS[2].color = 'red'   # 9-11X_AF
    TRV.LINKS[3].color = 'red'   # 13-19X_AF
    TRV.LINKS[5].color = 'red'   # 25-29X_AF
    TRV.LINKS[6].color = 'red'   # 31-33X_AF
    TRV.LINKS[7].color = 'red'   # 37-39X_AF
    TRV.LINKS[9].color = 'red'   # 45-47X_AF
    TRV.LINKS[13].color = 'red'  # NS_AF
    TRV.LINKS[14].color = 'red'  # NS Yard_AF
    TRV.LINKS[17].color = 'red'  # 0_0_AF
    TRV.LINKS[18].color = 'red'  # 0_1_AF
    TRV.LINKS[19].color = 'red'  # 0_2_AF
    TRV.LINKS[20].color = 'red'  # 0_3_AF
    TRV.LINKS[21].color = 'red'  # 0_4_AF
    TRV.LINKS[22].color = 'red'  # 0_5_AF
    TRV.LINKS[23].color = 'red'  # 0_6_AF
    TRV.LINKS[28].color = 'red'  # 1_4_AF
    TRV.LINKS[29].color = 'red'  # 1_5_AF
    TRV.LINKS[30].color = 'red'  # 1_6_AF
    TRV.LINKS[31].color = 'red'  # 1_7_AF
    TRV.LINKS[37].color = 'red'  # 2_5_AF

    TRV.NODES[6].color = 'red'   # Ex Main 1_AF
    TRV.NODES[7].color = 'red'   # NS_org_AF
    TRV.NODES[8].color = 'red'   # NS_Yard_AF
    TRV.NODES[15].color = 'red'  # 7_S_AF
    TRV.NODES[16].color = 'red'  # 9_S_AF
    TRV.NODES[17].color = 'red'  # 11_S_AF
    TRV.NODES[18].color = 'red'  # 13_S_AF
    TRV.NODES[19].color = 'red'  # 19_S_AF
    TRV.NODES[23].color = 'red'  # 27_S_AF
    TRV.NODES[25].color = 'red'  # 31_S_AF
    TRV.NODES[26].color = 'red'  # 33_S_AF
    TRV.NODES[27].color = 'red'  # 35_S_AF
    TRV.NODES[22].color = 'red'  # 25_S_AF
    TRV.NODES[24].color = 'red'  # 29_S_AF
    TRV.NODES[28].color = 'red'  # 37_S_AF
    TRV.NODES[29].color = 'red'  # 39_S_AF
    TRV.NODES[32].color = 'red'  # 45_S_AF
    TRV.NODES[33].color = 'red'  # 47_S_AF
    TRV.NODES[34].color = 'red'  # Main 0_AF
    TRV.NODES[35].color = 'red'  # Main 1_AF
    TRV.NODES[36].color = 'red'  # Main 2_AF

elif AFSlatersMain0Closed and AFSlatersMain1Closed and AFSlatersMain3Closed:
    # Example of closing main 0/1/3
    TRV.LINKS[7].color = 'red'   # 37-39X_AF
    TRV.LINKS[8].color = 'red'   # 41-43X_AF
    TRV.LINKS[10].color = 'red'  # yard1_AF
    TRV.LINKS[11].color = 'red'  # y1_2_AF
    TRV.LINKS[22].color = 'red'  # 0_5_AF
    TRV.LINKS[23].color = 'red'  # 0_6_AF
    TRV.LINKS[31].color = 'red'  # 1_7_AF
    TRV.LINKS[40].color = 'red'  # 3_2_AF
    TRV.LINKS[41].color = 'red'  # 3_3_AF
    TRV.LINKS[42].color = 'red'  # 3_4_AF

    TRV.NODES[0].color = 'red'   # NS Horn Track 1_AF
    TRV.NODES[1].color = 'red'   # y1e_AF
    TRV.NODES[14].color = 'red'  # 6_S_AF
    TRV.NODES[29].color = 'red'  # 39_S_AF
    TRV.NODES[31].color = 'red'  # 43_S_AF
    TRV.NODES[34].color = 'red'  # main0_dest_AF
    TRV.NODES[35].color = 'red'  # Main1_dest_AF
    TRV.NODES[37].color = 'red'  # main3_dest_AF

elif AFSlatersMain0Closed and AFSlatersMain2Closed and AFSlatersMain3Closed:
    # Example of closing main 0/2/3
    TRV.LINKS[4].color = 'red'   # 13-19X_AF
    TRV.LINKS[7].color = 'red'   # 37-39X_AF
    TRV.LINKS[8].color = 'red'   # 41-43X_AF
    TRV.LINKS[9].color = 'red'   # 45-47X_AF
    TRV.LINKS[10].color = 'red'  # yard1_AF
    TRV.LINKS[11].color = 'red'  # y1_2_AF
    TRV.LINKS[22].color = 'red'  # 0_5_AF
    TRV.LINKS[23].color = 'red'  # 0_6_AF
    TRV.LINKS[34].color = 'red'  # 2_2_AF
    TRV.LINKS[35].color = 'red'  # 2_4_AF
    TRV.LINKS[36].color = 'red'  # 2_5_AF
    TRV.LINKS[37].color = 'red'  # 2_6_AF
    TRV.LINKS[40].color = 'red'  # 3_2_AF
    TRV.LINKS[41].color = 'red'  # 3_3_AF

    TRV.NODES[0].color = 'red'   # NS Horn Track 1_AF
    TRV.NODES[1].color = 'red'   # y1e_AF
    TRV.NODES[14].color = 'red'  # 6_S_AF
    TRV.NODES[21].color = 'red'  # 23_S_AF
    TRV.NODES[29].color = 'red'  # 39_S_AF
    TRV.NODES[30].color = 'red'  # 41_S_AF
    TRV.NODES[31].color = 'red'  # 43_S_AF
    TRV.NODES[33].color = 'red'  # 47_S_AF
    TRV.NODES[34].color = 'red'  # main0_dest_AF
    TRV.NODES[36].color = 'red'  # main2_dest_AF
    TRV.NODES[37].color = 'red'  # main3_dest_AF

elif AFSlatersMain1Closed and AFSlatersMain2Closed and AFSlatersMain3Closed:
    # Example of closing main 1/2/3
    TRV.LINKS[4].color = 'red'   # 21-23X_AF
    TRV.LINKS[6].color = 'red'   # 31-33X_AF
    TRV.LINKS[7].color = 'red'   # 37-39X_AF
    TRV.LINKS[8].color = 'red'   # 41-43X_AF
    TRV.LINKS[9].color = 'red'   # 45-47X_AF
    TRV.LINKS[10].color = 'red'  # yard1_AF
    TRV.LINKS[11].color = 'red'  # y1_2_AF
    TRV.LINKS[28].color = 'red'  # 1_4_AF
    TRV.LINKS[29].color = 'red'  # 1_5_AF
    TRV.LINKS[30].color = 'red'  # 1_6_AF
    TRV.LINKS[31].color = 'red'  # 1_7_AF
    TRV.LINKS[34].color = 'red'  # 2_2_AF
    TRV.LINKS[35].color = 'red'  # 2_4_AF
    TRV.LINKS[36].color = 'red'  # 2_5_AF
    TRV.LINKS[37].color = 'red'  # 2_6_AF
    TRV.LINKS[40].color = 'red'  # 3_2_AF
    TRV.LINKS[41].color = 'red'  # 3_3_AF
    TRV.LINKS[42].color = 'red'  # 3_4_AF

    TRV.NODES[0].color = 'red'   # NS Horn Track 1_AF
    TRV.NODES[1].color = 'red'   # y1e_AF
    TRV.NODES[14].color = 'red'  # 6_S_AF
    TRV.NODES[21].color = 'red'  # 23_S_AF
    TRV.NODES[26].color = 'red'  # 33_S_AF
    TRV.NODES[28].color = 'red'  # 37_S_AF
    TRV.NODES[30].color = 'red'  # 41_S_AF
    TRV.NODES[31].color = 'red'  # 43_S_AF
    TRV.NODES[32].color = 'red'  # 45_S_AF
    TRV.NODES[33].color = 'red'  # 47_S_AF
    TRV.NODES[35].color = 'red'  # Main1_dest_AF
    TRV.NODES[36].color = 'red'  # main2_dest_AF
    TRV.NODES[37].color = 'red'  # main3_dest_AF

# 6 combos of 2 tracks closed
elif AFSlatersMain0Closed and AFSlatersMain1Closed:
    # Example of closing main 0/1
    TRV.LINKS[7].color = 'red'   # 37-39X_AF
    TRV.LINKS[22].color = 'red'  # 0_5_AF
    TRV.LINKS[23].color = 'red'  # 0_6_AF
    TRV.LINKS[31].color = 'red'  # 1_7_AF

    TRV.NODES[29].color = 'red'  # 39_S_AF
    TRV.NODES[34].color = 'red'  # main0_dest_AF
    TRV.NODES[35].color = 'red'  # Main1_dest_AF

elif AFSlatersMain0Closed and AFSlatersMain2Closed:
    # Example of closing main 0/2
    TRV.LINKS[7].color = 'red'  # 37-39X_AF
    TRV.LINKS[9].color = 'red'  # 45-47X_AF
    TRV.LINKS[22].color = 'red'  # 0_5_AF
    TRV.LINKS[23].color = 'red'  # 0_6_AF
    TRV.LINKS[36].color = 'red'  # 2_5_AF
    TRV.LINKS[37].color = 'red'  # 2_6_AF

    TRV.NODES[29].color = 'red'  # 39_S_AF
    TRV.NODES[33].color = 'red'  # 47_S_AF
    TRV.NODES[34].color = 'red'  # main0_dest_AF
    TRV.NODES[36].color = 'red'  # main2_dest_AF

elif AFSlatersMain0Closed and AFSlatersMain3Closed:
    # Example of closing main 0/3
    TRV.LINKS[7].color = 'red'  # 37-39X_AF
    TRV.LINKS[8].color = 'red'  # 41-43X_AF
    TRV.LINKS[22].color = 'red'  # 0_5_AF
    TRV.LINKS[23].color = 'red'  # 0_6_AF
    TRV.LINKS[41].color = 'red'  # 3_3_AF
    TRV.LINKS[42].color = 'red'  # 3_4_AF

    TRV.NODES[29].color = 'red'  # 39_S_AF
    TRV.NODES[31].color = 'red'  # 43_S_AF
    TRV.NODES[34].color = 'red'  # main0_dest_AF
    TRV.NODES[37].color = 'red'  # main3_dest_AF

elif AFSlatersMain1Closed and AFSlatersMain2Closed:
    # Example of closing main 1/2
    TRV.LINKS[6].color = 'red'  # 31-33X_AF
    TRV.LINKS[9].color = 'red'  # 45-47X_AF
    TRV.LINKS[30].color = 'red'  # 1_6_AF
    TRV.LINKS[31].color = 'red'  # 1_7_AF
    TRV.LINKS[36].color = 'red'  # 2_5_AF
    TRV.LINKS[37].color = 'red'  # 2_6_AF

    TRV.NODES[32].color = 'red'  # 45_S_AF
    TRV.NODES[33].color = 'red'  # 47_S_AF
    TRV.NODES[35].color = 'red'  # Main1_dest_AF
    TRV.NODES[36].color = 'red'  # main2_dest_AF

elif AFSlatersMain2Closed and AFSlatersMain3Closed:
    TRV.LINKS[4].color = 'red'   # 21-23X_AF
    TRV.LINKS[8].color = 'red'   # 41-43X_AF
    TRV.LINKS[9].color = 'red'   # 45-47X_AF
    TRV.LINKS[10].color = 'red'  # yard1_AF
    TRV.LINKS[11].color = 'red'  # y1_2_AF
    TRV.LINKS[34].color = 'red'  # 2_2_AF
    TRV.LINKS[35].color = 'red'  # 2_3_AF
    TRV.LINKS[36].color = 'red'  # 2_4_AF
    TRV.LINKS[37].color = 'red'  # 2_5_AF
    TRV.LINKS[40].color = 'red'  # 3_2_AF
    TRV.LINKS[41].color = 'red'  # 3_3_AF
    TRV.LINKS[42].color = 'red'  # 3_4_AF

    TRV.NODES[0].color = 'red'   # NS Horn Track 1_AF
    TRV.NODES[1].color = 'red'   # y1e_AF
    TRV.NODES[14].color = 'red'  # 6_S_AF
    TRV.NODES[21].color = 'red'  # 23_S_AF
    TRV.NODES[30].color = 'red'  # 41_S_AF
    TRV.NODES[31].color = 'red'  # 43_S_AF
    TRV.NODES[33].color = 'red'  # 47_S_AF
    TRV.NODES[37].color = 'red'  # Main 3_AF
    TRV.NODES[36].color = 'red'  # Main 2_AF

elif AFSlatersMain1Closed and AFSlatersMain3Closed:
    # Example of closing main 1/3
    TRV.LINKS[8].color = 'red'   # 41-43X_AF
    TRV.LINKS[10].color = 'red'  # yard1_AF
    TRV.LINKS[11].color = 'red'  # y1_2_AF
    TRV.LINKS[31].color = 'red'  # 1_7_AF
    TRV.LINKS[40].color = 'red'  # 3_2_AF
    TRV.LINKS[41].color = 'red'  # 3_3_AF
    TRV.LINKS[42].color = 'red'  # 3_4_AF

    TRV.NODES[0].color = 'red'   # NS Horn Track 1_AF
    TRV.NODES[1].color = 'red'   # y1e_AF
    TRV.NODES[14].color = 'red'  # 6_S_AF
    TRV.NODES[31].color = 'red'  # 43_S_AF
    TRV.NODES[35].color = 'red'  # Main1_dest_AF
    TRV.NODES[37].color = 'red'  # main3_dest_AF

# 4 versions of 1 track closed (0,0,0,0 is 16th possible combo and not included since it's the default state)
elif AFSlatersMain3Closed:
    TRV.LINKS[8].color = 'red'   # 41-43X_AF
    TRV.LINKS[10].color = 'red'  # yard1_AF
    TRV.LINKS[11].color = 'red'  # y1_2_AF
    TRV.LINKS[40].color = 'red'  # 3_2_AF
    TRV.LINKS[41].color = 'red'  # 3_3_AF
    TRV.LINKS[42].color = 'red'  # 3_4_AF

    TRV.NODES[0].color = 'red'   # NS Horn Track 1_AF
    TRV.NODES[1].color = 'red'   # y1e_AF
    TRV.NODES[14].color = 'red'  # 6_S_AF
    TRV.NODES[31].color = 'red'  # 43_S_AF
    TRV.NODES[37].color = 'red'  # Main 3_AF

elif AFSlatersMain2Closed:
    TRV.LINKS[36].color = 'red'  # Main 2_AF
    TRV.LINKS[37].color = 'red'  # Main 3_AF
    TRV.LINKS[9].color = 'red'   # 45-47X_AF

    TRV.NODES[33].color = 'red'  # 47_S_AF
    TRV.NODES[36].color = 'red'  # Main 2_AF

elif AFSlatersMain1Closed:
    TRV.LINKS[31].color = 'red'  # 1_7_AF

    TRV.NODES[35].color = 'red'  # 2_3_AF

elif AFSlatersMain0Closed:
    TRV.LINKS[7].color = 'red'   # 37-39X_AF
    TRV.LINKS[22].color = 'red'  # 0_5_AF
    TRV.LINKS[23].color = 'red'  # 0_6_AF

    TRV.NODES[28].color = 'red'  # 1_4_AF
    TRV.NODES[29].color = 'red'  # 1_5_AF
    TRV.NODES[34].color = 'red'  # 2_2_AF

# Determine if the Routes are open or closed on either side of the interlocking
AF_signals_low = {
    # Origin Values (color, position)
    'NS_Yard': (TRV.LINKS[14].color, (85, 14.75), 'yard'),
    'Main 1': (TRV.LINKS[17].color, (85, 12.75), TRV.LINKS[23].color),
    'Main 2': (TRV.LINKS[24].color, (85, 10.75), TRV.LINKS[31].color),
    'Main 3': (TRV.LINKS[32].color, (85, 8.75), TRV.LINKS[37].color),
    'NS Horn Track 3': (TRV.LINKS[38].color, (85, 6.75), TRV.LINKS[41].color),
    'NS Horn Track 2': (TRV.LINKS[12].color, (85, 4.5), 'yard'),
    'NS Horn Track 1': (TRV.LINKS[10].color, (85, 2), 'yard')
}

AF_signals_low_high = {
    # Destinations
    'Setoff Track': (TRV.LINKS[16].color, (63, 12.75), 'yard'),
    'Main 0': (TRV.LINKS[23].color, (63, 10.75), TRV.LINKS[17].color),
    'Main 1': (TRV.LINKS[31].color, (63, 8.75), TRV.LINKS[24].color),
    'Main 2': (TRV.LINKS[37].color, (63, 6.75), TRV.LINKS[32].color),
    'Main 3': (TRV.LINKS[41].color, (63, 4.75), TRV.LINKS[38].color)

}

TRV.signal_attributes_low.update(AF_signals_low)
TRV.signal_attributes_high.update(AF_signals_low_high)




TRV.title = "←L'Enfant                        RO (CFP 110.1/Sta. 325+00)                                      Slater's Lane (CFP 106.3/Sta. 130+00)                                                  AF (CFP 104.3/Sta. 25+00)                    Franconia→"

# Define Interlocking breaks
TRV.breaks.append(2)
TRV.breaks.append(24)
TRV.breaks.append(34)
TRV.breaks.append(57)
TRV.breaks.append(63)
TRV.breaks.append(88.5)


st.pyplot(TRV.show_network(figsize=(60, 90)))
