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
    TRV.NODES[4].name = 'Main 2'
    TRV.NODES[5].name = 'Main 3'
    TRV.NODES[16].name = 'Main 2'
    TRV.NODES[17].name = 'Main 3'
    TRV.NODES[18].name = 'Main 2'
    TRV.NODES[19].name = 'Main 3'
    TRV.NODES[37].name = ''
    TRV.NODES[39].name = ''
    TRV.NODES[40].name = 'NS Horn 1'
    TRV.NODES[41].name = 'Main 4'
    TRV.NODES[42].name = 'Main 3'
    TRV.NODES[43].name = 'Main 2'
    TRV.NODES[45].name = 'Main 1'
    TRV.NODES[77].name = 'Main 1'
    TRV.NODES[91].name = 'NS Yard'
    TRV.NODES[104].name = ''

    # Get rid of signals that don't exist yet
    TRV.signal_attributes_low['RO_Proposed 2'][3] = True
    TRV.signal_attributes_low['RO_Existing 1'][3] = True
    TRV.signal_attributes_low['RO_Proposed 3'][3] = True
    TRV.signal_attributes_low['RO_Temp Proposed 0'][3] = False
    TRV.signal_attributes_low['RO_Proposed 2'][3] = False
    TRV.signal_attributes_low['RO_Proposed 3'][3] = False
    TRV.signal_attributes_low['AF_NS Horn Track 1'][3] = False
    TRV.signal_attributes_low['AF_NS Horn Track 2'][3] = False
    TRV.signal_attributes_low['slaters_Proposed 2_1'][3] = False
    TRV.signal_attributes_low['slaters_Proposed 3_1'][3] = False
    TRV.signal_attributes_low['RO_Temp Proposed 0'][3] = False

    TRV.signal_attributes_high['AF_Main 2_2'][3] = False
    TRV.signal_attributes_high['AF_Main 3_2'][3] = False
    TRV.signal_attributes_high['slaters_Proposed 2_0'][3] = False
    TRV.signal_attributes_high['slaters_Proposed 3_0'][3] = False


def phase_1_stage_1a():
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
    TRV.NODES[16].name = 'Main 2'
    TRV.NODES[17].name = 'Main 3'
    TRV.NODES[18].name = 'Main 2'
    TRV.NODES[19].name = 'Main 3'
    TRV.NODES[37].name = ''
    TRV.NODES[39].name = ''
    TRV.NODES[40].name = 'NS Horn 1'
    TRV.NODES[41].name = 'Main 4'
    TRV.NODES[42].name = 'Main 3'
    TRV.NODES[43].name = 'Main 2'
    TRV.NODES[45].name = 'Main 1'
    TRV.NODES[77].name = 'Main 1'
    TRV.NODES[91].name = 'NS Yard'
    TRV.NODES[104].name = ''

    red_links = [7, 25, 36, 24, 23, 22, 69, 66, 67, 68, 93, 63, 94, 76, 77, 78, 64, 65, 112]

    for x in red_links:
        TRV.LINKS[x].color = 'red'

    red_nodes = [1, 2, 30, 34, 17, 31, 72, 34, 86, 69, 65, 63, 59, 57, 56, 51, 50, 49, 40]

    for x in red_nodes:
        TRV.NODES[x].color = 'red'


    # Get rid of signals that don't exist yet
    TRV.signal_attributes_low['RO_Temp Proposed 0'][3] = False
    TRV.signal_attributes_low['RO_Proposed 2'][3] = False
    TRV.signal_attributes_low['RO_Proposed 3'][3] = False
    TRV.signal_attributes_low['AF_NS Horn Track 1'][3] = False
    TRV.signal_attributes_low['AF_NS Horn Track 2'][3] = False
    TRV.signal_attributes_low['slaters_Proposed 2_1'][3] = False
    TRV.signal_attributes_low['slaters_Proposed 3_1'][3] = False
    TRV.signal_attributes_low['RO_Temp Proposed 0'][3] = False

    TRV.signal_attributes_high['AF_Main 2_2'][3] = False
    TRV.signal_attributes_high['AF_Main 3_2'][3] = False
    TRV.signal_attributes_high['slaters_Proposed 2_0'][3] = False
    TRV.signal_attributes_high['slaters_Proposed 3_0'][3] = False


