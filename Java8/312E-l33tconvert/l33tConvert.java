public class l33tConvert {
	private static final CharSequence[][] conv_table = {
		{"A","B","E","I","L","M","N","O","S","T","V","W"},
	    {"4","6","3","1","|","(\\/)","(\\)","0","5","7","/\\","´//"}
	};
	private static int conv_length = conv_table[0].length;

	public static boolean isL33t (String input) {
		Boolean check = false;
		CharSequence[] values = conv_table[1];
		for (CharSequence value : values) {
			if (input.contains(value)) {
				check = true;
				break;
			}
		}
		return check;
	}

	public static String convert (String input) {
		String output = input.toUpperCase();	
		if (isL33t(input)) {
			for (int i = 0; i < conv_length; i++) {
				output = output.replace(conv_table[1][i], conv_table[0][i]);
			}
			output = output.substring(0,1).toUpperCase() + output.substring(1).toLowerCase();
		}	
		else {
			for (int i = 0; i < conv_length; i++) {
				output = output.replace(conv_table[0][i], conv_table[1][i]);
			}
		}
		return output;
	}

	public static void main(String args[]) {
		String[] inputs = {"I am elite.", "Da pain!", "Eye need help!", "3Y3 (\\)33d j00 t0 g37 d4 d0c70r.", "1 n33d m4 p1llz!", "570R(\\/)"};

		for (String input : inputs) {
			System.out.println(input + " -> " + convert(input));
		}
	}	
}