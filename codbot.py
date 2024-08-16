class Codbot_py:
    def __init__(self):
        self.knowledge_base = {
            "hello": "Hello! How can I help you?",
            "how are you": "I'm just a bot, but I'm functioning as expected. How can I help you?",
            "bye": "Goodbye! Have a great day!",
            "Who are You":"I am codbot, your personal coding partner",
            "What is Coding" : "Coding refers to the process of creating software by writing",
            "what is Python" : "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development",
            "What is Python?": "Python is an interpreted, high-level, and general-purpose programming language. It was created by Guido van Rossum and first released in 1991.",
            "What is the difference between a list and a tuple?": "A list is a mutable data structure that can hold any type of object. A tuple, on the other hand, is an immutable data structure that can hold only a fixed number of objects. The main difference between a list and a tuple is that lists can be modified after they are created, while tuples cannot.",
            "What is a dictionary in Python?": "A dictionary in Python is a mutable data structure that stores mappings of unique keys to values. Each key in a dictionary is associated with a value, and each key can map to only one value.",
            "How do you create a dictionary in Python?": "You can create a dictionary in Python using the curly braces {} notation. Here's an example: `my_dict = {'key1': 'value1', 'key2': 'value2'}`",
            "How do you access a value in a dictionary using its key?": "You can access a value in a dictionary using its key by using the square bracket notation. For example: `my_dict['key1']` would return 'value1'.",
            "How do you add a new key-value pair to a dictionary?": "You can add a new key-value pair to a dictionary using the assignment operator. For example: `my_dict['key3'] = 'value3'`",
            "How do you remove a key-value pair from a dictionary?": "You can remove a key-value pair from a dictionary using the `del` keyword. For example: `del my_dict['key1']` would remove the key-value pair with the key 'key1' from the dictionary.",
            "How do you iterate over a dictionary?": "You can iterate over a dictionary using the `items()` method, which returns a view object that displays a list of a dictionary's key-value tuple pairs. Here's an example: `for key, value in my_dict.items(): print(f'{key}: {value}')`",
            "What is the difference between a set and a list in Python?": "A set in Python is an unordered collection of unique elements. A list, on the other hand, is an ordered collection of elements. The main difference between a set and a list is that sets cannot contain duplicate elements, while lists can.",
            "How do you create a set in Python?": "You can create a set in Python using the curly braces {} notation, but you need to include only unique elements. Here's an example: `my_set = {1, 2, 3}`",
            "How do you add an element to a set in Python?": "You can add an element to a set using the `add()` method. For example: `my_set.add(4)` would add the number 4 to the set.",
            "How do you remove an element from a set in Python?": "You can remove an element from a set using the `remove()` method. For example: `my_set.remove(2)` would remove the number 2 from the set.",
            "How do you check if an element is in a set in Python?": "You can check if an element is in a set using the `in` keyword. For example: `if 1 in my_set:` would return True if the number 1 is in the set.",
            "How do you iterate over a set in Python?": "You can iterate over a set using a for loop. Here's an example: `for element in my_set: print(element)`",
            "What is the difference between a list, a tuple, and a set in Python?": "A list is a mutable data structure that can hold any type of object. A tuple is an immutable data structure that can hold only a fixed number of objects. A set is an unordered collection of unique elements. The main differences between a list, a tuple, and a set are their mutability, immutability, and the presence of duplicate elements.",
            "How do you create an empty dictionary, list, tuple, or set in Python?": "You can create an empty dictionary, list, tuple, or set in Python using the appropriate built-in function. Here are some examples: `my_dict = {}`, `my_list = []`, `my_tuple = ()`, `",
            "Resource Materials" : {
            "Getting Started": "https://docs.python.org/3/tutorial/index.html",
            "Syntax": "https://docs.python.org/3/reference/index.html",
            "Data Types": {
                "None": "https://docs.python.org/3/library/constants.html#None",
                "Numbers": "https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex",
                "Strings": "https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str",
                "Lists": "https://docs.python.org/3/library/stdtypes.html#lists",
                "Tuples": "https://docs.python.org/3/library/stdtypes.html#tuples",
                "Sets": "https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset",
                "Dictionaries": "https://docs.python.org/3/library/stdtypes.html#mapping-types-dict",
                "Booleans": "https://docs.python.org/3/library/stdtypes.html#boolean-objects",
                "Binary Sequences": "https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview",
            },
            "Modules": "https://docs.python.org/3/py-modindex.html",
            "Built-in Functions": "https://docs.python.org/3/library/functions.html",
            "Error Handling": "https://docs.python.org/3/tutorial/errors.html",
            "Control Flow": "https://docs.python.org/3/tutorial/controlflow.html",
            "Functions": "https://docs.python.org/3/tutorial/controlflow.html#defining-our-own-functions",
            "Object-oriented Programming": "https://docs.python.org/3/tutorial/classes.html",
            "File I/O": "https://docs.python.org/3/tutorial/inputoutput.html",
            "Standard Library": "https://docs.python.org/3/library/index.html",
            "C-API and Extensions": "https://docs.python.org/3/c-api/index.html",
            "dad":"7506461004"
            }
        }

    def search_knowledge_base(self, query):
        for key, value in self.knowledge_base.items():
            if query.lower() in key.lower():
                return value
        return None

    def generate_response(self, query):
        response = self.search_knowledge_base(query)
        if response is None:
            response = "I'm sorry, I don't know how to respond to that, Still Learing :)"
        return response

    def should_terminate(self, query) -> bool:
        if "thank you" in query.lower():
            return True
        return False
    
    def handle_query(self, query: str) -> bool:
        # Check if the user said "Thank you"
        if self.should_terminate(query):
            print("Codbot: You're welcome! Have a great day!")
            return False

        # Rest of the code for handling the query
        response = self.generate_response(query)
        print(response)
        return True


    ''' def handle_query(self, query):
        response = self.generate_response(query)
        print(response)'''

def main():
    bot = Codbot_py()
    while True:
        query = input("You: ")
        bot.handle_query(query)


if __name__ == "__main__":
    main()

    