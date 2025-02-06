'''3. Create a Book class that contains multiple Chapters, where each Chapter has a title and page count.
Write code to initialize a Book object with three chapters and display the total page count of the book'''

print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
class Chapter:
    def __init__(self, title, pcount):
        self.title = title
        self.pcount = pcount
    
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.chapters = []

    def add_chapter(self, chapter):
        self.chapters.append(chapter)

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")
        print("\nChapters:-")
        for i in self.chapters:
            print(f"Title: {i.title}, Page Count: {i.pcount}")
        print(f"Total Page Count = {sum([i.pcount for i in self.chapters])}")

b1 = Book("Harry Potter", "J.K. Rowling")
b1.add_chapter(Chapter("Sorcere's Stone", 200))
b1.add_chapter(Chapter("Chamber of Secrets", 300))
b1.add_chapter(Chapter("Prisoner of Azkaban", 400))
b1.display()


# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Title: Harry Potter, Author: J.K. Rowling

# Chapters:-
# Title: Sorcere's Stone, Page Count: 200
# Title: Chamber of Secrets, Page Count: 300
# Title: Prisoner of Azkaban, Page Count: 400
# Total Page Count = 900