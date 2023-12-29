import streamlit as st
st.set_page_config(page_title='cats')
st.markdown("## Types Of Cats")
col1,col2=st.columns(2)
with col1:
  st.subheader("persian Cat")
  st.image("./persian.jpg.jpg",width=300,caption="persian cat",use_column_width=True)
  st.write("persian cats are Cute")
with col2:
  st.subheader("ragdoll Cat")
  st.image("./ragdoll.jpg",width=300,caption="ragdoll cat",use_column_width=True)
  st.write("ragdoll cats are Cute")
  
