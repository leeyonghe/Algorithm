public static void main(String[] args) {
	while (true) {
		System.out.print(">>>>>>>>>>>>>>>>> Start");
		Scanner sc = new Scanner(System.in); // OR replace System.in with file to read
		List<Integer> input = new ArrayList<Integer>();
		while(sc.hasNext()){
			input.add(sc.nextInt());
			if (input.size() >= 2) {
				break;
			}
		}
		System.out.println(">>>>>>>>>>>>>>>>> input : "+input);
		input.sort(Comparator.naturalOrder());
		final int start_int = input.get(0);
		System.out.println(">>>>>>>>>>>>>>>>> start_int : "+start_int);
		final int end_int = input.get(1);
		System.out.println(">>>>>>>>>>>>>>>>> end_int : "+end_int);
		List<Integer> inputArray = new ArrayList<Integer>();
		for (int j = start_int; j <= end_int; j++) {
			int result = j;
			int cycle = 1;
			do {
				if (result%2 == 0) {
					result = result / 2;
				} else {
					result = result*3 + 1;
				}
				cycle++;
			} while (result != 1);
			System.out.println(">>>>>>>>>>>>>>>>> cycle : "+cycle);
			inputArray.add(cycle);
		}
		inputArray.sort(Comparator.reverseOrder());
		System.out.println(">>>>>>>>>>>>>>>>> inputArray Max : "+inputArray.get(0));
	}
}