def phase_1_stage_1b():
    # Reset the lines to all be green
    for link in TRV.LINKS:
        link.color = 'green'
    for node in TRV.NODES:
        node.color = 'green'

    red_nodes = [2, 3, 6, 7, 14, 15, 19, 22, 30, 31, 34, 40, 49, 50, 51, 56, 57, 59, 63, 65, 69, 72, 86, 102, 104]

    for x in red_nodes:
        TRV.NODES[x].color = 'red'

    # New Tracks
    red_links = [7, 9, 10, 11, 12, 13, 16, 22, 23, 24, 25, 33, 36, 63, 64, 65, 66, 67, 68, 69, 76, 77, 78, 93, 94,
                 102, 105, 106, 107, 109]

    for x in red_links:
        TRV.LINKS[x].color = 'red'

    # Hide tracks unavailable to trains
    black_links = [7, 8, 18, 26, 27, 28, 29, 30, 31, 32, 34, 35, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48,
                   49, 50, 70, 71, 72, 72, 73, 74, 75, 79, 80, 100, 103, 104, 108, 110, 110, 111, 112, 113, 114]

    for x in black_links:
        TRV.LINKS[x].color = (0,0,0,0)

    black_nodes = [1, 4, 17, 18, 23, 24, 27, 28, 29, 35, 36, 37, 38, 39, 48, 52, 55, 58, 67, 68, 70, 73, 74, 93,
                   94, 95, 96, 97, 99, 101]

    for x in black_nodes:
        TRV.NODES[x].color = (0,0,0,0)

    # Rename tracks to what their current names are
    TRV.NODES[4].name = 'Main 2'
    TRV.NODES[5].name = 'Main 3'
    TRV.NODES[16].name = 'Main 2'
    TRV.NODES[17].name = 'Main 3'
    TRV.NODES[18].name = 'Main 2'
    TRV.NODES[19].name = 'Main 3'
    TRV.NODES[37].name = ''
    TRV.NODES[39].name = ''
    TRV.NODES[40].name = 'NS Horn 1'
    TRV.NODES[41].name = 'Main 4'
    TRV.NODES[42].name = 'Main 3'
    TRV.NODES[43].name = 'Main 2'
    TRV.NODES[45].name = 'Main 1'
    TRV.NODES[77].name = 'Main 1'
    TRV.NODES[91].name = 'NS Yard'
    TRV.NODES[104].name = 'Main 0'

    # Get rid of signals that don't exist yet
    TRV.signal_attributes_low['RO_Temp Proposed 0'][3] = True
    TRV.signal_attributes_low['RO_Proposed 2'][3] = True
    TRV.signal_attributes_low['RO_Proposed 3'][3] = True
    TRV.signal_attributes_low['AF_NS Horn Track 1'][3] = False
    TRV.signal_attributes_low['AF_NS Horn Track 2'][3] = False
    TRV.signal_attributes_low['slaters_Proposed 2_1'][3] = False
    TRV.signal_attributes_low['slaters_Proposed 3_1'][3] = False
    TRV.signal_attributes_low['RO_Existing 3'][3] = False

    TRV.signal_attributes_high['slaters_Proposed 0_0'][3] = True
    TRV.signal_attributes_high['slaters_Proposed 0_0'][3] = True
    TRV.signal_attributes_high['AF_Main 2_2'][3] = False
    TRV.signal_attributes_high['AF_Main 3_2'][3] = False
    TRV.signal_attributes_high['slaters_Proposed 2_0'][3] = True
    TRV.signal_attributes_high['slaters_Proposed 2_0'][1] = (34, 14.75)


