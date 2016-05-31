// ShortHand
int x = (expression)? 1 : 2;


// Point
Point point = new Point(x, y);


// Character
int a = Character.getNumbericValue('A')


// String
String 
string.charAt(i)
char [] content = string.toCharArray()
String fromArray = new String(content);

Integer 


// StringBuilder   FASTER >   StringBuffer  (thread safe)



// StringBuffer
StringBuffer buffer = new StringBuffer();
buffer.append("hello");
buffer.reverse()   // Reverses the string
buffer.length()




// Array
int[] arr= { 1,2,3 };
int[] arr = new int[3];
int arr[] = new int[]{5,90,35,45,150,3};
arr.length
Arrays.toString(arr)
Collections.sort(arr,Collections.reverseOrder());



// ArrayList
ArrayList
/*
    .add(value)
    .add( index, element);
    .get(int index);
    .isEmpty();
    .remove(index)
    .indexOf( );
    .list.isEmpty();
    .list.size();
    .list.get(index);

    // SORT
    Collections.sort(arrlist) //ascending
    Collections.sort(this.arrayList, Collections.reverseOrder()); //descending

    

    .addAll(Collection)     // Add collection to the end of the array
    .addAll(index, Collection);
    .clear   //remove all
    .retainAll(Collection)


*/



// Stack
Stack<Node> stack = new Stack<>();
Stack<TreeNode> stack = new Stack<TreeNode>();
/*
    push
    pop
    peek
    isEmpty



*/






Queue<TreeNode> queue = new LinkedList<TreeNode>();
add
remove



// Queue
Queue<Node> queue = new ArrayDeque<>();

/*
    Insert 
        queue.offer()

    Remove
        queue.poll()

    Peek
        queue.peek()

*/


// PriorityQueue
PriorityQueue<Integer> queue = new PriorityQueue<Integer>(new myComparator);
PriorityQueue<ListNode> queue= new 
     PriorityQueue<ListNode>(lists.size(),new Comparator<ListNode>(){
    @Override
    public int compare(ListNode o1,ListNode o2){
        if (o1.val<o2.val)
            return -1;
        else if (o1.val==o2.val)
            return 0;
        else 
            return 1;
    }
});


class myComparator implements Comparator<TreeNode>{
    public compare(TreeNode n1, TreeNode n2){
        return n2.val - n1.val; // descending        
    }
}
/*
    Insert
        offer

    Remove
        remove


    while (queue.size() != 0){
        
    }
    


*/






// HashMap
Map<String, List<Integer>> map = new HashMap<String, List<Integer>>();
/*
    get
    put

    clear()
    size()
    containsValue()
    containsKey()
    get(value)

    for(Type key: )..  map.keySet()    map.Values()
    

    Values & Keys as SET
        map.getKeys()
        map.values()

    
    Iterate
        for(Map.Entry<Character, Integer> entry: ht.entrySet()) {
            String key = entry.getKey();
            Object value = entry.getValue();
        }



    for (Map.Entry en: map.entrySet()){
        en.getKey();
        en.getValue();
    }

    TreeMap - HashMap in ascending.
*/ 



// HashSet
Set<Integer> set = new HashSet<Integer>();
/*
    .add
    .contains(num)
    .remove()


    Iterate
    for (String s : set) {
        System.out.println(s);
    }

*/


