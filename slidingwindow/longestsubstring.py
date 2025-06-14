def longestsubstring(s):
  char = {}
  left = maxlen = 0
  for right in range(len(s)):
    if s[right] in char and char[s[right]]>=left:
      left = char[s[right]]+1
    char[s[right]] = right
    maxlen = max(maxlen,right-left+1)
  return maxlen
s = "abcabcde"
print(longestsubstring(s))   
                 