#include <iostream>
#include <string>
#include <bitset>

int main() {
    int lines;
    std::string bit_string = "";
    std::cin >> lines;
    for (int l = 0; l < lines; l++) { 
        char temp;
        std::cin >> temp;
        //std::cout << temp;
        //std::cout << '\n';
        if (temp == 'O') {
            bit_string += '1';
        } else {
            bit_string += '0';
        }
    }
    //std::cout << bit_string << '\n';
    std::bitset<60> b(bit_string);
    unsigned char c = (b.to_ulong());
    std::cout << static_cast<int>(c);
    return 0;
    
}
