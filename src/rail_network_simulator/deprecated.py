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
    pre_AF_yard1_disabled = st.checkbox("Yard 1 Outage", key='pre_AF_yard1_disabled')
    pre_AF_yard2_disabled = st.checkbox("Yard 2 Outage", key='pre_AF_yard2_disabled')
    pre_AF_yard3_disabled = st.checkbox("Yard 3 Outage", key='pre_AF_yard3_disabled')
    pre_AF_main3_disabled = st.checkbox("Main 3 Outage", key='pre_AF_main3_disabled')
    pre_AF_main2_disabled = st.checkbox("Main 2 Outage", key='pre_AF_main2_disabled')
    pre_AF_main1_disabled = st.checkbox("Main 1 Outage", key='pre_AF_main1_disabled')
    pre_AF_ns_disabled = st.checkbox("NS Outage",     key='pre_AF_ns_disabled')


# ================================= Signal Controls - RO ===========================================================

if Main2AfterRO & Main3AfterRO:
    for link in TRV.LINKS:
        link.color = 'red'
    for node in TRV.NODES:
        node.color = 'red'

if Main2AfterRO:
    TRV.LINKS[0].color = 'red'     # Existing 2
    TRV.LINKS[1].color = 'red'     # 0_1_RO
    TRV.LINKS[14].color = 'red'    # 1-3_RO

    TRV.NODES[4].color = 'red'     # Existing 2
    TRV.NODES[8].color = 'red'     # 1_S_RO

elif Main3AfterRO:
    TRV.LINKS[3].color = 'red'   # Ex 3_RO
    TRV.LINKS[4].color = 'red'   # 1_1_RO
    TRV.LINKS[8].color = 'red'   # 9_S_RO
    TRV.LINKS[9].color = 'red'   # 2_1_RO
    TRV.LINKS[10].color = 'red'  # 2_2_RO
    TRV.LINKS[12].color = 'red'  # 15_S_RO
    TRV.LINKS[13].color = 'red'  # Main 3_RO

    TRV.NODES[5].color = 'red'   # Existing 3
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
    TRV.LINKS[0+17].color = 'red'   # Pepco Lead
    TRV.LINKS[1+17].color = 'red'   # 3_S
    TRV.LINKS[2+17].color = 'red'   # 0_0
    TRV.LINKS[3+17].color = 'red'   # 0_1
    TRV.LINKS[4+17].color = 'red'   # 0_2
    TRV.LINKS[6+17].color = 'red'   # 1_0
    TRV.LINKS[7+17].color = 'red'   # 1_1
    TRV.LINKS[8+17].color = 'red'   # 1_2
    TRV.LINKS[17+17].color = 'red'  # 13_15X
    TRV.LINKS[19+17].color = 'red'  # 9_11X
    TRV.LINKS[20+17].color = 'red'  # 17_19X

    TRV.NODES[4+16].color = 'red'   # OOS_NS
    TRV.NODES[5+16].color = 'red'  # Slaters-AF Main 0
    TRV.NODES[6+16].color = 'red'  # Slaters-AF Main 1
    TRV.NODES[9+16].color = 'red'   # NS_OOS
    TRV.NODES[10+16].color = 'red'  # 3_S
    TRV.NODES[14+16].color = 'red'  # 11_S
    TRV.NODES[15+16].color = 'red'  # 13_S
    TRV.NODES[16+16].color = 'red'  # 15_S
    TRV.NODES[17+16].color = 'red'  # 17_S
    TRV.NODES[18+16].color = 'red'  # 18_S

elif SlatersROMain0Closed & SlatersROMain2Closed:
    # Comment to collapse in IDE
    TRV.LINKS[17+17].color = 'red'  # 13_15X

elif SlatersROMain0Closed & SlatersROMain3Closed:
    TRV.NODES[20+16].color = 'red'  # 23_S

    TRV.LINKS[17+17].color = 'red'  # 13_15X
    TRV.LINKS[21+17].color = 'red'  # 21_23X
    TRV.LINKS[15+17].color = 'red'  # 3_1

