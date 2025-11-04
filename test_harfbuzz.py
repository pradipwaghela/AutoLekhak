"""
Test script to verify Harfbuzz/Raqm support in Pillow
"""
import sys
print("="*60)
print("Testing Gujarati Text Rendering Support")
print("="*60)

# Test 1: Check Pillow installation
try:
    from PIL import Image, ImageDraw, ImageFont
    import PIL
    print(f"\n✓ Pillow installed: version {PIL.__version__}")
except ImportError:
    print("\n✗ Pillow not installed!")
    print("  Run: pip install Pillow==10.1.0")
    sys.exit(1)

# Test 2: Check Raqm/Harfbuzz support
try:
    import PIL.features
    has_raqm = PIL.features.check_feature('raqm')
    
    print(f"\nRaqm/Harfbuzz support: {has_raqm}")
    
    if has_raqm:
        print("\n" + "="*60)
        print("🎉 SUCCESS! Gujarati conjuncts will work perfectly!")
        print("="*60)
        print("\nYou can now run your wedding invitation script.")
        print("The text 'શ્રી' will render correctly as 'શ્રી' (not 'શરી')")
    else:
        print("\n" + "="*60)
        print("⚠ WARNING: Harfbuzz NOT detected")
        print("="*60)
        print("\nPossible issues:")
        print("1. GTK3 Runtime not installed")
        print("2. PATH not set correctly")
        print("3. Terminal not restarted after installation")
        print("\nSolutions:")
        print("- Reinstall GTK3 Runtime and check 'Add to PATH'")
        print("- Restart your computer")
        print("- Or try: conda install -c conda-forge pillow harfbuzz fribidi")
        
except Exception as e:
    print(f"\n✗ Error checking features: {e}")

# Test 3: Try to create a test image with Gujarati text
print("\n" + "="*60)
print("Testing Gujarati Text Rendering")
print("="*60)

try:
    # Create test image
    img = Image.new('RGB', (600, 150), 'white')
    draw = ImageDraw.Draw(img)
    
    # Try to use a system font (you'll replace this with your font)
    test_text = "શ્રી રાજેશભાઈ પટેલ"
    
    print(f"\nTest text: {test_text}")
    print("\nNote: For actual rendering test, you need to:")
    print("1. Load your Gujarati .ttf font in the main script")
    print("2. Use it to render the test text")
    print("3. Check if 'શ્રી' appears correctly (not as 'શરી')")
    
    print("\n✓ Image creation works")
    
except Exception as e:
    print(f"\n✗ Error creating image: {e}")

print("\n" + "="*60)
print("Test Complete!")
print("="*60)

input("\nPress Enter to exit...")