import java.util.ArrayList;
import java.util.List;

public class NumberMeter {
    private static int sum;
    private static int totalSum;

    public NumberMeter() {
    }

    static int CountAllNumber(List<String> ListOfString) {
        for (String lines : ListOfString) {
            totalSum += findAllNumbers(lines);
        }
        return totalSum;
    }

    static int findAllNumbers(String string) {
        String ConcatTwoNumbers = "";
        List<Integer> countIndex = new ArrayList<>();
        for (int i = 0; i < string.length(); i++) {
            if (Character.isDigit(string.charAt(i))) {
                countIndex.add(i);
            }
        }
        if (countIndex.isEmpty())
            return 0;
        else if (countIndex.size() == 1) {
            sum = Integer.parseInt(java.lang.String.valueOf(string.charAt(countIndex.getFirst()))) * 11;
        } else if (countIndex.size() > 1) {
            ConcatTwoNumbers = ConcatTwoNumbers.concat(java.lang.String.valueOf(string.charAt(countIndex.getFirst()))).concat(java.lang.String.valueOf(string.charAt(countIndex.getLast())));
            sum = Integer.parseInt(ConcatTwoNumbers);
        }
        return sum;
    }
}
