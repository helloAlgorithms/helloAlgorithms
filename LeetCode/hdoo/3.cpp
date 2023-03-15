#include <algorithm>
#include <iostream>
#include <map>

class Solution
{
  public:
	int lengthOfLongestSubstring(std::string s)
	{
		int length = 0, maxlength = 0, j = 0;

		std::map<char, int> mp;

		for (int i = 0; i < s.size(); i++)
		{
			mp[s[i]]++;
			length++;
			while (mp[s[i]] > 1)
			{
				mp[s[j++]]--;
				length--;
			}
			maxlength = std::max(maxlength, length);
		}
		return maxlength;
	}
};
