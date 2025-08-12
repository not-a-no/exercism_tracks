public class JedliksToyCar {
    private int meters = 0;
    private int battery = 100;
    public static JedliksToyCar buy() {
        return new JedliksToyCar();
    }

    public String distanceDisplay() {
        return "Driven " + meters + " meters";
    }

    public String batteryDisplay() {
        if (battery <= 0) {
            return "Battery empty";
        }
        return "Battery at " + battery + "%";
    }

    public void drive() {
        if (battery > 0) {
            battery = battery - 1;
            meters = meters + 20;
        }
       
    }
}
