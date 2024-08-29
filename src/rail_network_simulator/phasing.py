from network_definitions import TRV


def existing_conditions():
    # Reset the lines to all be green
    for link in TRV.LINKS:
        link.color = 'green'
    for node in TRV.NODES:
        node.color = 'green'

    black_nodes = [3, 12, 14, 15, 18, 19, 19, 23, 24, 27, 28, 29, 35, 36, 37, 38, 39, 48, 52, 55, 58, 67, 68, 70, 73,
                   73, 74, 93, 94, 94, 95, 96, 97, 99, 102, 104]

    for x in black_nodes:
        TRV.NODES[x].color = (0, 0, 0, 0)

    black_links = [8, 9, 10, 11, 12, 13, 16, 18, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 41, 42, 43,
                   44, 45, 46, 47, 48, 49, 50, 70, 71, 72, 73, 74, 75, 75, 79, 80, 99, 102, 103, 104, 105, 106, 107,
                   108, 109, 110, 111, 113, 114]

    for x in black_links:
        TRV.LINKS[x].color = (0, 0, 0, 0)

    # Hide the lines that don't yet exist or are removed

    TRV.NODES[6].color = (0,0,0,0)
    TRV.NODES[7].color = (0,0,0,0)

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

    black_links = [8, 9, 10, 11, 12, 13, 16, 18, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 41, 42, 43, 44, 45,
                   46, 47, 48, 49, 50, 70, 71, 72, 73, 74, 75, 79, 80, 100, 102, 103, 104, 105, 106, 107, 108, 109,
                   110, 111, 113, 114]


    for x in black_links:
        TRV.LINKS[x].color = (0, 0, 0, 0)
    # Define the links as they exist in 1B

    black_nodes = [6, 7, 12, 15, 14, 18, 19, 24, 27, 36, 68, 70, 67, 58, 73, 74, 28, 29, 35, 55, 52, 48, 38, 39, 37, 93,
                   99, 97, 96, 95, 94, 101, 104, 3, 19, 102, 23, 73]

    for x in black_nodes:
        TRV.NODES[x].color = (0,0,0,0)


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

    red_nodes = [2, 3, 6, 7, 14, 15, 30, 31, 34, 72]

    for x in red_nodes:
        TRV.NODES[x].color = 'red'

    # New Tracks
    red_links = [7, 9, 10, 11, 12, 13, 16, 22, 23, 24, 25, 36, 69, 109]

    for x in red_links:
        TRV.LINKS[x].color = 'red'

    # Hide tracks unavailable to trains
    black_links = [7, 8, 18, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48,
                   49, 50, 70, 71, 72, 72, 73, 74, 75, 79, 80, 100, 102, 103, 104, 105, 106, 107, 108, 110, 110,
                   111, 112, 113, 114]

    for x in black_links:
        TRV.LINKS[x].color = (0,0,0,0)

    black_nodes = [1, 17, 18, 23, 24, 27, 28, 29, 35, 36, 37, 38, 39, 48, 52, 55, 58, 67, 68, 70, 73, 74, 93, 94,
                   95, 96, 97, 99, 101, 102, 104]

    for x in black_nodes:
        TRV.NODES[x].color = (0,0,0,0)


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

    red_nodes = [2, 3, 6, 7, 14, 15, 19, 22, 30, 31, 34, 72, 86, 102, 104]

    for x in red_nodes:
        TRV.NODES[x].color = 'red'

    # New Tracks
    red_links = [7, 9, 10, 11, 12, 13, 16, 22, 23, 24, 25, 33, 36, 69, 102, 103, 104, 105, 106, 107, 109]

    for x in red_links:
        TRV.LINKS[x].color = 'red'

    # Hide tracks unavailable to trains
    black_links = [7, 8, 18, 26, 27, 28, 29, 30, 31, 32, 34, 35, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48,
                   49, 50, 70, 71, 72, 72, 73, 74, 75, 79, 80, 100, 108, 110, 110, 111, 112, 113, 114]

    for x in black_links:
        TRV.LINKS[x].color = (0,0,0,0)

    black_nodes = [1, 4, 17, 18, 23, 24, 27, 28, 29, 35, 36, 37, 38, 39, 48, 52, 55, 58, 67, 68, 70, 73, 74, 93,
                   94, 95, 96, 97, 99, 101]

    for x in black_nodes:
        TRV.NODES[x].color = (0, 0, 0, 0)


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

    black_nodes = [1, 17, 18, 23, 24, 27, 28, 29, 35, 36, 37, 38, 39, 48, 52, 55, 58, 67, 68, 70, 73, 74, 92, 96,
                   97, 101]

    for x in black_nodes:
        TRV.NODES[x].color = (0,0,0,0)

    red_nodes = [3, 6, 7, 14, 15, 19, 20, 25, 46, 47, 75, 77, 78, 80, 93, 94, 95, 98, 99, 100, 102, 103, 104]

    for x in red_nodes:
        TRV.NODES[x].color = 'red'

    # Hide Tracks
    black_links = [7, 18, 26, 27, 28, 29, 30, 31, 32, 34, 35, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                   50, 53, 70, 71, 72, 73, 74, 75, 79, 80, 82, 86, 90, 99, 100, 100, 101, 103, 104, 106, 108,
                   109, 111, 112, 113, 114]

    for x in black_links:
        TRV.LINKS[x].color = (0,0,0,0)

    # New Tracks
    red_links = [8, 9, 10, 11, 12, 13, 16, 17, 53, 54, 82, 83, 86, 87, 88, 89, 90, 102, 105, 106, 107, 109,
                 110, 115]

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
    black_links = [7, 18, 26, 27, 28, 29, 30, 31, 32, 34, 35, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                   50, 53, 70, 71, 72, 73, 74, 75, 79, 80, 82, 86, 90, 99, 100, 100, 101, 103, 104, 106, 108,
                   111, 112, 115]

    for x in black_links:
        TRV.LINKS[x].color = (0,0,0,0)

    black_nodes = [1, 16, 17, 18, 23, 24, 27, 28, 29, 35, 36, 37, 38, 39, 48, 52, 55, 58, 67, 68, 70, 73, 74, 96, 97,
                   101]

    for x in black_nodes:
        TRV.NODES[x].color = (0,0,0,0)

    # New Tracks
    red_links = [17, 53, 54, 82, 83, 86, 87, 88, 89, 90, 102, 105, 106, 107, 113, 114]

    for x in red_links:
        TRV.LINKS[x].color = 'red'

    red_nodes = [20, 25, 46, 47, 75, 77, 78, 80, 92, 93, 94, 95, 98, 99, 100, 103, 104]

    for x in red_nodes:
        TRV.NODES[x].color = 'red'

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
    black_links = [7, 18, 26, 27, 28, 29, 30, 31, 32, 34, 35, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                   50, 70, 71, 72, 73, 74, 75, 79, 80, 99, 100, 100, 101, 103, 104, 108, 109, 111, 112, 115]

    for x in black_links:
        TRV.LINKS[x].color = (0,0,0,0)

    black_nodes = [1, 16, 17, 18, 23, 23, 23, 24, 26, 27, 28, 29, 35, 36, 37, 38, 39, 48, 52, 55, 58, 67, 68, 70, 73,
                   73, 74, 96, 97, 101]

    for x in black_nodes:
        TRV.NODES[x].color = (0,0,0,0)

    red_nodes = [0, 2, 3, 6, 7, 14, 15, 19, 21, 30, 31, 32, 33, 34, 40, 49, 50, 51, 56, 57, 59, 63, 65, 66, 69, 71, 72,
                 79, 85, 86, 102]

    for x in red_nodes:
        TRV.NODES[x].color = 'red'

    # New Tracks
    red_links = [8, 9, 10, 11, 12, 13, 16, 19, 20, 21, 21, 22, 23, 24, 24, 25, 25, 33, 36, 60, 61, 63, 64, 65, 66, 67,
                 68, 69, 76, 77, 78, 81, 81, 84, 85, 93, 94, 109, 110]

    for x in red_links:
        TRV.LINKS[x].color = 'red'

    TRV.NODES[104].name = 'Main 0'
    TRV.NODES[77].name = 'Main 1'
    TRV.NODES[16].name = ''
    TRV.NODES[17].name = ''
    TRV.NODES[19].name = 'Main 3'
    TRV.NODES[18].name = 'Main 2'

