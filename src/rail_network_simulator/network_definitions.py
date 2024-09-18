from matplotlib.pyplot import xlabel

from simulator_functions import *

# Create the World Object
TRV = World(
    name="TRV",
    deltan=1,
    tmax=1000,
    print_mode=1, save_mode=0, show_mode=1,
    random_seed=0
)

# =====================================   Node - Definitions    =======================================================
# Define Southern (Low MP) Origins
TRV.addNode("N0", 30, 12)
TRV.addNode("N1", 30, 10)
TRV.addNode("N2", 32, 10)
TRV.addNode("N3", 30, 6)

# Define Northern (High MP) Origins
TRV.addNode("N4", 0, 12, label_color='white', voffset=.4, hoffset=1)
TRV.addNode("N5", 0, 10, label_color='white', voffset=.4, hoffset=1)
TRV.addNode("N6", 6, 8)
TRV.addNode("N7", 10, 6)

# Define Switch Points
TRV.addNode("N8", 8, 12)
TRV.addNode("N9", 10, 10)
TRV.addNode("N10", 14, 10)
TRV.addNode("N11", 16, 12)
TRV.addNode("N12", 4, 10)
TRV.addNode("N13", 20, 10)
TRV.addNode("N14", 22, 8)
TRV.addNode("N15", 8, 8)

# ======================================= Slaters Lane - Definitions ==================================================

# Define Southern (Low MP) Origins
TRV.addNode("N16", 30, 12, label_color='white', voffset=.7, hoffset=1)  # RO-Slaters Main 0
TRV.addNode("N17", 30, 10, label_color='white', voffset=.7, hoffset=1)  # RO-Slaters Main 1
TRV.addNode("N18", 30, 8, label_color='white', voffset=.7, hoffset=1.7)  # RO-Slaters Main 2
TRV.addNode("N19", 30, 6, label_color='white', voffset=.7, hoffset=1.7)  # RO-Slaters Main 3

# Define Northern (High MP) Origins
TRV.addNode("N20", 58.5, 14)                                                   # OOS_NS
TRV.addNode("N21", 60, 12)                                                     # Slaters-AF Main 0
TRV.addNode("N22", 60, 10)                                                     # Slaters-AF Main 1
TRV.addNode("N23", 60, 8)                                                      # Slaters-AF Main 2
TRV.addNode("N24", 60, 6)                                                      # Slaters-AF Main 3

# Define Switch Points
TRV.addNode("N25", 54, 14)                # NS_OOS
TRV.addNode("N26", 52, 12)                # 3_S
TRV.addNode("N27", 54, 6)                 # 5_S
TRV.addNode("N28", 52, 8)                 # 7_S
TRV.addNode("N29", 45, 8)                 # 9_S
TRV.addNode("N30", 43, 10)                # 11_S
TRV.addNode("N31", 50, 10)                # 13_S
TRV.addNode("N32", 48, 12)                # 15_S
TRV.addNode("N33", 38, 12)                # 17_S
TRV.addNode("N34", 36, 10)                # 19_S
TRV.addNode("N35", 38, 8)                 # 21_S
TRV.addNode("N36", 36, 6)                 # 23_S

# =========================================== AF - Definitions ========================================================

# Define Southern (Low MP) Origins
TRV.addNode("N37", 90, 1, label_color='white', voffset=.4, hoffset=-3)             # NS Horn Track 1
TRV.addNode("N38", 84, 1)                                                          # y1e_AF
TRV.addNode("N39", 90, 3.5, label_color='white', voffset=.4, hoffset=-3)           # NS Horn Track 2
TRV.addNode("N40", 90, 6, label_color='white', voffset=.4, hoffset=-3)             # NS Horn Track 3
TRV.addNode("N41", 90, 8, label_color='white', voffset=.4, hoffset=-3)             # Ex Main 3
TRV.addNode("N42", 90, 10, label_color='white', voffset=.4, hoffset=-3)            # Ex Main 2
TRV.addNode("N43", 90, 12, label_color='white', voffset=.4, hoffset=-3)            # Ex Main 1
TRV.addNode("N44", 74, 14)                                                         # NS_org_AF
TRV.addNode("N45", 90, 14, label_color='white', voffset=.4, hoffset=-3)            # NS_yard
TRV.addNode("N46", 68, 14)                                                         # Setoff_org_AF
TRV.addNode("N47", 61, 14)                                                         # Setoff Track

