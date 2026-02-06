#!/usr/bin/env python3
"""
Generate Q1.1 plots for INVX4 Input Slew Sweep
"""

import matplotlib.pyplot as plt
import numpy as np

# Set up professional plot style
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

# ============================================================================
# Q1.1 Data: Input Slew Sweep (Load = 15fF)
# ============================================================================
input_slew = np.array([50, 100, 150, 200, 250])  # ps

# Delays
rise_delay = np.array([38.12, 51.78, 65.47, 77.14, 88.02])  # ps
fall_delay = np.array([32.68, 45.13, 57.16, 66.53, 74.94])  # ps

# Transitions
rise_tr = np.array([34.97, 38.48, 42.15, 49.84, 55.39])  # ps
fall_tr = np.array([27.54, 31.76, 37.14, 43.01, 49.40])  # ps

# ============================================================================
# Plot 1a: Input Slew vs Delays
# ============================================================================
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# Plot rise delay on primary axis (blue)
line1 = ax1.plot(input_slew, rise_delay, 'b-o', linewidth=2, 
                 markersize=8, label='Rise Delay')
ax1.set_xlabel('Input Slew (ps)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Rise Delay (ps)', color='b', fontsize=12, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='b')
ax1.grid(True, alpha=0.3)

# Plot fall delay on secondary axis (red)
line2 = ax2.plot(input_slew, fall_delay, 'r-s', linewidth=2, 
                 markersize=8, label='Fall Delay')
ax2.set_ylabel('Fall Delay (ps)', color='r', fontsize=12, fontweight='bold')
ax2.tick_params(axis='y', labelcolor='r')

# Title and legend
plt.title('Q1.1a: Inverter Delay vs Input Slew\n(Load=15fF, T=-40°C, VDD=0.65V)', 
          fontsize=13, fontweight='bold')
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=11)

plt.tight_layout()
plt.savefig('Q1.1a_delay_vs_slew.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Q1.1a_delay_vs_slew.png")
plt.close()

# ============================================================================
# Plot 1b: Input Slew vs Transition Times
# ============================================================================
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# Plot rise transition on primary axis (blue)
line1 = ax1.plot(input_slew, rise_tr, 'b-o', linewidth=2, 
                 markersize=8, label='Rise Transition')
ax1.set_xlabel('Input Slew (ps)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Rise Transition (ps)', color='b', fontsize=12, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='b')
ax1.grid(True, alpha=0.3)

# Plot fall transition on secondary axis (red)
line2 = ax2.plot(input_slew, fall_tr, 'r-s', linewidth=2, 
                 markersize=8, label='Fall Transition')
ax2.set_ylabel('Fall Transition (ps)', color='r', fontsize=12, fontweight='bold')
ax2.tick_params(axis='y', labelcolor='r')

# Title and legend
plt.title('Q1.1b: Inverter Transition Time vs Input Slew\n(Load=15fF, T=-40°C, VDD=0.65V)', 
          fontsize=13, fontweight='bold')
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=11)

plt.tight_layout()
plt.savefig('Q1.1b_transition_vs_slew.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Q1.1b_transition_vs_slew.png")
plt.close()

print("\n" + "="*60)
print("Q1.1 Plots Generated Successfully!")
print("="*60)
print("\nGenerated files:")
print("  1. Q1.1a_delay_vs_slew.png")
print("  2. Q1.1b_transition_vs_slew.png")
print("\nThese plots are ready for submission!")
print("="*60)
