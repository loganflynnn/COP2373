# Paragraph Sentence counter
# Logan Flynn
# 10/18/2025

# Import the regular expressions module to help identify sentence boundaries
import re

# Prompt the user to enter a paragraph of text that may contain multiple sentences.
def get_paragraph():
    """Prompt the user to enter a paragraph."""
    return input("Enter a paragraph (can include sentences beginning with numbers):\n\n")

# Split the user's paragraph into individual sentences using regular expressions.
def split_sentences(paragraph):
    """Split the paragraph into sentences using regular expressions."""
    # Split when ., ?, or ! is followed by one or more spaces or end of line
    sentences = re.split(r'(?<=[.!?])\s+', paragraph.strip())

    # Remove any extra whitespace or empty strings
    return [s.strip() for s in sentences if s.strip()]

def main():
    """Main program function."""
    # Get paragraph input from the user.
    paragraph = get_paragraph()
    # Split into sentences.
    sentences = split_sentences(paragraph)

    print("\n--- Individual Sentences ---")
    for i, sentence in enumerate(sentences, start=1):
        # Print each numbered sentence
        print(f"{i}. {sentence}")

    # Show total count
    print(f"\nTotal number of sentences: {len(sentences)}")

if __name__ == "__main__":
    main()
