def count_words(content):
    return len(content.split())

def count_char(content, only_alpha, as_list=False):
    result = {}
    lc_content = content.lower()
    for char in lc_content:
        if (not only_alpha) or char.isalpha():
            if not char in result:
                result[char] = 1
            else:
                result[char] += 1
    if as_list:
        list_result = []
        for char in result:
            list_result.append({"char":char,"count":result[char]})
        list_result.sort(reverse=True,key=sort_on)
        return list_result

    return result

def sort_on(element):
    return element["count"]

def generate_report(content, title):
    wordcount = count_words(content)
    charcount = count_char(content, True, True)

    print(f"--- Begin report of {title} ---")
    print(f"{wordcount} words found in the document")
    print(f"")
    for char in charcount:
        print(f"The '{char["char"]}' character was found {char["count"]} times")
    print(f"--- End report ---")


def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        generate_report(file_contents,book_path)


main()