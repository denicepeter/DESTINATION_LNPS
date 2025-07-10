from opentrons import protocol_api
 
requirements = {
    'robotType': 'Flex',
    'apiLevel': '2.17'
}
 
metadata = {
    'protocolName': 'ScaleUp LNP synthesis DSPE Maleimide',
    'author': 'DESTINATION',
    'description': 'LNP synthesis ScaleUp'
}
 
def run(protocol: protocol_api.ProtocolContext):
    plate_1 = protocol.load_labware(
        load_name="greiner_96_deepwell_2000ul",
        location="D1")

    plate_2 = protocol.load_labware(
        load_name="cytiva_96_wellplate_350ul",
        location="D3")

    reservoir = protocol.load_labware(
        load_name="nest_12_reservoir_15ml",
        location="D2")

    tuberack = protocol.load_labware(
        load_name="opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap",
        location="C3")
    
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
 
    trash = protocol.load_trash_bin("A3")
 
    left_pipette = protocol.load_instrument(
        instrument_name="flex_1channel_50",
        mount="left",
        tip_racks=[tiprack_left_1])
 
    right_pipette = protocol.load_instrument(
        instrument_name="flex_8channel_1000",
        mount="right",
        tip_racks=[tiprack_right_1, tiprack_right_2])
 
    sm_102 = tuberack.wells_by_name()['A1']
    dspc = tuberack.wells_by_name()['A2']
    cholesterol = tuberack.wells_by_name()['A3']
    dmg_peg = tuberack.wells_by_name()['A4']
    dspe_peg = tuberack.wells_by_name()['A5']
    ethanol = reservoir.wells_by_name()['A1']
    aqu1 = reservoir.wells_by_name()['A2']
    
    left_pipette.pick_up_tip()
    for col in plate_1.columns()[:5]:
        for well in col:
            left_pipette.aspirate(3.5, sm_102)
            left_pipette.dispense(3.5, well)
            left_pipette.blow_out(well.top())
    left_pipette.drop_tip()

    left_pipette.pick_up_tip()
    for col in plate_1.columns()[:5]:
        for well in col:
            left_pipette.aspirate(3.2, dspc)
            left_pipette.dispense(3.2, well)
            left_pipette.blow_out(well.top())
    left_pipette.drop_tip()

    left_pipette.pick_up_tip()
    for col in plate_1.columns()[:5]:
        for well in col:
            left_pipette.aspirate(7.21, cholesterol)
            left_pipette.dispense(7.21, well)
            left_pipette.blow_out(well.top())  
    left_pipette.drop_tip()

    left_pipette.pick_up_tip()
    for col in plate_1.columns()[:5]:
        for well in col:
            left_pipette.aspirate(20.16, dmg_peg)
            left_pipette.dispense(20.16, well)
            left_pipette.blow_out(well.top())  
    left_pipette.drop_tip()

    left_pipette.pick_up_tip()
    for col in plate_1.columns()[:5]:
        for well in col:
            left_pipette.aspirate(5, dspe_peg)
            left_pipette.dispense(5, well)
            left_pipette.blow_out(well.top())  
    left_pipette.drop_tip()

    for col in plate_1.columns()[:5]:
        right_pipette.pick_up_tip()
        for well in col:
            right_pipette.aspirate(11, ethanol)
            right_pipette.dispense(11, well)
            right_pipette.mix(2, 30, well)
        right_pipette.drop_tip()
    
    for col in plate_1.columns()[:5]:
        right_pipette.pick_up_tip()
        for well in col:
            right_pipette.aspirate(150, well)
            right_pipette.dispense(150, aqu1)
            right_pipette.mix(15, 150, aqu1, rate=2.5)
        right_pipette.drop_tip()