elif SlatersROMain1Closed & SlatersROMain2Closed:
    TRV.LINKS[7+17].color = 'red'  # 1_1
    TRV.LINKS[8+17].color = 'red'  # 1_2
    TRV.LINKS[18+17].color = 'red'  # 5_7X
    TRV.LINKS[19+17].color = 'red'  # 9_11X
    TRV.LINKS[20+17].color = 'red'  # 17_19X

    TRV.NODES[14+16].color = 'red'  # 11_S
    TRV.NODES[18+16].color = 'red'  # 19_S

elif SlatersROMain1Closed & SlatersROMain3Closed:
    TRV.LINKS[7+17].color = 'red'  # 1_2
    TRV.LINKS[8+17].color = 'red'  # 1_1
    TRV.LINKS[19+17].color = 'red'  # 9_11X
    TRV.LINKS[20+17].color = 'red'  # 17_19X
    TRV.LINKS[21+17].color = 'red'  # 21_23X
    TRV.LINKS[15+17].color = 'red'  # 3_1

    TRV.NODES[14+16].color = 'red'  # 11_S
    TRV.NODES[18+16].color = 'red'  # 19_S
    TRV.NODES[20+16].color = 'red'  # 23_S


elif SlatersROMain2Closed & SlatersROMain3Closed:
    TRV.NODES[19+16].color = 'red'  # 21_S
    TRV.NODES[20+16].color = 'red'  # 23_S

    TRV.LINKS[12+17].color = 'red'  # 2_2
    TRV.LINKS[15+17].color = 'red'  # 3_1
    TRV.LINKS[21+17].color = 'red'  # 21_23X

elif SlatersROMain0Closed & AFSlatersMain0Closed:
    TRV.LINKS[0+17].color = 'red'  # Pepco Lead
    TRV.LINKS[1+17].color = 'red'  # 3_S
    TRV.LINKS[3+17].color = 'red'  # 0_1
    TRV.LINKS[4+17].color = 'red'  # 0_2
    TRV.LINKS[20+17].color = 'red'  # 17_19X
    TRV.LINKS[17+17].color = 'red'  # 13_15X

    TRV.NODES[10+16].color = 'red'  # 3_S
    TRV.NODES[16+16].color = 'red'  # 15_S
    TRV.NODES[17+16].color = 'red'  # 17_S
    TRV.NODES[4+16].color = 'red'  # OOS_NS
    TRV.NODES[9+16].color = 'red'  # NS_OOS

elif SlatersROMain0Closed & AFSlatersMain1Closed:
    TRV.LINKS[7+17].color = 'red'  # 1_1
    TRV.LINKS[17+17].color = 'red'  # 13_15X

    TRV.NODES[15+16].color = 'red'  # 13_S

# AF/Slaters Closed
elif AFSlatersMain0Closed & AFSlatersMain1Closed:
    TRV.LINKS[0+17].color = 'red'  # Pepco Lead
    TRV.LINKS[1+17].color = 'red'  # 3_S
    TRV.LINKS[3+17].color = 'red'  # 0_1
    TRV.LINKS[4+17].color = 'red'  # 0_2
    TRV.LINKS[5+17].color = 'red'  # 0_3
    TRV.LINKS[7+17].color = 'red'  # 1_1X
    TRV.LINKS[17+17].color = 'red'  # 13_15X
    TRV.LINKS[20+17].color = 'red'  # 17_19X

    TRV.NODES[0+16].color = 'red'  # RO-Slaters Main 0
    TRV.NODES[4+16].color = 'red'  # OOS_NS
    TRV.NODES[9+16].color = 'red'  # NS_OOS
    TRV.NODES[10+16].color = 'red'  # 3_S
    TRV.NODES[15+16].color = 'red'  # 13_S
    TRV.NODES[16+16].color = 'red'  # 15_S
    TRV.NODES[17+16].color = 'red'  # 17_S

elif AFSlatersMain0Closed & AFSlatersMain2Closed:
    TRV.LINKS[3+17].color = 'red'  # 0_1
    TRV.LINKS[20+17].color = 'red'  # 17_19X

    TRV.NODES[10+16].color = 'red'  # 3_S
    TRV.NODES[17+16].color = 'red'  # 17_S

