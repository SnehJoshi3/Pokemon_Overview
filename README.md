# Pokémon Data Analysis & Interactive Dashboard

An exploratory data analysis and Power BI visualization project built out of curiosity to explore Pokémon distributions across generations, types, type/ability combinations, hidden abilities, categories, and Mega Evolutions.

---

## Project Overview

* **Dataset Scope:** Covers 9 generations, 18 types, 144 type combinations, 541 single-type entries, 48 Mega Evolutions, and 163 hidden abilities
* **Tools Used:** Python (Pandas) and Microsoft Power BI
* **Deliverables:** Cleaned dataset (`pokemon_data.csv`), Python data prep script, and an interactive Power BI dashboard

---

## Data Preparation & Feature Engineering

Starting from `pokemon.csv`, a focused subset of columns (`Name`, `Generation`, `Weight`, `Height`, `Type1`, `Type2`, `Ability1`, `Ability2`, `Ability_Hidden`, `Category`, `Mega_Evolution_Flag`, `Total`) was prepared in Python:

1. **Order-Independent Type Combinations:** Combined `Type1` and `Type2`, deduplicated, and sorted components (`sorted(set(...))`) so dual-type pairings are treated consistently regardless of ordering (`Type_Combo`), paired with `Type_count` to track single vs. dual typing.
2. **Ability Combinations & Counts:** Built `Ability_Combo` by deduplicating and sorting available abilities per entry alongside `Ability_count`.
3. **Flag & Missing-Value Standardization:** Normalized `Mega_Evolution_Flag` (`Mega` → `Yes`, filling blanks with `"No"`) and filled missing `Ability_Hidden` entries with `"No"`.
4. **Export:** Saved the processed dataset to `pokemon_data.csv` without an extra index column.

---

## Questions Answered Through Analysis & Dashboard

* **Which is the most common type combination?** **Normal & Flying** (`Flying,Normal`) with 31 entries, ahead of **Grass & Poison** (15) and **Bug & Flying** (14)
* **Which generation has the most Pokémon?** **5th Generation** with 169 entries, followed closely by **1st Generation** (167) and **3rd Generation** (163)
* **Which is the most common individual type?** **Water** (151), followed by **Normal** (136) and **Grass** (106)
* **How many Pokémon have only one type?** **541** single-type entries (44.97%), compared to dual-type entries making up 55.03%
* **How many Mega Evolutions are there?** **48** Mega entries across the dataset
* **How many unique hidden abilities are there?** **163** unique hidden abilities, led by **Telepathy** (24), **Sheer Force** (22), and **Regenerator** (20)
---
