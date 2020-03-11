from random import randrange, getrandbits
import math
def is_prime(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p
def generate_prime_number(length=1024):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p



def primeFactors(n): 
      
    # Print the number of two's that divide n 
    while n % 2 == 0:  
        n = (n//2)
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            n = (n // i)



def FindCoPrime(e):
    n = 2
    i = 0
    output = []
    while n < e:
        if  math.gcd(e,n) == 1:
            if is_prime(n):
                if n > 9999:
                    output.append(n)
                if n > 99999:
                    return output
        n+=1

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def encrypt(m, n, e):
    out = ((m**e) % n)
    return out

def decrypt(c, n, d):
    out = ((c**d) % n)
    return out


def handle_txt(txt):
    out = ""
    for char in txt:
        if char == "a" or char == "A":
            out += "65"
        elif char == "b" or char == "B":
            out += "66"
        elif char == "c" or char == "C":
            out += "67"
        elif char == "c" or char == "D":
            out += "68"
        elif char == "e" or char == "E":
            out += "69"
        elif char == "f" or char == "F":
            out += "70"
        elif char == "g" or char == "G":
            out += "71"
        elif char == "h" or char == "H":
            out += "72"
        elif char == "j" or char == "I":
            out += "73"
        elif char == "i" or char == "J":
            out += "74"
        elif char == "k" or char == "K":
            out += "75"
        elif char == "l" or char == "L":
            out += "76"
        elif char == "m" or char == "M":
            out += "77"
        elif char == "n" or char == "N":
            out += "78"
        elif char == "o" or char == "O":
            out += "79"
        elif char == "p" or char == "P":
            out += "80"
        elif char == "q" or char == "Q":
            out += "81"
        elif char == "r" or char == "R":
            out += "82"
        elif char == "s" or char == "S":
            out += "83"
        elif char == "t" or char == "T":
            out += "84"
        elif char == "u" or char == "U":
            out += "85"
        elif char == "v" or char == "V":
            out += "86"
        elif char == "w" or char == "W":
            out += "87"
        elif char == "x" or char == "X":
            out += "88"
        elif char == "y" or char == "Y":
            out += "89"
        elif char == "z" or char == "Z":
            out += "90"
    out = int(out)
    return out
        
        
# print(modinv(77,288))

p = generate_prime_number()
print("p:")
print(p)
print()

q = generate_prime_number()
print("q:")
print(q)
print()

n = p*q
print("n:")
print(n)
print()

phi = (p-1) * (q-1)
print("phi(n) / m:")
print(phi)
print()

e = FindCoPrime(phi)
e = e[randrange(1,len(e))]
print("e:")
print(e)
print()

d = modinv(e, phi)
print("d:")
print(d)

print("Press E for encryption or D for decryption")
choice = input()

if choice == "e" or choice == "E":
    print("Message to encrypt:")
    txt = input()
    e_txt = encrypt(txt, n, e)
    print("Encrypted:")
    print(e_txt)
elif choice == "d" or choice == "D":
    print("Message to decrypt:")
    e_txt = input()
    d_txt = decrypt(e_txt, n, d)
    print("Decrypted:")
    print(d_txt)
    print()


