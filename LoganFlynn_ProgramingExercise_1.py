# Cinema Tickets
# Logan Flynn
# 08/31/25
MAX_TICKETS = 10
MAX_PER_BUYER = 4

def prompt_ticket_request(remaining: int) -> int | None:
    """
    Ask the user how many tickets they want.
    Returns an int in [1, min(MAX_PER_BUYER, remaining)] or None if user presses Enter to skip/quit.
    """
    limit = min(MAX_PER_BUYER, remaining)
    while True:
        raw = input(f"Enter the amount of tickets you want to purchase (1–{limit})? "
                    f"Press Enter to skip: ").strip()

        if raw == "":
            return None  # user chose to skip / quit early

        if not raw.isdigit():
            print("Please enter a whole number.")
            continue

        tickets_bought = int(raw)
        if tickets_bought < 1:
            print("Please enter a positive number.")
            continue
        if tickets_bought > MAX_PER_BUYER:
            print(f"You can buy at most {MAX_PER_BUYER} tickets per buyer.")
            continue
        if tickets_bought > remaining:
            print(f"Only {remaining} ticket(s) remain. Enter {remaining} or less.")
            continue

        return tickets_bought


def process_purchase(remaining: int, tickets_bought: int | None) -> tuple[int, bool]:
    """
    Process a purchase of tickets_bought tickets (or skip if tickets_bought is None).
    Returns (new_remaining, purchased_flag).
    """
    if tickets_bought is None:
        return remaining, False

    new_remaining = remaining - tickets_bought
    print(f"Purchase successful. You bought {tickets_bought} ticket(s). "
          f"{new_remaining} ticket(s) remain.\n")
    return new_remaining, True


def main() -> None:
    print("=== Cinema Ticket Presale ===")
    print(f"Up to {MAX_TICKETS} tickets total; each buyer may purchase up to "
          f"{MAX_PER_BUYER}.\n")

    remaining = MAX_TICKETS
    total_buyers = 0

    # Keep offering until sold out or user skips twice in a row if they want
    while remaining > 0:
        tickets_bought = prompt_ticket_request(remaining)
        new_remaining, purchased = process_purchase(remaining, tickets_bought)

        if purchased:
            total_buyers += 1
            remaining = new_remaining
        else:
            # User skipped; you can break here if you want to end early:
            print("No purchase made. Offer to the next buyer or press Enter again to skip.\n")

    print("=== SOLD OUT ===" if remaining == 0 else "=== PRESALE ENDED ===")
    print(f"Total buyers: {total_buyers}")


if __name__ == "__main__":
    main()
