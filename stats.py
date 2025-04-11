def count_words_in_text(contents):
    split_contents = len(contents.split())
    return split_contents


def count_characters_in_text(contents):
    counted = {}
    for i in contents.lower():
        counted[i] = counted.get(i, 0) + 1
    return counted
    

def sorted_list(dicitonary_goes_here):

    char_list = []

    for char, count in dicitonary_goes_here.items():
        char_info = {"character": char, "count": count}
        char_list.append(char_info)
        char_list.sort(reverse=True, key=lambda dict: dict["count"])
    return char_list




    
    
    
    
    
    # varje dictionary ska vara {"character": "char", "count": "num" }
    # Sedan ska dessa läggas in i en lista med append kanske ?
    # Jag tror att jag måste loopa igenom counted för att plocka ur varje key och value för sig
    # En list comprehension kanske också kan fungera
    # Sedan ska dessa returnas då antar fast bara valuen i varje key som då alltså är bokstaven och mängden
    # använd .sort()