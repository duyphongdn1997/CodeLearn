package Chapter04;

public class Activity01{
    public static void main(String[] arg){
        Occurrences oc = new Occurrences();
        String[] text = {"So", "many", "books", "so", "little", "time"};
        String textToBeSearch = "so";
        oc.setText(text);
        oc.setTextToBeSearch(textToBeSearch);
        oc.occurrence();
    }
}

