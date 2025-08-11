class SqueakyClean {
    static String clean(String identifier) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < identifier.length(); i ++) {
            char c = identifier.charAt(i);
            if (c == ' ') {
                sb.append('_');
            } else if (i > 0 && identifier.charAt(i-1) == '-') {
                sb.append(Character.toUpperCase(c));
            } else if (c == '4') {
                sb.append('a');
            } else if (c == '3') {
                sb.append('e');
            } else if (c == '0') {
                sb.append('o');
            } else if (c == '1') {
                sb.append('l');
            } else if (c == '7') {
                sb.append('t');
            } else if (Character.isLetter(c)) {
                sb.append(c);
            }

        }
        return sb.toString();
    }
    
}
