#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int lines;
    std::vector<char> animals = std::vector<char>();
    std::cin >> lines;
    int ocelots = 0;
    for (int l = 0; l < lines; l++) { 
        char temp;
        std::cin >> temp;
        std::cout << temp;
        std::cout << '\n';
        animals.push_back(temp);
        if (temp == 'O') {
            ocelots++;
        }
    }
    std::vector<char> new_animals = std::vector<char>();
    int bells = 0;
    while (ocelots > 0) {
        for (int i = 0; i < animals.size(); i++) {
            char animal = animals[i];
            if (animal == 'Z') {
                new_animals.push_back('Z');
            } else {
                int num_turn = i;
                int cnt = std::count(animals.begin(), animals.begin() + i, 'O');
                
                ocelots -= cnt;
                std::cout << cnt << '\n';
                //std::fill(new_animals.begin(), animals.begin() + num_turn, 'Z');           
                //new_animals.push_back('Z');
                //ocelots--;
            }
            bells++;
        }
    }
    return 0;
}
