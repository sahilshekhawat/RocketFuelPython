import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.HashMap;
import java.util.HashSet;

//Finds IP addresses from traceroute paths.

public class Find_IP_Address_from_traceroutepath
{


	static String workingDir;
//	static String as = "AS6453";
	//static String[] ases = {"AS10310", "AS12956", "AS16509", "AS20485", "AS2497", "AS2828", "AS3216", "AS37100", "AS4826", "AS6762", "AS701", "AS8359", "AS9002"};
	static String[] ases = {"AS12389"};

	public static void main(String args[]) throws Exception

	{

		workingDir = System.getProperty("user.dir");


		for(String as: ases){


			BufferedReader br=new BufferedReader(new FileReader(new File(workingDir + "/traceroutes/" + as + "/" + as + "_path")));
			BufferedWriter bw=new BufferedWriter(new FileWriter(new File(workingDir + "/traceroutes/" + as + "/" + as + "_unique_IPs")));

			BufferedReader br1=new BufferedReader(new FileReader(new File(workingDir + "/IP/" + as)));
			HashSet<String> hs= new HashSet<String>();
			String strline;
			while((strline=br1.readLine())!=null)
			{
				hs.add(strline);
			}


			String line="";
			HashMap<String,Integer> hm=new HashMap<>();

			while((line=br.readLine())!=null)
			{
				String temp[]=line.split(" ");
				for(String s: temp){
					System.out.println(s);
				}

				String output="";

				for(int i=0;i<temp.length;i++)
				{
					if(hm.containsKey(temp[i]))
					{
						int count=hm.get(temp[i]);
						count=count+1;
						hm.put(temp[i], count);
					}
					else
					{
						hm.put(temp[i],1);
					}
				}
			}
			//System.out.println(hm);

			for(String e:hm.keySet())
			{
				// For Frequency of only those IP addresses which are in particular as
				if(hs.contains(e))
				{
					//System.out.println(e);
					System.out.println(hm.get(e));
				}
				//System.out.println(e);
				bw.write(e);
				bw.newLine();
			}
			bw.close();
			br.close();
			br1.close();


		}

		System.out.println("Done :)");

	}
}
