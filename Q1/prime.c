#include <stdio.h>
#include <math.h>

int is_prime(unsigned int n){
	int i;
	if( n%2==0 && n!=2 ) return 0;
	if (n%3!=0){
		for (i=5; i*i<=n; i=i+6){
			if(n%i==0 || n%(i+2)==0){
				return 0;
			}
		}
	}else{
		return 0;
	}

	return 1;

}

// https://tutorialspoint.dev/algorithm/mathematical-algorithms/multiplicative-inverse-under-modulo-m
unsigned int modInverse(unsigned int a, unsigned int m) {
    a = a%m; 
    for (unsigned int x=1; x<m; x++)
		if ((a*x) % m == 1) 
        	return x; 
}

// pow(message,d,n) overflows so we use the following function
// https://stackoverflow.com/questions/8496182/calculating-powa-b-mod-n
unsigned long long modpow(unsigned long long base, unsigned long long exp, unsigned long long modulus) {
  base %= modulus;
  unsigned int result = 1;
  while (exp > 0) {
    if (exp & 1) result = (result * base) % modulus;
    base = (base * base) % modulus;
    exp >>= 1;
  }
  return result;
}

int main(){
	unsigned int n, minnum=1, maxnum=127670779, e = 7, phi_n, p, q;

	int i;
	for (n=minnum|1; n<=maxnum; n=n+2){
		if (is_prime(n) == 1 && maxnum % n == 0 && is_prime( maxnum / n ) == 1){
			p = n;
			q = maxnum/n;
			break;
		}
	}

	unsigned int message1 = 32959265, message2 = 47487400,d;

	n = maxnum; // p*q = maxnum
	phi_n = (p-1)*(q-1);
	d = modInverse(e,phi_n);

	printf("mess=%u d=%u n=%u\n", message1,d,n);

	printf("message1 : %llu\n", modpow(message1,d,n) );
	printf("message2 : %llu\n", modpow(message2,d,n) );

}
