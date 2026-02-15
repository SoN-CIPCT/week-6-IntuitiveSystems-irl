# Week 6 Assignment: Conditional Lists and Nested Dictionaries

# ============ CONDITIONAL LISTS ============

# Create a list of existing web users
web_users = ["admin_lindsay", "jsmith99", "techguru", "cloud_walker", "pixel_queen"]

# Create a list of new users trying to register
# Two names match web_users ("jsmith99" and "techguru"), three are unique
new_users = ["jsmith99", "night_owl", "techguru", "data_ninja", "star_gazer"]

# Check if each new user name is already taken
for user in new_users:
    if user.lower() in [existing.lower() for existing in web_users]:
        print(f"{user}: This user name is already in use. Please choose a different user name.")
    else:
        print(f"{user}: This user name is available.")


# ============ NESTED DICTIONARIES ============

# Create a dictionary of cities, each with country, population, and a fact
cities = {
    "Tokyo": {
        "country": "Japan",
        "population": 14000000,
        "fact": "Tokyo is the most populous metropolitan area in the world.",
    },
    "Paris": {
        "country": "France",
        "population": 2200000,
        "fact": "Paris is home to the Louvre, the world's largest art museum.",
    },
    "Nairobi": {
        "country": "Kenya",
        "population": 4400000,
        "fact": "Nairobi is the only capital city in the world with a national park.",
    },
}

# Print the information for each city
for city, info in cities.items():
    print(f"\nCity: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