# Define Switches
TRV.addNode("N48", 86.5, 3.5)                 # 1_S_AF
TRV.addNode("N49", 84, 6)                     # 3_S_AF
TRV.addNode("N50", 82, 6)                     # 5_S_AF
TRV.addNode("N51", 79, 6)                     # 6_S_AF
TRV.addNode("N52", 80, 8)                     # 7_S_AF
TRV.addNode("N53", 80, 10)                    # 9_S_AF
TRV.addNode("N54", 78, 12)                    # 11_S_AF
TRV.addNode("N55", 78, 8)                     # 13_S_AF
TRV.addNode("N56", 76, 10)                    # 19_S_AF
TRV.addNode("N57", 75, 10)                    # 21_S_AF
TRV.addNode("N58", 73, 8)                     # 23_S_AF
TRV.addNode("N59", 74, 10)                    # 25_S_AF
TRV.addNode("N60", 72, 12)                    # 27_S_AF
TRV.addNode("N61", 72, 12)                    # 29_S_AF
TRV.addNode("N62", 71, 12)                    # 31_S_AF
TRV.addNode("N63", 69, 10)                    # 33_S_AF
TRV.addNode("N64", 70, 12)                    # 35_S_AF
TRV.addNode("N65", 68, 10)                    # 37_S_AF
TRV.addNode("N66", 66, 12)                    # 39_S_AF
TRV.addNode("N67", 70, 8)                     # 41_S_AF
TRV.addNode("N68", 68, 6)                     # 43_S_AF
TRV.addNode("N69", 67, 10)                    # 45_S_AF
TRV.addNode("N70", 65, 8)                     # 47_S_AF

# Add Destinations
TRV.addNode("N71", 60, 12)                    # Main 0_AF
TRV.addNode("N72", 60, 10)                    # Main 1_AF
TRV.addNode("N73", 60, 8)                     # Main 2_AF
TRV.addNode("N74", 60, 6)                     # Main 3_AF

TRV.addNode("N75", 21, 14)                                      # Remove_main_1
TRV.addNode("N76", 19, 12)                                      # 0_2_RO
TRV.addNode("N77", 30, 14, label_color='white', voffset=.7, hoffset=1)    # RO_Slaters_Main_1_0
TRV.addNode("N78", 50, 14)                                      # RO_Slaters_Main_1_1
TRV.addNode("N79", 43, 12)
TRV.addNode("N80", 45, 14)
TRV.addNode("N81", 75, 14)
TRV.addNode("N82", 77, 12)
TRV.addNode("N83", 80, 14)
TRV.addNode("N84", 82, 12)
TRV.addNode("N85", 68, 12)
TRV.addNode("N86", 66, 10)
TRV.addNode("N87", 84, 8)
TRV.addNode("N88", 82, 10)
TRV.addNode("N89", 77, 14)
TRV.addNode("N90", 79, 16)
TRV.addNode("N91", 90, 16, label_color='white', voffset=.4, hoffset=-3)
TRV.addNode("N92", 22, 12)
TRV.addNode("N93", 23, 16)
TRV.addNode("N94", 42, 16)
TRV.addNode("N95", 37, 16)
TRV.addNode("N96", 35, 18)
TRV.addNode("N97", 32, 18)
TRV.addNode("N98", 40, 14)
TRV.addNode("N99", 47, 16)
TRV.addNode("N100", 49, 14)
TRV.addNode("N101", 34, 8)
TRV.addNode("N102", 28, 8)
TRV.addNode("N103", 24, 14)
TRV.addNode("N104", 30, 16, label_color='white', voffset=.7, hoffset=1)
TRV.addNode("N105", 66, 14)  # Setoff_org_AF
TRV.addNode("N106", 64, 16)  # Setoff_org_AF


