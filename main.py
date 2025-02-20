import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "c3d743ea-a3cc-4f20-981b-727cf67d1012"
FLOW_ID = "959da673-e784-469d-84bb-0ab179650a95"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "social_tantradnya" # The endpoint name of the flow


def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("SocialVyakhyana: From Likes to Logic")
    
    message = st.text_area("Post Type", placeholder="Enter the Post Type whose analysis you want to know..")
    
    if st.button("Analyze"):
        if not message.strip():
            st.error("Please enter a message")
            return
    
        try:
            with st.spinner("Analyzing... Please be patient as this might take some time"):
                response = run_flow(message)
            
            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))

if __name__ == "__main__":
    main()