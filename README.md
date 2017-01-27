#Mosaic For Lego Digital Designer

![Mosaic for Lego Digital Designer](banner.png?raw=true "Mosaic for Lego Digital Designer")

##What is Mosaic?
Mosaic converts images to LEGO mosaics that can be opened with LEGO Digital Designer.

###How does it work?
  1. The image is processed pixel by pixel
  2. Colors are reduced to the LEGO color palette
  3. Each pixel becomes a 1x1 brick
  4. Bricks are written to .lxf file

###How to run mosaic
  1. Download the program files
  2. Download Python 3.5 for your operating system
  3. Install Tkinter and Pillow packages with PIP
  4. Run main.py with Python 3.5

###How to use mosaic
  1. Run main.py with Python 3.5
  2. Select a .jpg or .png image
  3. Select a destination to save your .lxf mosaic
  4. Open .lxf with LEGO Digital Designer 4.3

![Starry Night](screenshots/starrynight.png?raw=true "Starry Night")
Starry Night created from 48x48px jpg image - 2304 bricks, ~15x15in when built

![Mona Lisa](screenshots/mona.png?raw=true "Mona Lisa")
Mona Lisa created from 48x96px jpg image - 4608 bricks, ~15x30in when built

![Sunday on La Grande Jatte](screenshots/park.png?raw=true "Sunday on La Grande Jatte")
Mona Lisa created from 150×100px jpg image - 15000 bricks, ~48x32in when built

###You call that a GUI?
  I'm working on it, calm yourself. I'm working on a launcher folks can drag-and-drop image files onto.

### Author
* **Joe Samela** - *Initial work* - [ForYourBrain.net](https://www.ForYourBrain.net)
