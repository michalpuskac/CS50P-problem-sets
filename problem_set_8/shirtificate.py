from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        # Add title at the top of the page
        self.set_font("Arial", size=24, style="B")
        self.cell(0, 10, "CS50 Shirtificate", ln=True, align="C")

def main():
    name = input("Name: ").strip()

    # Create a PDF instance
    pdf = Shirtificate(orientation="P", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    # Add the shirt image
    shirt_image_path = "shirtificate.png"  # This image exists in the same directory
    pdf.image(shirt_image_path, x=0, y=60, w=210)  # Centered horizontally (A4 -210mm)

    # Add the user's name
    pdf.set_xy(0, 150)  # Adjust position to overlay the shirt
    pdf.set_font("Arial", size=32, style="B")
    pdf.set_text_color(255, 255, 255)  # White text
    pdf.cell(0, 10, f"{name} took CS50", ln=True, align="C")

    # Output the PDF
    pdf.output("shirtificate.pdf")
    print("Shirtificate created successfully!")

if __name__ == "__main__":
    main()