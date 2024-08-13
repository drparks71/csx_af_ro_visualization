from src.rail_network_simulator.network_definitions import TRV

def existing_conditions():
    TRV.LINKS[99].color = 'black'
    TRV.LINKS[8].color = 'black'
    TRV.LINKS[9].color = 'black'
    TRV.LINKS[10].color = 'black'
    TRV.LINKS[11].color = 'black'
    TRV.LINKS[12].color = 'black'
    TRV.LINKS[13].color = 'black'
    TRV.LINKS[18].color = 'black'
    TRV.LINKS[26].color = 'black'
    TRV.LINKS[27].color = 'black'
    TRV.LINKS[28].color = 'black'
    TRV.LINKS[29].color = 'black'
    TRV.LINKS[30].color = 'black'
    TRV.LINKS[32].color = 'black'
    TRV.LINKS[33].color = 'black'
    TRV.LINKS[34].color = 'black'
    TRV.LINKS[37].color = 'black'
    TRV.LINKS[38].color = 'black'
    TRV.LINKS[39].color = 'black'
    TRV.LINKS[16].color = 'black'
    TRV.LINKS[35].color = 'black'
    TRV.LINKS[31].color = 'black'
    TRV.LINKS[81].color = 'black'
    TRV.LINKS[47].color = 'black'
    TRV.LINKS[42].color = 'black'
    TRV.LINKS[43].color = 'black'
    TRV.LINKS[45].color = 'black'
    TRV.LINKS[46].color = 'black'
    TRV.LINKS[48].color = 'black'
    TRV.LINKS[49].color = 'black'
    TRV.LINKS[50].color = 'black'
    TRV.LINKS[75].color = 'black'
    TRV.LINKS[72].color = 'black'
    TRV.LINKS[73].color = 'black'
    TRV.LINKS[74].color = 'black'
    TRV.LINKS[75].color = 'black'
    TRV.LINKS[41].color = 'black'
    TRV.LINKS[71].color = 'black'
    TRV.LINKS[70].color = 'black'
    TRV.LINKS[79].color = 'black'
    TRV.LINKS[80].color = 'black'
    TRV.LINKS[44].color = 'black'
    TRV.LINKS[81].color = 'green'

    TRV.NODES[6].color = 'black'
    TRV.NODES[7].color = 'black'
    TRV.NODES[12].color = 'black'
    TRV.NODES[15].color = 'black'
    TRV.NODES[14].color = 'black'
    TRV.NODES[18].color = 'black'
    TRV.NODES[19].color = 'black'
    TRV.NODES[24].color = 'black'
    TRV.NODES[27].color = 'black'
    TRV.NODES[36].color = 'black'
    TRV.NODES[68].color = 'black'
    TRV.NODES[70].color = 'black'
    TRV.NODES[67].color = 'black'
    TRV.NODES[58].color = 'black'
    TRV.NODES[73].color = 'black'
    TRV.NODES[74].color = 'black'
    TRV.NODES[28].color = 'black'
    TRV.NODES[29].color = 'black'
    TRV.NODES[35].color = 'black'
    TRV.NODES[55].color = 'black'
    TRV.NODES[52].color = 'black'
    TRV.NODES[48].color = 'black'
    TRV.NODES[38].color = 'black'
    TRV.NODES[39].color = 'black'
    TRV.NODES[37].color = 'black'

    # Hide tracks names that aren't open to traffic yet
    TRV.NODES[18].label_color = 'black'
    TRV.NODES[19].label_color = 'black'
    TRV.NODES[39].label_color = 'black'
    TRV.NODES[37].label_color = 'black'

    # Rename tracks to what their current names are
    TRV.NODES[4].name = 'Main 2'
    TRV.NODES[5].name = 'Main 3'
    TRV.NODES[77].name = 'Main 1'
    TRV.NODES[16].name = 'Main 2'
    TRV.NODES[17].name = 'Main 3'
    TRV.NODES[45].name = 'Main 1'
    TRV.NODES[43].name = 'Main 2'
    TRV.NODES[42].name = 'Main 3'
    TRV.NODES[41].name = 'Main 4'
    TRV.NODES[40].name = 'NS Horn 1'
    TRV.NODES[91].name = 'NS Yard'

    try:
        # Get rid of signals that don't exist yet
        del TRV.signal_attributes_low['Proposed 2']
        del TRV.signal_attributes_low['Proposed 3']
        del TRV.signal_attributes_low['NS Horn Track 1']
        del TRV.signal_attributes_low['NS Horn Track 2']
        del TRV.signal_attributes_low['slaters_Proposed 2_8']
        del TRV.signal_attributes_low['slaters_Proposed 3_9']

        del TRV.signal_attributes_high['Main 2_2']
        del TRV.signal_attributes_high['Main 3_2']
        del TRV.signal_attributes_high['slaters_Proposed 2_3']
        del TRV.signal_attributes_high['slaters_Proposed 3_4']
    except KeyError:
        pass

