#include <bits/stdc++.h>

using namespace std;

string random_letter(vector<string> alphabet) {
    return alphabet[rand() % 4];
}

int main(int argc, char **argv) {
    if (argc != 3) {
        cout << "Type ./synthetic_genome_gen num_genome repeat_size" << endl;
    }

    int num_genome = atoi(argv[1]);
    int X_size = atoi(argv[2]); 
    string X, name, prefix, suffix = ""; 

    vector<string> alphabet;
    alphabet.push_back("A");
    alphabet.push_back("T");
    alphabet.push_back("G");
    alphabet.push_back("C");

    // sequence before X 
    for (int i = 0; i < 500; i++) {
        prefix += random_letter(alphabet);
    }

    // sequence after X
    for (int i = 0; i < 500; i++) {
        suffix += random_letter(alphabet);
    }

    // Generate the random sequence X 
    for (int i = 0; i < X_size; i++) {
        X += random_letter(alphabet);
    }

    // Generate the .fa files     
    for (int i = 0; i < num_genome; i++) {
        string curr_genome;
        int j = i + 1;

        curr_genome += prefix;
        while (j > 0) {
            curr_genome += X;
            j --;
        }
        curr_genome += suffix;
        //cout << curr_genome.size() << endl;
        
        fstream file;
        name = "genome" + to_string(i) + ".fa";
        file.open(name, ios::out);
        
        if(!file.is_open()) {
            cout << "error in file creation !!";
        } else {
            file << ">" << "genome" << to_string(i) << endl;
            int start = 0;
            int size = 80;
            while (start+size < curr_genome.size()) {
                //cout << start << ", " << start+size << endl;
                string current = curr_genome.substr(start,size);
                file << current << endl;
                start += size;
            }
            file << curr_genome.substr(start,curr_genome.size());
        }
    }
    return 0;
}