# Mancala

Mancala Game
UMBC - Fall 2023
Overview
This Python program implements the classic board game Mancala with a text-based interface. Players take turns selecting cups to move stones around the board, with the goal of collecting the most stones in their Mancala by the end of the game.
Game Description
Mancala is one of the oldest known board games, with variations played around the world. The game involves:

A board with 12 small cups (6 on each player's side)
Two larger cups (Mancalas) at the ends, one for each player
48 stones distributed evenly at the start (4 in each small cup)

Features

Two-player gameplay with customizable player names
ASCII-art game board display
Turn-based stone movement according to traditional Mancala rules
Extra turns when a player's last stone lands in their own Mancala
Game over detection and winner announcement

How to Play

Run the program: python mancala.py
Enter names for both players
On your turn, select a cup number from your side of the board
The stones in that cup will be distributed one by one counterclockwise
If the last stone lands in your Mancala, you get another turn
Game ends when all cups on one side are empty
The player with the most stones in their Mancala wins


Rules Implemented

Players must choose cups from their own side
If a player's last stone lands in their Mancala, they get another turn
Game ends when all cups on one side are empty
At the end, the player with the most stones in their Mancala wins


Technical Details

Written in Python 3
Uses ASCII art for the game board display
Implements board as nested lists for cup state tracking
No external dependencies required

Author

Timothy Rauck
Section: 52
E-mail: trauck1@umbc.edu
Date: November 3, 2023
