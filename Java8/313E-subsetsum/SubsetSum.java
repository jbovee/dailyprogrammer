import java.util.Arrays;

public class SubsetSum {
	public static void main(String args[]) {
		int[][] inputs = {{1, 2, 3}, {-5, -3, -1, 2, 4, 6}, {-1, 1}, {}, {-97364, -71561, -69336, 19675, 71561, 97863}, {-53974, -39140, -36561, -23935, -15680, 0}};

		for (int[] input : inputs) {
			System.out.print(Arrays.toString(input) + " -> ");
			if (isSubsetSum(input)) System.out.println("true");
			else System.out.println("false");
		}
	}

	public static boolean isSubsetSum (int[] inputs) {
		for (int inp1 : inputs) {
			if (inp1 == 0) return true;
			for (int inp2 : inputs) {
				if (inp2 == 0) return true;
				if ((inp1 + inp2) == 0) return true;
			}
		}
		return false;
	}
}