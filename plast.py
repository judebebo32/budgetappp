import streamlit as st

# Function to calculate the mass of plasticizer and solvent
def calculate_masses(ps_mass, plasticizer_concentration):
    # Calculate mass of plasticizer
    plasticizer_mass = (plasticizer_concentration / 100) * ps_mass / (1 - (plasticizer_concentration / 100))
    
    # Calculate total mass of polystyrene and plasticizer
    total_solute_mass = ps_mass + plasticizer_mass
    
    # Calculate the mass of solvent needed to bring the total mass to 10 g
    solvent_mass = 10 - total_solute_mass
    
    return plasticizer_mass, solvent_mass

# Streamlit app
st.title("Plasticizer and Solvent Mass Calculator")

# Input fields
ps_mass = st.number_input("Enter the mass of polystyrene (in grams)", min_value=0.0, value=2.5)
plasticizer_concentration = st.number_input("Enter the plasticizer concentration (in %)", min_value=0.0, max_value=100.0, value=29.0)

# Calculate the required masses
if st.button("Calculate"):
    plasticizer_mass, solvent_mass = calculate_masses(ps_mass, plasticizer_concentration)
    
    # Display the results
    st.write(f"Mass of plasticizer needed: {plasticizer_mass:.2f} g")
    st.write(f"Mass of solvent (xylene) needed: {solvent_mass:.2f} g")

    st.write(f"To achieve a {plasticizer_concentration}% concentration, you need {plasticizer_mass:.2f} g of plasticizer and {solvent_mass:.2f} g of solvent (xylene) to bring the total mass to 10 g.")
