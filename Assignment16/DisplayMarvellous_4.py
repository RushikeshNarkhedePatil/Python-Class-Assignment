# 4.Write a program which display 5 times Marvellous on screen.
# Output :
# Marvellous
# Marvellous
# Marvellous
# Marvellous
# Marvellous

def DisplayMarvellous():
    for _ in range(5):  # Loop to print 5 times _ is used as a throwaway variable
        print("Marvellous")

def main():
    DisplayMarvellous()

if __name__ == "__main__":
    main()