def phase1A_staging():
    # Examples of Manipulating Nodes/Links
    # TRV.LINKS[12].label_color = 'black'
    # TRV.LINKS[12].name = 'Hello'
    TRV.LINKS[8].color = 'black'
    TRV.LINKS[9].color = 'black'
    TRV.LINKS[10].color = 'black'
    TRV.LINKS[11].color = 'black'
    TRV.LINKS[12].color = 'black'
    TRV.LINKS[13].color = 'black'
    TRV.LINKS[18].color = 'black'
    TRV.LINKS[26].color = 'black'
    TRV.LINKS[27].color = 'black'
    TRV.LINKS[28].color = 'black'
    TRV.LINKS[29].color = 'black'
    TRV.LINKS[30].color = 'black'
    TRV.LINKS[32].color = 'black'
    TRV.LINKS[33].color = 'black'
    TRV.LINKS[34].color = 'black'
    TRV.LINKS[37].color = 'black'
    TRV.LINKS[38].color = 'black'
    TRV.LINKS[39].color = 'black'
    TRV.LINKS[16].color = 'black'
    TRV.LINKS[35].color = 'black'
    TRV.LINKS[31].color = 'black'
    TRV.LINKS[81].color = 'black'
    TRV.LINKS[47].color = 'black'
    TRV.LINKS[42].color = 'black'
    TRV.LINKS[43].color = 'black'
    TRV.LINKS[45].color = 'black'
    TRV.LINKS[46].color = 'black'
    TRV.LINKS[48].color = 'black'
    TRV.LINKS[49].color = 'black'
    TRV.LINKS[50].color = 'black'
    TRV.LINKS[75].color = 'black'
    TRV.LINKS[72].color = 'black'
    TRV.LINKS[73].color = 'black'
    TRV.LINKS[74].color = 'black'
    TRV.LINKS[75].color = 'black'
    TRV.LINKS[41].color = 'black'
    TRV.LINKS[71].color = 'black'
    TRV.LINKS[70].color = 'black'
    TRV.LINKS[79].color = 'black'
    TRV.LINKS[80].color = 'black'
    TRV.LINKS[44].color = 'black'
    TRV.LINKS[81].color = 'green'
    TRV.LINKS[99].color = 'green'
    TRV.LINKS[100].color = 'black'

    TRV.NODES[6].color = 'black'
    TRV.NODES[7].color = 'black'
    TRV.NODES[12].color = 'black'
    TRV.NODES[15].color = 'black'
    TRV.NODES[14].color = 'black'
    TRV.NODES[18].color = 'black'
    TRV.NODES[19].color = 'black'
    TRV.NODES[24].color = 'black'
    TRV.NODES[27].color = 'black'
    TRV.NODES[36].color = 'black'
    TRV.NODES[68].color = 'black'
    TRV.NODES[70].color = 'black'
    TRV.NODES[67].color = 'black'
    TRV.NODES[58].color = 'black'
    TRV.NODES[73].color = 'black'
    TRV.NODES[74].color = 'black'
    TRV.NODES[28].color = 'black'
    TRV.NODES[29].color = 'black'
    TRV.NODES[35].color = 'black'
    TRV.NODES[55].color = 'black'
    TRV.NODES[52].color = 'black'
    TRV.NODES[48].color = 'black'
    TRV.NODES[38].color = 'black'
    TRV.NODES[39].color = 'black'
    TRV.NODES[37].color = 'black'

    # Hide tracks names that aren't open to traffic yet
    TRV.NODES[18].label_color = 'black'
    TRV.NODES[19].label_color = 'black'
    TRV.NODES[39].label_color = 'black'
    TRV.NODES[37].label_color = 'black'

    # Rename tracks to what their current names are
    TRV.NODES[4].name = 'Main 2'
    TRV.NODES[5].name = 'Main 3'
    TRV.NODES[77].name = 'Main 1'
    TRV.NODES[16].name = 'Main 2'
    TRV.NODES[17].name = 'Main 3'
    TRV.NODES[45].name = 'Main 1'
    TRV.NODES[43].name = 'Main 2'
    TRV.NODES[42].name = 'Main 3'
    TRV.NODES[41].name = 'Main 4'
    TRV.NODES[40].name = 'NS Horn 1'
    TRV.NODES[91].name = 'NS Yard'

    TRV.LINKS[3].color = 'red'
    TRV.LINKS[4].color = 'red'
    TRV.LINKS[7].color = 'red'
    TRV.LINKS[25].color = 'red'
    TRV.LINKS[36].color = 'red'
    TRV.LINKS[24].color = 'red'
    TRV.LINKS[23].color = 'red'
    TRV.LINKS[22].color = 'red'
    TRV.LINKS[69].color = 'red'
    TRV.LINKS[66].color = 'red'
    TRV.LINKS[67].color = 'red'
    TRV.LINKS[68].color = 'red'
    TRV.LINKS[93].color = 'red'
    TRV.LINKS[63].color = 'red'
    TRV.LINKS[94].color = 'red'
    TRV.LINKS[76].color = 'red'
    TRV.LINKS[77].color = 'red'
    TRV.LINKS[78].color = 'red'
    TRV.LINKS[64].color = 'red'
    TRV.LINKS[65].color = 'red'


    TRV.NODES[1].color = 'red'
    TRV.NODES[5].color = 'red'
    TRV.NODES[12].color = 'red'
    TRV.NODES[30].color = 'red'
    TRV.NODES[34].color = 'red'
    TRV.NODES[17].color = 'red'
    TRV.NODES[31].color = 'red'
    TRV.NODES[72].color = 'red'
    TRV.NODES[34].color = 'red'
    TRV.NODES[86].color = 'red'
    TRV.NODES[69].color = 'red'
    TRV.NODES[65].color = 'red'
    TRV.NODES[63].color = 'red'
    TRV.NODES[59].color = 'red'
    TRV.NODES[57].color = 'red'
    TRV.NODES[56].color = 'red'
    TRV.NODES[51].color = 'red'
    TRV.NODES[50].color = 'red'
    TRV.NODES[49].color = 'red'
    TRV.NODES[40].color = 'red'



    try:
        # Get rid of signals that don't exist yet
        del TRV.signal_attributes_low['Proposed 2']
        del TRV.signal_attributes_low['Proposed 3']
        del TRV.signal_attributes_low['NS Horn Track 1']
        del TRV.signal_attributes_low['NS Horn Track 2']
        del TRV.signal_attributes_low['slaters_Proposed 2_8']
        del TRV.signal_attributes_low['slaters_Proposed 3_9']

        del TRV.signal_attributes_high['Main 2_2']
        del TRV.signal_attributes_high['Main 3_2']
        del TRV.signal_attributes_high['slaters_Proposed 2_3']
        del TRV.signal_attributes_high['slaters_Proposed 3_4']
    except KeyError:
        pass