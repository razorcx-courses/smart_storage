import streamlit as st
import streamlit.components.v1 as components

def run():
    # Page configuration
    st.set_page_config(
        page_title="Smart Storage Centre",
        page_icon="🏢",
        layout="wide"
    )

    # Custom CSS for better styling
    st.markdown("""
        <style>
        .main {
            padding: 0rem 1rem;
        }
        .stContainer {
            background-color: white;
            padding: 2rem;
            border-radius: 0.5rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        .header-container {
            background-color: #2563eb;
            padding: 2rem;
            color: white;
            border-radius: 0.5rem;
            margin-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header section
    with st.container():
        header = st.container(border=True)
        with header:
            st.title("Smart Storage Centre")
            col1, col2 = st.columns(2)
            with col1:
                st.write("3425 Airport Road, Penticton, BC, V2A 8X1")
                st.write("Email: smartstoragecanada@icloud.com")
            with col2:
                st.write("Bookings/Reservations: (844) 900-0737")
                st.write("Technical Support: (833) 257-0240")
                st.write("Gate Hours: 6:00 AM - 11:00 PM (daily)")

    # Main content
    main_content = st.container(border=True)
    with main_content:
        st.header("Smart Storage, Smarter Living")
        st.subheader("Secure, Convenient, and Easy Storage Solutions for Penticton")
        
        st.write("""
        At Smart Storage Centre, we understand that your belongings are more than just things – 
        they're part of your life story. That's why we've revolutionized self-storage with 
        cutting-edge security and unparalleled convenience.
        """)

    # Features in a styled container
    features_container = st.container(border=True)
    with features_container:
        st.subheader("Our Features")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("📱 State-of-the-art facility with app-controlled access")
            st.write("🚨 Responsive alarms and regular police presence")
            st.write("🔑 Digital key-sharing feature")
            st.write("✨ Clean, well-maintained facility")
        
        with col2:
            st.write("😊 Friendly, responsive customer service")
            st.write("💻 Flexible online booking")
            st.write("💲 Competitive pricing")
            st.write("🔒 24/7 security monitoring")

    # Storage Units in cards
    st.header("Storage Unit Sizes and Prices")
    unit_cols = st.columns(4)

    units = {
        "Small (4x8)": {
            "price": "C$99.00/month",
            "yearly": "C$1,069.20",
            "size": "32 sq ft",
            "description": "Comparable to an extra large hallway closet, ideal for twin mattress set, small dressers, TVs, cabinets, chairs, bookcases, tools, yard equipment, winter/summer tires, and bicycles."
        },
        "Medium (6.5x8)": {
            "price": "C$109.00/month",
            "yearly": "C$1,177.20",
            "size": "52 sq ft",
            "description": "Around the size of a large walk-in closet, ideal for studio apartment or one bedroom storage. Common uses include seasonal items, sporting gear, queen sized mattress, appliances, and home decluttering."
        },
        "Large (10x8)": {
            "price": "C$139.00/month",
            "yearly": "C$1,501.20",
            "size": "80 sq ft",
            "description": "Around half the size of a single car garage, perfect for storing larger items or one bedroom apartment contents. Ideal for king sized mattress sets, couches, entertainment center, major appliances."
        },
        "Extra Large (20x8)": {
            "price": "C$169.00/month",
            "yearly": "C$1,825.20",
            "size": "160 sq ft",
            "description": "Just a little smaller than a single car garage, fits contents of four rooms or three furnished bedrooms. Suitable for exercise equipment, bedroom sets, appliances, patio furniture, dining room sets."
        }
    }

    for col, (unit_name, details) in zip(unit_cols, units.items()):
        with col:
            unit_card = st.container(border=True)
            with unit_card:
                st.markdown(f"### {unit_name}")
                st.markdown(f"**Size:** {details['size']}")
                st.markdown(f"**Monthly:** {details['price']}")
                st.markdown(f"**Yearly:** {details['yearly']}")
                st.markdown("**Deposit:** C$25")
                with st.expander("Unit Details"):
                    st.write(details['description'])
                    
    # Locks
    lock_container = st.container(border=True)
    with lock_container:
        st.header("Lock Technology")
        components.iframe("https://player.vimeo.com/video/503547447?h=809754af53", height=360)
        
    # Features and Technology
    tech_container = st.container(border=True)
    with tech_container:
        st.header("Features and Technology")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("- Drive-Up Access: All units")
            st.write("- Doors: Roll-up doors")
            st.write("- Locks: Electronic locks")
            st.write("- Sensors: Motion sensors")
            st.write("- Keyless Entry: Via Noke App")
        
        with col2:
            st.write("- Digital Key Sharing: Available")
            st.write("- Video Surveillance: 24-hour")
            st.write("- Online Rentals and Payments: Available")
            st.write("- Contactless Move-Ins: Available")

    # Footer
    st.caption("© 2024 Smart Storage Centre. All rights reserved.")