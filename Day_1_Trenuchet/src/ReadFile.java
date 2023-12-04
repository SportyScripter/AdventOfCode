import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.logging.ErrorManager;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class ReadFile {
    static List<String> allLinesFromFile = new ArrayList<>();

    public ReadFile() throws IOException {
    }

   static List<String> allLinesFromFile(String fileName)  {
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String linia;
            while ((linia = br.readLine()) != null) {
                allLinesFromFile.add(linia);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return allLinesFromFile;
    }
}