def phase_1_stage_2a():
    # Reset the lines to all be green
    for link in TRV.LINKS:
        link.color = 'green'
    for node in TRV.NODES:
        node.color = 'green'

    black_nodes = [0, 1, 16, 17, 18, 23, 24, 27, 28, 29, 35, 36, 37, 38, 39, 48, 52, 55, 58, 67, 68, 70,
                   73, 74, 92, 96, 97, 101]

    for x in black_nodes:
        TRV.NODES[x].color = (0,0,0,0)

    red_nodes = [13, 14, 93, 94, 95, 99, 102, 104]

    for x in red_nodes:
        TRV.NODES[x].color = 'red'

    # Hide Tracks
    black_links = [7, 18, 26, 27, 28, 29, 30, 31, 32, 34, 35, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                   50, 70, 71, 72, 73, 74, 75, 79, 80, 99, 100, 100, 101, 103, 104, 106, 108,
                   111, 112, 113, 114]

    for x in black_links:
        TRV.LINKS[x].color = (0,0,0,0)

    # New Tracks
    red_links = [6, 10, 11, 16, 21, 102, 105, 106, 107, 110]

    for x in red_links:
        TRV.LINKS[x].color = 'red'

    # Rename tracks to what their current names are
    TRV.NODES[4].name = 'Main 2'
    TRV.NODES[5].name = 'Main 3'
    TRV.NODES[16].name = ''
    TRV.NODES[17].name = ''
    TRV.NODES[18].name = 'Main 2'
    TRV.NODES[19].name = 'Main 3'
    TRV.NODES[37].name = ''
    TRV.NODES[39].name = ''
    TRV.NODES[40].name = 'NS Horn 1'
    TRV.NODES[41].name = 'Main 4'
    TRV.NODES[42].name = 'Main 3'
    TRV.NODES[43].name = 'Main 2'
    TRV.NODES[45].name = 'Main 1'
    TRV.NODES[77].name = 'Main 1'
    TRV.NODES[91].name = 'NS Yard'
    TRV.NODES[104].name = 'Main 0'

    # Get rid of signals that don't exist yet
    TRV.signal_attributes_low['RO_Proposed 2'][3] = True
    TRV.signal_attributes_low['RO_Proposed 3'][3] = True
    TRV.signal_attributes_low['AF_NS Horn Track 1'][3] = False
    TRV.signal_attributes_low['AF_NS Horn Track 2'][3] = False
    TRV.signal_attributes_low['slaters_Proposed 2_1'][3] = False
    TRV.signal_attributes_low['slaters_Proposed 3_1'][3] = False
    TRV.signal_attributes_low['RO_Existing 2'][3] = False
    TRV.signal_attributes_low['RO_Existing 3'][3] = False

    TRV.signal_attributes_high['AF_Main 2_2'][3] = False
    TRV.signal_attributes_high['AF_Main 3_2'][3] = False
    TRV.signal_attributes_high['slaters_Proposed 2_0'][1] = (34, 14.75)
    TRV.signal_attributes_high['slaters_Proposed 3_0'][3] = False


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
    red_links = [1, 2, 15, 17, 53, 54, 82, 83, 85, 86, 87, 88, 89, 90, 102, 105, 106, 107, 113, 114]

    for x in red_links:
        TRV.LINKS[x].color = 'red'

    red_nodes = [11, 20, 25, 46, 47, 75, 76, 77, 78, 80, 92, 93, 94, 95, 98, 99, 100, 103, 104]

    for x in red_nodes:
        TRV.NODES[x].color = 'red'

    # Rename tracks to what their current names are
    TRV.NODES[4].name = 'Main 2'
    TRV.NODES[5].name = 'Main 3'
    TRV.NODES[16].name = ''
    TRV.NODES[17].name = ''
    TRV.NODES[18].name = 'Main 2'
    TRV.NODES[19].name = 'Main 3'
    TRV.NODES[37].name = ''
    TRV.NODES[39].name = ''
    TRV.NODES[40].name = 'NS Horn 1'
    TRV.NODES[41].name = 'Main 4'
    TRV.NODES[42].name = 'Main 3'
    TRV.NODES[43].name = 'Main 2'
    TRV.NODES[45].name = 'Main 1'
    TRV.NODES[77].name = 'Main 1'
    TRV.NODES[91].name = 'NS Yard'
    TRV.NODES[104].name = 'Main 0'

    TRV.signal_attributes_low['RO_Temp Proposed 0'][3] = True
    TRV.signal_attributes_low['RO_Existing 2'][3] = False
    TRV.signal_attributes_low['RO_Existing 3'][3] = False


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

    # Rename tracks to what their current names are
    TRV.NODES[4].name = 'Main 2'
    TRV.NODES[5].name = 'Main 3'
    TRV.NODES[16].name = ''
    TRV.NODES[17].name = ''
    TRV.NODES[18].name = 'Main 2'
    TRV.NODES[19].name = 'Main 3'
    TRV.NODES[40].name = 'NS Horn 1'
    TRV.NODES[41].name = 'Main 4'
    TRV.NODES[42].name = 'Main 3'
    TRV.NODES[43].name = 'Main 2'
    TRV.NODES[45].name = 'Main 1'
    TRV.NODES[77].name = 'Main 1'
    TRV.NODES[91].name = 'NS Yard'
    TRV.NODES[104].name = 'Main 0'

    # TRV.NODES[104].name = 'Main 0'
    # TRV.NODES[77].name = 'Main 1'
    # TRV.NODES[16].name = ''
    # TRV.NODES[17].name = ''
    # TRV.NODES[19].name = 'Main 3'
    # TRV.NODES[18].name = 'Main 2'

    TRV.signal_attributes_low['RO_Temp Proposed 0'][3] = True
    TRV.signal_attributes_low['RO_Existing 2'][3] = False
    TRV.signal_attributes_low['RO_Existing 3'][3] = False
