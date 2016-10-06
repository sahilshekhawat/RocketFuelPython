
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Find_IPaddress_In_particularAs {

	static String workingDir;
	static String as;
	//static String[] ases = {"10310", "12956", "16509", "20485", "2497", "2828", "3216", "37100", "4826", "6762", "701", "8359", "9002", "6453", "6461", "6939"};
	//static String asno = "6453";
	static String[] ases = {"2914","3257","13030","1239","1273","32787","16735","10026","6830","3491","18881"};
	public static void main(String[] args) throws IOException
	{

		for(String asno: ases){


			as = "AS" + asno;
			workingDir = System.getProperty("user.dir");

			// TODO Auto-generated method stub
			BufferedReader br=new BufferedReader(new FileReader(new File(workingDir + "/traceroutes/" + as + "/" + as + "_ip_to_AS_results")));
			BufferedWriter bw=new BufferedWriter(new FileWriter(new File(workingDir + "/traceroutes/" + as + "/IP_in_" + as)));

			String line;
			String splitted[]=null;
			while((line=br.readLine())!=null)
			{

				splitted=line.split("\\|");
				//int length=splitted.length;
				//System.out.println(splitted[0] + " " + splitted[1]);
				//System.out.println(splitted[0].trim().length());
				if(splitted[0].trim().equals(asno))
				{
					//System.out.println("++++++++++++++++++++++++++++++");
					//System.out.println(splitted[1].trim());
					bw.write(splitted[1].trim());
					bw.newLine();
				}
			}

			bw.close();
			br.close();

		}


		System.out.println("Done :)");

	}

}