elif AFSlatersMain0Closed & AFSlatersMain3Closed:
    TRV.LINKS[3+17].color = 'red'  # 0_1
    TRV.LINKS[15+17].color = 'red'  # 3_1
    TRV.LINKS[18+17].color = 'red'  # 5_7X
    TRV.LINKS[20+17].color = 'red'  # 17_19X

    TRV.NODES[10+16].color = 'red'  # 3_S
    TRV.NODES[11+16].color = 'red'  # 5_S
    TRV.NODES[17+16].color = 'red'  # 17_S

elif AFSlatersMain1Closed & AFSlatersMain2Closed:
    TRV.LINKS[7+17].color = 'red'  # 1_1
    TRV.LINKS[17+17].color = 'red'  # 13_15X

    TRV.NODES[15+16].color = 'red'  # 13_S

elif AFSlatersMain1Closed & AFSlatersMain3Closed:
    TRV.LINKS[7+17].color = 'red'  # 1_1
    TRV.LINKS[15+17].color = 'red'  # 3_1
    TRV.LINKS[17+17].color = 'red'  # 13_15X
    TRV.LINKS[18+17].color = 'red'  # 5_7X

    TRV.NODES[11+16].color = 'red'  # 5_S
    TRV.NODES[15+16].color = 'red'  # 13_S

elif AFSlatersMain2Closed & AFSlatersMain3Closed:
    TRV.LINKS[11+17].color = 'red'  # 2_1
    TRV.LINKS[12+17].color = 'red'  # 2_2
    TRV.LINKS[13+17].color = 'red'  # 2_3
    TRV.LINKS[15+17].color = 'red'  # 3_1
    TRV.LINKS[16+17].color = 'red'  # 3_2
    TRV.LINKS[18+17].color = 'red'  # 5_7X
    TRV.LINKS[19+17].color = 'red'  # 9_11X
    TRV.LINKS[21+17].color = 'red'  # 21_23X

    TRV.NODES[2+16].color = 'red'  # RO-Slaters Main 2
    TRV.NODES[3+16].color = 'red'  # RO-Slaters Main 3
    TRV.NODES[11+16].color = 'red'  # 5_S
    TRV.NODES[12+16].color = 'red'  # 7_S
    TRV.NODES[13+16].color = 'red'  # 9_S
    TRV.NODES[19+16].color = 'red'  # 21_S
    TRV.NODES[20+16].color = 'red'  # 23_S

elif AFSlatersMain1Closed & SlatersROMain1Closed:
    TRV.LINKS[7+17].color = 'red'  # 1_1
    TRV.LINKS[8+17].color = 'red'  # 1_2
    TRV.LINKS[17+17].color = 'red'  # 13_15X
    TRV.LINKS[19+17].color = 'red'  # 9_11X
    TRV.LINKS[20+17].color = 'red'  # 17_19X

    TRV.NODES[14+16].color = 'red'  # 11_S
    TRV.NODES[18+16].color = 'red'  # 19_S
    TRV.NODES[15+16].color = 'red'  # 13_S

elif AFSlatersMain2Closed & SlatersROMain2Closed:
    TRV.LINKS[11+17].color = 'red'  # 2_1
    TRV.LINKS[12+17].color = 'red'  # 2_2
    TRV.LINKS[18+17].color = 'red'  # 5_7X
    TRV.LINKS[19+17].color = 'red'  # 9_11X
    TRV.LINKS[21+17].color = 'red'  # 21_23X

    TRV.NODES[12+16].color = 'red'  # 7_S
    TRV.NODES[13+16].color = 'red'  # 9_S
    TRV.NODES[19+16].color = 'red'  # 21_S

elif AFSlatersMain3Closed & SlatersROMain3Closed:
    TRV.LINKS[15+17].color = 'red'  # 3_1
    TRV.LINKS[18+17].color = 'red'  # 5_7X
    TRV.LINKS[21+17].color = 'red'  # 21_23X

    TRV.NODES[11+16].color = 'red'  # 5_S
    TRV.NODES[20+16].color = 'red'  # 23_S

