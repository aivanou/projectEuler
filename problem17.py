
def find():
    d1=['one','two','three','four','five','six','seven','eight','nine']
    d2=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    h = 'hundred'
    d3=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    a = 'and'
    sm = 0
    [sm+len(n) for n in d1]
    [sm+len(n) for n in d2]
    [sm+len(n) for n in d3]

    for n1 in d1:
        for n2 in d2:
            sm+=len(n1)+len(n2)
    for n1 in d1:
        sm+=len(n1)
        sm+=len(h)
        for n2 in d1:
            sm +=len(n1)+len(h)+len(a)+len(n2)
        for n2 in d2:
            sm +=len(n1)+len(h)+len(a)+len(n2)
        for n2 in d3:
            sm +=len(n1)+len(h)+len(a)+len(n2)
        for n2 in d2:
            for n3 in d1:
                sm+=len(n1)+len(h)+len(a)+len(n2)+len(n3)
                print  n1,n2,n3
    sm+=len('one')
    sm+=len('thousand')
    print sm

if __name__ == '__main__':
    find()

public static void main(String[] args){
    
}

public static void printNextGreaterElement(int[] arr){
    Stack<Integer> stack = new Stack<>();
    int[] res=new int[arr.length];
    res[arr.length-1]=-1;
    stack.push(arr[arr.length-1]);
    for(int i=arr.length-2;i>=0;--i){
        while(!stack.isEmpty() && stack.peek() < arr[i]){
            stack.pop();
        }
        if(stack.isEmpty()){
            res[i]=-1;
        }else{
            res[i]=stack.peek();
        }
        stack.push(arr[i]);
    }
    System.out.println(Arrays.toString(res));
}

public static void sortStack(Stack<Integer> stack){
    if(stack.isEmpty()) return;
    int el = stack.pop();
    sortStack(stack);
    insert(stack,el);
}

public static void insert(Stack<Integer> st,int el){
    if(st.isEmpty() || st.peek()>=el){
        st.push(el);
    }else{
        int temp = st.pop();
        insert(st,el);
        st.push(temp);
    }
}

public static int[] stockPlan(int[] arr){
    int[][] tb = new int[arr.length][2];
    Stack<Integer> st = new Stack<>();
    int[] res = new int[arr.length];
    for(int i=0;i<arr.length;++i){
        int num = 0;
        while(!st.isEmpty() && tb[st.peek()][0] <= arr[i]){
            num+=tb[st.peek()][1];
            st.pop();
        }
        res[i]=num+1;
        tb[i][0]=arr[i];
        tb[i][1]=num+1;
        st.push(i);
    }
    return res;    
}




