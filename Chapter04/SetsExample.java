package Chapter04;

import java.util.*;
import java.io.Console;
import java.util.Map;


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

 class Example15 {
    public static void main(String[] args) {
        Map<String, Object> map = new HashMap<>();
        map.put("number", new Integer(1));
        map.put("text", new String("hola"));
        map.put("decimal", new Double(5.7));
        System.out.println(map.get("text"));
        if (!map.containsKey("byte")) {
            System.out.println("There are no bytes here!");
        }
        System.out.println(map.entrySet());
    }
}


class Example16 {
    public static void main(String[] args) {
        List<Integer> array = new ArrayList<>();
        array.add(5);
        array.add(2);
        array.add(37);
        Iterator<Integer> iterator = array.iterator();
        while (iterator.hasNext()) {
                // point to next element
                int i = iterator.next();
                // print elements
                System.out.print(i + " ");
        }

    }
}