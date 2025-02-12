import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

def process_gst_reconciliation(tally_file, gstr_file):
    # Implement logic from Final_First_Task
    return "GST Reconciliation Report.xlsx", BytesIO()

def process_debit_note_reconciliation(debit_file, gstr_file):
    # Implement logic from DEBITNOTE
    return "Debit_Note_Reconciliation.xlsx", BytesIO()

def process_gst_summary(tally_file, debit_file, gstr_file):
    # Implement logic from gstdifference
    return "GST_Reconciliation_Summary.xlsx", BytesIO()

st.title("GST Reconciliation App")

st.sidebar.header("Upload Input Files")
tally_file = st.sidebar.file_uploader("Upload Tally Purchase Register", type=["xlsx"], key="tally")
debit_file = st.sidebar.file_uploader("Upload Debit Note Register", type=["xlsx"], key="debit")
gstr_file = st.sidebar.file_uploader("Upload GSTR-2B", type=["xlsx"], key="gstr")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("GST Reconciliation Report"):
        if tally_file and gstr_file:
            filename, filedata = process_gst_reconciliation(tally_file, gstr_file)
            st.download_button("Download Report", filedata, file_name=filename)
        else:
            st.warning("Please upload required files: Tally Purchase Register and GSTR-2B")

with col2:
    if st.button("Debit Note Reconciliation Report"):
        if debit_file and gstr_file:
            filename, filedata = process_debit_note_reconciliation(debit_file, gstr_file)
            st.download_button("Download Report", filedata, file_name=filename)
        else:
            st.warning("Please upload required files: Debit Note Register and GSTR-2B")

with col3:
    if st.button("GST Reconciliation Summary"):
        if tally_file and debit_file and gstr_file:
            filename, filedata = process_gst_summary(tally_file, debit_file, gstr_file)
            st.download_button("Download Report", filedata, file_name=filename)
        else:
            st.warning("Please upload required files: Tally Purchase Register, Debit Note Register, and GSTR-2B")
            