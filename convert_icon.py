"""
Convert DnD_icon.jpg to DnD_icon.ico for use with PyInstaller
"""

try:
    from PIL import Image
    
    # Open the JPG file
    img = Image.open('DnD_icon.jpg')
    
    # Convert to ICO with multiple sizes for better quality
    # Windows typically uses 16x16, 32x32, 48x48, and 256x256
    img.save('DnD_icon.ico', format='ICO', sizes=[(16,16), (32,32), (48,48), (256,256)])
    
    print("✓ Successfully converted DnD_icon.jpg to DnD_icon.ico")
    print("  Icon includes sizes: 16x16, 32x32, 48x48, 256x256")
    
except ImportError:
    print("✗ Pillow (PIL) not installed. Installing...")
    import subprocess
    subprocess.run(['python', '-m', 'pip', 'install', 'pillow'], check=True)
    print("✓ Pillow installed. Please run this script again.")
    
except FileNotFoundError:
    print("✗ Error: DnD_icon.png not found in current directory")
    
except Exception as e:
    print(f"✗ Error converting icon: {e}")
