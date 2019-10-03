#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<std::string> as(n);
    std::vector<std::string> bs(n);

    for (int i = 0; i < n; i++) {
        std::cin >> as[i];
        std::cin >> bs[i];
    }

    printf("\n");
    
    return 0;
}
