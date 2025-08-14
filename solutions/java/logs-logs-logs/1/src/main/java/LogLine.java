public class LogLine {
    String logLine;
    ;
    public LogLine(String logLine) {
        this.logLine = logLine;
    }

    public LogLevel getLogLevel() {
        int levelIndex = this.logLine.indexOf("]");
        String logLevel = this.logLine.substring(1, levelIndex);
        switch (logLevel) {
            case "TRC":
                return LogLevel.TRACE;
            case "DBG":
                return LogLevel.DEBUG;
            case "INF":
                return LogLevel.INFO;
            case "WRN":
                return LogLevel.WARNING;
            case "ERR":
                return LogLevel.ERROR;
            case "FTL":
                return LogLevel.FATAL;
            default:
                return LogLevel.UNKNOWN;
        }
    }

    public String getOutputForShortLog() {
        int colonIndex = this.logLine.indexOf(":");
        String messages = this.logLine.substring(colonIndex+1).trim();
        return getLogLevel().getLogNumber() + ":" + messages;
    }
}


