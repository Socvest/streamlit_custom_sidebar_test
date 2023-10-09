import streamlit as st
from streamlit_custom_sidebar import CustomSidebarDefault
import streamlit_float # recommended

st.set_page_config(layout="wide", page_title="Home Page")


streamlit_float.float_init()

data_ = [
            {"index":0, "label":"Home Page", "page":"home-page", "href":"https://custom-sidebar.streamlit.app/"},
            {"index":1, "label":"Dummy Page", "page":"dummy-page", "icon":"ri-logout-box-r-line", "href":"https://custom-sidebar.streamlit.app/dummy-page"},
            {"index":3, "label":"Closed Nav Onload Page", "page":"closed-nav-onload", "icon":"ri-logout-box-r-line", "href":"https://custom-sidebar.streamlit.app/closed-nav-onload"}
        ]

if "currentPage" not in st.session_state: # required as component will be looking for this in session state to change page via `switch_page`
    st.session_state["currentPage"] = data_[0] 
else:
    st.session_state["currentPage"] = data_[0] 


with st.container():
    defaultSidebar = CustomSidebarDefault(closeNavOnLoad=False, webMedium="streamlit-cloud", backgroundColor="brown", loadPageName=None, data=data_, LocalOrSessionStorage=1, serverRendering=False) 
    defaultSidebar.load_custom_sidebar()
    defaultSidebar.change_page()
    
    streamlit_float.float_parent(css="position:fixed; top:-1000px;")


st.subheader("This is the Home Page")

js_el = '''
<script>
            let iframeScreenComp = window.parent.document.querySelectorAll('iframe[title="streamlit_session_browser_storage.st_session_browser_storage"]')
            iframeScreenComp[0].parentNode.style.display = "none";
</script>

'''
st.components.v1.html(js_el, height=0, width=0)


