import streamlit as st
import requests

st.set_page_config(page_title="Shipment Tracker", page_icon="📦")
st.title("📦 Real-Time Shipment Tracking")

st.write("Submit your tracking details below to monitor delivery status.")

# Input fields
tracking_id = st.text_input("Enter Tracking ID", max_chars=50)
carrier = st.text_input("Enter Carrier Name", max_chars=50)

# Webhook URL (replace with your actual n8n URL)
WEBHOOK_URL = "https://your-n8n-url/webhook/track-shipment"

# On button click
if st.button("Submit to Track"):
    if tracking_id and carrier:
        payload = {
            "tracking_id": tracking_id,
            "carrier": carrier
        }

        try:
            response = requests.post(WEBHOOK_URL, json=payload)

            if response.status_code == 200:
                st.success("✅ Data successfully sent to n8n!")
            else:
                st.error(f"❌ Failed with status: {response.status_code}")
        except Exception as e:
            st.error(f"🚨 Error: {e}")
    else:
        st.warning("⚠️ Please fill in all fields.")
