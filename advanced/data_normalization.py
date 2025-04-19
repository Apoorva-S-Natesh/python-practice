import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import pandas as pd

def normalize_nucleotide_matrix(raw_values=None):
    """
    Normalize nucleotide position frequency matrix values to range 0-1.
    
    Parameters:
    raw_values : If provided, use these values rather than the example from the image
    
    Returns:
    DataFrame with normalized values
    """
    # Define nucleotides and positions from the image
    nucleotides = ['A', 'C', 'G', 'T']
    positions = ['NN', 'NG', 'NI', 'NS', 'HD', 'Other']
    
    # If raw values aren't provided, use estimated values from the image
    if raw_values is None:
        # Estimate values based on circle sizes (0 = no circle, 10 = largest)
        # These are rough estimates based on visual inspection of the image
        raw_values = [
            # A row (green circles)
            [2, 3.7, 3, 1, 1.4, 3.2],
            # C row (blue circles)
            [4.3, 6.2, 5.7, 0, 3.7, 1],
            # G row (no visible circles)
            [0, 0, 0, 0, 0, 0],
            # T row (red circles)
            [9.5, 9, 9.3, 4.8, 9.2, 7.2]
        ]
    
    # Convert to numpy array for easier manipulation
    values = np.array(raw_values)
    
    # Normalize to 0-1 range (divide by maximum value)
    max_value = np.max(values)
    if max_value > 0:  # Avoid division by zero
        normalized = values / max_value
    else:
        normalized = values
    
    # Create DataFrame for easier reading
    df = pd.DataFrame(normalized, index=nucleotides, columns=positions)
    
    return df

# Generate normalized values
normalized_matrix = normalize_nucleotide_matrix()

# Display the normalized values
print("Normalized values (0-1 range):")
print(normalized_matrix)

# Optionally, visualize the normalized matrix
def visualize_matrix(matrix):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    nucleotides = matrix.index
    positions = matrix.columns
    
    for i, nuc in enumerate(nucleotides):
        for j, pos in enumerate(positions):
            value = matrix.loc[nuc, pos]
            if value > 0:
                circle = Circle((j, -i), radius=value/2, 
                              color={'A': 'green', 'C': 'blue', 'G': 'gray', 'T': 'red'}[nuc],
                              alpha=0.7)
                ax.add_patch(circle)
            
            # Add text label with value
            ax.text(j, -i, f"{value:.2f}", ha='center', va='center', fontsize=8)
    
    ax.set_xlim(-1, len(positions))
    ax.set_ylim(-len(nucleotides), 1)
    ax.set_xticks(range(len(positions)))
    ax.set_xticklabels(positions)
    ax.set_yticks(range(-len(nucleotides) + 1, 1))
    ax.set_yticklabels(nucleotides)
    ax.set_title("Normalized Nucleotide Matrix")
    ax.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()

# Uncomment to visualize
# visualize_matrix(normalized_matrix)