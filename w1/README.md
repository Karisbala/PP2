# Problem A: 188041. Venom vs Carnage.

Venom tries to defeat his opponent Carnage. Venom has a number `n`. Since Carnage is his complete opposite, Venom needs to find out the number `k` - opposite in bit representation to the number `n`.

### Input format
You are given number `n - (1 <= n <= 1000)`

### Output format

Print `k` - number that has all inverted bits of `n`.

### Examples

```
Input: 23
Output: -24

Input: 129
Output: -130
```


# Problem B: 196111. Boris the Chef.

Chef Boris is testing new dishes. He wants to find the most delicious dishes. But Boris is not only a chef, but also a programmer. Therefore, a dish is considered tasty if the sum of the ASCII codes of all letters in its name is more than 300. Write a program that will find tasty dishes..

### Input format
You are given number `S` - name of the dish

### Output format

Print "It is tasty!" if the dish is tasty. Otherwise, print "Oh, no!."

### Examples

```
Input: OK
Output: Oh, no!

Input: sosisochki
Output: It is tasty!

```


# Problem C: 187587. To Lowercase.

Given a string `s`. Create a function `toLowercase` that will replace every uppercase in `s` with the same lowercase letter and return the lowercase string.

### Input format
String `s - (1 <= s.size() <= 100)`

### Output format

Print the string that you will get as a result of the `toLowercase` function.

### Examples

```
Input: aLmAtY
Output: almaty

Input: pp1
Output: pp1
```


# Problem D: 186885. Asman + Systems = Astems

Asman is a programmer, but he is also an engineer. He is standing in the cafeteria after a hard day and trying to understand why there are 1024 bytes in 1 kilobyte? Indeed, in physics, a kilo is 10 to 3 degrees, but for programmers it is differently like that. And he realizes that he is confused. Help Asman. You need to convert bytes to kilobytes, or kilobytes to bytes.

### Input format
You are given char `z` - command that convert, `c` - how many digits after the decimal point (if number integer no need to output the remainder). If `z=\k'` it is mean need to convert from byte to kilobyte. If `x=\b'` it is mean need to convert from kilobyte to byte.

### Output format

Print the result of conversion.

### Examples

```
Input: 
3032
k
6
Output: 2.960938

Input: 
12
b
Output: 12288
```


# Problem E: 188812. Gunner.

Edya decided to practice rifle shooting. He is given a random number of cartridges if the distance to the target does not exceed `500` meters and is also a prime number and when this number of cartridges is even, he is guaranteed to hit the target. Otherwise, he misses.
The number `n` is entered from the keyboard - the distance to the target as well as the number of cartridges `f`. The program must calculate whether the shooter will hit the target.

### Input format
Two integers in one line: `n` - distance `1 <= n <= 1000`
`f` - count cartridges `1 <= f <= 1000`

### Output format

String
If miss print: "Try next time!"
Else print: "Good job!"

### Examples

```
Input: 443 10
Output: Good job!

Input: 883 976
Output: Try next time!
```


# Problem F: 193526. Tears.

Daniil wanted to create an if-else problem, but it turned out as always: BFS, DFS... But this time it’s not such a task, it’s a simple task. You are given `n` numbers. Each number represents how much Daniil worked per week.

If he worked less than or equal to 10 hours, output: "Go to work!"

If more than 10 and less than or equal to 25, output: "You are weak"

If more than 25 hours, but less than or equal to 45, output: "Okay, fine"

If more than 45 hours, output: "Burn! Burn! Burn Young!"

### Input format
First line integer `n` - amount of numbers  `(0 <= n <= 100)`
Next lines `n` integers `ai(0 <= ai <= 168)`

### Output format

In each line output string depens on work hours.

### Examples

```
Input: 
3
5
25
45
Output: 
Go to work!
You are weak
Okay, fine

Input: 
4
0
168
11
48
Output: 
Go to work!
Burn! Burn! Burn Young!
You are weak
Burn! Burn! Burn Young!
```


# Problem G: 195718. To decimal.

You are given some binary string (consisting only from ‘1’ and ‘0’). Convert this string to the decimal number.

`Solve only using recursion!`

### Input format
The only line of input contains a binary string `n (1 <= |s| <= 30)`

### Output format

Convert string `s` to decimal number and print it.

### Examples

```
Input: 1100
Output: 12

Input: 1000000000000000
Output: 32768
```


# Problem H: 187532. First and last occurrence. 

Given a string `s` and letter `t`. If `s` contains the letter `t` only once, print its index. If it occurs two or more times, print the index of its first and last occurrence. If the letter t does not appear in the given line, do not print anything.
### Input format
Given two strings `s (1 <= s <= 100)`, `t(t.size() == 1)`

### Output format

Print the result.

### Examples

```
Input: 
midterm
m
Output: 
0 6

Input: 
concentrate
t
Output: 
6 9
```


# Problem I: 189327. Dimash that's too bad.

Dimash hacked the database and he got all the email addresses to send out spam. But Dimash’s program works differently.
The program should only receive logins from `@gmail.com`
Help the young hacker get the logins. Help him do it!!!

### Input format
`n` - num of words `(1 <= n <= 1000)`
`n` strings `s` in each line.

### Output format

Clear mails in each line.

### Examples

```
Input: 
2
1234ghdsh@gmail.com
2523sdfg@mail.cry
Output: 
1234ghdsh

Input:
3
helloguys@gmail.com
goodbye@mail.com
helloagain
Output: 
helloguys
```


# Problem J: Levy the cryptographer

Captain Levi was able to decipher a secret message from Erwin Smith last time and saved the squad! Finally, it’s time to come up with a new cipher. Now Levi wants to use only words with a certain number of letters in the message. The number of letters in the desired word is more than 3. Help Levi to write a program that will automatically decrypt the message.

### Input format
You are given a message in one string.

### Output format

Print the space-separeted decrypted message in one line.

### Examples

```
Input: hello boris how are you
Output: hello boris how are you 

Input: I am fine and what about u?
Output: fine and what about 
```