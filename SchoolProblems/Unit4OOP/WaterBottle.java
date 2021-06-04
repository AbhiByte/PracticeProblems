//Abhinav Ramesh
//ICS4U0
//April 19th, 2021
//Class worked on in class, including instance variables, constructors, methods, getters, setters and toString.
//Based on the features of a water bottle
public class WaterBottle
{
    //Instance variables
    private double capRadius; //radius of the bottle cap
    private double bottleHeight; //height of bottle
    private double bottleRadius; //radius of the bottle
    private String materialType; //material of bottle
    int capStatus; //Cap open/close. 0 = closed, 1 = open, public to aid in ArrayOfBottles method
    private boolean drinking; //Drinking or not
    private String colour; //Colour of the bottle

    //In this case, class variables may be used but not applicable to our purpose

    //Constructor
    public WaterBottle()
    {   //Standard dimensions/features of a water bottle
        setBottleHeight(20); //Using setter to set bottle height. Can be assigned normally as well
        bottleRadius = 1;
        materialType = "metal";
        capRadius = 4;
        bottleHeight = 3;
    }
    //Input constructor
    public WaterBottle(double capRadius, double bottleHeight, double bottleRadius, String materialType)
    {   //User assigns values for certain variables using this constructor
        this.capRadius = capRadius;
        this.bottleHeight = bottleHeight;
        this.bottleRadius = bottleRadius;
        this.materialType = materialType;
    }
    //Comparision method. If bottles are same, returns true. If not, returns false
    public boolean equals (WaterBottle bottle)
    {   //2 bottles are considered to be equal if their radius/height (and hence volume) is the same and if they are made from the same material
        if (this.bottleRadius == bottle.bottleRadius && this.bottleHeight == bottle.bottleHeight && this.materialType == bottle.materialType)
        {
            return true;
        }
        //If not equal...
        else
        {
            return false;
        }
    }



    //Takes the bottle radius and bottle height as parameters and returns the volume of the bottle
    public double volume (double bottleRadius, double bottleHeight)
    {   //Formula for volume of a cylinder: pi*r^2*h
        double volumeOfBottle = Math.PI*Math.pow(bottleRadius, 2.0)*bottleHeight;
        return volumeOfBottle;
    }
    //Volume method for default constructor. Uses default constructor values and returns volume
    public double volume2 ()
    {
        double volumeOfBottle = Math.PI*Math.pow(bottleRadius, 2.0)*bottleHeight;
        return volumeOfBottle;
    }

    //Returns the status of the cap. If cap == 1, bottle is open. Else, it is closed
    public String CapOpenClose (int cap)
    {   //Returns string value. Can be modified to return data type based on application
        if (cap == 1)
        {
            return "The cap is open!";
        }
        else
        {
            return "The cap is closed :(";
        }
    }
    //Drinking method. Takes drink and volume as input. If drink == true, 10% is subtracted
    //from the volume of the bottle, simulating water or another liquid leaving the bottle
    //when someone drinks from it
    public double drink (boolean drink, double volume)
    {
        if (drink == true)
        {   //removing 10% of volume
            volume -= (0.1*volume);
            return volume;
        }
        else
        {
            return volume;
        }
    }

    //Heat capacity of the bottle based on the material
    public int heatCapacity(String material)
    {   //These are pseudo-random values and the method could be expanded to include more materials
        if (material == "metal")
        {
            return 300;
        }
        //If plastic
        else if (material == "plastic")
        {
            return 80;
        }
        //Any other material
        else
        {
            return 50;
        }
    }

    //Strength of bottle. Relative strength of the material.
    public int strength (String material)
    {   //'2' for metals
        if (material.toLowerCase() == "metal")
        {
            return 2;
        }
        //'1' for plastic
        else if (material.toLowerCase() == "plastic")
        {
            return 1;
        }
        //'0' for any other material
        else
        {
            return 0;
        }
    }

    //Setters. Sets variable to parameter passed. Same format for all variables
    public void setBottleHeight (double height)
    {
        if (height >= 10)
        {
            this.bottleHeight = height;
        }
    }
    public void setMaterialType(String material)
    {
        this.materialType = material;
    }
    public void setCapRadius (double radius)
    {
        if (radius < 10)
        {
            this.capRadius = radius;
        }
        else
        {
            System.out.println("Please enter a believable cap radius!");
        }
    }
    public void setBottleRadius (double bRad)
    {
        this.bottleRadius = bRad;
    }
    public void setCapStatus (int status)
    {
        this.capStatus = status;
    }
    //Getters. Returns variable value to user. Same format for all variables
    public String getMaterialType()
    {
        return materialType;
    }
    public double getBottleHeight()
    {
        return bottleHeight;
    }
    public double getCapRadius()
    {
        return capRadius;
    }
    public double getBottleRadius()
    {
        return bottleRadius;
    }
    public int getCapStatus()
    {
        return capStatus;
    }

    //toString. Outputs bottle features in a format understandable by the user.
    public String toString()
    {
        return ("This water bottle has\nCapRadius: " + capRadius + "\nBottle height: " + bottleHeight + "\nBottle radius: " + bottleRadius + "\nMaterial Type: " + materialType);
    }


}
