def palindrome(word: str):
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False
        left = left + 1
        right = right - 1
        
    return True

if __name__ == "__main__":
    word = "racecar"
    isPalindrome = palindrome(word)
    print(isPalindrome)