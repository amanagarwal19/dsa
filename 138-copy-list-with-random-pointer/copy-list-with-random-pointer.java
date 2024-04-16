/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        Node newlist=null;
        // 7-null,null

        Node curr = head;
        Node ans = newlist;
        HashMap<Node,Node> map = new HashMap<>();
        while(curr!=null){
            Node newNode = new Node(curr.val);
            if(newlist==null){
                newlist = newNode;
                map.put(curr,newNode);
                ans = newlist;
            }
            Node nextNode = curr.next;
            Node randomNode = curr.random;

            if(nextNode!=null){
                if(map.containsKey(nextNode)){
                    Node newRefOfNextNode = map.get(nextNode);
                    newlist.next = newRefOfNextNode;
                }else{
                    Node nextNewNode = new Node(nextNode.val);
                    newlist.next = nextNewNode;
                    map.put(nextNode,nextNewNode);
                }
            }else{
                newlist.next=nextNode;
            }
            if(randomNode!=null){
                if(map.containsKey(randomNode)){
                    Node newRefOfRandomNode = map.get(randomNode);
                    newlist.random = newRefOfRandomNode;
                }
                else{
                    Node randomNewNode = new Node(randomNode.val);
                    newlist.random = randomNewNode;
                    map.put(randomNode,randomNewNode);
                }
            }else{
                newlist.random = randomNode;
            }
            curr = curr.next;
            newlist = newlist.next;
        }
        return ans;
    }
}