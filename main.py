from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

data_frame = pd.read_csv("topics.csv")

for index, row in data_frame.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="L",
             ln=1, border=0)
    pdf.line(10, 21, 200, 21)
    print(row['Topic'])

pdf.output("output.pdf")
