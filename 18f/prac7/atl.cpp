#include <iostream>

int main() {
    int lines;
    int t, h;
    std::cin >> lines;
    for (int l = 0; l < lines; l++) { 
        std::cin >> t >> h;
        std::cout << t << " " << h;
        std::cout << '\n';
    }
    return 0;
}
