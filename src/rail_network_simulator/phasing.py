from src.rail_network_simulator.network_definitions import TRV


def existing_conditions():
    # Reset the lines to all be green
    for link in TRV.LINKS:
        link.color = 'green'
    for node in TRV.NODES:
        node.color = 'green'

    # Hide the lines that don't yet exist or are removed
    TRV.LINKS[99].color = (0,0,0,0)
    TRV.LINKS[8].color = (0,0,0,0)
    TRV.LINKS[9].color = (0,0,0,0)
    TRV.LINKS[10].color = (0,0,0,0)
    TRV.LINKS[11].color = (0,0,0,0)
    TRV.LINKS[12].color = (0,0,0,0)
    TRV.LINKS[13].color = (0,0,0,0)
    TRV.LINKS[18].color = (0,0,0,0)
    TRV.LINKS[26].color = (0,0,0,0)
    TRV.LINKS[27].color = (0,0,0,0)
    TRV.LINKS[28].color = (0,0,0,0)
    TRV.LINKS[29].color = (0,0,0,0)
    TRV.LINKS[30].color = (0,0,0,0)
    TRV.LINKS[32].color = (0,0,0,0)
    TRV.LINKS[33].color = (0,0,0,0)
    TRV.LINKS[34].color = (0,0,0,0)
    TRV.LINKS[37].color = (0,0,0,0)
    TRV.LINKS[38].color = (0,0,0,0)
    TRV.LINKS[39].color = (0,0,0,0)
    TRV.LINKS[16].color = (0,0,0,0)
    TRV.LINKS[35].color = (0,0,0,0)
    TRV.LINKS[31].color = (0,0,0,0)
    TRV.LINKS[81].color = (0,0,0,0)
    TRV.LINKS[47].color = (0,0,0,0)
    TRV.LINKS[42].color = (0,0,0,0)
    TRV.LINKS[43].color = (0,0,0,0)
    TRV.LINKS[45].color = (0,0,0,0)
    TRV.LINKS[46].color = (0,0,0,0)
    TRV.LINKS[48].color = (0,0,0,0)
    TRV.LINKS[49].color = (0,0,0,0)
    TRV.LINKS[50].color = (0,0,0,0)
    TRV.LINKS[75].color = (0,0,0,0)
    TRV.LINKS[72].color = (0,0,0,0)
    TRV.LINKS[73].color = (0,0,0,0)
    TRV.LINKS[74].color = (0,0,0,0)
    TRV.LINKS[75].color = (0,0,0,0)
    TRV.LINKS[41].color = (0,0,0,0)
    TRV.LINKS[71].color = (0,0,0,0)
    TRV.LINKS[70].color = (0,0,0,0)
    TRV.LINKS[79].color = (0,0,0,0)
    TRV.LINKS[80].color = (0,0,0,0)
    TRV.LINKS[44].color = (0,0,0,0)
    TRV.LINKS[81].color = 'green'
    TRV.LINKS[102].color = (0,0,0,0)
    TRV.LINKS[103].color = (0,0,0,0)
    TRV.LINKS[104].color = (0,0,0,0)
    TRV.LINKS[105].color = (0,0,0,0)
    TRV.LINKS[106].color = (0,0,0,0)
    TRV.LINKS[107].color = (0,0,0,0)
    TRV.LINKS[108].color = (0,0,0,0)
    TRV.LINKS[109].color = (0,0,0,0)
    TRV.LINKS[110].color = (0,0,0,0)
    TRV.LINKS[111].color = (0, 0, 0, 0)
    TRV.LINKS[113].color = (0, 0, 0, 0)
    TRV.LINKS[114].color = (0, 0, 0, 0)

    TRV.NODES[6].color = (0,0,0,0)
    TRV.NODES[7].color = (0,0,0,0)
    TRV.NODES[12].color = (0,0,0,0)
    TRV.NODES[15].color = (0,0,0,0)
    TRV.NODES[14].color = (0,0,0,0)
    TRV.NODES[18].color = (0,0,0,0)
    TRV.NODES[19].color = (0,0,0,0)
    TRV.NODES[24].color = (0,0,0,0)
    TRV.NODES[27].color = (0,0,0,0)
    TRV.NODES[36].color = (0,0,0,0)
    TRV.NODES[68].color = (0,0,0,0)
    TRV.NODES[70].color = (0,0,0,0)
    TRV.NODES[67].color = (0,0,0,0)
    TRV.NODES[58].color = (0,0,0,0)
    TRV.NODES[73].color = (0,0,0,0)
    TRV.NODES[74].color = (0,0,0,0)
    TRV.NODES[28].color = (0,0,0,0)
    TRV.NODES[29].color = (0,0,0,0)
    TRV.NODES[35].color = (0,0,0,0)
    TRV.NODES[55].color = (0,0,0,0)
    TRV.NODES[52].color = (0,0,0,0)
    TRV.NODES[48].color = (0,0,0,0)
    TRV.NODES[38].color = (0,0,0,0)
    TRV.NODES[39].color = (0,0,0,0)
    TRV.NODES[37].color = (0,0,0,0)
    TRV.NODES[93].color = (0,0,0,0)
    TRV.NODES[99].color = (0,0,0,0)
    TRV.NODES[97].color = (0,0,0,0)
    TRV.NODES[96].color = (0,0,0,0)
    TRV.NODES[95].color = (0,0,0,0)
    TRV.NODES[94].color = (0,0,0,0)
    TRV.NODES[101].color = (0,0,0,0)

    # Hide tracks names that aren't open to traffic yet
    TRV.NODES[18].label_color = (0,0,0,0)
    TRV.NODES[19].label_color = (0,0,0,0)
    TRV.NODES[39].label_color = (0,0,0,0)
    TRV.NODES[37].label_color = (0,0,0,0)

    # Rename tracks to what their current names are
    TRV.NODES[104].name = ''
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
    # //TODO - Switch to list method of assigning these when possible
    # Reset the lines to all be green
    for link in TRV.LINKS:
        link.color = 'green'
    for node in TRV.NODES:
        node.color = 'green'

    # Define the links as they exist in 1B
    TRV.LINKS[8].color = (0,0,0,0)
    TRV.LINKS[9].color = (0,0,0,0)
    TRV.LINKS[10].color = (0,0,0,0)
    TRV.LINKS[11].color = (0,0,0,0)
    TRV.LINKS[12].color = (0,0,0,0)
    TRV.LINKS[13].color = (0,0,0,0)
    TRV.LINKS[18].color = (0,0,0,0)
    TRV.LINKS[26].color = (0,0,0,0)
    TRV.LINKS[27].color = (0,0,0,0)
    TRV.LINKS[28].color = (0,0,0,0)
    TRV.LINKS[29].color = (0,0,0,0)
    TRV.LINKS[30].color = (0,0,0,0)
    TRV.LINKS[32].color = (0,0,0,0)
    TRV.LINKS[33].color = (0,0,0,0)
    TRV.LINKS[34].color = (0,0,0,0)
    TRV.LINKS[37].color = (0,0,0,0)
    TRV.LINKS[38].color = (0,0,0,0)
    TRV.LINKS[39].color = (0,0,0,0)
    TRV.LINKS[16].color = (0,0,0,0)
    TRV.LINKS[35].color = (0,0,0,0)
    TRV.LINKS[31].color = (0,0,0,0)
    TRV.LINKS[81].color = (0,0,0,0)
    TRV.LINKS[47].color = (0,0,0,0)
    TRV.LINKS[42].color = (0,0,0,0)
    TRV.LINKS[43].color = (0,0,0,0)
    TRV.LINKS[45].color = (0,0,0,0)
    TRV.LINKS[46].color = (0,0,0,0)
    TRV.LINKS[48].color = (0,0,0,0)
    TRV.LINKS[49].color = (0,0,0,0)
    TRV.LINKS[50].color = (0,0,0,0)
    TRV.LINKS[75].color = (0,0,0,0)
    TRV.LINKS[72].color = (0,0,0,0)
    TRV.LINKS[73].color = (0,0,0,0)
    TRV.LINKS[74].color = (0,0,0,0)
    TRV.LINKS[75].color = (0,0,0,0)
    TRV.LINKS[41].color = (0,0,0,0)
    TRV.LINKS[71].color = (0,0,0,0)
    TRV.LINKS[70].color = (0,0,0,0)
    TRV.LINKS[79].color = (0,0,0,0)
    TRV.LINKS[80].color = (0,0,0,0)
    TRV.LINKS[44].color = (0,0,0,0)
    TRV.LINKS[81].color = 'green'
    TRV.LINKS[99].color = 'green'
    TRV.LINKS[100].color = (0,0,0,0)
    TRV.LINKS[102].color = (0,0,0,0)
    TRV.LINKS[103].color = (0,0,0,0)
    TRV.LINKS[104].color = (0,0,0,0)
    TRV.LINKS[105].color = (0,0,0,0)
    TRV.LINKS[106].color = (0,0,0,0)
    TRV.LINKS[107].color = (0,0,0,0)
    TRV.LINKS[108].color = (0,0,0,0)
    TRV.LINKS[109].color = (0,0,0,0)
    TRV.LINKS[110].color = (0,0,0,0)
    TRV.LINKS[111].color = (0, 0, 0, 0)
    TRV.LINKS[113].color = (0, 0, 0, 0)
    TRV.LINKS[114].color = (0, 0, 0, 0)

    TRV.NODES[6].color = (0,0,0,0)
    TRV.NODES[7].color = (0,0,0,0)
    TRV.NODES[12].color = (0,0,0,0)
    TRV.NODES[15].color = (0,0,0,0)
    TRV.NODES[14].color = (0,0,0,0)
    TRV.NODES[18].color = (0,0,0,0)
    TRV.NODES[19].color = (0,0,0,0)
    TRV.NODES[24].color = (0,0,0,0)
    TRV.NODES[27].color = (0,0,0,0)
    TRV.NODES[36].color = (0,0,0,0)
    TRV.NODES[68].color = (0,0,0,0)
    TRV.NODES[70].color = (0,0,0,0)
    TRV.NODES[67].color = (0,0,0,0)
    TRV.NODES[58].color = (0,0,0,0)
    TRV.NODES[73].color = (0,0,0,0)
    TRV.NODES[74].color = (0,0,0,0)
    TRV.NODES[28].color = (0,0,0,0)
    TRV.NODES[29].color = (0,0,0,0)
    TRV.NODES[35].color = (0,0,0,0)
    TRV.NODES[55].color = (0,0,0,0)
    TRV.NODES[52].color = (0,0,0,0)
    TRV.NODES[48].color = (0,0,0,0)
    TRV.NODES[38].color = (0,0,0,0)
    TRV.NODES[39].color = (0,0,0,0)
    TRV.NODES[37].color = (0,0,0,0)
    TRV.NODES[93].color = (0,0,0,0)
    TRV.NODES[99].color = (0,0,0,0)
    TRV.NODES[97].color = (0,0,0,0)
    TRV.NODES[96].color = (0,0,0,0)
    TRV.NODES[95].color = (0,0,0,0)
    TRV.NODES[94].color = (0,0,0,0)
    TRV.NODES[101].color = (0,0,0,0)

    # Hide tracks names that aren't open to traffic yet
    TRV.NODES[18].label_color = (0,0,0,0)
    TRV.NODES[19].label_color = (0,0,0,0)
    TRV.NODES[39].label_color = (0,0,0,0)
    TRV.NODES[37].label_color = (0,0,0,0)

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
    TRV.LINKS[112].color = 'red'

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
                   35, 34, 45, 43, 33, 18, 47, 46, 42, 72, 41, 72, 71, 70, 44, 49, 38, 39, 50, 48, 110, 111, 112, 113,
                   114, 7, 110]

    for x in black_links:
        TRV.LINKS[x].color = (0,0,0,0)

    TRV.NODES[93].color = (0,0,0,0)
    TRV.NODES[99].color = (0,0,0,0)
    TRV.NODES[97].color = (0,0,0,0)
    TRV.NODES[96].color = (0,0,0,0)
    TRV.NODES[95].color = (0,0,0,0)
    TRV.NODES[94].color = (0,0,0,0)

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
    black_links = [8, 108, 100, 29, 37, 32, 28, 31, 27, 26, 30, 75, 80, 74, 73, 79, 110, 111, 112, 110, 7,
                   35, 34, 45, 43, 18, 47, 46, 42, 72, 41, 72, 71, 70, 44, 49, 38, 39, 50, 48, 113, 114]

    for x in black_links:
        TRV.LINKS[x].color = (0,0,0,0)

    TRV.NODES[93].color = (0,0,0,0)
    TRV.NODES[99].color = (0,0,0,0)
    TRV.NODES[97].color = (0,0,0,0)
    TRV.NODES[96].color = (0,0,0,0)
    TRV.NODES[95].color = (0,0,0,0)
    TRV.NODES[94].color = (0,0,0,0)

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
    black_links = [7, 100, 101, 82, 104, 106, 103, 99, 109, 86, 18, 53, 90, 72, 73, 74, 46, 47,
                   45, 42, 79, 48, 49, 44, 43, 38, 50, 41,  70, 71, 39, 108, 29, 28, 32, 31, 27, 34, 26, 30, 75, 80,
                   37, 35, 111, 112, 100, 113, 114]

    for x in black_links:
        TRV.LINKS[x].color = (0,0,0,0)

    # New Tracks
    red_links = [8, 9, 12, 16, 102, 83, 82, 86, 105, 106, 107, 87, 88, 17, 90, 53, 89, 54, 109, 110, 10, 13,
                 11, 115]

    for x in red_links:
        TRV.LINKS[x].color = 'red'

    TRV.NODES[104].name = 'Main 0'
    TRV.NODES[77].name = 'Main 1'
    TRV.NODES[16].name = ''
    TRV.NODES[17].name = ''
    TRV.NODES[18].name = 'Main 2'
    TRV.NODES[19].name = 'Main 3'


