package traceroute;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;

public class FrequencyOfEdgeRouters {


	static String workingDir;
	static String as = "AS6939";

	public static void main(String[] args) throws IOException
	{
		workingDir = System.getProperty("user.dir");

		// TODO Auto-generated method stub
		BufferedReader br1=new BufferedReader(new FileReader(new File(workingDir + "/traceroutes/" + as + "/" + as + "_Edge_routers")));
		HashSet<String> hs= new HashSet<String>();
		String strline;
		while((strline=br1.readLine())!=null)
		{
			hs.add(strline.trim());
		}

		BufferedReader br2=new BufferedReader(new FileReader(new File(workingDir + "/traceroutes/" + as + "/" + as + "_Cumulative_IP")));
		String line;
		HashMap<String,String> hm=new HashMap<>();
		int count=0;
		while((line=br2.readLine())!=null)
		{
						//System.out.println(count);
			//String temp[]=line.split("	");
			if(hs.contains(line.trim()))
			{
				count++;
			}

			//String output="";
			//hm.put(temp[0].trim(), temp[1].trim());
		}

//		for(String e:hm.keySet())
//		{
//			if(!hs.contains(e))
//			{
//				count++;
//				System.out.println(hm.get(e));
//			}
//		}
		System.out.println(count);

	}

}
