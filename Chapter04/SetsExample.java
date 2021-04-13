package Chapter04;

import java.util.*;
import java.io.Console;

public class SetsExample {
    public static void main(String[] args) {
        Set<Integer> set1 = new LinkedHashSet<>();
        set1.add(35);
        set1.add(19);
        set1.add(11);
        set1.add(83);
        set1.add(7);
        Set<Integer> set2 = new LinkedHashSet<>();
        set2.add(3);
        set2.add(19);
        set2.add(11);
        set2.add(0);
        set2.add(7);
        set1.removeAll(set2);
        System.out.println(set1);
    }
}

class AnalyzeInput {
    public static void main(String[] args) {
        Console cons;
        String line = "";
        List<String> list = new ArrayList<>(); 
        while ((cons = System.console()) != null && (line = cons.readLine()) != null && (!line.equals("end"))) {
            list.add(line);
        }
        for(int i = 0;i<list.size();i++){
            System.out.println("You typed: " + list.get(i));
        }
    }
}