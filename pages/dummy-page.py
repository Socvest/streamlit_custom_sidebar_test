import streamlit as st
from streamlit_custom_sidebar import CustomSidebarDefault
import streamlit_float # recommended


streamlit_float.float_init()

data_ = [
            {"index":0, "label":"Home Page", "page":"home-page", "href":"http://localhost:8501/"},
            {"index":1, "label":"Dummy Page", "page":"dummy-page", "icon":"ri-logout-box-r-line", "href":"http://localhost:8501/dummy-page"}
        ]

if "currentPage" not in st.session_state: # required as component will be looking for this in session state to change page via `switch_page`
    st.session_state["currentPage"] = data_[0] 
else:
    st.session_state["currentPage"] = data_[0] 


with st.container():
    defaultSidebar = CustomSidebarDefault(closeNavOnLoad=False, webMedium="streamlit-cloud", backgroundColor="brown", loadPageName=None, data=data_, LocalOrSessionStorage=1, serverRendering=False, webMedium="local") 
    defaultSidebar.load_custom_sidebar()
    defaultSidebar.change_page()
    
    streamlit_float.float_parent(css="top:-1000px;")
