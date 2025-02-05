from opentrons import protocol_api

requirements = {
    'robotType': 'Flex',
    'apiLevel': '2.17'
}

# Metadata
metadata = {
    'protocolName': 'LNP Wash',
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

    tiprack_right_1 = protocol.load_labware(
            load_name="opentrons_flex_96_filtertiprack_200ul",
            location="A1")

    tiprack_right_2 = protocol.load_labware(
            load_name="opentrons_flex_96_filtertiprack_200ul",
            location="A2")

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
        tip_racks=[tiprack_right_1, tiprack_right_2, tiprack_1000])

    pbs_1 = reservoir.wells_by_name()['A1']
    pbs_2 = reservoir.wells_by_name()['A2']
    pbs_3 = reservoir.wells_by_name()['A3']
    pbs_4 = reservoir.wells_by_name()['A4']
    lnp_output = plate_1.rows()  
    wash = plate_2.rows()

    for col in range(1, 5):
        source_1 = plate_1.columns_by_name()[str(col)]
        dest_1 = plate_2.columns_by_name()[str(col)]
        right_pipette.transfer(50, source_1, dest_1, mix_before=(2, 40), new_tip='always')

    source_2 = [str(i) for i in range(1, 5)]
    dest_2 = [str(i) for i in range(5, 9)]

    for src_col2, dest_col2 in zip(source_2, dest_2):
        source_wells2 = plate_1.columns_by_name()[src_col2]
        dest_wells2 = plate_2.columns_by_name()[dest_col2]
        right_pipette.transfer(50, source_wells2, dest_wells2, mix_before=(2, 40), new_tip='always')
        
    source_3 = [str(i) for i in range(1, 5)]
    dest_3 = [str(i) for i in range(9, 13)]

    for src_col3, dest_col3 in zip(source_3, dest_3):
        source_wells3 = plate_1.columns_by_name()[src_col3]
        dest_wells3 = plate_2.columns_by_name()[dest_col3]
        right_pipette.transfer(50, source_wells3, dest_wells3, mix_before=(2, 40), new_tip='always')

    


