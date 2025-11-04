# AutoLekhak – Intelligent PDF Text Writer (with Gujarati Support)

A Python GUI application to automatically add **custom text to PDFs** — perfect for invitations, certificates, greeting cards, and any document personalization task.  
Designed with **perfect Gujarati text rendering** (including conjuncts like શ્રી, ક્ષ, જ્ઞ) and intuitive GUI controls.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20Mac-lightgrey.svg)

## ✨ Features

- 🎨 **Visual GUI** - Easy-to-use graphical interface
- 📝 **Perfect Gujarati Rendering** - Supports complex conjuncts like શ્રી, ક્ષ, જ્ઞ
- 🖼️ **PDF Preview** - See your invitation while marking positions
- 📍 **Multiple Positions** - Add names at multiple locations across pages
- 🎯 **Click-to-Position** - Simply click where you want names to appear
- 🧪 **Test Before Generate** - Preview with sample name before batch processing
- 🎨 **Customizable** - Adjust font size, color, and rendering quality
- ⚡ **Batch Processing** - Generate hundreds of personalized invitations automatically
- 🔍 **Zoom Controls** - Precise positioning with zoom in/out

## 📸 Screenshots

```
┌─────────────────────────────────────────────────────────┐
│  Controls               │  PDF Preview                  │
│  ─────────              │  ─────────────                │
│  □ Load Font            │                               │
│  □ Load PDF             │    [Your Invitation PDF]      │
│  □ Add Positions        │         ↓ Click here          │
│  □ Load Guest CSV       │       📝 (Red Marker)         │
│  □ Generate All         │                               │
└─────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Windows / Linux / macOS

### Installation

#### 1. Install GTK3 Runtime (Required for Gujarati Text Rendering)

**Windows:**

1. Download GTK3 Runtime from: [GTK3-Runtime-Win64-Installer](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases)
2. Install to any location (e.g., `C:\Program Files\GTK3-Runtime Win64` or `D:\software\GTK3-Runtime Win64`)
3. **Important:** Add the `bin` folder to your system PATH:
   - Open Environment Variables (Win+X → System → Advanced → Environment Variables)
   - Edit "Path" under System variables
   - Add new entry: `[Your GTK3 Install Path]\bin`
   - Example: `D:\software\GTK3-Runtime Win64\bin`
4. **Restart your computer** (required for PATH changes)

**Linux:**
```bash
sudo apt-get update
sudo apt-get install libraqm0 libharfbuzz-dev libfribidi-dev
```

**Mac:**
```bash
brew install harfbuzz fribidi
```

#### 1. Clone the Repository

```bash
git clone https://github.com/pradipwaghela/AutoLekhak.git
cd wedding-invitation-automation
```

#### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv wedding_env
wedding_env\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv wedding_env
source wedding_env/bin/activate
```

#### 3. Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**requirements.txt:**
```
PyMuPDF==1.23.8
Pillow==10.1.0
```

#### 4. Verify Installation

```bash
python test_harfbuzz.py
```

You should see: **"🎉 SUCCESS! Gujarati conjuncts will work perfectly!"**

