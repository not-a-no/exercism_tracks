public class LogLevels {
    
    public static String message(String logLine) {
        int colonIndex = logLine.indexOf(":");
        return logLine.substring(colonIndex + 1).trim();
    }

    public static String logLevel(String logLine) {
        int colonIndex = logLine.indexOf("]");
        return logLine.substring(1, colonIndex).toLowerCase();
    }

    public static String reformat(String logLine) {
        return message(logLine) + " (" + logLevel(logLine) + ")";
    }
}
