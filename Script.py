def name_number(name):
    total = 0
    for ch in name.upper():
        if ch.isalpha():
            total += ord(ch) - 64

    while total > 9:
        total = sum(int(d) for d in str(total))

    return total


def astrology_bio(name):
    number = name_number(name)

    profiles = {
        1: "A born leader with strong confidence and independence.",
        2: "A calm peacemaker who values relationships and harmony.",
        3: "Creative, expressive, and naturally charming.",
        4: "Hardworking, practical, and highly disciplined.",
        5: "Adventurous, energetic, and loves freedom.",
        6: "Caring, responsible, and family-oriented.",
        7: "Deep thinker, spiritual, and analytical.",
        8: "Ambitious, powerful, and success-driven.",
        9: "Compassionate, wise, and humanitarian."
    }

    bio = profiles.get(number, "Unique and mysterious personality.")

    return f"""
Astrology Biography Report
-------------------------
Name: {name}
Destiny Number: {number}

Personality:
{bio}

Strengths:
- Determined
- Intelligent
- Adaptable

Career Style:
Prefers meaningful work and steady growth.

Life Theme:
Learning, growth, and self-discovery.
"""


# ---- MAIN ----
name = input().strip()   # ✅ CHANGED LINE
print(astrology_bio(name))
