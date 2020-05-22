# Hackerrank - merge_the_tools https://www.hackerrank.com/challenges/merge-the-tools

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        char = ""
        for j in range(i,i+k):
            if string[j] not in char:
                char += string[j]
        print(char)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
