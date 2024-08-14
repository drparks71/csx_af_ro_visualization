from src.rail_network_simulator.network_definitions import TRV


def existing_conditions():
    # Reset the lines to all be green
    for link in TRV.LINKS:
        link.color = 'green'
    for node in TRV.NODES:
        node.color = 'green'

    # Hide the lines that don't yet exist or are removed
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
    TRV.LINKS[102].color = 'black'
    TRV.LINKS[103].color = 'black'
    TRV.LINKS[104].color = 'black'
    TRV.LINKS[105].color = 'black'
    TRV.LINKS[106].color = 'black'
    TRV.LINKS[107].color = 'black'
    TRV.LINKS[108].color = 'black'
    TRV.LINKS[109].color = 'black'
    TRV.LINKS[110].color = 'black'


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
    TRV.NODES[93].color = 'black'
    TRV.NODES[99].color = 'black'
    TRV.NODES[97].color = 'black'
    TRV.NODES[96].color = 'black'
    TRV.NODES[95].color = 'black'
    TRV.NODES[94].color = 'black'
    TRV.NODES[101].color = 'black'

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

    # Get rid of signals that don't exist yet
    TRV.signal_attributes_low['Proposed 2'][3] = False
    TRV.signal_attributes_low['Proposed 3'][3] = False
    TRV.signal_attributes_low['NS Horn Track 1'][3] = False
    TRV.signal_attributes_low['NS Horn Track 2'][3] = False
    TRV.signal_attributes_low['slaters_Proposed 2_8'][3] = False
    TRV.signal_attributes_low['slaters_Proposed 3_9'][3] = False

    TRV.signal_attributes_high['Main 2_2'][3] = False
    TRV.signal_attributes_high['Main 3_2'][3] = False
    TRV.signal_attributes_high['slaters_Proposed 2_3'][3] = False
    TRV.signal_attributes_high['slaters_Proposed 3_4'][3] = False


def phase_1_stage_1a():
    # Reset the lines to all be green
    for link in TRV.LINKS:
        link.color = 'green'
    for node in TRV.NODES:
        node.color = 'green'

    # Define the links as they exist in 1B
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
    TRV.LINKS[102].color = 'black'
    TRV.LINKS[103].color = 'black'
    TRV.LINKS[104].color = 'black'
    TRV.LINKS[105].color = 'black'
    TRV.LINKS[106].color = 'black'
    TRV.LINKS[107].color = 'black'
    TRV.LINKS[108].color = 'black'
    TRV.LINKS[109].color = 'black'
    TRV.LINKS[110].color = 'black'

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
    TRV.NODES[93].color = 'black'
    TRV.NODES[99].color = 'black'
    TRV.NODES[97].color = 'black'
    TRV.NODES[96].color = 'black'
    TRV.NODES[95].color = 'black'
    TRV.NODES[94].color = 'black'
    TRV.NODES[101].color = 'black'

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
    TRV.NODES[2].color = 'red'
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

    # Get rid of signals that don't exist yet
    TRV.signal_attributes_low['Proposed 2'][3] = False
    TRV.signal_attributes_low['Proposed 3'][3] = False
    TRV.signal_attributes_low['NS Horn Track 1'][3] = False
    TRV.signal_attributes_low['NS Horn Track 2'][3] = False
    TRV.signal_attributes_low['slaters_Proposed 2_8'][3] = False
    TRV.signal_attributes_low['slaters_Proposed 3_9'][3] = False

    TRV.signal_attributes_high['Main 2_2'][3] = False
    TRV.signal_attributes_high['Main 3_2'][3] = False
    TRV.signal_attributes_high['slaters_Proposed 2_3'][3] = False
    TRV.signal_attributes_high['slaters_Proposed 3_4'][3] = False


