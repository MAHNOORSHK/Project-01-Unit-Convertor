import streamlit as st
from pint import UnitRegistry

# Initialize unit registry
ureg = UnitRegistry()

# Streamlit UI Enhancements
st.set_page_config(page_title="Unit Converter", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        color: #ffffff;
    }
    .title {
        font-size: 32px;
        font-weight: bold;
        color: #0077B6;
        text-align: center;
    }
    .subheader {
        font-size: 24px;
        font-weight: bold;
        color: #468FAF;
        text-align: center;
    }
    .stButton>button {
        background-color: #0077B6;
        color: white;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to:", ["Home", "Unit Converter", "About", "Contact"])

if menu == "Home":
    st.markdown("<div class='title'>Unit Converter - Smart. Fast. Accurate</div>", unsafe_allow_html=True)
    st.markdown("<div class='subheader'>Convert Anything, Anytime</div>", unsafe_allow_html=True)
    st.write("Unit Converter allows you to seamlessly convert units for various categories including length, weight, time, volume, area, speed, pressure, energy, power, data storage, angle, force, density, and fuel economy.")
    st.image("images.png", use_container_width=True)

elif menu == "Unit Converter":
    st.markdown("<div class='title'>Unit Converter</div>", unsafe_allow_html=True)
    
    categories = [
        "Length", "Weight", "Time", "Volume", "Area", "Speed", "Pressure", 
        "Energy", "Power", "Data Storage", "Angle", "Force", "Density", "Fuel Economy"
    ]
    category = st.selectbox("Choose conversion type:", categories)

    def convert_units(value, from_unit, to_unit):
        try:
            return (value * ureg(from_unit)).to(to_unit).magnitude
        except Exception as e:
            return f"Error: {e}"

    units_dict = {
        "Length": ["meter", "kilometer", "mile", "foot", "inch", "centimeter", "yard"],
        "Weight": ["gram", "kilogram", "pound", "ounce", "ton"],
        "Time": ["second", "minute", "hour", "day"],
        "Volume": ["liter", "milliliter", "gallon"],
        "Area": ["square_meter", "square_foot", "acre"],
        "Speed": ["kilometer_per_hour", "mile_per_hour", "meter_per_second"],
        "Pressure": ["pascal", "bar", "psi"],
        "Energy": ["joule", "calorie", "kilowatt_hour"],
        "Power": ["watt", "horsepower"],
        "Data Storage": ["byte", "kilobyte", "megabyte", "gigabyte"],
        "Angle": ["degree", "radian"],
        "Force": ["newton", "dyne"],
        "Density": ["kilogram_per_cubic_meter", "gram_per_cubic_centimeter"],
        "Fuel Economy": ["kilometer_per_liter", "mile_per_gallon"]
    }
    
    col1, col2 = st.columns(2)
    from_unit = col1.selectbox("From:", units_dict[category])
    to_unit = col2.selectbox("To:", units_dict[category])
    
    value = st.number_input("Enter value:", min_value=0.0, format="%f")
    
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result} {to_unit}")

elif menu == "About":
    st.markdown("<div class='title'>About UniConvert</div>", unsafe_allow_html=True)
    st.write("Unit Converter is a comprehensive unit conversion tool designed to assist professionals, students, and general users in their daily calculations.")
    
    st.subheader("Why We Created This App")
    st.write("- **Efficiency**: Eliminates the hassle of manual unit conversion.")
    st.write("- **Accuracy**: Ensures precise calculations using reliable conversion data.")
    st.write("- **Convenience**: A single platform for all unit conversions.")
    
    st.subheader("How It Works")
    st.write("- Select the type of conversion.")
    st.write("- Input the value and choose the units.")
    st.write("- Click 'Convert' and get instant results!")

elif menu == "Contact":
    st.markdown("<div class='title'>Contact Information</div>", unsafe_allow_html=True)
    st.write("**Name:** Mahnoor")
    st.write("**Education:** MPhil in IT")
    st.write("**City:** Hyderabad")
    st.write("**Course:** GIAIC Q3")
    st.write("**Slot:** Sunday Afternoon")
    st.write("**LinkedIn:** [Mahnoor's LinkedIn](https://www.linkedin.com/in/mahnoor-shaikh/)")
    st.write("**GitHub:** [Mahnoor's GitHub](https://github.com/MAHNOORSHK/)")

# Footer
st.markdown("---")
st.caption("Copyright © 2025 Unit Converter | Built by Mahnoor - Q3 GIAIC Student")