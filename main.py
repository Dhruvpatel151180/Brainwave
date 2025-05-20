import streamlit as st

# Assuming app_doc.py and app_chat.py have functions that run their respective content
from app_doc import main_document
from app_chat import main_spreadsheet



# CSS for light blue box
custom_style = """
       <style>
       [data-testid="stSidebarHeader"] img{
            width:200px;
            height:35px; 
            
        }
       
       .stSidebar{
           width:350px !important;
       }
       [data-testid="stVerticalBlock"] {
        gap:12px !important;
       }
       .st-emotion-cache-1mi2ry5{
        padding-top:1rem;
        padding-bottom:1rem;
       }
       .st-emotion-cache-nok2kl h1{
       padding-top:0px;
       padding-bottom:1.25rem
       }
       ::-webkit-scrollbar {
         display: none;
       } 
       .st-emotion-cache-1gwvy71 {{
        padding: 0 1rem 0 !important;
       }}
       [data-testid="stSidebarUserContent"]{
        padding-bottom:0
       }
       </style>
   """

# custom CSS
st.sidebar.markdown(custom_style, unsafe_allow_html=True)


selected_app = st.sidebar.radio("Select an option:", ("Document Files", "Spreadsheet Files"))

# Run the appropriate app based on the selection
if selected_app == "Document Files":
    main_document()  # This will call the function from app_doc.py
elif selected_app == "Spreadsheet Files":
    main_spreadsheet()  # This will call the function from app_chat.py