def phase_1_stage_1b():
    # Reset the lines to all be green
    for link in TRV.LINKS:
        link.color = 'green'
    for node in TRV.NODES:
        node.color = 'green'

    # New Tracks
    red_links = [7, 9, 10, 11, 16, 12, 13, 22, 23, 24, 25, 36, 69, 109]
    for x in red_links:
        TRV.LINKS[x].color = 'red'

    # Hide tracks unavailable to trains
    black_links = [8, 108, 100, 102, 103, 104, 105, 106, 107, 29, 37, 32, 28, 31, 27, 26, 30, 75, 80, 74, 73, 79,
                   35, 34, 45, 43, 33, 18, 47, 46, 42, 72, 41, 72, 71, 70, 44, 49, 38, 39, 50, 48]
    for x in black_links:
        TRV.LINKS[x].color = 'black'

    TRV.NODES[93].color = 'black'
    TRV.NODES[99].color = 'black'
    TRV.NODES[97].color = 'black'
    TRV.NODES[96].color = 'black'
    TRV.NODES[95].color = 'black'
    TRV.NODES[94].color = 'black'

    # AF Names
    TRV.NODES[40].name = 'NS Horn 1'
    TRV.NODES[41].name = 'Main 4'
    TRV.NODES[42].name = 'Main 3'
    TRV.NODES[43].name = 'Main 2'
    TRV.NODES[45].name = 'Main 1'
    TRV.NODES[91].name = 'NS Yard'

    # RO Names
    TRV.NODES[4].name = 'Main 2'
    TRV.NODES[5].name = 'Main 3'

    # RO to Slaters Names
    TRV.NODES[77].name = 'Main 1'
    TRV.NODES[16].name = 'Main 2'
    TRV.NODES[17].name = 'Main 3'


def phase_1_stage_1c():
    # Reset the lines to all be green
    for link in TRV.LINKS:
        link.color = 'green'
    for node in TRV.NODES:
        node.color = 'green'

    # New Tracks
    red_links = [7, 9, 10, 11, 16, 12, 13, 22, 23, 24, 25, 69, 109, 102, 105, 107, 106, 33, 36, 104, 103]

    for x in red_links:
        TRV.LINKS[x].color = 'red'

    # Hide tracks unavailable to trains
    black_links = [8, 108, 100, 29, 37, 32, 28, 31, 27, 26, 30, 75, 80, 74, 73, 79,
                   35, 34, 45, 43, 18, 47, 46, 42, 72, 41, 72, 71, 70, 44, 49, 38, 39, 50, 48]
    for x in black_links:
        TRV.LINKS[x].color = 'black'

    TRV.NODES[93].color = 'black'
    TRV.NODES[99].color = 'black'
    TRV.NODES[97].color = 'black'
    TRV.NODES[96].color = 'black'
    TRV.NODES[95].color = 'black'
    TRV.NODES[94].color = 'black'

    # AF Names
    TRV.NODES[40].name = 'NS Horn 1'
    TRV.NODES[41].name = 'Main 4'
    TRV.NODES[42].name = 'Main 3'
    TRV.NODES[43].name = 'Main 2'
    TRV.NODES[45].name = 'Main 1'
    TRV.NODES[91].name = 'NS Yard'

    # RO Names
    TRV.NODES[4].name = 'Main 2'
    TRV.NODES[5].name = 'Main 3'

    # RO to Slaters Names
    TRV.NODES[77].name = 'Main 1'
    TRV.NODES[16].name = 'Main 2'
    TRV.NODES[17].name = 'Main 3'


def phase_1_stage_2a():
    # Reset the lines to all be green
    for link in TRV.LINKS:
        link.color = 'green'
    for node in TRV.NODES:
        node.color = 'green'

    # Hide Tracks
    black_links = [7, 100, 101, 82, 104, 106, 103, 99, 109, 86, 85, 18, 53, 90, 72, 73, 74, 46, 47,
                   45, 42, 79, 48, 49, 44, 43, 38, 50, 41,  70, 71, 39]

    for x in black_links:
        TRV.LINKS[x].color = 'black'

    # New Tracks
    red_links = [8, 9, 12, 16, 102, 83, 82, 86, 100, 105, 106, 107, 87, 88, 17, 90, 53, 89, 54, 109]

    for x in red_links:
        TRV.LINKS[x].color = 'red'

    TRV.NODES[77].name = 'Main 1'
    TRV.NODES[19].name = 'Main 3'
    TRV.NODES[18].name = 'Main 2'

def phase_1_stage_2b():
    # Reset the lines to all be green
    for link in TRV.LINKS:
        link.color = 'green'
    for node in TRV.NODES:
        node.color = 'green'

def phase_1_stage_3():
    # Reset the lines to all be green
    for link in TRV.LINKS:
        link.color = 'green'
    for node in TRV.NODES:
        node.color = 'green'

