import java.io.*;
public class WriteToAFile{
    public static void main(String[]args)throws IOException{
        BufferedWriter writeFile = new BufferedWriter(new FileWriter("C:\\Users\\abhin\\github\\PracticeProblems\\SchoolProblems\\writeFileTest.txt"));
        String[] myFruits = {"Apples", "Oranges", "Peaches", "Watermelons", "Mangoes"};

        for (int i = 0; i < myFruits.length; i++)
        {
            writeFile.write(myFruits[i]);
            writeFile.newLine();
        }
        writeFile.close();
    }

}
