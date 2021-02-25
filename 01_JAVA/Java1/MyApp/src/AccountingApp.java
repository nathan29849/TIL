public class AccountingApp {
    public static void main(String[] args){

        double valueOfSupply = Double.parseDouble(args[0]); // Replace 단축키 : command + r
        double vatRate = 0.1; // variable 설정 단축키 :  option + command + v
        double expenseRate = 0.3;
        double vat = valueOfSupply * vatRate;
        double total = valueOfSupply + valueOfSupply * vatRate;
        double expense = valueOfSupply * expenseRate;
        double income = valueOfSupply - expense;
        double devidend1 = income * 0.5;
        double devidend2 = income * 0.3;
        double devidend3 = income * 0.2;

        System.out.println("Value of supply : "+ valueOfSupply);
        System.out.println("VAT : "+ vat);
        System.out.println("Total : "+ total);
        System.out.println("Expense : "+ expense);
        System.out.println("Income : "+ income);
        System.out.println("Devidend 1 : "+ devidend1);
        System.out.println("Devidend 2 : "+ devidend2);
        System.out.println("Devidend 3 : "+ devidend3);
    }
}
