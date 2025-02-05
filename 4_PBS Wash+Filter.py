from opentrons import protocol_api

requirements = {
    'robotType': 'Flex',
    'apiLevel': '2.17'
}

# Metadata
metadata = {
    'protocolName': 'PBS',
    'author': 'Denice Peter',
    'description': 'Protocol for Distribution and Washing LNP using Opentron Flex robot'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate_1 = protocol.load_labware(
            load_name="corning_96_wellplate_360ul_flat",
            location="D1")

    plate_2 = protocol.load_labware(
            load_name="corning_96_wellplate_360ul_flat",
            location="D2")

    plate_3 = protocol.load_labware(
            load_name="analytical_96_wellplate_400ul",
            location="D3")

    tiprack_1000 = protocol.load_labware(
            load_name="opentrons_flex_96_filtertiprack_1000ul",
            location="B1")

    reservoir = protocol.load_labware(
            load_name="nest_12_reservoir_15ml",
            location="C3")

    trash = protocol.load_trash_bin("A3")

    right_pipette = protocol.load_instrument(
        instrument_name="flex_8channel_1000",
        mount="right",
        tip_racks=[tiprack_1000])

    pbs_1 = reservoir.wells_by_name()['A3']
    pbs_2 = reservoir.wells_by_name()['A4']
    pbs_3 = reservoir.wells_by_name()['A5']
    pbs_4 = reservoir.wells_by_name()['A6']
    lnp_output = plate_1.rows()  
    wash = plate_2.rows()

    right_pipette.pick_up_tip()
    right_pipette.distribute(200, pbs_1, [well for row in lnp_output for well in row[:4]], blow_out=True, new_tip='never')
    right_pipette.drop_tip()

    right_pipette.pick_up_tip()
    right_pipette.distribute(200, pbs_2, [well for row in wash for well in row[:4]], blow_out=True, new_tip='never')
    right_pipette.drop_tip()

    pbs_wash_3 = [well for col in range(5, 9) for well in plate_2.columns_by_name()[str(col)]]
    right_pipette.pick_up_tip()
    right_pipette.distribute(200, pbs_3, pbs_wash_3, blow_out=True, new_tip='never')
    right_pipette.drop_tip()

    pbs_wash_4 = [well for col in range(9, 13) for well in plate_2.columns_by_name()[str(col)]]
    right_pipette.pick_up_tip()
    right_pipette.distribute(200, pbs_4, pbs_wash_4, blow_out=True, new_tip='never')
    right_pipette.drop_tip()

    for col in range(1, 13):
        source_filter = plate_2.columns_by_name()[str(col)]
        dest_filter = plate_3.columns_by_name()[str(col)]
        right_pipette.transfer(250, source_filter, dest_filter, new_tip='always')