# Define Links
TRV.addLink("L0", "N4", "N8", length=20)
TRV.addLink("L1", "N8", "N11", length=20)
TRV.addLink("L2", "N11", "N76", length=20)
TRV.addLink("L3", "N5", "N12", length=20)
TRV.addLink("L4", "N12", "N9", length=20)
TRV.addLink("L5", "N9", "N10", length=20)
TRV.addLink("L6", "N10", "N13", length=20)
TRV.addLink("L7", "N13", "N1", length=20)
TRV.addLink("L8", "N12", "N6", length=20)
TRV.addLink("L9", "N6", "N15", length=20)
TRV.addLink("L10", "N15", "N14", length=20)
TRV.addLink("L11", "N14", "N102", length=20)
TRV.addLink("L12", "N15", "N7", length=20)
TRV.addLink("L13", "N7", "N3", length=20)

# Define X-Overs
TRV.addLink("L14", "N8", "N9", length=20)
TRV.addLink("L15", "N10", "N11", length=20)
TRV.addLink("L16", "N13", "N14", length=20)

# Track Segments
TRV.addLink("L17", "N20", "N25", length=50)                        # 17
TRV.addLink("L18", "N25", "N26", length=50)                        # 18
TRV.addLink("L19", "N21", "N26", length=50)                        # 19
TRV.addLink("L20", "N26", "N32", length=50)                        # 20
TRV.addLink("L21", "N33", "N16", length=50)                        # 21
TRV.addLink("L22", "N22", "N31", length=50)                        # 22
TRV.addLink("L23", "N31", "N30", length=50)                        # 23
TRV.addLink("L24", "N30", "N34", length=50)                        # 24
TRV.addLink("L25", "N34", "N2", length=50)  # 25
TRV.addLink("L26", "N23", "N28", length=50)                        # 26
TRV.addLink("L27", "N28", "N29", length=50)                        # 27
TRV.addLink("L28", "N29", "N35", length=50)                        # 28
TRV.addLink("L29", "N101", "N35", length=50)                       # 29
TRV.addLink("L30", "N24", "N27", length=50)                        # 30
TRV.addLink("L31", "N27", "N36", length=50)                        # 31
TRV.addLink("L32", "N36", "N19", length=50)                        # 32

# Cross Overs
TRV.addLink("L33", "N31", "N32", length=20)                        # 33
TRV.addLink("L34", "N27", "N28", length=20)                        # 34
TRV.addLink("L35", "N29", "N30", length=20)                        # 35
TRV.addLink("L36", "N33", "N34", length=20)                        # 36
TRV.addLink("L37", "N35", "N36", length=20)                        # 37

# Define links between Values
# Crossovers
TRV.addLink("L38", "N48", "N49", length=50)                        # 38
TRV.addLink("L39", "N50", "N52", length=50)                        # 39
TRV.addLink("L40", "N53", "N54", length=50)                        # 40
TRV.addLink("L41", "N55", "N56", length=50)                        # 41
TRV.addLink("L42", "N57", "N58", length=50)                        # 42
TRV.addLink("L43", "N59", "N61", length=50)                        # 43
TRV.addLink("L44", "N62", "N63", length=50)                        # 44
TRV.addLink("L45", "N65", "N66", length=50, voffset=.2)  # 45
TRV.addLink("L46", "N67", "N68", length=50)                        # 46
TRV.addLink("L47", "N69", "N70", length=50)                        # 47

