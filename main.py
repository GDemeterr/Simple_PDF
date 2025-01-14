from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto="False", margin=0)
df = pd.read_csv("topics.csv")


for index, row in df.iterrows():

    pdf.add_page()

    # Set the header

    pdf.set_font(family="TIMES", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"],
             ln=1, align="L")
    pdf.line(10, 21, 200, 21)

    for i in range(31, 288, 10):
        pdf.line(10, i, 200, i)

    # Set the footer
    pdf.ln(264)
    pdf.set_font(family="TIMES", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"],
             ln=1, align="R")

    for i in range(row["Pages"]-1):
        pdf.add_page()

        for i in range(10, 288, 10):
            pdf.line(10, i, 200, i)

        # Set the footer
        pdf.ln(276)
        pdf.set_font(family="TIMES", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"],
                 ln=1, align="R")


pdf.output("output.pdf")