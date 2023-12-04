import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;


public class Main {

    public static void main(String[] args) throws IOException {
        System.out.println(NumberMeter.CountAllNumber(ReadFile.allLinesFromFile("HidenNumbers.txt")));
    }
}