# Yard Segments
TRV.addLink("L48", "N37", "N38", length=50)                        # 48
TRV.addLink("L49", "N38", "N51", length=50)                        # 49
TRV.addLink("L50", "N39", "N48", length=50)                        # 50
TRV.addLink("L51", "N44", "N60", length=50)                        # 51
TRV.addLink("L52", "N45", "N44", length=50)                        # 52
TRV.addLink("L53", "N47", "N46", length=50)                        # 53
TRV.addLink("L54", "N64", "N46", length=50)                        # 54

# Main 0 Segments
TRV.addLink("L55", "N43", "N54", length=50)                        # 55
TRV.addLink("L56", "N54", "N60", length=50)                        # 56
TRV.addLink("L57", "N60", "N61", length=50)                        # 57
TRV.addLink("L58", "N61", "N62", length=50)                        # 58
TRV.addLink("L59", "N62", "N64", length=50)                        # 59
TRV.addLink("L60", "N64", "N66", length=50)                        # 60
TRV.addLink("L61", "N66", "N71", length=50)                        # 61

# Main 1 Segments
TRV.addLink("L62", "N42", "N53", length=50)                        # 62
TRV.addLink("L63", "N53", "N56", length=50)                        # 63
TRV.addLink("L64", "N56", "N57", length=50)                        # 64
TRV.addLink("L65", "N57", "N59", length=50)                        # 65
TRV.addLink("L66", "N59", "N63", length=50)                        # 66
TRV.addLink("L67", "N63", "N65", length=50)                        # 67
TRV.addLink("L68", "N65", "N69", length=50)                        # 68
TRV.addLink("L69", "N69", "N72", length=50)                        # 69

# Main 2 Segments
TRV.addLink("L70", "N87", "N52", length=50)                        # 70
TRV.addLink("L71", "N52", "N55", length=50)                        # 71
TRV.addLink("L72", "N55", "N58", length=50)                        # 72
TRV.addLink("L73", "N58", "N67", length=50)                        # 73
TRV.addLink("L74", "N67", "N70", length=50)                        # 74
TRV.addLink("L75", "N70", "N73", length=50)                        # 75

# Main 3 Segments
TRV.addLink("L76", "N40", "N49", length=50)                        # 76
TRV.addLink("L77", "N49", "N50", length=50)                        # 77
TRV.addLink("L78", "N50", "N51", length=50)                        # 78
TRV.addLink("L79", "N51", "N68", length=50)                        # 79
TRV.addLink("L80", "N68", "N74", length=50)                        # 80

# ================================================= Existing Views ====================================================

TRV.addLink("L81", "N33", "N79", length=50)
TRV.addLink("L82", "N75", "N76", length=50)
TRV.addLink("L83", "N103", "N77", length=50)
TRV.addLink("L84", "N79", "N32", length=50)
TRV.addLink("L85", "N79", "N80", length=50)
TRV.addLink("L86", "N77", "N80", length=50)
TRV.addLink("L87", "N80", "N78", length=50)
TRV.addLink("L88", "N78", "N25", length=50)
TRV.addLink("L89", "N20", "N47", length=50)
TRV.addLink("L90", "N46", "N44", length=50)
TRV.addLink("L91", "N81", "N82", length=50)
TRV.addLink("L92", "N83", "N84", length=50)
TRV.addLink("L93", "N86", "N85", length=50)
TRV.addLink("L94", "N51", "N57", length=50)
TRV.addLink("L95", "N87", "N88", length=50)
TRV.addLink("L96", "N87", "N41", length=50)
TRV.addLink("L97", "N89", "N90", length=50)
TRV.addLink("L98", "N90", "N91", length=50)
TRV.addLink("L99", "N13", "N92", length=50)
TRV.addLink("L100", "N76", "N92", length=50)
TRV.addLink("L101", "N92", "N0", length=50)
TRV.addLink("L102", "N93", "N94", length=50)
TRV.addLink("L103", "N97", "N96", length=50)
TRV.addLink("L104", "N96", "N95", length=50)
TRV.addLink("L105", "N98", "N94", length=50)
TRV.addLink("L106", "N94", "N99", length=50)
TRV.addLink("L107", "N99", "N100", length=50)
TRV.addLink("L108", "N18", "N101", length=50)
TRV.addLink("L109", "N19", "N2", length=50)
TRV.addLink("L110", "N102", "N0", length=50)
TRV.addLink("L111", "N102", "N18", length=50)
TRV.addLink("L112", "N17", "N2", length=50)
TRV.addLink("L113", "N13", "N103", length=50)
TRV.addLink("L114", "N75", "N93", length=50)
TRV.addLink("L115", "N103", "N75", length=50)
TRV.addLink("L116", "N99", "N106", length=50)
TRV.addLink("L117", "N105", "N106", length=50)



