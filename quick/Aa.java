import java.io.*;
import javax.xml.parsers.*;
import org.w3c.dom.*;




public class Aa
{

	public static void main(String args[])
	{
		try
		{		
		File f=new File("aa.xml");
		DocumentBuilderFactory dm=DocumentBuilderFactory.newInstance();
		DocumentBuilder d=dm.newDocumentBuilder();
		Document doc=d.parse(f);
		
		doc.getDocumentElement().normalize();
		
		System.out.println("Root :"+doc.getDocumentElement().getNodeName());

		NodeList n1=doc.getElementsByTagName("item");	

		int a[]=new int[n1.getLength()];

		for (int i=0;i<n1.getLength();i++)
		{
			Node n=n1.item(i);
			a[i]=Integer.parseInt(n.getTextContent());	
		}


		long st=System.nanoTime();
		
		Thread t=new Thread(new Quick(a,0,a.length-1));
		t.start();
		t.join();

		long ft=System.nanoTime();

		System.out.println("\nsorte:");
		for(int i:a)
		{
			System.out.println(i);
		}
		System.out.println("time:"+(st-ft));
		}
		catch(Exception e)
		{
		}
	}	

}


class Quick implements Runnable
{

	int a[];
	int start;
	int end;

	public Quick(int a[],int start,int end)
	{
		this.a=a;
		this.start=start;
		this.end=end;
	}

	public int sort(int a[],int start,int end)
	{
						
		int pivot=a[start];
		int i=start;
		int j=end+1;
		int temp;
		
		do
		{
			do
			{
				i++;
			}while(a[i]<pivot && i<=end);
			do
			{
				j--;
			}while(a[j]>pivot);
		
			if(i<j)
			{
				 temp=a[i];
				a[i]=a[j];
				a[j]=temp;
			}
		}while(i<j);
		a[start]=a[j];
		a[j]=pivot;
		
		
		return j;	
		
	}


	public void sort1(int a[],int start,int end)
	{
		try
		{		
		int j;
		if(start<end)
		{
			j=sort(a,start,end);
			Thread t=new Thread(new Quick(a,start,j-1));
			t.start();
			t.join();
			Thread t1=new Thread(new Quick(a,j+1,end));
			t1.start();
			t1.join();
		}
		}
		catch(Exception e)
		{
		}

	}		
			

	public void run()
	{
		try
		{
			sort1(a,start,end);
		}
		catch(Exception e)
		{
		}
	}	
}			
				
