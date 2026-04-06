import streamlit as st

st.title("🎬 Movie Ticket Booking System")

# Input
name = st.text_input("Enter Customer Name")

movie = st.selectbox("Select Movie", ["Avengers", "Kung Fu Panda", "Frozen"])

time = st.selectbox("Select Show Time", ["10:00 AM", "2:00 PM", "8:00 PM"])

seat = st.radio("Select Seat Type", ["Standard", "Premium"])

# Button
if st.button("Book Ticket"):
    try:
        if name == "":
            raise ValueError("Customer name cannot be empty!")

        st.success("✅ Booking Successful!")

        st.write("### Booking Information")
        st.write(f"""
        Customer Name : {name}  
        Movie Title   : {movie}  
        Show Time     : {time}  
        Seat Type     : {seat}
        """)

    except ValueError as e:
        st.error(f"❌ Error: {e}")

    except Exception as e:
        st.error(f"⚠ Unexpected Error: {e}")
