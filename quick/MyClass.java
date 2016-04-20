/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package myclass;

import java.util.Arrays;
import java.util.Arrays.*;
import java.io.File;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.naming.ldap.SortControl;
import javax.xml.parsers.DocumentBuilder;
import org.w3c.dom.*;
/**
 *
 * @author Sahil
 */
public class MyClass {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        try{
            File f = new File("C:\\Users\\Sahil p\\Documents\\NetBeansProjects\\MyClass\\src\\myclass\\myxml.xml");
            DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
            DocumentBuilder db = dbf.newDocumentBuilder();
            Document doc = db.parse(f);
            doc.getDocumentElement().normalize();
           		NodeList nl=doc.getElementsByTagName("item");
	
			int num[]=new int[nl.getLength()];
			
			for(int i=0;i<nl.getLength();i++){
				Node n=nl.item(i);
				num[i]=Integer.parseInt(n.getTextContent());
			}
			int[] num2=num;
			System.out.println("File read!");
                        Thread t = new Thread(new QuickSortClass(num, 0, num.length-1));
			t.start();
			t.join();
                        for(int i:num){
                            System.out.print(i+" ");
                        } 
        } catch(Exception e){
            System.out.println(e.getMessage());
        }
    }
    
}
