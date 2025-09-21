# Spam Detection
# Logan Flynn
# 09/16/25

def build_keywords():
    """
    Return a list of 30 common spam words/phrases.
    Keep this simple so it’s easy to edit for your instructor’s rubric.
    """
    return [
        "free", "winner", "cash", "prize", "click", "urgent",
        "limited time", "act now", "offer", "risk-free",
        "guarantee", "money back", "cheap", "discount",
        "save", "deal", "bonus", "congratulations",
        "exclusive", "trial", "credit", "debt", "loan",
        "viagra", "investment", "bitcoin", "crypto",
        "miracle", "weight loss", "work from home"
    ]

def analyze_message(message, keywords):
    """
    Scan the message for each keyword/phrase.
    For every occurrence add 1 point to the spam score.
    Returns a tuple: (score, likelihood_text, hits_report)
    where hits_report is a printable multi‑line string listing
    each word/phrase found and how many times it appeared.
    """
    text = message.lower()
    score = 0

    # two parallel lists to avoid using dictionaries
    found_words = []
    found_counts = []

    i = 0
    while i < len(keywords):
        word = keywords[i]
        count = text.count(word)
        if count > 0:
            score = score + count
            # track the word and its count
            found_words.append(word)
            found_counts.append(count)
        i = i + 1

    # Rate the likelihood by the thresholds
    if score == 0:
        likelihood = "Very unlikely spam"
    elif score <= 2:
        likelihood = "Unlikely spam"
    elif score <= 6:
        likelihood = "Possible spam"
    elif score <= 14:
        likelihood = "Likely spam"
    else:
        likelihood = "Very likely spam"

    # The printable report of hits
    if len(found_words) == 0:
        hits_report = "No spam words/phrases found."
    else:
        hits_report = "Matched words/phrases:\n"
        j = 0
        while j < len(found_words):
            hits_report = hits_report + f"  - {found_words[j]} : {found_counts[j]}\n"
            j = j + 1

    return score, likelihood, hits_report


if __name__ == "__main__":
    print("Simple Spam Scanner (Chapter 1–2 friendly)")
    print("- Enter/paste your email message below.")
    print("- Press Enter on an empty line to finish.\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    message = "\n".join(lines)

    # Build the list and analyze
    keywords = build_keywords()
    score, likelihood, hits_report = analyze_message(message, keywords)

    print("\n--- Results ---")
    print("Spam score:", score)
    print("Rating:", likelihood)
    print(hits_report)
    print("\nWords/phrases checked:", len(keywords))
