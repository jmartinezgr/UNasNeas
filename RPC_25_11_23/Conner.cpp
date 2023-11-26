#include <iostream>
#include <unordered_set>

std::unordered_set<int> obtener_numeros(int limite, int paso) {
    std::unordered_set<int> numeros;

    if (paso == 0) {
        for (int i = 1; i <= limite; ++i) {
            numeros.insert(i);
        }
    } else {
        int numero = 1 + paso;
        while (numero <= limite) {
            numeros.insert(numero);
            numero += 1 + paso;
        }
    }

    return numeros;
}

int main() {
    int casos;
    std::cin >> casos;

    for (int i = 0; i < casos; ++i) {
        int r, v, a, n;
        std::cin >> r >> v >> a >> n;

        std::unordered_set<int> conjunto_n = obtener_numeros(n, r);
        conjunto_n.insert(obtener_numeros(n, v).begin(), obtener_numeros(n, v).end());
        conjunto_n.insert(obtener_numeros(n, a).begin(), obtener_numeros(n, a).end());

        std::cout << conjunto_n.size() << std::endl;
    }

    return 0;
}
