package Chapter04;
import java.util.Arrays;
public class Occurrences {
    private String[] text;
    private String textToBeSearch;
    
    public Occurrences(){

    }

    public Occurrences(String[] text, String textToBeSearch){
        this.text = text;
        this.textToBeSearch = textToBeSearch;
    }
    public void setText(String[] text){
        this.text = text;
    }
    public String[] getText(){
        return text;
    }

    public void setTextToBeSearch(String textToBeSearch){
        this.textToBeSearch = textToBeSearch;
    }

    public String getTextToBeSearch(){
        return textToBeSearch;
    }

    public int occurrence (){
        int occurrence = 0;
        int temp = 0;
        for (int i = 0; i < text.length; i++){
            temp = textToBeSearch.compareToIgnoreCase(text[i]);
            System.out.println(temp);
            if(temp == 0){
                System.out.print(i);
                System.out.println(" "+ text[i]);
                occurrence++;
            }
        }
        return occurrence;
    }
}