# 1 track of RO-Slaters Closed
elif SlatersROMain0Closed and not (AFSlatersMain2Closed or AFSlatersMain3Closed):
    # Comment to make the statement collapsible in IDE
    TRV.LINKS[17+17].color = 'red'  # 13_15X

elif SlatersROMain1Closed:
    TRV.LINKS[7+17].color = 'red'  # 1_2
    TRV.LINKS[8+17].color = 'red'  # 1_1
    TRV.LINKS[19+17].color = 'red'  # 9_11X
    TRV.LINKS[20+17].color = 'red'  # 17_19X

    TRV.NODES[14+16].color = 'red'  # 11_S
    TRV.NODES[18+16].color = 'red'  # 19_S

elif SlatersROMain2Closed:
    # Handled by the associated track segment logic alone
    pass

elif SlatersROMain3Closed:
    TRV.NODES[20+16].color = 'red'  # 23_S
    TRV.LINKS[21+17].color = 'red'  # 21_23X
    TRV.LINKS[15+17].color = 'red'  # 3_1


# 1 Track of AF - SlatersMain closed
elif AFSlatersMain0Closed:
    TRV.LINKS[3+17].color = 'red'  # 0_1
    TRV.NODES[10+16].color = 'red'  # 3_S

elif AFSlatersMain1Closed:
    TRV.LINKS[7+17].color = 'red'  # 1_1X
    TRV.LINKS[17+17].color = 'red'  # 13_15X

    TRV.NODES[15+16].color = 'red'  # 13_S

elif AFSlatersMain2Closed:
    # Handled by the associated track segment logic alone
    pass

elif AFSlatersMain3Closed:
    TRV.LINKS[15+17].color = 'red'  # 3_1
    TRV.LINKS[18+17].color = 'red'  # 5_7X

    TRV.NODES[11+16].color = 'red'  # 5_S

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
    TRV.LINKS[40].color = 'red'   # 25-29X_AF
    TRV.LINKS[41].color = 'red'   # 9-11X_AF
    TRV.LINKS[42].color = 'red'   # 13-19X_AF
    TRV.LINKS[44].color = 'red'   # 25-29X_AF
    TRV.LINKS[45].color = 'red'   # 31-33X_AF
    TRV.LINKS[46].color = 'red'   # 37-39X_AF
    TRV.LINKS[48].color = 'red'   # 45-47X_AF
    TRV.LINKS[52].color = 'red'  # NS_AF
    TRV.LINKS[14+39].color = 'red'  # NS Yard_AF
    TRV.LINKS[17+39].color = 'red'  # 0_0_AF
    TRV.LINKS[18+39].color = 'red'  # 0_1_AF
    TRV.LINKS[19+39].color = 'red'  # 0_2_AF
    TRV.LINKS[20+39].color = 'red'  # 0_3_AF
    TRV.LINKS[21+39].color = 'red'  # 0_4_AF
    TRV.LINKS[22+39].color = 'red'  # 0_5_AF
    TRV.LINKS[23+39].color = 'red'  # 0_6_AF
    TRV.LINKS[28+39].color = 'red'  # 1_4_AF
    TRV.LINKS[29+39].color = 'red'  # 1_5_AF
    TRV.LINKS[30+39].color = 'red'  # 1_6_AF
    TRV.LINKS[31+39].color = 'red'  # 1_7_AF
    TRV.LINKS[37+39].color = 'red'  # 2_5_AF

    TRV.NODES[6+37].color = 'red'   # Ex Main 1
    TRV.NODES[7+37].color = 'red'   # NS_org_AF
    TRV.NODES[8+37].color = 'red'   # NS_Yard
    TRV.NODES[15+37].color = 'red'  # 7_S_AF
    TRV.NODES[16+37].color = 'red'  # 9_S_AF
    TRV.NODES[17+37].color = 'red'  # 11_S_AF
    TRV.NODES[18+37].color = 'red'  # 13_S_AF
    TRV.NODES[19+37].color = 'red'  # 19_S_AF
    TRV.NODES[23+37].color = 'red'  # 27_S_AF
    TRV.NODES[25+37].color = 'red'  # 31_S_AF
    TRV.NODES[26+37].color = 'red'  # 33_S_AF
    TRV.NODES[27+37].color = 'red'  # 35_S_AF
    TRV.NODES[22+37].color = 'red'  # 25_S_AF
    TRV.NODES[24+37].color = 'red'  # 29_S_AF
    TRV.NODES[28+37].color = 'red'  # 37_S_AF
    TRV.NODES[29+37].color = 'red'  # 39_S_AF
    TRV.NODES[32+37].color = 'red'  # 45_S_AF
    TRV.NODES[33+37].color = 'red'  # 47_S_AF
    TRV.NODES[34+37].color = 'red'  # Main 0_AF
    TRV.NODES[35+37].color = 'red'  # Main 1_AF
    TRV.NODES[36+37].color = 'red'  # Main 2_AF