# Determine if the Routes are open or closed on either side of RO interlocking
TRV.signal_attributes_high = {
    # Origin Values (color, position, opp end color)
    'RO_Existing 2': [TRV.LINKS[0].color, (3, 10.75), TRV.LINKS[2].color, True],
    'RO_Existing 3': [TRV.LINKS[3].color, (3, 8.75), TRV.LINKS[7].color, True],
}

TRV.signal_attributes_low = {
    # Destinations
    'RO_Temp Proposed 0': [TRV.LINKS[2].color, (22.5, 16.75), TRV.LINKS[0].color, True],
    'RO_Existing 1': [TRV.LINKS[2].color, (22.5, 14.75), TRV.LINKS[0].color, True],
    'RO_Existing 2': [TRV.LINKS[2].color, (22.5, 12.75), TRV.LINKS[0].color, True],
    'RO_Existing 3': [TRV.LINKS[7].color, (22.5, 10.75), TRV.LINKS[3].color, True],
    'RO_Proposed 2': [TRV.LINKS[11].color, (22.5, 8.75), TRV.LINKS[3].color, True],
    'RO_Proposed 3': [TRV.LINKS[13].color, (22.5, 6.75), TRV.LINKS[3].color, True]
}

# Determine if the Routes are open or closed on either side of Slater's interlocking
slaters_signals_high = {
    # Slaters RO (color, position, opp end color)
    'slaters_Proposed 0_0': [TRV.LINKS[86].color, (34, 12.75), TRV.LINKS[17].color, True],
    'slaters_Proposed 0_2': [TRV.LINKS[22].color, (34, 10.75), TRV.LINKS[19].color, True],
    'slaters_Proposed 1_0': [TRV.LINKS[26].color, (34, 8.75), TRV.LINKS[23].color, True],
    'slaters_Proposed 2_0': [TRV.LINKS[30].color, (34, 6.75), TRV.LINKS[27].color, True],
    'slaters_Proposed 3_0': [TRV.LINKS[33].color, (34, 4.75), TRV.LINKS[31].color, True]
}

TRV.signal_attributes_high.update(slaters_signals_high)

slaters_signals_low = {
    # AF to Slaters
    'slaters_OOS_NS_5': [TRV.LINKS[17].color, (54.5, 14.75), TRV.LINKS[86].color, True],
    'slaters_Proposed 0_1': [TRV.LINKS[19].color, (54.5, 12.75), TRV.LINKS[22].color, True],
    'slaters_Proposed 1_1': [TRV.LINKS[23].color, (54.5, 10.75), TRV.LINKS[26].color, True],
    'slaters_Proposed 2_1': [TRV.LINKS[27].color, (54.5, 8.75), TRV.LINKS[30].color, True],
    'slaters_Proposed 3_1': [TRV.LINKS[31].color, (54.5, 6.75), TRV.LINKS[33].color, True]
}

TRV.signal_attributes_low.update(slaters_signals_low)

