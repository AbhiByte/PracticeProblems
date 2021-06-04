public class LockTester
{
    public static void main(String [] args)

    {

        Lock lock1 = new Lock(111);
        Lock lock2 = new Lock(222);


        lock1.close();
        lock2.close();


        System.out.println(lock1.isOpen()); //prints false

        lock1.open(123);					//fails to open lock1
        lock1.open(456);					//fails to open lock1
        lock2.open(222);                    //opens lock2
        System.out.println(lock2.isOpen());	//prints true
        lock1.open(789); 					//fails – prints ALARM
        lock1.open(111); 					//opens lock1


    }

}
