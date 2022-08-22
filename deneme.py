import streamlit as st

import time
i = 0
while True:
    st.write(i)
    i=i+1
    time.sleep(1)
    if i == 2000:
        break

