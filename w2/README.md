# Problem A: 190087. Asmay.

Asman has always loved jumping. And so he thought, what if you jump over the array? And he had an idea for a problem. You are given an integer array. You are initially located at the 1 element in array, and each element represents your maximum jump length at that position.

### Input format
You are given an integer array.
`1 <= array.size() <= 1000`
`0 <= array[i] <= 10000`

### Output format

Print 1 if you can reach the last index, or 0 otherwise.

### Examples

```
Input: 2 3 1 1 4
Output: 1

Input: 3 2 1 0 4
Output: 0
```


# Problem B: 187378. Maximum product of two elements. 

You are given an integer array. Print the maximum product of any two elements in the array.

### Input format
The number of elements in the array - n`(2 <= n <= 500)` and array a`(1 <= ai <= 100)`.

### Output format

Integer number - the maximum product of any two elements.

### Examples

```
Input: 
4
5 2 1 7
Output: 35

Input: 
7
9 4 7 4 8 9 10
Output: 90

```

### Notes

In the first example, the maximum product is 35 because if we multiply 5(0th) and 7(3rd) elements of the array we will get 35.


# Problem C: 187698. Diagonal x.

You are given int n the size of table, you have to create multiplication table and output diagonal x*y

### Input format
Input integer N where `1 <= N <= 100`

### Output format

Output 2d-array where 1 row and column iterated to N and diagonal are result of multiplication

### Examples

```
Input: 5
Output: 
0 1 2 3 4 
1 1 0 0 0 
2 0 4 0 0 
3 0 0 9 0 
4 0 0 0 16 
```

### Notes

Index starts from 0


# Problem D: 188131. Tsunami.

Scientists have reported that an earthquake in the sea will soon occur near Paradis Island. This could trigger a large tsunami that could damage the island. However, we know that if the tsunami height is an even number, then it should go in the opposite direction, towards Marley. Draw tsunami moving in the desired direction.
### Input format
You are given integer `N`- the height of tsunami.

### Output format

Draw the tsunami.

### Examples

```
Input: 5
Output: 
....#
...##
..###
.####
#####

Input: 6
Output: 
#.....
##....
###...
####..
#####.
######
```


# Problem E: 187639. XOR in an array.

You’re given 2 integer numbers `n` and `x`. For solving this problem you need to create array `arr` where `arr[i] = x + 2*i` and the size of array is equal to given `n`. Remember that array starts from 0. Print the bitwise XOR of all elements of the array `arr`.

### Input format
Two integers numbers: n`(1 <= n <= 1000)`, x`(0 <= x <= 1000)`

### Output format

Print the single integer - XOR of all items of the `arr`.

### Examples

```
Input: 4 3
Output: 8

Input: 5 0
Output: 8
```

### Notes

In the first example, array `arr` is equal to [3, 5, 7, 9], answer = (3 ^ 5 ^ 7 ^ 9) = 8.


# Problem F: 196670. Compensations.

Due to the end of finals, KBTU administration decided to give every student whose GPA is greater than 3.5 some compensation. But the accounting department messed up a little bit, so they have payed the compensation more than once to some students. Also the amount of the compensations were different.

But they decided to show their kindness, and they need your help. You should find the students(-s) who received maximum compensation, and for every other students you need to calculate the amount of money they have to receive so that in total they received the same amount as the student(-s) who was/were paid the most.

### Input format
The first line contains an integer `n`, the number of payments made by accounting department `(1 <= n <= 100000)`
Each of the next `n` line contains a student’s surname `si` and the amount of payment he/she received `xi` `si(1 <= si <= 100,1 <= xi <= 10000)`

### Output format

You should print the students’ surnames in alphabetical and the amount of money they have to receive to equalize all the compensations across students. If the student already received maximum compensation across all students, print “<STUDENT_SURNAME> is lucky!”.

### Examples

