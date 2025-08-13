public class SalaryCalculator {
    public double salaryMultiplier(int daysSkipped) {
        return daysSkipped < 5 ? 1.0 : 0.85;
    }

    public int bonusMultiplier(int productsSold) {
        return productsSold < 20 ? 10 : 13;
    }

    public double bonusForProductsSold(int productsSold) {
        return productsSold * bonusMultiplier(productsSold);
    }

    public double finalSalary(int daysSkipped, int productsSold) {
        double potentialSalary = 1000.00 * salaryMultiplier(daysSkipped) + bonusForProductsSold(productsSold);
        return potentialSalary >= 2000 ? 2000 : potentialSalary;
    } 
}
