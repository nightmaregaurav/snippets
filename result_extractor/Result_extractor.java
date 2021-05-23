/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.*;
import java.util.Scanner;

/**
 *
 * @author Gaurav Nyaupane "NIGHTMARE"
 *
 * --+ COPYRIGHT PROTECTED MATERIAL +--
 *
 **/
public class result_extractor {

    /**
     * @param args the command line arguments
     */
    @SuppressWarnings({"CallToPrintStackTrace", "ConvertToTryWithResources"})
    public static void main(String[] args) throws FileNotFoundException {
        try{
            FileReader reader = new FileReader("result.txt");
            BufferedReader bf = new BufferedReader(reader);
            Scanner scan = new Scanner(System.in);
            String line;

            System.out.print("Input the symbol no of campus(eg. 02): ");
            String sym = scan.nextLine().trim();
            System.out.print("Input the name campus(eg. Mechi Multiple Campus): ");
            String name = scan.nextLine().trim();
            System.out.print("Input the address campus(eg. Bhadrapur, Jhapa.): ");
            String addr = scan.nextLine().trim();
            System.out.print("Input one valid symbol number for pattern Identification(eg. 02001): ");
            String pat = scan.nextLine().trim();

            System.out.println("\n\n\tAllNepalRank\tCampusRank\t SymbolNo\n");
            System.out.println("-------------------------------------------\n\n");

            StringBuilder text_file = new StringBuilder("BCA Entrance Result\n"
                    + "Campus: " + name + "\n"
                    + "Address: " + addr + "\n"
                    + "Code: " + sym + "\n");

            StringBuilder html_file = new StringBuilder("<!DOCTYPE html>\n"
					+ "<html>\n"
					+ "<head>\n"
					+ "	<title>" + sym + "</title>\n"
					+ "</head>\n"
					+ "<body>\n"
					+ "	<center>\n"
					+ "		<table border='2px'>\n"
					+ "			<thead>\n"
					+ "				<tr>\n"
					+ "					<th colspan='3'>\n"
					+ "						BCA Entrance Result\n"
					+ "					</th>\n"
					+ "				</tr>\n"
					+ "				<tr>\n"
					+ "					<th colspan='3'>\n"
					+ "						Campus: " + name + "\n"
					+ "					</th>\n"
					+ "				</tr>\n"
					+ "				<tr>\n"
					+ "					<th colspan='3'>\n"
					+ "						Address: " + addr + "\n"
					+ "					</th>\n"
					+ "				</tr>\n"
					+ "				<tr>\n"
					+ "					<th colspan='3'>\n"
					+ "						Code: " + sym + "\n"
					+ "					</th>\n"
					+ "				</tr>\n"
					+ "				<tr>\n"
					+ "					<th colspan='3'>\n"
					+ "						"
					+ "					</th>\n"
					+ "				</tr>\n"
					+ "				<tr>\n"
					+ "					<th>\n"
					+ "						All Nepal Rank\n"
					+ "					</th>\n"
					+ "					<th>\n"
					+ "						Campus Rank\n"
					+ "					</th>\n"
					+ "					<th>\n"
					+ "						Symbol No\n"
					+ "					</th>\n"
					+ "				</tr>\n"
					+ "			</thead>\n"
					+ "			<tbody>\n");
					
            String post_file = text_file.toString();
            post_file += "Link: <<replace_me>>\n\n";

            text_file.append("\nAllNepalRank\t CampusRank\t SymbolNo\n");

            long i=1,j=1;
            while((line = bf.readLine())!=null){
                if(line.length()>sym.length() && line.trim().startsWith(sym)){
                    String line_to_match;
                    if(line.contains(" "))
                        line_to_match = line.split(" ", 2)[0];
                    else
                        line_to_match = line;

                    if (line_to_match.length()==pat.length()){
                        System.out.printf("\t %d\t %d\t %s\n",j,i,line);

                        text_file.append(j).append("\t ").append(i).append("\t ").append(line).append("\n");

                        html_file.append("<tr>\n"
								+ "					<td>\n"
								+ "						" + j + "\n"
								+ "					</td>\n"
								+ "					<td>\n"
								+ "						" + i + "\n"
								+ "					</td>\n"
								+ "					<td>\n"
								+ "						" + line + "\n"
								+ "					</td>\n"
								+ "				</tr>\n");

                        i++;
                    }
                }
                j++;
            }

            html_file.append("</tbody>\n"
					+ "		</table>\n"
					+ "	</center>\n"
					+ "</body>\n"
					+ "</html>\n");

            post_file += "Search your campus' result using hashtag<campus code>(eg. #BCA2020TU_" + sym + ")\n"
            		+ "If result for your campus is not published, inbox us your campus' code/symbol no to get it published.\n"
            		+"#BCA #EntranceResult2020 #BCATU";

            System.out.println("\nDear admin, copy and paste whatever is in '" + sym + "_post_file.txt' which is inside your current directory and post it in the facebook page after uploading PDF version of the '" + sym + ".html'(print as PDF) file which is inside 'result_outputs' folder of your current directory to google drive and changing the link of uploaded file in fifth line of '" + sym + "_post_file.txt'.\n\n\tRegards\n\t-Gaurav Nyaupane\n\n");

            File f;
            FileWriter fw;

            f = new File("result_outputs/");
            if(!f.exists()){
                f.mkdir();
            }

            f = new File(sym + "_post_file.txt");
            if(f.exists())
                //noinspection ResultOfMethodCallIgnored
                f.delete();
            fw = new FileWriter(sym + "_post_file.txt");
            fw.write(post_file);
            fw.close();

            f = new File("result_outputs/" + sym + ".txt");
            if(f.exists())
                //noinspection ResultOfMethodCallIgnored
                f.delete();
            fw = new FileWriter("result_outputs/" + sym + ".txt");
            fw.write(text_file.toString());
            fw.close();

            f = new File("result_outputs/" + sym + ".html");
            if(f.exists())
                //noinspection ResultOfMethodCallIgnored
                f.delete();
            fw = new FileWriter("result_outputs/" + sym + ".html");
            fw.write(html_file.toString());
            fw.close();

            bf.close();
            reader.close();
        }catch(Exception E){
            E.printStackTrace();
        }
    }
}