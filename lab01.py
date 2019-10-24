import random

def main(x):
    sum = 0
    for count in range(x):
        randnums = random.randrange(1,10)
        sum += randnums 
        print(randnums, '; ')
    print('sum =', sum)
    print('avg = ', sum/x)

if __name__ == "__main__":
	main(5)