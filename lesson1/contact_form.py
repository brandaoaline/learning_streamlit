import streamlit as st

st.header(":mailbox: Get in touch with me!")


# https://formsubmit.co/ for the endpoint of the forms
# ativation not performed

contact_form = """
    <form action="https://formsubmit.co/your@email.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your best E-mail" required>
        <textarea name="message" placeholder="Message"></textarea>
        <button type="submit">Send</button>
    </form>
"""

st.markdown(contact_form, unsafe_allow_html=True)


# Use local CSS file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
