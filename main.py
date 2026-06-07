#!/usr/bin/env python3
"""
mouse_mover.py — Keeps your computer awake by nudging the mouse every few seconds.
Press Ctrl+C to stop.
"""

import pyautogui
import time
import math
import sys

# ── Settings ──────────────────────────────────────────────────────────────────
INTERVAL   = 15      # seconds between each nudge
RADIUS     = 20      # pixels to move away from the starting point
STEPS      = 30      # smoothness of the circular movement
DURATION   = 0.5     # seconds to complete each nudge
# ──────────────────────────────────────────────────────────────────────────────

pyautogui.FAILSAFE = True   # move mouse to top-left corner to abort instantly


def nudge(cx: int, cy: int, step: int) -> None:
    """Move the mouse in a small circle around (cx, cy)."""
    angle = 2 * math.pi * step / STEPS
    x = int(cx + RADIUS * math.cos(angle))
    y = int(cy + RADIUS * math.sin(angle))
    pyautogui.moveTo(x, y, duration=DURATION / STEPS)


def main() -> None:
    print("🖱️  Mouse Mover started.")
    print(f"   Nudging every {INTERVAL}s  |  radius {RADIUS}px  |  Ctrl+C to quit\n")

    step = 0
    try:
        while True:
            cx, cy = pyautogui.position()
            nudge(cx, cy, step)
            step = (step + 1) % STEPS

            # Return to original position
            pyautogui.moveTo(cx, cy, duration=DURATION / STEPS)

            remaining = INTERVAL
            while remaining > 0:
                sys.stdout.write(f"\r   Next nudge in {remaining:3d}s …")
                sys.stdout.flush()
                time.sleep(1)
                remaining -= 1

    except KeyboardInterrupt:
        print("\n\n✅  Mouse Mover stopped. Bye!")


if __name__ == "__main__":
    main()