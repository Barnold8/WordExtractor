


def clean_arr(word_array):

    arr = word_array

    for i in range(len(arr)):
        arr[i] = arr[i].strip("\n")
    
 
    return arr

def main():

    PATH = input("Please input the relative file path:\t")
    x = int(input("What words do you want to extract from the file?\n1.Nouns\n2.Verbs\n\nPick one:\t"))
    words = ""



    if x == 1:
        with open("nouns.txt","r") as file:
            
            test_cases = file.readlines()
            test_cases = clean_arr(test_cases)
    else:
        with open("verbs.txt","r") as file:
            test_cases = file.readlines()
            test_cases = clean_arr(test_cases)

    with open(PATH,"r") as file:

        lines = file.readlines()
        lines = clean_arr(lines)
        for i in range(len(lines)):
            lines[i] = lines[i].lower()
            f = lines[i].split()
            if(len(f) > 0):
                for j in range(len(f)):
                    words +=  f[j] + " "


        words = words.split()
        #print(words)
        extraction = [[i for i in words if i in test_cases]]
        print(extraction)
        

        
        
            
        



main()

    
