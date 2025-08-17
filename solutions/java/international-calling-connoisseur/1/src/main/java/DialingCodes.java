import java.util.Map;
import java.util.HashMap;

public class DialingCodes {
    private Map<Integer, String> codes = new HashMap<>();
    public Map<Integer, String> getCodes() {
        return codes;
    }

    public void setDialingCode(Integer code, String country) {
        codes.put(code, country);
    }

    public String getCountry(Integer code) {
        return codes.get(code);
    }

    public void addNewDialingCode(Integer code, String country) {
            if (codes.containsKey(code) || codes.containsValue(country)) {
                return; 
            }
            setDialingCode(code, country);
    }

    public Integer findDialingCode(String country) {
        for (Integer key : codes.keySet()) {
            if (codes.get(key).equals(country)) {
                return key;
            }
        }
        return null;
            
    }

    public void updateCountryDialingCode(Integer code, String country) {
        if (findDialingCode(country).equals(null)) {
            return;
        }
        codes.remove(findDialingCode(country));
        codes.put(code, country);
    }
}
