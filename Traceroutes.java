import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Timer;
import java.util.TimerTask;

import com.jcraft.jsch.ChannelExec;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.Session;

import java.util.Scanner;

public class Traceroutes {

	 //static String workingDir = "E://PlanetLab/";
	 static String workingDir;
	 static String AS;
	 static String nodesFile;
	 static String privateKeyFile = "planet_lab";
	 static String tracerouteFile;
	 static ArrayList<String> ip = new ArrayList<String>();
	 static ArrayList<String> nodes = new ArrayList<String>();

	public static void main(String[] args)
	{
		// TODO Auto-generated method stub


			//static String abc="test";
			//static ChannelExec channel = null;
				workingDir = System.getProperty("user.dir");
				Scanner sc = new Scanner(System.in);
				AS = sc.nextLine();
				nodesFile = sc.nextLine();
				tracerouteFile = AS + "_" + nodesFile;

				loadip();
				//String planetnodes = args[0];   //planet nodes in text file through command line argument
				//String planetnodes = "planetnodes1";
				//loadnodes(planetnodes);
				loadnodes();
				//ssh(planetnodes);
				ssh();
		}

			public static void loadip()
			{
				try
				{

					FileReader f1=new FileReader(new File(workingDir +"/IP/" + AS));
					BufferedReader br= new BufferedReader(f1);
					//BufferedReader br = new BufferedReader(new FileReader(new File(workingDir +"ip.txt")));
					String strline;
					while((strline = br.readLine()) != null)
					{
						ip.add(strline);
					}
					br.close();
				}
				catch(Exception e)
				{
					e.printStackTrace();
					e.getCause();
				}
			}

			public static void loadnodes()
			{
				try
				{
					BufferedReader br = new BufferedReader(new FileReader(new File(workingDir + "/Nodes/"+ nodesFile)));
					String strline;
					while((strline = br.readLine()) != null)
					{
						strline=strline.trim();
						nodes.add(strline);
					}
					br.close();
				}
				catch(Exception e)
				{
					e.printStackTrace();
					e.getCause();
				}
			}


			//static Session session = null;

			public static void ssh()
			{
				try
				{

					//File file = new File(workingDir + "/planet/" + planetnodes + "_traceroutes.txt");
					File file = new File(workingDir + "/traceroutes/"+ tracerouteFile);
					// if file doesnt exists, then create it
			        if (!file.exists())
			        {
			            file.createNewFile();
			        }
			        FileWriter fw = new FileWriter(file.getAbsoluteFile());
			        BufferedWriter bw = new BufferedWriter(fw);

			        //.................................................................

			        for(String n : nodes)
			        {
			        	try
			        	{
				        	bw.write("HOST : " + n);
				        	bw.newLine();
				        	System.out.println("HOST : " + n);
				        	System.out.println();

				        	JSch jsch = new JSch();

				            String user = "iiitd_anshika";

				            String host = n;

				            int port = 22;
				            String privateKey = workingDir + "/" + privateKeyFile;

				            jsch.addIdentity(privateKey);
				            System.out.println("identity added ");

				            Session session = jsch.getSession(user, host, port);
				            //session = jsch.getSession(user, host, port);
				            System.out.println("session created.");

				            java.util.Properties config = new java.util.Properties();
				            config.put("StrictHostKeyChecking", "no");
				            session.setConfig(config);

				            session.setTimeout(90000);

				            session.connect();
				            System.out.println("session connected.....");

				            ChannelExec channel = null;

				            for(String s : ip)
				            {

				            	//abc = "test";
				            	String command = "sudo traceroute " + s + ";";

				            	//System.out.println();
				            	System.out.println(command);
				            	//bw.write(command);
				            	//bw.newLine();

				            	channel=(ChannelExec) session.openChannel("exec");
				                BufferedReader in=new BufferedReader(new InputStreamReader(channel.getInputStream()));

				            	channel.setCommand(command);
				                channel.connect(90000);



				                //System.out.println("test..");
				                String msg = null;
				                while((msg=in.readLine())!=null)
				                {
				                	//System.out.println(msg);
				                	bw.write(msg);
				                	bw.newLine();
				                }

				                bw.newLine();
				                bw.flush();
				                System.out.println("TEST");
				            }

				            //System.out.println("test...");
				            channel.disconnect();
				            session.disconnect();
			        	}
			        	catch(Exception e)
			        	{
			        		e.printStackTrace();
			        		e.getCause();
			        		bw.newLine();
			        		continue;
			        	}

			        }

			        bw.close();

				}
				catch(Exception e)
				{
					e.printStackTrace();
					e.getCause();
				}
			}




	}
