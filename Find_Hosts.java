package traceroute;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

//Finds hosts in an AS from its final Traceroute path.

public class Find_Hosts {

	public static void main(String[] args) throws IOException
	{
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new FileReader(new File("E://Rocketfuel/AS10201/Traceroutes_final.txt")));
		String temp1;
		String temp2;
		int count=0;
		while((temp1=br.readLine())!=null)
		{
			if(temp1.contains("HOST :"))
			{
				//temp2=br.readLine();
				//if(temp2.contains("traceroute"))
				//{
					count++;
					System.out.println(temp1);
				//}



			}


		}
		System.out.println(count);

	}

}
