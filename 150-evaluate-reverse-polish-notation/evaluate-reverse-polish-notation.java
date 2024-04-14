class Solution {
    public int evalRPN(String[] tokens) {
        int n = tokens.length;

        if(n==1){
            return Integer.parseInt(tokens[0]);
        }

        int op1,op2;
        int curr=0;
        Stack<Integer> stack = new Stack<>();
        stack.push(Integer.parseInt(tokens[0]));
        stack.push(Integer.parseInt(tokens[1]));

        for(int i=2;i<n;i++){
            String str = tokens[i];
            if(str.equals("+") || str.equals("*") ||str.equals("/") || str.equals("-")){
                op2 = stack.pop();
                op1 = stack.pop();

                if(str.equals("+") )
                    curr = op1+op2;
                if(str.equals("-") )
                    curr = op1-op2;
                if(str.equals("/") )
                    curr = op1/op2;
                if(str.equals("*") )
                    curr = op1*op2;
                stack.push(curr);
                }
            else
                stack.push(Integer.parseInt(str));
        }
        return curr;
    }
}