```
Input: 
6
era 100
era 500
pes 900
era 34
asman 5000
pes 10000
Output: 
asman has to receive 5900 tenge
era has to receive 10266 tenge
pes is lucky!

Input: 
5
LongSurname 10000
VeryLongSurname 7000
SomeOtherSurname 5000
LongSurname 10000
SomeOtherSurname 4000
Output: 
LongSurname is lucky!
SomeOtherSurname has to receive 11000 tenge
VeryLongSurname has to receive 13000 tenge
```


# Problem G: Demon slayer

The Demon Hunters went into battle. Several demons are in front of them. Every demon hunter can kill the k demons, with a demon that has a weakness for the ability of the hunter. A demon with water weakness can be killed by a hunter with water abilities. But demon cannot be killed by a hunter who, for example, has the ability to flame.

How many demons will survive after the battle?

### Input format
First line integer `n` - amount of demons `(1 <= n <= 100000)`.
Next `n` lines consist of strings `d` and `w` - demon name and demon weakness.
Next line integer `m` - amount of hunters `(1 <= m <= 100000)`.
Next `m` lines consist of strings `h`, `a` and `k` integer - hunter name, ability, the number of demons a hunter can kill

### Output format

Print - "Demons left:" and number of remaining demons

### Examples

```
Input: 
5
akaza water
zenitsu_brother thunder
Susamaru water
Spider_demon_father water
Spider_demon_son sun
3
tanjiro water 10
zenitsu thunder 1
giyuu water 11
Output: Demons left: 1

Input: 
5
Muzan sun
Spider_Sister insect
Gyokko fog
Akaza flame
Gyokko_2 fog
3
Muichiro fog 1
Rengoku flame 100000
Shinobu insect 500
Output: Demons left: 2
```


# Problem H: Closest point

You are given single point `P` in `x,y` coordinates system, and also list of `n` points.

You have to sort points by closest point to `P`.

Closest point - Ближайшая точка.

### Input format
In the first line given `x, y` coordinates of point `P`.

In the second line given `n`, number of points.

In the next `n` lines given `x,y` coordinates of each points.

### Output format

Print the array after sorting by closest point to .

### Examples

```
Input: 
0 0
5
5 5
2 10
1 2
2 2
3 3
Output: 
1 2
2 2
3 3
5 5
2 10

Input: 
5 5
5
2 10
3 4
2 1
3 3
6 6
Output: 
6 6
3 4
3 3
2 1
2 10
```


# Problem I: 77244. Discs.

Akniet lost her cartoon discs. Her brother Askat bought many discs and put those discs to her shelf. He can put discs to the shelf or take at the shelf. Operations are described by a pair of numbers. Number 1 mean - putting to the end of the shelf and after followed the name of the disc, 2 - taking from the begin of the shelf. There is a guarantee that we invoke the second operation if the shelf isn’t empty. At the beginning the shelf is empty. Your task is to find what discs Askat took.

### Input format

You are given N integer number, then N,`(1 <= N <= 100)` operations that Askat performed.

### Output format

Print the name of discs that Askat took to each second operation.

### Examples

```
Input: 
5
1 discovery
1 TomandJerry
2
1 comedy
2
Output: 
discovery TomandJerry 

Input:
2
1 disney
2
Output: 
disney 
```


# Problem J: 195834. Boris and Passwords.

Boris is still working on his website. This time he decided to check all the passwords that his users use. Boris believes that a password is considered strong if it contains uppercase, lowercase letters and numbers. Write a program that will find unique strong passwords.

### Input format
First line contains integer N,`(1 <= N <= 1000)` - number of passwords. Next lines contain passwords.

### Output format

In the first line print total number of strong passwords. Then, print on separate lines all strong unique passwords in sorted order.

### Examples

```
Input: 
5
KotletaBoris001
Romawka5
burger
WATER
Romawka5
Output: 
2
KotletaBoris001
Romawka5 

Input: 
7
qwerty
qwerty11
QwErTy1
tSarka9
tSarka
qwerty11
tsarkA1
Output: 
3
QwErTy1
tSarka9
tsarkA1
```

