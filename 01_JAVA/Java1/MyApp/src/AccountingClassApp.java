class Accounting {
    public double valueOfSupply;
    public double vatRate;
    public double expenseRate;

    public void print() {
        System.out.println("Value of supply : "+ valueOfSupply); // 전역변수라 그대로 변수로 써도 됨.
        System.out.println("VAT : "+ getVAT());
        System.out.println("Total : "+ getTotal());
        System.out.println("Expense : "+ getExpense());
        System.out.println("Income : "+ getIncome());
    }

    private  double getIncome()  {

        return valueOfSupply - getExpense();
    }

    private  double getExpense() {

        return valueOfSupply * expenseRate;
    }

    private  double getTotal() {

        return valueOfSupply + getVAT();
    }

    private  double getVAT() {

        return valueOfSupply * vatRate;
    }
}
//class Accounting2 {
//    public static double valueOfSupply;
//    public static double vatRate;
//    public static double expenseRate;
//
//    public static void print() {
//        System.out.println("Value of supply : "+ valueOfSupply); // 전역변수라 그대로 변수로 써도 됨.
//        System.out.println("VAT : "+ getVAT());
//        System.out.println("Total : "+ getTotal());
//        System.out.println("Expense : "+ getExpense());
//        System.out.println("Income : "+ getIncome());
//    }
//
//    private static double getIncome()  {
//
//        return valueOfSupply - getExpense();
//    }
//
//    private static double getExpense() {
//
//        return valueOfSupply * expenseRate;
//    }
//
//    private static double getTotal() {
//
//        return valueOfSupply + getVAT();
//    }
//
//    private static double getVAT() {
//
//        return valueOfSupply * vatRate;
//    }
//}

public class AccountingClassApp {
    public static void main(String[] args){
//        System.out.println("Account1");
//        Accounting1.valueOfSupply = 10000.0;
//        Accounting1.vatRate = 0.1;
//        Accounting1.expenseRate = 0.3;
//        Accounting1.print();
//
//        System.out.println();
//        System.out.println("Account2");
//        Accounting2.valueOfSupply = 30000.0;
//        Accounting2.vatRate = 0.3;
//        Accounting2.expenseRate = 0.1;
//        Accounting2.print();
        // instance (이때는 static을 class 내부에서는 사용하면 안됨! )
        Accounting a1 = new Accounting();
        a1.valueOfSupply = 100000.0;
        a1.vatRate = 0.1;
        a1.expenseRate = 0.3;
        a1.print();

        Accounting a2 = new Accounting();
        a2.valueOfSupply = 100000.0;
        a2.vatRate = 0.4;
        a2.expenseRate = 0.2;
        a2.print();

    }
}
