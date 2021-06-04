public class Television
{
	private String brand;
	private int size;
	private int volume;
	private int channel;
	private boolean on;

	public Television(String brand, int size)
	{
		this.brand = brand;
		this.size = size;
		this.volume = 10;
		this.channel = 2;
		this.on = false;
	}

	public void turnOn()
	{
		this.on = true;
	}

	public void turnOff()
	{
		this.on = false;
	}

	public void changeChannel(int newChannel)
	{
		if (on)
			channel = newChannel;
	}

	public void turnUpVol()
	{
		if (on && volume < 50)
			volume++;
	}

	public void turnDownVol()
	{
		if (on && volume > 0)
			volume--;
	}

	public String toString()
	{
		if (on)
			return String.format("%s %d\" on channel %d volume: %d",
					brand, size, channel, volume);
		else
			return String.format("%s %d\" turned off", brand, size);
	}

}
