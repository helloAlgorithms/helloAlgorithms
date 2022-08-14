#include <iostream>

int main(){
	std::ios_base::sync_with_stdio(0);
	int cnt;
	std::cin >> cnt;
	int got;
	int min = 1000001;
	int max = -1000001;
	for (int i = 0; i < cnt ; i++) {
		std::cin >> got;
		if (got < min)
			min = got;
		if (got > max)
			max = got;
	}
	std::cout << min << " " <<  max;
}

 

