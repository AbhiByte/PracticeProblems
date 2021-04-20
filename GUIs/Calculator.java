//Abhinav Ramesh
//ICS4U0
//April 20th, 2021
//Calculator implemented using Swing GUI
//Credits to YouTube channel Bro Code for inspiration and ideas

//Importing Swing and
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class Calculator implements ActionListener
{
    JFrame frame; //Frame
    JTextField textField; //Text field
    JButton[] numberButtons = new JButton[10]; //10 numbers, 0-9
    JButton[] functionButtons = new JButton[9];
    //Instantiating all the buttons
    JButton addButton, subButton, multiplyButton, divButton, decimalButton, equalsButton, deleteButton, clrButton, negativeNumButton;
    JPanel panel;

    //creating a font variable
    Font myFont = new Font("handwritten", Font.BOLD, 20);

    //Answer and operator variables
    double number1 = 0;
    double number2 = 0;
    double result = 0;
    char operator;

    //Constructor
    Calculator()
    {   //Frame
        frame = new JFrame("Calculator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(420, 550);
        frame.setLayout(null); //No layout manager

        //Text field
        textField = new JTextField();
        textField.setBounds(50, 25, 300, 50);
        textField.setFont(myFont);
        textField.setEditable(false); //user cannot enter text in text field

        //Creating all the buttons on the calculator
        addButton = new JButton("+");
        subButton = new JButton("-");
        multiplyButton = new JButton("x");
        divButton = new JButton("/");
        decimalButton = new JButton(".");
        equalsButton = new JButton("=");
        deleteButton = new JButton("Delete");
        clrButton = new JButton("Clear");
        negativeNumButton = new JButton("(-)");

        //Adding above^ buttons to functionButtons
        functionButtons[0] = addButton;
        functionButtons[1] = subButton;
        functionButtons[2] = multiplyButton;
        functionButtons[3] = divButton;
        functionButtons[4] = decimalButton;
        functionButtons[5] = equalsButton;
        functionButtons[6] = deleteButton;
        functionButtons[7] = clrButton;
        functionButtons[8] = negativeNumButton;

        //Add action listener, font, and remove focusable to each button
        for (int i = 0; i < functionButtons.length; i++)
        {
            functionButtons[i].addActionListener(this);
            functionButtons[i].setFont(myFont);
            functionButtons[i].setFocusable(false);
        }

        for (int i = 0; i < 10; i++)
        {
            numberButtons[i] = new JButton(String.valueOf(i));
            numberButtons[i].addActionListener(this);
            numberButtons[i].setFont(myFont);
            numberButtons[i].setFocusable(false);
        }
        negativeNumButton.setBounds(35, 430, 75, 50);
        deleteButton.setBounds(100, 430, 165, 50);
        clrButton.setBounds(250, 430, 150, 50);

        panel = new JPanel();
        panel.setBounds(50, 100, 300, 300);
        panel.setLayout(new GridLayout(4, 4, 10, 10)); //Grid layout manager

        panel.add(numberButtons[1]);
        panel.add(numberButtons[2]);
        panel.add(numberButtons[3]);
        panel.add(addButton);
        panel.add(numberButtons[4]);
        panel.add(numberButtons[5]);
        panel.add(numberButtons[6]);
        panel.add(subButton);
        panel.add(numberButtons[7]);
        panel.add(numberButtons[8]);
        panel.add(numberButtons[9]);
        panel.add(multiplyButton);
        panel.add(decimalButton);
        panel.add(numberButtons[0]);
        panel.add(equalsButton);
        panel.add(divButton);


        frame.add(panel);
        frame.add(negativeNumButton);
        frame.add(deleteButton);
        frame.add(clrButton);
        frame.add(textField);
        frame.setVisible(true);

    }
    //Main method runs the calculator
    public static void main(String[]args)
    {
        Calculator calc = new Calculator();
    }

    @Override
    public void actionPerformed(ActionEvent e)
    {
        for (int i = 0; i < 10; i++)
        {
            if (e.getSource() == numberButtons[i])
            {
                textField.setText(textField.getText().concat(String.valueOf(i)));
            }
        }
        if (e.getSource() == decimalButton)
        {
            textField.setText(textField.getText().concat(String.valueOf(".")));
        }
        if (e.getSource() == addButton)
        {
            number1 = Double.parseDouble(textField.getText());
            operator = '+';
            textField.setText("");
        }
        if (e.getSource() == subButton)
        {
            number1 = Double.parseDouble(textField.getText());
            operator = '-';
            textField.setText("");
        }
        if (e.getSource() == multiplyButton)
        {
            number1 = Double.parseDouble(textField.getText());
            operator = '*';
            textField.setText("");
        }
        if (e.getSource() == divButton)
        {
            number1 = Double.parseDouble(textField.getText());
            operator = '/';
            textField.setText("");
        }
        if (e.getSource() == equalsButton)
        {
            number2=Double.parseDouble(textField.getText());

            switch(operator)
            {
            case '+':
                result = number1 + number2;
                break;
            case '-':
                result = number1 - number2;
                break;
            case '*':
                result = number1 * number2;
                break;
                case '/':
                result = number1 / number2;
                break;
            }
            textField.setText(String.valueOf(result));
            number1 = result;
        }
        if (e.getSource() == clrButton)
        {
            textField.setText("");
        }
        if (e.getSource() == deleteButton)
        {
            String string = textField.getText();
            textField.setText("");
            for (int i = 0; i < string.length() - 1; i++)
            {
                textField.setText(textField.getText()+string.charAt(i));
            }
        }
        if (e.getSource() == negativeNumButton)
        {
            double temp = Double.parseDouble(textField.getText());
            temp *= -1;
            textField.setText(String.valueOf(temp));
        }
    }
}
