# ![Gethenian](/static/icons/Chennis.svg) Gethenian Chess

![Starting position](/static/images/CVariantsGuide/Gethenian_starting_position.png)

> *When the Ekuman first came to Gethen they brought with them the ancient Terran game of Chess. As has happened in all time and places, the peoples of Karhide and Orgoreyn adapted it for themselves. The nature of Gethenian Chess is thus reflected in the old Handdaran lay that begins "Light is the left hand of darkness and darkness the right hand of light."*

**Gethenian Chess** is a variant set in the fictional world of Ursula K. Le Guin's science-fiction novel "The Left Hand of Darkness." As in [**Kyoto Shogi**](/variants/kyotoshogi) and [**Chennis**](/variants/chennis), pieces alternately promote or demote between two sides when moved. Rather than pieces alternating between short- and long-range movements, however, pieces in Gethenian Chess alternate between similar range movements but with left- and right-handed themes. These are termed "light" and "dark," respectively, and are represented visually in the default piece theme for the first player (cyan) and the second player (magenta), shown below.

![Piece combinations](/static/images/CVariantsGuide/Gethenian_piece_combinations.png)

Similar to Shogi, captured pieces may be returned or "dropped" back onto the board on any unoccupied square, potentially delivering checkmate in the process. The King's mobility is also limited by flipping between capturing and non-capturing sides (i.e., passive movement only), making checks especially strong.

## Goals of the game

There are three ways to win:

* **Checkmate**: Put your opponent's King in check with no legal moves to avoid capture.
* **Stalemate**: Leave your opponent with no legal moves (unlike in Chess where stalemate is a draw).
* **Resignation**: Your opponent resigns.

Additionally, the game is **drawn** if no captures have been made in 50 moves or if pieces are moved with three-fold repitition.

## Pieces

![King movement](/static/images/CVariantsGuide/Gethenian_king_movement.png)

The *Light King* moves and captures one square in each direction (shown above with green circles). When it moves, it promotes to the *Dark King*, which can only move without capturing (i.e., passively) forward, backward, left, and right (shown above with yellow circles). When the Dark King moves, it demotes back to the Light King. Because the Dark King cannot capture, a Light King can deliver check or mate, and two Dark Kings may also be adjacent to each other.

![Minister movement](/static/images/CVariantsGuide/Gethenian_minister_movement.png)

The *Light* and *Dark Minister's* move and capture the same way as the Gold and Silver Generals in Shogi.

![Bishop and Rook movements](/static/images/CVariantsGuide/Gethenian_bishop_rook_movement.png)

The *Bishop-Rook* come in a *Left* and *Right* pair. The *Left Bishop* can move and capture along the top-left-to-bottom-right diagonal and promotes to a Rook limited to horizontal movement. Similarly, the *Right Bishop* can move and capture along the top-right-to-bottom-left diagonal. Both Rooks move in the same way, and inset arrows are added to the default piece theme to indicate which Bishop they demote to.

Light Knight | Dark Knight
--- | ---
![Light Knight movement](/static/images/CVariantsGuide/Gethenian_knight_light_movement.png) | ![Dark Knight movement](/static/images/CVariantsGuide/Gethenian_knight_dark_movement.png)

The *Light Knight* moves and captures on the left-handed spaces of a standard Knight movement (shown in the above left image). It promotes to the *Dark Knight*, which moves and captures on the right-handed spaces (above right).

## Piece values

Approximate piece values are 2.0 for the Minister, Left-Bishop, and Right-Bishop, 1.0 for the Knight, and 0.4 for the current move (i.e., the initiative). The piece values were determined by logistic regression using the [chess-variant-stats](https://github.com/ianfab/chess-variant-stats) code repository. Keep in mind that for drop variants such as Gethenian position and tempo are generally more important than material advantage.

## Strategy

Similar to Shogi and other drop variants, the initiative and King mobility are paramount. Note also that due to the limited number of pieces per side, hung pieces can be forked relatively easily by dropped pieces and strong, mutually defended formations take care to organize. Simple beginner guidelines are thus (1) always check the available flight squares for the King, and (2) avoid leaving pieces undefended if possible.