# Determine if the Routes are open or closed on either side of AF interlocking
AF_signals_low = {
    # Origin Values (color, position)
    'AF_yard': [TRV.LINKS[98].color, (85, 16.75), 'yard', True],
    'AF_Main 0_1': [TRV.LINKS[53].color, (85, 14.75), TRV.LINKS[52].color, True],
    'AF_Main 1_1': [TRV.LINKS[56].color, (85, 12.75), TRV.LINKS[62].color, True],
    'AF_Main 2_1': [TRV.LINKS[63].color, (85, 10.75), TRV.LINKS[70].color, True],
    'AF_Main 3_1': [TRV.LINKS[71].color, (85, 8.75), 'yard', True],
    'AF_NS Horn Track 3': [TRV.LINKS[77].color, (85, 6.75), 'yard', True],
    'AF_NS Horn Track 2': [TRV.LINKS[51].color, (85, 4.5), 'yard', True],
    'AF_NS Horn Track 1': [TRV.LINKS[49].color, (85, 2), 'yard', True]
}

AF_signals_low_high = {
    # Destinations
    'AF_Setoff Track': [TRV.LINKS[55].color, (63, 12.75), TRV.LINKS[61].color, True],
    'AF_Main 0_2': [TRV.LINKS[62].color, (63, 10.75), TRV.LINKS[56].color, True],
    'AF_Main 1_2': [TRV.LINKS[70].color, (63, 8.75), TRV.LINKS[63].color, True],
    'AF_Main 2_2': [TRV.LINKS[76].color, (63, 6.75), TRV.LINKS[71].color, True],
    'AF_Main 3_2': [TRV.LINKS[80].color, (63, 4.75), TRV.LINKS[77].color, True]
}

TRV.signal_attributes_low.update(AF_signals_low)
TRV.signal_attributes_high.update(AF_signals_low_high)

# Define Interlocking breaks
TRV.breaks.append(2)
TRV.breaks.append(24)
TRV.breaks.append(34)
TRV.breaks.append(57)
TRV.breaks.append(63)
TRV.breaks.append(88.5)

# Match the links in slaters to their values in other areas
TRV.NODES[16].color = TRV.NODES[0].color  # RO-Slaters Main 0
TRV.NODES[17].color = TRV.NODES[1].color  # RO-Slaters Main 1
TRV.NODES[18].color = TRV.NODES[2].color  # RO-Slaters Main 2
TRV.NODES[19].color = TRV.NODES[3].color  # RO-Slaters Main 3

TRV.LINKS[22].color = TRV.LINKS[2].color     # Slaters 0_3 = RO Main 0
TRV.LINKS[26].color = TRV.LINKS[7].color     # Slaters 1_3 = RO Main 1
TRV.LINKS[13+17].color = TRV.LINKS[11].color   # Slaters 2_3 = RO Main 2
TRV.LINKS[16+17].color = TRV.LINKS[13].color   # Slaters 3_2 = RO Main 3

TRV.NODES[5+16].color = TRV.NODES[34+37].color  # RO-Slaters Main 0
TRV.NODES[6+16].color = TRV.NODES[35+37].color  # RO-Slaters Main 1
TRV.NODES[7+16].color = TRV.NODES[36+37].color  # RO-Slaters Main 2
TRV.NODES[8+16].color = TRV.NODES[37+37].color  # RO-Slaters Main 3

TRV.LINKS[2+17].color = TRV.LINKS[23+39].color   # Slaters 0_0 = AF 0_6
TRV.LINKS[6+17].color = TRV.LINKS[31+39].color   # Slaters 1_0 = AF 1_7
TRV.LINKS[10+17].color = TRV.LINKS[37+39].color  # Slaters 2_0 = AF 2_5
TRV.LINKS[14+17].color = TRV.LINKS[42+39].color  # Slaters 3_0 = AF 3_4

TRV.title = "←L'Enfant                  RO (CFP 110.1/Sta. 325+00)                                     Slater's Lane (CFP 106.3/Sta. 130+00)                                    AF (CFP 104.3/Sta. 25+00)                    Franconia→"
