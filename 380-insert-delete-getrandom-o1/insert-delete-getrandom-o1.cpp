class RandomizedSet {
public:

    unordered_map<int,int> map; // [value, index_in_list]
    vector<int> list;
    int idx;
    RandomizedSet() {
        idx=0;
    }
    
    bool insert(int val) {
        // cout<<"insert\n";
        if(map.find(val)==map.end()) //val not in map
        {
            map[val] = idx;
            list.push_back(val);
            idx++;
            return true;
        }
        return false;
    }
    
    bool remove(int val) {
        // cout<<"remove\n";
        if(map.find(val)==map.end()) //not found
            return false;

        //get index of value from map
        int index = map[val];
        int n = list.size();
        //update index of last element because we will swap it and remove the current element.
        int lastElementOfList = list[n-1];
        map[lastElementOfList] = index;
        map.erase(val); //remove from map

        //swap element in array
        int temp = list[index];
        list[index] = list[n-1];
        list[n-1] = temp;
        list.pop_back();
        idx--;
        return true;

    }
    
    int getRandom() {
        int n = list.size();
        int randIdx = (rand()%n);
                // cout<<"get random"<<n<<"    "<<randIdx<<endl;;
        return list[randIdx];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */