from fpdf import FPDF

# Create instance of FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)

# Title
pdf.cell(0, 10, "Mobley CMB Anomaly Cluster - Results Summary", 0, 1, "C")

pdf.ln(10)
pdf.set_font("Arial", "", 12)

# Summary text
summary_text = """
Total Pixels: 50,331,648
Anomalous Pixels: 153,122
Percentage Anomalous: 0.304%
Mean (μ): 1.2127e-12
Std Dev (σ): 1.0834e-04
σ Range: -17.13 → +16.25
Nside: 2048
"""

pdf.multi_cell(0, 8, summary_text)

# Sample coordinates
pdf.ln(5)
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 8, "Sample Anomalous Pixel Coordinates (θ, φ in deg):", 0, 1)
pdf.set_font("Arial", "", 12)
coords = [
    (98.8144, 87.7841), (97.8061, 87.7613), (98.7245, 87.7613),
    (97.7273, 87.7384), (98.6364, 87.7384), (99.5455, 87.7384),
    (96.7500, 87.7156), (97.6500, 87.7156), (98.5500, 87.7156),
    (99.4500, 87.7156)
]
for t, p in coords:
    pdf.cell(0, 8, f"{t:.4f}, {p:.4f}", 0, 1)

# Save PDF
pdf.output("Mobley_CMB_Results_Summary.pdf")
print("PDF generated successfully!")
