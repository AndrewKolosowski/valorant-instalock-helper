This repository provides a small utility for Valorant that rapidly moves the mouse cursor between the lock and confirm buttons. It does not perform automatic mouse clicks or fully lock onto targets on its own. This is intentional, as Valorant’s kernel-level anti-cheat detects and blocks mouse clicks that are not generated directly by the player. As a result, you must manually click the mouse at the correct moment while the script is running to confirm a target. The behavior is implemented in main.py.

1. **Create a virtual environment**
   ```sh
   python -m venv venv
   ```

2. **Activate the virtual environment**
   ```sh
   # On Windows:
   venv\Scripts\activate

   # On macOS / Linux:
   source venv/bin/activate
   ```

3. **Install the requirements:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Install pyinstaller**
   ```sh
   pip install pyinstaller
   ```

5. **Convert to exe**
   ```sh
   pyinstaller --onefile main.py
   ```

6. **Run the exe**