If not, see [Troubleshooting](#troubleshooting) section.

#### 5. Download Gujarati Font

Download one of these fonts:

- **Noto Sans Gujarati** (Recommended): [Google Fonts](https://fonts.google.com/noto/specimen/Noto+Sans+Gujarati)
- **Hind Vadodara**: [Google Fonts](https://fonts.google.com/specimen/Hind+Vadodara)

**Recommendation:** Use the **Bold** variant (e.g., `NotoSansGujarati-Bold.ttf`) for better visibility and conjunct rendering.

Place the `.ttf` file in your project folder for easy access.

---

## 📖 Usage Guide

### Step 1: Prepare Your Files

#### A. Wedding Invitation PDF
- Your multi-page invitation card PDF
- Can be created from photos or any PDF editor

#### B. Guest Names CSV File

Create a CSV file with guest names in Gujarati:

**guests.csv:**
```csv
name
શ્રી રાજેશભાઈ પટેલ
શ્રીમતી સીતાબેન શાહ
શ્રી મહેશભાઈ દેસાઈ
શ્રીમતી લીલાબેન વ્યાસ
શ્રી અશોકભાઈ ત્રિવેદી
```

**Important:** Save with UTF-8 encoding!

#### C. Gujarati Font File
- Download `.ttf` file (see step 6 above)
- Keep it handy for loading in the GUI

---

### Step 2: Run the Application

```bash
# Activate virtual environment
wedding_env\Scripts\activate  # Windows
source wedding_env/bin/activate  # Linux/Mac

# Run the script
python kk_naming.py
```

---

### Step 3: Using the GUI

#### **STEP 0: Load Gujarati Font** 🔤
1. Click **"🔤 Select Gujarati Font (.ttf)"**
2. Browse and select your Gujarati font file (e.g., `NotoSansGujarati-Bold.ttf`)
3. Status should show: "✓ Loaded: [font-name]" in green

#### **STEP 1: Load PDF Template** 📄
1. Click **"📄 Select PDF Template"**
2. Choose your wedding invitation PDF
3. PDF preview will appear on the right side
4. Status should show: "Loaded: [filename]" in green

#### **STEP 2: Navigate & Add Positions** 📍
1. Use **"◀ Prev" / "Next ▶"** buttons to navigate between pages
2. **Adjust font settings:**
   - **Font Size:** 20-40 (recommended: 24-28)
   - **Text Color:** Choose from Black, Red, Blue, Gold, Green, Maroon
   - **Rendering:** Select "Better Quality" for sharper text
3. **Click on the PDF** where you want the guest name to appear
4. A **red marker 📝** will appear at that position
5. The position will be added to the "Added Positions" list
6. Repeat for second/third position (can be on different pages)
7. **Tips:**
   - Use **🔍+ / 🔍−** to zoom for precise positioning
   - To remove a position: Select from list → Click "❌ Remove Selected Position"

#### **STEP 3: Load Guest CSV** 📋
1. Click **"📋 Load Guest CSV File"**
2. Select your `guests.csv` file
3. Status should show: "Loaded: guests.csv (X guests)" in green

#### **STEP 4: Test with Sample Name** 🧪 *(Important!)*
1. Click **"🧪 Test with Sample Name"**
2. Enter a test name (default: "શ્રી રાજેશભાઈ પટેલ")
3. Click "Generate Test PDF"
4. Choose where to save the test file
5. **Open and verify:**
   - ✓ Does "શ્રી" appear correctly? (Not "શરી")
   - ✓ Is the position correct?
   - ✓ Is the size appropriate?
   - ✓ Is the color visible?
6. If not perfect: Adjust settings and test again

#### **STEP 5: Generate All Invitations** 🎉
1. Once test looks perfect, click **"🎉 GENERATE ALL INVITATIONS 🎉"**
2. Confirm you've tested and are ready to proceed
3. Choose output directory for saving invitations
4. Wait for progress bar to complete
5. Done! All personalized invitations are saved as:
   - `invitation_શ્રી રાજેશભાઈ પટેલ.pdf`
   - `invitation_શ્રીમતી સીતાબેન શાહ.pdf`
   - etc.

---

## ⚙️ Configuration Options

### Font Settings
- **Size:** 8-120 pixels (recommended: 24-28 for invitations)
- **Color Options:**
  - Black (traditional)
  - Red (auspicious)
  - Blue
  - Gold (elegant)
  - Green
  - Maroon (wedding theme)

### Rendering Quality
- **Normal:** Faster, good quality (2x resolution)
- **Better Quality:** Slower, excellent quality (3x resolution) - *Recommended for final output*

---

## 🗂️ Project Structure

```
wedding-invitation-automation/
│
├── kk_naming.py              # Main application script
├── test_harfbuzz.py          # Harfbuzz installation tester
├── diagnose_harfbuzz.py      # Diagnostic tool (optional)
├── requirements.txt          # Python dependencies
├── README.md                 # This file
│
├── guests.csv                # Your guest list (create this)
├── invitation_template.pdf   # Your invitation PDF (your file)
├── NotoSansGujarati-Bold.ttf # Gujarati font (download)
│
├── wedding_env/              # Virtual environment (created during setup)
└── output/                   # Generated invitations (created automatically)
```

---

## 🐛 Troubleshooting

### Issue 1: "Raqm/Harfbuzz support: False"

**Solution:**
```bash
# 1. Verify GTK3 bin folder is in PATH
echo %PATH%  # Windows
echo $PATH   # Linux/Mac

# 2. Check if libharfbuzz-0.dll exists (Windows)
dir "D:\software\GTK3-Runtime Win64\bin\libharfbuzz-0.dll"

# 3. Reinstall Pillow
pip uninstall Pillow
pip install Pillow==10.1.0

# 4. Restart computer
# 5. Test again
python test_harfbuzz.py
```

### Issue 2: "શ્રી" still shows as "શરી"

**Causes:**
- Harfbuzz not properly installed
- Font doesn't support conjuncts well

**Solutions:**
1. Run diagnostic: `python diagnose_harfbuzz.py`
2. Try different font (Lohit Gujarati or Noto Sans Gujarati Bold)
3. Ensure "Better Quality" rendering is selected
4. Restart computer after installing GTK3

### Issue 3: Names Not Visible in PDF

**Solutions:**
- Increase font size (try 40+)
- Change text color (if background is dark)
- Check position by testing with sample name
- Verify font file is loaded correctly

### Issue 4: "No module named 'fitz'"

**Solution:**
```bash
pip install PyMuPDF==1.23.8
```

### Issue 5: GUI Buttons Not Visible

**Solution:**
- Maximize the window
- Scroll down in the left control panel
- The script has a scrollable interface

### Issue 6: CSV Error "No 'name' column"

**Solution:**
- Ensure CSV has header row: `name`
- Save CSV with UTF-8 encoding
- Example format:
  ```csv
  name
  શ્રી રાજેશભાઈ પટેલ
  ```

---

## 💡 Tips & Best Practices

1. **Always test with sample name first** before generating all invitations
2. **Use Bold fonts** (e.g., NotoSansGujarati-Bold.ttf) for better visibility
3. **Zoom in** (🔍+) before clicking positions for accuracy
4. **Start with 2-3 test guests** before processing entire list
5. **Keep backup** of your original PDF template
6. **Font size 24-28** works well for most invitation cards
7. **Select "Better Quality"** rendering for final generation
8. **Traditional colors:** Maroon or Black for Gujarati weddings
9. **Test different pages** if your invitation is multi-page
10. **Save your positions** - the app remembers them until you close it

---

## 🎨 Recommended Settings

**For Traditional Wedding Invitations:**
```
Font: NotoSansGujarati-Bold.ttf
Size: 26
Color: Maroon or Black
Rendering: Better Quality
```

**For Modern/Colorful Invitations:**
```
Font: NotoSansGujarati-Bold.ttf
Size: 28
Color: Gold or Blue
Rendering: Better Quality
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### To Contribute:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **PyMuPDF (fitz)** - PDF manipulation
- **Pillow (PIL)** - Image processing and text rendering
- **Harfbuzz** - Text shaping engine for complex scripts
- **GTK3 Runtime** - Providing Harfbuzz libraries for Windows
- **Google Fonts** - Noto Sans Gujarati font
- **Lohit Project** - Lohit Gujarati font

---

## 📧 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Run diagnostic: `python diagnose_harfbuzz.py`
3. Open an issue on GitHub with:
   - Your Python version: `python --version`
   - Output of: `python test_harfbuzz.py`
   - Screenshot of error (if applicable)

---

## 🌟 Star This Repository

If this project helped you create beautiful wedding invitations, please ⭐ star this repository!

---

## 📚 Additional Resources

- [Gujarati Unicode Guide](https://en.wikipedia.org/wiki/Gujarati_script)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [PyMuPDF Documentation](https://pymupdf.readthedocs.io/)
- [Harfbuzz Text Shaping](https://harfbuzz.github.io/)

---

**Made with ❤️ for the Gujarati Community**

*Happy Wedding Planning! 🎊 લગ્ન મુબારક!*