#!/usr/bin/env python3
"""
Generate Q1.2 plots for INVX4 Output Load Sweep
"""

import matplotlib.pyplot as plt
import numpy as np

# Set up professional plot style
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

# ============================================================================
# Q1.2 Data: Output Load Sweep (Slew = 150ps)
# ============================================================================
output_load = np.array([5, 10, 15, 20, 25])  # fF

# Delays
rise_delay = np.array([35.01, 47.44, 57.16, 64.05, 70.91])  # ps
fall_delay = np.array([42.27, 55.43, 65.47, 73.70, 80.97])  # ps

# Transitions
rise_tr = np.array([26.46, 34.98, 42.15, 51.01, 61.35])  # ps
fall_tr = np.array([23.00, 30.53, 37.14, 44.10, 50.26])  # ps

# ============================================================================
# Plot 2a: Output Load vs Delays
# ============================================================================
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# Plot rise delay on primary axis (blue)
line1 = ax1.plot(output_load, rise_delay, 'b-o', linewidth=2, 
                 markersize=8, label='Rise Delay')
ax1.set_xlabel('Output Load (fF)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Rise Delay (ps)', color='b', fontsize=12, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='b')
ax1.grid(True, alpha=0.3)

# Plot fall delay on secondary axis (red)
line2 = ax2.plot(output_load, fall_delay, 'r-s', linewidth=2, 
                 markersize=8, label='Fall Delay')
ax2.set_ylabel('Fall Delay (ps)', color='r', fontsize=12, fontweight='bold')
ax2.tick_params(axis='y', labelcolor='r')

# Title and legend
plt.title('Q1.2a: Inverter Delay vs Output Load\n(Slew=150ps, T=-40°C, VDD=0.65V)', 
          fontsize=13, fontweight='bold')
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=11)

plt.tight_layout()
plt.savefig('Q1.2a_delay_vs_load.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Q1.2a_delay_vs_load.png")
plt.close()

# ============================================================================
# Plot 2b: Output Load vs Transition Times
# ============================================================================
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# Plot rise transition on primary axis (blue)
line1 = ax1.plot(output_load, rise_tr, 'b-o', linewidth=2, 
                 markersize=8, label='Rise Transition')
ax1.set_xlabel('Output Load (fF)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Rise Transition (ps)', color='b', fontsize=12, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='b')
ax1.grid(True, alpha=0.3)

# Plot fall transition on secondary axis (red)
line2 = ax2.plot(output_load, fall_tr, 'r-s', linewidth=2, 
                 markersize=8, label='Fall Transition')
ax2.set_ylabel('Fall Transition (ps)', color='r', fontsize=12, fontweight='bold')
ax2.tick_params(axis='y', labelcolor='r')

# Title and legend
plt.title('Q1.2b: Inverter Transition Time vs Output Load\n(Slew=150ps, T=-40°C, VDD=0.65V)', 
          fontsize=13, fontweight='bold')
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=11)

plt.tight_layout()
plt.savefig('Q1.2b_transition_vs_load.png', dpi=300, bbox_inches='tight')
print("✓ Saved: Q1.2b_transition_vs_load.png")
plt.close()

print("\n" + "="*60)
print("Q1.2 Plots Generated Successfully!")
print("="*60)
print("\nGenerated files:")
print("  1. Q1.2a_delay_vs_load.png")
print("  2. Q1.2b_transition_vs_load.png")
print("\nThese plots are ready for submission!")
print("="*60)
