import time
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', filename="logfile.log")

def add(*args):
    result = args[0]
    for i in args[1:]:
      result += float(i)
    return result
def subt(*args):
    result = args[0]
    for i in args[1:]:
      result -= float(i)
    return result
def mply(*args):
    result = args[0]
    for i in args[1:]:
        result *= float(i)
    return result
def div(*args):
    try: 
        result = args[0]
        for i in args[1:]:
            result /= float(i)
        return result
    except:
        logging.error("ZeroDivisionError, Div")
        print("\nBłąd!\nNie można dzielić przez 0!")
def expo(*args):
    if args[0] == 0 and args[1] == 0:
        logging.error("ZeroDivisionError, Expo")
        print("\nBłąd!\nNie można podnieść 0 do potęgi 0.\nSą tacy, którzy twierdzą, że result powinien być 0 lub 1 ale obowiązuje zasada, że takie działanie nie ma miejsca ;)\nPo prostu jest nic, czyli:")
    else:
        return args[0] ** args[1]
def root(*args):
    if args[1] > 0:
        return args[0] ** (1/args[1])
    else:
        logging.error("ZeroDivisionError, Root")
        print("\nBłąd!\nNie można pierwiastkować przez stopień 0!") 

logging.info("Session init.")
print("KALKULATOR by PD\n")
time.sleep(1)
print("Ważna informacja.\nJeżeli chcesz użyć liczb dziesiętnych to zamiast przecinka użyj kropki.")
print("Np. 26,17 - źle, 26.17 - dobrze :)\n")

print("Możesz wybrać rodzaj kalkulatora:\n1. Zwykły\n2. Z bajerem ;)\n")
calc_type = input("Wybierz swój kalkulator :) : ")

def calc():
    while True:
        logging.info("User input in progress.")
        def user_input_choice():
            maths = [
                    "1. Dodawanie.",
                    "2. Odejmowanie.",
                    "3. Mnożenie.",
                    "4. Dzielenie.",
                    "5. Potęgowanie.",
                    "6. Pierwiastkowanie."
            ]
            print("\nWybierz działanie wpisując odpowiednią cyfrę.", *maths, sep = '\n')
            choice = input("Twój wybór to... ")
            return choice
        choice = user_input_choice()

        if choice in ('1', '2', '3', '4'):  
            def user_input_multi_nums():
                input_nums = input("Podaj co najmniej dwie liczby, rozdzielając je spacją: ")
                nums = input_nums.split(' ')
                for value in nums:
                    try:
                        float(value)
                    except:
                        logging.warning("Wrong input found on nums.index(value).Input correct variable (number) request.")
                        print(f"'{value}' nie jest liczbą!\n")
                        valued = input(f"Wpisz liczbę żeby podmienić '{value}': ")
                        nums[nums.index(value)] = valued
                nums = [float(value) for value in nums]
                return nums
            nums = user_input_multi_nums()
            
        else:
            def user_input_two_nums():
            
                descr = []
                des_1 = (", która będzie potęgowana: ", ", która będzie potęgą: ")
                des_2 = (", którą chcesz spierwiastkować: ", ", która jest stopniem pierwiastka: ")
                if choice == '5':
                    descr.extend(des_1)
                elif choice == '6':
                    descr.extend(des_2)

                while True:
                    num1 = input(f"Podaj liczbę{descr[0]}")
                    try:
                        float(num1)
                        break
                    except:
                        logging.warning("Wrong input: word or letter instead of number.Input correct variable (number) request.")
                        print("To nie jest liczba!")
                while True:
                    num2 = input(f"Podaj liczbę{descr[1]}")
                    try:
                        float(num2)
                        break
                    except:
                        logging.warning("Wrong input: word or letter instead of number.Input correct variable (number) request.")
                        print("To nie jest liczba!")
                num1 = float(num1)
                num2 = float(num2)
                return num1, num2
            num1, num2 = user_input_two_nums()

        logging.info("Printing result.")
        result = 0
        if choice == '1':
            result = "Rozwiązanie: suma liczb ", nums, " = ", add(*nums)
        elif choice == '2':
            result = "Rozwiązanie: różnica liczb ", nums, " = ", subt(*nums)
        elif choice == '3':
            result = "Rozwiązanie: iloczyn liczb ", nums, " = ", mply(*nums)
        elif choice == '4':
            result = "Rozwiązanie: iloraz liczb  ", nums, " = ", div(*nums)
        elif choice == '5':
            result = f"Rozwiązanie: {num1} podniesiona do potęgi {num2} = ", expo(num1, num2)
        elif choice == '6':
            result = f"Rozwiązanie: {num1} √ ({num2}) = ", root(num1, num2)
        
        print(*result)
        next_calc = input("\nWykonać kolejne obliczenie?\nT =Tak, N = Nie: ")
        if next_calc.lower() == "n":
            logging.info("End of program, runs correctly")
            print("Dzięki za skorzystanie z mojego kalkulatora ;)")
            exit(0)
        else:
            logging.info("Next calculation in current session")
            pass    

def type_calc():
    if calc_type == '1':
        calc()
    elif calc_type == '2':
        logging.info("Curiosity is the first step to hell :D")
        print("Uruchamiam kalkulator z bajerem...")
        time.sleep(3)
        print("\nBang!\nSpotyka się dwóch programistów:")
        time.sleep(1)
        print("- Słyszałem, że straciłeś pracę. Jak to jest być bezrobotnym?")
        time.sleep(2)
        print("- To było najgorsze pół godziny mojego życia!\n")
        time.sleep(2)
        print("Niezły bajer, co? :D")
        time.sleep(3)
        print("Zaraz uruchomię ZWYKŁY kalkulator ;)")
        time.sleep(2)
        calc()
type_calc()