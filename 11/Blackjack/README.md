# 🃏 Blackjack

A terminal-based Blackjack game written in Python. Play against the dealer with a standard 52-card deck (×4), complete with natural Blackjack detection, Ace handling, and dealer Computer.

---

## Features

- **Full 4-deck shoe** shuffled at the start of each session
- **Natural Blackjack detection** on the opening deal
- **Automatic Ace conversion** (11 → 1) to prevent unnecessary busts
- **Dealer Logic** that hits until reaching 17 or above (standard casino rules)
- **Play again** loop — keep playing until you choose to quit

---

## Requirements

- Python 3.x

## Usage

```bash
python blackjack.py
```

Follow the prompts to play. Enter `Y` to draw a card or play again, and `N` to stand or exit.

---

## Game Rules

| Situation | Outcome |
|---|---|
| Player or Dealer hits 21 on opening deal | Natural Blackjack |
| Both hit 21 on opening deal | Draw |
| Player exceeds 21 | Bust — Dealer wins |
| Dealer exceeds 21 | Dealer busts — Player wins |
| Neither busts | Higher hand wins |
| Equal hands | Push (tie) |

- **Aces** count as 11, but automatically convert to 1 if the hand would otherwise bust.
- The **dealer always hits on 16 or below** and stands on 17 or above.

---

## Project Structure

```
blackjack.py   # Main game logic
art.py         # Logo file
```

---

## License

MIT
