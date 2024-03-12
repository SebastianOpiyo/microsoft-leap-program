using Internal;
using System;
using System.Collections.Generic;

class Solution {
    public int solution(int A)
    {
        // initiallize a set
        HashSet<int> absoluteValues = new HashSet<int>();

        // Iterate the list
        foreach(int item in absoluteValues)
        {
            absoluteValues.Add(Math.Abs (item));
        }
        return absoluteValues.Count;
    }
}

 