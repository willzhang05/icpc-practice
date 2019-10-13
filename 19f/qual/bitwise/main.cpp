#include <iostream>
#include <string>
#include <vector>

int main() {   
    int n;
    int k;
    std::vector<int> circle;
    std::cin >> n >> k;
    //printf("%d %d\n", n, k);
    for (int i = 0; i < n; i++) {
        int b;
        std::cin >> b;
        circle[i] = b;
        printf("%d\n", circle[i]);
    }
    return 0;
}
