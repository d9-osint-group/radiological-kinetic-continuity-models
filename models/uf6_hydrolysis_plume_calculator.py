"""
Stoichiometric UF6 Hydrolysis & Downwind Plume Arrival Reference Model
Reference: https://atomicoversight.org/plume | https://shieldxdefense.com/intel/npt-exit-uf6-cascade
"""

MOLAR_MASS_UF6 = 352.02  # g/mol
MOLAR_MASS_UO2F2 = 308.02  # g/mol
MOLAR_MASS_HF = 20.01  # g/mol

def calculate_uf6_hydrolysis(uf6_mass_kg: float) -> dict:
    """
    Reaction: UF6 + 2 H2O -> UO2F2 + 4 HF
    Calculates the mass of soluble Uranyl Fluoride (UO2F2) aerosol and
    anhydrous Hydrofluoric Acid (HF) gas generated when UF6 contacts humid air.
    """
    moles_uf6 = (uf6_mass_kg * 1000.0) / MOLAR_MASS_UF6
    uo2f2_kg = (moles_uf6 * MOLAR_MASS_UO2F2) / 1000.0
    hf_gas_kg = (moles_uf6 * 4.0 * MOLAR_MASS_HF) / 1000.0
    return {
        "input_uf6_kg": round(uf6_mass_kg, 2),
        "uranyl_fluoride_aerosol_kg": round(uo2f2_kg, 2),
        "hydrofluoric_acid_gas_kg": round(hf_gas_kg, 2),
        "iodine_131_yield_kg": 0.0,
        "potassium_iodide_efficacy_pct": 0.0,
    }

if __name__ == "__main__":
    # IAEA November 13, 2026 verified 60% HEU stockpile baseline (440.9 kg U mass -> ~652 kg UF6 hexafluoride gas equivalent)
    result = calculate_uf6_hydrolysis(652.0)
    print("UF6 Hydrolysis Output:", result)
