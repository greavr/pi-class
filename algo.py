# For any given array of numbers put all the 0's at the end
# sample array [1,4,0,1,5,2,7,0,3,1,7,0,0,4,7,0]
# expected output [1,4,1,5,2,7,3,1,7,4,7]

def reorder_zeros(input):
    # Accept an array of any size and push the 0's to the end
    # order the numbers from smallest to lowest and reverse order
    result = sorted(input)
    result.reverse()
    return result

def remove_zeros(input):
    result = []
    for i in input:
        if not i == 0:
            result.append(i)

    return result

def remove_value(input, value_to_remove):
    result = []
    for i in input:
        if not i == value_to_remove:
            result.append(i)
    return result

# Create a function / alo which returned the top 10 most common words in a list
input_string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way--in short, the period was so far like the present period that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."

def top_ten_words(input):
    result = {}
    max_len = 10

    word_list = input.split()
    for a_word in word_list:
        # Check if word already in list
        if a_word in result:
            # Word found increment counter
            result[a_word] += 1
        else:
            # Word not found add value
            result[a_word] = 1

    # Return top 10
    print(result)


top_ten_words(input_string)