### Notes

In the first example, the `KotletaBoris001` password has uppercase, lowercase letters and numbers, so it is strong.


# Problem K: 195846. Final essay.

Students wrote an essay on the final exam in Philosophy. The teacher wants to count how many unique words there are in the essay. Help him write such a program.

### Input format
You are given a set of words in one line - a student’s essay.

### Output format

In the first line print number of unique words. Then, print each unique word in separated line sorted lexicographically.

### Examples

```
Input: 
Hello, Boris! How are you?
Output: 
5
Boris
Hello
How
are
you
```

### Notes

Punctuation marks should not be counted. Uppercase and lowercase letters differ. For example, `boris != Boris`, so both of them are unique.
Also remember, lexicographically lower case letters greater that that upper case letters. For example `a` 
and `b` are greater that `A` in lexicographically order


# Problem L: 194034. Open Closed.

Help Eva with the task. A finite sequence consisting of left and right brackets of various specified types:

{,(,[,},)and]

is given. It is necessary to determine whether it is possible to add numbers and signs of arithmetic operations to it so that the correct arithmetic expression is obtained.

### Input format
Input string S,`(1 <= S <= 10^8)`

### Output format

Output answer Yes or No.

### Examples

```
Input: [(([
Output: No

Input: []
Output: Yes
```


# Problem M: 197032. Important dates.

Professor of History during the lecture says a lot of important dates, but they come in random-like order. You should listen for all the dates the professor says, and then sort them to restore the chronological order of the events.

### Input format
You are given some amount of dates (not more than `10^5` and in in the format “dd mm yyyy”) each on next line. After the last date comes symbol “0”. It is guaranteed that each date is valid.

### Output format

Print the dates in the chronological order in the format “dd mm yyyy”.

### Examples

```
Input: 
11 09 0201
08 05 1945
23 10 1953
07 01 0001
12 12 2021
22 06 1941
21 12 2012
0
Output: 
07 01 0001
11 09 0201
22 06 1941
08 05 1945
23 10 1953
21 12 2012
12 12 2021

Input: 
31 12 2000
01 10 1852
30 09 1852
01 01 2001
01 09 1853
0
Output: 
30 09 1852
01 10 1852
01 09 1853
31 12 2000
01 01 2001
```


# Problem N: 194739. We got stronger.

Game N has a counter system that counts all frags in the game. We are given unknown number of players. Daniil wants to divide them into pairs, according to a simple system. The first in line is combined with the last, the second with the penultimate, and so on. Implement this in your program, use a vector!

### Input format
Integer in each line. Input ends with the number 0.

### Output format

Print numbers by the sum of the ﬁrst and last elements of the original array, the second by the sum of the second and penultimate, etc. if the array has an odd number of elements, the central element does not change.

### Examples

```
Input: 
1
2
3
1
2
3
0
Output: 
4 4 4 

Input: 
2
5
10
30
40
0
Output: 
42 35 10
```
### Notes

You can use vector.


# Problem O: 147221. String calculator.

Do you remember calculator problem from the first quiz? Now you need to calculate sum of two numbers, but digits are given as triplet of uppercase English characters. For example "ONETWOSEV" will be equal to `127`. And you should print the answer in the same way as given numbers, using triplets of characters. SOLVE BY USING FUNCTIONS!

### Input format
You’re given string consisting only from uppercase English letters, denoting the expression you need to calculate.

### Output format

Output result of given expression using triplets of letters.

### Examples

```
Input: 
ONETWOTHR+FOUFIVSIX
Output: 
FIVSEVNIN

Input: 
ONETWOTHRFOUFIVSIXSEVEIGNINZER+ZER
Output: 
ONETWOTHRFOUFIVSIXSEVEIGNINZER
```

### Notes

Solutions without function will be graded zero.
ONE - `1`
TWO - `2`
THR - `3`
FOU - `4`
FIV - `5`
SIX - `6`
SEV - `7`
EIG - `8`
NIN - `9`
ZER - `0`