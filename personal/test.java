/*
 * Complete the function below.
 */

	import java.util.Random;

	static int partition(int arr[], int left, int right, int pivot){
		int value = arr[pivot];
		swap(arr, pivot, right);

		int index = left;
		for (int i = left; i < right; i++) {
			if (arr[i] < value) {
				swap(arr, i, storeIndex);
				index++;
			}
		}
		swap(arr, right, index);
		return index;
	}
 

    static int selection(int[] array, int position, int length){
    	int left = 0;
    	int right = length - 1;
 		Random random = new Random(0, n);

 		while (right >= left){
 			int pIndex = partition(arr, left, right, rand.nextInt(right - left + 1) + left);

 			if (pIndex == position){
 				return arr[pIndex];
 			}

 			else if (pIndex < position) {
 				left = pIndex + 1; 				
 			}

 			else {
 				right = pIndex - 1;
 			}
 		}

 		return -1;
    }

    static void swamp(int[] arr, int i, int j){
    	if (i != j){
    		int aux = arr[i];
    		arr[i] = arr[j];
    		arr[j] = aux;
    	}
    }

    static int ThirdLargest(int[] arr) {
    	int element = 3;
    	int position = arr.length - 3;
    	int length = arr.length;

        result = partition(arr, position, length)
                
    }



