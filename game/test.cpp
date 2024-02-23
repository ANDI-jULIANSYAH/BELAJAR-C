#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

string nama, n_club;
int potensial_ability, ability;
int apps, goal, assist, title_lague, champions, balon_dor, golden_boot;

void ability_set() {
    srand(time(0));
    double randomabillity = (double) rand() / RAND_MAX;
    if (randomabillity < 0.1) {
        ability = rand() % 28 + 100;
    } else if (randomabillity < 0.3) {
        ability = rand() % 11 + 90;
    } else if (randomabillity < 0.3) {
        ability = rand() % 11 + 80;
    } else if (randomabillity < 0.4) {
        ability = rand() % 11 + 70;
    } else if (randomabillity < 0.5) {
        ability = rand() % 11 + 60;
    } else if (randomabillity < 0.6) {
        ability = rand() % 11 + 50;
    } else if (randomabillity < 0.7) {
        ability = rand() % 11 + 40;
    } else {
        ability = rand() % 11 + 40;
    }
    potensial_ability = rand() % ability + 40;
}
int club_add() {
    string region[6] = {"Asia", "Eropa", "Afrika", "Amerika_utara", "Amerika_selatan", "Australia"};

    cout << "List Region" << endl;
    for (int i = 0; i < 6; i++) {
        cout << i << ": " << region[i] << endl;
    }

    cout << "Masukan Angka dari Benua Di atas (0-5) : ";
    int regionid;
    cin >> regionid;

    if (regionid < 0 || regionid > 5) {
        cout << "Invalid input. Plase enter a number between 0 - 5" << endl;
        club_add();
        return 1; // Return 1 when the user input is invalid
    }

    cout << "Kamu Memilih " << region[regionid] << "." << endl;
    cout << "Apakah Kamu Yakin?(y/n) : ";
    char regionconfirm;
    cin >> regionconfirm;
    if (regionconfirm == 'y') {
        if (regionid == 0) {
        }
    }
    return 0; // Return 0 when the user input is valid
}

void match() {
    double randomvalue;
    int goals_in_match = 0;
    for (int i = 0; i < 100; i++) {
        randomvalue = (double)rand() / RAND_MAX;

        if (randomvalue < 0.5) {
            goal = rand() % 2 + 1;
        } else if (randomvalue < 0.8) {
            goal = 3;
        } else if (randomvalue < 0.9) {
            goal = 4;
        } else if (randomvalue < 0.95) {
            goal = rand() % 2 + 5;
        } else if (randomvalue < 0.99) {
            goal = rand() % 2 + 7;
        }
        goals_in_match += goal;
    }
    apps++;
    goal += goals_in_match;
}

int main() {
    int awal = 0;
    while (true) {
        cout << "1. Mulai" << endl;
        cout << "2. Keluar" << endl;
        cout << "Masukan Angka Dari Opsi Di Atas (1/2) : ";
        int pilihan;
        cin >> pilihan;

        if (pilihan == 1) {
            if (awal == 0) {
                ability_set();
                awal = club_add();
            } else {
                cout << "Ability : " << ability << endl;
                cout << "Potensial : " << potensial_ability << endl;
                awal = club_add();
            }
        } else if (pilihan == 2) {
            break;
        } else {
            cout << "Invalid input. Plase enter 1 or 2." << endl;
        }
    }

    return 0;
}