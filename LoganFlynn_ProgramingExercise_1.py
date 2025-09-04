# Cinema Tickets
# Logan Flynn
# 08/31/25
MAX_TICKETS = 20
MAX_PER_BUYER = 4

def prompt_ticket_request(remaining: int) -> int | None:
    """
    Ask the user how many tickets they want.
    Returns an int in [1, min(MAX_PER_BUYER, remaining)] or None if user presses Enter to skip/quit.
    """
    limit = min(MAX_PER_BUYER, remaining)
    while True:
        raw = input(f"How many tickets would you like (1–{limit})? "
                    f"Press Enter to skip: ").strip()

        if raw == "":
            return None  # user chose to skip / quit early

        if not raw.isdigit():
            print("Please enter a whole number.")
            continue

        qty = int(raw)
        if qty < 1:
            print("Please enter a positive number.")
            continue
        if qty > MAX_PER_BUYER:
            print(f"You can buy at most {MAX_PER_BUYER} tickets per buyer.")
            continue
        if qty > remaining:
            print(f"Only {remaining} ticket(s) remain. Enter {remaining} or less.")
            continue

        return qty


def process_purchase(remaining: int, qty: int | None) -> tuple[int, bool]:
    """
    Process a purchase of qty tickets (or skip if qty is None).
    Returns (new_remaining, purchased_flag).
    """
    if qty is None:
        return remaining, False

    new_remaining = remaining - qty
    print(f"Purchase successful. You bought {qty} ticket(s). "
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
        qty = prompt_ticket_request(remaining)
        new_remaining, purchased = process_purchase(remaining, qty)

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
