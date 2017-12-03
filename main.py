# This is an ebay program to check shipping of an item
# This works with home depot right now
# This is devloped by Jason Gahr 11/25/2017

import main_functions as m

def main():
    
    print("Welcome to the ebay shipping tool\nCreated by Jason Gahr")
    m.change_directory()
    m.download_links()
    return

if __name__ == "__main__":
    main()