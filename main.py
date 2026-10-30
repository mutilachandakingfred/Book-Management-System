def main():

    try:
        #initialise books list
        bookList = []
        infile = open("theBookList.txt", "r")
        line = infile.readline()
        while line:
            bookList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()

    except FileNotFoundError:
        print("No existing <theBookList.txt> file is found.")
        print("Creating a new <theBookList.txt> file...")
        bookList = []
        
    
    choice = 0
    while choice != 4:
        print("*** Books Manager ***")
        print("1. Add Book")
        print("2. Lookup a book")
        print("3. Display all books")
        print("4. Exit")
        choice = int(input("Enter your choice: "))



        if choice == 1:
            print("Adding a book...")
            nBook = input("Enter the name of the book>>> ")
            nAuthor = input("Enter the author of the book>>> ")
            nPages = int(input("Enter the number of pages>>> "))
            bookList.append([nBook, nAuthor, nPages])

        elif choice == 2:
            print("Looking up a book...")
            keyword = input("Enter the name of the book to lookup>>> ")
            for book in bookList:
                if keyword in book:
                    print(book)

        elif choice == 3:
            print("Displaying all books...")
            for i in range(len(bookList)):
                print(bookList[i])

        elif choice == 4:
            print("Exiting the program...")
            break
    print("Thank you for using the Books Manager!")            


    #Saving to external file

    outfile = open("theBookList.txt", "w")
    for book in bookList:
        outfile.write(",".join(map(str, book)) + "\n")
    outfile.close()
    


if __name__ == "__main__":
    main()
    