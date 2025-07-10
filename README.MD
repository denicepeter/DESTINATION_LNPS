# Automated LNP Synthesis Protocol – Opentrons Flex

This script automates the scale-up synthesis of lipid nanoparticles using the Opentrons Flex liquid handling robot. It involves precise dispensing of lipids (SM-102, DSPC, Cholesterol, DMG-PEG, DSPE-PEG) and mixing with ethanol and aqueous buffers.

#Protocol Summary
- Platform: Opentrons Flex
- API Level: 2.17
- Labware: 96-well deep plates, reservoirs, tube racks, etc.
- Functions: Automated pipetting, mixing, scale-up nanoparticle formulation

#Files
- `scaleup_dspe_maleimide.py`: The main protocol script
- `README.md`: Description and usage guide

#Usage
To run this protocol:
1. Open Opentrons App.
2. Upload this `.py` file under the "Protocol" section.
3. Set up your deck layout as defined in the script.
4. Run simulation or execute on your robot.

Author
DESTINATION Lab @ UTEP  
Denice Peter Rout, PhD Student
Mario Mata, MS Student BME

## 📄 License
This project is open-source. Feel free to use and modify with attribution.
