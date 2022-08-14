#include <vector>
#include <iostream>
int main(){
	std::vector<int> got;
	for (int i = 0; i < 2; i++) {
		int t;
		std::cin >> t;
		got.push_back(t);
	}
	int sum = 0;
	for (std::vector<int>::iterator p  = got.begin(); p != got.end();p++) {
		sum += *p;
	}
		std::cout << sum;
}
