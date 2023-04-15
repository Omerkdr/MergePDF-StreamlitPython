import streamlit as st
from PyPDF2 import PdfMerger, PdfReader, PdfFileWriter
import io

# Sayfa stil ayarları
st.set_page_config(
    page_title="APUS PDF Birleştirici",
    page_icon=":books:",
    layout="wide"
)

# APUS logosu ve başlık
col1, col2 = st.columns([0.3, 1])
with col1:
    st.image("apus_logo.png", width=100)
with col2:
    st.title("APUS PDF Birleştirici")

# Dosya yükleme alanı
st.write("")
st.write("")
pdf_files = st.file_uploader("Birleştirmek istediğiniz PDF dosyalarını yükleyin.", type=["pdf"], accept_multiple_files=True)

# Dosyaların birleştirilmesi ve indirme bağlantısının oluşturulması
if pdf_files:
    merger = PdfMerger()
    for pdf in pdf_files:
        file_contents = pdf.read()
        if len(file_contents) == 0:
            continue
        merger.append(PdfReader(io.BytesIO(file_contents)))

    output_buffer = io.BytesIO()
    merger.write(output_buffer)
    merged_pdf = output_buffer.getvalue()

    st.success("PDF dosyaları başarıyla birleştirildi!")
    st.download_button(label="Birleştirilmiş PDF'yi İndirin", data=merged_pdf, file_name="merged_pdf.pdf")
