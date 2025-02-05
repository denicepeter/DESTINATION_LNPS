from opentrons import protocol_api
 
requirements = {
    'robotType': 'Flex',
    'apiLevel': '2.17'
}
 
# Metadata
metadata = {
    'protocolName': 'LNP no triplicates (Plate Mapping Ethanol Volumes)',
    'author': 'Denice Peter',
    'description': 'Protocol for synthesizing lipid nanoparticles using Opentron Flex robot'
}
 
def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_1 = protocol.load_labware(
            load_name="corning_96_wellplate_360ul_flat",
            location="D1")
 
    plate_2 = protocol.load_labware(
            load_name="corning_96_wellplate_360ul_flat",
            location="D2")
 
    tiprack_left_1 = protocol.load_labware(
            load_name="opentrons_flex_96_filtertiprack_50ul",
            location="A1")
 
    tiprack_left_2 = protocol.load_labware(
            load_name="opentrons_flex_96_filtertiprack_50ul",
            location="A2")
 
    tiprack_right_1 = protocol.load_labware(
            load_name="opentrons_flex_96_filtertiprack_200ul",
            location="B1")
 
    tiprack_right_2 = protocol.load_labware(
            load_name="opentrons_flex_96_filtertiprack_200ul",
            location="B2")
 
    tiprack_right_3 = protocol.load_labware(
            load_name="opentrons_flex_96_filtertiprack_200ul",
            location="C1")
 
    tiprack_right_4 = protocol.load_labware(
            load_name="opentrons_flex_96_filtertiprack_200ul",
            location="C2")
 
    tube_rack = protocol.load_labware(
            load_name="opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap",
            location="B3")
 
    reservoir = protocol.load_labware(
            load_name="nest_12_reservoir_15ml",
            location="C3")
 
    trash = protocol.load_trash_bin("A3")
 
    # Pipettes
    left_pipette = protocol.load_instrument(
        instrument_name="flex_1channel_1000",
        mount="left",
        tip_racks=[tiprack_left_1])
 
    right_pipette = protocol.load_instrument(
        instrument_name="flex_8channel_1000",
        mount="right",
        tip_racks=[tiprack_right_1, tiprack_right_2, tiprack_right_3, tiprack_right_4])
 
    sm_102 = tube_rack.wells_by_name()['A4']
    dspc = reservoir.wells_by_name()['A7']
    cholesterol = tube_rack.wells_by_name()['A1']
    dmg_peg = tube_rack.wells_by_name()['A2']
    ethanol = tube_rack.wells_by_name()['A3']
    aquous_1 = reservoir.wells_by_name()['A1']
    aquous_2 = reservoir.wells_by_name()['A2']
    lnp_output = plate_1.rows()
    lipid = plate_2.rows()
 
    right_pipette.pick_up_tip()
    right_pipette.distribute(150, aquous_1, [well for row in lnp_output for well in row[:4]], blow_out=True, new_tip='never')
    right_pipette.drop_tip()

    left_pipette.pick_up_tip()
    left_pipette.distribute(7, sm_102, [well for row in lipid for well in row[:4]], air_gap=7, blow_out=True, new_tip='never')
    left_pipette.drop_tip()
 
    left_pipette.pick_up_tip()
    for row in lipid[:4]:
        for well in row[:4]:
            left_pipette.aspirate(10, cholesterol)
            left_pipette.dispense(10, well)
    left_pipette.drop_tip()
 
    left_pipette.pick_up_tip()
    for row in lipid[4:]:
        for well in row[:4]:
            left_pipette.aspirate(15, cholesterol)
            left_pipette.dispense(15, well)
    left_pipette.drop_tip()

    water_volumes = [
        14, 13, 12, 11,
        9, 8, 7, 6,
        13, 12, 11, 10,
        8, 7, 6, 5,
        12, 11, 10, 9,
        7, 6, 5, 4, 
        11, 10, 9, 8, 
        6, 5, 4, 3 
        ]

    left_pipette.distribute(water_volumes, ethanol, plate_2.columns()[:4])
 
    left_pipette.pick_up_tip()
    for well in lipid[0][:4]:
        left_pipette.aspirate(12, dmg_peg)
        left_pipette.dispense(12, well)
 
    for well in lipid[4][:4]:
        left_pipette.aspirate(12, dmg_peg)
        left_pipette.dispense(12, well)
    left_pipette.drop_tip()

    left_pipette.pick_up_tip()
    for well in lipid[1][:4]:
        left_pipette.aspirate(13, dmg_peg)
        left_pipette.dispense(13, well)

    for well in lipid[5][:4]:
        left_pipette.aspirate(13, dmg_peg)
        left_pipette.dispense(13, well)
    left_pipette.drop_tip()

    left_pipette.pick_up_tip()
    for well in lipid[2][:4]:
        left_pipette.aspirate(14, dmg_peg)
        left_pipette.dispense(14, well)

    for well in lipid[6][:4]:
        left_pipette.aspirate(14, dmg_peg)
        left_pipette.dispense(14, well)
    left_pipette.drop_tip()

    left_pipette.pick_up_tip()
    for well in lipid[3][:4]:
        left_pipette.aspirate(15, dmg_peg)
        left_pipette.dispense(15, well)

    for well in lipid[7][:4]:
        left_pipette.aspirate(15, dmg_peg)
        left_pipette.dispense(15, well)
    left_pipette.drop_tip()

    right_pipette.transfer(7, dspc, plate_2.columns_by_name()['1'])
    right_pipette.transfer(8, dspc, plate_2.columns_by_name()['2'])
    right_pipette.transfer(9, dspc, plate_2.columns_by_name()['3'])
    right_pipette.transfer(10, dspc, plate_2.columns_by_name()['4'])
