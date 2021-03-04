class Accounting {
    public static double valueOfSupply;
    public static double vatRate;
    public static double expenseRate;

    public static void print() {
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

public class AccountingClassApp {
    public static void main(String[] args){
        Accounting.valueOfSupply = 10000.0;
        Accounting.vatRate = 0.1;
        Accounting.expenseRate = 0.3;
        Accounting.print();
    }

}
