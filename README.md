# WAR_GAME_SIM

## Introduction

The **War Card Game** is a Python implementation of the classic card game "War". In this game, two players are pitted against each other in a battle of cards. The objective is to win all the cards in the deck through successive rounds of comparisons.

This program demonstrates fundamental concepts in object-oriented programming, including classes, methods, and encapsulation, while providing a fun and interactive gameplay experience.

## How the Game Works

### Game Setup

1. **Deck Initialization**: A standard deck of 52 cards is created. Each card has:
   - A suit (Hearts, Diamonds, Spades, Clubs).
   - A rank (e.g., Two, Three, ... King, Ace).
   - A value associated with its rank (e.g., Two = 2, Ace = 14).
2. **Shuffle and Deal**: The deck is shuffled, and each player is dealt 26 cards.

### Game Flow

1. **Round Start**:

   - Players each draw one card from the top of their deck.
   - The cards are compared based on their values.

2. **Comparison Outcomes**:

   - **Player One's card > Player Two's card**: Player One takes both cards and adds them to their deck.
   - **Player One's card < Player Two's card**: Player Two takes both cards and adds them to their deck.
   - **Player One's card == Player Two's card**: A **WAR** occurs.

3. **WAR Condition**:

   - Each player places 5 additional cards face down.
   - Then, they reveal the next card.
   - The revealed cards are compared:
     - If one player's revealed card has a higher value, they win all the cards played in that WAR.
     - If the revealed cards are again of equal value, the WAR continues with another set of 5 cards (if possible).
   - If a player cannot place enough cards for a WAR, they lose the game.

4. **Game End**:
   - The game continues until one player runs out of cards, and the other player is declared the winner.

---

## Classes and Methods

### **Card Class**

Represents an individual playing card.

- **Attributes**:
  - `suit`: The suit of the card (e.g., Hearts).
  - `rank`: The rank of the card (e.g., Ace).
  - `value`: The numerical value of the card (e.g., 14 for Ace).
- **Methods**:
  - `__str__`: Returns a human-readable representation of the card (e.g., "Ace of Hearts").

### **Deck Class**

Represents the entire deck of cards.

- **Attributes**:
  - `all_cards`: A list containing all 52 card objects.
- **Methods**:
  - `shuffle_deck`: Shuffles the deck.
  - `deal_one`: Removes and returns one card from the deck.

### **Player Class**

Represents a player in the game.

- **Attributes**:
  - `name`: The name of the player.
  - `all_cards`: A list of the player's current cards.
- **Methods**:
  - `remove_one`: Removes the top card from the player's deck.
  - `add_cards`: Adds one or more cards to the player's deck.
  - `__str__`: Returns the player's name and the number of cards they have.

---

## How to Play

1. **Run the Script**: Execute the Python script to start the game.
2. **Gameplay**:
   - The game automatically handles card drawing, comparisons, and resolving WAR scenarios.
   - Each round's results and WAR conditions are displayed in the console.
3. **Winning**:
   - A player wins when their opponent runs out of cards.

---

## Example Gameplay Output

```
Round : 1
Round : 2
-----------WAR!!!!-------------------
Player Two cant play war :<
Player One Wins
```

This output indicates that after a series of rounds, a WAR occurred, and Player Two did not have enough cards to continue, resulting in Player One's victory.
