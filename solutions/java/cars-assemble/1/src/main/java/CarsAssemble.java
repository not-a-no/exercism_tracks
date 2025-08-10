public class CarsAssemble {
    final double rate4 = 1.0;
    final double rate8 = 0.9;
    final double rate9 = 0.8;
    final double rate10 = 0.77;
    final int unitCarPerHour = 221;
    public double productionRatePerHour(int speed) {
        int totalCar = unitCarPerHour * speed;
        if (speed <= 4) {
            return totalCar * rate4;
        } else if (speed <= 8) {
            return totalCar * rate8;
        } else if (speed == 9) {
            return totalCar * rate9;
        } else {
            return totalCar * rate10;
        }
    }

    public int workingItemsPerMinute(int speed) {
        return (int) productionRatePerHour(speed) / 60;
    }
}
