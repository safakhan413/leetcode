# 692. Top K Frequent Words
# Medium
# Topics
# Companies
# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. 
# Sort the words with the same frequency by their lexicographical order.

 

# Example 1:

# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:

# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
def topKFrequent(words, k):
    from collections import Counter, OrderedDict

    print(words,k)
    counter = Counter(words)

    a = sorted(counter, key= lambda word: (-counter[word], word))

    # a = OrderedDict(Counter(words))
    # Order
    print(a)
    return a[:k]
    # return list(a.keys())[:k]



# words = ["i","love","leetcode","i","love","coding"]
# k = 2
# print(topKFrequent(words, k))
# # Output: ["i","love"]


# words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
# k = 4


words = ["i","love","leetcode","i","love","coding"]
k = 3


print(topKFrequent(words, k))
# Output: ["the","is","sunny","day"]