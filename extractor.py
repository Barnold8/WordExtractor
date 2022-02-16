def clean_arr(word_array):

    arr = word_array

    for i in range(len(arr)):
        arr[i] = arr[i].strip("\n")
    return arr

def MD(words,extracted):

    ind = 0

    with open("output.md","w") as file:
        file.write("# Before processing")
        file.write("\n\n")
        for w in words:
            file.write(w)
            file.write(" ")
        file.write("\n\n# After processing: ")
        file.write("\n\n")
        for i in range(len(words)):

            if(words[i] == extracted[ind]):
                ind += 1
                file.write(" **")
                file.write(words[i])
                file.write("** ")
            else:
                file.write(words[i])
                file.write(" ")
            
        

def main():

    PATH = input("Please input the relative file path:\t")
    try:
        x = int(input("What words do you want to extract from the file?\n1.Nouns\n2.Verbs\n\nPick one:\t"))
    except Exception as e:
        print("Cannot parse letters.\n\nExiting program")
        exit()
    
    
    words = ""
    # taken from https://www.thoughtco.com/common-suffixes-in-english-1692725
    suffixes_noun = ["acy","al","ance","ence","dom","er","or","ism","ist","ity","ty","ment","ness","ship","sion","tion"]
    suffixes_verb = ["ate","en","ify","fy","ize","ise"]
    # taken from https://www.thoughtco.com/common-suffixes-in-english-1692725        
     


    if x == 1:
        with open("nouns.txt","r") as file:
            
            test_cases = file.readlines()
            test_cases = clean_arr(test_cases)
            curr_length = len(test_cases)

            for i in range(curr_length):
                for j in range(len(suffixes_noun)):
                    test_cases.append(test_cases[i] + suffixes_noun[j])

    else:
        with open("verbs.txt","r") as file:
            test_cases = file.readlines()
            test_cases = clean_arr(test_cases)
            curr_length = len(test_cases)

            for i in range(curr_length):
                for j in range(len(suffixes_verb)):
                    test_cases.append(test_cases[i] + suffixes_verb[j])

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
        extraction = [i for i in words if i in test_cases]
        extraction = [i for i in extraction if len(i) > 1]
        print("Words found:\n")

        for i in range(len(extraction)):
            print("Word {}: \t{}".format(i,extraction[i]))

        MD(words,extraction)

main()  
