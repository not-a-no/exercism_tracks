import java.util.List;
import java.util.Set;
import java.util.HashSet;

class GottaSnatchEmAll {

    static Set<String> newCollection(List<String> cards) {
        return new HashSet<>(cards);
    }

    static boolean addCard(String card, Set<String> collection) {
        return collection.add(card);
    }

    static boolean canTrade(Set<String> myCollection, Set<String> theirCollection) {
        boolean iHaveExtra = false;
        boolean theyHaveExtra = false;

        for (String card : myCollection) {
            if (!theirCollection.contains(card)) {
                iHaveExtra = true;
                break; // no need to keep looking
            }
        }

        for (String card : theirCollection) {
            if (!myCollection.contains(card)) {
                theyHaveExtra = true;
                break; // stop once we find one
            }
        }

        return iHaveExtra && theyHaveExtra;
    }

    static Set<String> commonCards(List<Set<String>> collections) {
        Set<String> common = new HashSet<>(collections.get(0));
        for (int i = 1; i < collections.size(); i++) {
            common.retainAll(collections.get(i));
        };
        return common;
    }

    static Set<String> allCards(List<Set<String>> collections) {
        Set<String> combined = new HashSet<>(collections.get(0));
        for (int i = 1; i < collections.size(); i++) {
            combined.addAll(collections.get(i));
        };
        return combined;
    }
}