elif AFSlatersMain0Closed and AFSlatersMain1Closed and AFSlatersMain3Closed:
    # Example of closing main 0/1/3
    TRV.LINKS[7+39].color = 'red'   # 37-39X_AF
    TRV.LINKS[8+39].color = 'red'   # 41-43X_AF
    TRV.LINKS[10+39].color = 'red'  # yard1_AF
    TRV.LINKS[11+39].color = 'red'  # y1_2_AF
    TRV.LINKS[22+39].color = 'red'  # 0_5_AF
    TRV.LINKS[23+39].color = 'red'  # 0_6_AF
    TRV.LINKS[31+39].color = 'red'  # 1_7_AF
    TRV.LINKS[40+39].color = 'red'  # 3_2_AF
    TRV.LINKS[41+39].color = 'red'  # 3_3_AF
    TRV.LINKS[42+39].color = 'red'  # 3_4_AF

    TRV.NODES[0+37].color = 'red'   # NS Horn Track 1
    TRV.NODES[1+37].color = 'red'   # y1e_AF
    TRV.NODES[14+37].color = 'red'  # 6_S_AF
    TRV.NODES[29+37].color = 'red'  # 39_S_AF
    TRV.NODES[31+37].color = 'red'  # 43_S_AF
    TRV.NODES[34+37].color = 'red'  # main0_dest_AF
    TRV.NODES[35+37].color = 'red'  # Main1_dest_AF
    TRV.NODES[37+37].color = 'red'  # main3_dest_AF

elif AFSlatersMain0Closed and AFSlatersMain2Closed and AFSlatersMain3Closed:
    # Example of closing main 0/2/3
    TRV.LINKS[4+39].color = 'red'   # 13-19X_AF
    TRV.LINKS[7+39].color = 'red'   # 37-39X_AF
    TRV.LINKS[8+39].color = 'red'   # 41-43X_AF
    TRV.LINKS[9+39].color = 'red'   # 45-47X_AF
    TRV.LINKS[10+39].color = 'red'  # yard1_AF
    TRV.LINKS[11+39].color = 'red'  # y1_2_AF
    TRV.LINKS[22+39].color = 'red'  # 0_5_AF
    TRV.LINKS[23+39].color = 'red'  # 0_6_AF
    TRV.LINKS[34+39].color = 'red'  # 2_2_AF
    TRV.LINKS[35+39].color = 'red'  # 2_4_AF
    TRV.LINKS[36+39].color = 'red'  # 2_5_AF
    TRV.LINKS[37+39].color = 'red'  # 2_6_AF
    TRV.LINKS[40+39].color = 'red'  # 3_2_AF
    TRV.LINKS[41+39].color = 'red'  # 3_3_AF

    TRV.NODES[0+37].color = 'red'   # NS Horn Track 1
    TRV.NODES[1+37].color = 'red'   # y1e_AF
    TRV.NODES[14+37].color = 'red'  # 6_S_AF
    TRV.NODES[21+37].color = 'red'  # 23_S_AF
    TRV.NODES[29+37].color = 'red'  # 39_S_AF
    TRV.NODES[30+37].color = 'red'  # 41_S_AF
    TRV.NODES[31+37].color = 'red'  # 43_S_AF
    TRV.NODES[33+37].color = 'red'  # 47_S_AF
    TRV.NODES[34+37].color = 'red'  # main0_dest_AF
    TRV.NODES[36+37].color = 'red'  # main2_dest_AF
    TRV.NODES[37+37].color = 'red'  # main3_dest_AF

