#include <iostream>
#include <vector>
#include <complex>
#include <functional>
#include <cmath>
#include <string>


using namespace std;
int LENG;
typedef complex<double> cpx;
typedef vector<cpx> vtcpx;
typedef function<void(vtcpx&)> rev_bit;


rev_bit reverse_bit() {
    vector<int> rev_arr(LENG);

    for (int i = 0; i < LENG; ++i) {rev_arr[i] = i;}

    int half = LENG >> 1;
    int j = 0;

    for (int i = 1; i < LENG; ++i) {
        int bit = half;
        while (j >= bit) {
            j -= bit;
            bit >>= 1;
        }
        j += bit;

        if (i < j) {swap(rev_arr[i], rev_arr[j]);}
    }

    auto func = [rev_arr](vtcpx& arr) {
        for (int i = 0; i < LENG; ++i) {
            int j = rev_arr[i];
            if (i < j) {swap(arr[i], arr[j]);}
        }
    };

    return func;
}


void fft(vtcpx& arr, rev_bit& func, bool inv=false) {
    func(arr);
    int size = 2, half = 1;
    cpx pow_w;
    double two_pi = 2 * M_PI * (inv ? 1 : -1);

    while (size <= LENG) {
        cpx w = exp(cpx(0, two_pi / size));
        
        for (int i = 0; i < LENG; i += size) {
            pow_w.real(1); pow_w.imag(0);

            for (int j = i; j < i + half; ++j) {
                int k = j + half;
                cpx a = arr[j], b = arr[k] * pow_w;
                arr[j] = a + b; 
                arr[k] = a - b;
                pow_w *= w;
            }
        }

        half = size; size <<= 1;
    }

    if (inv) {for (int i = 0; i < LENG; ++i) {arr[i] /= LENG;}}
}


int main() {
    string a, b;
    cin >> a >> b;

    if (a == "0" || b == "0") { 
        cout << "0" << endl;
    
    } else {
        int a_size = size(a), b_size = size(b);
        LENG = 1 << (static_cast<int>(log2(a_size + b_size)) + 1);

        vtcpx a_arr(LENG), b_arr(LENG);
        for (int i = 0; i < a_size; ++i) a_arr[i].real(a[i] - 48);
        for (int i = 0; i < b_size; ++i) b_arr[i].real(b[i] - 48);

        rev_bit rev_bit_func = reverse_bit();
        fft(a_arr, rev_bit_func); fft(b_arr, rev_bit_func);
        for (int i = 0; i < LENG; ++i) {a_arr[i] *= b_arr[i];}
        fft(a_arr, rev_bit_func, true);

        vector<int> answer(LENG);
        for (int i = LENG - 1; i > 0; --i) {
            int n = answer[i] + round(a_arr[i].real());
            answer[i - 1] += n / 10;
            answer[i] = n % 10;
        }
        answer[0] += round(a_arr[0].real());
        
        if (answer[0]) cout << answer[0];
        for (int i = 1; i < a_size + b_size - 1; ++i) cout << answer[i];
        cout << endl;
    }
}
