

from breezypythongui import EasyFrame
Tax = 0.40
standardz = 6000.0
Dependenttax = 1000.0


class TaxCalculator(EasyFrame):
    """Application window for the tax calculator."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title="Tax Calculator")

     
        self.addLabel(text="Gross income", row=0, column=0)
        self.incomeField = self.addFloatField(
            value=0.0, row=0, column=1, width=15)

     
        self.addLabel(text="Dependents", row=1, column=0)
        self.depField = self.addIntegerField(
            value=0, row=1, column=1, width=10)

     
        self.addButton(text="Compute", row=2, column=1,
                       columnspan=1,
                       command=self.computeTax)

      
        self.addLabel(text="Total Tax", row=3, column=0)
        self.taxField = self.addFloatField(
            value=0.0, row=3, column=1, width=15)

  
    def computeTax(self):
        """Obtains the data from the input field and uses
        them to compute the tax, which is sent to the
        output field."""
        number = self.incomeField.getNumber()
        dependents = self.depField.getNumber()
        result = (number - standardz - dependents*Dependenttax)*Tax
        self.taxField.setNumber(result)
        pass


def main():
    TaxCalculator().mainloop()


if __name__ == "__main__":
    main()
