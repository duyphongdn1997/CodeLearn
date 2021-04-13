package Chapter04;

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
        for (int i = 0; i < text.length; i++){
            if(textToBeSearch.equals(text[i])){
                System.out.print(i);
                occurrence++;
            }
        }
        return occurrence;
    }
}
