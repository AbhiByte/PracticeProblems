public class TelevisionTest
{
    public static void main (String[]args)
    {
        Television first = new Television("Sony", 43);
        Television second = new Television("Samsung", 54);

        //System.out.println(first); //Sony 43" turned off
        //System.out.println(second); //Samsung 54" turned off

        first.turnOn();
        first.turnUpVol();
        second.turnDownVol();
        first.changeChannel(34);
        second.turnOn();
        second.changeChannel(17);

        //System.out.println(first); //Sony 43" on channel 34 volume: 11
        //System.out.println(second); //Samsung 54" on channel 17 volume: 10

        for (int press = 1; press <= 60; press++){
	       first.turnUpVol();
       }

       for (int press = 1; press <= 20; press++){
	      second.turnDownVol();
      }
      //System.out.println(first); //Sony 43" on channel 34 volume: 50
      //System.out.println(second);//Samsung 54" on channel 17 volume: 0

      first.turnOff();
      first.changeChannel(21);

      second.changeChannel(13);
      first.turnOn();
      first.turnDownVol();
      second.turnUpVol();

      System.out.println(first); //Sony 43" on channel 34 volume: 49
      System.out.println(second); //Samsung 54" on channel 13 volume: 1

      /*
      b) Material, colour, cost, smartOrNot, etc
      c) fps, mute, streamContent (String), etc



    }
}