def phase_1_stage_2b():
    # Reset the lines to all be green
    for link in TRV.LINKS:
        link.color = 'green'
    for node in TRV.NODES:
        node.color = 'green'

    # Hide Tracks
    black_links = [7, 100, 101, 82, 104, 106, 103, 99, 109, 86, 18, 53, 90, 72, 73, 74, 46, 47,
                   45, 42, 79, 48, 49, 44, 43, 38, 50, 41,  70, 71, 39, 108, 29, 28, 32, 31, 27, 34, 26, 30, 75, 80,
                   37, 35, 111, 112, 100, 115]

    for x in black_links:
        TRV.LINKS[x].color = (0,0,0,0)

    # New Tracks
    red_links = [8, 9, 12, 16, 102, 83, 82, 86, 105, 106, 107, 87, 88, 17, 90, 53, 89, 54, 109, 110, 10, 13,
                 11, 113, 114]

    for x in red_links:
        TRV.LINKS[x].color = 'red'

    TRV.NODES[104].name = 'Main 0'
    TRV.NODES[77].name = 'Main 1'
    TRV.NODES[16].name = ''
    TRV.NODES[17].name = ''
    TRV.NODES[19].name = 'Main 3'
    TRV.NODES[18].name = 'Main 2'

def phase_1_stage_3():
    # Reset the lines to all be green
    for link in TRV.LINKS:
        link.color = 'green'
    for node in TRV.NODES:
        node.color = 'green'

    # Hide Tracks
    black_links = [7, 100, 101, 104, 103, 99, 109, 18, 72, 73, 74, 46, 47,
                   45, 42, 79, 48, 49, 44, 43, 38, 50, 41, 70, 71, 39, 108, 29, 28, 32, 31, 27, 34, 26, 30, 75, 80,
                   37, 35, 111, 112, 100, 115]

    for x in black_links:
        TRV.LINKS[x].color = (0,0,0,0)

    # New Tracks
    red_links = [8, 9, 12, 16, 109, 110, 10, 13, 21, 25, 24, 81, 36, 33, 19, 22, 81, 21, 84, 25, 24, 11, 85, 23, 20,
                 61, 69, 68, 67, 66, 65, 64, 63, 93, 60, 94, 78, 77, 76]

    for x in red_links:
        TRV.LINKS[x].color = 'red'

    TRV.NODES[104].name = 'Main 0'
    TRV.NODES[77].name = 'Main 1'
    TRV.NODES[16].name = ''
    TRV.NODES[17].name = ''
    TRV.NODES[19].name = 'Main 3'
    TRV.NODES[18].name = 'Main 2'

