import difflib

def check_plagiarism(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()

    seq = difflib.SequenceMatcher(None, text1, text2)
    similarity_ratio = seq.ratio() * 100
    return similarity_ratio

# Example usage
file1 = 'file1.txt'
file2 = 'file2.txt'
similarity = check_plagiarism(file1, file2)
print(f"Similarity between {file1} and {file2}: {similarity}%")
