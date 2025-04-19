#  Personal Library Manager
#  This script manages a personal library of books, allowing users to add, remove, and view books.
#  It also allows users to search for books by title or author and provides a simple command-line interface for interaction.
#  The script uses a JSON file to store the library data, ensuring that the data persists between runs.

#  Intall uv by running the following command: powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" 
#  uv --version
#  streamlit --version
#  uv init personal_library_manager  (Creating a New Project Folder)
#  uv add streamlit
#  .venv\Scripts\activate

import streamlit as st
import json

#  Load and Save Library Data
def load_library(filename='library.json'):
    """Load the library data from a JSON file. If the file does not exist, return an empty list."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []   

def save_library(library, filename='library.json'):
    """Save the library data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(library, file, indent=4)

#  Initialize Library
library = load_library()

#  My App Title
st.title("📚Personal Library Manager")

#  Main Menu of the App
menu = st.sidebar.radio("✔️Select An Option", ["View Library", "Add Book", "Remove Book", "View Books", "Search Books", "Save & Exit"])

#  1- View Library
if menu == "View Library":
    st.subheader("📙Your Library")
    if library:
        for book in library:
            st.write(f"✅{book['title']} by {book['author']}")
    else:
        st.write("❎Your library is empty. Add some books!")

#  2- Add Book
elif menu == "Add Book":
    st.subheader("📘Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author Name")
    if st.button("Add Book"):
        if title and author:
            library.append({"title": title, "author": author})
            save_library(library)
            st.success(f"✅Added '{title}' by {author} to your library.")
        else:
            st.error("❎Please provide both title and author.")

#  3- Remove Book
elif menu == "Remove Book":
    st.subheader("📗Remove a Book")
    title = st.text_input("Book Title to Remove")
    if st.button("Remove Book"):
        for book in library:
            if book['title'].lower() == title.lower():
                library.remove(book)
                save_library(library)
                st.success(f"✅Removed '{title}' from your library.")
                break
        else:
            st.error(f"❎'{title}' not found in your library.")

#  4- View Books
elif menu == "View Books":
    st.subheader("📕View All Books")
    if library:
        for book in library:
            st.write(f"✅{book['title']} by {book['author']}")
    else:
        st.write("❎Your library is empty. Add some books!")

#  5- Search Books
elif menu == "Search Books":
    st.subheader("📓Search for a Book")
    search_term = st.text_input("Enter title or author to search")
    if st.button("Search"):
        results = [book for book in library if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower()]
        if results:
            st.write("Search Results:")
            for book in results:
                st.write(f"✅{book['title']} by {book['author']}")
        else:
            st.write("❎No books found matching your search.")

#  6- Save & Exit
elif menu == "Save & Exit":
    st.subheader("🚪Save and Exit")
    save_library(library)
    st.success("🔐Library saved. You can close the app now.")

