def substring(s):
    count = 0
#     # chunks = [ ]
    for i in range(0,len(s),3):
        chunk = s[i:i+3]
#         # chunks.append(chunk)

#     # return chunks
        if len(set(chunk))==3 and len(chunk)==3:
            count +=1
    return count
print(substring("abcddf"))
# def substring(s):
#     count = 0
#     for i in range(len(s) - 2):  # Use sliding window of size 3
#         chunk = s[i:i+3]
#         if len(set(chunk)) == 3:  # All characters unique
#             count += 1
#     return count
# print(substring("abccf"))

