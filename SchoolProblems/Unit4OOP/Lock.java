public class Lock
{
    //Instance variables
    int key; //Int representing a key
    Boolean status;//true for open, false for closed

    
    int attemptCount; //Keep count of number of attempts

    //constructor
    public Lock (int key)
    {
        this.key = key;
        status = true;
    }

    //methods
    public void close()
    {
        this.status = false;
    }

    public boolean isOpen()
    {
        if (this.status == true)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    public void open(int key)
    {
        //If the inputted key == the true key
        if (this.key == key && this.status == false)
        {
            this.status = true;
            attemptCount = 0;

        }
        //If not
        else
        {
            attemptCount++;
            this.status = false;
            //If counter == 3...
            if (attemptCount == 3)
            {
                System.out.println("ALARM");
            }
        }

    }
}
