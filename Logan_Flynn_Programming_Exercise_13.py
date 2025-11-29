# Logan Flynn
# Population growth and decline simulator
# 11/29/2025

import sqlite3
import random
import matplotlib.pyplot as plt

# Name of the database file
DB_NAME = "population_LF.db"


def create_database():
    """
    Create the database and population table.
    Insert population data for 10 Florida cities for the year 2023.
    """
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Create the table if it doesn't already exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER,
            PRIMARY KEY (city, year)
        )
    """)

    # 10 Florida cities with made-up 2023 population values
    base_pop_2023 = {
        "Miami": 462000,
        "Orlando": 316000,
        "Tampa": 403000,
        "Jacksonville": 971000,
        "Tallahassee": 203000,
        "St. Petersburg": 258000,
        "Fort Lauderdale": 183000,
        "Gainesville": 145000,
        "Sarasota": 56200,
        "Pensacola": 55000
    }

    # Clear any old data so we can re-run the program without duplicates
    cur.execute("DELETE FROM population")

    # Insert 2023 data into the table
    for city, pop in base_pop_2023.items():
        cur.execute("""
            INSERT INTO population (city, year, population)
            VALUES (?, ?, ?)
        """, (city, 2023, pop))

    conn.commit()
    conn.close()
    print("Database created and 2023 data inserted.")


def simulate_population_growth(years=20, min_rate=-0.02, max_rate=0.04):
    """
    Simulate population changes for the next `years` years.
    Each year, each city changes by a random rate between min_rate and max_rate.
    The new values are inserted into the table.
    """
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Get all cities and their 2023 populations
    cur.execute("SELECT city, year, population FROM population WHERE year = 2023")
    rows = cur.fetchall()

    # Seed the random number generator so results are repeatable
    random.seed(0)

    # For each city, simulate population for the next `years` years
    for city, start_year, population in rows:
        current_pop = population

        for offset in range(1, years + 1):
            year = start_year + offset

            # Pick a random growth rate between min_rate and max_rate
            growth_rate = random.uniform(min_rate, max_rate)

            # Update the population based on the growth rate
            current_pop = int(current_pop * (1 + growth_rate))

            # Store the new year and population in the table
            cur.execute("""
                INSERT OR REPLACE INTO population (city, year, population)
                VALUES (?, ?, ?)
            """, (city, year, current_pop))

    conn.commit()
    conn.close()
    print(f"Simulated {years} years of population data and saved to database.")


def plot_city_population():
    """
    Ask the user to choose a city and show its population
    over time in a line graph using matplotlib.
    """
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Get a list of all cities in the table
    cur.execute("SELECT DISTINCT city FROM population ORDER BY city")
    cities = [row[0] for row in cur.fetchall()]

    # If there are no cities, we can't plot anything
    if not cities:
        print("No cities found. Run create_database() and simulate_population_growth() first.")
        conn.close()
        return

    # Show city options to the user
    print("Available cities:")
    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city}")

    # Let the user choose by number or by name
    choice = input("Choose a city by number or type its name: ").strip()

    if choice.isdigit():
        idx = int(choice)
        if 1 <= idx <= len(cities):
            city_choice = cities[idx - 1]
        else:
            print("Invalid number.")
            conn.close()
            return
    else:
        # Match the city name ignoring case
        matches = [c for c in cities if c.lower() == choice.lower()]
        if not matches:
            print("City not found.")
            conn.close()
            return
        city_choice = matches[0]

    # Get all years and populations for the chosen city
    cur.execute("""
        SELECT year, population
        FROM population
        WHERE city = ?
        ORDER BY year
    """, (city_choice,))
    data = cur.fetchall()
    conn.close()

    # If there is no data for that city, stop
    if not data:
        print("No data found for that city.")
        return

    years = [row[0] for row in data]
    pops = [row[1] for row in data]

    # Plot the data using matplotlib
    plt.figure()
    plt.plot(years, pops, marker="o")
    plt.title(f"Population of {city_choice} (2023–{years[-1]})")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Run everything in order:
    # Create DB and insert 2023 data
    # Simulate 20 years of growth/decline
    # Plot the population for a city the user chooses
    create_database()
    simulate_population_growth(years=20)
    plot_city_population()

