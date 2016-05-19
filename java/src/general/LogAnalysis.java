package general;

import java.io.*;
import java.util.*;

public class LogAnalysis {
	public static void splitJson(String json){
		
	}
	
    public static void logAnalysis(ArrayList<String> log){
        HashSet<String> sn = new HashSet<>();
        HashSet<String> si = new HashSet<>();
        
        int info = 0;
        int warn = 0;
        int max_ss = Integer.MIN_VALUE;
        
        for(int i = 0; i < log.size(); i++){
            String[] split = log.get(i).split(" ", 2);
            if (split[0].equals("INFO:") || split[0].equals("WARN:")){                       
                String type = split[0].trim().substring(0, split[0].length() - 1);
                String jsonString = split[1].trim().substring(1, split[1].length() - 1);
                
                if (type.equals("INFO"))
                    info ++;
                else
                    warn ++;
                
                String[] json = jsonString.split(",", 5);
                for(String json_entry: json){
                	String[] keyPair = json_entry.split(":", 2);
                	keyPair[0] = keyPair[0].trim();
                	keyPair[1] = keyPair[1].trim();
                	
                	String key = keyPair[0];
                	String value = keyPair[1];
                	
                	if (key.equals("\"sn\"")){
                		sn.add(value);
                	}
                	else if(key.equals("\"ht\"")){
                		value = value.substring(2, value.length() - 2);       
                		for(String inner_entry: value.split(",")){                			
                			String[] keyPair_inner = inner_entry.split(":", 2);
                			keyPair_inner[0] = keyPair_inner[0].trim();
                			keyPair_inner[1] = keyPair_inner[1].trim();
                        	
                        	String key_inner = keyPair_inner[0];
                        	String value_inner = keyPair_inner[1];
                        	
                        	if(key_inner.equals("\"ss\"")){
                        		max_ss = Math.max(max_ss, Integer.parseInt(value_inner));
                        	}
                        	else if (key_inner.equals("\"si\"")){
                        		si.add(value_inner);
                        	}
                		}
                	}                	
                	                	
                }
            }                
        }
        
        System.out.println(info);
        System.out.println(warn);
        System.out.println(sn.size());
        System.out.println(si.size());
        System.out.println(max_ss);   
        
        
    }
    
    public static void main(String args[] ) throws Exception { 
    	String input = String.join("\n",    
		"Jun 23, 2015 11:00:00 PM org.apache.jsp.index_jsp _jspService",
		"INFO: {\"sq\": 0, \"vs\": 3, \"pf\": 11, \"sn\": \"1965f45398abbf9e995fe9eb18282510\", \"ht\": [{\"cn\": 1, \"ap\": 0, \"ss\": -51, \"s2\": 2601, \"s3\": -132651, \"si\": \"x524b976cd3bb7071\", \"sh\": -51, \"sm\": \"C49A02\", \"sl\": -51, \"ot\": 1435100360, \"ct\": 1435100360}]}",
		"Jun 23, 2015 11:00:00 PM org.apache.jsp.index_jsp _jspService",
		"INFO: {\"sq\": 0, \"vs\": 3, \"pf\": 11, \"sn\": \"1965f45398abbf9e995fe9eb18282510\", \"ht\": [{\"cn\": 1, \"ap\": 0, \"ss\": -75, \"s2\": 5625, \"s3\": -421875, \"si\": \"x05c96aa3599619ef\", \"sh\": -75, \"sm\": \"00C610\", \"sl\": -75, \"ot\": 1435100398, \"ct\": 1435100398}]}",
		"Jun 23, 2015 11:00:00 PM org.apache.jsp.index_jsp _jspService",
		"INFO: {\"sq\": 0, \"vs\": 3, \"pf\": 11, \"sn\": \"1965f45398abbf9e995fe9eb18282510\", \"ht\": [{\"cn\": 1, \"ap\": 0, \"ss\": -85, \"s2\": 7225, \"s3\": -614125, \"si\": \"x085ed8ad97ec29ab\", \"sh\": -85, \"sm\": \"6476BA\", \"sl\": -85, \"ot\": 1435100340, \"ct\": 1435100340}]}",
		"Jun 23, 2015 11:00:00 PM org.apache.jsp.index_jsp _jspService",
		"INFO: {\"sq\": 0, \"vs\": 3, \"pf\": 11, \"sn\": \"1965f45398abbf9e995fe9eb18282510\", \"ht\": [{\"cn\": 1, \"ap\": 0, \"ss\": -71, \"s2\": 5041, \"s3\": -357911, \"si\": \"x7aff7156cc42d14e\", \"sh\": -71, \"sm\": \"0C4885\", \"sl\": -71, \"ot\": 1435100378, \"ct\": 1435100378}]}" );
    	
        Scanner scan = new Scanner(input);
        ArrayList<String> log = new ArrayList<>();
        
        while (scan.hasNextLine()){
            String string = scan.nextLine();
            log.add(string);
        }
        
        logAnalysis(log);
    }
}