import streamlit as st

# Set the title of the app
st.title("User Details Form")

# Create a form
with st.form("user_form"):
    st.header("Fill in your details")

    # Input fields
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0, step=1)
    bio = st.text_area("Short Bio")

    # Submit button
    submitted = st.form_submit_button("Submit")

# Display the submitted data
if submitted:
    st.success("Form submitted successfully!")
    st.write("### Submitted Details:")
    st.write(f"**Name:** {name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Age:** {age}")
    st.write(f"**Bio:** {bio}")