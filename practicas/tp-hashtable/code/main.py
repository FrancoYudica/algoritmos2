import dictionary


if __name__ == "__main__":
    d = dictionary.Dictionary()
    d.insert(10, "Hello")
    d.display()
    print(f"The result of the search for key 10: {d.search(10)}")
    d.delete(10)

    d.display()