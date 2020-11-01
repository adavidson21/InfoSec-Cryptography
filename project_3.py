import hashlib
import math
import random
# Do NOT alter the import list!!!!

class Project3:

    def __init__(self):
        pass

    # BEGIN HELPER METHODS
    def integral_power_of_2(self, z: int):  # for Brent's Factorization implementation
        power = 1
        while power <= z:
            if power == z:
                return True
            power = power * 2

    def set_new_values_euclid(self, old, quotient, new): # for Extended Euclidean Algorithm
        # Takes care of the assignments and the actual calculation for ext_euclid()
        temp = new
        new = old - quotient * temp
        old = temp
        return new, old
    
    def ext_euclid(self, e, phi):
        # Extended Euclid's Algorithm
        # Pseudocode used from: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Modular_integers
        x = 0   
        old_x = 1
        original_phi = remainder = phi 
        old_remainder = e
         
        while remainder != 0: 
            quotient = old_remainder // remainder 
            remainder, old_remainder = self.set_new_values_euclid(old_remainder, quotient, remainder)
            x, old_x = self.set_new_values_euclid(old_x, quotient, x)
    
        if phi != 0:
            # ax + by = gcd(a,b)
            bezout_y = (old_remainder - old_x * e ) // phi
        else:
            bezout_y = 0
        
        # if the value is negative, add the original phi value to restore to a positive number
        if (old_x < 0):
            old_x = old_x + original_phi 
        
        return old_x, bezout_y # old_remainder = modular inverse

    def find_root(self, power, n):
        # Using binary search to find the root of a number (for large numbers)
        # ref: https://www.geeksforgeeks.org/find-cubic-root-of-a-number/
        minimum = 0
        maximum = n
        while minimum < maximum:
            middle = (minimum + maximum) // 2 # takes the middle value of the range
            if pow(middle,power) < n: # if the number^power is smaller than n, then we can increment up to test
                minimum = middle + 1
            else: # if it's not, then that's the largest value (so far) that we can test. 
                maximum = middle
        return minimum

    
    def find_crt(self, c_1, n_1, c_2, n_2, c_3, n_3):
        # Chinese Remainder Theorem
        # ref: https://en.wikipedia.org/wiki/Chinese_remainder_theorem#:~:text=In%20number%20theory%2C%20the%20Chinese,the%20divisors%20are%20pairwise%20coprime.
        # ref: https://www.youtube.com/watch?v=DKWnvyCsh9A
        # adding n and c values to list in order to iterate through them.
        c_vals = [c_1, c_2, c_3] 
        n_vals = [n_1, n_2, n_3]
        # initialization
        ans = 0
        product = 1
        for x in range(len(c_vals)):
            product *= n_vals[x] # the product of all given n values.
            
        for i in range(len(n_vals)):
            y = product // n_vals[i]
            ex, bezout = self.ext_euclid(n_vals[i], y) # extended euclid to find the bezout value (ex is mod inv that we don't need.)
            ans += (c_vals[i] * bezout * y)

        return ans % product
    # END HELPER METHODS

    def get_factors(self, n: int):
        # Brent's Factorization Method - Ref: http://connellybarnes.com/documents/factoring.pdf
        x = y = 2
        # we only have to check values up to the square root of the original n value.
        for i in range(1, n):
            x = ((x ** 2) + 1) % n
            s = math.gcd((x - y), n)
            if s != 1 and s != n:
                return s, n//s  # p, q
            if self.integral_power_of_2(i): # checks if the index is an integral power of 2
                y = x 

    def get_private_key_from_p_q_e(self, p: int, q: int, e: int):
        # d ≡ e^−1 mod φ(N)
        phi = (p-1) * (q-1)  # φ(N) = (p−1)∗(q−1)
        d, e = self.ext_euclid(e, phi) # use Extended Euclid's Algorithm to find the modular inverse.
        return d

    def task_1(self, n_str: str, d_str: str, c_str: str):
        n = int(n_str, 16)
        d = int(d_str, 16)
        c = int(c_str, 16)
        # function: pow(base, exponent, modulus) ref: https://www.w3schools.com/python/ref_func_pow.asp
        m = pow(c, d, n)
        return hex(m).rstrip('L')

    def task_2(self, password_hash: str):
        # The password list is prepopulated for your convenience
        common_password_list = ['123456', '12345', '123456789', 'password', 'iloveyou', 'princess', '1234567',
                                'rockyou', '12345678',
                                'abc123', 'nicole', 'daniel', 'babygirl', 'monkey', 'lovely', 'jessica', '654321',
                                'michael', 'ashley',
                                'qwerty', '111111', 'iloveu', '0', 'michelle', 'tigger', 'sunshine', 'chocolate',
                                'password1', 'soccer',
                                'anthony', 'friends', 'butterfly', 'purple', 'angel', 'jordan', 'liverpool', 'justin',
                                'loveme', '123123',
                                'football', 'secret', 'andrea', 'carlos', 'jennifer', 'joshua', 'bubbles', '1234567890',
                                'superman',
                                'hannah', 'amanda', 'loveyou', 'pretty', 'basketball', 'andrew', 'angels', 'tweety',
                                'flower', 'hello',
                                'elizabeth', 'hottie', 'tinkerbell', 'charlie', 'samantha', 'barbie', 'chelsea',
                                'lovers', 'teamo',
                                'jasmine', 'brandon', '666666', 'shadow', 'melissa', 'eminem', 'matthew', 'robert',
                                'danielle', 'forever',
                                'family', 'jonathan', '987654321', 'computer', 'whatever', 'dragon', 'vanessa',
                                'cookie', 'naruto',
                                'summer', 'sweety', 'spongebob', 'joseph', 'junior', 'softball', 'taylor', 'yellow',
                                'daniela', 'lauren',
                                'mickey', 'princesa', 'alexandra', 'alexis', 'jesus', 'estrella', 'miguel', 'william',
                                'thomas',
                                'beautiful', 'mylove', 'angela', 'poohbear', 'patrick', 'iloveme', 'sakura', 'adrian',
                                'alexander',
                                'destiny', 'christian', '121212', 'sayang', 'america', 'dancer', 'monica', 'richard',
                                '112233', 'princess1',
                                '555555', 'diamond', 'carolina', 'steven', 'rangers', 'louise', 'orange', '789456',
                                '999999', 'shorty',
                                '11111', 'nathan', 'snoopy', 'gabriel', 'hunter', 'cherry', 'killer', 'sandra',
                                'alejandro', 'buster',
                                'george', 'brittany', 'alejandra', 'patricia', 'rachel', 'tequiero', '7777777',
                                'cheese', '159753',
                                'arsenal', 'dolphin', 'antonio', 'heather', 'david', 'ginger', 'stephanie', 'peanut',
                                'blink182', 'sweetie',
                                '222222', 'beauty', '987654', 'victoria', 'honey', '0', 'fernando', 'pokemon', 'maggie',
                                'corazon',
                                'chicken', 'pepper', 'cristina', 'rainbow', 'kisses', 'manuel', 'myspace', 'rebelde',
                                'angel1', 'ricardo',
                                'babygurl', 'heaven', '55555', 'baseball', 'martin', 'greenday', 'november', 'alyssa',
                                'madison', 'mother',
                                '123321', '123abc', 'mahalkita', 'batman', 'september', 'december', 'morgan',
                                'mariposa', 'maria',
                                'gabriela', 'iloveyou2', 'bailey', 'jeremy', 'pamela', 'kimberly', 'gemini', 'shannon',
                                'pictures',
                                'sophie', 'jessie', 'hellokitty', 'claudia', 'babygirl1', 'angelica', 'austin',
                                'mahalko', 'victor',
                                'horses', 'tiffany', 'mariana', 'eduardo', 'andres', 'courtney', 'booboo', 'kissme',
                                'harley', 'ronaldo',
                                'iloveyou1', 'precious', 'october', 'inuyasha', 'peaches', 'veronica', 'chris',
                                '888888', 'adriana',
                                'cutie', 'james', 'banana', 'prince', 'friend', 'jesus1', 'crystal', 'celtic',
                                'zxcvbnm', 'edward',
                                'oliver', 'diana', 'samsung', 'freedom', 'angelo', 'kenneth', 'master', 'scooby',
                                'carmen', '456789',
                                'sebastian', 'rebecca', 'jackie', 'spiderman', 'christopher', 'karina', 'johnny',
                                'hotmail', '123456789',
                                'school', 'barcelona', 'august', 'orlando', 'samuel', 'cameron', 'slipknot', 'cutiepie',
                                'monkey1',
                                '50cent', 'bonita', 'kevin', 'maganda', 'babyboy', 'casper', 'brenda', 'adidas',
                                'kitten', 'karen',
                                'mustang', 'isabel', 'natalie', 'cuteako', 'javier', '789456123', '123654', 'sarah',
                                'bowwow', 'portugal',
                                'laura', '777777', 'marvin', 'denise', 'tigers', 'volleyball', 'jasper', 'rockstar',
                                'january', 'alicia',
                                'nicholas', 'flowers', 'cristian', 'tintin', 'bianca', 'chrisbrown', 'chester',
                                '101010', 'smokey',
                                'silver', 'internet', 'sweet', 'strawberry', 'garfield', 'dennis', 'panget', 'francis',
                                'cassie', 'benfica',
                                'love123', 'asdfgh', 'lollipop', 'olivia', 'cancer', 'camila', 'qwertyuiop',
                                'superstar', 'harrypotter',
                                'charles', 'monique', 'midnight', 'vincent', 'christine', 'apples', 'scorpio',
                                'jordan23', 'lorena',
                                'andreea', 'mercedes', 'katherine', 'charmed', 'abigail', 'rafael', 'icecream',
                                'mexico', 'brianna',
                                'nirvana', 'aaliyah', 'pookie', 'johncena', 'lovelove', 'abcdef', 'benjamin', '131313',
                                'gangsta', 'brooke',
                                '333333', 'hiphop', 'aaaaaa', 'mybaby', 'sergio', 'welcome', 'metallica', 'julian',
                                'travis', 'myspace1',
                                'babyblue', 'sabrina', 'michael1', 'jeffrey', 'stephen', 'love', 'dakota', 'catherine',
                                'badboy',
                                'fernanda', 'westlife', 'blondie', 'sasuke', 'smiley', 'jackson', 'simple', 'melanie',
                                'steaua', 'dolphins',
                                'roberto', 'fluffy', 'teresa', 'piglet', 'ronald', 'slideshow', 'asdfghjkl', 'minnie',
                                'newyork', 'jason',
                                'raymond', 'santiago', 'jayson', '88888888', '5201314', 'jerome', 'gandako', 'muffin',
                                'gatita', 'babyko',
                                '246810', 'sweetheart', 'chivas', 'ladybug', 'kitty', 'popcorn', 'alberto', 'valeria',
                                'cookies', 'leslie',
                                'jenny', 'nicole1', '12345678910', 'leonardo', 'jayjay', 'liliana', 'dexter', '232323',
                                'amores', 'rockon',
                                'christ', 'babydoll', 'anthony1', 'marcus', 'fatima', 'miamor', 'lover', 'chris1',
                                'single', 'eeyore',
                                'lalala', '252525', 'scooter', 'natasha', 'skittles', 'brooklyn', 'colombia', '159357',
                                'teddybear',
                                'winnie', 'happy', 'manutd', '123456a', 'britney', 'katrina', 'christina', 'pasaway',
                                'cocacola', 'mahal',
                                'grace', 'linda', 'albert', 'tatiana', 'london', 'cantik', '123456', 'lakers', 'marie',
                                'teiubesc',
                                '147258369', 'charlotte', 'natalia', 'francisco', 'amorcito', 'smile', 'paola',
                                'angelito', 'manchester',
                                'hahaha', 'elephant', 'mommy1', 'shelby', '147258', 'kelsey', 'genesis', 'amigos',
                                'snickers', 'xavier',
                                'turtle', 'marlon', 'linkinpark', 'claire', 'stupid', '147852', 'marina', 'garcia',
                                'diego', 'brandy',
                                'letmein', 'hockey', '444444', 'sharon', 'bonnie', 'spider', 'iverson', 'andrei',
                                'justine', 'frankie',
                                'pimpin', 'disney', 'rabbit', '54321', 'fashion', 'soccer1', 'red123', 'bestfriend',
                                'england', 'hermosa',
                                '456123', 'qazwsx', 'bandit', 'danny', 'allison', 'emily', '102030', 'lucky1',
                                'sporting', 'miranda',
                                'dallas', 'hearts', 'camille', 'wilson', 'potter', 'pumpkin', 'iloveu2', 'number1',
                                'katie', 'guitar',
                                '212121', 'truelove', 'jayden', 'savannah', 'hottie1', 'phoenix', 'monster', 'player',
                                'ganda', 'people',
                                'scotland', 'nelson', 'jasmin', 'timothy', 'onelove', 'ilovehim', 'shakira',
                                'estrellita', 'bubble',
                                'smiles', 'brandon1', 'sparky', 'barney', 'sweets', 'parola', 'evelyn', 'familia',
                                'love12', 'nikki',
                                'motorola', 'florida', 'omarion', 'monkeys', 'loverboy', 'elijah', 'joanna', 'canada',
                                'ronnie', 'mamita',
                                'emmanuel', 'thunder', '999999999', 'broken', 'rodrigo', 'maryjane', 'westside',
                                'california', 'lucky',
                                'mauricio', 'yankees', 'jamaica', 'justin1', 'amigas', 'preciosa', 'shopping', 'flores',
                                'mariah', 'matrix',
                                'isabella', 'tennis', 'trinity', 'jorge', 'sunflower', 'kathleen', 'bradley', 'cupcake',
                                'hector',
                                'martinez', 'elaine', 'robbie', 'friendster', 'cheche', 'gracie', 'connor', 'hello1',
                                'valentina', 'melody',
                                'darling', 'sammy', 'jamie', 'santos', 'abcdefg', 'joanne', 'candy', 'loser', 'dominic',
                                'pebbles',
                                'sunshine1', 'swimming', 'millie', 'loving', 'gangster', 'blessed', 'compaq', 'taurus',
                                'gloria', 'tyler',
                                'aaron', 'darkangel', 'kitkat', 'megan', 'dreams', 'sweetpea', 'bettyboop', 'jessica1',
                                'cynthia',
                                'cheyenne', 'ferrari', 'dustin', 'iubire', 'a123456', 'snowball', 'purple1', 'violet',
                                'darren', 'starwars',
                                'bestfriends', 'inlove', 'kelly', 'batista', 'karla', 'sophia', 'chacha', 'marian',
                                'sydney', 'pogiako',
                                'gerald', 'jordan1', '10203', 'daddy1', 'zachary', 'daddysgirl', 'billabong',
                                'carebear', 'froggy', 'pinky',
                                'erika', 'oscar', 'skater', 'raiders', 'nenita', 'tigger1', 'ashley1', 'charlie1',
                                'gatito', 'lokita',
                                'maldita', 'buttercup', 'nichole', 'bambam', 'nothing', 'glitter', 'bella', 'amber',
                                'apple', '123789',
                                'sister', 'zacefron', 'tokiohotel', 'loveya', 'lindsey', 'money', 'lovebug',
                                'bubblegum', 'marissa',
                                'dreamer', 'darkness', 'cecilia', 'lollypop', 'nicolas', 'google', 'lindsay', 'cooper',
                                'passion',
                                'kristine', 'green', 'puppies', 'ariana', 'chubby', 'raquel', 'lonely', 'anderson',
                                'sammie', 'mario',
                                'butter', 'willow', 'roxana', 'mememe', 'caroline', 'susana', 'kristen', 'baller',
                                'hotstuff', 'carter',
                                'stacey', 'babylove', 'angelina', 'miller', 'scorpion', 'sierra', 'sweet16', '12345',
                                'rocker', 'bhebhe',
                                'gustavo', 'marcos', 'chance', '123qwe', 'kayla', 'james1', 'football1', 'eagles',
                                'loveme1', 'milagros',
                                'stella', 'lilmama', 'beyonce', 'lovely1', 'rocky', 'daddy', 'catdog', 'armando',
                                'margarita', '151515',
                                'loves', 'lolita', '202020', 'gerard', 'undertaker', 'amistad', 'williams', 'qwerty1',
                                'freddy',
                                'capricorn', 'caitlin', 'bryan', 'delfin', 'dance', 'cheerleader', 'password2',
                                'PASSWORD', 'martha',
                                'lizzie', 'georgia', 'matthew1', 'enrique', 'zxcvbn', 'badgirl', 'andrew1', '141414',
                                '11111111', 'dancing',
                                'cuteme', 'booger', 'amelia', 'vampire', 'skyline', 'chiquita', 'angeles', 'scoobydoo',
                                'janine', 'tamara',
                                'carlitos', 'money1', 'sheila', 'justme', 'ireland', 'kittycat', 'hotdog', 'yamaha',
                                'tristan', 'harvey',
                                'israel', 'legolas', 'michelle1', 'maddie', 'angie', 'cinderella', 'lester', 'ashton',
                                'tazmania',
                                'remember', 'xxxxxx', 'tekiero', 'thebest', 'princesita', 'lucky7', 'peewee', 'paloma',
                                'buddy1', 'deedee',
                                'miriam', 'april', 'patches', 'regina', 'janice', 'cowboys', 'myself', 'lipgloss',
                                'jazmin', 'rosita',
                                'happy1', 'felipe', 'chichi', 'pangit', 'mierda', 'genius', '741852963', 'hernandez',
                                'awesome', 'walter',
                                'tinker', 'arturo', 'silvia', 'melvin', 'celeste', 'pussycat', 'gorgeous', 'david1',
                                'molly', 'honeyko',
                                'mylife', 'animal', 'penguin', 'babyboo', 'loveu', 'simpsons', 'lupita', 'boomer',
                                'panthers', 'hollywood',
                                'alfredo', 'musica', 'johnson', 'hawaii', 'sparkle', 'kristina', 'crazy', 'valerie',
                                'spencer', 'scarface',
                                'hardcore', '98765', '0', 'winter', 'hailey', 'trixie', 'hayden', 'micheal', 'wesley',
                                '242424',
                                '987654321', 'marisol', 'nikita', 'daisy', 'jeremiah', 'pineapple', 'mhine', 'isaiah',
                                'christmas', 'cesar',
                                'lolipop', 'butterfly1', 'chloe', 'lawrence', 'xbox360', 'sheena', 'murphy', 'madalina',
                                'anamaria',
                                'gateway', 'debbie', 'blonde', 'jasmine1', 'please', 'bubbles1', 'jimmy', 'beatriz',
                                'diamonds', 'whitney',
                                'friendship', 'sweetness', 'pauline', 'desiree', 'trouble', '741852', 'united',
                                'marley', 'brian',
                                'barbara', 'hannah1', 'bananas', 'julius', 'leanne', 'sandy', 'marie1', 'anita',
                                'lover1', 'chicago',
                                'twinkle', 'pantera', 'february', 'birthday', 'shadow1', 'qwert', 'bebita', '87654321',
                                'twilight',
                                'imissyou', 'pollito', 'ashlee', 'tucker', 'cookie1', 'shelly', 'catalina', '147852369',
                                'beckham',
                                'simone', 'nursing', 'iloveyou!', 'eugene', 'torres', 'damian', '123123123', 'joshua1',
                                'bobby', 'babyface',
                                'andre', 'donald', 'daniel1', 'panther', 'dinamo', 'mommy', 'juliana', 'cassandra']

        # Check each password in the list until the hashed password from the list matches the passed password hash
        for x in range(len(common_password_list)):
            password = common_password_list[x]
            hashed_password = hashlib.sha256(
                password.encode()).hexdigest()  # Gets the SHA256 hash
            if password_hash == hashed_password:
                return password

    def task_3(self, user_id_1: str, user_id_2: str, amount: int, prev_block_hash: str):
        nonce = 0  # initializing the nonce as 0, to be incremented.
        end_hash = user_id_1 + ":" + user_id_2 + ":" + str(
            amount) + prev_block_hash  # the static end of the string to be hashed
        hash = hashlib.sha256((str(
            nonce) + end_hash).encode()).hexdigest()  # initializes the hash with nonce = 0 + transaction string + previous block hash

        while hash[:2] != "00":  # if the proof of work is not 00, then we have not found the nonce value
            nonce += 1
            hash = hashlib.sha256(
                (str(nonce) + end_hash).encode()).hexdigest()  # recalculate the hash with the new nonce value
        return nonce  # if we get here, the lowest possible nonce value has been found

    def task_4(self, n_str: str, e_str: str):
        n = int(n_str, 16)
        e = int(e_str, 16)

        p, q = self.get_factors(n)  # get the factors of the given n   
        d = self.get_private_key_from_p_q_e(p, q, e) # use the factors and given e to calculate the private key

        return hex(d).rstrip('L')

    def task_5(self, given_public_key_n: int, given_public_key_e: int, public_key_list: list):
        # Get unique private key from the given public key
        # check the list, see which key makes gcd(n,k) > 1
        for i in range(len(public_key_list)): # check each item in the list
            if(math.gcd(given_public_key_n,public_key_list[i]) > 1): # if GCD > 1, then there is a factor (same random prime)
                p = math.gcd(given_public_key_n,public_key_list[i]) #GCD is one of the factors, p
                q = given_public_key_n // p # find the other factor using integer precision (for accuracy)

        d = self.get_private_key_from_p_q_e(p, q, given_public_key_e)
        return d

    def task_6(self, n_1_str: str, c_1_str: str, n_2_str: str, c_2_str: str, n_3_str: str, c_3_str: str):
        n_1 = int(n_1_str, 16)
        c_1 = int(c_1_str, 16)
        n_2 = int(n_2_str, 16)
        c_2 = int(c_2_str, 16)
        n_3 = int(n_3_str, 16)
        c_3 = int(c_3_str, 16)
       
        # ref: https://www.utc.edu/center-academic-excellence-cyber-defense/pdfs/course-paper-5600-rsa.pdf
        # ref: https://www.youtube.com/watch?v=DKWnvyCsh9A

        # Use Chinese Remainder Theroem to find c = m^3 mod(N1*N2*N3)
        c = self.find_crt(c_1, n_1, c_2, n_2, c_3, n_3) 
        m = int(self.find_root(3,c)) # c = m^3, therefore m = cubed root of c

        # Solve for m, which is an integer value, the line below will convert it to a string:
        msg = bytes.fromhex(hex(m).rstrip('L')[2:]).decode('UTF-8')
        return msg
