import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int h,m;
		h = input.nextInt();
		m = input.nextInt();
		if(m < 45)
		{
			m += 15;
			if(h == 0)
			{
				h = 23;
				System.out.println(h+ " " + m);
			}
			else
			{	h--;
				System.out.println(h+ " "+ m);
			}
		}
		else {
			m -= 45;
			System.out.println(h + " " + m); 
		}
		
	}

}
