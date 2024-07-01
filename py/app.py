import streamlit as st
import subprocess
import os
from generate_diagram import main

def run_generate_diagram(output_filename, direction, title, cluster_name, connections):
    try:
        main(output_filename, direction, title, cluster_name, connections)
        st.success(f"Diagram generated successfully: {output_filename}")
        st.image(output_filename)
    except Exception as e:
        st.error(f"Error generating diagram: {e}")

st.title("Salesforce Environment Generator")

output_filename = st.text_input("Output Filename (with extension, e.g., diagram.png)", "sf_env.png")
direction = st.selectbox("Direction", ["LR", "TB", "BT", "RL"], index=0)
title = st.text_input("Title", "Environments")
cluster_name = st.text_input("Cluster Name", "CRM")

st.markdown("#### Define Connections (one per line, e.g., 'sf_st >> sf_sit')")
connections_input = st.text_area( label="Connections", value="sf_st >> sf_sit >> sf_uat >> sf_staging >> sf_PROD\nsf_sit >> dev_int\nsf_uat >> QA_int\nsf_staging >> QA_int\nsf_PROD >> PROD_int", height=200)

if st.button("Generate Diagram"):
    connections = connections_input.split('\n')
    run_generate_diagram(output_filename, direction, title, cluster_name, connections)
