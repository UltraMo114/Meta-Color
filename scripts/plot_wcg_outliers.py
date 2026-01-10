
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def plot_wcg_outliers():
    input_path = Path("results/classic_audit_sucs/full_audit_data.csv")
    output_path = Path("results/classic_audit_sucs/wcg_outliers_sucs_plane_proxy.png")
    
    if not input_path.exists():
        print(f"Error: {input_path} not found.")
        return

    df = pd.read_csv(input_path)
    
    # Filter for WCG dataset
    wcg_df = df[df['DatasetID'] == 'WCG'].copy()
    
    if wcg_df.empty:
        print("Error: No data found for DatasetID 'WCG'")
        return

    # Check for Outlier column
    if 'Is_Outlier' not in wcg_df.columns:
        print("Error: 'Is_Outlier' column not found.")
        return

    # Ensure boolean
    # If read as string, convert
    if wcg_df['Is_Outlier'].dtype == object:
        wcg_df['Is_Outlier'] = wcg_df['Is_Outlier'].replace({'True': True, 'False': False})
    
    wcg_df['Is_Outlier'] = wcg_df['Is_Outlier'].astype(bool)

    outliers = wcg_df[wcg_df['Is_Outlier']]
    normal = wcg_df[~wcg_df['Is_Outlier']]
    
    print(f"WCG Total: {len(wcg_df)}")
    print(f"Outliers: {len(outliers)}")
    print(f"Normal: {len(normal)}")

    # Plotting
    # Using Ref_a and Ref_b as proxies for color space coordinates
    # Note: These are likely CIELAB a* b*, not sUCS a b, but we use them to visualize position.
    
    plt.figure(figsize=(10, 10))
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # Plot normal points
    plt.scatter(normal['Ref_a'], normal['Ref_b'], 
                c='gray', marker='o', alpha=0.6, label='Normal', edgecolors='none')
    
    # Plot outliers
    plt.scatter(outliers['Ref_a'], outliers['Ref_b'], 
                c='red', marker='^', s=60, label='Outliers', edgecolors='k', linewidth=0.5)
    
    plt.xlabel('$a^*$ (Reference)')
    plt.ylabel('$b^*$ (Reference)')
    plt.title('WCG Dataset Outliers in Color Space (CIELAB proxy)')
    plt.axis('equal') # Ensure standard Euclidean space aspect ratio
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    print(f"Plot saved to {output_path}")

if __name__ == "__main__":
    plot_wcg_outliers()
