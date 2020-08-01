

from breezypythongui import EasyFrame
Tax = 0.20
standardz = 10000.0
Dependenttax = 3000.0


class TaxCalculator(EasyFrame):
    """Application window for the tax calculator."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title="Tax Calculator")

        # Label and field for the income
        # (self.incomeField)
        self.addLabel(text="Gross income", row=0, column=0)
        self.incomeField = self.addFloatField(
            value=0.0, row=0, column=1, width=15)

        # Label and field for the number of dependents
        # (self.depField)
        self.addLabel(text="Dependents", row=1, column=0)
        self.depField = self.addIntegerField(
            value=0, row=1, column=1, width=10)

        # The command button
        self.addButton(text="Compute", row=2, column=1,
                       columnspan=1,
                       command=self.computeTax)

        # Label and field for the tax
        # (self.taxField)
        self.addLabel(text="Total Tax", row=3, column=0)
        self.taxField = self.addFloatField(
            value=0.0, row=3, column=1, width=15)

    # The event handler method for the button
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
