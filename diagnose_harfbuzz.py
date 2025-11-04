"""
Comprehensive diagnostic for Harfbuzz/Raqm support
"""
import os
import sys
from pathlib import Path

print("="*70)
print("HARFBUZZ DIAGNOSTIC TOOL")
print("="*70)

# Check 1: Python and Pillow info
print("\n1. PYTHON & PILLOW INFO")
print("-" * 70)
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")

try:
    import PIL
    from PIL import Image, ImageFont
    print(f"Pillow version: {PIL.__version__}")
    print(f"Pillow location: {PIL.__file__}")
except ImportError as e:
    print(f"ERROR: Pillow not installed - {e}")
    sys.exit(1)

# Check 2: Raqm support
print("\n2. RAQM/HARFBUZZ SUPPORT CHECK")
print("-" * 70)
try:
    import PIL.features
    has_raqm = PIL.features.check_feature('raqm')
    print(f"Raqm support: {has_raqm}")
    
    # Check all features
    print("\nAll Pillow features:")
    features = ['webp', 'webp_mux', 'webp_anim', 'jpg', 'jpg_2000', 
                'zlib', 'libtiff', 'raqm', 'libimagequant', 'xcb']
    for feature in features:
        try:
            status = PIL.features.check_feature(feature)
            print(f"  {feature}: {status}")
        except:
            print(f"  {feature}: Unknown")
            
except Exception as e:
    print(f"ERROR checking features: {e}")

# Check 3: System PATH
print("\n3. SYSTEM PATH CHECK")
print("-" * 70)
path_dirs = os.environ.get('PATH', '').split(';')
gtk_found = False
harfbuzz_found = False

print("Searching for GTK3 and Harfbuzz in PATH:")
for path_dir in path_dirs:
    path_lower = path_dir.lower()
    if 'gtk' in path_lower:
        print(f"  ✓ GTK found: {path_dir}")
        gtk_found = True
        
        # Check if harfbuzz DLL exists
        hb_path = Path(path_dir) / "libharfbuzz-0.dll"
        if hb_path.exists():
            print(f"    ✓ libharfbuzz-0.dll found!")
            harfbuzz_found = True

if not gtk_found:
    print("  ✗ No GTK directory found in PATH")

# Check 4: Look for GTK3 installation
print("\n4. GTK3 INSTALLATION CHECK")
print("-" * 70)
possible_gtk_paths = [
    r"C:\Program Files\GTK3-Runtime Win64\bin",
    r"C:\GTK3-Runtime Win64\bin",
    r"C:\msys64\mingw64\bin",
    r"C:\gtk\bin",
]

print("Checking common GTK3 installation locations:")
for gtk_path in possible_gtk_paths:
    if os.path.exists(gtk_path):
        print(f"  ✓ Found: {gtk_path}")
        
        # Check for harfbuzz
        hb_dll = os.path.join(gtk_path, "libharfbuzz-0.dll")
        if os.path.exists(hb_dll):
            print(f"    ✓ libharfbuzz-0.dll exists!")
            print(f"\n    ** ADD THIS TO YOUR PATH: {gtk_path}")
        else:
            print(f"    ✗ libharfbuzz-0.dll NOT found")
    else:
        print(f"  ✗ Not found: {gtk_path}")

# Check 5: Pillow build info
print("\n5. PILLOW BUILD INFORMATION")
print("-" * 70)
try:
    import PIL
    print("Pillow modules:")
    if hasattr(PIL, '_util'):
        print(f"  Pillow was built with: {dir(PIL)}")
except:
    pass

# Check 6: Try loading ImageFont with layout engine
print("\n6. IMAGEFONT LAYOUT ENGINE TEST")
print("-" * 70)
try:
    from PIL import ImageFont
    
    # Check if RAQM layout engine is available
    if hasattr(ImageFont, 'Layout'):
        print("  ✓ ImageFont.Layout class exists")
        if hasattr(ImageFont.Layout, 'RAQM'):
            print("  ✓ ImageFont.Layout.RAQM exists")
        else:
            print("  ✗ ImageFont.Layout.RAQM NOT available")
    else:
        print("  ✗ ImageFont.Layout class NOT available")
        
except Exception as e:
    print(f"  ERROR: {e}")

# Summary and Recommendations
print("\n" + "="*70)
print("DIAGNOSIS SUMMARY")
print("="*70)

if has_raqm:
    print("\n✅ HARFBUZZ IS WORKING!")
    print("   Your Gujarati text should render correctly.")
else:
    print("\n❌ HARFBUZZ IS NOT WORKING")
    print("\nRECOMMENDED ACTIONS:")
    print("\n1. Install GTK3 Runtime:")
    print("   https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases")
    
    if gtk_found and harfbuzz_found:
        print("\n2. ✓ GTK3 seems installed but not detected by Pillow")
        print("   Try: pip uninstall Pillow && pip install Pillow==10.1.0")
        print("   Then RESTART your computer")
    elif gtk_found and not harfbuzz_found:
        print("\n2. ✗ GTK3 found but libharfbuzz-0.dll is missing")
        print("   Reinstall GTK3 Runtime")
    else:
        print("\n2. ✗ GTK3 not found in PATH")
        print("   After installing GTK3, add to PATH:")
        print("   C:\\Program Files\\GTK3-Runtime Win64\\bin")
    
    print("\n3. After installation:")
    print("   - RESTART your computer (not just terminal)")
    print("   - Reactivate your venv")
    print("   - Run this diagnostic again")
    
    print("\n4. Alternative: Use the workaround script")
    print("   (I can provide a version that doesn't need Harfbuzz)")

print("\n" + "="*70)
input("\nPress Enter to exit...")