class ProductionRemoteControlCar implements RemoteControlCar, Comparable<ProductionRemoteControlCar> {
    private int distanceDriven = 0; 
    int numberOfVictories;
    public void drive() {
        distanceDriven += 10; ;
    }

    public int getDistanceTravelled() {
        return distanceDriven;
    }

    public int getNumberOfVictories() {
        return this.numberOfVictories;
    }

    public void setNumberOfVictories(int numberOfVictories) {
        this.numberOfVictories = numberOfVictories;
    }

    public int compareTo(ProductionRemoteControlCar other) {
        // Descending order of victories
        return Integer.compare(other.numberOfVictories, this.numberOfVictories);
    }
}
