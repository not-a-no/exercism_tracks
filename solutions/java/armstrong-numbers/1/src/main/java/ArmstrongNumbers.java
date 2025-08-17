class ArmstrongNumbers {

    boolean isArmstrongNumber(int numberToCheck) {
        int total = 0;
        int number = numberToCheck;
        int i = (int) Math.floor(Math.log10(numberToCheck)) + 1;
        while (number > 0) {
            total += (int) Math.pow((number % 10), i);
            number = number / 10;
        }
        return total == numberToCheck ? true : false;

    }

}
