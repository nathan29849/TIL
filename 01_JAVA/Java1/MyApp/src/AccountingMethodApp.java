public class AccountingMethodApp {
    public static double valueOfSupply;
    public static double vatRate;
    private static double expenseRate;

    public static void main(String[] args){
        valueOfSupply = 10000.0;
        vatRate = 0.1;
        expenseRate = 0.3;
//        double vat = getVAT();
//        double total = getTotal();
//        double expense = getExpense();
        double income = getIncome();

//        double rate1 = 0.5;
//        double rate2 = 0.3;
//        double rate3 = 0.2;
        double[] dividendRates = new double[3];
        dividendRates[0] = 0.5;
        dividendRates[1] = 0.3;
        dividendRates[2] = 0.2;

        double dividend1 = income * dividendRates[0];
        double dividend2 = income * dividendRates[1];
        double dividend3 = income * dividendRates[2];


        print();
//        System.out.println("Devidend 1 : "+ devidend1);
//        System.out.println("Devidend 2 : "+ devidend2);
//        System.out.println("Devidend 3 : "+ devidend3);
        int i = 0;
        while (i < dividendRates.length) {
            System.out.println("Devidend : "+ dividendRates[i]*income);
            i = i + 1;
        }
    }

    private static void print() {
        System.out.println("Value of supply : "+ valueOfSupply); // 전역변수라 그대로 변수로 써도 됨.
        System.out.println("VAT : "+ getVAT());
        System.out.println("Total : "+ getTotal());
        System.out.println("Expense : "+ getExpense());
        System.out.println("Income : "+ getIncome());
    }

    private static double getIncome()  {
        return valueOfSupply - getExpense();
    }

    private static double getExpense() {
        return valueOfSupply * expenseRate;
    }

    private static double getTotal() {
        return valueOfSupply + getVAT();
    }

    private static double getVAT() {
        return valueOfSupply * vatRate;
    }


}
