import streamlit as st



st.title("SAVINGS TRACKER")



pages = {
    "Home": [st.Page("navigation/Dashboard.py", title="Dashboard"),],
    "Month" : [
        st.Page("navigation/1_January.py", title="January"),
        st.Page("navigation/2_February.py", title="February"),
        st.Page("navigation/3_March.py", title="March"),
        st.Page("navigation/4_April.py", title="April"),
        st.Page("navigation/5_May.py", title="May"),
        st.Page("navigation/6_June.py", title="June"),
        st.Page("navigation/7_July.py", title="July"),
        st.Page("navigation/8_August.py", title="August"),
        st.Page("navigation/9_September.py", title="September"),
        st.Page("navigation/10_October.py", title="October"),
        st.Page("navigation/11_November.py", title="November"),
        st.Page("navigation/12_December.py", title="December")
    ],
  
}

pg = st.navigation(pages)
pg.run()