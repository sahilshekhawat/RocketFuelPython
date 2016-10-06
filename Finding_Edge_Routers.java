import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashSet;

public class Finding_Edge_Routers {

	static String workingDir;
	static String as = "AS6453";
	//static String[] ases = {"AS10310", "AS12956", "AS16509", "AS20485", "AS2497", "AS2828", "AS3216", "AS37100", "AS4826", "AS6762", "AS701", "AS8359", "AS9002", "AS6453", "AS6461", "AS6939"};
	static String[] ases = {"AS2914", "AS3257", "AS13030", "AS1239", "AS1273", "AS32787", "AS16735", "AS10026", "AS6830", "AS3491", "AS18881"};

	public static void main(String[] args) throws IOException
	{
		// TODO Auto-generated method stub
		workingDir = System.getProperty("user.dir");


		for (String as: ases){



			BufferedReader br=new BufferedReader(new FileReader(new File(workingDir + "/traceroutes/" +as + "/" + as +"_path")));
			String line="";

			BufferedReader br1=new BufferedReader(new FileReader(new File(workingDir + "/traceroutes/" + as + "/IP_in_" + as)));
			BufferedWriter bw=new BufferedWriter(new FileWriter(new File(workingDir + "/traceroutes/" + as + "/" + as + "_Edge_routers")));
			//BufferedWriter bw1=new BufferedWriter(new FileWriter(new File(workingDir + "/traceroutes/" + as + "/" + as + "_Core_routers")));


			HashSet<String> hs= new HashSet<String>();
			HashSet<String> hs1=new HashSet<String>();

			String strline;
			while((strline=br1.readLine())!=null)
			{
				hs.add(strline);
			}
			int count=0;
			while((line=br.readLine())!=null)
			{
				String temp[]=line.split(" ");

				String output="";

				for(int i=1;i<temp.length;i++)
				{
					if(hs.contains(temp[i]))
					{
						//count++;
						hs1.add(temp[i]);
						//System.out.println(temp[i]);
						break;
					}
				}
			}
			//System.out.println("Count="+count);
			//System.out.println(hs1.size());

			for(String s :hs1)
			{
				bw.write(s);
				bw.newLine();
			}

			bw.close();
			//System.out.println(hs1);



		}


	}

}
