
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Find_TraceRoute_Paths {

	static String workingDir;
	//static String[] ases = {"AS10310", "AS12956", "AS16509", "AS20485", "AS2497", "AS2828", "AS3216", "AS37100", "AS4826", "AS6762", "AS701", "AS8359", "AS9002"};
	//static String[] ases = {"AS209", "AS3549", "AS4134", "AS4323", "AS4837", "AS7018"};
	static String[] ases = {"AS2914", "AS3257", "AS13030", "AS1239", "AS1273", "AS32787", "AS16735", "AS10026", "AS6830", "AS3491", "AS18881"};

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		workingDir = System.getProperty("user.dir");


		for(String as: ases){


			FileReader f1=new FileReader(new File(workingDir + "/traceroutes/" + as + "/" + as +"_ALL"));

			BufferedWriter bw=new BufferedWriter(new FileWriter(new File(workingDir + "/traceroutes/" +as + "/" + as +"_path")));
			BufferedReader br= new BufferedReader(f1);
			String temp1;
			HashMap<String,Integer> hm=new HashMap<>();
			temp1=br.readLine();
			while(temp1!=null)
			{
				if(temp1.contains("traceroute"))
				{
					HashSet<String> hs= new HashSet<String>();
					int count=0;
					String path="";
					do
					{
					Pattern pattern =
				        Pattern.compile("(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)");
				    Matcher match = pattern.matcher(temp1);

				    while(match.find())
				    {
				    	String Ip_address=match.group();
				    	if(!hs.contains(Ip_address) )
				    	{
				    		if(count!=0)
				    		{
				    			path=path+" "+Ip_address;
				    		}
				    		else
				    		{
				    			path=Ip_address;
				    		}
				    	}
				    	hs.add(Ip_address);

				    }
				    //System.out.println(hs);
				    temp1=br.readLine();
				    //System.out.println(temp1);
				    count++;
					}while(temp1!=null && !temp1.contains("traceroute") );
					//System.out.println(path);
					bw.write(path);
					bw.newLine();
				}
				else
				{
					temp1=br.readLine();
				}
			}

		}

		
		System.out.println("Done :)");
//		System.out.println(hm.size());
	}

}