elif AFSlatersMain1Closed and AFSlatersMain2Closed and AFSlatersMain3Closed:
    # Example of closing main 1/2/3
    TRV.LINKS[4+39].color = 'red'   # 21-23X_AF
    TRV.LINKS[6+39].color = 'red'   # 31-33X_AF
    TRV.LINKS[7+39].color = 'red'   # 37-39X_AF
    TRV.LINKS[8+39].color = 'red'   # 41-43X_AF
    TRV.LINKS[9+39].color = 'red'   # 45-47X_AF
    TRV.LINKS[10+39].color = 'red'  # yard1_AF
    TRV.LINKS[11+39].color = 'red'  # y1_2_AF
    TRV.LINKS[28+39].color = 'red'  # 1_4_AF
    TRV.LINKS[29+39].color = 'red'  # 1_5_AF
    TRV.LINKS[30+39].color = 'red'  # 1_6_AF
    TRV.LINKS[31+39].color = 'red'  # 1_7_AF
    TRV.LINKS[34+39].color = 'red'  # 2_2_AF
    TRV.LINKS[35+39].color = 'red'  # 2_4_AF
    TRV.LINKS[36+39].color = 'red'  # 2_5_AF
    TRV.LINKS[37+39].color = 'red'  # 2_6_AF
    TRV.LINKS[40+39].color = 'red'  # 3_2_AF
    TRV.LINKS[41+39].color = 'red'  # 3_3_AF
    TRV.LINKS[42+39].color = 'red'  # 3_4_AF

    TRV.NODES[0+37].color = 'red'   # NS Horn Track 1
    TRV.NODES[1+37].color = 'red'   # y1e_AF
    TRV.NODES[14+37].color = 'red'  # 6_S_AF
    TRV.NODES[21+37].color = 'red'  # 23_S_AF
    TRV.NODES[26+37].color = 'red'  # 33_S_AF
    TRV.NODES[28+37].color = 'red'  # 37_S_AF
    TRV.NODES[30+37].color = 'red'  # 41_S_AF
    TRV.NODES[31+37].color = 'red'  # 43_S_AF
    TRV.NODES[32+37].color = 'red'  # 45_S_AF
    TRV.NODES[33+37].color = 'red'  # 47_S_AF
    TRV.NODES[35+37].color = 'red'  # Main1_dest_AF
    TRV.NODES[36+37].color = 'red'  # main2_dest_AF
    TRV.NODES[37+37].color = 'red'  # main3_dest_AF

# 6 combos of 2 tracks closed
elif AFSlatersMain0Closed and AFSlatersMain1Closed:
    # Example of closing main 0/1
    TRV.LINKS[7+39].color = 'red'   # 37-39X_AF
    TRV.LINKS[22+39].color = 'red'  # 0_5_AF
    TRV.LINKS[23+39].color = 'red'  # 0_6_AF
    TRV.LINKS[31+39].color = 'red'  # 1_7_AF

    TRV.NODES[29+37].color = 'red'  # 39_S_AF
    TRV.NODES[34+37].color = 'red'  # main0_dest_AF
    TRV.NODES[35+37].color = 'red'  # Main1_dest_AF

elif AFSlatersMain0Closed and AFSlatersMain2Closed:
    # Example of closing main 0/2
    TRV.LINKS[7+39].color = 'red'   # 37-39X_AF
    TRV.LINKS[9+39].color = 'red'   # 45-47X_AF
    TRV.LINKS[22+39].color = 'red'  # 0_5_AF
    TRV.LINKS[23+39].color = 'red'  # 0_6_AF
    TRV.LINKS[36+39].color = 'red'  # 2_5_AF
    TRV.LINKS[37+39].color = 'red'  # 2_6_AF

    TRV.NODES[29+37].color = 'red'  # 39_S_AF
    TRV.NODES[33+37].color = 'red'  # 47_S_AF
    TRV.NODES[34+37].color = 'red'  # main0_dest_AF
    TRV.NODES[36+37].color = 'red'  # main2_dest_AF

