class Solution {
public:
    string convert(string s, int numRows) {

        if(numRows==1)
            return s;

        int n = s.length();
        int charsInSection = 2*numRows-2;
        string answer;

        // for each row identify characters in each section to be appended
        for(int currRow = 0; currRow < numRows; currRow++){
            int idx = currRow; //0,1,2,3
            // this idx goes across each row's different sections
            cout<<"\n";
            while(idx < n){
                // write a single character for each section's first and last row , 
                // else write second character of each row also
                answer+=s[idx]; 

                // if first row or last row, the next character for that
                // row is 2n-2 characters away because each section has 2n-2
                // characters
                int nextCharDistance;
                if(currRow !=0 && currRow != numRows-1)
                {
                    // there are 2*currRow characters seen
                    // there are charsInSection - seenCharacters left
                    // that is the distance to the next character for that row
                    int charsSeen = 2*currRow;
                    nextCharDistance = charsInSection - charsSeen;
                    if(idx+nextCharDistance <n )
                        answer += s[idx+nextCharDistance];
                }
                // dont go to next character for same row, because
                // nextchardistance will be relative to current row starting value
                // and the difference between 2 characters of the same row will oscilate
                // between a large and small number because characters between same section
                // will have a larger gap than 2 characters across sections
                // So, BETTER IS TO JUMP TO NEXT SECTION AND NOT NEXT CHARACTER
                idx = idx + charsInSection;
            }
        }
        return answer;
    }
};