elif AFSlatersMain0Closed and AFSlatersMain3Closed:
    # Example of closing main 0/3
    TRV.LINKS[7+39].color = 'red'  # 37-39X_AF
    TRV.LINKS[8+39].color = 'red'  # 41-43X_AF
    TRV.LINKS[22+39].color = 'red'  # 0_5_AF
    TRV.LINKS[23+39].color = 'red'  # 0_6_AF
    TRV.LINKS[41+39].color = 'red'  # 3_3_AF
    TRV.LINKS[42+39].color = 'red'  # 3_4_AF

    TRV.NODES[29+37].color = 'red'  # 39_S_AF
    TRV.NODES[31+37].color = 'red'  # 43_S_AF
    TRV.NODES[34+37].color = 'red'  # main0_dest_AF
    TRV.NODES[37+37].color = 'red'  # main3_dest_AF

elif AFSlatersMain1Closed and AFSlatersMain2Closed:
    # Example of closing main 1/2
    TRV.LINKS[6+39].color = 'red'  # 31-33X_AF
    TRV.LINKS[9+39].color = 'red'  # 45-47X_AF
    TRV.LINKS[30+39].color = 'red'  # 1_6_AF
    TRV.LINKS[31+39].color = 'red'  # 1_7_AF
    TRV.LINKS[36+39].color = 'red'  # 2_5_AF
    TRV.LINKS[37+39].color = 'red'  # 2_6_AF

    TRV.NODES[32+37].color = 'red'  # 45_S_AF
    TRV.NODES[33+37].color = 'red'  # 47_S_AF
    TRV.NODES[35+37].color = 'red'  # Main1_dest_AF
    TRV.NODES[36+37].color = 'red'  # main2_dest_AF

elif AFSlatersMain2Closed and AFSlatersMain3Closed:
    TRV.LINKS[4+39].color = 'red'   # 21-23X_AF
    TRV.LINKS[8+39].color = 'red'   # 41-43X_AF
    TRV.LINKS[9+39].color = 'red'   # 45-47X_AF
    TRV.LINKS[10+39].color = 'red'  # yard1_AF
    TRV.LINKS[11+39].color = 'red'  # y1_2_AF
    TRV.LINKS[34+39].color = 'red'  # 2_2_AF
    TRV.LINKS[35+39].color = 'red'  # 2_3_AF
    TRV.LINKS[36+39].color = 'red'  # 2_4_AF
    TRV.LINKS[37+39].color = 'red'  # 2_5_AF
    TRV.LINKS[40+39].color = 'red'  # 3_2_AF
    TRV.LINKS[41+39].color = 'red'  # 3_3_AF
    TRV.LINKS[42+39].color = 'red'  # 3_4_AF

    TRV.NODES[0+37].color = 'red'   # NS Horn Track 1
    TRV.NODES[1+37].color = 'red'   # y1e_AF
    TRV.NODES[14+37].color = 'red'  # 6_S_AF
    TRV.NODES[21+37].color = 'red'  # 23_S_AF
    TRV.NODES[30+37].color = 'red'  # 41_S_AF
    TRV.NODES[31+37].color = 'red'  # 43_S_AF
    TRV.NODES[33+37].color = 'red'  # 47_S_AF
    TRV.NODES[37+37].color = 'red'  # Main 3_AF
    TRV.NODES[36+37].color = 'red'  # Main 2_AF

elif AFSlatersMain1Closed and AFSlatersMain3Closed:
    # Example of closing main 1/3
    TRV.LINKS[8+39].color = 'red'   # 41-43X_AF
    TRV.LINKS[10+39].color = 'red'  # yard1_AF
    TRV.LINKS[11+39].color = 'red'  # y1_2_AF
    TRV.LINKS[31+39].color = 'red'  # 1_7_AF
    TRV.LINKS[40+39].color = 'red'  # 3_2_AF
    TRV.LINKS[41+39].color = 'red'  # 3_3_AF
    TRV.LINKS[42+39].color = 'red'  # 3_4_AF

    TRV.NODES[0+37].color = 'red'   # NS Horn Track 1
    TRV.NODES[1+37].color = 'red'   # y1e_AF
    TRV.NODES[14+37].color = 'red'  # 6_S_AF
    TRV.NODES[31+37].color = 'red'  # 43_S_AF
    TRV.NODES[35+37].color = 'red'  # Main1_dest_AF
    TRV.NODES[37+37].color = 'red'  # main3_dest_AF

# 4 versions of 1 track closed (0,0,0,0 is 16th possible combo and not included since it's the default state)
elif AFSlatersMain3Closed:
    TRV.LINKS[8+39].color = 'red'   # 41-43X_AF
    TRV.LINKS[10+39].color = 'red'  # yard1_AF
    TRV.LINKS[11+39].color = 'red'  # y1_2_AF
    TRV.LINKS[40+39].color = 'red'  # 3_2_AF
    TRV.LINKS[41+39].color = 'red'  # 3_3_AF
    TRV.LINKS[42+39].color = 'red'  # 3_4_AF

    TRV.NODES[0+37].color = 'red'   # NS Horn Track 1
    TRV.NODES[1+37].color = 'red'   # y1e_AF
    TRV.NODES[14+37].color = 'red'  # 6_S_AF
    TRV.NODES[31+37].color = 'red'  # 43_S_AF
    TRV.NODES[37+37].color = 'red'  # Main 3_AF

elif AFSlatersMain2Closed:
    TRV.LINKS[36+39].color = 'red'  # Main 2_AF
    TRV.LINKS[37+39].color = 'red'  # Main 3_AF
    TRV.LINKS[9+39].color = 'red'   # 45-47X_AF

    TRV.NODES[33+37].color = 'red'  # 47_S_AF
    TRV.NODES[36+37].color = 'red'  # Main 2_AF

elif AFSlatersMain1Closed:
    TRV.LINKS[31+39].color = 'red'  # 1_7_AF

    TRV.NODES[35+37].color = 'red'  # 2_3_AF

elif AFSlatersMain0Closed:
    TRV.LINKS[7+39].color = 'red'   # 37-39X_AF
    TRV.LINKS[22+39].color = 'red'  # 0_5_AF
    TRV.LINKS[23+39].color = 'red'  # 0_6_AF

    TRV.NODES[28+37].color = 'red'  # 1_4_AF
    TRV.NODES[29+37].color = 'red'  # 1_5_AF
    TRV.NODES[34+37].color = 'red'  # 2_2_AF

# ================================= Signal Controls - After AF ========================================================

if pre_AF_yard1_disabled:
    TRV.LINKS[49].color = 'red'  # yard1_AF
    TRV.LINKS[50].color = 'red'  # y1_2_AF

    TRV.NODES[37].color = 'red'  # NS Horn Track 1
    TRV.NODES[38].color = 'red'  # y1e_AF

if pre_AF_yard2_disabled:
    TRV.LINKS[39].color = 'red'  # 1-3X_AF
    TRV.LINKS[51].color = 'red'  # yard2_AF

    TRV.NODES[39].color = 'red'  # NS Horn Track 2
    TRV.NODES[48].color = 'red'  # 1_S_AF

if pre_AF_yard3_disabled:
    TRV.LINKS[77].color = 'red'  # 3_0_AF

    TRV.NODES[40].color = 'red'  # NS Horn Track 3

if pre_AF_main3_disabled:
    TRV.LINKS[71].color = 'red'  # "2_0_AF"
    TRV.NODES[41].color = 'red'  # Ex Main 3

if pre_AF_main2_disabled:
    TRV.LINKS[63].color = 'red'  # "1_0_AF"
    TRV.NODES[42].color = 'red'  # Ex Main 2

if pre_AF_main1_disabled:
    TRV.LINKS[56].color = 'red'  # "0_0_AF"
    TRV.NODES[43].color = 'red'  # Ex Main 1


if pre_AF_ns_disabled:
    TRV.LINKS[52].color = 'red'  # NS_AF
    TRV.LINKS[53].color = 'red'  # NS Yard_AF

    TRV.NODES[45].color = 'red'  # NS_Yard
    TRV.NODES[44].color = 'red'  # NS_Yard